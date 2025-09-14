#!/usr/bin/env python3
"""
Simplified updated common functions for aws2tf that use ConfigurationManager.

This module contains the core updated functions that accept
a ConfigurationManager parameter instead of using global variables.
"""

import boto3
from botocore.exceptions import ClientError
import sys
import subprocess
import os
import json
from typing import Optional, Dict, Any, List, Union

# Import the configuration system
from .config import ConfigurationManager


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
        
        # For now, we'll use a simplified approach that just marks resources as processed
        # The full implementation would integrate with the existing resource modules
        
        if config.is_debug_enabled():
            print(f"Processing {resource_type} {resource_id}")
        
        # Simulate resource processing
        success = process_resource_simple(config, resource_type, resource_id)
        
        # Log processed resource
        with open('processed-resources.log', 'a') as f4:
            f4.write(f"{resource_type} : {resource_id}\n")
        
        # Mark as processed
        if resource_id is not None:
            config.mark_resource_processed(f"{resource_type}.{resource_id}")
        
        return success
        
    except Exception as e:
        error_msg = f"Error processing {resource_type} {resource_id}: {str(e)}"
        print(error_msg)
        
        if config.is_debug_enabled():
            import traceback
            traceback.print_exc()
        
        return False


def process_resource_simple(config: ConfigurationManager, resource_type: str, resource_id: str) -> bool:
    """
    Simplified resource processing function.
    
    Args:
        config: Configuration manager.
        resource_type: Type of AWS resource.
        resource_id: Resource ID.
        
    Returns:
        True if resource was processed successfully.
    """
    try:
        # Get AWS session from config
        session = config.get_aws_session()
        
        # Map resource types to AWS services
        service_map = {
            'aws_vpc': 'ec2',
            'aws_subnet': 'ec2',
            'aws_security_group': 'ec2',
            'aws_instance': 'ec2',
            'aws_s3_bucket': 's3',
            'aws_iam_role': 'iam',
            'aws_lambda_function': 'lambda'
        }
        
        service = service_map.get(resource_type, 'ec2')  # Default to ec2
        
        # Create client
        client = session.client(service)
        
        # Verify resource exists (simplified check)
        if resource_type == 'aws_vpc':
            response = client.describe_vpcs(VpcIds=[resource_id])
            if not response.get('Vpcs'):
                print(f"VPC {resource_id} not found")
                return False
        elif resource_type == 'aws_subnet':
            response = client.describe_subnets(SubnetIds=[resource_id])
            if not response.get('Subnets'):
                print(f"Subnet {resource_id} not found")
                return False
        elif resource_type == 'aws_security_group':
            response = client.describe_security_groups(GroupIds=[resource_id])
            if not response.get('SecurityGroups'):
                print(f"Security Group {resource_id} not found")
                return False
        elif resource_type == 'aws_instance':
            response = client.describe_instances(InstanceIds=[resource_id])
            if not response.get('Reservations'):
                print(f"Instance {resource_id} not found")
                return False
        elif resource_type == 'aws_s3_bucket':
            try:
                client.head_bucket(Bucket=resource_id)
            except ClientError:
                print(f"S3 Bucket {resource_id} not found or not accessible")
                return False
        elif resource_type == 'aws_iam_role':
            try:
                client.get_role(RoleName=resource_id)
            except ClientError:
                print(f"IAM Role {resource_id} not found")
                return False
        elif resource_type == 'aws_lambda_function':
            try:
                client.get_function(FunctionName=resource_id)
            except ClientError:
                print(f"Lambda Function {resource_id} not found")
                return False
        
        # Generate simplified Terraform files
        generate_terraform_file(config, resource_type, resource_id)
        generate_import_file(config, resource_type, resource_id)
        
        if config.is_debug_enabled():
            print(f"Successfully processed {resource_type} {resource_id}")
        
        return True
        
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if 'NotFound' in error_code or 'InvalidId' in error_code:
            print(f"Resource {resource_id} not found")
        else:
            print(f"AWS API error: {error_code} - {e.response['Error']['Message']}")
        return False
    except Exception as e:
        print(f"Error processing {resource_type} {resource_id}: {str(e)}")
        if config.is_debug_enabled():
            import traceback
            traceback.print_exc()
        return False


def generate_terraform_file(config: ConfigurationManager, resource_type: str, resource_id: str) -> None:
    """
    Generate a simplified Terraform configuration file.
    
    Args:
        config: Configuration manager.
        resource_type: Type of AWS resource.
        resource_id: Resource ID.
    """
    try:
        # Clean up resource ID for Terraform naming
        tf_name = resource_id.replace('-', '_').replace('.', '_').replace(':', '_')
        
        # Generate basic Terraform configuration
        tf_content = f'''# {resource_type}: {resource_id}
resource "{resource_type}" "{tf_name}" {{
  # Configuration will be generated by terraform plan -generate-config-out
  # This is a placeholder for the import process
}}
'''
        
        # Write to file
        tf_file = os.path.join(config.runtime.path1, f"{resource_type}__{tf_name}.tf")
        with open(tf_file, 'w') as f:
            f.write(tf_content)
        
        if config.is_debug_enabled():
            print(f"Generated Terraform file: {tf_file}")
            
    except Exception as e:
        print(f"Error generating Terraform file for {resource_type} {resource_id}: {str(e)}")


def generate_import_file(config: ConfigurationManager, resource_type: str, resource_id: str) -> None:
    """
    Generate Terraform import file.
    
    Args:
        config: Configuration manager.
        resource_type: Type of AWS resource.
        resource_id: Resource ID.
    """
    try:
        # Clean up resource ID for Terraform naming
        tf_name = resource_id.replace('-', '_').replace('.', '_').replace(':', '_')
        
        # Generate import configuration
        import_content = f'''import {{
  to = {resource_type}.{tf_name}
  id = "{resource_id}"
}}
'''
        
        # Write to file
        import_file = os.path.join(config.runtime.path1, f"import__{resource_type}__{tf_name}.tf")
        with open(import_file, 'w') as f:
            f.write(import_content)
        
        if config.is_debug_enabled():
            print(f"Generated import file: {import_file}")
            
    except Exception as e:
        print(f"Error generating import file for {resource_type} {resource_id}: {str(e)}")


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
        
        if hasattr(args, 'profile') and args.profile is not None:
            f3.write(f'  profile                  = "{config.aws.profile}"\n')
        
        if not config.runtime.serverless:
            f3.write('  shared_credentials_files = ["~/.aws/credentials"]\n')
        
        f3.write('}\n')
    
    # Copy to imported directory
    os.makedirs('imported', exist_ok=True)
    import shutil
    shutil.copy('provider.tf', 'imported/provider.tf')
    
    # Create data sources file if it doesn't exist
    if not os.path.isfile("data-aws.tf"):
        with open("data-aws.tf", 'w') as f3:
            f3.write('data "aws_region" "current" {}\n')
            f3.write('data "aws_caller_identity" "current" {}\n')
            f3.write('data "aws_availability_zones" "available" {\n')
            f3.write('  state = "available"\n')
            f3.write('}\n')


def ctrl_c_handler(signum, frame):
    """
    Handle Ctrl-C interrupt.
    
    Args:
        signum: Signal number.
        frame: Current stack frame.
    """
    print("Ctrl-C pressed.")
    print("exit 036")
    # Note: In a real implementation, we'd need to import timed_int
    # For now, just exit
    exit()


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