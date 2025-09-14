#!/usr/bin/env python3
"""
Migrated resources module for aws2tf that uses ConfigurationManager.

This module contains resource type definitions and AWS API metadata
updated to use ConfigurationManager instead of global variables.
"""

from typing import List, Tuple, Optional
from .config import ConfigurationManager
from fixtf_aws_resources import aws_dict


def resource_types(config: ConfigurationManager, resource_type: str) -> List[str]:
    """
    Get list of AWS resource types for a given category.
    
    Args:
        config: Configuration manager (for future extensibility).
        resource_type: Type category to get resources for.
        
    Returns:
        List of AWS resource type names.
    """
    rets = []
    
    if resource_type == "net":  # Common VPC networking resources
        rets = ["aws_vpc", "aws_vpc_dhcp_options", "aws_subnet", "aws_internet_gateway", 
                "aws_nat_gateway", "aws_route_table", "aws_route_table_association", 
                "aws_vpc_endpoint", "aws_security_group"]
        return rets
    elif resource_type == "acm":
        rets = ["aws_acm_certificate"]
        return rets  # ACM Certificates
    elif resource_type == "api" or resource_type == "apigw":
        rets = ["aws_api_gateway_rest_api"]
        return rets  # API Gateway and dependencies
    elif resource_type == "appmesh":
        rets = ["aws_appmesh_mesh"]
        return rets  # App Mesh and dependencies
    elif resource_type == "apprunner":
        rets = ["aws_apprunner_service"]
        return rets  # AppRunner resources
    elif resource_type == "appstream":
        rets = ["aws_appstream_image_builder", "aws_appstream_stack", 
                "aws_appstream_fleet", "aws_appstream_user"]
        return rets  # Appstream fleet, users etc.
    elif resource_type == "artifact":
        rets = ["aws_codeartifact_domain", "aws_codeartifact_repository"]
        return rets  # Code Artifact
    elif resource_type == "athena":
        rets = ["aws_athena_named_query", "aws_athena_data_catalog"]
        return rets  # Athena Resources
    elif resource_type == "aurora":
        rets = ["aws_rds_cluster"]
        return rets  # RDS Cluster
    elif resource_type == "autoscaling" or resource_type == "asg":
        rets = ["aws_autoscaling_group"]
        return rets  # Autoscaling Group
    elif resource_type == "bedrock":
        rets = ["aws_bedrock_guardrail", "aws_bedrockagent_agent"]
        return rets  # Bedrock resources
    elif resource_type == "batch":
        rets = ["aws_batch_compute_environment", "aws_batch_job_definition", 
                "aws_batch_scheduling_policy"]
        return rets  # AWS Batch resources
    elif resource_type == "code":
        rets = ["aws_codestarnotifications_notification_rule", "aws_codebuild_project", 
                "aws_codeartifact_domain", "aws_codeartifact_repository", 
                "aws_codecommit_repository", "aws_codepipeline"]
        return rets  # Codebuild, Code commit etc
    elif resource_type == "cloudfront" or resource_type == "cf":
        rets = ["aws_cloudfront_distribution", "aws_cloudfront_origin_request_policy", 
                "aws_cloudfront_origin_access_identity", "aws_cloudfront_origin_access_control", 
                "aws_cloudfront_cache_policy", "aws_cloudfront_function"]
        return rets  # Cloudfront Distribution
    elif resource_type == "cloudtrail" or resource_type == "ct":
        rets = ["aws_cloudtrail"]
        return rets  # CloudTrail
    elif resource_type == "cloudwan" or resource_type == "wan":
        rets = ["aws_networkmanager_global_network"]
        return rets  # CloudWAN
    elif resource_type == "cw" or resource_type == "cloudwatch" or resource_type == "logs":
        rets = ["aws_cloudwatch_log_group", "aws_cloudwatch_metric_alarm"]
        return rets  # Cloudwatch logs groups and alarms
    elif resource_type == "cloud9" or resource_type == "c9":
        rets = ["aws_cloud9_environment_ec2"]
        return rets  # Cloud9 EC2 environments
    elif resource_type == "cloudform":
        rets = ["aws_cloudformation_stack"]
        return rets  # Cloudformation stacks
    elif resource_type == "cognito":
        rets = ["aws_cognito_identity_pool", "aws_cognito_identity_pool_roles_attachment", 
                "aws_cognito_user_pool", "aws_cognito_user_pool_client"]
        return rets  # Cognito pools etc
    elif resource_type == "config":
        rets = ["aws_config_configuration_recorder", "aws_config_delivery_channel", 
                "aws_config_configuration_recorder_status", "aws_config_config_rule"]
        return rets  # Config rules, recorders etc.
    elif resource_type == "connect":
        rets = ["aws_connect_instance"]
        return rets  # Amazon Connect
    elif resource_type == "datazone" or resource_type == "dz":
        rets = ["aws_datazone_domain"]
        return rets  # Amazon DataZone
    elif resource_type == "dms":
        rets = ["aws_dms_replication_instance", "aws_dms_endpoint", "aws_dms_replication_task"]
        return rets  # DMS replication tasks and endpoints
    elif resource_type == "dynamodb":
        rets = ["aws_dynamodb_table"]
        return rets  # dynamodb tables
    elif resource_type == "eb":
        rets = ["aws_cloudwatch_event_bus"]
        return rets  # cloudwatch event bus and rules
    elif resource_type == "ec2":
        rets = ["aws_ec2_host", "aws_instance"]
        return rets  # EC2 hosts and instances
    elif resource_type == "ecr":
        rets = ["aws_ecr_repository"]
        return rets  # ECR repositories
    elif resource_type == "ecs":
        rets = ["aws_ecs_cluster"]
        return rets  # ECS clusters
    elif resource_type == "efs":
        rets = ["aws_efs_file_system"]
        return rets  # EFS filesystems
    elif resource_type == "eks":
        rets = ["aws_eks_cluster"]
        return rets  # EKS clusters
    elif resource_type == "emr":
        rets = ["aws_emr_cluster", "aws_emr_security_configuration"]
        return rets  # EMR clusters
    elif resource_type == "elasticache":
        rets = ["aws_elasticache_cluster", "aws_elasticache_serverless_cache"]
        return rets  # elasticache clusters
    elif resource_type == "glue":
        rets = ["aws_glue_crawler", "aws_glue_job", "aws_glue_connection"]
        return rets  # Glue crawlers, jobs and connections
    elif resource_type == "glue2":
        rets = ["aws_glue_catalog_table", "aws_glue_partition"]
        return rets  # Glue tables and partitions
    elif resource_type == "groups" or resource_type == "group":
        rets = ["aws_iam_group"]
        return rets  # IAM Groups
    elif resource_type == "igw":
        rets = ["aws_internet_gateway"]
        return rets  # Internet Gateways
    elif resource_type == "iam":
        rets = ["aws_iam_role", "aws_iam_policy"]
        return rets  # IAM Roles
    elif resource_type == "kendra":
        rets = ["aws_kendra_index"]
        return rets  # Kendra Indexes
    elif resource_type == "kinesis":
        rets = ["aws_kinesis_stream", "aws_kinesis_firehose_delivery_stream"]
        return rets  # Kinesis streams and firehose
    elif resource_type == "kms":
        rets = ["aws_kms_key"]
        return rets  # KMS keys
    elif resource_type == "lambda":
        rets = ["aws_lambda_function"]
        return rets  # Lambda functions and some dependencies
    elif resource_type == "lb" or resource_type == "elb":
        rets = ["aws_lb"]
        return rets  # load balancers alb/elb
    elif resource_type == "lf":
        rets = ["aws_lakeformation_data_lake_settings", "aws_lakeformation_resource", 
                "aws_lakeformation_permissions"]
        return rets  # Lake Formation
    elif resource_type == "msk":
        rets = ["aws_msk_cluster", "aws_msk_configuration"]
        return rets  # MSK Clusters and dependencies
    elif resource_type == "mwaa":
        rets = ["aws_mwaa_environment"]
        return rets  # MWAA Environment and dependencies
    elif resource_type == "natgw":
        rets = ["aws_nat_gateway"]
        return rets  # NAT gateway and dependencies
    elif resource_type == "nfw":
        rets = ["aws_networkfirewall_firewall"]
        return rets  # AWS Network Firewall
    elif resource_type == "org":
        rets = ["aws_organizations_organization", "aws_organizations_account", 
                "aws_organizations_resource_policy", "aws_organizations_policy"]
        return rets  # AWS Organizations and some dependencies
    elif resource_type == "params":
        rets = ["aws_ssm_parameter"]
        return rets  # SSM parameters
    elif resource_type == "privatelink":
        rets = ["aws_vpc_endpoint_service"]
        return rets  # VPC privatelink resources
    elif resource_type == "ram":
        rets = ["aws_ram_resource_share"]
        return rets  # RAM shares
    elif resource_type == "redshift":
        rets = ["aws_redshift_cluster", "aws_redshiftserverless_workgroup"]
        return rets  # Redshift
    elif resource_type == "route53":
        rets = ["aws_route53_zone"]
        return rets  # Route53 Zones
    elif resource_type == "rds":
        rets = ["aws_db_instance", "aws_db_parameter_group", "aws_db_event_subscription"]
        return rets  # RDS cluster and some dependencies
    elif resource_type == "s3":
        rets = ["aws_s3_bucket"]
        return rets  # AWS S3 bucket and bucket config
    elif resource_type == "s3tables":
        rets = ["aws_s3tables_table_bucket"]
        return rets  # AWS S3 tables
    elif resource_type == "subnet":
        rets = ["aws_subnet"]
        return rets  # AWS subnet and common dependencies
    elif resource_type == "sagemaker":
        rets = ["aws_sagemaker_domain", "aws_sagemaker_user_profile", "aws_sagemaker_image", 
                "aws_sagemaker_app", "aws_sagemaker_studio_lifecycle_config"]
        return rets  # SageMaker domain and dependencies
    elif resource_type == "secrets" or resource_type == "secret":
        rets = ["aws_secretsmanager_secret"]
        return rets  # secrets manager secrets
    elif resource_type == "sc":
        rets = ["aws_servicecatalog_portfolio"]
        return rets  # service catalog
    elif resource_type == "sfn":
        rets = ["aws_sfn_state_machine"]
        return rets  # State machines
    elif resource_type == "security-group":
        rets = ["aws_security_group"]
        return rets  # security group
    elif resource_type == "sns":
        rets = ["aws_sns_topic"]
        return rets  # SNS topics
    elif resource_type == "sqs":
        rets = ["aws_sqs_queue"]
        return rets  # SQS queues
    elif resource_type == "spot":
        rets = ["aws_spot_fleet_request"]
        return rets  # Spot fleet request
    elif resource_type == "ssmpatches":
        rets = ["aws_ssm_patch_baseline", "aws_ssm_default_patch_baseline"]
        return rets  # ssm patch baselines
    elif resource_type == "sso":
        rets = ["aws_ssoadmin_instances"]
        return rets  # Single sign on resources
    elif resource_type == "tgw":
        rets = ["aws_ec2_transit_gateway"]
        return rets  # Transit Gateway
    elif resource_type == "transfer":
        rets = ["aws_transfer_server"]
        return rets  # AWS Transfer family
    elif resource_type == "vpclattice" or resource_type == "lattice":
        rets = ["aws_vpclattice_service_network", "aws_vpclattice_service", 
                "aws_vpclattice_auth_policy"]
        return rets  # VPC Lattice and dependencies
    elif resource_type == "users" or resource_type == "user":
        rets = ["aws_iam_user", "aws_iam_group"]
        return rets  # IAM user and groups
    elif resource_type == "vpc":
        rets = ["aws_vpc"]
        return rets  # VPC's and its common dependencies
    elif resource_type == "waf":
        rets = ["aws_waf_web_acl"]
        return rets  # AWS WAF Classic acl's, unsupported as of September 2025
    elif resource_type == "wafv2":
        rets = ["aws_wafv2_web_acl", "aws_wafv2_ip_set", "aws_wafv2_rule_group"]
        return rets  # AWS WAF(v2) resources
    elif resource_type == "workspaces":
        rets = ["aws_workspaces_workspace"]
        return rets  # Amazon Workspaces
    elif resource_type == "all":
        keys_list = aws_dict.aws_resources.keys()
        for i in keys_list:
            rets.append(i)
        return rets
    elif resource_type == "test":
        rets = [
            "aws_api_gateway_resource", "aws_api_gateway_rest_api",
            "aws_appautoscaling_policy", "aws_appautoscaling_target",
            "aws_appmesh_gateway_route", "aws_appmesh_mesh", "aws_appmesh_route", 
            "aws_appmesh_virtual_gateway", "aws_appmesh_virtual_node", 
            "aws_appmesh_virtual_router", "aws_appmesh_virtual_service",
            "aws_appstream_fleet", "aws_appstream_image_builder", "aws_appstream_stack", 
            "aws_appstream_user", "aws_athena_named_query", "aws_athena_workgroup",
            "aws_autoscaling_group", "aws_autoscaling_lifecycle_hook",
            "aws_cloud9_environment_ec2", "aws_cloudformation_stack", 
            "aws_cloudfront_distribution", "aws_cloudtrail",
            "aws_cloudwatch_event_bus", "aws_cloudwatch_event_rule", 
            "aws_cloudwatch_event_target", "aws_cloudwatch_log_group", 
            "aws_cloudwatch_metric_alarm", "aws_codeartifact_domain", 
            "aws_codeartifact_repository", "aws_codebuild_project",
            "aws_codecommit_repository", "aws_codepipeline",
            "aws_codestarnotifications_notification_rule",
            "aws_cognito_identity_pool", "aws_cognito_identity_pool_roles_attachment",
            "aws_cognito_user_pool", "aws_cognito_user_pool_client", "aws_config_config_rule",
            "aws_config_configuration_recorder", "aws_config_configuration_recorder_status",
            "aws_config_delivery_channel", "aws_customer_gateway",
            "aws_db_event_subscription", "aws_db_instance", "aws_db_parameter_group", 
            "aws_db_subnet_group", "aws_default_network_acl",
            "aws_directory_service_directory", "aws_dms_endpoint", 
            "aws_dms_replication_instance", "aws_dms_replication_task",
            "aws_dynamodb_table", "aws_ec2_client_vpn_endpoint", 
            "aws_ec2_client_vpn_network_association", "aws_ec2_host",
            "aws_ec2_transit_gateway", "aws_ec2_transit_gateway_route", 
            "aws_ec2_transit_gateway_route_table", "aws_ec2_transit_gateway_vpc_attachment",
            "aws_ec2_transit_gateway_vpn_attachment", "aws_ecr_repository",
            "aws_ecs_capacity_provider", "aws_ecs_cluster", "aws_ecs_cluster_capacity_providers",
            "aws_ecs_service", "aws_ecs_task_definition", "aws_efs_access_point", 
            "aws_efs_file_system", "aws_efs_file_system_policy", "aws_efs_mount_target",
            "aws_eip", "aws_eks_cluster", "aws_eks_fargate_profile", 
            "aws_eks_identity_provider_config", "aws_eks_node_group",
            "aws_emr_cluster", "aws_emr_instance_group", "aws_emr_managed_scaling_policy", 
            "aws_emr_security_configuration", "aws_flow_log",
            "aws_glue_catalog_database", "aws_glue_catalog_table", "aws_glue_connection", 
            "aws_glue_crawler", "aws_glue_job", "aws_glue_partition",
            "aws_iam_access_key", "aws_iam_group", "aws_iam_instance_profile",
            "aws_iam_policy", "aws_iam_role", "aws_iam_role_policy", 
            "aws_iam_role_policy_attachment", "aws_iam_service_linked_role", 
            "aws_iam_user", "aws_iam_user_group_membership", "aws_iam_user_policy_attachment",
            "aws_instance", "aws_internet_gateway", "aws_key_pair",
            "aws_kinesis_firehose_delivery_stream", "aws_kinesis_stream",
            "aws_kms_alias", "aws_kms_key", "aws_lakeformation_data_lake_settings", 
            "aws_lakeformation_permissions", "aws_lakeformation_resource",
            "aws_lambda_alias", "aws_lambda_event_source_mapping", "aws_lambda_function", 
            "aws_lambda_function_event_invoke_config", "aws_lambda_layer_version", 
            "aws_lambda_permission", "aws_launch_configuration", "aws_launch_template",
            "aws_lb", "aws_lb_listener", "aws_lb_listener_rule", "aws_lb_target_group",
            "aws_network_acl", "aws_network_interface", "aws_organizations_account", 
            "aws_organizations_organization", "aws_organizations_organizational_unit",
            "aws_organizations_policy", "aws_organizations_policy_attachment",
            "aws_ram_principal_association", "aws_ram_resource_share",
            "aws_rds_cluster", "aws_rds_cluster_instance", "aws_rds_cluster_parameter_group",
            "aws_redshift_cluster", "aws_redshift_subnet_group"
        ]
        return rets
    else:
        # Handle single resource types that might be passed directly
        if resource_type.startswith("aws_"):
            return [resource_type]
        else:
            if config.is_debug_enabled():
                print(f"Unknown resource type: {resource_type}")
            return []


def resource_data(config: ConfigurationManager, resource_type: str, 
                 resource_id: Optional[str] = None) -> Tuple[Optional[str], Optional[str], 
                                                           Optional[str], Optional[str], 
                                                           Optional[str]]:
    """
    Get AWS API metadata for a specific resource type.
    
    Args:
        config: Configuration manager (for debug output).
        resource_type: AWS resource type (e.g., 'aws_vpc').
        resource_id: Optional resource ID for filtering logic.
        
    Returns:
        Tuple of (clfn, descfn, topkey, key, filterid) for AWS API calls.
    """
    clfn = None
    descfn = None
    topkey = None
    key = None
    filterid = None
    
    try:
        clfn = aws_dict.aws_resources[resource_type]['clfn']
    except KeyError:
        if config.is_debug_enabled():
            print(f"WARNING: may not be a Terraform resource? or it might be being "
                  f"skipped deliberately type={resource_type}")
            print("(eg. aws_network_interface is skipped)")
        return clfn, descfn, topkey, key, filterid
    
    descfn = aws_dict.aws_resources[resource_type]['descfn']
    topkey = aws_dict.aws_resources[resource_type]['topkey']
    key = aws_dict.aws_resources[resource_type]['key']
    filterid = aws_dict.aws_resources[resource_type]['filterid']
    
    if config.is_debug_enabled():
        print(f"resource_data: type={resource_type}, id={resource_id}, "
              f"clfn={clfn}, descfn={descfn}, topkey={topkey}, key={key}, filterid={filterid}")
    
    # filterid overrides - depending on what's in resource_id
    if resource_id is not None:
        if "vpc-" in resource_id:
            if resource_type == "aws_vpc_endpoint":
                filterid = "VpcId"
                return clfn, descfn, topkey, key, filterid
            elif resource_type == "aws_subnet":
                filterid = "VpcId"
                return clfn, descfn, topkey, key, filterid
            elif resource_type == "aws_security_group":
                filterid = "VpcId"
                return clfn, descfn, topkey, key, filterid
            elif resource_type == "aws_internet_gateway":
                filterid = ".Attachments.0.VpcId"
                return clfn, descfn, topkey, key, filterid
            elif resource_type == "aws_nat_gateway":
                filterid = "VpcId"
                return clfn, descfn, topkey, key, filterid
            elif resource_type == "aws_network_acl":
                filterid = "VpcId"
                return clfn, descfn, topkey, key, filterid
            elif resource_type == "aws_default_network_acl":
                filterid = "VpcId"
                return clfn, descfn, topkey, key, filterid
            elif resource_type == "aws_route_table":
                filterid = "VpcId"
                return clfn, descfn, topkey, key, filterid
            elif resource_type == "aws_route_table_association":
                filterid = ".Associations.0.VpcId"
                return clfn, descfn, topkey, key, filterid
            elif resource_type == "aws_default_route_table":
                filterid = "VpcId"
                return clfn, descfn, topkey, key, filterid
            elif resource_type == "aws_default_security_group":
                filterid = "VpcId"
                return clfn, descfn, topkey, key, filterid
            elif resource_type == "aws_default_subnet":
                filterid = "VpcId"
                return clfn, descfn, topkey, key, filterid
            elif resource_type == "aws_default_internet_gateway":
                filterid = "attachment.vpc-id"
                return clfn, descfn, topkey, key, filterid
            elif resource_type == "aws_image":
                filterid = "VpcId"
                return clfn, descfn, topkey, key, filterid
            elif resource_type == "aws_key_pair":
                filterid = "VpcId"
                return clfn, descfn, topkey, key, filterid
            elif resource_type == "aws_launch_configuration":
                filterid = "VpcId"
                return clfn, descfn, topkey, key, filterid
            elif resource_type == "aws_vpc_ipv4_cidr_block_association":
                filterid = "VpcId"
                return clfn, descfn, topkey, key, filterid
            elif resource_type == "aws_flow_log":
                filterid = "VpcId"
                return clfn, descfn, topkey, key, filterid
        
        elif "arn:aws:iam::" in resource_id:
            if resource_type == "aws_iam_role":
                filterid = "Arn"
                return clfn, descfn, topkey, key, filterid
            elif resource_type == "aws_iam_policy":
                filterid = "Arn"
                return clfn, descfn, topkey, key, filterid
            elif resource_type == "aws_iam_user":
                filterid = "Arn"
                return clfn, descfn, topkey, key, filterid
        
        elif "subnet-" in resource_id:
            if resource_type == "aws_route_table_association":
                filterid = ".Associations.0.SubnetId"
                return clfn, descfn, topkey, key, filterid
        
        elif "lt-" in resource_id:
            if resource_type == "aws_launch_template":
                filterid = "LaunchTemplateIds"
                return clfn, descfn, topkey, key, filterid
        
        # Add more ID-based filtering logic as needed...
    
    return clfn, descfn, topkey, key, filterid


# Utility functions for resource management

def get_supported_resource_types(config: ConfigurationManager) -> List[str]:
    """
    Get all supported AWS resource types.
    
    Args:
        config: Configuration manager.
        
    Returns:
        List of all supported AWS resource types.
    """
    return list(aws_dict.aws_resources.keys())


def is_resource_type_supported(config: ConfigurationManager, resource_type: str) -> bool:
    """
    Check if a resource type is supported.
    
    Args:
        config: Configuration manager.
        resource_type: AWS resource type to check.
        
    Returns:
        True if resource type is supported.
    """
    return resource_type in aws_dict.aws_resources


def get_resource_categories(config: ConfigurationManager) -> List[str]:
    """
    Get all available resource categories.
    
    Args:
        config: Configuration manager.
        
    Returns:
        List of resource category names.
    """
    categories = [
        "net", "acm", "api", "apigw", "appmesh", "apprunner", "appstream", 
        "artifact", "athena", "aurora", "autoscaling", "asg", "bedrock", 
        "batch", "code", "cloudfront", "cf", "cloudtrail", "ct", "cloudwan", 
        "wan", "cw", "cloudwatch", "logs", "cloud9", "c9", "cloudform", 
        "cognito", "config", "connect", "datazone", "dz", "dms", "dynamodb", 
        "eb", "ec2", "ecr", "ecs", "efs", "eks", "emr", "elasticache", 
        "glue", "glue2", "groups", "group", "igw", "iam", "kendra", 
        "kinesis", "kms", "lambda", "lb", "elb", "lf", "msk", "mwaa", 
        "natgw", "nfw", "org", "params", "privatelink", "ram", "redshift", 
        "route53", "rds", "s3", "s3tables", "subnet", "sagemaker", 
        "secrets", "secret", "sc", "sfn", "security-group", "sns", "sqs", 
        "spot", "ssmpatches", "sso", "tgw", "transfer", "vpclattice", 
        "lattice", "users", "user", "vpc", "waf", "wafv2", "workspaces", 
        "all", "test"
    ]
    return categories


def validate_resource_type_category(config: ConfigurationManager, category: str) -> bool:
    """
    Validate if a resource type category is valid.
    
    Args:
        config: Configuration manager.
        category: Resource category to validate.
        
    Returns:
        True if category is valid.
    """
    valid_categories = get_resource_categories(config)
    return category in valid_categories