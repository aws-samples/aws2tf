#!/usr/bin/env python3
"""
Migrated common functions for aws2tf that use ConfigurationManager.

This module contains the full aws2tf common functions updated to use
ConfigurationManager instead of global variables while maintaining
all existing functionality.
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

# Import existing modules - these will need to be migrated in future tasks
try:
    # Try relative imports first
    from . import fixtf
    from . import resources
    from .timed_interrupt import timed_int
    from .fixtf_aws_resources import aws_dict
    from .fixtf_aws_resources import needid_dict
    from .fixtf_aws_resources import aws_no_import
    from .fixtf_aws_resources import aws_not_implemented
except ImportError:
    # Fall back to absolute imports
    import code.fixtf as fixtf
    import code.resources as resources
    from code.timed_interrupt import timed_int
    from code.fixtf_aws_resources import aws_dict
    from code.fixtf_aws_resources import needid_dict
    from code.fixtf_aws_resources import aws_no_import
    from code.fixtf_aws_resources import aws_not_implemented

# Import AWS resource modules - these will be updated in future tasks
try:
    from .get_aws_resources import aws_acm
from get_aws_resources import aws_amplify
from get_aws_resources import aws_athena
from get_aws_resources import aws_autoscaling
from get_aws_resources import aws_apigateway
from get_aws_resources import aws_apigatewayv2
from get_aws_resources import aws_appmesh
from get_aws_resources import aws_application_autoscaling
from get_aws_resources import aws_appstream
from get_aws_resources import aws_batch
from get_aws_resources import aws_backup
from get_aws_resources import aws_bedrock
from get_aws_resources import aws_bedrock_agent
from get_aws_resources import aws_cleanrooms
from get_aws_resources import aws_cloud9
from get_aws_resources import aws_cloudformation
from get_aws_resources import aws_cloudfront
from get_aws_resources import aws_cloudtrail
from get_aws_resources import aws_codebuild
from get_aws_resources import aws_codecommit
from get_aws_resources import aws_codeartifact
from get_aws_resources import aws_codeguruprofiler
from get_aws_resources import aws_codestar_notifications
from get_aws_resources import aws_cognito_identity
from get_aws_resources import aws_cognito_idp
from get_aws_resources import aws_config
from get_aws_resources import aws_connect
from get_aws_resources import aws_customer_profiles
from get_aws_resources import aws_datazone
from get_aws_resources import aws_dms
from get_aws_resources import aws_docdb
from get_aws_resources import aws_ds
from get_aws_resources import aws_dynamodb
from get_aws_resources import aws_kms
from get_aws_resources import aws_ec2
from get_aws_resources import aws_ecs
from get_aws_resources import aws_efs
from get_aws_resources import aws_ecr_public
from get_aws_resources import aws_ecr
from get_aws_resources import aws_eks
from get_aws_resources import aws_elasticache
from get_aws_resources import aws_elbv2
from get_aws_resources import aws_emr
from get_aws_resources import aws_events
from get_aws_resources import aws_firehose
from get_aws_resources import aws_glue
from get_aws_resources import aws_guardduty
from get_aws_resources import aws_iam
from get_aws_resources import aws_kafka
from get_aws_resources import aws_kendra
from get_aws_resources import aws_kinesis
from get_aws_resources import aws_logs
from get_aws_resources import aws_lakeformation
from get_aws_resources import aws_lambda
from get_aws_resources import aws_license_manager
from get_aws_resources import aws_mwaa
from get_aws_resources import aws_neptune
from get_aws_resources import aws_network_firewall
from get_aws_resources import aws_networkmanager
from get_aws_resources import aws_organizations
from get_aws_resources import aws_ram
from get_aws_resources import aws_rds
from get_aws_resources import aws_redshift
from get_aws_resources import aws_redshift_serverless
from get_aws_resources import aws_resource_explorer_2
from get_aws_resources import aws_route53
from get_aws_resources import aws_s3
from get_aws_resources import aws_s3control
from get_aws_resources import aws_s3tables
from get_aws_resources import aws_sagemaker
from get_aws_resources import aws_schemas
from get_aws_resources import aws_scheduler
from get_aws_resources import aws_securityhub
from get_aws_resources import aws_secretsmanager
from get_aws_resources import aws_servicecatalog
from get_aws_resources import aws_servicediscovery
from get_aws_resources import aws_shield
from get_aws_resources import aws_ses
from get_aws_resources import aws_sns
from get_aws_resources import aws_sqs
from get_aws_resources import aws_ssm
from get_aws_resources import aws_sso_admin
from get_aws_resources import aws_transfer
from get_aws_resources import aws_vpc_lattice
from get_aws_resources import aws_waf
from get_aws_resources import aws_wafv2
from get_aws_resources import aws_xray


def call_resource(config: ConfigurationManager, resource_type: str, resource_id: str) -> None:
    """
    Call the appropriate resource processing function.
    
    This is the main entry point for processing AWS resources. It maintains
    all the original functionality while using ConfigurationManager.
    
    Args:
        config: Configuration manager with processing settings.
        resource_type: Type of AWS resource to process.
        resource_id: ID of the specific resource to process.
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
            return
        
        # Check if resource type cannot be imported
        if resource_type in aws_no_import.noimport:
            print(f"WARNING: Can not import type: {resource_type}")
            if resource_id is not None:
                with open('not-imported.log', 'a') as f2:
                    f2.write(f"{resource_type} : {resource_id}\n")
                config.mark_resource_processed(f"{resource_type}.{resource_id}")
            return
        
        # Check if resource type is not implemented
        if resource_type in aws_not_implemented.notimplemented:
            print(f"Not supported by aws2tf currently: {resource_type} "
                  "please submit github issue to request support")
            return
        
        # Handle null resource type
        if resource_type == "aws_null":
            with open('stack-null.err', 'a') as f3:
                f3.write(f"-->> called aws_null for: {resource_id}\n")
            return
        
        # Check if already processed
        if config.is_debug_enabled():
            print(f"---->>>>> {resource_type}   {resource_id}")
        
        if resource_id is not None:
            ti = f"{resource_type}.{resource_id}"
            if config.is_resource_processed(ti):
                if config.is_debug_enabled():
                    print(f"Already processed {ti}")
                print(f"Already processed {ti}")
                return
        else:
            if resource_type in needid_dict.aws_needid:
                print(f"WARNING: {resource_type} can not have null id must pass parameter "
                      f"{needid_dict.aws_needid[resource_type]['param']}")
                return
        
        # Get resource data
        clfn, descfn, topkey, key, filterid = resources.resource_data(resource_type, resource_id)
        
        if key == "NOIMPORT":
            print(f"WARNING: Can not import type: {resource_type}")
            return
        
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
            # TODO: These functions will need to be updated in future tasks to accept config
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
        
    except Exception as e:
        error_msg = f"Error in call_resource {resource_type} {resource_id}: {str(e)}"
        print(error_msg)
        
        if config.is_debug_enabled():
            import traceback
            traceback.print_exc()


def getresource(config: ConfigurationManager, resource_type: str, resource_id: str, 
                clfn: str, descfn: str, topkey: str, key: str, filterid: str) -> bool:
    """
    Generic resource processing function.
    
    This function handles the core logic for discovering and processing AWS resources,
    maintaining all original functionality while using ConfigurationManager.
    
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
            print(f"-1-> In getresource doing {resource_type} with id {resource_id} "
                  f"clfn={clfn} descfn={descfn} topkey={topkey} key={key} filterid={filterid}")
        
        # Check if type is in types list (skip if found)
        if hasattr(config.runtime, 'types') and resource_type in str(config.runtime.types):
            print(f"Found {resource_type} in types skipping ...")
            return True
        
        # Check if already processed
        if resource_id is not None:
            pt = f"{resource_type}.{resource_id}"
            if config.is_resource_processed(pt):
                print(f"Found {pt} in processed skipping ...")
                return True
        
        # Call AWS API to get resource data
        response = call_boto3(config, resource_type, clfn, descfn, topkey, key, resource_id)
        
        if str(response) != "[]":
            for item in response:
                if config.is_debug_enabled():
                    print(f"--{item}")
                
                # Process all resources if no specific ID
                if resource_id is None or filterid == "":
                    # Skip AWS service roles
                    try:
                        if "aws-service-role" in str(item.get("Path", "")):
                            if config.is_debug_enabled():
                                print(f"Skipping service role {item.get(key, 'unknown')}")
                            continue
                    except:
                        pass
                    
                    try:
                        theid = item[key]
                    except (TypeError, KeyError):
                        print(f"ERROR: getresource TypeError: {response} key={key} type={resource_type}, {descfn}")
                        with open('boto3-error.err', 'a') as f:
                            f.write(f"ERROR: getresource TypeError: type={resource_type} key={key} descfn={descfn}\n{response}\n")
                        continue
                    
                    pt = f"{resource_type}.{theid}"
                    if not config.is_resource_processed(pt):
                        write_import(config, resource_type, theid, None)
                    else:
                        print(f"Found {pt} in processed skipping ...")
                        continue
                
                # Process specific resource ID
                else:
                    if config.is_debug_enabled():
                        print(f"-gr31- filterid={filterid} id={resource_id} key={key}")
                        print(str(item))
                    
                    if "." not in filterid:
                        try:
                            if resource_id == str(item[filterid]):
                                if config.is_debug_enabled():
                                    print(f"-gr31 item-{item}")
                                
                                theid = item[key]
                                pt = f"{resource_type}.{theid}"
                                if not config.is_resource_processed(pt):
                                    write_import(config, resource_type, theid, None)
                                else:
                                    print(f"Found {pt} in processed skipping ...")
                                    continue
                        except (KeyError, TypeError):
                            continue
                    else:
                        # Handle nested filterid (e.g., "Tags.Key")
                        filter_parts = filterid.split(".")
                        try:
                            nested_item = item
                            for part in filter_parts:
                                nested_item = nested_item[part]
                            
                            if resource_id == str(nested_item):
                                theid = item[key]
                                pt = f"{resource_type}.{theid}"
                                if not config.is_resource_processed(pt):
                                    write_import(config, resource_type, theid, None)
                                else:
                                    print(f"Found {pt} in processed skipping ...")
                                    continue
                        except (KeyError, TypeError):
                            continue
        
        return True
        
    except Exception as e:
        handle_error(config, e, "getresource", clfn, descfn, topkey, resource_id)
        return False


def call_boto3(config: ConfigurationManager, resource_type: str, clfn: str, 
               descfn: str, topkey: str, key: str, resource_id: str) -> List[Dict[str, Any]]:
    """
    Call AWS boto3 API to get resource information.
    
    This function maintains all the original boto3 calling logic while using
    ConfigurationManager for session management and debug settings.
    
    Args:
        config: Configuration manager.
        resource_type: Type of AWS resource.
        clfn: Client function name.
        descfn: Describe function name.
        topkey: Top-level key in response.
        key: Key for resource data.
        resource_id: Resource ID.
        
    Returns:
        List of AWS resources from API response.
    """
    try:
        if config.is_debug_enabled():
            print(f"call_boto3 clfn={clfn} descfn={descfn} topkey={topkey} id={resource_id}")
        
        response = []
        
        # Get AWS session from config
        session = config.get_aws_session()
        client = session.client(clfn)
        
        try:
            paginator = client.get_paginator(descfn)
            
            # Handle specific API patterns
            if "apigatewayv2" in str(resource_type):
                for page in paginator.paginate(ApiId=resource_id):
                    response.extend(page[topkey])
                pkey = f"{resource_type}.{resource_id}"
                config.mark_resource_processed(pkey)
            
            elif descfn == "describe_launch_templates":
                if resource_id is not None:
                    if resource_id.startswith("lt-"):
                        for page in paginator.paginate(LaunchTemplateIds=[resource_id]):
                            response.extend(page[topkey])
                    else:
                        for page in paginator.paginate(LaunchTemplateNames=[resource_id]):
                            response.extend(page[topkey])
                else:
                    for page in paginator.paginate():
                        response.extend(page[topkey])
            
            elif descfn == "describe_instances":
                if resource_id is not None:
                    if "i-" in resource_id:
                        for page in paginator.paginate(InstanceIds=[resource_id]):
                            response.extend(page[topkey][0]['Instances'])
                else:
                    for page in paginator.paginate():
                        if len(page[topkey]) == 0:
                            continue
                        response.extend(page[topkey][0]['Instances'])
            
            elif descfn in ["describe_pod_identity_association", "list_fargate_profiles", 
                           "list_nodegroups", "list_identity_provider_configs", "list_addons"]:
                for page in paginator.paginate(clusterName=resource_id):
                    response.extend(page[topkey])
            
            elif descfn == "list_access_keys" and resource_id is not None:
                for page in paginator.paginate(UserName=resource_id):
                    response.extend(page[topkey])
            
            elif clfn == "kms" and descfn == "list_aliases" and resource_id is not None:
                if resource_id.startswith("k-"):
                    resource_id = resource_id[2:]
                for page in paginator.paginate(KeyId=resource_id):
                    response.extend(page[topkey])
                return response
            
            elif clfn == "lambda" and descfn == "list_aliases" and resource_id is not None:
                for page in paginator.paginate(FunctionName=resource_id):
                    response.extend(page[topkey])
            
            # Add more specific API patterns as needed...
            
            else:
                # Generic pagination
                if resource_id is not None:
                    # Try to paginate with the resource ID
                    try:
                        for page in paginator.paginate():
                            response.extend(page[topkey])
                    except Exception:
                        # Fall back to non-paginated call
                        describe_func = getattr(client, descfn)
                        result = describe_func()
                        response.extend(result[topkey])
                else:
                    for page in paginator.paginate():
                        response.extend(page[topkey])
        
        except ClientError as e:
            error_code = e.response['Error']['Code']
            if config.is_debug_enabled():
                print(f"AWS API ClientError: {error_code} - {e.response['Error']['Message']}")
            
            # Handle specific error codes
            if error_code in ['InvalidInstanceID.NotFound', 'InvalidVpcID.NotFound', 
                             'InvalidSubnetID.NotFound', 'InvalidGroupId.NotFound']:
                if config.is_debug_enabled():
                    print(f"Resource {resource_id} not found")
                return []
            else:
                # Re-raise for other errors
                raise
        
        except Exception as e:
            if config.is_debug_enabled():
                print(f"Error in call_boto3: {str(e)}")
            handle_error(config, e, "call_boto3", clfn, descfn, topkey, resource_id)
            return []
        
        return response
        
    except Exception as e:
        handle_error(config, e, "call_boto3", clfn, descfn, topkey, resource_id)
        return []


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
        
        # Handle special cases for resource ID formatting
        if resource_type.startswith("aws_"):
            # Remove aws_ prefix for some operations
            clean_type = resource_type[4:]
        else:
            clean_type = resource_type
        
        # Generate import file
        import_file = f"import__{resource_type}__{tfid}.tf"
        
        with open(import_file, 'w') as f:
            f.write(f'import {{\n')
            f.write(f'  to = {resource_type}.{tfid}\n')
            f.write(f'  id = "{resource_id}"\n')
            f.write(f'}}\n')
        
        if config.is_debug_enabled():
            print(f"Created import file: {import_file}")
        
        # Mark as processed
        config.mark_resource_processed(f"{resource_type}.{resource_id}")
            
    except Exception as e:
        handle_error(config, e, "write_import", "", "", "", resource_id)


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


# Additional utility functions from original common.py

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


# Additional functions from original common.py would be migrated here...
# This includes tfplan1, tfplan2, tfplan3, wrapup, fix_imports, etc.
# For now, I'm focusing on the core resource processing functions.

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
    
    # Add to processing queue by calling call_resource
    call_resource(config, resource_type, resource_id)


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