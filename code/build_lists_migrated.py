#!/usr/bin/env python3
"""
Migrated build_lists module for aws2tf that uses ConfigurationManager.

This module contains resource list building functions updated to use
ConfigurationManager instead of global variables while maintaining
thread-safe concurrent processing.
"""

import boto3
import concurrent.futures
import json
import datetime
from typing import List, Tuple, Dict, Any, Optional
from .config import ConfigurationManager


def build_lists(config: ConfigurationManager) -> bool:
    """
    Build core resource lists using concurrent processing.
    
    Args:
        config: Configuration manager for AWS session and resource tracking.
        
    Returns:
        True if lists were built successfully.
    """
    print("Building core resource lists ...")
    config.set_tracking_message("Stage 2 of 10, Building core resource lists ...")
    
    def fetch_lambda_data() -> List[Tuple[str, str]]:
        """Fetch Lambda function data."""
        try:
            session = config.get_aws_session()
            client = session.client('lambda')
            response = []
            paginator = client.get_paginator('list_functions')
            for page in paginator.paginate():
                response.extend(page['Functions'])
            return [('lambda', j['FunctionName']) for j in response]
        except Exception as e:
            if config.is_debug_enabled():
                print(f"Error fetching Lambda data: {e}")
            return []
    
    def fetch_vpc_data() -> List[Tuple[str, str]]:
        """Fetch VPC data."""
        try:
            session = config.get_aws_session()
            client = session.client('ec2')
            response = []
            paginator = client.get_paginator('describe_vpcs')
            for page in paginator.paginate():
                response.extend(page['Vpcs'])
            
            # Store VPC data in configuration
            config.resources.set_vpc_data(response)
            return [('vpc', j['VpcId']) for j in response]
        except Exception as e:
            if config.is_debug_enabled():
                print(f"Error fetching VPC data: {e}")
            return []
    
    def fetch_s3_data() -> List[Tuple[str, str]]:
        """Fetch S3 bucket data."""
        try:
            session = config.get_aws_session()
            client = session.client('s3')
            response = []
            paginator = client.get_paginator('list_buckets')
            
            # Note: S3 list_buckets doesn't support BucketRegion parameter in paginator
            # We'll filter by region after getting the list
            for page in paginator.paginate():
                response.extend(page['Buckets'])
            
            # Filter buckets by region
            region_buckets = []
            for bucket in response:
                try:
                    bucket_location = client.get_bucket_location(Bucket=bucket['Name'])
                    bucket_region = bucket_location.get('LocationConstraint')
                    # us-east-1 returns None for LocationConstraint
                    if bucket_region is None:
                        bucket_region = 'us-east-1'
                    
                    if bucket_region == config.aws.region:
                        region_buckets.append(bucket)
                except Exception:
                    # Skip buckets we can't access
                    continue
            
            return [('s3', j['Name']) for j in region_buckets]
        except Exception as e:
            if config.is_debug_enabled():
                print(f"Error fetching S3 data: {e}")
            return []
    
    def fetch_sg_data() -> List[Tuple[str, str]]:
        """Fetch Security Group data."""
        try:
            session = config.get_aws_session()
            client = session.client('ec2')
            response = []
            paginator = client.get_paginator('describe_security_groups')
            for page in paginator.paginate():
                response.extend(page['SecurityGroups'])
            return [('sg', j['GroupId']) for j in response]
        except Exception as e:
            if config.is_debug_enabled():
                print(f"Error fetching Security Group data: {e}")
            return []
    
    def fetch_subnet_data() -> List[Tuple[str, str]]:
        """Fetch Subnet data."""
        try:
            session = config.get_aws_session()
            client = session.client('ec2')
            response = []
            paginator = client.get_paginator('describe_subnets')
            for page in paginator.paginate():
                response.extend(page['Subnets'])
            return [('subnet', j['SubnetId']) for j in response]
        except Exception as e:
            if config.is_debug_enabled():
                print(f"Error fetching Subnet data: {e}")
            return []
    
    def fetch_tgw_data() -> List[Tuple[str, str]]:
        """Fetch Transit Gateway data."""
        try:
            session = config.get_aws_session()
            client = session.client('ec2')
            response = []
            paginator = client.get_paginator('describe_transit_gateways')
            for page in paginator.paginate():
                response.extend(page['TransitGateways'])
            return [('tgw', j['TransitGatewayId']) for j in response]
        except Exception as e:
            if config.is_debug_enabled():
                print(f"Error fetching Transit Gateway data: {e}")
            return []
    
    def fetch_roles_data() -> List[Tuple[str, str]]:
        """Fetch IAM Roles data."""
        try:
            session = config.get_aws_session()
            client = session.client('iam', region_name='us-east-1')  # IAM is global
            response = []
            paginator = client.get_paginator('list_roles')
            for page in paginator.paginate():
                response.extend(page['Roles'])
            
            # Save roles data to file
            import os
            os.makedirs('imported', exist_ok=True)
            with open('imported/roles.json', 'w') as f:
                json.dump(response, f, indent=2, default=str)
            
            return [('iam', j['RoleName']) for j in response]
        except Exception as e:
            if config.is_debug_enabled():
                print(f"Error fetching IAM Roles data: {e}")
            return []
    
    def fetch_policies_data() -> List[Tuple[str, str]]:
        """Fetch IAM Policies data."""
        try:
            session = config.get_aws_session()
            client = session.client('iam', region_name='us-east-1')  # IAM is global
            response = []
            paginator = client.get_paginator('list_policies')
            for page in paginator.paginate(Scope='Local'):
                response.extend(page['Policies'])
            return [('pol', j['Arn']) for j in response]
        except Exception as e:
            if config.is_debug_enabled():
                print(f"Error fetching IAM Policies data: {e}")
            return []
    
    # Use ThreadPoolExecutor to parallelize API calls
    max_workers = config.get_cores()
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(fetch_vpc_data),
            executor.submit(fetch_lambda_data),
            executor.submit(fetch_s3_data),
            executor.submit(fetch_sg_data),
            executor.submit(fetch_subnet_data),
            executor.submit(fetch_tgw_data),
            executor.submit(fetch_roles_data),
            executor.submit(fetch_policies_data)
        ]
        
        # Process results as they complete
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                if isinstance(result, list) and result:
                    if isinstance(result[0], tuple):
                        # Handle resource ID lists
                        resource_type = result[0][0]
                        
                        if resource_type == 'vpc':
                            for _, vpc_id in result:
                                config.resources.add_vpc_to_list(vpc_id)
                        
                        elif resource_type == 'lambda':
                            for _, lambda_id in result:
                                config.resources.add_lambda_to_list(lambda_id)
                        
                        elif resource_type == 's3':
                            session = config.get_aws_session()
                            client = session.client('s3')
                            for _, bucket in result:
                                try:
                                    # Test bucket accessibility
                                    client.list_objects_v2(Bucket=bucket, MaxKeys=1)
                                    config.resources.add_s3_to_list(bucket)
                                except Exception as e:
                                    if config.is_debug_enabled():
                                        print(f"Cannot access bucket {bucket}: {e}")
                                    continue
                        
                        elif resource_type == 'sg':
                            for _, sg_id in result:
                                config.resources.add_sg_to_list(sg_id)
                        
                        elif resource_type == 'subnet':
                            for _, subnet_id in result:
                                config.resources.add_subnet_to_list(subnet_id)
                        
                        elif resource_type == 'tgw':
                            for _, tgw_id in result:
                                config.resources.add_tgw_to_list(tgw_id)
                        
                        elif resource_type == 'iam':
                            for _, role_name in result:
                                config.resources.add_role_to_list(role_name)
                        
                        elif resource_type == 'pol':
                            for _, policy_arn in result:
                                config.resources.add_policy_to_list(policy_arn)
            
            except Exception as e:
                if config.is_debug_enabled():
                    print(f"Error processing future result: {e}")
                continue
    
    return True


def build_secondary_lists(config: ConfigurationManager, resource_id: Optional[str] = None) -> bool:
    """
    Build secondary IAM resource lists.
    
    Args:
        config: Configuration manager for AWS session and resource tracking.
        resource_id: Optional specific resource ID to process.
        
    Returns:
        True if secondary lists were built successfully.
    """
    if resource_id is None:
        st1 = datetime.datetime.now()
        print("Building secondary IAM resource lists ...")
        
        # Get role count for estimation
        role_count = len(config.resources.get_role_list())
        config.processing.set_estimated_time((role_count * 3) / 4)
        config.set_tracking_message("Stage 2 of 10, Building secondary IAM resource lists ...")
        
        # Process all roles
        roles = config.resources.get_role_list()
        return process_role_attachments(config, list(roles.keys()))
    else:
        # Process specific resource
        return process_role_attachments(config, [resource_id])


def process_role_attachments(config: ConfigurationManager, role_names: List[str]) -> bool:
    """
    Process IAM role policy attachments.
    
    Args:
        config: Configuration manager.
        role_names: List of role names to process.
        
    Returns:
        True if processing was successful.
    """
    def fetch_role_policies(role_name: str) -> List[Tuple[str, str, str]]:
        """Fetch policies attached to a role."""
        try:
            session = config.get_aws_session()
            client = session.client('iam', region_name='us-east-1')
            
            # Get attached managed policies
            attached_policies = []
            paginator = client.get_paginator('list_attached_role_policies')
            for page in paginator.paginate(RoleName=role_name):
                attached_policies.extend(page['AttachedPolicies'])
            
            # Get inline policies
            inline_policies = []
            paginator = client.get_paginator('list_role_policies')
            for page in paginator.paginate(RoleName=role_name):
                inline_policies.extend(page['PolicyNames'])
            
            results = []
            # Add managed policies
            for policy in attached_policies:
                results.append(('managed_policy', role_name, policy['PolicyArn']))
            
            # Add inline policies
            for policy_name in inline_policies:
                results.append(('inline_policy', role_name, policy_name))
            
            return results
            
        except Exception as e:
            if config.is_debug_enabled():
                print(f"Error fetching policies for role {role_name}: {e}")
            return []
    
    # Use ThreadPoolExecutor for concurrent processing
    max_workers = min(config.get_cores(), len(role_names))
    if max_workers == 0:
        return True
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(fetch_role_policies, role_name)
            for role_name in role_names
        ]
        
        # Process results as they complete
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                for policy_type, role_name, policy_identifier in result:
                    if policy_type == 'managed_policy':
                        config.resources.add_role_policy_attachment(role_name, policy_identifier)
                    elif policy_type == 'inline_policy':
                        config.resources.add_role_inline_policy(role_name, policy_identifier)
            except Exception as e:
                if config.is_debug_enabled():
                    print(f"Error processing role policy future: {e}")
                continue
    
    return True


def build_resource_dependencies(config: ConfigurationManager, resource_type: str) -> bool:
    """
    Build resource dependency lists for a specific resource type.
    
    Args:
        config: Configuration manager.
        resource_type: Type of resource to build dependencies for.
        
    Returns:
        True if dependencies were built successfully.
    """
    if config.is_debug_enabled():
        print(f"Building dependencies for resource type: {resource_type}")
    
    if resource_type == "vpc":
        return build_vpc_dependencies(config)
    elif resource_type == "ec2":
        return build_ec2_dependencies(config)
    elif resource_type == "iam":
        return build_iam_dependencies(config)
    elif resource_type == "s3":
        return build_s3_dependencies(config)
    else:
        if config.is_debug_enabled():
            print(f"No specific dependency builder for {resource_type}")
        return True


def build_vpc_dependencies(config: ConfigurationManager) -> bool:
    """
    Build VPC-related resource dependencies.
    
    Args:
        config: Configuration manager.
        
    Returns:
        True if VPC dependencies were built successfully.
    """
    try:
        session = config.get_aws_session()
        ec2_client = session.client('ec2')
        
        # Get all VPCs
        vpc_list = config.resources.get_vpc_list()
        
        for vpc_id in vpc_list.keys():
            # Find subnets in this VPC
            try:
                subnets_response = ec2_client.describe_subnets(
                    Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}]
                )
                for subnet in subnets_response['Subnets']:
                    config.resources.add_subnet_to_list(subnet['SubnetId'])
                    config.resources.add_vpc_subnet_relationship(vpc_id, subnet['SubnetId'])
            except Exception as e:
                if config.is_debug_enabled():
                    print(f"Error fetching subnets for VPC {vpc_id}: {e}")
            
            # Find security groups in this VPC
            try:
                sgs_response = ec2_client.describe_security_groups(
                    Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}]
                )
                for sg in sgs_response['SecurityGroups']:
                    config.resources.add_sg_to_list(sg['GroupId'])
                    config.resources.add_vpc_sg_relationship(vpc_id, sg['GroupId'])
            except Exception as e:
                if config.is_debug_enabled():
                    print(f"Error fetching security groups for VPC {vpc_id}: {e}")
        
        return True
        
    except Exception as e:
        if config.is_debug_enabled():
            print(f"Error building VPC dependencies: {e}")
        return False


def build_ec2_dependencies(config: ConfigurationManager) -> bool:
    """
    Build EC2-related resource dependencies.
    
    Args:
        config: Configuration manager.
        
    Returns:
        True if EC2 dependencies were built successfully.
    """
    try:
        session = config.get_aws_session()
        ec2_client = session.client('ec2')
        
        # Get all instances and their dependencies
        instances_response = ec2_client.describe_instances()
        
        for reservation in instances_response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                
                # Add VPC relationship
                if 'VpcId' in instance:
                    config.resources.add_vpc_instance_relationship(
                        instance['VpcId'], instance_id
                    )
                
                # Add subnet relationship
                if 'SubnetId' in instance:
                    config.resources.add_subnet_instance_relationship(
                        instance['SubnetId'], instance_id
                    )
                
                # Add security group relationships
                for sg in instance.get('SecurityGroups', []):
                    config.resources.add_sg_instance_relationship(
                        sg['GroupId'], instance_id
                    )
        
        return True
        
    except Exception as e:
        if config.is_debug_enabled():
            print(f"Error building EC2 dependencies: {e}")
        return False


def build_iam_dependencies(config: ConfigurationManager) -> bool:
    """
    Build IAM-related resource dependencies.
    
    Args:
        config: Configuration manager.
        
    Returns:
        True if IAM dependencies were built successfully.
    """
    # IAM dependencies are built in build_secondary_lists
    return build_secondary_lists(config)


def build_s3_dependencies(config: ConfigurationManager) -> bool:
    """
    Build S3-related resource dependencies.
    
    Args:
        config: Configuration manager.
        
    Returns:
        True if S3 dependencies were built successfully.
    """
    try:
        session = config.get_aws_session()
        s3_client = session.client('s3')
        
        # Get all S3 buckets and their policies/configurations
        bucket_list = config.resources.get_s3_list()
        
        for bucket_name in bucket_list.keys():
            try:
                # Check for bucket policy
                try:
                    policy_response = s3_client.get_bucket_policy(Bucket=bucket_name)
                    config.resources.add_s3_policy_relationship(bucket_name, "has_policy")
                except s3_client.exceptions.NoSuchBucketPolicy:
                    # No policy is fine
                    pass
                
                # Check for bucket notification configuration
                try:
                    notification_response = s3_client.get_bucket_notification_configuration(
                        Bucket=bucket_name
                    )
                    if notification_response.get('LambdaConfigurations'):
                        config.resources.add_s3_lambda_relationship(bucket_name, "has_lambda_notifications")
                except Exception:
                    # No notifications is fine
                    pass
                    
            except Exception as e:
                if config.is_debug_enabled():
                    print(f"Error processing S3 bucket {bucket_name}: {e}")
                continue
        
        return True
        
    except Exception as e:
        if config.is_debug_enabled():
            print(f"Error building S3 dependencies: {e}")
        return False


def get_resource_counts(config: ConfigurationManager) -> Dict[str, int]:
    """
    Get counts of all discovered resources.
    
    Args:
        config: Configuration manager.
        
    Returns:
        Dictionary with resource type counts.
    """
    return {
        'vpcs': len(config.resources.get_vpc_list()),
        'subnets': len(config.resources.get_subnet_list()),
        'security_groups': len(config.resources.get_sg_list()),
        'lambda_functions': len(config.resources.get_lambda_list()),
        's3_buckets': len(config.resources.get_s3_list()),
        'transit_gateways': len(config.resources.get_tgw_list()),
        'iam_roles': len(config.resources.get_role_list()),
        'iam_policies': len(config.resources.get_policy_list())
    }


def print_resource_summary(config: ConfigurationManager) -> None:
    """
    Print a summary of discovered resources.
    
    Args:
        config: Configuration manager.
    """
    counts = get_resource_counts(config)
    
    print("\nResource Discovery Summary:")
    print("=" * 40)
    for resource_type, count in counts.items():
        print(f"{resource_type.replace('_', ' ').title()}: {count}")
    
    total = sum(counts.values())
    print(f"\nTotal Resources: {total}")
    
    if config.is_debug_enabled():
        print(f"\nUsing {config.get_cores()} cores for processing")
        print(f"Region: {config.aws.region}")
        print(f"Account: {config.aws.account_id}")