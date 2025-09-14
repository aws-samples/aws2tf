#!/usr/bin/env python3
"""
Minimal common functions for aws2tf that use ConfigurationManager.

This is a simplified version that avoids complex imports to enable testing
of the configuration management system.
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
            print(f"Processing {resource_type} {resource_id}")
        
        # Check if resource type is in exclusion list
        if hasattr(config.runtime, 'all_extypes') and resource_type in config.runtime.all_extypes:
            if config.is_debug_enabled():
                print(f"Excluding: {resource_type}, {resource_id}")
            pkey = f"{resource_type}.{resource_id}"
            config.mark_resource_processed(pkey)
            return True
        
        # Simple resource processing
        success = process_resource_minimal(config, resource_type, resource_id)
        
        # Log processed resource
        try:
            with open('processed-resources.log', 'a') as f4:
                f4.write(f"{resource_type} : {resource_id}\n")
        except Exception:
            pass  # Don't fail if we can't write log
        
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


def process_resource_minimal(config: ConfigurationManager, resource_type: str, resource_id: str) -> bool:
    """
    Minimal resource processing function.
    
    Args:
        config: Configuration manager.
        resource_type: Type of AWS resource.
        resource_id: Resource ID.
        
    Returns:
        True if resource was processed successfully.
    """
    try:
        print(f"Processing {resource_type}: {resource_id}")
        
        # Get AWS session from config
        session = config.get_aws_session()
        
        # Map resource types to AWS services
        service_map = {
            'aws_vpc': 'ec2',
            'vpc': 'ec2',  # Allow shorthand
            'aws_subnet': 'ec2',
            'subnet': 'ec2',
            'aws_security_group': 'ec2',
            'sg': 'ec2',
            'aws_instance': 'ec2',
            'ec2': 'ec2',
            'aws_s3_bucket': 's3',
            's3': 's3',
            'aws_iam_role': 'iam',
            'iam': 'iam',
            'aws_lambda_function': 'lambda',
            'lambda': 'lambda'
        }
        
        service = service_map.get(resource_type, 'ec2')  # Default to ec2
        
        # Create client
        client = session.client(service)
        
        # For resource types without specific ID, list resources
        if resource_id is None:
            return list_resources_minimal(config, client, resource_type, service)
        
        # Verify specific resource exists
        if resource_type in ['aws_vpc', 'vpc']:
            response = client.describe_vpcs(VpcIds=[resource_id])
            if not response.get('Vpcs'):
                print(f"VPC {resource_id} not found")
                return False
            vpc = response['Vpcs'][0]
            print(f"Found VPC: {vpc['VpcId']} ({vpc.get('CidrBlock', 'N/A')})")
            
        elif resource_type in ['aws_subnet', 'subnet']:
            response = client.describe_subnets(SubnetIds=[resource_id])
            if not response.get('Subnets'):
                print(f"Subnet {resource_id} not found")
                return False
            subnet = response['Subnets'][0]
            print(f"Found Subnet: {subnet['SubnetId']} ({subnet.get('CidrBlock', 'N/A')})")
            
        elif resource_type in ['aws_security_group', 'sg']:
            response = client.describe_security_groups(GroupIds=[resource_id])
            if not response.get('SecurityGroups'):
                print(f"Security Group {resource_id} not found")
                return False
            sg = response['SecurityGroups'][0]
            print(f"Found Security Group: {sg['GroupId']} ({sg.get('GroupName', 'N/A')})")
            
        elif resource_type in ['aws_instance', 'ec2']:
            response = client.describe_instances(InstanceIds=[resource_id])
            if not response.get('Reservations'):
                print(f"Instance {resource_id} not found")
                return False
            instance = response['Reservations'][0]['Instances'][0]
            print(f"Found Instance: {instance['InstanceId']} ({instance.get('State', {}).get('Name', 'N/A')})")
            
        elif resource_type in ['aws_s3_bucket', 's3']:
            try:
                client.head_bucket(Bucket=resource_id)
                print(f"Found S3 Bucket: {resource_id}")
            except ClientError:
                print(f"S3 Bucket {resource_id} not found or not accessible")
                return False
                
        elif resource_type in ['aws_iam_role', 'iam']:
            try:
                response = client.get_role(RoleName=resource_id)
                role = response['Role']
                print(f"Found IAM Role: {role['RoleName']}")
            except ClientError:
                print(f"IAM Role {resource_id} not found")
                return False
                
        elif resource_type in ['aws_lambda_function', 'lambda']:
            try:
                response = client.get_function(FunctionName=resource_id)
                function = response['Configuration']
                print(f"Found Lambda Function: {function['FunctionName']}")
            except ClientError:
                print(f"Lambda Function {resource_id} not found")
                return False
        else:
            print(f"Resource type {resource_type} not yet supported in minimal mode")
            return False
        
        # Generate minimal Terraform files
        generate_terraform_file_minimal(config, resource_type, resource_id)
        generate_import_file_minimal(config, resource_type, resource_id)
        
        print(f"Successfully processed {resource_type} {resource_id}")
        return True
        
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if 'NotFound' in error_code or 'InvalidId' in error_code:
            print(f"Resource {resource_id} not found: {error_code}")
        else:
            print(f"AWS API error: {error_code} - {e.response['Error']['Message']}")
        return False
    except Exception as e:
        print(f"Error processing {resource_type} {resource_id}: {str(e)}")
        if config.is_debug_enabled():
            import traceback
            traceback.print_exc()
        return False


def list_resources_minimal(config: ConfigurationManager, client, resource_type: str, service: str) -> bool:
    """
    List resources of a given type.
    
    Args:
        config: Configuration manager.
        client: AWS client.
        resource_type: Type of AWS resource.
        service: AWS service name.
        
    Returns:
        True if listing was successful.
    """
    try:
        print(f"Listing all {resource_type} resources...")
        
        if resource_type in ['aws_vpc', 'vpc']:
            response = client.describe_vpcs()
            vpcs = response.get('Vpcs', [])
            print(f"Found {len(vpcs)} VPCs:")
            for vpc in vpcs[:10]:  # Limit to first 10
                print(f"  - {vpc['VpcId']} ({vpc.get('CidrBlock', 'N/A')})")
                # Process each VPC
                call_resource(config, 'aws_vpc', vpc['VpcId'])
                
        elif resource_type in ['aws_subnet', 'subnet']:
            response = client.describe_subnets()
            subnets = response.get('Subnets', [])
            print(f"Found {len(subnets)} Subnets:")
            for subnet in subnets[:10]:  # Limit to first 10
                print(f"  - {subnet['SubnetId']} ({subnet.get('CidrBlock', 'N/A')})")
                
        elif resource_type in ['aws_instance', 'ec2']:
            response = client.describe_instances()
            instances = []
            for reservation in response.get('Reservations', []):
                instances.extend(reservation.get('Instances', []))
            print(f"Found {len(instances)} Instances:")
            for instance in instances[:10]:  # Limit to first 10
                print(f"  - {instance['InstanceId']} ({instance.get('State', {}).get('Name', 'N/A')})")
                
        elif resource_type in ['aws_s3_bucket', 's3']:
            response = client.list_buckets()
            buckets = response.get('Buckets', [])
            print(f"Found {len(buckets)} S3 Buckets:")
            for bucket in buckets[:10]:  # Limit to first 10
                print(f"  - {bucket['Name']}")
                
        else:
            print(f"Listing not yet supported for {resource_type}")
            return False
            
        return True
        
    except Exception as e:
        print(f"Error listing {resource_type}: {str(e)}")
        return False


def generate_terraform_file_minimal(config: ConfigurationManager, resource_type: str, resource_id: str) -> None:
    """
    Generate a minimal Terraform configuration file.
    
    Args:
        config: Configuration manager.
        resource_type: Type of AWS resource.
        resource_id: Resource ID.
    """
    try:
        # Ensure we have a path1 directory
        if not hasattr(config.runtime, 'path1') or not config.runtime.path1:
            print("Warning: No output path configured, skipping Terraform file generation")
            return
            
        # Create directory if it doesn't exist
        os.makedirs(config.runtime.path1, exist_ok=True)
        
        # Clean up resource ID for Terraform naming
        tf_name = resource_id.replace('-', '_').replace('.', '_').replace(':', '_')
        
        # Normalize resource type
        if not resource_type.startswith('aws_'):
            if resource_type == 'vpc':
                resource_type = 'aws_vpc'
            elif resource_type == 'subnet':
                resource_type = 'aws_subnet'
            elif resource_type == 'sg':
                resource_type = 'aws_security_group'
            elif resource_type == 'ec2':
                resource_type = 'aws_instance'
            elif resource_type == 's3':
                resource_type = 'aws_s3_bucket'
            elif resource_type == 'iam':
                resource_type = 'aws_iam_role'
            elif resource_type == 'lambda':
                resource_type = 'aws_lambda_function'
        
        # Generate basic Terraform configuration
        tf_content = f'''# {resource_type}: {resource_id}
# Generated by aws2tf with ConfigurationManager
resource "{resource_type}" "{tf_name}" {{
  # Configuration will be generated by terraform plan -generate-config-out
  # This is a placeholder for the import process
}}
'''
        
        # Write to file
        tf_file = os.path.join(config.runtime.path1, f"{resource_type}__{tf_name}.tf")
        with open(tf_file, 'w') as f:
            f.write(tf_content)
        
        print(f"Generated Terraform file: {tf_file}")
            
    except Exception as e:
        print(f"Error generating Terraform file for {resource_type} {resource_id}: {str(e)}")


def generate_import_file_minimal(config: ConfigurationManager, resource_type: str, resource_id: str) -> None:
    """
    Generate Terraform import file.
    
    Args:
        config: Configuration manager.
        resource_type: Type of AWS resource.
        resource_id: Resource ID.
    """
    try:
        # Ensure we have a path1 directory
        if not hasattr(config.runtime, 'path1') or not config.runtime.path1:
            print("Warning: No output path configured, skipping import file generation")
            return
            
        # Create directory if it doesn't exist
        os.makedirs(config.runtime.path1, exist_ok=True)
        
        # Clean up resource ID for Terraform naming
        tf_name = resource_id.replace('-', '_').replace('.', '_').replace(':', '_')
        
        # Normalize resource type
        if not resource_type.startswith('aws_'):
            if resource_type == 'vpc':
                resource_type = 'aws_vpc'
            elif resource_type == 'subnet':
                resource_type = 'aws_subnet'
            elif resource_type == 'sg':
                resource_type = 'aws_security_group'
            elif resource_type == 'ec2':
                resource_type = 'aws_instance'
            elif resource_type == 's3':
                resource_type = 'aws_s3_bucket'
            elif resource_type == 'iam':
                resource_type = 'aws_iam_role'
            elif resource_type == 'lambda':
                resource_type = 'aws_lambda_function'
        
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
    return subprocess.run(cmd, shell=True, capture_output=True)


def check_python_version() -> None:
    """
    Check Python and boto3 versions.
    
    Raises:
        SystemExit: If versions are too old.
    """
    version = sys.version_info
    major = version.major
    minor = version.minor
    
    if major < 3 or (major == 3 and minor < 8):
        print("This program requires Python 3.8 or later.")
        sys.exit(1)
    
    # Check boto3 version if available
    try:
        import boto3
        bv = str(boto3.__version__)
        print(f"boto3 version: {bv}")
        
        if boto3.__version__ < '1.36.13':
            vs = bv.split(".")
            v1 = int(vs[0]) * 100000 + int(vs[1]) * 1000 + int(vs[2])
            if v1 < 136013:
                print(f"boto3 version: {bv}")
                print("This program requires boto3 1.36.13 or later.")
                print("Try: pip install boto3  -or-  pip install boto3==1.36.13")
                sys.exit(1)
    except ImportError:
        print("Warning: boto3 not found")


def aws_tf(config: ConfigurationManager, region: str, args) -> None:
    """
    Generate Terraform provider configuration.
    
    Args:
        config: Configuration manager.
        region: AWS region.
        args: Command line arguments.
    """
    try:
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
                
        print("Generated Terraform provider configuration")
        
    except Exception as e:
        print(f"Error generating Terraform configuration: {str(e)}")


def ctrl_c_handler(signum, frame):
    """
    Handle Ctrl-C interrupt.
    
    Args:
        signum: Signal number.
        frame: Current stack frame.
    """
    print("Ctrl-C pressed.")
    print("exit 036")
    exit()