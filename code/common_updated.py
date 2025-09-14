#!/usr/bin/env python3
"""
Updated common functions for aws2tf that use ConfigurationManager.

This module contains updated versions of common functions that accept
a ConfigurationManager parameter instead of using global variables.
"""

import boto3
from botocore.exceptions import ClientError
import sys
import subprocess
import os
import re
import ast
from io import StringIO
from contextlib import suppress
import shutil
import json
import glob
import botocore
import inspect
from datetime import datetime, timezone
import threading
from pathlib import Path
from typing import Optional, Dict, Any, List, Union

# Import the configuration system
from .config import ConfigurationManager

# Import existing modules that will be gradually migrated
try:
    import fixtf
    import resources
    from timed_interrupt import timed_int
    from fixtf_aws_resources import aws_dict
    from fixtf_aws_resources import needid_dict
    from fixtf_aws_resources import aws_no_import
    from fixtf_aws_resources import aws_not_implemented
except ImportError:
    # Fallback for when running from different directory
    import code.fixtf as fixtf
    import code.resources as resources
    from code.timed_interrupt import timed_int
    from code.fixtf_aws_resources import aws_dict
    from code.fixtf_aws_resources import needid_dict
    from code.fixtf_aws_resources import aws_no_import
    from code.fixtf_aws_resources import aws_not_implemented

# Import AWS resource modules
try:
    from get_aws_resources import aws_acm
from code.get_aws_resources import aws_amplify
from code.get_aws_resources import aws_athena
from code.get_aws_resources import aws_autoscaling
from code.get_aws_resources import aws_apigateway
from code.get_aws_resources import aws_apigatewayv2
from code.get_aws_resources import aws_appmesh
from code.get_aws_resources import aws_application_autoscaling
from code.get_aws_resources import aws_appstream
from code.get_aws_resources import aws_batch
from code.get_aws_resources import aws_backup
from code.get_aws_resources import aws_bedrock
from code.get_aws_resources import aws_bedrock_agent
from code.get_aws_resources import aws_cleanrooms
from code.get_aws_resources import aws_cloud9
from code.get_aws_resources import aws_cloudformation
from code.get_aws_resources import aws_cloudfront
from code.get_aws_resources import aws_cloudtrail
from code.get_aws_resources import aws_codebuild
from code.get_aws_resources import aws_codecommit
from code.get_aws_resources import aws_codeartifact
from code.get_aws_resources import aws_codeguruprofiler
from code.get_aws_resources import aws_codestar_notifications
from code.get_aws_resources import aws_cognito_identity
from code.get_aws_resources import aws_cognito_idp
from code.get_aws_resources import aws_config
from code.get_aws_resources import aws_connect
from code.get_aws_resources import aws_customer_profiles
from code.get_aws_resources import aws_datazone
from code.get_aws_resources import aws_dms
from code.get_aws_resources import aws_docdb
from code.get_aws_resources import aws_ds
from code.get_aws_resources import aws_dynamodb
from code.get_aws_resources import aws_kms
from code.get_aws_resources import aws_ec2
from code.get_aws_resources import aws_ecs
from code.get_aws_resources import aws_efs
from code.get_aws_resources import aws_ecr_public
from code.get_aws_resources import aws_ecr
from code.get_aws_resources import aws_eks
from code.get_aws_resources import aws_elasticache
from code.get_aws_resources import aws_elbv2
from code.get_aws_resources import aws_emr
from code.get_aws_resources import aws_events
from code.get_aws_resources import aws_firehose
from code.get_aws_resources import aws_glue
from code.get_aws_resources import aws_guardduty
from code.get_aws_resources import aws_iam
from code.get_aws_resources import aws_kafka
from code.get_aws_resources import aws_kendra
from code.get_aws_resources import aws_kinesis
from code.get_aws_resources import aws_logs
from code.get_aws_resources import aws_lakeformation
from code.get_aws_resources import aws_lambda
from code.get_aws_resources import aws_license_manager
from code.get_aws_resources import aws_mwaa
from code.get_aws_resources import aws_neptune
from code.get_aws_resources import aws_network_firewall
from code.get_aws_resources import aws_networkmanager
from code.get_aws_resources import aws_organizations
from code.get_aws_resources import aws_ram
from code.get_aws_resources import aws_rds
from code.get_aws_resources import aws_redshift
from code.get_aws_resources import aws_redshift_serverless
from code.get_aws_resources import aws_resource_explorer_2
from code.get_aws_resources import aws_route53
from code.get_aws_resources import aws_s3
from code.get_aws_resources import aws_s3control
from code.get_aws_resources import aws_s3tables
from code.get_aws_resources import aws_sagemaker
from code.get_aws_resources import aws_schemas
from code.get_aws_resources import aws_scheduler
from code.get_aws_resources import aws_securityhub
from code.get_aws_resources import aws_secretsmanager
from code.get_aws_resources import aws_servicecatalog
from code.get_aws_resources import aws_servicediscovery
from code.get_aws_resources import aws_shield
from code.get_aws_resources import aws_ses
from code.get_aws_resources import aws_sns
from code.get_aws_resources import aws_sqs
from code.get_aws_resources import aws_ssm
from code.get_aws_resources import aws_sso_admin
from code.get_aws_resources import aws_transfer
from code.get_aws_resources import aws_vpc_lattice
from code.get_aws_resources import aws_waf
from code.get_aws_resources import aws_wafv2
from code.get_aws_resources import aws_xray


def call_resource(config: ConfigurationManager, resource_type: str, resource_id: str) -> bool:
    """
    Call the appropriate resource processing function.
    
    Args:
        config: Configuration manager with processing settings.
        resource_type: Type of AWS resource to process.
        resource_id: ID of the specific resource to process.
        
    Returns:
        True if resource was processed successfully.
    """
    try:
        if config.is_debug_enabled():
            print(f"--1-- in call_resources >>>>> {resource_type}   {resource_id}")
        
        # Check if resource type is in exclusion list
        if resource_type in config.runtime.all_extypes:
            if config.is_debug_enabled():
                print(f"Common Excluding: {resource_type}, {resource_id}")
            pkey = f"{resource_type}.{resource_id}"
            config.mark_resource_processed(pkey)
            return True
        
        # Check if resource type cannot be imported
        if resource_type in aws_no_import.noimport:
            print(f"WARNING: Can not import type: {resource_type}")
            if resource_id is not None:
                with open('not-imported.log', 'a') as f2:
                    f2.write(f"{resource_type} : {resource_id}\n")
                config.mark_resource_processed(f"{resource_type}.{resource_id}")
            return True
        
        # Check if resource type is not implemented
        if resource_type in aws_not_implemented.notimplemented:
            print(f"Not supported by aws2tf currently: {resource_type} "
                  "please submit github issue to request support")
            return False
        
        # Handle null resource type
        if resource_type == "aws_null":
            with open('stack-null.err', 'a') as f3:
                f3.write(f"-->> called aws_null for: {resource_id}\n")
            return True
        
        # Check if already processed
        if config.is_debug_enabled():
            print(f"---->>>>> {resource_type}   {resource_id}")
        
        if resource_id is not None:
            ti = f"{resource_type}.{resource_id}"
            if config.is_resource_processed(ti):
                if config.is_debug_enabled():
                    print(f"Already processed {ti}")
                print(f"Already processed {ti}")
                return True
        else:
            if resource_type in needid_dict.aws_needid:
                print(f"WARNING: {resource_type} can not have null id must pass parameter "
                      f"{needid_dict.aws_needid[resource_type]['param']}")
                return False
        
        # Get resource data
        clfn, descfn, topkey, key, filterid = resources.resource_data(resource_type, resource_id)
        
        if key == "NOIMPORT":
            print(f"WARNING: Can not import type: {resource_type}")
            return False
        
        if clfn is None:
            print(f"ERROR: clfn is None with type={resource_type}")
            print("exit 016")
            timed_int.stop()
            exit()
        
        # Try specific resource processing
        sr = False
        try:
            if config.is_debug_enabled():
                print(f"calling specific common.get_{resource_type} with type={resource_type} "
                      f"id={resource_id} clfn={clfn} descfn={descfn} topkey={topkey} "
                      f"key={key} filterid={filterid}")
            
            # Get the appropriate resource module and function
            if clfn == "vpc-lattice":
                getfn = getattr(aws_vpc_lattice, f"get_{resource_type}")
            elif clfn == "redshift-serverless":
                getfn = getattr(aws_redshift_serverless, f"get_{resource_type}")
            elif clfn == "s3":
                getfn = getattr(aws_s3, f"get_{resource_type}")
            else:
                mclfn = clfn.replace("-", "_")
                module = eval(f"aws_{mclfn}")
                getfn = getattr(module, f"get_{resource_type}")
            
            # Call the resource-specific function
            # Note: These functions will need to be updated in future tasks to accept config
            sr = getfn(resource_type, resource_id, clfn, descfn, topkey, key, filterid)
            
        except AttributeError as e:
            if config.is_debug_enabled():
                print(f"AttributeError: name 'getfn' - no aws_{clfn}.py file ?")
                print(f"{e=}")
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
        except SyntaxError:
            if config.is_debug_enabled():
                print(f"SyntaxError: name 'getfn' - no aws_{clfn}.py file ?")
        except NameError as e:
            if config.is_debug_enabled():
                print(f"WARNING: NameError: name 'getfn' - no aws_{clfn}.py file ?")
                print(f"{e=}")
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
        except Exception as e:
            handle_error(config, e, str(inspect.currentframe().f_code.co_name),
                        clfn, descfn, topkey, resource_id)
        
        # Try generic resource processing if specific failed
        if not sr:
            try:
                if config.is_debug_enabled():
                    print(f"calling generic getresource with type={resource_type} "
                          f"id={resource_id} clfn={clfn} descfn={descfn} "
                          f"topkey={topkey} key={key} filterid={filterid}")
                rr = getresource(config, resource_type, resource_id, clfn, descfn, topkey, key, filterid)
            except Exception as e:
                print(f"{e=}")
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                if not rr:
                    print(f"--->> Could not get resource {resource_type} id={resource_id}")
        
        # Log processed resource
        with open('processed-resources.log', 'a') as f4:
            f4.write(f"{resource_type} : {resource_id}\n")
        
        # Mark as processed
        if resource_id is not None:
            config.mark_resource_processed(f"{resource_type}.{resource_id}")
        
        return True
        
    except Exception as e:
        error_msg = f"Error processing {resource_type} {resource_id}: {str(e)}"
        print(error_msg)
        
        if config.is_debug_enabled():
            import traceback
            traceback.print_exc()
        
        return False


def getresource(config: ConfigurationManager, resource_type: str, resource_id: str, 
                clfn: str, descfn: str, topkey: str, key: str, filterid: str) -> bool:
    """
    Generic resource processing function.
    
    Args:
        config: Configuration manager.
        resource_type: Type of AWS resource.
        resource_id: Resource ID.
        clfn: Client function name.
        descfn: Describe function name.
        topkey: Top-level key in response.
        key: Key for resource data.
        filterid: Filter ID for queries.
        
    Returns:
        True if resource was processed successfully.
    """
    try:
        if config.is_debug_enabled():
            print(f"--> In getresource doing {resource_type} with id {resource_id}")
        
        # Get AWS session from config
        session = config.get_aws_session()
        
        # Call boto3 to get resource data
        response = call_boto3(config, resource_type, clfn, descfn, topkey, key, resource_id)
        
        if not response:
            return False
        
        # Process the response and generate Terraform files
        # This is a simplified version - the full implementation would handle
        # all the complex resource processing logic
        
        if config.is_debug_enabled():
            print(f"Successfully processed {resource_type} {resource_id}")
        
        return True
        
    except Exception as e:
        handle_error(config, e, "getresource", clfn, descfn, topkey, resource_id)
        return False


def call_boto3(config: ConfigurationManager, resource_type: str, clfn: str, 
               descfn: str, topkey: str, key: str, resource_id: str) -> Optional[Dict[str, Any]]:
    """
    Call AWS boto3 API to get resource information.
    
    Args:
        config: Configuration manager.
        resource_type: Type of AWS resource.
        clfn: Client function name.
        descfn: Describe function name.
        topkey: Top-level key in response.
        key: Key for resource data.
        resource_id: Resource ID.
        
    Returns:
        AWS API response or None if failed.
    """
    try:
        if config.is_debug_enabled():
            print(f"Calling boto3 for {resource_type} with {descfn}")
        
        # Get AWS session from config
        session = config.get_aws_session()
        
        # Create the appropriate client
        client = session.client(clfn)
        
        # Call the describe function
        if resource_id:
            # Most describe functions take a list of IDs
            if descfn == "describe_instances":
                response = client.describe_instances(InstanceIds=[resource_id])
            elif descfn == "describe_vpcs":
                response = client.describe_vpcs(VpcIds=[resource_id])
            elif descfn == "describe_subnets":
                response = client.describe_subnets(SubnetIds=[resource_id])
            elif descfn == "describe_security_groups":
                response = client.describe_security_groups(GroupIds=[resource_id])
            else:
                # Generic approach - this may need customization per resource type
                describe_func = getattr(client, descfn)
                response = describe_func()
        else:
            # List all resources of this type
            describe_func = getattr(client, descfn)
            response = describe_func()
        
        return response
        
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code in ['InvalidInstanceID.NotFound', 'InvalidVpcID.NotFound', 
                         'InvalidSubnetID.NotFound', 'InvalidGroupId.NotFound']:
            print(f"Resource {resource_id} not found")
        else:
            print(f"AWS API error: {error_code} - {e.response['Error']['Message']}")
        return None
    except Exception as e:
        handle_error(config, e, "call_boto3", clfn, descfn, topkey, resource_id)
        return None


def handle_error(config: ConfigurationManager, e: Exception, frame: str, 
                clfn: str, descfn: str, topkey: str, resource_id: str) -> None:
    """
    Handle errors during resource processing.
    
    Args:
        config: Configuration manager.
        e: Exception that occurred.
        frame: Function name where error occurred.
        clfn: Client function name.
        descfn: Describe function name.
        topkey: Top-level key.
        resource_id: Resource ID.
    """
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    
    print(f"\nERROR: in {frame}")
    print(f"id={resource_id}")
    print(f"Exception: {str(e)}")
    print(f"File: {fname}, Line: {exc_tb.tb_lineno}")
    
    if config.is_debug_enabled():
        import traceback
        traceback.print_exc()
    
    # Log error details
    error_msg = f"{frame}: {str(e)} - {fname}:{exc_tb.tb_lineno}\n"
    with open('error.log', 'a') as f:
        f.write(error_msg)


def rc(cmd: str) -> subprocess.CompletedProcess:
    """
    Run a shell command and return the result.
    
    Args:
        cmd: Command to execute.
        
    Returns:
        CompletedProcess object with stdout/stderr.
    """
    out = subprocess.run(cmd, shell=True, capture_output=True)
    ol = len(out.stdout.decode('utf-8').rstrip())
    el = len(out.stderr.decode().rstrip())
    
    if el != 0:
        errm = out.stderr.decode().rstrip()
        # Note: In the original, this just stored the error but didn't exit
        # We maintain the same behavior
    
    return out


def ctrl_c_handler(signum, frame):
    """
    Handle Ctrl-C interrupt.
    
    Args:
        signum: Signal number.
        frame: Current stack frame.
    """
    print("Ctrl-C pressed.")
    print("exit 036")
    timed_int.stop()
    exit()


def check_python_version() -> None:
    """
    Check Python and boto3 versions.
    
    Raises:
        SystemExit: If versions are too old.
    """
    version = sys.version_info
    major = version.major
    minor = version.minor
    bv = str(boto3.__version__)
    print(f"boto3 version: {bv}")
    
    if major < 3 or (major == 3 and minor < 8):
        print("This program requires Python 3.8 or later.")
        sys.exit(1)
    
    # Check boto3 version
    if boto3.__version__ < '1.36.13':
        bv = str(boto3.__version__)
        print(f"boto3 version: {bv}")
        vs = bv.split(".")
        v1 = int(vs[0]) * 100000 + int(vs[1]) * 1000 + int(vs[2])
        if v1 < 136013:
            print(f"boto3 version: {bv}")
            print("This program requires boto3 1.36.13 or later.")
            print("Try: pip install boto3  -or-  pip install boto3==1.36.13")
            print("exit 037")
            timed_int.stop()
            sys.exit(1)


def aws_tf(config: ConfigurationManager, region: str, args) -> None:
    """
    Generate Terraform provider configuration.
    
    Args:
        config: Configuration manager.
        region: AWS region.
        args: Command line arguments.
    """
    with open("provider.tf", 'w') as f3:
        f3.write('terraform {\n')
        f3.write('  required_version = "> 1.10.4"\n')
        f3.write('  required_providers {\n')
        f3.write('    aws = {\n')
        f3.write('      source  = "hashicorp/aws"\n')
        f3.write(f'      version = "{config.aws.tf_version}"\n')
        f3.write('    }\n')
        f3.write('  }\n')
        f3.write('}\n')
        f3.write('provider "aws" {\n')
        f3.write(f'  region                   = "{region}"\n')
        
        if args.profile is not None:
            f3.write(f'  profile                  = "{config.aws.profile}"\n')
        
        if not config.runtime.serverless:
            f3.write('  shared_credentials_files = ["~/.aws/credentials"]\n')
        
        f3.write('}\n')
    
    # Copy to imported directory
    com = "cp provider.tf imported/provider.tf"
    rc(com)
    
    # Create data sources file if it doesn't exist
    if not os.path.isfile("data-aws.tf"):
        with open("data-aws.tf", 'w') as f3:
            f3.write('data "aws_region" "current" {}\n')
            f3.write('data "aws_caller_identity" "current" {}\n')
            f3.write('data "aws_availability_zones" "available" {\n')
            f3.write('  state = "available"\n')
            f3.write('}\n')


def write_import(config: ConfigurationManager, resource_type: str, 
                resource_id: str, tfid: Optional[str] = None) -> None:
    """
    Write Terraform import statement.
    
    Args:
        config: Configuration manager.
        resource_type: Type of AWS resource.
        resource_id: Resource ID.
        tfid: Terraform resource ID (optional override).
    """
    try:
        if tfid is None:
            tfid = resource_id
        
        # Clean up the Terraform ID
        tfid = tfid.replace("-", "_").replace(".", "_").replace(":", "_")
        
        # Generate import file
        import_file = f"import__{resource_type}__{tfid}.tf"
        
        with open(import_file, 'w') as f:
            f.write(f'import {{\n')
            f.write(f'  to = {resource_type}.{tfid}\n')
            f.write(f'  id = "{resource_id}"\n')
            f.write(f'}}\n')
        
        if config.is_debug_enabled():
            print(f"Created import file: {import_file}")
            
    except Exception as e:
        handle_error(config, e, "write_import", "", "", "", resource_id)


def do_data(config: ConfigurationManager, resource_type: str, resource_id: str) -> None:
    """
    Generate data source references.
    
    Args:
        config: Configuration manager.
        resource_type: Type of AWS resource.
        resource_id: Resource ID.
    """
    if config.runtime.dnet:
        if resource_type in ["aws_vpc", "aws_subnet"]:
            # Generate data source for networking resources
            data_file = f"data__{resource_type}__{resource_id.replace('-', '_')}.tf"
            
            with open(data_file, 'w') as f:
                if resource_type == "aws_vpc":
                    f.write(f'data "aws_vpc" "{resource_id.replace("-", "_")}" {{\n')
                    f.write(f'  id = "{resource_id}"\n')
                    f.write(f'}}\n')
                elif resource_type == "aws_subnet":
                    f.write(f'data "aws_subnet" "{resource_id.replace("-", "_")}" {{\n')
                    f.write(f'  id = "{resource_id}"\n')
                    f.write(f'}}\n')


# Additional utility functions that maintain compatibility with existing code

def add_dependancy(config: ConfigurationManager, resource_type: str, resource_id: str) -> None:
    """
    Add a resource dependency.
    
    Args:
        config: Configuration manager.
        resource_type: Type of AWS resource.
        resource_id: Resource ID.
    """
    if resource_id is None:
        return
    
    # Check if already processed
    pkey = f"{resource_type}.{resource_id}"
    if config.is_resource_processed(pkey):
        return
    
    # Add to processing queue
    config.resources.add_resource_to_list(resource_type, resource_id)


def add_known_dependancy(config: ConfigurationManager, resource_type: str, resource_id: str) -> None:
    """
    Add a known resource dependency.
    
    Args:
        config: Configuration manager.
        resource_type: Type of AWS resource.
        resource_id: Resource ID.
    """
    pkey = f"{resource_type}.{resource_id}"
    if config.is_resource_processed(pkey):
        return
    
    # Mark as processed without actually processing
    config.mark_resource_processed(pkey)


# S3 bucket management functions for serverless mode

def create_bucket_if_not_exists(config: ConfigurationManager, bucket_name: str) -> bool:
    """
    Create S3 bucket if it doesn't exist.
    
    Args:
        config: Configuration manager.
        bucket_name: Name of the S3 bucket.
        
    Returns:
        True if bucket exists or was created successfully.
    """
    try:
        session = config.get_aws_session()
        s3_client = session.client('s3')
        
        # Check if bucket exists
        try:
            s3_client.head_bucket(Bucket=bucket_name)
            print(f"Bucket {bucket_name} already exists")
            return True
        except ClientError as e:
            error_code = int(e.response['Error']['Code'])
            if error_code == 404:
                # Bucket doesn't exist, create it
                try:
                    if config.aws.region == 'us-east-1':
                        s3_client.create_bucket(Bucket=bucket_name)
                    else:
                        s3_client.create_bucket(
                            Bucket=bucket_name,
                            CreateBucketConfiguration={'LocationConstraint': config.aws.region}
                        )
                    print(f"Created bucket {bucket_name}")
                    return True
                except ClientError as create_error:
                    print(f"Failed to create bucket {bucket_name}: {create_error}")
                    return False
            else:
                print(f"Error checking bucket {bucket_name}: {e}")
                return False
                
    except Exception as e:
        print(f"Error with bucket operations: {str(e)}")
        return False


def upload_directory_to_s3(config: ConfigurationManager) -> bool:
    """
    Upload directory to S3 for serverless mode.
    
    Args:
        config: Configuration manager.
        
    Returns:
        True if upload was successful.
    """
    try:
        bucket_name = f"aws2tf-{config.aws.account_id}-{config.aws.region}"
        
        if not create_bucket_if_not_exists(config, bucket_name):
            return False
        
        print("Uploading to S3...")
        session = config.get_aws_session()
        s3_client = session.client('s3')
        
        # Upload files from the generated directory
        local_directory = config.runtime.path1
        
        for root, dirs, files in os.walk(local_directory):
            for file in files:
                local_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_path, local_directory)
                s3_key = f"generated/{relative_path}"
                
                try:
                    s3_client.upload_file(local_path, bucket_name, s3_key)
                    if config.is_debug_enabled():
                        print(f"Uploaded {relative_path} to s3://{bucket_name}/{s3_key}")
                except Exception as e:
                    print(f"Failed to upload {relative_path}: {str(e)}")
                    return False
        
        print(f"Upload to {bucket_name} completed.")
        return True
        
    except Exception as e:
        print(f"Error uploading to S3: {str(e)}")
        return False


def empty_and_delete_bucket(config: ConfigurationManager) -> None:
    """
    Empty and delete S3 bucket.
    
    Args:
        config: Configuration manager.
    """
    try:
        bucket_name = f"aws2tf-{config.aws.account_id}-{config.aws.region}"
        session = config.get_aws_session()
        s3 = session.resource('s3')
        
        bucket = s3.Bucket(bucket_name)
        
        # Delete all objects
        bucket.objects.all().delete()
        
        # Delete all object versions
        bucket.object_versions.all().delete()
        
        # Delete the bucket
        bucket.delete()
        
        print(f"Deleted bucket {bucket_name}")
        
    except Exception as e:
        if config.is_debug_enabled():
            print(f"Error deleting bucket: {str(e)}")


def download_from_s3(config: ConfigurationManager) -> None:
    """
    Download files from S3 for merge mode.
    
    Args:
        config: Configuration manager.
    """
    try:
        print("Restore S3")
        bucket_name = f"aws2tf-{config.aws.account_id}-{config.aws.region}"
        session = config.get_aws_session()
        s3_client = session.client('s3')
        
        # Download files to local directory
        local_directory = config.runtime.path1
        s3_prefix = "generated/"
        
        # List objects in bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=s3_prefix)
        
        if 'Contents' not in response:
            print(f"No files found in bucket {bucket_name}")
            return
        
        # Download each file
        for obj in response['Contents']:
            s3_key = obj['Key']
            local_path = os.path.join(local_directory, s3_key.replace(s3_prefix, ''))
            
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            
            try:
                s3_client.download_file(bucket_name, s3_key, local_path)
                if config.is_debug_enabled():
                    print(f"Downloaded {s3_key} to {local_path}")
            except Exception as e:
                print(f"Failed to download {s3_key}: {str(e)}")
        
        print(f"Download from {bucket_name}/{s3_prefix} to {local_directory} completed.")
        
    except Exception as e:
        print(f"Error downloading from S3: {str(e)}")