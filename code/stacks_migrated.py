#!/usr/bin/env python3
"""
Migrated stacks module for aws2tf that uses ConfigurationManager.

This module contains CloudFormation stack processing functions updated to use
ConfigurationManager instead of global variables while maintaining all
stack discovery and resource processing functionality.
"""

import boto3
import os
import sys
import botocore
from typing import List, Optional, Dict, Any
from .config import ConfigurationManager


def get_stacks(config: ConfigurationManager, stack_name: str) -> None:
    """
    Process CloudFormation stacks and their nested stacks.
    
    Args:
        config: Configuration manager for AWS session and processing settings.
        stack_name: Name of the CloudFormation stack to process.
    """
    session = config.get_aws_session()
    client = session.client('cloudformation')
    nested = []
    
    print(f"Level 1 stack nesting for {stack_name}")
    nested = getstack(config, stack_name, nested, client)
    
    if nested is not None:
        print("Level 2 stack nesting")
        for nest in nested:
            sn = nest.split("/")[1]
            if sn != stack_name:
                if config.is_debug_enabled():
                    print(f"Processing nested stack: {sn}")
                nested = getstack(config, sn, nested, client)
        
        print("-------------------------------------------")
        nst = len(nested)
        i = 1
        
        # Create stacks.sh file for batch processing
        with open("stacks.sh", "a") as f6:
            for nest in nested:
                sn = nest.split("/")[1]
                f6.write(f"../../aws2tf.py -t stack -i {sn}\n")
                print(f"\n############## Getting resources for stack {sn} {i} of {nst} ##############")
                getstackresources(config, nest, client)
                i = i + 1
            print(f"Stack {stack_name} done")


def getstack(config: ConfigurationManager, stack_name: str, nested: List[str], 
            client) -> Optional[List[str]]:
    """
    Get stack resources and identify nested stacks.
    
    Args:
        config: Configuration manager for debug output and region info.
        stack_name: Name of the stack to process.
        nested: List of already discovered nested stacks.
        client: CloudFormation client.
        
    Returns:
        Updated list of nested stacks, or None if error.
    """
    try:
        resp = client.describe_stack_resources(StackName=stack_name)
        response = resp['StackResources']
    
    except botocore.exceptions.ClientError as err:
        print("ValidationError error in getstack")
        print(f"Stack {stack_name} may not exist in region {config.aws.region}")
        if config.is_debug_enabled():
            print(f"ClientError details: {err}")
        return None
    
    except Exception as e:
        print(f"Unexpected error in getstack: {e}")
        if config.is_debug_enabled():
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"{exc_type}, {fname}, {exc_tb.tb_lineno}")
        return None
    
    for j in response:
        resource_type = j['ResourceType']
        status = j['ResourceStatus']
        stack_id = j['StackId']
        
        if stack_id not in str(nested):
            nested = nested + [stack_id]
        
        # Handle nested CloudFormation stacks
        if resource_type == "AWS::CloudFormation::Stack":
            if status in ["CREATE_COMPLETE", "CREATE_FAILED"]:
                if status == "CREATE_FAILED":
                    print(f"WARNING: Stack {stack_name} status is CREATE_FAILED")
                
                stack_resource = j['PhysicalResourceId']
                if stack_resource not in str(nested):
                    nested = nested + [stack_resource]
    
    return nested


def getstackresources(config: ConfigurationManager, stack_name: str, client) -> None:
    """
    Process all resources in a CloudFormation stack.
    
    Args:
        config: Configuration manager for AWS session and processing.
        stack_name: Name/ARN of the stack to process.
        client: CloudFormation client.
    """
    try:
        print(f"Getting resources for stack: {stack_name.split('/')[1]}")
        
        resp = client.describe_stack_resources(StackName=stack_name)
        response = resp['StackResources']
        
    except Exception as e:
        print(f"Unexpected error in getstackresources: {e}")
        if config.is_debug_enabled():
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"{exc_type}, {fname}, {exc_tb.tb_lineno}")
        print("exit 014")
        return
    
    ri = 0
    rl = len(response)
    
    # Open log files for tracking
    with open('stack-fetched-implicit.log', 'a') as f3, \
         open('stack-fetched-explicit.log', 'a') as f4, \
         open('stack-custom-resources.log', 'a') as f5:
        
        for j in response:
            resource_type = j['ResourceType']
            status = j['ResourceStatus']
            
            if status == "CREATE_FAILED":
                print(f"CREATE_FAILED status for {resource_type} skipping .....")
                continue
            
            physical_id = j['PhysicalResourceId'].split('/')[-1]
            physical_arn = j['PhysicalResourceId']
            logical_id = j['LogicalResourceId']
            ri = ri + 1
            
            if config.is_debug_enabled():
                print(f"type={resource_type}")
            
            sn = stack_name.split('/')[-2]
            print(f"Importing {ri} of {rl} type={resource_type} pid={physical_id}")
            
            f4.write(f"Type={resource_type} pid={physical_id} parn={physical_arn}\n")
            
            # Skip CloudFormation stacks (handled separately)
            if resource_type == "AWS::CloudFormation::Stack":
                continue
            elif "AWS::CloudFormation::WaitCondition" in resource_type:
                f3.write(f"skipping {resource_type}\n")
                continue
            
            # Process resources by type - import the common module for call_resource
            from . import common_migrated as common
            
            # Application Auto Scaling
            if resource_type == "AWS::ApplicationAutoScaling::ScalableTarget":
                common.call_resource(config, "aws_appautoscaling_target", physical_id)
            elif resource_type == "AWS::ApplicationAutoScaling::ScalingPolicy":
                common.call_resource(config, "aws_appautoscaling_policy", physical_id)
            
            # App Mesh
            elif resource_type == "AWS::AppMesh::Mesh":
                common.call_resource(config, "aws_appmesh_mesh", physical_id)
            elif resource_type == "AWS::AppMesh::VirtualGateway":
                f3.write(f"{resource_type} {physical_id} fetched as part of parent mesh\n")
            elif resource_type == "AWS::AppMesh::VirtualNode":
                f3.write(f"{resource_type} {physical_id} fetched as part of parent mesh\n")
            elif resource_type == "AWS::AppMesh::VirtualRouter":
                f3.write(f"{resource_type} {physical_id} fetched as part of parent mesh\n")
            elif resource_type == "AWS::AppMesh::VirtualService":
                f3.write(f"{resource_type} {physical_id} fetched as part of parent mesh\n")
            
            # Athena
            elif resource_type == "AWS::Athena::NamedQuery":
                common.call_resource(config, "aws_athena_named_query", physical_id)
            elif resource_type == "AWS::Athena::WorkGroup":
                common.call_resource(config, "aws_athena_workgroup", physical_id)
            
            # Auto Scaling
            elif resource_type == "AWS::AutoScaling::AutoScalingGroup":
                common.call_resource(config, "aws_autoscaling_group", physical_id)
            elif resource_type == "AWS::AutoScaling::LaunchConfiguration":
                common.call_resource(config, "aws_launch_configuration", physical_id)
            elif resource_type == "AWS::AutoScaling::LifecycleHook":
                common.call_resource(config, "aws_autoscaling_lifecycle_hook", physical_id)
            
            # CloudFront
            elif resource_type == "AWS::CloudFront::Distribution":
                common.call_resource(config, "aws_cloudfront_distribution", physical_id)
            elif resource_type == "AWS::CloudFront::OriginRequestPolicy":
                common.call_resource(config, "aws_cloudfront_origin_request_policy", physical_id)
            elif resource_type == "AWS::CloudFront::CachePolicy":
                common.call_resource(config, "aws_cloudfront_cache_policy", physical_id)
            
            # CloudWatch
            elif resource_type == "AWS::CloudWatch::Alarm":
                common.call_resource(config, "aws_cloudwatch_metric_alarm", physical_id)
            elif resource_type == "AWS::Logs::LogGroup":
                common.call_resource(config, "aws_cloudwatch_log_group", physical_id)
            
            # DynamoDB
            elif resource_type == "AWS::DynamoDB::Table":
                common.call_resource(config, "aws_dynamodb_table", physical_id)
            
            # EC2
            elif resource_type == "AWS::EC2::Instance":
                common.call_resource(config, "aws_instance", physical_id)
            elif resource_type == "AWS::EC2::VPC":
                common.call_resource(config, "aws_vpc", physical_id)
            elif resource_type == "AWS::EC2::Subnet":
                common.call_resource(config, "aws_subnet", physical_id)
            elif resource_type == "AWS::EC2::SecurityGroup":
                common.call_resource(config, "aws_security_group", physical_id)
            elif resource_type == "AWS::EC2::InternetGateway":
                common.call_resource(config, "aws_internet_gateway", physical_id)
            elif resource_type == "AWS::EC2::NatGateway":
                common.call_resource(config, "aws_nat_gateway", physical_id)
            elif resource_type == "AWS::EC2::RouteTable":
                common.call_resource(config, "aws_route_table", physical_id)
            elif resource_type == "AWS::EC2::Route":
                f3.write(f"{resource_type} {physical_id} fetched as part of route table\n")
            elif resource_type == "AWS::EC2::SubnetRouteTableAssociation":
                common.call_resource(config, "aws_route_table_association", physical_id)
            elif resource_type == "AWS::EC2::VPCEndpoint":
                common.call_resource(config, "aws_vpc_endpoint", physical_id)
            elif resource_type == "AWS::EC2::TransitGateway":
                common.call_resource(config, "aws_ec2_transit_gateway", physical_id)
            elif resource_type == "AWS::EC2::LaunchTemplate":
                common.call_resource(config, "aws_launch_template", physical_id)
            
            # ECS
            elif resource_type == "AWS::ECS::Cluster":
                common.call_resource(config, "aws_ecs_cluster", physical_id)
            elif resource_type == "AWS::ECS::Service":
                common.call_resource(config, "aws_ecs_service", physical_id)
            elif resource_type == "AWS::ECS::TaskDefinition":
                common.call_resource(config, "aws_ecs_task_definition", physical_arn)
            
            # EFS
            elif resource_type == "AWS::EFS::FileSystem":
                common.call_resource(config, "aws_efs_file_system", physical_id)
            elif resource_type == "AWS::EFS::MountTarget":
                common.call_resource(config, "aws_efs_mount_target", physical_id)
            
            # EKS
            elif resource_type == "AWS::EKS::Cluster":
                common.call_resource(config, "aws_eks_cluster", physical_id)
            elif resource_type == "AWS::EKS::Nodegroup":
                common.call_resource(config, "aws_eks_node_group", physical_id)
            elif resource_type == "AWS::EKS::FargateProfile":
                common.call_resource(config, "aws_eks_fargate_profile", physical_id)
            
            # ElastiCache
            elif resource_type == "AWS::ElastiCache::CacheCluster":
                common.call_resource(config, "aws_elasticache_cluster", physical_id)
            elif resource_type == "AWS::ElastiCache::ReplicationGroup":
                common.call_resource(config, "aws_elasticache_replication_group", physical_id)
            
            # Elastic Load Balancing
            elif resource_type == "AWS::ElasticLoadBalancingV2::LoadBalancer":
                common.call_resource(config, "aws_lb", physical_id)
            elif resource_type == "AWS::ElasticLoadBalancingV2::Listener":
                common.call_resource(config, "aws_lb_listener", physical_id)
            elif resource_type == "AWS::ElasticLoadBalancingV2::TargetGroup":
                common.call_resource(config, "aws_lb_target_group", physical_id)
            
            # IAM
            elif resource_type == "AWS::IAM::Role":
                common.call_resource(config, "aws_iam_role", physical_id)
            elif resource_type == "AWS::IAM::Policy":
                common.call_resource(config, "aws_iam_policy", physical_arn)
            elif resource_type == "AWS::IAM::User":
                common.call_resource(config, "aws_iam_user", physical_id)
            elif resource_type == "AWS::IAM::Group":
                common.call_resource(config, "aws_iam_group", physical_id)
            elif resource_type == "AWS::IAM::InstanceProfile":
                common.call_resource(config, "aws_iam_instance_profile", physical_id)
            
            # KMS
            elif resource_type == "AWS::KMS::Key":
                common.call_resource(config, "aws_kms_key", physical_id)
            elif resource_type == "AWS::KMS::Alias":
                common.call_resource(config, "aws_kms_alias", physical_id)
            
            # Lambda
            elif resource_type == "AWS::Lambda::Function":
                common.call_resource(config, "aws_lambda_function", physical_id)
            elif resource_type == "AWS::Lambda::Permission":
                common.call_resource(config, "aws_lambda_permission", physical_id)
            elif resource_type == "AWS::Lambda::EventSourceMapping":
                common.call_resource(config, "aws_lambda_event_source_mapping", physical_id)
            
            # RDS
            elif resource_type == "AWS::RDS::DBInstance":
                common.call_resource(config, "aws_db_instance", physical_id)
            elif resource_type == "AWS::RDS::DBCluster":
                common.call_resource(config, "aws_rds_cluster", physical_id)
            elif resource_type == "AWS::RDS::DBSubnetGroup":
                common.call_resource(config, "aws_db_subnet_group", physical_id)
            elif resource_type == "AWS::RDS::DBParameterGroup":
                common.call_resource(config, "aws_db_parameter_group", physical_id)
            
            # S3
            elif resource_type == "AWS::S3::Bucket":
                common.call_resource(config, "aws_s3_bucket", physical_id)
            elif resource_type == "AWS::S3::BucketPolicy":
                f3.write(f"{resource_type} {physical_id} fetched as part of bucket\n")
            
            # SNS
            elif resource_type == "AWS::SNS::Topic":
                common.call_resource(config, "aws_sns_topic", physical_arn)
            elif resource_type == "AWS::SNS::Subscription":
                common.call_resource(config, "aws_sns_topic_subscription", physical_arn)
            
            # SQS
            elif resource_type == "AWS::SQS::Queue":
                common.call_resource(config, "aws_sqs_queue", physical_arn)
            
            # SSM
            elif resource_type == "AWS::SSM::Parameter":
                common.call_resource(config, "aws_ssm_parameter", physical_id)
            
            # Custom Resources and Unsupported Types
            elif resource_type.startswith("Custom::"):
                f5.write(f"Custom resource: {resource_type} {physical_id}\n")
                if config.is_debug_enabled():
                    print(f"Skipping custom resource: {resource_type}")
            
            else:
                # Log unsupported resource types
                f3.write(f"Unsupported resource type: {resource_type} {physical_id}\n")
                if config.is_debug_enabled():
                    print(f"Unsupported resource type: {resource_type}")


def get_stack_info(config: ConfigurationManager, stack_name: str) -> Optional[Dict[str, Any]]:
    """
    Get detailed information about a CloudFormation stack.
    
    Args:
        config: Configuration manager for AWS session.
        stack_name: Name of the stack to get info for.
        
    Returns:
        Dictionary with stack information, or None if error.
    """
    try:
        session = config.get_aws_session()
        client = session.client('cloudformation')
        
        # Get stack details
        response = client.describe_stacks(StackName=stack_name)
        
        if not response['Stacks']:
            print(f"Stack {stack_name} not found")
            return None
        
        stack = response['Stacks'][0]
        
        # Get stack resources
        resources_response = client.describe_stack_resources(StackName=stack_name)
        resources = resources_response['StackResources']
        
        # Get stack events (last 10)
        events_response = client.describe_stack_events(StackName=stack_name)
        events = events_response['StackEvents'][:10]
        
        return {
            'stack': stack,
            'resources': resources,
            'events': events,
            'resource_count': len(resources)
        }
        
    except botocore.exceptions.ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == 'ValidationError':
            print(f"Stack {stack_name} does not exist in region {config.aws.region}")
        else:
            print(f"Error getting stack info: {error_code} - {e.response['Error']['Message']}")
        return None
    except Exception as e:
        print(f"Unexpected error getting stack info: {e}")
        if config.is_debug_enabled():
            import traceback
            traceback.print_exc()
        return None


def list_stacks(config: ConfigurationManager, status_filter: Optional[List[str]] = None) -> List[Dict[str, Any]]:
    """
    List all CloudFormation stacks in the region.
    
    Args:
        config: Configuration manager for AWS session.
        status_filter: Optional list of stack statuses to filter by.
        
    Returns:
        List of stack summaries.
    """
    try:
        session = config.get_aws_session()
        client = session.client('cloudformation')
        
        stacks = []
        paginator = client.get_paginator('list_stacks')
        
        # Default to active stacks if no filter provided
        if status_filter is None:
            status_filter = [
                'CREATE_COMPLETE', 'UPDATE_COMPLETE', 'UPDATE_ROLLBACK_COMPLETE',
                'IMPORT_COMPLETE', 'IMPORT_ROLLBACK_COMPLETE'
            ]
        
        for page in paginator.paginate(StackStatusFilter=status_filter):
            stacks.extend(page['StackSummaries'])
        
        return stacks
        
    except Exception as e:
        print(f"Error listing stacks: {e}")
        if config.is_debug_enabled():
            import traceback
            traceback.print_exc()
        return []


def validate_stack_template(config: ConfigurationManager, template_body: str) -> bool:
    """
    Validate a CloudFormation template.
    
    Args:
        config: Configuration manager for AWS session.
        template_body: CloudFormation template as string.
        
    Returns:
        True if template is valid.
    """
    try:
        session = config.get_aws_session()
        client = session.client('cloudformation')
        
        client.validate_template(TemplateBody=template_body)
        return True
        
    except botocore.exceptions.ClientError as e:
        print(f"Template validation error: {e.response['Error']['Message']}")
        return False
    except Exception as e:
        print(f"Error validating template: {e}")
        return False


def print_stack_summary(config: ConfigurationManager, stack_name: str) -> None:
    """
    Print a summary of a CloudFormation stack.
    
    Args:
        config: Configuration manager.
        stack_name: Name of the stack to summarize.
    """
    stack_info = get_stack_info(config, stack_name)
    
    if not stack_info:
        print(f"Could not get information for stack: {stack_name}")
        return
    
    stack = stack_info['stack']
    resources = stack_info['resources']
    
    print(f"\nStack Summary: {stack_name}")
    print("=" * 50)
    print(f"Status: {stack['StackStatus']}")
    print(f"Creation Time: {stack['CreationTime']}")
    if 'LastUpdatedTime' in stack:
        print(f"Last Updated: {stack['LastUpdatedTime']}")
    print(f"Resources: {len(resources)}")
    
    # Count resources by type
    resource_types = {}
    for resource in resources:
        res_type = resource['ResourceType']
        resource_types[res_type] = resource_types.get(res_type, 0) + 1
    
    print(f"\nResource Types:")
    for res_type, count in sorted(resource_types.items()):
        print(f"  {res_type}: {count}")
    
    # Show parameters if any
    if 'Parameters' in stack and stack['Parameters']:
        print(f"\nParameters:")
        for param in stack['Parameters']:
            print(f"  {param['ParameterKey']}: {param['ParameterValue']}")
    
    # Show outputs if any
    if 'Outputs' in stack and stack['Outputs']:
        print(f"\nOutputs:")
        for output in stack['Outputs']:
            print(f"  {output['OutputKey']}: {output['OutputValue']}")
            if 'Description' in output:
                print(f"    Description: {output['Description']}")
    
    print()  # Empty line at end