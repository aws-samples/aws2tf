# provider version 5.31.0 - January 2024
#
aws_vpc = {
	"clfn":		"ec2",
	"descfn":	"describe_vpcs",
	"topkey":	"Vpcs",
	"key":		"VpcId",
	"filterid":	"VpcId"
}

aws_vpc_ipv4_cidr_block_association = {
	"clfn":		"ec2",
	"descfn":	"describe_vpcs",
	"topkey":	"Vpcs",
	"key":		"AssociationId",
	"filterid":	"AssociationId"
}

aws_vpc_endpoint = {
	"clfn":		"ec2",
	"descfn":	"describe_vpc_endpoints",
	"topkey":	"VpcEndpoints",
	"key":		"VpcEndpointId",
	"filterid":	"VpcEndpointId"
}

aws_subnet = {
	"clfn":		"ec2",
	"descfn":	"describe_subnets",
	"topkey":	"Subnets",
	"key":		"SubnetId",
	"filterid":	"SubnetId"
}

aws_security_group = {
	"clfn":		"ec2",
	"descfn":	"describe_security_groups",
	"topkey":	"SecurityGroups",
	"key":		"GroupId",
	"filterid":	"GroupId"
}

aws_internet_gateway = {
	"clfn":		"ec2",
	"descfn":	"describe_internet_gateways",
	"topkey":	"InternetGateways",
	"key":		"InternetGatewayId",
	"filterid":	"InternetGatewayId"
}

aws_nat_gateway = {
	"clfn":		"ec2",
	"descfn":	"describe_nat_gateways",
	"topkey":	"NatGateways",
	"key":		"NatGatewayId",
	"filterid":	"NatGatewayId"
}

aws_network_acl = {
	"clfn":		"ec2",
	"descfn":	"describe_network_acls",
	"topkey":	"NetworkAcls",
	"key":		"NetworkAclId",
	"filterid":	"NetworkAclId"
}

aws_default_network_acl = {
	"clfn":		"ec2",
	"descfn":	"describe_network_acls",
	"topkey":	"NetworkAcls",
	"key":		"NetworkAclId",
	"filterid":	"NetworkAclId"
}

aws_route_table = {
	"clfn":		"ec2",
	"descfn":	"describe_route_tables",
	"topkey":	"RouteTables",
	"key":		"RouteTableId",
	"filterid":	"RouteTableId"
}

aws_route_table_association = {
	"clfn":		"ec2",
	"descfn":	"describe_route_tables",
	"topkey":	"RouteTables",
	"key":		".Associations.0.SubnetId",
	"filterid":	".Associations.0.SubnetId"
}

aws_default_route_table = {
	"clfn":		"ec2",
	"descfn":	"describe_route_tables",
	"topkey":	"RouteTables",
	"key":		"RouteTableId",
	"filterid":	"RouteTableId"
}

aws_default_security_group = {
	"clfn":		"ec2",
	"descfn":	"describe_security_groups",
	"topkey":	"SecurityGroups",
	"key":		"GroupId",
	"filterid":	"GroupId"
}


aws_vpc_dhcp_options = {
	"clfn":		"ec2",
	"descfn":	"describe_dhcp_options",
	"topkey":	"DhcpOptions",
	"key":		"DhcpOptionsId",
	"filterid":	""
}

aws_key_pair = {
	"clfn":		"ec2",
	"descfn":	"describe_key_pairs",
	"topkey":	"KeyPairs",
	"key":		"KeyName",
	"filterid":	"KeyName"
}

aws_launch_configuration = {
	"clfn":		"autoscaling",
	"descfn":	"describe_launch_configurations",
	"topkey":	"LaunchConfigurations",
	"key":		"LaunchConfigurationName",
	"filterid":	"LaunchConfigurationName"
}

aws_launch_template = {
	"clfn":		"ec2",
	"descfn":	"describe_launch_templates",
	"topkey":	"LaunchTemplates",
	"key":		"LaunchTemplateIds",
	"filterid":	"LaunchTemplateNames"
}

aws_flow_log = {
	"clfn":		"ec2",
	"descfn":	"describe_flow_logs",
	"topkey":	"FlowLogs",
	"key":		"FlowLogId",
	"filterid":	"FlowLogId"
}

aws_iam_role = {
	"clfn":		"iam",
	"descfn":	"list_roles",
	"topkey":	"Roles",
	"key":		"RoleName",
	"filterid":	"RoleName"
}

aws_iam_policy = {
	"clfn":		"iam",
	"descfn":	"list_policies",
	"topkey":	"Policies",
	"key":		"PolicyName",
	"filterid":	"PolicyName"
}

aws_iam_role_policy = {
	"clfn":		"iam",
	"descfn":	"list_role_policies",
	"topkey":	"PolicyNames",
	"key":		"PolicyNames",
	"filterid":	"RoleName"
}

aws_iam_role_policy_attachment = {
	"clfn":		"iam",
	"descfn":	"list_attached_role_policies",
	"topkey":	"AttachedPolicies",
	"key":		"PolicyName",
	"filterid":	"RoleName"
}

aws_iam_user = {
	"clfn":		"iam",
	"descfn":	"list_users",
	"topkey":	"Users",
	"key":		"UserName",
	"filterid":	"UserName"
}

aws_iam_instance_profile = {
	"clfn":		"iam",
	"descfn":	"get_instance_profile",
	"topkey":	"InstanceProfile",
	"key":		"InstanceProfileName",
	"filterid":	"InstanceProfileName"
}

aws_vpclattice_access_log_subscription = {
	"clfn":		"vpc-lattice",
	"descfn":	"list_access_log_subscriptions",
	"topkey":	"items",
	"key":		"id",
	"filterid":	"name"
}

aws_vpclattice_auth_policy = {
	"clfn":		"vpc-lattice",
	"descfn":	"get_auth_policy",
	"topkey":	"items",
	"key":		"id",
	"filterid":	"id"
}

aws_vpclattice_listener = {
	"clfn":		"vpc-lattice",
	"descfn":	"list_listeners",
	"topkey":	"items",
	"key":		"id",
	"filterid":	"name"
}

aws_vpclattice_listener_rule = {
	"clfn":		"vpc-lattice",
	"descfn":	"list_rules",
	"topkey":	"items",
	"key":		"id",
	"filterid":	"name"
}

aws_vpclattice_resource_policy = {
	"clfn":		"vpc-lattice",
	"descfn":	"get_resource_policy",
	"topkey":	"policy",
	"key":		"resourceArn",
	"filterid":	"resourceArn"
}

aws_vpclattice_service = {
	"clfn":		"vpc-lattice",
	"descfn":	"list_services",
	"topkey":	"items",
	"key":		"id",
	"filterid":	"name"  # no filter on list-users so use jq like filter"
}

aws_vpclattice_service_network = {
	"clfn":		"vpc-lattice",
	"descfn":	"list_service_networks",
	"topkey":	"items",
	"key":		"id",
	"filterid":	"name"
}

aws_vpclattice_service_network_service_association = {
	"clfn":		"vpc-lattice",
	"descfn":	"list_service_network_service_associations",
	"topkey":	"items",
	"key":		"id",
	"filterid":	"name"
}

aws_vpclattice_service_network_vpc_association = {
	"clfn":		"vpc-lattice",
	"descfn":	"list_service_network_vpc_associations",
	"topkey":	"items",
	"key":		"id",
	"filterid":	"name"
}

aws_vpclattice_target_group = {
	"clfn":		"vpc-lattice",
	"descfn":	"list_target_groups",
	"topkey":	"items",
	"key":		"id",
	"filterid":	"name"
}

aws_eks_access_entry = {
  	"clfn":		"eks",
	"descfn":	"list_access_entries",  
    "topkey":	"accessEntries",
	"key":		"clusterName",
	"filterid":	"clusterName"
}

aws_eks_access_policy_association = {
    "clfn":		"eks",
	"descfn":	"list_access_policies",  
    "topkey":	"accessPolicies",
	"key":		"name",
	"filterid":	"arn" 

}

aws_eks_cluster = {
	"clfn":		"eks",
	"descfn":	"list_clusters",
	"topkey":	"clusters",
	"key":		"name",
	"filterid":	"name"
}

aws_eks_fargate_profile = {
	"clfn":		"eks",
	"descfn":	"list_fargate_profiles",
	"topkey":	"fargateProfileNames",
	"key":		"clusterName",
	"filterid":	"clusterName"
}

aws_eks_node_group = {
	"clfn":		"eks",
	"descfn":	"list_nodegroups",
	"topkey":	"nodegroups",
	"key":		"clusterName",
	"filterid":	"clusterName"
}

aws_eks_addon = {
	"clfn":		"eks",
	"descfn":	"list_addons",
	"topkey":	"addons",
	"key":		"clusterName",
	"filterid":	"clusterName"
}

aws_eks_identity_provider_config = {
	"clfn":		"eks",
	"descfn":	"list_identity_provider_configs",
	"topkey":	"identityProviderConfigs",
	"key":		"clusterName",
	"filterid":	"clusterName"
}

aws_kms_key = {
	"clfn":		"kms",
	"descfn":	"list_keys",
	"topkey":	"Keys",
	"key":		"KeyId",
	"filterid":	"KeyArn"
}

aws_kms_alias = {
	"clfn":		"kms",
	"descfn":	"list_aliases",
	"topkey":	"Aliases",
	"key":		"TargetKeyId",
	"filterid":	"AliasName"
}

aws_ecs_cluster = {
	"clfn":		"ecs",
	"descfn":	"list_clusters",
	"topkey":	"clusterArns",
	"key":		"cluster",
	"filterid":	"clusterArn"
}

aws_cloudwatch_log_group = {
	"clfn":		"logs",
	"descfn":	"describe_log_groups",
	"topkey":	"logGroups",
	"key":		"logGroupName",
	"filterid":	"logGroupName"
}

aws_config_config_rule = {
	"clfn":		"config",
	"descfn":	"describe_config_rules",
	"topkey":	"ConfigRules",
	"key":		"ConfigRuleName",
	"filterid":	"ConfigRuleName"
}

aws_instance = {
	"clfn":		"ec2",
	"descfn":	"describe_instances",
	"topkey":	"Reservations",
	"key":		"InstanceId",
	"filterid":	"InstanceId"
}

aws_lambda_function = {
	"clfn":		"lambda",
	"descfn":	"list_functions",
	"topkey":	"Functions",
	"key":		"FunctionName",
	"filterid":	"FunctionName"
}

aws_lambda_alias = {
	"clfn":		"lambda",
	"descfn":	"list_aliases",
	"topkey":	"Aliases",
	"key":		"FunctionName",
	"filterid":	"FunctionName"
}

aws_lambda_permission = {
	"clfn":		"lambda",
	"descfn":	"get_policy",
	"topkey":	"Policy",
	"key":		"FunctionName",
	"filterid":	"FunctionName"
}

aws_lambda_layer_version = {
	"clfn":		"lambda",
	"descfn":	"list_layer_versions",
	"topkey":	"LayerVersions",
	"key":		"LayerName",
	"filterid":	"LayerName"
}

aws_lambda_function_event_invoke_config = {
	"clfn":		"lambda",
	"descfn":	"list_function_event_invoke_configs",
	"topkey":	"FunctionEventInvokeConfigs",
	"key":		"FunctionName",
	"filterid":	"FunctionName"
}

aws_lambda_event_source_mapping = {
	"clfn":		"lambda",
	"descfn":	"list_event_source_mappings",
	"topkey":	"EventSourceMappings",
	"key":		"FunctionName",
	"filterid":	"FunctionName"
}

aws_lb = {
	"clfn":		"elbv2",
	"descfn":	"describe_load_balancers",
	"topkey":	"LoadBalancers",
	"key":		"LoadBalancerArn",
	"filterid":	"Names"
}

aws_redshiftserverless_workgroup = {
	"clfn":		"redshift-serverless",
	"descfn":	"get_workgroup",
	"topkey":	"workgroup",
	"key":		"workgroupName",
	"filterid":	"workgroupName"
}

aws_redshiftserverless_namespace = {
	"clfn":		"redshift-serverless",
	"descfn":	"get_namespace",
	"topkey":	"namespace",
	"key":		"namespaceName",
	"filterid":	"namespaceName"
}

aws_redshift_cluster = {
	"clfn":		"redshift",
	"descfn":	"describe_clusters",
	"topkey":	"Clusters",
	"key":		"ClusterIdentifier",
	"filterid":	"ClusterIdentifier"
}

aws_redshift_subnet_group = {
	"clfn":		"redshift",
	"descfn":	"describe_cluster_subnet_groups",
	"topkey":	"ClusterSubnetGroups",
	"key":		"ClusterSubnetGroupName",
	"filterid":	"ClusterSubnetGroupName"
}

aws_redshift_parameter_group = {
	"clfn":		"redshift",
	"descfn":	"describe_cluster_parameter_groups",
	"topkey":	"ParameterGroups",
	"key":		"ParameterGroupName",
	"filterid":	"ParameterGroupName"
}

aws_rds_cluster = {
	"clfn":		"rds",
	"descfn":	"describe_db_clusters",
	"topkey":	"DBClusters",
	"key":		"DBClusterIdentifier",
	"filterid":	"DBClusterIdentifier"
}

aws_rds_cluster_parameter_group = {
	"clfn":		"rds",
	"descfn":	"describe_db_cluster_parameter_groups",
	"topkey":	"DBClusterParameterGroups",
	"key":		"DBClusterParameterGroupName",
	"filterid":	"DBClusterParameterGroupName"
}

aws_rds_cluster_instance = {
	"clfn":		"rds",
	"descfn":	"describe_db_instances",
	"topkey":	"DBInstances",
	"key":		"DBInstanceIdentifier",
	"filterid":	"DBInstanceIdentifier"
}

aws_db_parameter_group = {
	"clfn":		"rds",
	"descfn":	"describe_db_parameter_groups",
	"topkey":	"DBParameterGroups",
	"key":		"DBParameterGroupName",
	"filterid":	"DBParameterGroupName"
}

aws_db_subnet_group = {
	"clfn":		"rds",
	"descfn":	"describe_db_subnet_groups",
	"topkey":	"DBSubnetGroups",
	"key":		"DBSubnetGroupName",
	"filterid":	"DBSubnetGroupName"
}

aws_db_instance = {
	"clfn":		"rds",
	"descfn":	"describe_db_instances",
	"topkey":	"DBInstances",
	"key":		"DBInstanceIdentifier",
	"filterid":	"DBInstanceIdentifier"
}

aws_db_event_subscription = {
	"clfn":		"rds",
	"descfn":	"describe_event_subscriptions",
	"topkey":	"EventSubscriptionsList",
	"key":		"SubscriptionName",
	"filterid":	"SubscriptionName"
}

aws_glue_crawler = {
	"clfn":		"glue",
	"descfn":	"get_crawlers",
	"topkey":	"Crawlers",
	"key":		"Name",
	"filterid":	"Name"
}

aws_glue_catalog_database = {
	"clfn":		"glue",
	"descfn":	"get_databases",
	"topkey":	"DatabaseList",
	"key":		"Name",
	"filterid":	"Name"
}

aws_kinesis_stream = {
	"clfn":		"kinesis",
	"descfn":	"list_streams",
	"topkey":	"StreamSummaries",
	"key":		"StreamName",
	"filterid":	"StreamName"
}

aws_secretsmanager_secret = {
	"clfn":		"secretsmanager",
	"descfn":	"list_secrets",
	"topkey":	"SecretList",
	"key":		"ARN",
	"filterid":	"ARN"
}

aws_cloudwatch_event_rule = {
	"clfn":		"events",
	"descfn":	"list_rules",
	"topkey":	"Rules",
	"key":		"Name",
	"filterid":	"Name"
}

aws_accessanalyzer_analyzer = {
	"clfn":		"accessanalyzer",
	"descfn":	"list_analyzers",
	"topkey":	"analyzers",
	"key":		"name",
	"filterid":	"name"
}

aws_accessanalyzer_archive_rule = {
	"clfn":		"accessanalyzer",
	"descfn":	"list_archive_rules",
	"topkey":	"archiveRules",
	"key":		"ruleName",
	"filterid":	"ruleName"
}

aws_account_alternate_contact = {
	"clfn":		"organizations",
	"descfn":	"describe_account",
	"topkey":	"Account",
	"key":		"Id",
	"filterid":	"Id"
}

aws_account_primary_contact = {
	"clfn":		"organizations",
	"descfn":	"describe_account",
	"topkey":	"Account",
	"key":		"Id",
	"filterid":	"Id"
}

aws_acm_certificate = {
	"clfn":		"acm",
	"descfn":	"list_certificates",
	"topkey":	"CertificateSummaryList",
	"key":		"CertificateArn",
	"filterid":	"CertificateArn"
}


aws_acm_certificate_validation = {
	"clfn":		"acm",
	"descfn":	"list_certificates",
	"topkey":	"CertificateSummaryList",
	"key":		"CertificateArn",
	"filterid":	"CertificateArn"
}

aws_acmpca_certificate = {
	"clfn":		"acm-pca",
	"descfn":	"get_certificate",
	"topkey":	"CertificateAuthorityList",
	"key":		"Certificate",
	"filterid":	"Arn"
}

aws_acmpca_certificate_authority = {
	"clfn":		"acm-pca",
	"descfn":	"list_certificate_authorities",
	"topkey":	"CertificateAuthorities",
	"key":		"Arn",
	"filterid":	"Arn"
}

aws_acmpca_certificate_authority_certificate = {
	"clfn":		"acm-pca",
	"descfn":	"list_certificate_authorities",
	"topkey":	"CertificateAuthorities",
	"key":		"Arn",
	"filterid":	"Arn"
}

aws_acmpca_permission = {
	"clfn":		"acm-pca",
	"descfn":	"list_permissions",
	"topkey":	"Permissions",
	"key":		"Permission",
	"filterid":	"Permission"
}

aws_acmpca_policy = {
	"clfn":		"acm-pca",
	"descfn":	"get_policy",
	"topkey":	"Policy",
	"key":		"ResourceArn",
	"filterid":	"ResourceArn"
}

aws_ami = {
	"clfn":		"ec2",
	"descfn":	"describe_images",
	"topkey":	"Images",
	"key":		"ImageId",
	"filterid":	"ImageId"
}

aws_ami_copy = {
	"clfn":		"ec2",
	"descfn":	"describe_images",
	"topkey":	"Images",
	"key":		"ImageId",
	"filterid":	"ImageId"
}

aws_ami_from_instance = {
	"clfn":		"ec2",
	"descfn":	"describe_images",
	"topkey":	"Images",
	"key":		"ImageId",
	"filterid":	"ImageId"
}

aws_ami_launch_permission = {
	"clfn":		"ec2",
	"descfn":	"describe_images",
	"topkey":	"Images",
	"key":		"ImageId",
	"filterid":	"ImageId"
}

aws_amplify_app = {
	"clfn":		"amplify",
	"descfn":	"list_apps",
	"topkey":	"apps",
	"key":		"appId",
	"filterid":	"appId"
}

aws_amplify_backend_environment = {
	"clfn":		"amplify",
	"descfn":	"list_backend_environments",
	"topkey":	"backendEnvironments",
	"key":		"environmentName",
	"filterid":	"environmentName"
}

aws_amplify_branch = {
	"clfn":		"amplify",
	"descfn":	"list_branches",
	"topkey":	"branches",
	"key":		"branchName",
	"filterid":	"branchName"
}

aws_amplify_domain_association = {
	"clfn":		"amplify",
	"descfn":	"list_domain_associations",
	"topkey":	"domainAssociations",
	"key":		"domainName",
	"filterid":	"domainName"
}

aws_amplify_webhook = {
	"clfn":		"amplify",
	"descfn":	"list_webhooks",
	"topkey":	"webhooks",
	"key":		"webhookName",
	"filterid":	"webhookName"
}

aws_api_gateway_account = {
	"clfn":		"apigateway",
	"descfn":	"get_account",
	"topkey":	"account",
	"key":		"cloudwatchRoleArn",
	"filterid":	"cloudwatchRoleArn"
}

aws_api_gateway_api_key = {
	"clfn":		"apigateway",
	"descfn":	"get_api_keys",
	"topkey":	"items",
	"key":		"id",
	"filterid":	"id"
}

aws_api_gateway_authorizer = {
	"clfn":		"apigateway",
	"descfn":	"get_authorizers",
	"topkey":	"items",
	"key":		"id",
	"filterid":	"id"
}

aws_api_gateway_base_path_mapping = {
	"clfn":		"apigateway",
	"descfn":	"get_base_path_mappings",
	"topkey":	"items",
	"key":		"id",
	"filterid":	"id"
}

aws_api_gateway_client_certificate = {
	"clfn":		"apigateway",
	"descfn":	"get_client_certificates",
	"topkey":	"items",
	"key":		"clientCertificateId",
	"filterid":	"clientCertificateId"
}

aws_api_gateway_deployment = {
	"clfn":		"apigateway",
	"descfn":	"get_deployments",
	"topkey":	"items",
	"key":		"id",
	"filterid":	"id"
}

aws_api_gateway_documentation_part = {
	"clfn":		"apigateway",
	"descfn":	"get_documentation_parts",
	"topkey":	"items",
	"key":		"id",
	"filterid":	"id"
}

aws_api_gateway_documentation_version = {
	"clfn":		"apigateway",
	"descfn":	"get_documentation_versions",
	"topkey":	"items",
	"key":		"version",
	"filterid":	"version"
}

aws_api_gateway_domain_name = {
	"clfn":		"apigateway",
	"descfn":	"get_domain_names",
	"topkey":	"items",
	"key":		"domainName",
	"filterid":	"domainName"
}

aws_api_gateway_gateway_response = {
	"clfn":		"apigateway",
	"descfn":	"get_gateway_responses",
	"topkey":	"items",
	"key":		"responseType",
	"filterid":	"responseType"
}

aws_api_gateway_integration = {
	"clfn":		"apigateway",
	"descfn":	"get_integration",
	"topkey":	"items",
	"key":		"restApiId",
	"filterid":	"restApiId"
}

aws_api_gateway_integration_response = {
	"clfn":		"apigateway",
	"descfn":	"get_integration_responses",
	"topkey":	"items",
	"key":		"id",
	"filterid":	"id"
}

aws_api_gateway_method = {
	"clfn":		"apigateway",
	"descfn":	"get_methods",
	"topkey":	"items",
	"key":		"httpMethod",
	"filterid":	"httpMethod"
}

aws_api_gateway_method_response = {
	"clfn":		"apigateway",
	"descfn":	"get_method_responses",
	"topkey":	"items",
	"key":		"httpMethod",
	"filterid":	"httpMethod"
}

aws_api_gateway_method_settings = {
	"clfn":		"apigateway",
	"descfn":	"get_method_settings",
	"topkey":	"items",
	"key":		"httpMethod",
	"filterid":	"httpMethod"
}

aws_api_gateway_model = {
	"clfn":		"apigateway",
	"descfn":	"get_models",
	"topkey":	"items",
	"key":		"id",
	"filterid":	"id"
}

aws_api_gateway_request_validator = {
	"clfn":		"apigateway",
	"descfn":	"get_request_validators",
	"topkey":	"items",
	"key":		"id",
	"filterid":	"id"
}

aws_api_gateway_resource = {
	"clfn":		"apigateway",
	"descfn":	"get_resources",
	"topkey":	"items",
	"key":		"id",
	"filterid":	"id"
}

aws_api_gateway_rest_api = {
	"clfn":		"apigateway",
	"descfn":	"get_rest_apis",
	"topkey":	"items",
	"key":		"id",
	"filterid":	"id"
}

aws_api_gateway_rest_api_policy = {
	"clfn":		"apigateway",
	"descfn":	"get_rest_api_policy",
	"topkey":	"policy",
	"key":		"id",
	"filterid":	"id"
}

aws_api_gateway_stage = {
	"clfn":		"apigateway",
	"descfn":	"get_stages",
	"topkey":	"items",
	"key":		"stageName",
	"filterid":	"stageName"
}

aws_api_gateway_usage_plan = {
	"clfn":		"apigateway",
	"descfn":	"get_usage_plans",
	"topkey":	"items",
	"key":		"id",
	"filterid":	"id"
}

aws_api_gateway_usage_plan_key = {
	"clfn":		"apigateway",
	"descfn":	"get_usage_plan_keys",
	"topkey":	"items",
	"key":		"id",
	"filterid":	"id"
}

aws_api_gateway_vpc_link = {
	"clfn":		"apigateway",
	"descfn":	"get_vpc_links",
	"topkey":	"items",
	"key":		"id",
	"filterid":	"id"
}

aws_apigatewayv2_api = {
	"clfn":		"apigatewayv2",
	"descfn":	"get_apis",
	"topkey":	"Items",
	"key":		"ApiId",
	"filterid":	"ApiId"
}

aws_apigatewayv2_api_mapping = {
	"clfn":		"apigatewayv2",
	"descfn":	"get_api_mappings",
	"topkey":	"Items",
	"key":		"ApiMappingId",
	"filterid":	"ApiMappingId"
}

aws_apigatewayv2_authorizer = {
	"clfn":		"apigatewayv2",
	"descfn":	"get_authorizers",
	"topkey":	"Items",
	"key":		"AuthorizerId",
	"filterid":	"AuthorizerId"
}

aws_apigatewayv2_deployment = {
	"clfn":		"apigatewayv2",
	"descfn":	"get_deployments",
	"topkey":	"Items",
	"key":		"DeploymentId",
	"filterid":	"DeploymentId"
}

aws_apigatewayv2_domain_name = {
	"clfn":		"apigatewayv2",
	"descfn":	"get_domain_names",
	"topkey":	"Items",
	"key":		"DomainNameId",
	"filterid":	"DomainNameId"
}

aws_apigatewayv2_integration = {
	"clfn":		"apigatewayv2",
	"descfn":	"get_integrations",
	"topkey":	"Items",
	"key":		"IntegrationId",
	"filterid":	"IntegrationId"
}

aws_apigatewayv2_integration_response = {
	"clfn":		"apigatewayv2",
	"descfn":	"get_integration_responses",
	"topkey":	"Items",
	"key":		"IntegrationResponseId",
	"filterid":	"IntegrationResponseId"
}

aws_apigatewayv2_model = {
	"clfn":		"apigatewayv2",
	"descfn":	"get_models",
	"topkey":	"Items",
	"key":		"ModelId",
	"filterid":	"ModelId"
}

aws_apigatewayv2_route = {
	"clfn":		"apigatewayv2",
	"descfn":	"get_routes",
	"topkey":	"Items",
	"key":		"RouteId",
	"filterid":	"RouteId"
}

aws_apigatewayv2_route_response = {
	"clfn":		"apigatewayv2",
	"descfn":	"get_route_responses",
	"topkey":	"Items",
	"key":		"RouteResponseId",
	"filterid":	"RouteResponseId"
}

aws_apigatewayv2_stage = {
	"clfn":		"apigatewayv2",
	"descfn":	"get_stages",
	"topkey":	"Items",
	"key":		"StageName",
	"filterid":	"StageName"
}

aws_apigatewayv2_vpc_link = {
	"clfn":		"apigatewayv2",
	"descfn":	"get_vpc_links",
	"topkey":	"Items",
	"key":		"VpcLinkId",
	"filterid":	"VpcLinkId"
}

aws_app_cookie_stickiness_policy = {
	"clfn":		"elb",
	"descfn":	"describe_load_balancers",
	"topkey":	"LoadBalancerDescriptions",
	"key":		"AppCookieStickinessPolicyNames",
	"filterid":	"AppCookieStickinessPolicyNames"
}

aws_appautoscaling_policy = {
	"clfn":		"application-autoscaling",
	"descfn":	"describe_scaling_policies",
	"topkey":	"ScalingPolicies",
	"key":		"PolicyName",
	"filterid":	"PolicyName"
}

aws_appautoscaling_scheduled_action = {
	"clfn":		"application-autoscaling",
	"descfn":	"describe_scheduled_actions",
	"topkey":	"ScheduledActions",
	"key":		"ScheduledActionName",
	"filterid":	"ScheduledActionName"
}

aws_appautoscaling_target = {
	"clfn":		"application-autoscaling",
	"descfn":	"describe_scalable_targets",
	"topkey":	"ScalableTargets",
	"key":		"ResourceId",
	"filterid":	"ResourceId"
}

aws_appconfig_application = {
	"clfn":		"appconfig",
	"descfn":	"list_applications",
	"topkey":	"Items",
	"key":		"Id",
	"filterid":	"Id"
}

aws_appconfig_configuration_profile = {
	"clfn":		"appconfig",
	"descfn":	"list_configuration_profiles",
	"topkey":	"Items",
	"key":		"Id",
	"filterid":	"Id"
}

aws_appconfig_deployment = {
	"clfn":		"appconfig",
	"descfn":	"list_deployments",
	"topkey":	"Items",
	"key":		"Id",
	"filterid":	"Id"
}

aws_appconfig_deployment_strategy = {
	"clfn":		"appconfig",
	"descfn":	"list_deployment_strategies",
	"topkey":	"Items",
	"key":		"Id",
	"filterid":	"Id"
}

aws_appconfig_environment = {
	"clfn":		"appconfig",
	"descfn":	"list_environments",
	"topkey":	"Items",
	"key":		"Id",
	"filterid":	"Id"
}

aws_appconfig_extension_association = {
	"clfn":		"appconfig",
	"descfn":	"list_extension_associations",
	"topkey":	"Items",
	"key":		"Id",
	"filterid":	"Id"
}

aws_appconfig_hosted_configuration_version = {
	"clfn":		"appconfig",
	"descfn":	"list_hosted_configuration_versions",
	"topkey":	"Items",
	"key":		"Id",
	"filterid":	"Id"
}

aws_appflow_connector_profile = {
	"clfn":		"appflow",
	"descfn":	"list_connector_profiles",
	"topkey":	"ConnectorProfileDetailsList",
	"key":		"ConnectorProfileName",
	"filterid":	"ConnectorProfileName"
}

aws_appflow_flow = {
	"clfn":		"appflow",
	"descfn":	"list_flows",
	"topkey":	"Flows",
	"key":		"FlowName",
	"filterid":	"FlowName"
}

aws_appintegrations_data_integration = {
	"clfn":		"appintegrations",
	"descfn":	"list_data_integrations",
	"topkey":	"DataIntegrations",
	"key":		"Name",
	"filterid":	"Name"
}

aws_appintegrations_event_integration = {
	"clfn":		"appintegrations",
	"descfn":	"list_event_integrations",
	"topkey":	"EventIntegrations",
	"key":		"Name",
	"filterid":	"Name"
}

aws_applicationinsights_application = {
	"clfn":		"application-insights",
	"descfn":	"list_applications",
	"topkey":	"ApplicationInfoList",
	"key":		"Name",
	"filterid":	"Name"
}

aws_appmesh_gateway_route = {
	"clfn":		"appmesh",
	"descfn":	"list_gateway_routes",
	"topkey":	"GatewayRoutes",
	"key":		"GatewayRouteName",
	"filterid":	"GatewayRouteName"
}

aws_appmesh_mesh = {
	"clfn":		"appmesh",
	"descfn":	"list_meshes",
	"topkey":	"Meshes",
	"key":		"MeshName",
	"filterid":	"MeshName"
}

aws_appmesh_route = {
	"clfn":		"appmesh",
	"descfn":	"list_routes",
	"topkey":	"Routes",
	"key":		"RouteName",
	"filterid":	"RouteName"
}

aws_appmesh_virtual_gateway = {
	"clfn":		"appmesh",
	"descfn":	"list_virtual_gateways",
	"topkey":	"VirtualGateways",
	"key":		"VirtualGatewayName",
	"filterid":	"VirtualGatewayName"
}

aws_appmesh_virtual_node = {
	"clfn":		"appmesh",
	"descfn":	"list_virtual_nodes",
	"topkey":	"VirtualNodes",
	"key":		"VirtualNodeName",
	"filterid":	"VirtualNodeName"
}

aws_appmesh_virtual_router = {
	"clfn":		"appmesh",
	"descfn":	"list_virtual_routers",
	"topkey":	"VirtualRouters",
	"key":		"VirtualRouterName",
	"filterid":	"VirtualRouterName"
}

aws_appmesh_virtual_service = {
	"clfn":		"appmesh",
	"descfn":	"list_virtual_services",
	"topkey":	"VirtualServices",
	"key":		"VirtualServiceName",
	"filterid":	"VirtualServiceName"
}

aws_apprunner_auto_scaling_configuration_version = {
	"clfn":		"apprunner",
	"descfn":	"list_auto_scaling_configuration_versions",
	"topkey":	"AutoScalingConfigurationVersions",
	"key":		"AutoScalingConfigurationVersionArn",
	"filterid":	"AutoScalingConfigurationVersionArn"
}

aws_apprunner_connection = {
	"clfn":		"apprunner",
	"descfn":	"list_connections",
	"topkey":	"Connections",
	"key":		"ConnectionArn",
	"filterid":	"ConnectionArn"
}

aws_apprunner_custom_domain_association = {
	"clfn":		"apprunner",
	"descfn":	"list_custom_domain_associations",
	"topkey":	"CustomDomainAssociations",
	"key":		"CustomDomainAssociationArn",
	"filterid":	"CustomDomainAssociationArn"
}

aws_apprunner_default_auto_scaling_configuration_version = {
	"clfn":		"apprunner",
	"descfn":	"list_default_auto_scaling_configurations",
	"topkey":	"DefaultAutoScalingConfigurations",
	"key":		"DefaultAutoScalingConfigurationArn",
	"filterid":	"DefaultAutoScalingConfigurationArn"
}

aws_apprunner_observability_configuration = {
	"clfn":		"apprunner",
	"descfn":	"list_observability_configurations",
	"topkey":	"ObservabilityConfigurations",
	"key":		"ObservabilityConfigurationArn",
	"filterid":	"ObservabilityConfigurationArn"
}

aws_apprunner_service = {
	"clfn":		"apprunner",
	"descfn":	"list_services",
	"topkey":	"Services",
	"key":		"ServiceArn",
	"filterid":	"ServiceArn"
}

aws_apprunner_vpc_connector = {
	"clfn":		"apprunner",
	"descfn":	"list_vpc_connectors",
	"topkey":	"VpcConnectors",
	"key":		"VpcConnectorArn",
	"filterid":	"VpcConnectorArn"
}

aws_apprunner_vpc_ingress_connection = {
	"clfn":		"apprunner",
	"descfn":	"list_vpc_ingress_connections",
	"topkey":	"VpcIngressConnections",
	"key":		"VpcIngressConnectionArn",
	"filterid":	"VpcIngressConnectionArn"
}

aws_appstream_directory_config = {
	"clfn":		"appstream",
	"descfn":	"list_directory_configs",
	"topkey":	"DirectoryConfigs",
	"key":		"DirectoryName",
	"filterid":	"DirectoryName"
}

aws_appstream_fleet = {
	"clfn":		"appstream",
	"descfn":	"list_fleets",
	"topkey":	"Fleets",
	"key":		"Name",
	"filterid":	"Name"
}

aws_appstream_fleet_stack_association = {
	"clfn":		"appstream",
	"descfn":	"list_fleet_stack_associations",
	"topkey":	"FleetStackAssociations",
	"key":		"FleetName",
	"filterid":	"FleetName"
}

aws_appstream_image_builder = {
	"clfn":		"appstream",
	"descfn":	"list_image_builders",
	"topkey":	"ImageBuilders",
	"key":		"Name",
	"filterid":	"Name"
}

aws_appstream_stack = {
	"clfn":		"appstream",
	"descfn":	"list_stacks",
	"topkey":	"Stacks",
	"key":		"Name",
	"filterid":	"Name"
}

aws_appstream_user = {
	"clfn":		"appstream",
	"descfn":	"list_users",
	"topkey":	"Users",
	"key":		"UserName",
	"filterid":	"UserName"
}

aws_appstream_user_stack_association = {
	"clfn":		"appstream",
	"descfn":	"list_user_stack_associations",
	"topkey":	"UserStackAssociations",
	"key":		"UserName",
	"filterid":	"UserName"
}

aws_appsync_api_cache = {
	"clfn":		"appsync",
	"descfn":	"list_api_caches",
	"topkey":	"ApiCaches",
	"key":		"ApiCacheName",
	"filterid":	"ApiCacheName"
}

aws_appsync_api_key = {
	"clfn":		"appsync",
	"descfn":	"list_api_keys",
	"topkey":	"ApiKeys",
	"key":		"ApiKeyId",
	"filterid":	"ApiKeyId"
}

aws_appsync_datasource = {
	"clfn":		"appsync",
	"descfn":	"list_data_sources",
	"topkey":	"DataSources",
	"key":		"DataSourceName",
	"filterid":	"DataSourceName"
}

aws_appsync_domain_name = {
	"clfn":		"appsync",
	"descfn":	"list_domain_names",
	"topkey":	"DomainNames",
	"key":		"DomainName",
	"filterid":	"DomainName"
}

aws_appsync_domain_name_api_association = {
	"clfn":		"appsync",
	"descfn":	"list_domain_name_api_associations",
	"topkey":	"DomainNameApiAssociations",
	"key":		"DomainName",
	"filterid":	"DomainName"
}

aws_appsync_function = {
	"clfn":		"appsync",
	"descfn":	"list_functions",
	"topkey":	"Functions",
	"key":		"FunctionId",
	"filterid":	"FunctionId"
}

aws_appsync_graphql_api = {
	"clfn":		"appsync",
	"descfn":	"list_graphql_apis",
	"topkey":	"GraphqlApis",
	"key":		"ApiId",
	"filterid":	"ApiId"
}

aws_appsync_resolver = {
	"clfn":		"appsync",
	"descfn":	"list_resolvers",
	"topkey":	"Resolvers",
	"key":		"ResolverArn",
	"filterid":	"ResolverArn"
}

aws_appsync_type = {
	"clfn":		"appsync",
	"descfn":	"list_types",
	"topkey":	"Types",
	"key":		"TypeName",
	"filterid":	"TypeName"
}

aws_athena_data_catalog = {
	"clfn":		"athena",
	"descfn":	"list_data_catalogs",
	"topkey":	"DataCatalogs",
	"key":		"Name",
	"filterid":	"Name"
}

aws_athena_database = {
	"clfn":		"athena",
	"descfn":	"list_databases",
	"topkey":	"Databases",
	"key":		"Name",
	"filterid":	"Name"
}

aws_athena_named_query = {
	"clfn":		"athena",
	"descfn":	"list_named_queries",
	"topkey":	"NamedQueries",
	"key":		"NamedQueryId",
	"filterid":	"NamedQueryId"
}

aws_athena_prepared_statement = {
	"clfn":		"athena",
	"descfn":	"list_prepared_statements",
	"topkey":	"PreparedStatements",
	"key":		"PreparedStatementName",
	"filterid":	"PreparedStatementName"
}

aws_athena_workgroup = {
	"clfn":		"athena",
	"descfn":	"list_work_groups",
	"topkey":	"WorkGroups",
	"key":		"Name",
	"filterid":	"Name"
}

aws_auditmanager_account_registration = {
	"clfn":		"auditmanager",
	"descfn":	"list_account_registrations",
	"topkey":	"AccountRegistrations",
	"key":		"Id",
	"filterid":	"Id"
}

aws_auditmanager_assessment = {
	"clfn":		"auditmanager",
	"descfn":	"list_assessments",
	"topkey":	"Assessments",
	"key":		"Id",
	"filterid":	"Id"
}

aws_auditmanager_assessment_delegation = {
	"clfn":		"auditmanager",
	"descfn":	"list_assessment_delegations",
	"topkey":	"AssessmentDelegations",
	"key":		"Id",
	"filterid":	"Id"
}

aws_auditmanager_assessment_report = {
	"clfn":		"auditmanager",
	"descfn":	"list_assessment_reports",
	"topkey":	"AssessmentReports",
	"key":		"Id",
	"filterid":	"Id"
}

aws_auditmanager_control = {
	"clfn":		"auditmanager",
	"descfn":	"list_controls",
	"topkey":	"Controls",
	"key":		"Id",
	"filterid":	"Id"
}

aws_auditmanager_framework = {
	"clfn":		"auditmanager",
	"descfn":	"list_frameworks",
	"topkey":	"Frameworks",
	"key":		"Id",
	"filterid":	"Id"
}

aws_auditmanager_framework_share = {
	"clfn":		"auditmanager",
	"descfn":	"list_framework_shares",
	"topkey":	"FrameworkShares",
	"key":		"Id",
	"filterid":	"Id"
}

aws_auditmanager_organization_admin_account_registration = {
	"clfn":		"auditmanager",
	"descfn":	"list_organization_admin_accounts",
	"topkey":	"OrganizationAdminAccounts",
	"key":		"Id",
	"filterid":	"Id"
}

aws_autoscaling_attachment = {
	"clfn":		"autoscaling",
	"descfn":	"list_attachments",
	"topkey":	"Attachments",
	"key":		"AttachmentName",
	"filterid":	"AttachmentName"
}

aws_autoscaling_group = {
	"clfn":		"autoscaling",
	"descfn":	"list_groups",
	"topkey":	"Groups",
	"key":		"AutoScalingGroupName",
	"filterid":	"AutoScalingGroupName"
}

aws_autoscaling_group_tag = {
	"clfn":		"autoscaling",
	"descfn":	"list_tags",
	"topkey":	"Tags",
	"key":		"ResourceId",
	"filterid":	"ResourceId"
}

aws_autoscaling_lifecycle_hook = {
	"clfn":		"autoscaling",
	"descfn":	"list_lifecycle_hooks",
	"topkey":	"LifecycleHooks",
	"key":		"LifecycleHookName",
	"filterid":	"LifecycleHookName"
}

aws_autoscaling_notification = {
	"clfn":		"autoscaling",
	"descfn":	"list_notifications",
	"topkey":	"Notifications",
	"key":		"TopicARN",
	"filterid":	"TopicARN"
}

aws_autoscaling_policy = {
	"clfn":		"autoscaling",
	"descfn":	"list_policies",
	"topkey":	"Policies",
	"key":		"PolicyName",
	"filterid":	"PolicyName"
}

aws_autoscaling_schedule = {
	"clfn":		"autoscaling",
	"descfn":	"list_schedules",
	"topkey":	"Schedules",
	"key":		"ScheduleName",
	"filterid":	"ScheduleName"
}

aws_autoscaling_traffic_source_attachment = {
	"clfn":		"autoscaling",
	"descfn":	"list_traffic_source_attachments",
	"topkey":	"TrafficSourceAttachments",
	"key":		"TrafficSourceAttachmentName",
	"filterid":	"TrafficSourceAttachmentName"
}

aws_autoscalingplans_scaling_plan = {
	"clfn":		"autoscaling-plans",
	"descfn":	"list_scaling_plans",
	"topkey":	"ScalingPlans",
	"key":		"ScalingPlanName",
	"filterid":	"ScalingPlanName"
}

aws_backup_framework = {
	"clfn":		"backup",
	"descfn":	"list_frameworks",
	"topkey":	"Frameworks",
	"key":		"FrameworkName",
	"filterid":	"FrameworkName"
}

aws_backup_global_settings = {
	"clfn":		"backup",
	"descfn":	"list_global_settings",
	"topkey":	"GlobalSettings",
	"key":		"GlobalSettingsName",
	"filterid":	"GlobalSettingsName"
}

aws_backup_plan = {
	"clfn":		"backup",
	"descfn":	"list_plans",
	"topkey":	"Plans",
	"key":		"PlanName",
	"filterid":	"PlanName"
}

aws_backup_region_settings = {
	"clfn":		"backup",
	"descfn":	"list_region_settings",
	"topkey":	"RegionSettings",
	"key":		"RegionSettingsName",
	"filterid":	"RegionSettingsName"
}

aws_backup_report_plan = {
	"clfn":		"backup",
	"descfn":	"list_report_plans",
	"topkey":	"ReportPlans",
	"key":		"ReportPlanName",
	"filterid":	"ReportPlanName"
}

aws_backup_selection = {
	"clfn":		"backup",
	"descfn":	"list_selections",
	"topkey":	"Selections",
	"key":		"SelectionName",
	"filterid":	"SelectionName"
}

aws_backup_vault = {
	"clfn":		"backup",
	"descfn":	"list_vaults",
	"topkey":	"Vaults",
	"key":		"VaultName",
	"filterid":	"VaultName"
}

aws_backup_vault_lock_configuration = {
	"clfn":		"backup",
	"descfn":	"list_vault_lock_configuration",
	"topkey":	"VaultLockConfiguration",
	"key":		"VaultLockConfigurationName",
	"filterid":	"VaultLockConfigurationName"
}

aws_backup_vault_notifications = {
	"clfn":		"backup",
	"descfn":	"list_vault_notifications",
	"topkey":	"VaultNotifications",
	"key":		"VaultNotificationsName",
	"filterid":	"VaultNotificationsName"
}

aws_backup_vault_policy = {
	"clfn":		"backup",
	"descfn":	"list_vault_policies",
	"topkey":	"VaultPolicies",
	"key":		"VaultName",
	"filterid":	"VaultName"
}

aws_batch_compute_environment = {
	"clfn":		"batch",
	"descfn":	"list_compute_environments",
	"topkey":	"ComputeEnvironments",
	"key":		"ComputeEnvironmentName",
	"filterid":	"ComputeEnvironmentName"
}

aws_batch_job_definition = {
	"clfn":		"batch",
	"descfn":	"list_job_definitions",
	"topkey":	"JobDefinitions",
	"key":		"JobDefinitionName",
	"filterid":	"JobDefinitionName"
}

aws_batch_job_queue = {
	"clfn":		"batch",
	"descfn":	"list_job_queues",
	"topkey":	"JobQueues",
	"key":		"JobQueueName",
	"filterid":	"JobQueueName"
}

aws_batch_scheduling_policy = {
	"clfn":		"batch",
	"descfn":	"list_scheduling_policies",
	"topkey":	"SchedulingPolicies",
	"key":		"SchedulingPolicyName",
	"filterid":	"SchedulingPolicyName"
}

aws_bedrock_model_invocation_logging_configuration = {
	"clfn":		"bedrock",
	"descfn":	"list_model_invocation_logging_configurations",
	"topkey":	"ModelInvocationLoggingConfigurations",
	"key":		"ModelInvocationLoggingConfigurationName",
	"filterid":	"ModelInvocationLoggingConfigurationName"
}

aws_budgets_budget = {
	"clfn":		"budgets",
	"descfn":	"list_budgets",
	"topkey":	"Budgets",
	"key":		"BudgetName",
	"filterid":	"BudgetName"
}

aws_budgets_budget_action = {
	"clfn":		"budgets",
	"descfn":	"list_budget_actions",
	"topkey":	"BudgetActions",
	"key":		"ActionId",
	"filterid":	"ActionId"
}

aws_ce_anomaly_monitor = {
	"clfn":		"ce",
	"descfn":	"list_anomaly_monitors",
	"topkey":	"AnomalyMonitors",
	"key":		"MonitorName",
	"filterid":	"MonitorName"
}

aws_ce_anomaly_subscription = {
	"clfn":		"ce",
	"descfn":	"list_anomaly_subscriptions",
	"topkey":	"AnomalySubscriptions",
	"key":		"SubscriptionName",
	"filterid":	"SubscriptionName"
}

aws_ce_cost_allocation_tag = {
	"clfn":		"ce",
	"descfn":	"list_cost_allocation_tags",
	"topkey":	"CostAllocationTags",
	"key":		"CostAllocationTagKey",
	"filterid":	"CostAllocationTagKey"
}

aws_ce_cost_category = {
	"clfn":		"ce",
	"descfn":	"list_cost_categories",
	"topkey":	"CostCategories",
	"key":		"CostCategoryArn",
	"filterid":	"CostCategoryArn"
}

aws_chime_voice_connector = {
	"clfn":		"chime-sdk-voice",
	"descfn":	"list_voice_connectors",
	"topkey":	"VoiceConnectors",
	"key":		"Name",
	"filterid":	"Name"
}

aws_chime_voice_connector_group = {
	"clfn":		"chime-sdk-voice",
	"descfn":	"list_voice_connector_groups",
	"topkey":	"VoiceConnectorGroups",
	"key":		"Name",
	"filterid":	"Name"
}

aws_chime_voice_connector_logging = {
	"clfn":		"chime-sdk-voice",
	"descfn":	"list_voice_connector_logging_configurations",
	"topkey":	"VoiceConnectorLoggingConfigurations",
	"key":		"VoiceConnectorName",
	"filterid":	"VoiceConnectorName"
}

aws_chime_voice_connector_origination = {
	"clfn":		"chime-sdk-voice",
	"descfn":	"list_voice_connector_origination_configurations",
	"topkey":	"VoiceConnectorOriginationConfigurations",
	"key":		"VoiceConnectorName",
	"filterid":	"VoiceConnectorName"
}

aws_chime_voice_connector_streaming = {
	"clfn":		"chime-sdk-voice",
	"descfn":	"list_voice_connector_streaming_configurations",
	"topkey":	"VoiceConnectorStreamingConfigurations",
	"key":		"VoiceConnectorName",
	"filterid":	"VoiceConnectorName"
}

aws_chime_voice_connector_termination = {
	"clfn":		"chime-sdk-voice",
	"descfn":	"list_voice_connector_termination_configurations",
	"topkey":	"VoiceConnectorTerminationConfigurations",
	"key":		"VoiceConnectorName",
	"filterid":	"VoiceConnectorName"
}

aws_chime_voice_connector_termination_credentials = {
	"clfn":		"chime-sdk-voice",
	"descfn":	"list_voice_connector_termination_credentials",
	"topkey":	"VoiceConnectorTerminationCredentials",
	"key":		"Name",
	"filterid":	"Name"
}

aws_chimesdkmediapipelines_media_insights_pipeline_configuration = {
	"clfn":		"chime-sdk-media-pipelines",
	"descfn":	"list_media_insights_pipelines",
	"topkey":	"MediaInsightsPipelines",
	"key":		"Name",
	"filterid":	"Name"
}

aws_chimesdkvoice_global_settings = {
	"clfn":		"chime-sdk-voice",
	"descfn":	"list_global_settings",
	"topkey":	"GlobalSettings",
	"key":		"GlobalSettingsName",
	"filterid":	"GlobalSettingsName"
}

aws_chimesdkvoice_sip_media_application = {
	"clfn":		"chime-sdk-voice",
	"descfn":	"list_sip_media_applications",
	"topkey":	"SipMediaApplications",
	"key":		"Name",
	"filterid":	"Name"
}

aws_chimesdkvoice_sip_rule = {
	"clfn":		"chime-sdk-voice",
	"descfn":	"list_sip_rules",
	"topkey":	"SipRules",
	"key":		"Name",
	"filterid":	"Name"
}

aws_chimesdkvoice_voice_profile_domain = {
	"clfn":		"chime-sdk-voice",
	"descfn":	"list_voice_profile_domains",
	"topkey":	"VoiceProfileDomains",
	"key":		"Name",
	"filterid":	"Name"
}

aws_cleanrooms_collaboration = {
	"clfn":		"cleanrooms",
	"descfn":	"list_collaborations",
	"topkey":	"Collaborations",
	"key":		"CollaborationId",
	"filterid":	"CollaborationId"
}

aws_cleanrooms_configured_table = {
	"clfn":		"cleanrooms",
	"descfn":	"list_configured_tables",
	"topkey":	"ConfiguredTables",
	"key":		"ConfiguredTableName",
	"filterid":	"ConfiguredTableName"
}

aws_cloud9_environment_ec2 = {
	"clfn":		"cloud9",
	"descfn":	"list_environments",
	"topkey":	"Environments",
	"key":		"Name",
	"filterid":	"Name"
}

aws_cloud9_environment_membership = {
	"clfn":		"cloud9",
	"descfn":	"list_environment_memberships",
	"topkey":	"Memberships",
	"key":		"Id",
	"filterid":	"Id"
}

aws_cloudcontrolapi_resource = {
	"clfn":		"cloudcontrol",
	"descfn":	"list_resources",
	"topkey":	"Resources",
	"key":		"Identifier",
	"filterid":	"Identifier"
}

aws_cloudformation_stack = {
	"clfn":		"cloudformation",
	"descfn":	"list_stacks",
	"topkey":	"Stacks",
	"key":		"StackName",
	"filterid":	"StackName"
}

aws_cloudformation_stack_set = {
	"clfn":		"cloudformation",
	"descfn":	"list_stack_sets",
	"topkey":	"StackSets",
	"key":		"StackSetName",
	"filterid":	"StackSetName"
}

aws_cloudformation_stack_set_instance = {
	"clfn":		"cloudformation",
	"descfn":	"list_stack_set_instances",
	"topkey":	"StackSetInstances",
	"key":		"Id",
	"filterid":	"Id"
}

aws_cloudformation_type = {
	"clfn":		"cloudformation",
	"descfn":	"list_types",
	"topkey":	"Types",
	"key":		"Arn",
	"filterid":	"Arn"
}

aws_cloudfront_cache_policy = {
	"clfn":		"cloudfront",
	"descfn":	"list_cache_policies",
	"topkey":	"CachePolicies",
	"key":		"CachePolicyId",
	"filterid":	"CachePolicyId"
}

aws_cloudfront_continuous_deployment_policy = {
	"clfn":		"cloudfront",
	"descfn":	"list_continuous_deployment_policies",
	"topkey":	"ContinuousDeploymentPolicies",
	"key":		"ContinuousDeploymentPolicyId",
	"filterid":	"ContinuousDeploymentPolicyId"
}

aws_cloudfront_distribution = {
	"clfn":		"cloudfront",
	"descfn":	"list_distributions",
	"topkey":	"Distributions",
	"key":		"Id",
	"filterid":	"Id"
}

aws_cloudfront_field_level_encryption_config = {
	"clfn":		"cloudfront",
	"descfn":	"list_field_level_encryption_configs",
	"topkey":	"FieldLevelEncryptionConfigs",
	"key":		"Id",
	"filterid":	"Id"
}

aws_cloudfront_field_level_encryption_profile = {
	"clfn":		"cloudfront",
	"descfn":	"list_field_level_encryption_profiles",
	"topkey":	"FieldLevelEncryptionProfiles",
	"key":		"Id",
	"filterid":	"Id"
}

aws_cloudfront_function = {
	"clfn":		"cloudfront",
	"descfn":	"list_functions",
	"topkey":	"Functions",
	"key":		"FunctionId",
	"filterid":	"FunctionId"
}

aws_cloudfront_key_group = {
	"clfn":		"cloudfront",
	"descfn":	"list_key_groups",
	"topkey":	"KeyGroups",
	"key":		"KeyGroupId",
	"filterid":	"KeyGroupId"
}

aws_cloudfront_monitoring_subscription = {
	"clfn":		"cloudfront",
	"descfn":	"list_monitoring_subscriptions",
	"topkey":	"MonitoringSubscriptions",
	"key":		"Id",
	"filterid":	"Id"
}

aws_cloudfront_origin_access_control = {
	"clfn":		"cloudfront",
	"descfn":	"list_origin_access_controls",
	"topkey":	"OriginAccessControls",
	"key":		"Id",
	"filterid":	"Id"
}

aws_cloudfront_origin_access_identity = {
	"clfn":		"cloudfront",
	"descfn":	"list_origin_access_identities",
	"topkey":	"OriginAccessIdentities",
	"key":		"Id",
	"filterid":	"Id"
}

aws_cloudfront_origin_request_policy = {
	"clfn":		"cloudfront",
	"descfn":	"list_origin_request_policies",
	"topkey":	"OriginRequestPolicies",
	"key":		"Id",
	"filterid":	"Id"
}

aws_cloudfront_public_key = {
	"clfn":		"cloudfront",
	"descfn":	"list_public_keys",
	"topkey":	"PublicKeys",
	"key":		"Id",
	"filterid":	"Id"
}

aws_cloudfront_realtime_log_config = {
	"clfn":		"cloudfront",
	"descfn":	"list_realtime_log_configs",
	"topkey":	"RealtimeLogConfigs",
	"key":		"Id",
	"filterid":	"Id"
}

aws_cloudfront_response_headers_policy = {
	"clfn":		"cloudfront",
	"descfn":	"list_response_headers_policies",
	"topkey":	"ResponseHeadersPolicies",
	"key":		"Id",
	"filterid":	"Id"
}

aws_cloudhsm_v2_cluster = {
	"clfn":		"cloudhsmv2",
	"descfn":	"list_clusters",
	"topkey":	"Clusters",
	"key":		"ClusterId",
	"filterid":	"ClusterId"
}

aws_cloudhsm_v2_hsm = {
	"clfn":		"cloudhsmv2",
	"descfn":	"list_hsms",
	"topkey":	"Hsms",
	"key":		"HsmId",
	"filterid":	"HsmId"
}

aws_cloudsearch_domain = {
	"clfn":		"cloudsearch",
	"descfn":	"list_domains",
	"topkey":	"DomainNames",
	"key":		"DomainName",
	"filterid":	"DomainName"
}

aws_cloudsearch_domain_service_access_policy = {
	"clfn":		"cloudsearch",
	"descfn":	"list_domain_service_access_policies",
	"topkey":	"DomainServiceAccessPolicies",
	"key":		"DomainName",
	"filterid":	"DomainName"
}

aws_cloudtrail = {
	"clfn":		"cloudtrail",
	"descfn":	"list_trails",
	"topkey":	"Trails",
	"key":		"Name",
	"filterid":	"Name"
}

aws_cloudtrail_event_data_store = {
	"clfn":		"cloudtrail",
	"descfn":	"list_event_data_stores",
	"topkey":	"EventDataStores",
	"key":		"Name",
	"filterid":	"Name"
}

aws_cloudwatch_composite_alarm = {
	"clfn":		"cloudwatch",
	"descfn":	"list_composite_alarms",
	"topkey":	"CompositeAlarms",
	"key":		"AlarmName",
	"filterid":	"AlarmName"
}

aws_cloudwatch_dashboard = {
	"clfn":		"cloudwatch",
	"descfn":	"list_dashboards",
	"topkey":	"Dashboards",
	"key":		"DashboardName",
	"filterid":	"DashboardName"
}

aws_cloudwatch_event_api_destination = {
	"clfn":		"cloudwatch",
	"descfn":	"list_api_destinations",
	"topkey":	"ApiDestinations",
	"key":		"Name",
	"filterid":	"Name"
}

aws_cloudwatch_event_archive = {
	"clfn":		"cloudwatch",
	"descfn":	"list_archives",
	"topkey":	"Archives",
	"key":		"ArchiveName",
	"filterid":	"ArchiveName"
}

aws_cloudwatch_event_bus = {
	"clfn":		"cloudwatch",
	"descfn":	"list_event_buses",
	"topkey":	"EventBusNames",
	"key":		"Name",
	"filterid":	"Name"
}

aws_cloudwatch_event_bus_policy = {
	"clfn":		"cloudwatch",
	"descfn":	"list_event_bus_policies",
	"topkey":	"EventBusPolicies",
	"key":		"Name",
	"filterid":	"Name"
}

aws_cloudwatch_event_connection = {
	"clfn":		"cloudwatch",
	"descfn":	"list_connections",
	"topkey":	"Connections",
	"key":		"Name",
	"filterid":	"Name"
}

aws_cloudwatch_event_endpoint = {
	"clfn":		"cloudwatch",
	"descfn":	"list_endpoints",
	"topkey":	"Endpoints",
	"key":		"Name",
	"filterid":	"Name"
}

aws_cloudwatch_event_permission = {
	"clfn":		"cloudwatch",
	"descfn":	"list_permissions",
	"topkey":	"Permissions",
	"key":		"Name",
	"filterid":	"Name"
}

aws_cloudwatch_event_target = {
	"clfn":		"cloudwatch",
	"descfn":	"list_targets",
	"topkey":	"Targets",
	"key":		"Name",
	"filterid":	"Name"
}

aws_cloudwatch_log_data_protection_policy = {
	"clfn":		"cloudwatch",
	"descfn":	"list_data_protection_policies",
	"topkey":	"DataProtectionPolicies",
	"key":		"Name",
	"filterid":	"Name"
}

aws_cloudwatch_log_destination = {
	"clfn":		"cloudwatch",
	"descfn":	"list_destinations",
	"topkey":	"Destinations",
	"key":		"DestinationName",
	"filterid":	"DestinationName"
}

aws_cloudwatch_log_destination_policy = {
	"clfn":		"cloudwatch",
	"descfn":	"list_destination_policies",
	"topkey":	"DestinationPolicies",
	"key":		"DestinationName",
	"filterid":	"DestinationName"
}

aws_cloudwatch_log_metric_filter = {
	"clfn":		"cloudwatch",
	"descfn":	"list_metric_filters",
	"topkey":	"MetricFilters",
	"key":		"Name",
	"filterid":	"Name"
}

aws_cloudwatch_log_resource_policy = {
	"clfn":		"cloudwatch",
	"descfn":	"list_resource_policies",
	"topkey":	"ResourcePolicies",
	"key":		"Name",
	"filterid":	"Name"
}

aws_cloudwatch_log_stream = {
	"clfn":		"cloudwatch",
	"descfn":	"list_log_streams",
	"topkey":	"LogStreams",
	"key":		"LogStreamName",
	"filterid":	"LogStreamName"
}

aws_cloudwatch_log_subscription_filter = {
	"clfn":		"cloudwatch",
	"descfn":	"list_subscription_filters",
	"topkey":	"SubscriptionFilters",
	"key":		"Name",
	"filterid":	"Name"
}

aws_cloudwatch_metric_alarm = {
	"clfn":		"cloudwatch",
	"descfn":	"list_alarms",
	"topkey":	"MetricAlarms",
	"key":		"AlarmName",
	"filterid":	"AlarmName"
}

aws_cloudwatch_metric_stream = {
	"clfn":		"cloudwatch",
	"descfn":	"list_metric_streams",
	"topkey":	"MetricStreams",
	"key":		"Name",
	"filterid":	"Name"
}

aws_cloudwatch_query_definition = {
	"clfn":		"cloudwatch",
	"descfn":	"list_query_definitions",
	"topkey":	"QueryDefinitions",
	"key":		"Name",
	"filterid":	"Name"
}

aws_codeartifact_domain = {
	"clfn":		"codeartifact",
	"descfn":	"list_domains",
	"topkey":	"Domains",
	"key":		"Name",
	"filterid":	"Name"
}

aws_codeartifact_domain_permissions_policy = {
	"clfn":		"codeartifact",
	"descfn":	"list_domain_permissions_policies",
	"topkey":	"DomainPermissionsPolicies",
	"key":		"Name",
	"filterid":	"Name"
}

aws_codeartifact_repository = {
	"clfn":		"codeartifact",
	"descfn":	"list_repositories",
	"topkey":	"Repositories",
	"key":		"Name",
	"filterid":	"Name"
}

aws_codeartifact_repository_permissions_policy = {
	"clfn":		"codeartifact",
	"descfn":	"list_repository_permissions_policies",
	"topkey":	"RepositoryPermissionsPolicies",
	"key":		"Name",
	"filterid":	"Name"
}

aws_codebuild_project = {
	"clfn":		"codebuild",
	"descfn":	"list_projects",
	"topkey":	"Projects",
	"key":		"Name",
	"filterid":	"Name"
}

aws_codebuild_report_group = {
	"clfn":		"codebuild",
	"descfn":	"list_report_groups",
	"topkey":	"ReportGroups",
	"key":		"Name",
	"filterid":	"Name"
}

aws_codebuild_resource_policy = {
	"clfn":		"codebuild",
	"descfn":	"list_resource_policies",
	"topkey":	"ResourcePolicies",
	"key":		"Name",
	"filterid":	"Name"
}

aws_codebuild_source_credential = {
	"clfn":		"codebuild",
	"descfn":	"list_source_credentials",
	"topkey":	"SourceCredentialsInfos",
	"key":		"Arn",
	"filterid":	"Arn"
}

aws_codebuild_webhook = {
	"clfn":		"codebuild",
	"descfn":	"list_webhooks",
	"topkey":	"Webhooks",
	"key":		"Name",
	"filterid":	"Name"
}

aws_codecatalyst_dev_environment = {
	"clfn":		"codecatalyst",
	"descfn":	"list_dev_environments",
	"topkey":	"DevEnvironments",
	"key":		"Id",
	"filterid":	"Id"
}

aws_codecatalyst_project = {
	"clfn":		"codecatalyst",
	"descfn":	"list_projects",
	"topkey":	"Projects",
	"key":		"Id",
	"filterid":	"Id"
}

aws_codecatalyst_source_repository = {
	"clfn":		"codecatalyst",
	"descfn":	"list_source_repositories",
	"topkey":	"SourceRepositories",
	"key":		"Id",
	"filterid":	"Id"
}

aws_codecommit_approval_rule_template = {
	"clfn":		"codecommit",
	"descfn":	"list_approval_rule_templates",
	"topkey":	"ApprovalRuleTemplates",
	"key":		"Name",
	"filterid":	"Name"
}

aws_codecommit_approval_rule_template_association = {
	"clfn":		"codecommit",
	"descfn":	"list_associated_approval_rule_templates",
	"topkey":	"AssociatedApprovalRuleTemplates",
	"key":		"Name",
	"filterid":	"Name"
}

aws_codecommit_repository = {
	"clfn":		"codecommit",
	"descfn":	"list_repositories",
	"topkey":	"Repositories",
	"key":		"Name",
	"filterid":	"Name"
}

aws_codecommit_trigger = {
	"clfn":		"codecommit",
	"descfn":	"list_repository_triggers",
	"topkey":	"RepositoryTriggers",
	"key":		"Name",
	"filterid":	"Name"
}

aws_codedeploy_app = {
	"clfn":		"codedeploy",
	"descfn":	"list_apps",
	"topkey":	"Apps",
	"key":		"Name",
	"filterid":	"Name"
}

aws_codedeploy_deployment_config = {
	"clfn":		"codedeploy",
	"descfn":	"list_deployment_configs",
	"topkey":	"DeploymentConfigs",
	"key":		"Name",
	"filterid":	"Name"
}

aws_codedeploy_deployment_group = {
	"clfn":		"codedeploy",
	"descfn":	"list_deployment_groups",
	"topkey":	"DeploymentGroups",
	"key":		"Name",
	"filterid":	"Name"
}

aws_codeguruprofiler_profiling_group = {
	"clfn":		"codeguruprofiler",
	"descfn":	"list_profiling_groups",
	"topkey":	"ProfilingGroups",
	"key":		"Name",
	"filterid":	"Name"
}

aws_codegurureviewer_repository_association = {
	"clfn":		"codeguru-reviewer",
	"descfn":	"list_repository_associations",
	"topkey":	"RepositoryAssociations",
	"key":		"Name",
	"filterid":	"Name"
}

aws_codepipeline = {
	"clfn":		"codepipeline",
	"descfn":	"list_pipelines",
	"topkey":	"Pipelines",
	"key":		"Name",
	"filterid":	"Name"
}

aws_codepipeline_custom_action_type = {
	"clfn":		"codepipeline",
	"descfn":	"list_custom_action_types",
	"topkey":	"CustomActionTypes",
	"key":		"Category",
	"filterid":	"Category"
}

aws_codepipeline_webhook = {
	"clfn":		"codepipeline",
	"descfn":	"list_webhooks",
	"topkey":	"Webhooks",
	"key":		"Name",
	"filterid":	"Name"
}

aws_codestarconnections_connection = {
	"clfn":		"codestar-connections",
	"descfn":	"list_connections",
	"topkey":	"Connections",
	"key":		"ConnectionName",
	"filterid":	"ConnectionName"
}

aws_codestarconnections_host = {
	"clfn":		"codestar-connections",
	"descfn":	"list_hosts",
	"topkey":	"Hosts",
	"key":		"Name",
	"filterid":	"Name"
}

aws_codestarnotifications_notification_rule = {
	"clfn":		"codestar-notifications",
	"descfn":	"list_notification_rules",
	"topkey":	"NotificationRules",
	"key":		"Name",
	"filterid":	"Name"
}

aws_cognito_identity_pool = {
	"clfn":		"cognito-identity",
	"descfn":	"list_identity_pools",
	"topkey":	"IdentityPools",
	"key":		"IdentityPoolName",
	"filterid":	"IdentityPoolName"
}

aws_cognito_identity_pool_provider_principal_tag = {
	"clfn":		"cognito-identity",
	"descfn":	"list_identity_pool_roles",
	"topkey":	"IdentityPoolRoles",
	"key":		"IdentityPoolId",
	"filterid":	"IdentityPoolId"
}

aws_cognito_identity_pool_roles_attachment = {
	"clfn":		"cognito-identity",
	"descfn":	"list_identity_pool_roles_attachments",
	"topkey":	"IdentityPoolRolesAttachments",
	"key":		"IdentityPoolId",
	"filterid":	"IdentityPoolId"
}

aws_cognito_identity_provider = {
	"clfn":		"cognito-idp",
	"descfn":	"list_identity_providers",
	"topkey":	"IdentityProviders",
	"key":		"ProviderName",
	"filterid":	"ProviderName"
}

aws_cognito_managed_user_pool_client = {
	"clfn":		"cognito-idp",
	"descfn":	"list_user_pool_clients",
	"topkey":	"UserPoolClients",
	"key":		"ClientName",
	"filterid":	"ClientName"
}

aws_cognito_resource_server = {
	"clfn":		"cognito",
	"descfn":	"list_resource_servers",
	"topkey":	"ResourceServers",
	"key":		"Identifier",
	"filterid":	"Identifier"
}

aws_cognito_risk_configuration = {
	"clfn":		"cognito-idp",
	"descfn":	"list_risk_configurations",
	"topkey":	"RiskConfigurations",
	"key":		"Id",
	"filterid":	"Id"
}

aws_cognito_user = {
	"clfn":		"cognito-idp",
	"descfn":	"list_users",
	"topkey":	"Users",
	"key":		"Username",
	"filterid":	"Username"
}

aws_cognito_user_group = {
	"clfn":		"cognito-idp",
	"descfn":	"list_user_groups",
	"topkey":	"UserGroups",
	"key":		"GroupName",
	"filterid":	"GroupName"
}

aws_cognito_user_in_group = {
	"clfn":		"cognito-idp",
	"descfn":	"list_users_in_group",
	"topkey":	"UsersInGroup",
	"key":		"Username",
	"filterid":	"Username"
}

aws_cognito_user_pool = {
	"clfn":		"cognito-idp",
	"descfn":	"list_user_pools",
	"topkey":	"UserPools",
	"key":		"Name",
	"filterid":	"Name"
}

aws_cognito_user_pool_client = {
	"clfn":		"cognito-idp",
	"descfn":	"list_user_pool_clients",
	"topkey":	"UserPoolClients",
	"key":		"ClientName",
	"filterid":	"ClientName"
}

aws_cognito_user_pool_domain = {
	"clfn":		"cognito-idp",
	"descfn":	"list_user_pool_domains",
	"topkey":	"UserPoolDomains",
	"key":		"Domain",
	"filterid":	"Domain"
}

aws_cognito_user_pool_ui_customization = {
	"clfn":		"cognito-idp",
	"descfn":	"list_user_pool_uis",
	"topkey":	"UserPoolUis",
	"key":		"UserPoolId",
	"filterid":	"UserPoolId"
}

aws_comprehend_document_classifier = {
	"clfn":		"comprehend",
	"descfn":	"list_document_classifiers",
	"topkey":	"DocumentClassifiers",
	"key":		"DocumentClassifierArn",
	"filterid":	"DocumentClassifierArn"
}

aws_comprehend_entity_recognizer = {
	"clfn":		"comprehend",
	"descfn":	"list_entity_recognizers",
	"topkey":	"EntityRecognizers",
	"key":		"EntityRecognizerArn",
	"filterid":	"EntityRecognizerArn"
}

aws_config_aggregate_authorization = {
	"clfn":		"config",
	"descfn":	"list_aggregate_authorizations",
	"topkey":	"AggregateAuthorizations",
	"key":		"AuthorizationName",
	"filterid":	"AuthorizationName"
}

aws_config_configuration_aggregator = {
	"clfn":		"config",
	"descfn":	"list_configuration_aggregators",
	"topkey":	"ConfigurationAggregators",
	"key":		"ConfigurationAggregatorName",
	"filterid":	"ConfigurationAggregatorName"
}

aws_config_configuration_recorder = {
	"clfn":		"config",
	"descfn":	"list_configuration_recorders",
	"topkey":	"ConfigurationRecorders",
	"key":		"name",
	"filterid":	"name"
}

aws_config_configuration_recorder_status = {
	"clfn":		"config",
	"descfn":	"list_configuration_recorder_status",
	"topkey":	"ConfigurationRecorderStatus",
	"key":		"name",
	"filterid":	"name"
}

aws_config_conformance_pack = {
	"clfn":		"config",
	"descfn":	"list_conformance_packs",
	"topkey":	"ConformancePackNames",
	"key":		"ConformancePackName",
	"filterid":	"ConformancePackName"
}

aws_config_delivery_channel = {
	"clfn":		"config",
	"descfn":	"list_delivery_channels",
	"topkey":	"DeliveryChannels",
	"key":		"name",
	"filterid":	"name"
}

aws_config_organization_conformance_pack = {
	"clfn":		"config",
	"descfn":	"list_organization_conformance_packs",
	"topkey":	"OrganizationConformancePackNames",
	"key":		"ConformancePackName",
	"filterid":	"ConformancePackName"
}

aws_config_organization_custom_policy_rule = {
	"clfn":		"config",
	"descfn":	"list_organization_custom_policy_rules",
	"topkey":	"OrganizationCustomPolicyRules",
	"key":		"PolicyRuleName",
	"filterid":	"PolicyRuleName"
}

aws_config_organization_custom_rule = {
	"clfn":		"config",
	"descfn":	"list_organization_custom_rules",
	"topkey":	"OrganizationCustomRules",
	"key":		"PolicyRuleName",
	"filterid":	"PolicyRuleName"
}

aws_config_organization_managed_rule = {
	"clfn":		"config",
	"descfn":	"list_organization_managed_rules",
	"topkey":	"OrganizationManagedRules",
	"key":		"PolicyRuleName",
	"filterid":	"PolicyRuleName"
}

aws_config_remediation_configuration = {
	"clfn":		"config",
	"descfn":	"list_remediation_configurations",
	"topkey":	"RemediationConfigurations",
	"key":		"ConfigRuleName",
	"filterid":	"ConfigRuleName"
}

aws_connect_bot_association = {
	"clfn":		"connect",
	"descfn":	"list_bot_associations",
	"topkey":	"BotAssociations",
	"key":		"Name",
	"filterid":	"Name"
}

aws_connect_contact_flow = {
	"clfn":		"connect",
	"descfn":	"list_contact_flows",
	"topkey":	"ContactFlows",
	"key":		"Name",
	"filterid":	"Name"
}

aws_connect_contact_flow_module = {
	"clfn":		"connect",
	"descfn":	"list_contact_flow_modules",
	"topkey":	"ContactFlowModules",
	"key":		"Name",
	"filterid":	"Name"
}

aws_connect_hours_of_operation = {
	"clfn":		"connect",
	"descfn":	"list_hours_of_operations",
	"topkey":	"HoursOfOperations",
	"key":		"Name",
	"filterid":	"Name"
}

aws_connect_instance = {
	"clfn":		"connect",
	"descfn":	"list_instances",
	"topkey":	"Instances",
	"key":		"Id",
	"filterid":	"Id"
}

aws_connect_instance_storage_config = {
	"clfn":		"connect",
	"descfn":	"list_instance_storage_configs",
	"topkey":	"InstanceStorageConfigs",
	"key":		"InstanceId",
	"filterid":	"InstanceId"
}

aws_connect_lambda_function_association = {
	"clfn":		"connect",
	"descfn":	"list_lambda_function_associations",
	"topkey":	"LambdaFunctionAssociations",
	"key":		"InstanceId",
	"filterid":	"InstanceId"
}

aws_connect_phone_number = {
	"clfn":		"connect",
	"descfn":	"list_phone_numbers",
	"topkey":	"PhoneNumbers",
	"key":		"PhoneNumber",
	"filterid":	"PhoneNumber"
}

aws_connect_queue = {
	"clfn":		"connect",
	"descfn":	"list_queues",
	"topkey":	"Queues",
	"key":		"Id",
	"filterid":	"Id"
}

aws_connect_quick_connect = {
	"clfn":		"connect",
	"descfn":	"list_quick_connects",
	"topkey":	"QuickConnects",
	"key":		"Id",
	"filterid":	"Id"
}

aws_connect_routing_profile = {
	"clfn":		"connect",
	"descfn":	"list_routing_profiles",
	"topkey":	"RoutingProfiles",
	"key":		"Id",
	"filterid":	"Id"
}

aws_connect_security_profile = {
	"clfn":		"connect",
	"descfn":	"list_security_profiles",
	"topkey":	"SecurityProfiles",
	"key":		"Id",
	"filterid":	"Id"
}

aws_connect_user = {
	"clfn":		"connect",
	"descfn":	"list_users",
	"topkey":	"Users",
	"key":		"Id",
	"filterid":	"Id"
}

aws_connect_user_hierarchy_group = {
	"clfn":		"connect",
	"descfn":	"list_user_hierarchy_groups",
	"topkey":	"UserHierarchyGroups",
	"key":		"Id",
	"filterid":	"Id"
}

aws_connect_user_hierarchy_structure = {
	"clfn":		"connect",
	"descfn":	"list_user_hierarchy_structures",
	"topkey":	"UserHierarchyStructures",
	"key":		"Id",
	"filterid":	"Id"
}

aws_connect_vocabulary = {
	"clfn":		"connect",
	"descfn":	"list_vocabularies",
	"topkey":	"Vocabularies",
	"key":		"Id",
	"filterid":	"Id"
}

aws_controltower_control = {
	"clfn":		"controltower",
	"descfn":	"list_controls",
	"topkey":	"Controls",
	"key":		"Id",
	"filterid":	"Id"
}

aws_cur_report_definition = {
	"clfn":		"cur",
	"descfn":	"list_report_definitions",
	"topkey":	"ReportDefinitions",
	"key":		"ReportName",
	"filterid":	"ReportName"
}

aws_customer_gateway = {
	"clfn":		"ec2",
	"descfn":	"describe_customer_gateways",
	"topkey":	"CustomerGateways",
	"key":		"CustomerGatewayId",
	"filterid":	"CustomerGatewayId"
}

aws_customerprofiles_domain = {
	"clfn":		"customer-profiles",
	"descfn":	"list_domains",
	"topkey":	"Domains",
	"key":		"DomainName",
	"filterid":	"DomainName"
}

aws_customerprofiles_profile = {
	"clfn":		"customerprofiles",
	"descfn":	"list_profiles",
	"topkey":	"Profiles",
	"key":		"ProfileArn",
	"filterid":	"ProfileArn"
}

aws_dataexchange_data_set = {
	"clfn":		"dataexchange",
	"descfn":	"list_data_sets",
	"topkey":	"DataSets",
	"key":		"Id",
	"filterid":	"Id"
}

aws_dataexchange_revision = {
	"clfn":		"dataexchange",
	"descfn":	"list_revisions",
	"topkey":	"Revisions",
	"key":		"Id",
	"filterid":	"Id"
}

aws_datapipeline_pipeline = {
	"clfn":		"datapipeline",
	"descfn":	"list_pipelines",
	"topkey":	"Pipelines",
	"key":		"Name",
	"filterid":	"Name"
}

aws_datapipeline_pipeline_definition = {
	"clfn":		"datapipeline",
	"descfn":	"list_pipeline_definition",
	"topkey":	"PipelineDefinition",
	"key":		"Name",
	"filterid":	"Name"
}

aws_datasync_agent = {
	"clfn":		"datasync",
	"descfn":	"list_agents",
	"topkey":	"Agents",
	"key":		"AgentArn",
	"filterid":	"AgentArn"
}

aws_datasync_location_azure_blob = {
	"clfn":		"datasync",
	"descfn":	"list_location_s3",
	"topkey":	"Locations",
	"key":		"LocationArn",
	"filterid":	"LocationArn"
}

aws_datasync_location_efs = {
	"clfn":		"datasync",
	"descfn":	"list_location_efs",
	"topkey":	"Locations",
	"key":		"LocationArn",
	"filterid":	"LocationArn"
}

aws_datasync_location_fsx_lustre_file_system = {
	"clfn":		"datasync",
	"descfn":	"list_location_fsx_lustre",
	"topkey":	"Locations",
	"key":		"LocationArn",
	"filterid":	"LocationArn"
}

aws_datasync_location_fsx_ontap_file_system = {
	"clfn":		"datasync",
	"descfn":	"list_location_fsx_ontap",
	"topkey":	"Locations",
	"key":		"LocationArn",
	"filterid":	"LocationArn"
}

aws_datasync_location_fsx_openzfs_file_system = {
	"clfn":		"datasync",
	"descfn":	"list_location_fsx_openzfs",
	"topkey":	"Locations",
	"key":		"LocationArn",
	"filterid":	"LocationArn"
}

aws_datasync_location_fsx_windows_file_system = {
	"clfn":		"datasync",
	"descfn":	"list_location_fsx_windows",
	"topkey":	"Locations",
	"key":		"LocationArn",
	"filterid":	"LocationArn"
}

aws_datasync_location_hdfs = {
	"clfn":		"datasync",
	"descfn":	"list_location_hdfs",
	"topkey":	"Locations",
	"key":		"LocationArn",
	"filterid":	"LocationArn"
}

aws_datasync_location_nfs = {
	"clfn":		"datasync",
	"descfn":	"list_location_nfs",
	"topkey":	"Locations",
	"key":		"LocationArn",
	"filterid":	"LocationArn"
}

aws_datasync_location_object_storage = {
	"clfn":		"datasync",
	"descfn":	"list_location_object_storage",
	"topkey":	"Locations",
	"key":		"LocationArn",
	"filterid":	"LocationArn"
}

aws_datasync_location_s3 = {
	"clfn":		"datasync",
	"descfn":	"list_location_s3",
	"topkey":	"Locations",
	"key":		"LocationArn",
	"filterid":	"LocationArn"
}

aws_datasync_location_smb = {
	"clfn":		"datasync",
	"descfn":	"list_location_smb",
	"topkey":	"Locations",
	"key":		"LocationArn",
	"filterid":	"LocationArn"
}

aws_datasync_task = {
	"clfn":		"datasync",
	"descfn":	"list_tasks",
	"topkey":	"Tasks",
	"key":		"TaskArn",
	"filterid":	"TaskArn"
}

aws_dax_cluster = {
	"clfn":		"dax",
	"descfn":	"list_clusters",
	"topkey":	"Clusters",
	"key":		"ClusterName",
	"filterid":	"ClusterName"
}

aws_dax_parameter_group = {
	"clfn":		"dax",
	"descfn":	"list_parameter_groups",
	"topkey":	"ParameterGroups",
	"key":		"ParameterGroupName",
	"filterid":	"ParameterGroupName"
}

aws_dax_subnet_group = {
	"clfn":		"dax",
	"descfn":	"list_subnet_groups",
	"topkey":	"SubnetGroups",
	"key":		"SubnetGroupName",
	"filterid":	"SubnetGroupName"
}

aws_db_cluster_snapshot = {
	"clfn":		"rds",
	"descfn":	"describe_db_cluster_snapshots",
	"topkey":	"DBClusterSnapshots",
	"key":		"DBClusterSnapshotIdentifier",
	"filterid":	"DBClusterSnapshotIdentifier"
}

aws_db_instance = {
	"clfn":		"rds",
	"descfn":	"describe_db_instances",
	"topkey":	"DBInstances",
	"key":		"DBInstanceIdentifier",
	"filterid":	"DBInstanceIdentifier"
}

aws_db_instance_automated_backups_replication = {
	"clfn":		"rds",
	"descfn":	"describe_db_instance_automated_backups",
	"topkey":	"DBInstanceAutomatedBackups",
	"key":		"DBInstanceArn",
	"filterid":	"DBInstanceArn"
}

aws_db_instance_role_association = {
	"clfn":		"rds",
	"descfn":	"describe_db_instance_role_associations",
	"topkey":	"DBInstanceRoleAssociations",
	"key":		"DBInstanceArn",
	"filterid":	"DBInstanceArn"
}

aws_db_option_group = {
	"clfn":		"rds",
	"descfn":	"describe_option_groups",
	"topkey":	"OptionGroupsList",
	"key":		"OptionGroupName",
	"filterid":	"OptionGroupName"
}

aws_db_proxy = {
	"clfn":		"rds",
	"descfn":	"describe_db_proxies",
	"topkey":	"DBProxies",
	"key":		"DBProxyName",
	"filterid":	"DBProxyName"
}

aws_db_proxy_default_target_group = {
	"clfn":		"rds",
	"descfn":	"describe_db_proxy_default_target_groups",
	"topkey":	"DBProxyDefaultTargetGroups",
	"key":		"DBProxyName",
	"filterid":	"DBProxyName"
}

aws_db_proxy_endpoint = {
	"clfn":		"rds",
	"descfn":	"describe_db_proxy_endpoints",
	"topkey":	"DBProxyEndpoints",
	"key":		"DBProxyEndpointName",
	"filterid":	"DBProxyEndpointName"
}

aws_db_proxy_target = {
	"clfn":		"rds",
	"descfn":	"describe_db_proxy_targets",
	"topkey":	"DBProxyTargets",
	"key":		"TargetGroupName",
	"filterid":	"TargetGroupName"
}

aws_db_snapshot = {
	"clfn":		"rds",
	"descfn":	"describe_db_snapshots",
	"topkey":	"DBSnapshots",
	"key":		"DBSnapshotIdentifier",
	"filterid":	"DBSnapshotIdentifier"
}

aws_db_snapshot_copy = {
	"clfn":		"rds",
	"descfn":	"describe_db_snapshot_attributes",
	"topkey":	"DBSnapshotAttributesResult",
	"key":		"DBSnapshotIdentifier",
	"filterid":	"DBSnapshotIdentifier"
}

aws_default_vpc_dhcp_options = {
	"clfn":		"ec2",
	"descfn":	"describe_vpc_dhcp_options",
	"topkey":	"VpcDhcpOptions",
	"key":		"VpcDhcpOptionsId",
	"filterid":	"VpcDhcpOptionsId"
}

aws_detective_graph = {
	"clfn":		"detective",
	"descfn":	"list_graphs",
	"topkey":	"Graphs",
	"key":		"GraphArn",
	"filterid":	"GraphArn"
}

aws_detective_invitation_accepter = {
	"clfn":		"detective",
	"descfn":	"list_invitation_accepters",
	"topkey":	"InvitationAccepters",
	"key":		"GraphArn",
	"filterid":	"GraphArn"
}

aws_detective_member = {
	"clfn":		"detective",
	"descfn":	"list_members",
	"topkey":	"Members",
	"key":		"GraphArn",
	"filterid":	"GraphArn"
}

aws_detective_organization_admin_account = {
	"clfn":		"detective",
	"descfn":	"list_organization_admin_accounts",
	"topkey":	"OrganizationAdminAccounts",
	"key":		"GraphArn",
	"filterid":	"GraphArn"
}

aws_detective_organization_configuration = {
	"clfn":		"detective",
	"descfn":	"list_organization_configurations",
	"topkey":	"OrganizationConfigurations",
	"key":		"GraphArn",
	"filterid":	"GraphArn"
}

aws_devicefarm_device_pool = {
	"clfn":		"devicefarm",
	"descfn":	"list_device_pools",
	"topkey":	"DevicePools",
	"key":		"Arn",
	"filterid":	"Arn"
}

aws_devicefarm_instance_profile = {
	"clfn":		"devicefarm",
	"descfn":	"list_instance_profiles",
	"topkey":	"InstanceProfiles",
	"key":		"Arn",
	"filterid":	"Arn"
}

aws_devicefarm_network_profile = {
	"clfn":		"devicefarm",
	"descfn":	"list_network_profiles",
	"topkey":	"NetworkProfiles",
	"key":		"Arn",
	"filterid":	"Arn"
}

aws_devicefarm_project = {
	"clfn":		"devicefarm",
	"descfn":	"list_projects",
	"topkey":	"Projects",
	"key":		"Arn",
	"filterid":	"Arn"
}

aws_devicefarm_test_grid_project = {
	"clfn":		"devicefarm",
	"descfn":	"list_test_grid_projects",
	"topkey":	"TestGridProjects",
	"key":		"Arn",
	"filterid":	"Arn"
}

aws_devicefarm_upload = {
	"clfn":		"devicefarm",
	"descfn":	"list_uploads",
	"topkey":	"Uploads",
	"key":		"Arn",
	"filterid":	"Arn"
}

aws_directory_service_conditional_forwarder = {
	"clfn":		"ds",
	"descfn":	"list_conditional_forwarders",
	"topkey":	"ConditionalForwarders",
	"key":		"DirectoryId",
	"filterid":	"DirectoryId"
}

aws_directory_service_directory = {
	"clfn":		"ds",
	"descfn":	"list_directories",
	"topkey":	"DirectoryDescriptions",
	"key":		"DirectoryId",
	"filterid":	"DirectoryId"
}

aws_directory_service_log_subscription = {
	"clfn":		"ds",
	"descfn":	"list_log_subscriptions",
	"topkey":	"LogSubscriptions",
	"key":		"DirectoryId",
	"filterid":	"DirectoryId"
}

aws_directory_service_radius_settings = {
	"clfn":		"ds",
	"descfn":	"list_radius_settings",
	"topkey":	"RadiusSettings",
	"key":		"DirectoryId",
	"filterid":	"DirectoryId"
}

aws_directory_service_region = {
	"clfn":		"ds",
	"descfn":	"list_regions",
	"topkey":	"Regions",
	"key":		"DirectoryId",
	"filterid":	"DirectoryId"
}

aws_directory_service_shared_directory = {
	"clfn":		"ds",
	"descfn":	"list_shared_directories",
	"topkey":	"SharedDirectories",
	"key":		"SharedDirectoryId",
	"filterid":	"SharedDirectoryId"
}

aws_directory_service_trust = {
	"clfn":		"ds",
	"descfn":	"list_trusts",
	"topkey":	"Trusts",
	"key":		"TrustId",
	"filterid":	"TrustId"
}

aws_dlm_lifecycle_policy = {
	"clfn":		"dlm",
	"descfn":	"list_policies",
	"topkey":	"Policies",
	"key":		"PolicyId",
	"filterid":	"PolicyId"
}

aws_dms_certificate = {
	"clfn":		"dms",
	"descfn":	"describe_certificates",
	"topkey":	"Certificates",
	"key":		"CertificateIdentifier",
	"filterid":	"CertificateIdentifier"
}

aws_dms_endpoint = {
	"clfn":		"dms",
	"descfn":	"describe_endpoints",
	"topkey":	"Endpoints",
	"key":		"EndpointIdentifier",
	"filterid":	"EndpointIdentifier"
}

aws_dms_event_subscription = {
	"clfn":		"dms",
	"descfn":	"describe_event_subscriptions",
	"topkey":	"EventSubscriptionsList",
	"key":		"SubscriptionName",
	"filterid":	"SubscriptionName"
}

aws_dms_replication_config = {
	"clfn":		"dms",
	"descfn":	"describe_replication_configs",
	"topkey":	"ReplicationConfigs",
	"key":		"ReplicationConfigIdentifier",
	"filterid":	"ReplicationConfigIdentifier"
}

aws_dms_replication_instance = {
	"clfn":		"dms",
	"descfn":	"describe_replication_instances",
	"topkey":	"ReplicationInstances",
	"key":		"ReplicationInstanceIdentifier",
	"filterid":	"ReplicationInstanceIdentifier"
}

aws_dms_replication_subnet_group = {
	"clfn":		"dms",
	"descfn":	"describe_replication_subnet_groups",
	"topkey":	"ReplicationSubnetGroups",
	"key":		"ReplicationSubnetGroupIdentifier",
	"filterid":	"ReplicationSubnetGroupIdentifier"
}

aws_dms_replication_task = {
	"clfn":		"dms",
	"descfn":	"describe_replication_tasks",
	"topkey":	"ReplicationTasks",
	"key":		"ReplicationTaskIdentifier",
	"filterid":	"ReplicationTaskIdentifier"
}

aws_dms_s3_endpoint = {
	"clfn":		"dms",
	"descfn":	"describe_s3_endpoints",
	"topkey":	"S3Endpoints",
	"key":		"EndpointIdentifier",
	"filterid":	"EndpointIdentifier"
}

aws_docdb_cluster = {
	"clfn":		"docdb",
	"descfn":	"describe_db_clusters",
	"topkey":	"DBClusters",
	"key":		"DBClusterIdentifier",
	"filterid":	"DBClusterIdentifier"
}

aws_docdb_cluster_instance = {
	"clfn":		"docdb",
	"descfn":	"describe_db_cluster_instances",
	"topkey":	"DBClusterInstances",
	"key":		"DBClusterIdentifier",
	"filterid":	"DBClusterIdentifier"
}

aws_docdb_cluster_parameter_group = {
	"clfn":		"docdb",
	"descfn":	"describe_db_cluster_parameter_groups",
	"topkey":	"DBClusterParameterGroups",
	"key":		"DBClusterParameterGroupName",
	"filterid":	"DBClusterParameterGroupName"
}

aws_docdb_cluster_snapshot = {
	"clfn":		"docdb",
	"descfn":	"describe_db_cluster_snapshots",
	"topkey":	"DBClusterSnapshots",
	"key":		"DBClusterSnapshotIdentifier",
	"filterid":	"DBClusterSnapshotIdentifier"
}

aws_docdb_event_subscription = {
	"clfn":		"docdb",
	"descfn":	"describe_event_subscriptions",
	"topkey":	"EventSubscriptionsList",
	"key":		"SubscriptionName",
	"filterid":	"SubscriptionName"
}

aws_docdb_global_cluster = {
	"clfn":		"docdb",
	"descfn":	"describe_global_clusters",
	"topkey":	"GlobalClusters",
	"key":		"GlobalClusterIdentifier",
	"filterid":	"GlobalClusterIdentifier"
}

aws_docdb_subnet_group = {
	"clfn":		"docdb",
	"descfn":	"describe_db_subnet_groups",
	"topkey":	"DBSubnetGroups",
	"key":		"DBSubnetGroupName",
	"filterid":	"DBSubnetGroupName"
}

aws_docdbelastic_cluster = {
	"clfn":		"docdb-elastic",
	"descfn":	"describe_clusters",
	"topkey":	"Clusters",
	"key":		"ClusterName",
	"filterid":	"ClusterName"
}

aws_dx_bgp_peer = {
	"clfn":		"directconnect",
	"descfn":	"describe_bgp_peers",
	"topkey":	"BgpPeers",
	"key":		"BgpPeerId",
	"filterid":	"BgpPeerId"
}

aws_dx_connection = {
	"clfn":		"directconnect",
	"descfn":	"describe_connections",
	"topkey":	"Connections",
	"key":		"ConnectionId",
	"filterid":	"ConnectionId"
}

aws_dx_connection_association = {
	"clfn":		"directconnect",
	"descfn":	"describe_connection_associations",
	"topkey":	"ConnectionAssociations",
	"key":		"ConnectionId",
	"filterid":	"ConnectionId"
}

aws_dx_connection_confirmation = {
	"clfn":		"directconnect",
	"descfn":	"describe_confirmations",
	"topkey":	"Confirmations",
	"key":		"ConfirmationToken",
	"filterid":	"ConfirmationToken"
}

aws_dx_gateway = {
	"clfn":		"directconnect",
	"descfn":	"describe_gateways",
	"topkey":	"Gateways",
	"key":		"GatewayId",
	"filterid":	"GatewayId"
}

aws_dx_gateway_association = {
	"clfn":		"directconnect",
	"descfn":	"describe_gateway_associations",
	"topkey":	"GatewayAssociations",
	"key":		"GatewayId",
	"filterid":	"GatewayId"
}

aws_dx_gateway_association_proposal = {
	"clfn":		"directconnect",
	"descfn":	"describe_gateway_association_proposals",
	"topkey":	"GatewayAssociationProposals",
	"key":		"GatewayId",
	"filterid":	"GatewayId"
}

aws_dx_hosted_connection = {
	"clfn":		"directconnect",
	"descfn":	"describe_gateway_association_proposals",
	"topkey":	"GatewayAssociationProposals",
	"key":		"ProposalId",
	"filterid":	"ProposalId"
}

aws_dx_hosted_private_virtual_interface = {
	"clfn":		"directconnect",
	"descfn":	"describe_hosted_private_virtual_interfaces",
	"topkey":	"VirtualInterfaces",
	"key":		"VirtualInterfaceId",
	"filterid":	"VirtualInterfaceId"
}

aws_dx_hosted_private_virtual_interface_accepter = {
	"clfn":		"directconnect",
	"descfn":	"describe_hosted_private_virtual_interfaces",
	"topkey":	"VirtualInterfaces",
	"key":		"VirtualInterfaceId",
	"filterid":	"VirtualInterfaceId"
}

aws_dx_hosted_public_virtual_interface = {
	"clfn":		"directconnect",
	"descfn":	"describe_hosted_public_virtual_interfaces",
	"topkey":	"VirtualInterfaces",
	"key":		"VirtualInterfaceId",
	"filterid":	"VirtualInterfaceId"
}

aws_dx_hosted_public_virtual_interface_accepter = {
	"clfn":		"directconnect",
	"descfn":	"describe_hosted_public_virtual_interfaces",
	"topkey":	"VirtualInterfaces",
	"key":		"VirtualInterfaceId",
	"filterid":	"VirtualInterfaceId"
}

aws_dx_hosted_transit_virtual_interface = {
	"clfn":		"directconnect",
	"descfn":	"describe_hosted_transit_virtual_interfaces",
	"topkey":	"VirtualInterfaces",
	"key":		"VirtualInterfaceId",
	"filterid":	"VirtualInterfaceId"
}

aws_dx_hosted_transit_virtual_interface_accepter = {
	"clfn":		"directconnect",
	"descfn":	"describe_hosted_transit_virtual_interfaces",
	"topkey":	"VirtualInterfaces",
	"key":		"VirtualInterfaceId",
	"filterid":	"VirtualInterfaceId"
}

aws_dx_lag = {
	"clfn":		"directconnect",
	"descfn":	"describe_lags",
	"topkey":	"Lags",
	"key":		"LagId",
	"filterid":	"LagId"
}

aws_dx_macsec_key_association = {
	"clfn":		"directconnect",
	"descfn":	"describe_macsec_key_associations",
	"topkey":	"MacsecKeyAssociations",
	"key":		"AssociationId",
	"filterid":	"AssociationId"
}

aws_dx_private_virtual_interface = {
	"clfn":		"directconnect",
	"descfn":	"describe_private_virtual_interfaces",
	"topkey":	"VirtualInterfaces",
	"key":		"VirtualInterfaceId",
	"filterid":	"VirtualInterfaceId"
}

aws_dx_public_virtual_interface = {
	"clfn":		"directconnect",
	"descfn":	"describe_public_virtual_interfaces",
	"topkey":	"VirtualInterfaces",
	"key":		"VirtualInterfaceId",
	"filterid":	"VirtualInterfaceId"
}

aws_dx_transit_virtual_interface = {
	"clfn":		"directconnect",
	"descfn":	"describe_transit_virtual_interfaces",
	"topkey":	"VirtualInterfaces",
	"key":		"VirtualInterfaceId",
	"filterid":	"VirtualInterfaceId"
}

aws_dynamodb_contributor_insights = {
	"clfn":		"dynamodb",
	"descfn":	"describe_contributor_insights",
	"topkey":	"ContributorInsightsList",
	"key":		"ContributorInsightsArn",
	"filterid":	"ContributorInsightsArn"
}

aws_dynamodb_global_table = {
	"clfn":		"dynamodb",
	"descfn":	"describe_global_tables",
	"topkey":	"GlobalTables",
	"key":		"GlobalTableName",
	"filterid":	"GlobalTableName"
}

aws_dynamodb_kinesis_streaming_destination = {
	"clfn":		"dynamodb",
	"descfn":	"describe_kinesis_streaming_destination",
	"topkey":	"KinesisStreamingDestination",
	"key":		"TableName",
	"filterid":	"TableName"
}

aws_dynamodb_table = {
	"clfn":		"dynamodb",
	"descfn":	"describe_table",
	"topkey":	"Table",
	"key":		"TableName",
	"filterid":	"TableName"
}

aws_dynamodb_table_item = {
	"clfn":		"dynamodb",
	"descfn":	"describe_table",
	"topkey":	"Table",
	"key":		"TableName",
	"filterid":	"TableName"
}

aws_dynamodb_table_replica = {
	"clfn":		"dynamodb",
	"descfn":	"describe_table_replica_auto_scaling",
	"topkey":	"TableReplicaAutoScalingDescription",
	"key":		"TableName",
	"filterid":	"TableName"
}

aws_dynamodb_tag = {
	"clfn":		"dynamodb",
	"descfn":	"list_tags_of_resource",
	"topkey":	"Tags",
	"key":		"Key",
	"filterid":	"Key"
}

aws_ebs_default_kms_key = {
	"clfn":		"ebs",
	"descfn":	"describe_default_kms_key",
	"topkey":	"DefaultKmsKeyId",
	"key":		"DefaultKmsKeyId",
	"filterid":	"DefaultKmsKeyId"
}

aws_ebs_encryption_by_default = {
	"clfn":		"ebs",
	"descfn":	"describe_ebs_encryption_by_default",
	"topkey":	"EbsEncryptionByDefault",
	"key":		"EbsEncryptionByDefault",
	"filterid":	"EbsEncryptionByDefault"
}

aws_ebs_snapshot = {
	"clfn":		"ebs",
	"descfn":	"describe_snapshots",
	"topkey":	"Snapshots",
	"key":		"SnapshotId",
	"filterid":	"SnapshotId"
}

aws_ebs_snapshot_copy = {
	"clfn":		"ebs",
	"descfn":	"describe_snapshot_copy_grants",
	"topkey":	"SnapshotCopyGrants",
	"key":		"SnapshotCopyGrantName",
	"filterid":	"SnapshotCopyGrantName"
}

aws_ebs_snapshot_import = {
	"clfn":		"ebs",
	"descfn":	"describe_snapshot_import_tasks",
	"topkey":	"SnapshotTasks",
	"key":		"SnapshotTaskIdentifier",
	"filterid":	"SnapshotTaskIdentifier"
}

aws_ebs_volume = {
	"clfn":		"ebs",
	"descfn":	"describe_volumes",
	"topkey":	"Volumes",
	"key":		"VolumeId",
	"filterid":	"VolumeId"
}

aws_ec2_availability_zone_group = {
	"clfn":		"ec2",
	"descfn":	"describe_availability_zone_groups",
	"topkey":	"AvailabilityZoneGroups",
	"key":		"GroupName",
	"filterid":	"GroupName"
}

aws_ec2_capacity_reservation = {
	"clfn":		"ec2",
	"descfn":	"describe_capacity_reservations",
	"topkey":	"CapacityReservations",
	"key":		"CapacityReservationId",
	"filterid":	"CapacityReservationId"
}

aws_ec2_carrier_gateway = {
	"clfn":		"ec2",
	"descfn":	"describe_carrier_gateways",
	"topkey":	"CarrierGateways",
	"key":		"CarrierGatewayId",
	"filterid":	"CarrierGatewayId"
}

aws_ec2_client_vpn_authorization_rule = {
	"clfn":		"ec2",
	"descfn":	"describe_client_vpn_authorization_rules",
	"topkey":	"AuthorizationRules",
	"key":		"ClientVpnEndpointId",
	"filterid":	"ClientVpnEndpointId"
}

aws_ec2_client_vpn_endpoint = {
	"clfn":		"ec2",
	"descfn":	"describe_client_vpn_endpoints",
	"topkey":	"ClientVpnEndpoints",
	"key":		"ClientVpnEndpointId",
	"filterid":	"ClientVpnEndpointId"
}

aws_ec2_client_vpn_network_association = {
	"clfn":		"ec2",
	"descfn":	"describe_client_vpn_network_associations",
	"topkey":	"Associations",
	"key":		"ClientVpnEndpointId",
	"filterid":	"ClientVpnEndpointId"
}

aws_ec2_client_vpn_route = {
	"clfn":		"ec2",
	"descfn":	"describe_client_vpn_routes",
	"topkey":	"Routes",
	"key":		"ClientVpnEndpointId",
	"filterid":	"ClientVpnEndpointId"
}

aws_ec2_fleet = {
	"clfn":		"ec2",
	"descfn":	"describe_fleets",
	"topkey":	"Fleets",
	"key":		"FleetId",
	"filterid":	"FleetId"
}

aws_ec2_host = {
	"clfn":		"ec2",
	"descfn":	"describe_hosts",
	"topkey":	"Hosts",
	"key":		"HostId",
	"filterid":	"HostId"
}

aws_ec2_image_block_public_access = {
	"clfn":		"ec2",
	"descfn":	"describe_image_attribute",
	"topkey":	"ImageAttribute",
	"key":		"ImageId",
	"filterid":	"ImageId"
}

aws_ec2_instance_connect_endpoint = {
	"clfn":		"ec2",
	"descfn":	"describe_instance_connect_endpoints",
	"topkey":	"InstanceConnectEndpoints",
	"key":		"InstanceConnectEndpointId",
	"filterid":	"InstanceConnectEndpointId"
}

aws_ec2_instance_state = {
	"clfn":		"ec2",
	"descfn":	"describe_instance_status",
	"topkey":	"InstanceStatuses",
	"key":		"InstanceId",
	"filterid":	"InstanceId"
}

aws_ec2_local_gateway_route = {
	"clfn":		"ec2",
	"descfn":	"describe_local_gateway_routes",
	"topkey":	"LocalGatewayRoutes",
	"key":		"LocalGatewayRouteTableId",
	"filterid":	"LocalGatewayRouteTableId"
}

aws_ec2_local_gateway_route_table_vpc_association = {
	"clfn":		"ec2",
	"descfn":	"describe_local_gateway_route_tables",
	"topkey":	"LocalGatewayRouteTables",
	"key":		"LocalGatewayRouteTableId",
	"filterid":	"LocalGatewayRouteTableId"
}

aws_ec2_managed_prefix_list = {
	"clfn":		"ec2",
	"descfn":	"describe_managed_prefix_lists",
	"topkey":	"PrefixLists",
	"key":		"PrefixListId",
	"filterid":	"PrefixListId"
}

aws_ec2_managed_prefix_list_entry = {
	"clfn":		"ec2",
	"descfn":	"describe_managed_prefix_list_entries",
	"topkey":	"Entries",
	"key":		"PrefixListId",
	"filterid":	"PrefixListId"
}

aws_ec2_subnet_cidr_reservation = {
	"clfn":		"ec2",
	"descfn":	"describe_subnet_cidr_reservations",
	"topkey":	"SubnetCidrReservations",
	"key":		"SubnetCidrReservationId",
	"filterid":	"SubnetCidrReservationId"
}

aws_ec2_tag = {
	"clfn":		"ec2",
	"descfn":	"describe_tags",
	"topkey":	"Tags",
	"key":		"ResourceId",
	"filterid":	"ResourceId"
}

aws_ec2_traffic_mirror_filter = {
	"clfn":		"ec2",
	"descfn":	"describe_traffic_mirror_filters",
	"topkey":	"TrafficMirrorFilters",
	"key":		"TrafficMirrorFilterId",
	"filterid":	"TrafficMirrorFilterId"
}

aws_ec2_traffic_mirror_filter_rule = {
	"clfn":		"ec2",
	"descfn":	"describe_traffic_mirror_filter_rules",
	"topkey":	"TrafficMirrorFilterRules",
	"key":		"TrafficMirrorFilterRuleId",
	"filterid":	"TrafficMirrorFilterRuleId"
}

aws_ec2_traffic_mirror_session = {
	"clfn":		"ec2",
	"descfn":	"describe_traffic_mirror_sessions",
	"topkey":	"TrafficMirrorSessions",
	"key":		"TrafficMirrorSessionId",
	"filterid":	"TrafficMirrorSessionId"
}

aws_ec2_traffic_mirror_target = {
	"clfn":		"ec2",
	"descfn":	"describe_traffic_mirror_targets",
	"topkey":	"TrafficMirrorTargets",
	"key":		"TrafficMirrorTargetId",
	"filterid":	"TrafficMirrorTargetId"
}

aws_ec2_transit_gateway = {
	"clfn":		"ec2",
	"descfn":	"describe_transit_gateways",
	"topkey":	"TransitGateways",
	"key":		"TransitGatewayId",
	"filterid":	"TransitGatewayId"
}

aws_ec2_transit_gateway_connect = {
	"clfn":		"ec2",
	"descfn":	"describe_transit_gateway_connects",
	"topkey":	"TransitGatewayConnects",
	"key":		"TransitGatewayConnectId",
	"filterid":	"TransitGatewayConnectId"
}

aws_ec2_transit_gateway_connect_peer = {
	"clfn":		"ec2",
	"descfn":	"describe_transit_gateway_connect_peers",
	"topkey":	"TransitGatewayConnectPeers",
	"key":		"TransitGatewayConnectPeerId",
	"filterid":	"TransitGatewayConnectPeerId"
}

aws_ec2_transit_gateway_multicast_domain = {
	"clfn":		"ec2",
	"descfn":	"describe_transit_gateway_multicast_domains",
	"topkey":	"TransitGatewayMulticastDomains",
	"key":		"TransitGatewayMulticastDomainId",
	"filterid":	"TransitGatewayMulticastDomainId"
}

aws_ec2_transit_gateway_multicast_domain_association = {
	"clfn":		"ec2",
	"descfn":	"describe_transit_gateway_multicast_domains",
	"topkey":	"TransitGatewayMulticastDomains",
	"key":		"TransitGatewayMulticastDomainId",
	"filterid":	"TransitGatewayMulticastDomainId"
}

aws_ec2_transit_gateway_multicast_group_member = {
	"clfn":		"ec2",
	"descfn":	"describe_transit_gateway_multicast_groups",
	"topkey":	"TransitGatewayMulticastGroups",
	"key":		"TransitGatewayMulticastGroupId",
	"filterid":	"TransitGatewayMulticastGroupId"
}

aws_ec2_transit_gateway_multicast_group_source = {
	"clfn":		"ec2",
	"descfn":	"describe_transit_gateway_multicast_groups",
	"topkey":	"TransitGatewayMulticastGroups",
	"key":		"TransitGatewayMulticastGroupId",
	"filterid":	"TransitGatewayMulticastGroupId"
}

aws_ec2_transit_gateway_peering_attachment = {
	"clfn":		"ec2",
	"descfn":	"describe_transit_gateway_peering_attachments",
	"topkey":	"TransitGatewayPeeringAttachments",
	"key":		"TransitGatewayPeeringAttachmentId",
	"filterid":	"TransitGatewayPeeringAttachmentId"
}

aws_ec2_transit_gateway_peering_attachment_accepter = {
	"clfn":		"ec2",
	"descfn":	"describe_transit_gateway_peering_attachments",
	"topkey":	"TransitGatewayPeeringAttachments",
	"key":		"TransitGatewayPeeringAttachmentId",
	"filterid":	"TransitGatewayPeeringAttachmentId"
}

aws_ec2_transit_gateway_policy_table = {
	"clfn":		"ec2",
	"descfn":	"describe_transit_gateway_policy_tables",
	"topkey":	"TransitGatewayPolicyTables",
	"key":		"TransitGatewayPolicyTableId",
	"filterid":	"TransitGatewayPolicyTableId"
}

aws_ec2_transit_gateway_policy_table_association = {
	"clfn":		"ec2",
	"descfn":	"describe_transit_gateway_policy_table_associations",
	"topkey":	"TransitGatewayPolicyTableAssociations",
	"key":		"TransitGatewayPolicyTableAssociationId",
	"filterid":	"TransitGatewayPolicyTableAssociationId"
}

aws_ec2_transit_gateway_prefix_list_reference = {
	"clfn":		"ec2",
	"descfn":	"describe_transit_gateway_prefix_list_references",
	"topkey":	"TransitGatewayPrefixListReferences",
	"key":		"TransitGatewayPrefixListReferenceId",
	"filterid":	"TransitGatewayPrefixListReferenceId"
}

aws_ec2_transit_gateway_route = {
	"clfn":		"ec2",
	"descfn":	"describe_transit_gateway_routes",
	"topkey":	"TransitGatewayRoutes",
	"key":		"TransitGatewayRouteId",
	"filterid":	"TransitGatewayRouteId"
}

aws_ec2_transit_gateway_route_table = {
	"clfn":		"ec2",
	"descfn":	"describe_transit_gateway_route_tables",
	"topkey":	"TransitGatewayRouteTables",
	"key":		"TransitGatewayRouteTableId",
	"filterid":	"TransitGatewayRouteTableId"
}

aws_ec2_transit_gateway_route_table_association = {
	"clfn":		"ec2",
	"descfn":	"describe_transit_gateway_route_table_associations",
	"topkey":	"TransitGatewayRouteTableAssociations",
	"key":		"TransitGatewayRouteTableAssociationId",
	"filterid":	"TransitGatewayRouteTableAssociationId"
}

aws_ec2_transit_gateway_vpc_attachment = {
	"clfn":		"ec2",
	"descfn":	"describe_transit_gateway_vpc_attachments",
	"topkey":	"TransitGatewayVpcAttachments",
	"key":		"TransitGatewayVpcAttachmentId",
	"filterid":	"TransitGatewayVpcAttachmentId"
}

aws_ec2_transit_gateway_vpc_attachment_accepter = {
	"clfn":		"ec2",
	"descfn":	"describe_transit_gateway_vpc_attachments",
	"topkey":	"TransitGatewayVpcAttachments",
	"key":		"TransitGatewayVpcAttachmentId",
	"filterid":	"TransitGatewayVpcAttachmentId"
}

aws_ecr_lifecycle_policy = {
	"clfn":		"ecr",
	"descfn":	"describe_lifecycle_policy",
	"topkey":	"lifecyclePolicyText",
	"key":		"lifecyclePolicyText",
	"filterid":	"lifecyclePolicyText"
}

aws_ecr_pull_through_cache_rule = {
	"clfn":		"ecr",
	"descfn":	"describe_pull_through_cache_rules",
	"topkey":	"pullThroughCacheRules",
	"key":		"registryId",
	"filterid":	"registryId"
}

aws_ecr_registry_policy = {
	"clfn":		"ecr",
	"descfn":	"describe_registry_policy",
	"topkey":	"registryPolicyText",
	"key":		"registryPolicyText",
	"filterid":	"registryPolicyText"
}

aws_ecr_registry_scanning_configuration = {
	"clfn":		"ecr",
	"descfn":	"describe_registry_scanning_configuration",
	"topkey":	"registryScanningConfiguration",
	"key":		"registryScanningConfiguration",
	"filterid":	"registryScanningConfiguration"
}

aws_ecr_replication_configuration = {
	"clfn":		"ecr",
	"descfn":	"describe_replication_configuration",
	"topkey":	"replicationConfiguration",
	"key":		"replicationConfiguration",
	"filterid":	"replicationConfiguration"
}

aws_ecr_repository = {
	"clfn":		"ecr",
	"descfn":	"describe_repositories",
	"topkey":	"repositories",
	"key":		"repositoryName",
	"filterid":	"repositoryName"
}

aws_ecr_repository_policy = {
	"clfn":		"ecr",
	"descfn":	"get_repository_policy",
	"topkey":	"policyText",
	"key":		"policyText",
	"filterid":	"policyText"
}

aws_ecrpublic_repository = {
	"clfn":		"ecr",
	"descfn":	"describe_repositories",
	"topkey":	"repositories",
	"key":		"repositoryName",
	"filterid":	"repositoryName"
}

aws_ecrpublic_repository_policy = {
	"clfn":		"ecr",
	"descfn":	"describe_repository_policy",
	"topkey":	"policyText",
	"key":		"policyText",
	"filterid":	"policyText"
}

aws_ecs_account_setting_default = {
	"clfn":		"ecs",
	"descfn":	"list_account_settings",
	"topkey":	"settings",
	"key":		"name",
	"filterid":	"name"
}

aws_ecs_capacity_provider = {
	"clfn":		"ecs",
	"descfn":	"describe_capacity_providers",
	"topkey":	"capacityProviders",
	"key":		"name",
	"filterid":	"name"
}

aws_ecs_cluster_capacity_providers = {
	"clfn":		"ecs",
	"descfn":	"describe_clusters",
	"topkey":	"clusters",
	"key":		"clusterName",
	"filterid":	"clusterName"
}

aws_ecs_service = {
	"clfn":		"ecs",
	"descfn":	"list_services",
	"topkey":	"serviceArns",
	"key":		"cluster",
	"filterid":	"cluster"
}

aws_ecs_tag = {
	"clfn":		"ecs",
	"descfn":	"list_tags_for_resource",
	"topkey":	"tags",
	"key":		"key",
	"filterid":	"key"
}

aws_ecs_task_definition = {
	"clfn":		"ecs",
	"descfn":	"describe_task_definition",
	"topkey":	"taskDefinition",
	"key":		"taskDefinition",
	"filterid":	"taskDefinition"
}

aws_ecs_task_set = {
	"clfn":		"ecs",
	"descfn":	"describe_task_sets",
	"topkey":	"taskSets",
	"key":		"id",
	"filterid":	"id"
}

aws_efs_access_point = {
	"clfn":		"efs",
	"descfn":	"describe_access_points",
	"topkey":	"AccessPoints",
	"key":		"AccessPointId",
	"filterid":	"AccessPointId"
}

aws_efs_backup_policy = {
	"clfn":		"efs",
	"descfn":	"describe_backup_policy",
	"topkey":	"BackupPolicy",
	"key":		"BackupPolicy",
	"filterid":	"BackupPolicy"
}

aws_efs_file_system = {
	"clfn":		"efs",
	"descfn":	"describe_file_systems",
	"topkey":	"FileSystems",
	"key":		"FileSystemId",
	"filterid":	"FileSystemId"
}

aws_efs_file_system_policy = {
	"clfn":		"efs",
	"descfn":	"describe_file_system_policy",
	"topkey":	"Policy",
	"key":		"Policy",
	"filterid":	"Policy"
}

aws_efs_mount_target = {
	"clfn":		"efs",
	"descfn":	"describe_mount_targets",
	"topkey":	"MountTargets",
	"key":		"MountTargetId",
	"filterid":	"MountTargetId"
}

aws_efs_replication_configuration = {
	"clfn":		"efs",
	"descfn":	"describe_replication_configuration",
	"topkey":	"ReplicationConfiguration",
	"key":		"ReplicationConfiguration",
	"filterid":	"ReplicationConfiguration"
}

aws_egress_only_internet_gateway = {
	"clfn":		"ec2",
	"descfn":	"describe_egress_only_internet_gateways",
	"topkey":	"EgressOnlyInternetGateways",
	"key":		"EgressOnlyInternetGatewayId",
	"filterid":	"EgressOnlyInternetGatewayId"
}

aws_eip = {
	"clfn":		"ec2",
	"descfn":	"describe_addresses",
	"topkey":	"Addresses",
	"key":		"PublicIp",
	"filterid":	"PublicIp"
}

aws_eip_association = {
	"clfn":		"ec2",
	"descfn":	"describe_addresses",
	"topkey":	"Addresses",
	"key":		"PublicIp",
	"filterid":	"PublicIp"
}

aws_eks_pod_identity_association = {
	"clfn":		"eks",
	"descfn":	"describe_pod_identity_association",
	"topkey":	"podIdentity",
	"key":		"podIdentityArn",
	"filterid":	"podIdentityArn"
}

aws_elastic_beanstalk_application = {
	"clfn":		"elasticbeanstalk",
	"descfn":	"describe_applications",
	"topkey":	"Applications",
	"key":		"ApplicationName",
	"filterid":	"ApplicationName"
}

aws_elastic_beanstalk_application_version = {
	"clfn":		"elasticbeanstalk",
	"descfn":	"describe_application_versions",
	"topkey":	"ApplicationVersions",
	"key":		"VersionLabel",
	"filterid":	"VersionLabel"
}

aws_elastic_beanstalk_configuration_template = {
	"clfn":		"elasticbeanstalk",
	"descfn":	"describe_configuration_settings",
	"topkey":	"ConfigurationSettings",
	"key":		"ApplicationName",
	"filterid":	"ApplicationName"
}

aws_elastic_beanstalk_environment = {
	"clfn":		"elasticbeanstalk",
	"descfn":	"describe_environments",
	"topkey":	"Environments",
	"key":		"EnvironmentName",
	"filterid":	"EnvironmentName"
}


aws_elasticache_cluster = {
	"clfn":		"elasticache",
	"descfn":	"describe_cache_clusters",
	"topkey":	"CacheClusters",
	"key":		"CacheClusterId",
	"filterid":	"CacheClusterId"
}

aws_elasticache_global_replication_group = {
	"clfn":		"elasticache",
	"descfn":	"describe_global_replication_groups",
	"topkey":	"GlobalReplicationGroups",
	"key":		"GlobalReplicationGroupId",
	"filterid":	"GlobalReplicationGroupId"
}

aws_elasticache_parameter_group = {
	"clfn":		"elasticache",
	"descfn":	"describe_cache_parameter_groups",
	"topkey":	"CacheParameterGroups",
	"key":		"CacheParameterGroupName",
	"filterid":	"CacheParameterGroupName"
}

aws_elasticache_replication_group = {
	"clfn":		"elasticache",
	"descfn":	"describe_replication_groups",
	"topkey":	"ReplicationGroups",
	"key":		"ReplicationGroupId",
	"filterid":	"ReplicationGroupId"
}

aws_elasticache_subnet_group = {
	"clfn":		"elasticache",
	"descfn":	"describe_cache_subnet_groups",
	"topkey":	"CacheSubnetGroups",
	"key":		"CacheSubnetGroupName",
	"filterid":	"CacheSubnetGroupName"
}

aws_elasticache_user = {
	"clfn":		"elasticache",
	"descfn":	"describe_users",
	"topkey":	"Users",
	"key":		"UserId",
	"filterid":	"UserId"
}

aws_elasticache_user_group = {
	"clfn":		"elasticache",
	"descfn":	"describe_user_groups",
	"topkey":	"UserGroups",
	"key":		"UserGroupId",
	"filterid":	"UserGroupId"
}

aws_elasticache_user_group_association = {
	"clfn":		"elasticache",
	"descfn":	"describe_user_group_memberships",
	"topkey":	"UserGroupMemberships",
	"key":		"UserGroupId",
	"filterid":	"UserGroupId"
}

aws_elasticsearch_domain = {
	"clfn":		"es",
	"descfn":	"describe_elasticsearch_domains",
	"topkey":	"DomainStatusList",
	"key":		"DomainName",
	"filterid":	"DomainName"
}

aws_elasticsearch_domain_policy = {
	"clfn":		"es",
	"descfn":	"describe_elasticsearch_domain_policy",
	"topkey":	"Policy",
	"key":		"Policy",
	"filterid":	"Policy"
}

aws_elasticsearch_vpc_endpoint = {
	"clfn":		"es",
	"descfn":	"describe_vpc_endpoints",
	"topkey":	"VpcEndpoints",
	"key":		"VpcEndpointId",
	"filterid":	"VpcEndpointId"
}

aws_elastictranscoder_pipeline = {
	"clfn":		"elastictranscoder",
	"descfn":	"list_pipelines",
	"topkey":	"Pipelines",
	"key":		"Id",
	"filterid":	"Id"
}

aws_elastictranscoder_preset = {
	"clfn":		"elastictranscoder",
	"descfn":	"list_presets",
	"topkey":	"Presets",
	"key":		"Id",
	"filterid":	"Id"
}

aws_elb = {
	"clfn":		"elb",
	"descfn":	"describe_load_balancers",
	"topkey":	"LoadBalancerDescriptions",
	"key":		"LoadBalancerName",
	"filterid":	"LoadBalancerName"
}

aws_elb_attachment = {
	"clfn":		"elb",
	"descfn":	"describe_load_balancer_attributes",
	"topkey":	"LoadBalancerAttributes",
	"key":		"LoadBalancerName",
	"filterid":	"LoadBalancerName"
}

aws_emr_block_public_access_configuration = {
	"clfn":		"emr",
	"descfn":	"describe_block_public_access_configurations",
	"topkey":	"BlockPublicAccessConfigurations",
	"key":		"Id",
	"filterid":	"Id"
}

aws_emr_cluster = {
	"clfn":		"emr",
	"descfn":	"describe_cluster",
	"topkey":	"Cluster",
	"key":		"Id",
	"filterid":	"Id"
}

aws_emr_instance_fleet = {
	"clfn":		"emr",
	"descfn":	"describe_instance_fleets",
	"topkey":	"InstanceFleets",
	"key":		"Id",
	"filterid":	"Id"
}

aws_emr_instance_group = {
	"clfn":		"emr",
	"descfn":	"describe_instance_groups",
	"topkey":	"InstanceGroups",
	"key":		"Id",
	"filterid":	"Id"
}

aws_emr_managed_scaling_policy = {
	"clfn":		"emr",
	"descfn":	"describe_managed_scaling_policies",
	"topkey":	"ManagedScalingPolicies",
	"key":		"Id",
	"filterid":	"Id"
}

aws_emr_security_configuration = {
	"clfn":		"emr",
	"descfn":	"describe_security_configurations",
	"topkey":	"SecurityConfigurations",
	"key":		"Name",
	"filterid":	"Name"
}

aws_emr_studio = {
	"clfn":		"emr",
	"descfn":	"describe_studios",
	"topkey":	"Studios",
	"key":		"Id",
	"filterid":	"Id"
}

aws_emr_studio_session_mapping = {
	"clfn":		"emr",
	"descfn":	"describe_studio_session_mappings",
	"topkey":	"SessionMappings",
	"key":		"Id",
	"filterid":	"Id"
}

aws_emrcontainers_job_template = {
	"clfn":		"emr-containers",
	"descfn":	"list_job_templates",
	"topkey":	"JobTemplates",
	"key":		"Id",
	"filterid":	"Id"
}

aws_emrcontainers_virtual_cluster = {
	"clfn":		"emr-containers",
	"descfn":	"list_virtual_clusters",
	"topkey":	"VirtualClusters",
	"key":		"Id",
	"filterid":	"Id"
}

aws_emrserverless_application = {
	"clfn":		"emr-serverless",
	"descfn":	"list_applications",
	"topkey":	"Applications",
	"key":		"Id",
	"filterid":	"Id"
}

aws_evidently_feature = {
	"clfn":		"evidently",
	"descfn":	"list_features",
	"topkey":	"Features",
	"key":		"Name",
	"filterid":	"Name"
}

aws_evidently_launch = {
	"clfn":		"evidently",
	"descfn":	"list_launches",
	"topkey":	"Launches",
	"key":		"Name",
	"filterid":	"Name"
}

aws_evidently_project = {
	"clfn":		"evidently",
	"descfn":	"list_projects",
	"topkey":	"Projects",
	"key":		"Name",
	"filterid":	"Name"
}

aws_evidently_segment = {
	"clfn":		"evidently",
	"descfn":	"list_segments",
	"topkey":	"Segments",
	"key":		"Name",
	"filterid":	"Name"
}

aws_finspace_kx_cluster = {
	"clfn":		"finspace",
	"descfn":	"list_clusters",
	"topkey":	"Clusters",
	"key":		"ClusterId",
	"filterid":	"ClusterId"
}

aws_finspace_kx_database = {
	"clfn":		"finspace",
	"descfn":	"list_databases",
	"topkey":	"Databases",
	"key":		"DatabaseId",
	"filterid":	"DatabaseId"
}

aws_finspace_kx_dataview = {
	"clfn":		"finspace",
	"descfn":	"list_data_views",
	"topkey":	"DataViews",
	"key":		"DataViewId",
	"filterid":	"DataViewId"
}

aws_finspace_kx_environment = {
	"clfn":		"finspace",
	"descfn":	"list_environments",
	"topkey":	"Environments",
	"key":		"EnvironmentId",
	"filterid":	"EnvironmentId"
}

aws_finspace_kx_scaling_group = {
	"clfn":		"finspace",
	"descfn":	"list_scaling_groups",
	"topkey":	"ScalingGroups",
	"key":		"ScalingGroupId",
	"filterid":	"ScalingGroupId"
}

aws_finspace_kx_user = {
	"clfn":		"finspace",
	"descfn":	"list_users",
	"topkey":	"Users",
	"key":		"UserId",
	"filterid":	"UserId"
}

aws_finspace_kx_volume = {
	"clfn":		"finspace",
	"descfn":	"list_volumes",
	"topkey":	"Volumes",
	"key":		"VolumeId",
	"filterid":	"VolumeId"
}

aws_fis_experiment_template = {
	"clfn":		"fis",
	"descfn":	"list_experiment_templates",
	"topkey":	"ExperimentTemplates",
	"key":		"Id",
	"filterid":	"Id"
}

aws_fms_admin_account = {
	"clfn":		"fms",
	"descfn":	"list_admin_accounts",
	"topkey":	"AdminAccounts",
	"key":		"AdminAccountId",
	"filterid":	"AdminAccountId"
}

aws_fms_policy = {
	"clfn":		"fms",
	"descfn":	"list_policies",
	"topkey":	"PolicyList",
	"key":		"PolicyId",
	"filterid":	"PolicyId"
}

aws_fsx_backup = {
	"clfn":		"fsx",
	"descfn":	"describe_backups",
	"topkey":	"Backups",
	"key":		"BackupId",
	"filterid":	"BackupId"
}

aws_fsx_data_repository_association = {
	"clfn":		"fsx",
	"descfn":	"describe_data_repository_associations",
	"topkey":	"DataRepositoryAssociations",
	"key":		"AssociationId",
	"filterid":	"AssociationId"
}

aws_fsx_file_cache = {
	"clfn":		"fsx",
	"descfn":	"describe_file_caches",
	"topkey":	"FileCaches",
	"key":		"FileCacheId",
	"filterid":	"FileCacheId"
}

aws_fsx_lustre_file_system = {
	"clfn":		"fsx",
	"descfn":	"describe_file_systems",
	"topkey":	"FileSystems",
	"key":		"FileSystemId",
	"filterid":	"FileSystemId"
}

aws_fsx_ontap_file_system = {
	"clfn":		"fsx",
	"descfn":	"describe_file_systems",
	"topkey":	"FileSystems",
	"key":		"FileSystemId",
	"filterid":	"FileSystemId"
}

aws_fsx_ontap_storage_virtual_machine = {
	"clfn":		"fsx",
	"descfn":	"describe_storage_virtual_machines",
	"topkey":	"StorageVirtualMachines",
	"key":		"StorageVirtualMachineId",
	"filterid":	"StorageVirtualMachineId"
}

aws_fsx_ontap_volume = {
	"clfn":		"fsx",
	"descfn":	"describe_volumes",
	"topkey":	"Volumes",
	"key":		"VolumeId",
	"filterid":	"VolumeId"
}

aws_fsx_openzfs_file_system = {
	"clfn":		"fsx",
	"descfn":	"describe_file_systems",
	"topkey":	"FileSystems",
	"key":		"FileSystemId",
	"filterid":	"FileSystemId"
}

aws_fsx_openzfs_snapshot = {
	"clfn":		"fsx",
	"descfn":	"describe_snapshots",
	"topkey":	"Snapshots",
	"key":		"SnapshotId",
	"filterid":	"SnapshotId"
}

aws_fsx_openzfs_volume = {
	"clfn":		"fsx",
	"descfn":	"describe_volumes",
	"topkey":	"Volumes",
	"key":		"VolumeId",
	"filterid":	"VolumeId"
}

aws_fsx_windows_file_system = {
	"clfn":		"fsx",
	"descfn":	"describe_file_systems",
	"topkey":	"FileSystems",
	"key":		"FileSystemId",
	"filterid":	"FileSystemId"
}

aws_gamelift_alias = {
	"clfn":		"gamelift",
	"descfn":	"list_aliases",
	"topkey":	"Aliases",
	"key":		"AliasId",
	"filterid":	"AliasId"
}

aws_gamelift_build = {
	"clfn":		"gamelift",
	"descfn":	"list_builds",
	"topkey":	"Builds",
	"key":		"BuildId",
	"filterid":	"BuildId"
}

aws_gamelift_fleet = {
	"clfn":		"gamelift",
	"descfn":	"list_fleets",
	"topkey":	"Fleets",
	"key":		"FleetId",
	"filterid":	"FleetId"
}

aws_gamelift_game_server_group = {
	"clfn":		"gamelift",
	"descfn":	"list_game_server_groups",
	"topkey":	"GameServerGroups",
	"key":		"GameServerGroupId",
	"filterid":	"GameServerGroupId"
}

aws_gamelift_game_session_queue = {
	"clfn":		"gamelift",
	"descfn":	"list_game_session_queues",
	"topkey":	"GameSessionQueues",
	"key":		"GameSessionQueueName",
	"filterid":	"GameSessionQueueName"
}

aws_gamelift_script = {
	"clfn":		"gamelift",
	"descfn":	"list_scripts",
	"topkey":	"Scripts",
	"key":		"ScriptId",
	"filterid":	"ScriptId"
}

aws_glacier_vault = {
	"clfn":		"glacier",
	"descfn":	"list_vaults",
	"topkey":	"VaultList",
	"key":		"VaultName",
	"filterid":	"VaultName"
}

aws_glacier_vault_lock = {
	"clfn":		"glacier",
	"descfn":	"list_vault_locks",
	"topkey":	"VaultLockList",
	"key":		"VaultLockId",
	"filterid":	"VaultLockId"
}

aws_globalaccelerator_accelerator = {
	"clfn":		"globalaccelerator",
	"descfn":	"list_accelerators",
	"topkey":	"Accelerators",
	"key":		"AcceleratorArn",
	"filterid":	"AcceleratorArn"
}

aws_globalaccelerator_custom_routing_accelerator = {
	"clfn":		"globalaccelerator",
	"descfn":	"list_accelerators",
	"topkey":	"Accelerators",
	"key":		"AcceleratorArn",
	"filterid":	"AcceleratorArn"
}

aws_globalaccelerator_custom_routing_endpoint_group = {
	"clfn":		"globalaccelerator",
	"descfn":	"list_endpoint_groups",
	"topkey":	"EndpointGroups",
	"key":		"EndpointGroupArn",
	"filterid":	"EndpointGroupArn"
}

aws_globalaccelerator_custom_routing_listener = {
	"clfn":		"globalaccelerator",
	"descfn":	"list_listeners",
	"topkey":	"Listeners",
	"key":		"ListenerArn",
	"filterid":	"ListenerArn"
}

aws_globalaccelerator_endpoint_group = {
	"clfn":		"globalaccelerator",
	"descfn":	"list_endpoint_groups",
	"topkey":	"EndpointGroups",
	"key":		"EndpointGroupArn",
	"filterid":	"EndpointGroupArn"
}

aws_globalaccelerator_listener = {
	"clfn":		"globalaccelerator",
	"descfn":	"list_listeners",
	"topkey":	"Listeners",
	"key":		"ListenerArn",
	"filterid":	"ListenerArn"
}

aws_glue_catalog_table = {
	"clfn":		"glue",
	"descfn":	"list_tables",
	"topkey":	"TableList",
	"key":		"Name",
	"filterid":	"Name"
}

aws_glue_classifier = {
	"clfn":		"glue",
	"descfn":	"list_classifiers",
	"topkey":	"Classifiers",
	"key":		"Name",
	"filterid":	"Name"
}

aws_glue_connection = {
	"clfn":		"glue",
	"descfn":	"list_connections",
	"topkey":	"ConnectionList",
	"key":		"Name",
	"filterid":	"Name"
}

aws_glue_data_catalog_encryption_settings = {
	"clfn":		"glue",
	"descfn":	"get_data_catalog_encryption_settings",
	"topkey":	"DataCatalogEncryptionSettings",
	"key":		"CatalogId",
	"filterid":	"CatalogId"
}

aws_glue_data_quality_ruleset = {
	"clfn":		"glue",
	"descfn":	"list_data_quality_rulesets",
	"topkey":	"RulesetNames",
	"key":		"Name",
	"filterid":	"Name"
}

aws_glue_dev_endpoint = {
	"clfn":		"glue",
	"descfn":	"list_dev_endpoints",
	"topkey":	"DevEndpoints",
	"key":		"EndpointName",
	"filterid":	"EndpointName"
}

aws_glue_job = {
	"clfn":		"glue",
	"descfn":	"list_jobs",
	"topkey":	"JobNames",
	"key":		"Name",
	"filterid":	"Name"
}

aws_glue_ml_transform = {
	"clfn":		"glue",
	"descfn":	"list_ml_transforms",
	"topkey":	"TransformIds",
	"key":		"TransformId",
	"filterid":	"TransformId"
}

aws_glue_partition = {
	"clfn":		"glue",
	"descfn":	"list_partitions",
	"topkey":	"Partitions",
	"key":		"PartitionValues",
	"filterid":	"PartitionValues"
}

aws_glue_partition_index = {
	"clfn":		"glue",
	"descfn":	"list_partition_indexes",
	"topkey":	"PartitionIndexNames",
	"key":		"Name",
	"filterid":	"Name"
}

aws_glue_registry = {
	"clfn":		"glue",
	"descfn":	"list_registries",
	"topkey":	"Registries",
	"key":		"RegistryId",
	"filterid":	"RegistryId"
}

aws_glue_resource_policy = {
	"clfn":		"glue",
	"descfn":	"list_resource_policies",
	"topkey":	"ResourcePolicies",
	"key":		"PolicyHash",
	"filterid":	"PolicyHash"
}

aws_glue_schema = {
	"clfn":		"glue",
	"descfn":	"list_schemas",
	"topkey":	"Schemas",
	"key":		"SchemaId",
	"filterid":	"SchemaId"
}

aws_glue_security_configuration = {
	"clfn":		"glue",
	"descfn":	"list_security_configurations",
	"topkey":	"SecurityConfigurations",
	"key":		"Name",
	"filterid":	"Name"
}

aws_glue_trigger = {
	"clfn":		"glue",
	"descfn":	"list_triggers",
	"topkey":	"Triggers",
	"key":		"Name",
	"filterid":	"Name"
}

aws_glue_user_defined_function = {
	"clfn":		"glue",
	"descfn":	"list_user_defined_functions",
	"topkey":	"UserDefinedFunctionNames",
	"key":		"Name",
	"filterid":	"Name"
}

aws_glue_workflow = {
	"clfn":		"glue",
	"descfn":	"list_workflows",
	"topkey":	"Workflows",
	"key":		"Name",
	"filterid":	"Name"
}

aws_grafana_license_association = {
	"clfn":		"grafana",
	"descfn":	"list_license_associations",
	"topkey":	"LicenseAssociations",
	"key":		"LicenseAssociationArn",
	"filterid":	"LicenseAssociationArn"
}

aws_grafana_role_association = {
	"clfn":		"grafana",
	"descfn":	"list_role_associations",
	"topkey":	"RoleAssociations",
	"key":		"RoleAssociationArn",
	"filterid":	"RoleAssociationArn"
}

aws_grafana_workspace = {
	"clfn":		"grafana",
	"descfn":	"list_workspaces",
	"topkey":	"Workspaces",
	"key":		"WorkspaceId",
	"filterid":	"WorkspaceId"
}

aws_grafana_workspace_api_key = {
	"clfn":		"grafana",
	"descfn":	"list_workspace_api_keys",
	"topkey":	"ApiKeys",
	"key":		"KeyId",
	"filterid":	"KeyId"
}

aws_grafana_workspace_saml_configuration = {
	"clfn":		"grafana",
	"descfn":	"list_workspace_saml_configurations",
	"topkey":	"SamlConfigurations",
	"key":		"SamlConfigurationId",
	"filterid":	"SamlConfigurationId"
}

aws_guardduty_detector = {
	"clfn":		"guardduty",
	"descfn":	"list_detectors",
	"topkey":	"DetectorIds",
	"key":		"DetectorId",
	"filterid":	"DetectorId"
}

aws_guardduty_detector_feature = {
	"clfn":		"guardduty",
	"descfn":	"list_detector_features",
	"topkey":	"DetectorFeatures",
	"key":		"DetectorFeatureName",
	"filterid":	"DetectorFeatureName"
}

aws_guardduty_filter = {
	"clfn":		"guardduty",
	"descfn":	"list_filters",
	"topkey":	"FilterNames",
	"key":		"FilterName",
	"filterid":	"FilterName"
}

aws_guardduty_invite_accepter = {
	"clfn":		"guardduty",
	"descfn":	"list_invitation_accepters",
	"topkey":	"InvitationAccepters",
	"key":		"InvitationAccepterId",
	"filterid":	"InvitationAccepterId"
}

aws_guardduty_ipset = {
	"clfn":		"guardduty",
	"descfn":	"list_ip_sets",
	"topkey":	"IpSetIds",
	"key":		"IpSetId",
	"filterid":	"IpSetId"
}

aws_guardduty_member = {
	"clfn":		"guardduty",
	"descfn":	"list_members",
	"topkey":	"Members",
	"key":		"MemberId",
	"filterid":	"MemberId"
}

aws_guardduty_organization_admin_account = {
	"clfn":		"guardduty",
	"descfn":	"list_organization_admin_accounts",
	"topkey":	"AdminAccounts",
	"key":		"AdminAccountId",
	"filterid":	"AdminAccountId"
}

aws_guardduty_organization_configuration = {
	"clfn":		"guardduty",
	"descfn":	"list_organization_configurations",
	"topkey":	"OrganizationConfigurations",
	"key":		"OrganizationConfigurationId",
	"filterid":	"OrganizationConfigurationId"
}

aws_guardduty_organization_configuration_feature = {
	"clfn":		"guardduty",
	"descfn":	"list_organization_configuration_features",
	"topkey":	"OrganizationConfigurationFeatures",
	"key":		"OrganizationConfigurationFeature",
	"filterid":	"OrganizationConfigurationFeature"
}

aws_guardduty_publishing_destination = {
	"clfn":		"guardduty",
	"descfn":	"list_publishing_destinations",
	"topkey":	"PublishingDestinations",
	"key":		"DestinationId",
	"filterid":	"DestinationId"
}

aws_guardduty_threatintelset = {
	"clfn":		"guardduty",
	"descfn":	"list_threat_intel_sets",
	"topkey":	"ThreatIntelSetIds",
	"key":		"ThreatIntelSetId",
	"filterid":	"ThreatIntelSetId"
}

aws_iam_access_key = {
	"clfn":		"iam",
	"descfn":	"list_access_keys",
	"topkey":	"AccessKeyMetadata",
	"key":		"AccessKeyId",
	"filterid":	"AccessKeyId"
}

aws_iam_account_alias = {
	"clfn":		"iam",
	"descfn":	"list_account_aliases",
	"topkey":	"AccountAliases",
	"key":		"AccountAlias",
	"filterid":	"AccountAlias"
}

aws_iam_account_password_policy = {
	"clfn":		"iam",
	"descfn":	"get_account_password_policy",
	"topkey":	"PasswordPolicy",
	"key":		"PasswordPolicy",
	"filterid":	"PasswordPolicy"
}

aws_iam_group = {
	"clfn":		"iam",
	"descfn":	"list_groups",
	"topkey":	"Groups",
	"key":		"GroupName",
	"filterid":	"GroupName"
}

aws_iam_group_membership = {
	"clfn":		"iam",
	"descfn":	"get_group",
	"topkey":	"Group",
	"key":		"GroupName",
	"filterid":	"GroupName"
}

aws_iam_group_policy = {
	"clfn":		"iam",
	"descfn":	"list_groups_for_user",
	"topkey":	"Groups",
	"key":		"GroupName",
	"filterid":	"GroupName"
}

aws_iam_group_policy_attachment = {
	"clfn":		"iam",
	"descfn":	"get_group_policy",
	"topkey":	"GroupPolicy",
	"key":		"GroupName",
	"filterid":	"GroupName"
}

aws_iam_openid_connect_provider = {
	"clfn":		"iam",
	"descfn":	"list_open_id_connect_providers",
	"topkey":	"OpenIDConnectProviderList",
	"key":		"Arn",
	"filterid":	"Arn"
}

aws_iam_policy = {
	"clfn":		"iam",
	"descfn":	"list_policies",
	"topkey":	"Policies",
	"key":		"PolicyName",
	"filterid":	"PolicyName"
}

aws_iam_policy_attachment = {
	"clfn":		"iam",
	"descfn":	"get_policy",
	"topkey":	"Policy",
	"key":		"PolicyArn",
	"filterid":	"PolicyArn"
}

aws_iam_saml_provider = {
	"clfn":		"iam",
	"descfn":	"list_saml_providers",
	"topkey":	"SAMLProviderList",
	"key":		"Arn",
	"filterid":	"Arn"
}

aws_iam_security_token_service_preferences = {
	"clfn":		"iam",
	"descfn":	"get_account_token_version",
	"topkey":	"AccountTokenVersion",
	"key":		"AccountTokenVersion",
	"filterid":	"AccountTokenVersion"
}

aws_iam_server_certificate = {
	"clfn":		"iam",
	"descfn":	"list_server_certificates",
	"topkey":	"ServerCertificateMetadataList",
	"key":		"ServerCertificateName",
	"filterid":	"ServerCertificateName"
}

aws_iam_service_linked_role = {
	"clfn":		"iam",
	"descfn":	"list_service_linked_roles",
	"topkey":	"ServiceLinkedRoles",
	"key":		"Arn",
	"filterid":	"Arn"
}

aws_iam_service_specific_credential = {
	"clfn":		"iam",
	"descfn":	"list_service_specific_credentials",
	"topkey":	"ServiceSpecificCredentials",
	"key":		"ServiceSpecificCredentialId",
	"filterid":	"ServiceSpecificCredentialId"
}

aws_iam_signing_certificate = {
	"clfn":		"iam",
	"descfn":	"list_signing_certificates",
	"topkey":	"Certificates",
	"key":		"CertificateId",
	"filterid":	"CertificateId"
}

aws_iam_user_group_membership = {
	"clfn":		"iam",
	"descfn":	"get_user_group_membership",
	"topkey":	"Groups",
	"key":		"GroupName",
	"filterid":	"GroupName"
}

aws_iam_user_login_profile = {
	"clfn":		"iam",
	"descfn":	"get_login_profile",
	"topkey":	"LoginProfile",
	"key":		"UserName",
	"filterid":	"UserName"
}

aws_iam_user_policy = {
	"clfn":		"iam",
	"descfn":	"list_user_policies",
	"topkey":	"PolicyNames",
	"key":		"PolicyName",
	"filterid":	"PolicyName"
}

aws_iam_user_policy_attachment = {
	"clfn":		"iam",
	"descfn":	"get_user_policy",
	"topkey":	"Policy",
	"key":		"UserName",
	"filterid":	"UserName"
}

aws_iam_user_ssh_key = {
	"clfn":		"iam",
	"descfn":	"list_ssh_public_keys",
	"topkey":	"SSHPublicKeys",
	"key":		"SSHPublicKeyId",
	"filterid":	"SSHPublicKeyId"
}

aws_iam_virtual_mfa_device = {
	"clfn":		"iam",
	"descfn":	"list_virtual_mfa_devices",
	"topkey":	"VirtualMFADevices",
	"key":		"SerialNumber",
	"filterid":	"SerialNumber"
}

aws_identitystore_group = {
	"clfn":		"identitystore",
	"descfn":	"list_groups",
	"topkey":	"Groups",
	"key":		"GroupId",
	"filterid":	"GroupId"
}

aws_identitystore_group_membership = {
	"clfn":		"identitystore",
	"descfn":	"list_group_memberships",
	"topkey":	"GroupMemberships",
	"key":		"GroupId",
	"filterid":	"GroupId"
}

aws_identitystore_user = {
	"clfn":		"identitystore",
	"descfn":	"list_users",
	"topkey":	"Users",
	"key":		"UserId",
	"filterid":	"UserId"
}

aws_imagebuilder_component = {
	"clfn":		"imagebuilder",
	"descfn":	"list_components",
	"topkey":	"Components",
	"key":		"ComponentArn",
	"filterid":	"ComponentArn"
}


aws_imagebuilder_container_recipe = {
	"clfn":		"imagebuilder",
	"descfn":	"list_container_recipes",
	"topkey":	"ContainerRecipes",
	"key":		"ContainerRecipeArn",
	"filterid":	"ContainerRecipeArn"
}


aws_imagebuilder_distribution_configuration = {
	"clfn":		"imagebuilder",
	"descfn":	"list_distribution_configurations",
	"topkey":	"DistributionConfigurations",
	"key":		"DistributionConfigurationArn",
	"filterid":	"DistributionConfigurationArn"
}


aws_imagebuilder_image = {
	"clfn":		"imagebuilder",
	"descfn":	"list_images",
	"topkey":	"Images",
	"key":		"ImageArn",
	"filterid":	"ImageArn"
}

aws_imagebuilder_image_pipeline = {
	"clfn":		"imagebuilder",
	"descfn":	"list_image_pipelines",
	"topkey":	"ImagePipelines",
	"key":		"ImagePipelineArn",
	"filterid":	"ImagePipelineArn"
}


aws_imagebuilder_image_recipe = {
	"clfn":		"imagebuilder",
	"descfn":	"list_image_recipes",
	"topkey":	"ImageRecipes",
	"key":		"ImageRecipeArn",
	"filterid":	"ImageRecipeArn"
}

aws_imagebuilder_infrastructure_configuration = {
	"clfn":		"imagebuilder",
	"descfn":	"list_infrastructure_configurations",
	"topkey":	"InfrastructureConfigurations",
	"key":		"InfrastructureConfigurationArn",
	"filterid":	"InfrastructureConfigurationArn"
}

aws_inspector2_delegated_admin_account = {
	"clfn":		"inspector2",
	"descfn":	"list_delegated_admin_accounts",
	"topkey":	"DelegatedAdminAccounts",
	"key":		"AccountId",
	"filterid":	"AccountId"
}

aws_inspector2_enabler = {
	"clfn":		"inspector2",
	"descfn":	"list_enablers",
	"topkey":	"Enablers",
	"key":		"Name",
	"filterid":	"Name"
}

aws_inspector2_member_association = {
	"clfn":		"inspector2",
	"descfn":	"list_member_associations",
	"topkey":	"MemberAssociations",
	"key":		"AccountId",
	"filterid":	"AccountId"
}

aws_inspector2_organization_configuration = {
	"clfn":		"inspector2",
	"descfn":	"list_organization_configurations",
	"topkey":	"OrganizationConfigurations",
	"key":		"OrganizationConfigurationArn",
	"filterid":	"OrganizationConfigurationArn"
}

aws_inspector_assessment_target = {
	"clfn":		"inspector",
	"descfn":	"list_assessment_targets",
	"topkey":	"AssessmentTargets",
	"key":		"Name",
	"filterid":	"Name"
}

aws_inspector_assessment_template = {
	"clfn":		"inspector",
	"descfn":	"list_assessment_templates",
	"topkey":	"AssessmentTemplates",
	"key":		"Name",
	"filterid":	"Name"
}

aws_inspector_resource_group = {
	"clfn":		"inspector",
	"descfn":	"list_resource_groups",
	"topkey":	"ResourceGroups",
	"key":		"Name",
	"filterid":	"Name"
}

aws_internet_gateway_attachment = {
	"clfn":		"ec2",
	"descfn":	"describe_internet_gateway_attachments",
	"topkey":	"InternetGatewayAttachments",
	"key":		"InternetGatewayId",
	"filterid":	"InternetGatewayId"
}

aws_internetmonitor_monitor = {
	"clfn":		"internetmonitor",
	"descfn":	"list_monitors",
	"topkey":	"Monitors",
	"key":		"MonitorId",
	"filterid":	"MonitorId"
}

aws_iot_authorizer = {
	"clfn":		"iot",
	"descfn":	"list_authorizers",
	"topkey":	"Authorizers",
	"key":		"AuthorizerName",
	"filterid":	"AuthorizerName"
}

aws_iot_billing_group = {
	"clfn":		"iot",
	"descfn":	"list_billing_groups",
	"topkey":	"BillingGroups",
	"key":		"BillingGroupName",
	"filterid":	"BillingGroupName"
}

aws_iot_ca_certificate = {
	"clfn":		"iot",
	"descfn":	"list_ca_certificates",
	"topkey":	"CACertificates",
	"key":		"Id",
	"filterid":	"Id"
}

aws_iot_certificate = {
	"clfn":		"iot",
	"descfn":	"list_certificates",
	"topkey":	"Certificates",
	"key":		"CertificateId",
	"filterid":	"CertificateId"
}

aws_iot_domain_configuration = {
	"clfn":		"iot",
	"descfn":	"list_domain_configurations",
	"topkey":	"DomainConfigurations",
	"key":		"DomainConfigurationName",
	"filterid":	"DomainConfigurationName"
}


aws_iot_event_configurations = {
	"clfn":		"iot",
	"descfn":	"list_event_configurations",
	"topkey":	"EventConfigurations",
	"key":		"EventConfigurationName",
	"filterid":	"EventConfigurationName"
}

aws_iot_indexing_configuration = {
	"clfn":		"iot",
	"descfn":	"list_indexing_configurations",
	"topkey":	"IndexingConfigurations",
	"key":		"IndexingConfigurationName",
	"filterid":	"IndexingConfigurationName"
}

aws_iot_logging_options = {
	"clfn":		"iot",
	"descfn":	"describe_logging_options",
	"topkey":	"LoggingOptions",
	"key":		"roleArn",
	"filterid":	"roleArn"
}

aws_iot_policy = {
	"clfn":		"iot",
	"descfn":	"list_policies",
	"topkey":	"policies",
	"key":		"policyName",
	"filterid":	"policyName"
}

aws_iot_policy_attachment = {
	"clfn":		"iot",
	"descfn":	"list_policies",
	"topkey":	"Policies",
	"key":		"PolicyName",
	"filterid":	"PolicyName"
}

aws_iot_provisioning_template = {
	"clfn":		"iot",
	"descfn":	"list_provisioning_templates",
	"topkey":	"ProvisioningTemplates",
	"key":		"TemplateName",
	"filterid":	"TemplateName"
}


aws_iot_role_alias = {
	"clfn":		"iot",
	"descfn":	"list_role_aliases",
	"topkey":	"RoleAliases",
	"key":		"RoleAliasName",
	"filterid":	"RoleAliasName"
}

aws_iot_thing = {
	"clfn":		"iot",
	"descfn":	"list_things",
	"topkey":	"things",
	"key":		"thingName",
	"filterid":	"thingName"
}

aws_iot_thing_group = {
	"clfn":		"iot",
	"descfn":	"list_thing_groups",
	"topkey":	"ThingGroups",
	"key":		"ThingGroupName",
	"filterid":	"ThingGroupName"
}

aws_iot_thing_group_membership = {
	"clfn":		"iot",
	"descfn":	"list_thing_group_memberships",
	"topkey":	"ThingGroupMemberships",
	"key":		"ThingGroupName",
	"filterid":	"ThingGroupName"
}

aws_iot_thing_principal_attachment = {
	"clfn":		"iot",
	"descfn":	"list_thing_principal_attachments",
	"topkey":	"ThingPrincipalAttachments",
	"key":		"ThingName",
	"filterid":	"ThingName"
}

aws_iot_thing_type = {
	"clfn":		"iot",
	"descfn":	"list_thing_types",
	"topkey":	"ThingTypes",
	"key":		"ThingTypeName",
	"filterid":	"ThingTypeName"
}

aws_iot_topic_rule = {
	"clfn":		"iot",
	"descfn":	"list_topic_rules",
	"topkey":	"rules",
	"key":		"ruleName",
	"filterid":	"ruleName"
}

aws_iot_topic_rule_destination = {
	"clfn":		"iot",
	"descfn":	"list_topic_rule_destinations",
	"topkey":	"destinations",
	"key":		"destinationName",
	"filterid":	"destinationName"
}

aws_ivs_channel = {
	"clfn":		"ivs",
	"descfn":	"list_channels",
	"topkey":	"Channels",
	"key":		"arn",
	"filterid":	"arn"
}

aws_ivs_playback_key_pair = {
	"clfn":		"ivs",
	"descfn":	"list_playback_key_pairs",
	"topkey":	"PlaybackKeyPairs",
	"key":		"arn",
	"filterid":	"arn"
}

aws_ivs_recording_configuration = {
	"clfn":		"ivs",
	"descfn":	"list_recording_configurations",
	"topkey":	"RecordingConfigurations",
	"key":		"arn",
	"filterid":	"arn"
}

aws_ivschat_logging_configuration = {
	"clfn":		"ivschat",
	"descfn":	"list_logging_configurations",
	"topkey":	"LoggingConfigurations",
	"key":		"arn",
	"filterid":	"arn"
}

aws_ivschat_room = {
	"clfn":		"ivschat",
	"descfn":	"list_rooms",
	"topkey":	"Rooms",
	"key":		"arn",
	"filterid":	"arn"
}

aws_kendra_data_source = {
	"clfn":		"kendra",
	"descfn":	"list_data_sources",
	"topkey":	"DataSources",
	"key":		"Id",
	"filterid":	"Id"
}

aws_kendra_experience = {
	"clfn":		"kendra",
	"descfn":	"list_experiences",
	"topkey":	"Experiences",
	"key":		"Id",
	"filterid":	"Id"
}

aws_kendra_faq = {
	"clfn":		"kendra",
	"descfn":	"list_faqs",
	"topkey":	"Faqs",
	"key":		"Id",
	"filterid":	"Id"
}

aws_kendra_index = {
	"clfn":		"kendra",
	"descfn":	"list_indices",
	"topkey":	"Indices",
	"key":		"Id",
	"filterid":	"Id"
}

aws_kendra_query_suggestions_block_list = {
	"clfn":		"kendra",
	"descfn":	"list_query_suggestions_block_lists",
	"topkey":	"QuerySuggestionsBlockLists",
	"key":		"Id",
	"filterid":	"Id"
}

aws_kendra_thesaurus = {
	"clfn":		"kendra",
	"descfn":	"list_thesauri",
	"topkey":	"Thesauri",
	"key":		"Id",
	"filterid":	"Id"
}

aws_keyspaces_keyspace = {
	"clfn":		"keyspaces",
	"descfn":	"list_keyspaces",
	"topkey":	"Keyspaces",
	"key":		"Name",
	"filterid":	"Name"
}

aws_keyspaces_table = {
	"clfn":		"keyspaces",
	"descfn":	"list_tables",
	"topkey":	"Tables",
	"key":		"Name",
	"filterid":	"Name"
}

aws_kinesis_analytics_application = {
	"clfn":		"kinesisanalytics",
	"descfn":	"list_applications",
	"topkey":	"ApplicationSummaries",
	"key":		"ApplicationName",
	"filterid":	"ApplicationName"
}

aws_kinesis_firehose_delivery_stream = {
	"clfn":		"firehose",
	"descfn":	"list_delivery_streams",
	"topkey":	"DeliveryStreamNames",
	"key":		"DeliveryStreamName",
	"filterid":	"DeliveryStreamName"
}

aws_kinesis_stream_consumer = {
	"clfn":		"kinesis",
	"descfn":	"list_stream_consumers",
	"topkey":	"Consumers",
	"key":		"ConsumerName",
	"filterid":	"ConsumerName"
}

aws_kinesis_video_stream = {
	"clfn":		"kinesisvideo",
	"descfn":	"list_streams",
	"topkey":	"StreamNames",
	"key":		"StreamName",
	"filterid":	"StreamName"
}

aws_kinesisanalyticsv2_application = {
	"clfn":		"kinesisanalyticsv2",
	"descfn":	"list_applications",
	"topkey":	"ApplicationSummaries",
	"key":		"ApplicationName",
	"filterid":	"ApplicationName"
}

aws_kinesisanalyticsv2_application_snapshot = {
	"clfn":		"kinesisanalyticsv2",
	"descfn":	"list_application_snapshots",
	"topkey":	"ApplicationSnapshots",
	"key":		"SnapshotName",
	"filterid":	"SnapshotName"
}

aws_kms_ciphertext = {
	"clfn":		"kms",
	"descfn":	"list_grants",
	"topkey":	"Grants",
	"key":		"GrantId",
	"filterid":	"GrantId"
}

aws_kms_custom_key_store = {
	"clfn":		"kms",
	"descfn":	"list_custom_key_stores",
	"topkey":	"CustomKeyStores",
	"key":		"CustomKeyStoreId",
	"filterid":	"CustomKeyStoreId"
}

aws_kms_external_key = {
	"clfn":		"kms",
	"descfn":	"list_external_keys",
	"topkey":	"ExternalKeys",
	"key":		"KeyId",
	"filterid":	"KeyId"
}

aws_kms_grant = {
	"clfn":		"kms",
	"descfn":	"list_grants",
	"topkey":	"Grants",
	"key":		"GrantId",
	"filterid":	"GrantId"
}

aws_kms_key_policy = {
	"clfn":		"kms",
	"descfn":	"list_key_policies",
	"topkey":	"PolicyNames",
	"key":		"PolicyName",
	"filterid":	"PolicyName"
}


aws_kms_replica_external_key = {
	"clfn":		"kms",
	"descfn":	"list_replica_keys",
	"topkey":	"ReplicaKeys",
	"key":		"KeyId",
	"filterid":	"KeyId"
}

aws_kms_replica_key = {
	"clfn":		"kms",
	"descfn":	"list_replica_keys",
	"topkey":	"ReplicaKeys",
	"key":		"KeyId",
	"filterid":	"KeyId"
}


aws_lakeformation_data_lake_settings = {
	"clfn":		"lakeformation",
	"descfn":	"list_data_lake_settings",
	"topkey":	"DataLakeSettings",
	"key":		"DataLakeSettingsId",
	"filterid":	"DataLakeSettingsId"
}

aws_lakeformation_lf_tag = {
	"clfn":		"lakeformation",
	"descfn":	"list_lf_tags",
	"topkey":	"LFTags",
	"key":		"LFTagKey",
	"filterid":	"LFTagKey"
}

aws_lakeformation_permissions = {
	"clfn":		"lakeformation",
	"descfn":	"list_permissions",
	"topkey":	"Permissions",
	"key":		"Principal",
	"filterid":	"Principal"
}

aws_lakeformation_resource = {
	"clfn":		"lakeformation",
	"descfn":	"list_resources",
	"topkey":	"ResourceInfoList",
	"key":		"ResourceArn",
	"filterid":	"ResourceArn"
}

aws_lakeformation_resource_lf_tags = {
	"clfn":		"lakeformation",
	"descfn":	"list_resource_lf_tags",
	"topkey":	"LFTags",
	"key":		"LFTagKey",
	"filterid":	"LFTagKey"
}

aws_lambda_code_signing_config = {
	"clfn":		"lambda",
	"descfn":	"list_code_signing_configs",
	"topkey":	"CodeSigningConfigs",
	"key":		"CodeSigningConfigArn",
	"filterid":	"CodeSigningConfigArn"
}

aws_lambda_function_url = {
	"clfn":		"lambda",
	"descfn":	"list_function_url_configs",
	"topkey":	"FunctionUrlConfigs",
	"key":		"FunctionName",
	"filterid":	"FunctionName"
}


aws_lambda_invocation = {
	"clfn":		"lambda",
	"descfn":	"list_functions",
	"topkey":	"Functions",
	"key":		"FunctionName",
	"filterid":	"FunctionName"
}

aws_lambda_layer_version_permission = {
	"clfn":		"lambda",
	"descfn":	"list_layer_version_permissions",
	"topkey":	"LayerVersionPermissions",
	"key":		"LayerName",
	"filterid":	"LayerName"
}

aws_lambda_provisioned_concurrency_config = {
	"clfn":		"lambda",
	"descfn":	"list_provisioned_concurrency_configs",
	"topkey":	"ProvisionedConcurrencyConfigs",
	"key":		"FunctionName",
	"filterid":	"FunctionName"
}

aws_lb_cookie_stickiness_policy = {
	"clfn":		"elbv2",
	"descfn":	"describe_load_balancer_policies",
	"topkey":	"PolicyDescriptions",
	"key":		"PolicyName",
	"filterid":	"PolicyName"
}

aws_lb_listener = {
	"clfn":		"elbv2",
	"descfn":	"describe_listeners",
	"topkey":	"Listeners",
	"key":		"ListenerArn",
	"filterid":	"ListenerArn"
}

aws_lb_listener_certificate = {
	"clfn":		"elbv2",
	"descfn":	"describe_listener_certificates",
	"topkey":	"Certificates",
	"key":		"CertificateArn",
	"filterid":	"CertificateArn"
}

aws_lb_listener_rule = {
	"clfn":		"elbv2",
	"descfn":	"describe_rules",
	"topkey":	"Rules",
	"key":		"RuleArn",
	"filterid":	"RuleArn"
}

aws_lb_ssl_negotiation_policy = {
	"clfn":		"elbv2",
	"descfn":	"describe_ssl_policies",
	"topkey":	"SslPolicies",
	"key":		"SslPolicyName",
	"filterid":	"SslPolicyName"
}

aws_lb_target_group = {
	"clfn":		"elbv2",
	"descfn":	"describe_target_groups",
	"topkey":	"TargetGroups",
	"key":		"TargetGroupArn",
	"filterid":	"TargetGroupArn"
}

aws_lb_target_group_attachment = {
	"clfn":		"elbv2",
	"descfn":	"describe_target_group_attributes",
	"topkey":	"Attributes",
	"key":		"Key",
	"filterid":	"Key"
}

aws_lb_trust_store = {
	"clfn":		"elbv2",
	"descfn":	"describe_load_balancer_attributes",
	"topkey":	"Attributes",
	"key":		"Key",
	"filterid":	"Key"
}

aws_lb_trust_store_revocation = {
	"clfn":		"elbv2",
	"descfn":	"describe_load_balancer_attributes",
	"topkey":	"Attributes",
	"key":		"Key",
	"filterid":	"Key"
}

aws_lex_bot = {
	"clfn":		"lex-models",
	"descfn":	"get_bots",
	"topkey":	"bots",
	"key":		"name",
	"filterid":	"name"
}

aws_lex_bot_alias = {
	"clfn":		"lex-models",
	"descfn":	"get_bot_aliases",
	"topkey":	"aliases",
	"key":		"name",
	"filterid":	"name"
}

aws_lex_intent = {
	"clfn":		"lex-models",
	"descfn":	"get_intents",
	"topkey":	"intents",
	"key":		"name",
	"filterid":	"name"
}

aws_lex_slot_type = {
	"clfn":		"lex-models",
	"descfn":	"get_slot_types",
	"topkey":	"slotTypes",
	"key":		"name",
	"filterid":	"name"
}

aws_lexv2models_bot = {
	"clfn":		"lexv2-models",
	"descfn":	"list_bots",
	"topkey":	"bots",
	"key":		"name",
	"filterid":	"name"
}

aws_lexv2models_bot_locale = {
	"clfn":		"lexv2-models",
	"descfn":	"list_bot_locales",
	"topkey":	"botLocales",
	"key":		"name",
	"filterid":	"name"
}

aws_lexv2models_bot_version = {
	"clfn":		"lexv2-models",
	"descfn":	"list_bot_versions",
	"topkey":	"botVersions",
	"key":		"name",
	"filterid":	"name"
}

aws_licensemanager_association = {
	"clfn":		"license-manager",
	"descfn":	"list_associations",
	"topkey":	"Associations",
	"key":		"LicenseConfigurationArn",
	"filterid":	"LicenseConfigurationArn"
}

aws_licensemanager_grant = {
	"clfn":		"license-manager",
	"descfn":	"list_grants",
	"topkey":	"Grants",
	"key":		"GrantArn",
	"filterid":	"GrantArn"
}

aws_licensemanager_grant_accepter = {
	"clfn":		"license-manager",
	"descfn":	"list_grant_accepters",
	"topkey":	"GrantAccepters",
	"key":		"GrantId",
	"filterid":	"GrantId"
}

aws_licensemanager_license_configuration = {
	"clfn":		"license-manager",
	"descfn":	"list_license_configurations",
	"topkey":	"LicenseConfigurations",
	"key":		"LicenseConfigurationArn",
	"filterid":	"LicenseConfigurationArn"
}

aws_lightsail_bucket = {
	"clfn":		"lightsail",
	"descfn":	"get_buckets",
	"topkey":	"Buckets",
	"key":		"name",
	"filterid":	"name"
}

aws_lightsail_bucket_access_key = {
	"clfn":		"lightsail",
	"descfn":	"get_bucket_access_keys",
	"topkey":	"AccessKeys",
	"key":		"name",
	"filterid":	"name"
}

aws_lightsail_bucket_resource_access = {
	"clfn":		"lightsail",
	"descfn":	"get_bucket_resources",
	"topkey":	"Buckets",
	"key":		"name",
	"filterid":	"name"
}

aws_lightsail_certificate = {
	"clfn":		"lightsail",
	"descfn":	"get_certificates",
	"topkey":	"Certificates",
	"key":		"name",
	"filterid":	"name"
}

aws_lightsail_container_service = {
	"clfn":		"lightsail",
	"descfn":	"get_container_services",
	"topkey":	"ContainerServices",
	"key":		"name",
	"filterid":	"name"
}

aws_lightsail_container_service_deployment_version = {
	"clfn":		"lightsail",
	"descfn":	"get_container_service_deployments",
	"topkey":	"Deployments",
	"key":		"name",
	"filterid":	"name"
}

aws_lightsail_database = {
	"clfn":		"lightsail",
	"descfn":	"get_databases",
	"topkey":	"Databases",
	"key":		"name",
	"filterid":	"name"
}

aws_lightsail_disk = {
	"clfn":		"lightsail",
	"descfn":	"get_disks",
	"topkey":	"Disks",
	"key":		"name",
	"filterid":	"name"
}

aws_lightsail_disk_attachment = {
	"clfn":		"lightsail",
	"descfn":	"get_disk_attachments",
	"topkey":	"DiskAttachments",
	"key":		"name",
	"filterid":	"name"
}

aws_lightsail_distribution = {
	"clfn":		"lightsail",
	"descfn":	"get_distributions",
	"topkey":	"Distributions",
	"key":		"name",
	"filterid":	"name"
}

aws_lightsail_domain = {
	"clfn":		"lightsail",
	"descfn":	"get_domains",
	"topkey":	"Domains",
	"key":		"name",
	"filterid":	"name"
}

aws_lightsail_domain_entry = {
	"clfn":		"lightsail",
	"descfn":	"get_domain_entries",
	"topkey":	"DomainEntries",
	"key":		"name",
	"filterid":	"name"
}

aws_lightsail_instance = {
	"clfn":		"lightsail",
	"descfn":	"get_instances",
	"topkey":	"Instances",
	"key":		"name",
	"filterid":	"name"
}

aws_lightsail_instance_public_ports = {
	"clfn":		"lightsail",
	"descfn":	"get_instance_public_ports",
	"topkey":	"PublicPorts",
	"key":		"name",
	"filterid":	"name"
}

aws_lightsail_key_pair = {
	"clfn":		"lightsail",
	"descfn":	"get_instance_public_ports",
	"topkey":	"PortInfo",
	"key":		"name",
	"filterid":	"name"
}

aws_lightsail_lb = {
	"clfn":		"lightsail",
	"descfn":	"get_key_pairs",
	"topkey":	"KeyPairs",
	"key":		"name",
	"filterid":	"name"
}

aws_lightsail_lb_attachment = {
	"clfn":		"lightsail",
	"descfn":	"get_load_balancers",
	"topkey":	"LoadBalancers",
	"key":		"name",
	"filterid":	"name"
}

aws_lightsail_lb_certificate = {
	"clfn":		"lightsail",
	"descfn":	"get_key_pairs",
	"topkey":	"KeyPairs",
	"key":		"name",
	"filterid":	"name"
}

aws_lightsail_lb_certificate_attachment = {
	"clfn":		"lightsail",
	"descfn":	"get_load_balancer_certificates",
	"topkey":	"Certificates",
	"key":		"name",
	"filterid":	"name"
}

aws_lightsail_lb_https_redirection_policy = {
	"clfn":		"lightsail",
	"descfn":	"get_key_pairs",
	"topkey":	"KeyPairs",
	"key":		"name",
	"filterid":	"name"
}

aws_lightsail_lb_stickiness_policy = {
	"clfn":		"lightsail",
	"descfn":	"get_load_balancer_https_redirection_policies",
	"topkey":	"HttpsRedirectPolicies",
	"key":		"name",
	"filterid":	"name"
}

aws_lightsail_static_ip = {
	"clfn":		"lightsail",
	"descfn":	"get_key_pairs",
	"topkey":	"KeyPairs",
	"key":		"name",
	"filterid":	"name"
}

aws_lightsail_static_ip_attachment = {
	"clfn":		"lightsail",
	"descfn":	"get_static_ips",
	"topkey":	"StaticIps",
	"key":		"name",
	"filterid":	"name"
}

aws_load_balancer_backend_server_policy = {
	"clfn":		"elbv2",
	"descfn":	"describe_backend_server_policies",
	"topkey":	"BackendServerDescriptions",
	"key":		"PolicyName",
	"filterid":	"PolicyName"
}

aws_load_balancer_listener_policy = {
	"clfn":		"elbv2",
	"descfn":	"describe_listeners",
	"topkey":	"Listeners",
	"key":		"PolicyNames",
	"filterid":	"PolicyNames"
}

aws_load_balancer_policy = {
	"clfn":		"elbv2",
	"descfn":	"describe_load_balancer_policies",
	"topkey":	"Policies",
	"key":		"PolicyName",
	"filterid":	"PolicyName"
}

aws_location_geofence_collection = {
	"clfn":		"location",
	"descfn":	"list_geofence_collections",
	"topkey":	"GeofenceCollections",
	"key":		"CollectionName",
	"filterid":	"CollectionName"
}

aws_location_map = {
	"clfn":		"location",
	"descfn":	"list_maps",
	"topkey":	"Maps",
	"key":		"MapName",
	"filterid":	"MapName"
}

aws_location_place_index = {
	"clfn":		"location",
	"descfn":	"list_place_indexes",
	"topkey":	"PlaceIndexes",
	"key":		"IndexName",
	"filterid":	"IndexName"
}

aws_location_route_calculator = {
	"clfn":		"location",
	"descfn":	"list_route_calculators",
	"topkey":	"RouteCalculators",
	"key":		"CalculatorName",
	"filterid":	"CalculatorName"
}

aws_location_tracker = {
	"clfn":		"location",
	"descfn":	"list_trackers",
	"topkey":	"Trackers",
	"key":		"TrackerName",
	"filterid":	"TrackerName"
}

aws_location_tracker_association = {
	"clfn":		"location",
	"descfn":	"list_tracker_associations",
	"topkey":	"TrackerAssociations",
	"key":		"TrackerName",
	"filterid":	"TrackerName"
}

aws_macie2_account = {
	"clfn":		"macie2",
	"descfn":	"list_account_settings",
	"topkey":	"AccountSettings",
	"key":		"Name",
	"filterid":	"Name"
}

aws_macie2_classification_export_configuration = {
	"clfn":		"macie2",
	"descfn":	"list_classification_export_configurations",
	"topkey":	"ClassificationExportConfigurations",
	"key":		"Id",
	"filterid":	"Id"
}

aws_macie2_classification_job = {
	"clfn":		"macie2",
	"descfn":	"list_classification_jobs",
	"topkey":	"ClassificationJobs",
	"key":		"Id",
	"filterid":	"Id"
}

aws_macie2_custom_data_identifier = {
	"clfn":		"macie2",
	"descfn":	"list_custom_data_identifiers",
	"topkey":	"CustomDataIdentifiers",
	"key":		"Id",
	"filterid":	"Id"
}

aws_macie2_findings_filter = {
	"clfn":		"macie2",
	"descfn":	"list_findings_filters",
	"topkey":	"FindingsFilters",
	"key":		"Name",
	"filterid":	"Name"
}

aws_macie2_invitation_accepter = {
	"clfn":		"macie2",
	"descfn":	"list_invitations",
	"topkey":	"Invitations",
	"key":		"AccountId",
	"filterid":	"AccountId"
}

aws_macie2_member = {
	"clfn":		"macie2",
	"descfn":	"list_invitation_accepters",
	"topkey":	"InvitationAccepters",
	"key":		"AccountId",
	"filterid":	"AccountId"
}

aws_macie2_organization_admin_account = {
	"clfn":		"macie2",
	"descfn":	"list_members",
	"topkey":	"Members",
	"key":		"AccountId",
	"filterid":	"AccountId"
}

aws_main_route_table_association = {
	"clfn":		"ec2",
	"descfn":	"describe_route_tables",
	"topkey":	"RouteTables",
	"key":		"Associations[].Main",
	"filterid":	"Associations[].Main"
}

aws_media_convert_queue = {
	"clfn":		"mediaconvert",
	"descfn":	"list_queues",
	"topkey":	"Queues",
	"key":		"Name",
	"filterid":	"Name"
}

aws_media_package_channel = {
	"clfn":		"mediapackage",
	"descfn":	"list_channels",
	"topkey":	"Channels",
	"key":		"Id",
	"filterid":	"Id"
}

aws_media_store_container = {
	"clfn":		"mediastore",
	"descfn":	"list_containers",
	"topkey":	"Containers",
	"key":		"Name",
	"filterid":	"Name"
}

aws_media_store_container_policy = {
	"clfn":		"mediastore",
	"descfn":	"list_container_policies",
	"topkey":	"ContainerPolicies",
	"key":		"Policy",
	"filterid":	"Policy"
}

aws_medialive_channel = {
	"clfn":		"medialive",
	"descfn":	"list_channels",
	"topkey":	"Channels",
	"key":		"Id",
	"filterid":	"Id"
}

aws_medialive_input = {
	"clfn":		"medialive",
	"descfn":	"list_inputs",
	"topkey":	"Inputs",
	"key":		"Id",
	"filterid":	"Id"
}

aws_medialive_input_security_group = {
	"clfn":		"medialive",
	"descfn":	"list_input_security_groups",
	"topkey":	"InputSecurityGroups",
	"key":		"Id",
	"filterid":	"Id"
}

aws_medialive_multiplex = {
	"clfn":		"medialive",
	"descfn":	"list_multiplexes",
	"topkey":	"Multiplexes",
	"key":		"Id",
	"filterid":	"Id"
}

aws_medialive_multiplex_program = {
	"clfn":		"medialive",
	"descfn":	"list_multiplex_programs",
	"topkey":	"MultiplexPrograms",
	"key":		"Id",
	"filterid":	"Id"
}

aws_memorydb_acl = {
	"clfn":		"memorydb",
	"descfn":	"list_acls",
	"topkey":	"ACLs",
	"key":		"Name",
	"filterid":	"Name"
}

aws_memorydb_cluster = {
	"clfn":		"memorydb",
	"descfn":	"list_clusters",
	"topkey":	"Clusters",
	"key":		"Name",
	"filterid":	"Name"
}

aws_memorydb_parameter_group = {
	"clfn":		"memorydb",
	"descfn":	"list_parameter_groups",
	"topkey":	"ParameterGroups",
	"key":		"Name",
	"filterid":	"Name"
}

aws_memorydb_snapshot = {
	"clfn":		"memorydb",
	"descfn":	"list_snapshots",
	"topkey":	"Snapshots",
	"key":		"Name",
	"filterid":	"Name"
}

aws_memorydb_subnet_group = {
	"clfn":		"memorydb",
	"descfn":	"list_subnet_groups",
	"topkey":	"SubnetGroups",
	"key":		"Name",
	"filterid":	"Name"
}

aws_memorydb_user = {
	"clfn":		"memorydb",
	"descfn":	"list_users",
	"topkey":	"Users",
	"key":		"Name",
	"filterid":	"Name"
}

aws_mq_broker = {
	"clfn":		"mq",
	"descfn":	"list_brokers",
	"topkey":	"BrokerSummaries",
	"key":		"BrokerName",
	"filterid":	"BrokerName"
}

aws_mq_configuration = {
	"clfn":		"mq",
	"descfn":	"list_configurations",
	"topkey":	"Configurations",
	"key":		"Name",
	"filterid":	"Name"
}

aws_msk_cluster = {
	"clfn":		"kafka",
	"descfn":	"list_clusters",
	"topkey":	"Clusters",
	"key":		"ClusterName",
	"filterid":	"ClusterName"
}

aws_msk_cluster_policy = {
	"clfn":		"kafka",
	"descfn":	"list_cluster_policies",
	"topkey":	"ClusterPolicies",
	"key":		"PolicyName",
	"filterid":	"PolicyName"
}

aws_msk_configuration = {
	"clfn":		"kafka",
	"descfn":	"list_configurations",
	"topkey":	"Configurations",
	"key":		"Arn",
	"filterid":	"Arn"
}

aws_msk_replicator = {
	"clfn":		"kafka",
	"descfn":	"list_replicators",
	"topkey":	"Replicators",
	"key":		"ReplicatorName",
	"filterid":	"ReplicatorName"
}

aws_msk_scram_secret_association = {
	"clfn":		"kafka",
	"descfn":	"list_scram_secrets",
	"topkey":	"ScramSecrets",
	"key":		"ClusterArn",
	"filterid":	"ClusterArn"
}

aws_msk_serverless_cluster = {
	"clfn":		"kafka",
	"descfn":	"list_serverless_clusters",
	"topkey":	"ServerlessClusters",
	"key":		"ClusterName",
	"filterid":	"ClusterName"
}

aws_msk_vpc_connection = {
	"clfn":		"kafka",
	"descfn":	"list_vpc_connections",
	"topkey":	"VpcConnections",
	"key":		"VpcConnectionName",
	"filterid":	"VpcConnectionName"
}

aws_mskconnect_connector = {
	"clfn":		"kafkaconnect",
	"descfn":	"list_connectors",
	"topkey":	"Connectors",
	"key":		"Name",
	"filterid":	"Name"
}

aws_mskconnect_custom_plugin = {
	"clfn":		"kafkaconnect",
	"descfn":	"list_custom_plugins",
	"topkey":	"CustomPlugins",
	"key":		"Name",
	"filterid":	"Name"
}

aws_mskconnect_worker_configuration = {
	"clfn":		"kafkaconnect",
	"descfn":	"list_worker_configurations",
	"topkey":	"WorkerConfigurations",
	"key":		"Name",
	"filterid":	"Name"
}

aws_mwaa_environment = {
	"clfn":		"mwaa",
	"descfn":	"list_environments",
	"topkey":	"Environments",
	"key":		"Name",
	"filterid":	"Name"
}

aws_neptune_cluster = {
	"clfn":		"neptune",
	"descfn":	"describe_db_clusters",
	"topkey":	"DBClusters",
	"key":		"DBClusterIdentifier",
	"filterid":	"DBClusterIdentifier"
}

aws_neptune_cluster_endpoint = {
	"clfn":		"neptune",
	"descfn":	"describe_db_cluster_endpoints",
	"topkey":	"DBClusterEndpoints",
	"key":		"Endpoint",
	"filterid":	"Endpoint"
}

aws_neptune_cluster_instance = {
	"clfn":		"neptune",
	"descfn":	"describe_db_cluster_instances",
	"topkey":	"DBClusterInstances",
	"key":		"DBInstanceIdentifier",
	"filterid":	"DBInstanceIdentifier"
}

aws_neptune_cluster_parameter_group = {
	"clfn":		"neptune",
	"descfn":	"describe_db_cluster_parameter_groups",
	"topkey":	"DBClusterParameterGroups",
	"key":		"DBClusterParameterGroupName",
	"filterid":	"DBClusterParameterGroupName"
}

aws_neptune_cluster_snapshot = {
	"clfn":		"neptune",
	"descfn":	"describe_db_cluster_snapshots",
	"topkey":	"DBClusterSnapshots",
	"key":		"DBClusterSnapshotIdentifier",
	"filterid":	"DBClusterSnapshotIdentifier"
}


aws_neptune_event_subscription = {
	"clfn":		"neptune",
	"descfn":	"describe_event_subscriptions",
	"topkey":	"EventSubscriptions",
	"key":		"SubscriptionName",
	"filterid":	"SubscriptionName"
}

aws_neptune_global_cluster = {
	"clfn":		"neptune",
	"descfn":	"describe_global_clusters",
	"topkey":	"GlobalClusters",
	"key":		"GlobalClusterIdentifier",
	"filterid":	"GlobalClusterIdentifier"
}

aws_neptune_parameter_group = {
	"clfn":		"neptune",
	"descfn":	"describe_db_parameter_groups",
	"topkey":	"DBParameterGroups",
	"key":		"DBParameterGroupName",
	"filterid":	"DBParameterGroupName"
}

aws_neptune_subnet_group = {
	"clfn":		"neptune",
	"descfn":	"describe_db_subnet_groups",
	"topkey":	"DBSubnetGroups",
	"key":		"DBSubnetGroupName",
	"filterid":	"DBSubnetGroupName"
}

aws_network_acl_association = {
	"clfn":		"ec2",
	"descfn":	"describe_network_acls",
	"topkey":	"NetworkAcls",
	"key":		"NetworkAclId",
	"filterid":	"NetworkAclId"
}

aws_network_acl_rule = {
	"clfn":		"ec2",
	"descfn":	"describe_network_acls",
	"topkey":	"NetworkAcls",
	"key":		"NetworkAclId",
	"filterid":	"NetworkAclId"
}

aws_network_interface_attachment = {
	"clfn":		"ec2",
	"descfn":	"describe_network_interfaces",
	"topkey":	"NetworkInterfaces",
	"key":		"NetworkInterfaceId",
	"filterid":	"NetworkInterfaceId"
}

aws_network_interface_sg_attachment = {
	"clfn":		"ec2",
	"descfn":	"describe_network_interfaces",
	"topkey":	"NetworkInterfaces",
	"key":		"NetworkInterfaceId",
	"filterid":	"NetworkInterfaceId"
}

aws_networkfirewall_firewall = {
	"clfn":		"network-firewall",
	"descfn":	"list_firewalls",
	"topkey":	"Firewalls",
	"key":		"FirewallArn",
	"filterid":	"FirewallArn"
}

aws_networkfirewall_firewall_policy = {
	"clfn":		"network-firewall",
	"descfn":	"list_firewall_policies",
	"topkey":	"FirewallPolicies",
	"key":		"FirewallPolicyArn",
	"filterid":	"FirewallPolicyArn"
}

aws_networkfirewall_logging_configuration = {
	"clfn":		"network-firewall",
	"descfn":	"list_logging_configurations",
	"topkey":	"LoggingConfigurations",
	"key":		"FirewallArn",
	"filterid":	"FirewallArn"
}

aws_networkfirewall_resource_policy = {
	"clfn":		"network-firewall",
	"descfn":	"list_resource_policies",
	"topkey":	"ResourcePolicies",
	"key":		"ResourceArn",
	"filterid":	"ResourceArn"
}

aws_networkfirewall_rule_group = {
	"clfn":		"network-firewall",
	"descfn":	"list_rule_groups",
	"topkey":	"RuleGroups",
	"key":		"RuleGroupArn",
	"filterid":	"RuleGroupArn"
}

aws_networkmanager_attachment_accepter = {
	"clfn":		"networkmanager",
	"descfn":	"list_attachment_accepters",
	"topkey":	"AttachmentAccepters",
	"key":		"AttachmentId",
	"filterid":	"AttachmentId"
}

aws_networkmanager_connect_attachment = {
	"clfn":		"networkmanager",
	"descfn":	"list_connect_attachments",
	"topkey":	"ConnectAttachments",
	"key":		"AttachmentId",
	"filterid":	"AttachmentId"
}

aws_networkmanager_connect_peer = {
	"clfn":		"networkmanager",
	"descfn":	"list_connect_peers",
	"topkey":	"ConnectPeers",
	"key":		"ConnectPeerId",
	"filterid":	"ConnectPeerId"
}

aws_networkmanager_connection = {
	"clfn":		"networkmanager",
	"descfn":	"list_connections",
	"topkey":	"Connections",
	"key":		"ConnectionId",
	"filterid":	"ConnectionId"
}

aws_networkmanager_core_network = {
	"clfn":		"networkmanager",
	"descfn":	"list_core_networks",
	"topkey":	"CoreNetworks",
	"key":		"CoreNetworkId",
	"filterid":	"CoreNetworkId"
}

aws_networkmanager_core_network_policy_attachment = {
	"clfn":		"networkmanager",
	"descfn":	"list_core_network_policy_attachments",
	"topkey":	"CoreNetworkPolicyAttachments",
	"key":		"CoreNetworkPolicyAttachmentId",
	"filterid":	"CoreNetworkPolicyAttachmentId"
}

aws_networkmanager_customer_gateway_association = {
	"clfn":		"networkmanager",
	"descfn":	"list_customer_gateway_associations",
	"topkey":	"CustomerGatewayAssociations",
	"key":		"CustomerGatewayAssociationId",
	"filterid":	"CustomerGatewayAssociationId"
}

aws_networkmanager_device = {
	"clfn":		"networkmanager",
	"descfn":	"list_devices",
	"topkey":	"Devices",
	"key":		"DeviceId",
	"filterid":	"DeviceId"
}

aws_networkmanager_global_network = {
	"clfn":		"networkmanager",
	"descfn":	"list_global_networks",
	"topkey":	"GlobalNetworks",
	"key":		"GlobalNetworkId",
	"filterid":	"GlobalNetworkId"
}

aws_networkmanager_link = {
	"clfn":		"networkmanager",
	"descfn":	"list_links",
	"topkey":	"Links",
	"key":		"LinkId",
	"filterid":	"LinkId"
}

aws_networkmanager_link_association = {
	"clfn":		"networkmanager",
	"descfn":	"list_link_associations",
	"topkey":	"LinkAssociations",
	"key":		"LinkAssociationId",
	"filterid":	"LinkAssociationId"
}

aws_networkmanager_site = {
	"clfn":		"networkmanager",
	"descfn":	"list_sites",
	"topkey":	"Sites",
	"key":		"SiteId",
	"filterid":	"SiteId"
}

aws_networkmanager_site_to_site_vpn_attachment = {
	"clfn":		"networkmanager",
	"descfn":	"list_site_to_site_vpn_attachments",
	"topkey":	"SiteToSiteVpnAttachments",
	"key":		"SiteToSiteVpnAttachmentId",
	"filterid":	"SiteToSiteVpnAttachmentId"
}

aws_networkmanager_transit_gateway_connect_peer_association = {
	"clfn":		"networkmanager",
	"descfn":	"list_transit_gateway_connect_peers",
	"topkey":	"TransitGatewayConnectPeers",
	"key":		"TransitGatewayConnectPeerId",
	"filterid":	"TransitGatewayConnectPeerId"
}

aws_networkmanager_transit_gateway_peering = {
	"clfn":		"networkmanager",
	"descfn":	"list_transit_gateway_peerings",
	"topkey":	"TransitGatewayPeerings",
	"key":		"TransitGatewayPeeringId",
	"filterid":	"TransitGatewayPeeringId"
}

aws_networkmanager_transit_gateway_registration = {
	"clfn":		"networkmanager",
	"descfn":	"list_transit_gateway_registrations",
	"topkey":	"TransitGatewayRegistrations",
	"key":		"TransitGatewayRegistrationId",
	"filterid":	"TransitGatewayRegistrationId"
}

aws_networkmanager_transit_gateway_route_table_attachment = {
	"clfn":		"networkmanager",
	"descfn":	"list_transit_gateway_route_tables",
	"topkey":	"TransitGatewayRouteTables",
	"key":		"TransitGatewayRouteTableId",
	"filterid":	"TransitGatewayRouteTableId"
}

aws_networkmanager_vpc_attachment = {
	"clfn":		"networkmanager",
	"descfn":	"list_vpc_attachments",
	"topkey":	"VpcAttachments",
	"key":		"VpcAttachmentId",
	"filterid":	"VpcAttachmentId"
}

aws_oam_link = {
	"clfn":		"networkmanager",
	"descfn":	"list_links",
	"topkey":	"Links",
	"key":		"LinkId",
	"filterid":	"LinkId"
}

aws_oam_sink = {
	"clfn":		"networkmanager",
	"descfn":	"list_links",
	"topkey":	"Links",
	"key":		"LinkId",
	"filterid":	"LinkId"
}

aws_oam_sink_policy = {
	"clfn":		"networkmanager",
	"descfn":	"list_links",
	"topkey":	"Links",
	"key":		"LinkId",
	"filterid":	"LinkId"
}

aws_opensearch_domain = {
	"clfn":		"opensearch",
	"descfn":	"list_domain_names",
	"topkey":	"DomainNames",
	"key":		"DomainName",
	"filterid":	"DomainName"
}

aws_opensearch_domain_policy = {
	"clfn":		"opensearch",
	"descfn":	"list_domain_names",
	"topkey":	"DomainNames",
	"key":		"DomainName",
	"filterid":	"DomainName"
}

aws_opensearch_domain_saml_options = {
	"clfn":		"opensearch",
	"descfn":	"list_domain_names",
	"topkey":	"DomainNames",
	"key":		"DomainName",
	"filterid":	"DomainName"
}

aws_opensearch_inbound_connection_accepter = {
	"clfn":		"opensearch",
	"descfn":	"list_inbound_connection_accepters",
	"topkey":	"InboundConnectionAccepters",
	"key":		"ConnectionId",
	"filterid":	"ConnectionId"
}

aws_opensearch_outbound_connection = {
	"clfn":		"opensearch",
	"descfn":	"list_inbound_connection_accepters",
	"topkey":	"InboundConnectionAccepters",
	"key":		"InboundConnectionId",
	"filterid":	"InboundConnectionId"
}

aws_opensearch_package = {
	"clfn":		"opensearch",
	"descfn":	"list_packages",
	"topkey":	"Packages",
	"key":		"PackageID",
	"filterid":	"PackageID"
}

aws_opensearch_package_association = {
	"clfn":		"opensearch",
	"descfn":	"list_packages",
	"topkey":	"Packages",
	"key":		"PackageID",
	"filterid":	"PackageID"
}

aws_opensearch_vpc_endpoint = {
	"clfn":		"opensearch",
	"descfn":	"list_vpc_endpoints",
	"topkey":	"VpcEndpoints",
	"key":		"VpcEndpointId",
	"filterid":	"VpcEndpointId"
}

aws_opensearchserverless_access_policy = {
	"clfn":		"opensearch",
	"descfn":	"list_access_policies",
	"topkey":	"AccessPolicies",
	"key":		"PolicyId",
	"filterid":	"PolicyId"
}

aws_opensearchserverless_collection = {
	"clfn":		"opensearch",
	"descfn":	"list_collections",
	"topkey":	"Collections",
	"key":		"CollectionId",
	"filterid":	"CollectionId"
}

aws_opensearchserverless_lifecycle_policy = {
	"clfn":		"opensearch",
	"descfn":	"list_lifecycle_policies",
	"topkey":	"LifecyclePolicies",
	"key":		"PolicyId",
	"filterid":	"PolicyId"
}

aws_opensearchserverless_security_config = {
	"clfn":		"opensearch",
	"descfn":	"list_security_configs",
	"topkey":	"SecurityConfigs",
	"key":		"SecurityConfigId",
	"filterid":	"SecurityConfigId"
}

aws_opensearchserverless_security_policy = {
	"clfn":		"opensearch",
	"descfn":	"list_security_policies",
	"topkey":	"SecurityPolicies",
	"key":		"PolicyId",
	"filterid":	"PolicyId"
}

aws_opensearchserverless_vpc_endpoint = {
	"clfn":		"opensearch",
	"descfn":	"list_vpc_endpoints",
	"topkey":	"VpcEndpoints",
	"key":		"VpcEndpointId",
	"filterid":	"VpcEndpointId"
}

aws_opsworks_application = {
	"clfn":		"opsworks",
	"descfn":	"list_applications",
	"topkey":	"Applications",
	"key":		"ApplicationId",
	"filterid":	"ApplicationId"
}

aws_opsworks_custom_layer = {
	"clfn":		"opsworks",
	"descfn":	"list_custom_layers",
	"topkey":	"CustomLayers",
	"key":		"LayerId",
	"filterid":	"LayerId"
}

aws_opsworks_ecs_cluster_layer = {
	"clfn":		"opsworks",
	"descfn":	"describe_ecs_clusters",
	"topkey":	"EcsClusters",
	"key":		"NOIMPORT",
	"filterid":	"LayerId"
}

aws_opsworks_ganglia_layer = {
	"clfn":		"opsworks",
	"descfn":	"list_ganglia_layers",
	"topkey":	"GangliaLayers",
	"key":		"LayerId",
	"filterid":	"LayerId"
}

aws_opsworks_haproxy_layer = {
	"clfn":		"opsworks",
	"descfn":	"list_haproxy_layers",
	"topkey":	"HaproxyLayers",
	"key":		"LayerId",
	"filterid":	"LayerId"
}

aws_opsworks_instance = {
	"clfn":		"opsworks",
	"descfn":	"list_instances",
	"topkey":	"Instances",
	"key":		"InstanceId",
	"filterid":	"InstanceId"
}

aws_opsworks_java_app_layer = {
	"clfn":		"opsworks",
	"descfn":	"list_java_app_layers",
	"topkey":	"JavaAppLayers",
	"key":		"LayerId",
	"filterid":	"LayerId"
}

aws_opsworks_memcached_layer = {
	"clfn":		"opsworks",
	"descfn":	"list_memcached_layers",
	"topkey":	"MemcachedLayers",
	"key":		"LayerId",
	"filterid":	"LayerId"
}

aws_opsworks_mysql_layer = {
	"clfn":		"opsworks",
	"descfn":	"list_mysql_layers",
	"topkey":	"MysqlLayers",
	"key":		"LayerId",
	"filterid":	"LayerId"
}

aws_opsworks_nodejs_app_layer = {
	"clfn":		"opsworks",
	"descfn":	"list_nodejs_app_layers",
	"topkey":	"NodejsAppLayers",
	"key":		"LayerId",
	"filterid":	"LayerId"
}

aws_opsworks_permission = {
	"clfn":		"opsworks",
	"descfn":	"list_permissions",
	"topkey":	"Permissions",
	"key":		"PermissionId",
	"filterid":	"PermissionId"
}

aws_opsworks_php_app_layer = {
	"clfn":		"opsworks",
	"descfn":	"list_php_app_layers",
	"topkey":	"PhpAppLayers",
	"key":		"LayerId",
	"filterid":	"LayerId"
}

aws_opsworks_rails_app_layer = {
	"clfn":		"opsworks",
	"descfn":	"list_rails_app_layers",
	"topkey":	"RailsAppLayers",
	"key":		"LayerId",
	"filterid":	"LayerId"
}

aws_opsworks_rds_db_instance = {
	"clfn":		"opsworks",
	"descfn":	"list_rds_db_instances",
	"topkey":	"RdsDbInstances",
	"key":		"DbInstanceArn",
	"filterid":	"DbInstanceArn"
}

aws_opsworks_stack = {
	"clfn":		"opsworks",
	"descfn":	"list_stacks",
	"topkey":	"Stacks",
	"key":		"StackId",
	"filterid":	"StackId"
}

aws_opsworks_static_web_layer = {
	"clfn":		"opsworks",
	"descfn":	"list_static_web_layers",
	"topkey":	"StaticWebLayers",
	"key":		"LayerId",
	"filterid":	"LayerId"
}

aws_opsworks_user_profile = {
	"clfn":		"opsworks",
	"descfn":	"list_user_profiles",
	"topkey":	"UserProfiles",
	"key":		"IamUserArn",
	"filterid":	"IamUserArn"
}

aws_organizations_account = {
	"clfn":		"organizations",
	"descfn":	"list_accounts",
	"topkey":	"Accounts",
	"key":		"Id",
	"filterid":	"Id"
}

aws_organizations_delegated_administrator = {
	"clfn":		"organizations",
	"descfn":	"list_delegated_administrators",
	"topkey":	"DelegatedAdministrators",
	"key":		"Id",
	"filterid":	"Id"
}

aws_organizations_organization = {
	"clfn":		"organizations",
	"descfn":	"list_organizations",
	"topkey":	"Organization",
	"key":		"Id",
	"filterid":	"Id"
}

aws_organizations_organizational_unit = {
	"clfn":		"organizations",
	"descfn":	"list_organizational_units",
	"topkey":	"OrganizationalUnits",
	"key":		"Id",
	"filterid":	"Id"
}

aws_organizations_policy = {
	"clfn":		"organizations",
	"descfn":	"list_policies",
	"topkey":	"Policies",
	"key":		"Id",
	"filterid":	"Id"
}

aws_organizations_policy_attachment = {
	"clfn":		"organizations",
	"descfn":	"list_policy_attachments",
	"topkey":	"PolicyAttachments",
	"key":		"Id",
	"filterid":	"Id"
}

aws_organizations_resource_policy = {
	"clfn":		"organizations",
	"descfn":	"list_resource_policies",
	"topkey":	"ResourcePolicies",
	"key":		"Id",
	"filterid":	"Id"
}

aws_pinpoint_adm_channel = {
	"clfn":		"pinpoint",
	"descfn":	"list_adm_channels",
	"topkey":	"AdmChannels",
	"key":		"Id",
	"filterid":	"Id"
}

aws_pinpoint_apns_channel = {
	"clfn":		"pinpoint",
	"descfn":	"list_apns_channels",
	"topkey":	"ApnsChannels",
	"key":		"Id",
	"filterid":	"Id"
}

aws_pinpoint_apns_sandbox_channel = {
	"clfn":		"pinpoint",
	"descfn":	"list_apns_sandbox_channels",
	"topkey":	"ApnsSandboxChannels",
	"key":		"Id",
	"filterid":	"Id"
}

aws_pinpoint_apns_voip_channel = {
	"clfn":		"pinpoint",
	"descfn":	"list_apns_voip_channels",
	"topkey":	"ApnsVoipChannels",
	"key":		"Id",
	"filterid":	"Id"
}

aws_pinpoint_apns_voip_sandbox_channel = {
	"clfn":		"pinpoint",
	"descfn":	"list_apns_voip_sandbox_channels",
	"topkey":	"ApnsVoipSandboxChannels",
	"key":		"Id",
	"filterid":	"Id"
}

aws_pinpoint_app = {
	"clfn":		"pinpoint",
	"descfn":	"list_apps",
	"topkey":	"Apps",
	"key":		"Id",
	"filterid":	"Id"
}

aws_pinpoint_baidu_channel = {
	"clfn":		"pinpoint",
	"descfn":	"list_baidu_channels",
	"topkey":	"BaiduChannels",
	"key":		"Id",
	"filterid":	"Id"
}

aws_pinpoint_email_channel = {
	"clfn":		"pinpoint",
	"descfn":	"list_email_channels",
	"topkey":	"EmailChannels",
	"key":		"Id",
	"filterid":	"Id"
}

aws_pinpoint_event_stream = {
	"clfn":		"pinpoint",
	"descfn":	"list_event_streams",
	"topkey":	"EventStreams",
	"key":		"Id",
	"filterid":	"Id"
}

aws_pinpoint_gcm_channel = {
	"clfn":		"pinpoint",
	"descfn":	"list_gcm_channels",
	"topkey":	"GcmChannels",
	"key":		"Id",
	"filterid":	"Id"
}

aws_pinpoint_sms_channel = {
	"clfn":		"pinpoint",
	"descfn":	"list_sms_channels",
	"topkey":	"SmsChannels",
	"key":		"Id",
	"filterid":	"Id"
}

aws_pipes_pipe = {
	"clfn":		"pipes",
	"descfn":	"list_pipes",
	"topkey":	"Pipes",
	"key":		"Name",
	"filterid":	"Name"
}

aws_placement_group = {
	"clfn":		"ec2",
	"descfn":	"describe_placement_groups",
	"topkey":	"PlacementGroups",
	"key":		"GroupName",
	"filterid":	"GroupName"
}

aws_prometheus_alert_manager_definition = {
	"clfn":		"amp",
	"descfn":	"list_alertmanager_definition",
	"topkey":	"AlertmanagerDefinition",
	"key":		"Name",
	"filterid":	"Name"
}

aws_prometheus_rule_group_namespace = {
	"clfn":		"amp",
	"descfn":	"list_rule_group_namespaces",
	"topkey":	"RuleGroupNamespaces",
	"key":		"Name",
	"filterid":	"Name"
}

aws_prometheus_workspace = {
	"clfn":		"amp",
	"descfn":	"list_workspaces",
	"topkey":	"Workspaces",
	"key":		"Name",
	"filterid":	"Name"
}

aws_proxy_protocol_policy = {
	"clfn":		"wafv2",
	"descfn":	"list_proxy_protocol_policies",
	"topkey":	"ProxyProtocolPolicies",
	"key":		"Name",
	"filterid":	"Name"
}

aws_qldb_ledger = {
	"clfn":		"qldb",
	"descfn":	"list_ledgers",
	"topkey":	"Ledgers",
	"key":		"Name",
	"filterid":	"Name"
}

aws_qldb_stream = {
	"clfn":		"qldb",
	"descfn":	"list_streams",
	"topkey":	"Streams",
	"key":		"Name",
	"filterid":	"Name"
}

aws_quicksight_account_subscription = {
	"clfn":		"quicksight",
	"descfn":	"list_account_subscriptions",
	"topkey":	"AccountSubscriptions",
	"key":		"SubscriptionId",
	"filterid":	"SubscriptionId"
}

aws_quicksight_analysis = {
	"clfn":		"quicksight",
	"descfn":	"list_analyses",
	"topkey":	"Analyses",
	"key":		"AnalysisId",
	"filterid":	"AnalysisId"
}

aws_quicksight_dashboard = {
	"clfn":		"quicksight",
	"descfn":	"list_dashboards",
	"topkey":	"Dashboards",
	"key":		"DashboardId",
	"filterid":	"DashboardId"
}

aws_quicksight_data_set = {
	"clfn":		"quicksight",
	"descfn":	"list_data_sets",
	"topkey":	"DataSets",
	"key":		"DataSetId",
	"filterid":	"DataSetId"
}

aws_quicksight_data_source = {
	"clfn":		"quicksight",
	"descfn":	"list_data_sources",
	"topkey":	"DataSources",
	"key":		"DataSourceId",
	"filterid":	"DataSourceId"
}

aws_quicksight_folder = {
	"clfn":		"quicksight",
	"descfn":	"list_folders",
	"topkey":	"Folders",
	"key":		"FolderId",
	"filterid":	"FolderId"
}

aws_quicksight_folder_membership = {
	"clfn":		"quicksight",
	"descfn":	"list_folder_memberships",
	"topkey":	"FolderMemberships",
	"key":		"FolderMembershipId",
	"filterid":	"FolderMembershipId"
}

aws_quicksight_group = {
	"clfn":		"quicksight",
	"descfn":	"list_groups",
	"topkey":	"Groups",
	"key":		"GroupName",
	"filterid":	"GroupName"
}

aws_quicksight_group_membership = {
	"clfn":		"quicksight",
	"descfn":	"list_group_memberships",
	"topkey":	"GroupMemberships",
	"key":		"GroupMembershipId",
	"filterid":	"GroupMembershipId"
}

aws_quicksight_iam_policy_assignment = {
	"clfn":		"quicksight",
	"descfn":	"list_iam_policy_assignments",
	"topkey":	"IamPolicyAssignments",
	"key":		"AssignmentName",
	"filterid":	"AssignmentName"
}

aws_quicksight_ingestion = {
	"clfn":		"quicksight",
	"descfn":	"list_ingestions",
	"topkey":	"Ingestions",
	"key":		"IngestionId",
	"filterid":	"IngestionId"
}

aws_quicksight_namespace = {
	"clfn":		"quicksight",
	"descfn":	"list_namespaces",
	"topkey":	"Namespaces",
	"key":		"Namespace",
	"filterid":	"Namespace"
}

aws_quicksight_refresh_schedule = {
	"clfn":		"quicksight",
	"descfn":	"list_refresh_schedules",
	"topkey":	"RefreshSchedules",
	"key":		"ScheduleId",
	"filterid":	"ScheduleId"
}

aws_quicksight_template = {
	"clfn":		"quicksight",
	"descfn":	"list_templates",
	"topkey":	"Templates",
	"key":		"TemplateId",
	"filterid":	"TemplateId"
}

aws_quicksight_template_alias = {
	"clfn":		"quicksight",
	"descfn":	"list_template_aliases",
	"topkey":	"TemplateAliases",
	"key":		"AliasName",
	"filterid":	"AliasName"
}

aws_quicksight_theme = {
	"clfn":		"quicksight",
	"descfn":	"list_themes",
	"topkey":	"Themes",
	"key":		"ThemeId",
	"filterid":	"ThemeId"
}

aws_quicksight_user = {
	"clfn":		"quicksight",
	"descfn":	"list_users",
	"topkey":	"Users",
	"key":		"UserName",
	"filterid":	"UserName"
}

aws_quicksight_vpc_connection = {
	"clfn":		"quicksight",
	"descfn":	"list_vpc_connections",
	"topkey":	"VpcConnections",
	"key":		"VpcConnectionId",
	"filterid":	"VpcConnectionId"
}

aws_ram_principal_association = {
	"clfn":		"ram",
	"descfn":	"list_principal_associations",
	"topkey":	"PrincipalAssociations",
	"key":		"PrincipalAssociationId",
	"filterid":	"PrincipalAssociationId"
}

aws_ram_resource_association = {
	"clfn":		"ram",
	"descfn":	"list_resource_associations",
	"topkey":	"ResourceAssociations",
	"key":		"ResourceAssociationId",
	"filterid":	"ResourceAssociationId"
}

aws_ram_resource_share = {
	"clfn":		"ram",
	"descfn":	"list_resource_shares",
	"topkey":	"ResourceShares",
	"key":		"ResourceShareArn",
	"filterid":	"ResourceShareArn"
}

aws_ram_resource_share_accepter = {
	"clfn":		"ram",
	"descfn":	"list_resource_share_accepters",
	"topkey":	"ResourceShareAccepters",
	"key":		"ResourceShareAccepterArn",
	"filterid":	"ResourceShareAccepterArn"
}

aws_ram_sharing_with_organization = {
	"clfn":		"ram",
	"descfn":	"list_sharing_accounts",
	"topkey":	"AccountIds",
	"key":		"AccountId",
	"filterid":	"AccountId"
}

aws_rbin_rule = {
	"clfn":		"rbin",
	"descfn":	"list_resolver_rules",
	"topkey":	"ResolverRules",
	"key":		"Id",
	"filterid":	"Id"
}

aws_rds_cluster_activity_stream = {
	"clfn":		"rds",
	"descfn":	"describe_db_cluster_activity_stream",
	"topkey":	"ActivityStream",
	"key":		"ActivityStreamId",
	"filterid":	"ActivityStreamId"
}

aws_rds_cluster_endpoint = {
	"clfn":		"rds",
	"descfn":	"describe_db_cluster_endpoints",
	"topkey":	"DBClusterEndpoints",
	"key":		"DBClusterEndpointIdentifier",
	"filterid":	"DBClusterEndpointIdentifier"
}

aws_rds_cluster_role_association = {
	"clfn":		"rds",
	"descfn":	"describe_db_cluster_role_associations",
	"topkey":	"DBClusterRoleAssociations",
	"key":		"DBClusterRoleAssociationId",
	"filterid":	"DBClusterRoleAssociationId"
}

aws_rds_custom_db_engine_version = {
	"clfn":		"rds",
	"descfn":	"describe_custom_db_engine_versions",
	"topkey":	"CustomDBEngineVersions",
	"key":		"EngineVersion",
	"filterid":	"EngineVersion"
}

aws_rds_export_task = {
	"clfn":		"rds",
	"descfn":	"describe_export_tasks",
	"topkey":	"ExportTasks",
	"key":		"ExportTaskIdentifier",
	"filterid":	"ExportTaskIdentifier"
}

aws_rds_global_cluster = {
	"clfn":		"rds",
	"descfn":	"describe_global_clusters",
	"topkey":	"GlobalClusters",
	"key":		"GlobalClusterIdentifier",
	"filterid":	"GlobalClusterIdentifier"
}

aws_rds_reserved_instance = {
	"clfn":		"rds",
	"descfn":	"describe_reserved_db_instances",
	"topkey":	"ReservedDBInstances",
	"key":		"ReservedDBInstanceId",
	"filterid":	"ReservedDBInstanceId"
}

aws_redshift_authentication_profile = {
	"clfn":		"redshift",
	"descfn":	"describe_authentication_profiles",
	"topkey":	"AuthenticationProfiles",
	"key":		"AuthenticationProfileName",
	"filterid":	"AuthenticationProfileName"
}

aws_redshift_cluster_iam_roles = {
	"clfn":		"redshift",
	"descfn":	"describe_cluster_iam_roles",
	"topkey":	"ClusterIamRoles",
	"key":		"ClusterIdentifier",
	"filterid":	"ClusterIdentifier"
}

aws_redshift_cluster_snapshot = {
	"clfn":		"redshift",
	"descfn":	"describe_cluster_snapshots",
	"topkey":	"Snapshots",
	"key":		"SnapshotIdentifier",
	"filterid":	"SnapshotIdentifier"
}

aws_redshift_endpoint_access = {
	"clfn":		"redshift",
	"descfn":	"describe_endpoint_access",
	"topkey":	"EndpointAccess",
	"key":		"EndpointName",
	"filterid":	"EndpointName"
}

aws_redshift_endpoint_authorization = {
	"clfn":		"redshift",
	"descfn":	"describe_endpoint_authorization",
	"topkey":	"EndpointAuthorization",
	"key":		"EndpointName",
	"filterid":	"EndpointName"
}

aws_redshift_event_subscription = {
	"clfn":		"redshift",
	"descfn":	"describe_event_subscriptions",
	"topkey":	"EventSubscriptionsList",
	"key":		"SubscriptionName",
	"filterid":	"SubscriptionName"
}

aws_redshift_hsm_client_certificate = {
	"clfn":		"redshift",
	"descfn":	"describe_hsm_client_certificates",
	"topkey":	"HsmClientCertificates",
	"key":		"HsmClientCertificateIdentifier",
	"filterid":	"HsmClientCertificateIdentifier"
}

aws_redshift_hsm_configuration = {
	"clfn":		"redshift",
	"descfn":	"describe_hsm_configurations",
	"topkey":	"HsmConfigurations",
	"key":		"HsmConfigurationIdentifier",
	"filterid":	"HsmConfigurationIdentifier"
}

aws_redshift_partner = {
	"clfn":		"redshift",
	"descfn":	"describe_partners",
	"topkey":	"Partners",
	"key":		"PartnerName",
	"filterid":	"PartnerName"
}

aws_redshift_resource_policy = {
	"clfn":		"redshift",
	"descfn":	"describe_resource_policies",
	"topkey":	"ResourcePolicies",
	"key":		"ResourcePolicyId",
	"filterid":	"ResourcePolicyId"
}

aws_redshift_scheduled_action = {
	"clfn":		"redshift",
	"descfn":	"describe_scheduled_actions",
	"topkey":	"ScheduledActions",
	"key":		"ScheduledActionName",
	"filterid":	"ScheduledActionName"
}

aws_redshift_snapshot_copy_grant = {
	"clfn":		"redshift",
	"descfn":	"describe_snapshot_copy_grants",
	"topkey":	"SnapshotCopyGrants",
	"key":		"SnapshotCopyGrantName",
	"filterid":	"SnapshotCopyGrantName"
}

aws_redshift_snapshot_schedule = {
	"clfn":		"redshift",
	"descfn":	"describe_snapshot_schedules",
	"topkey":	"SnapshotSchedules",
	"key":		"ScheduleIdentifier",
	"filterid":	"ScheduleIdentifier"
}

aws_redshift_snapshot_schedule_association = {
	"clfn":		"redshift",
	"descfn":	"describe_snapshot_schedule_associations",
	"topkey":	"SnapshotScheduleAssociations",
	"key":		"ScheduleAssociationId",
	"filterid":	"ScheduleAssociationId"
}

aws_redshift_usage_limit = {
	"clfn":		"redshift",
	"descfn":	"describe_usage_limits",
	"topkey":	"UsageLimits",
	"key":		"UsageLimitId",
	"filterid":	"UsageLimitId"
}

aws_redshiftdata_statement = {
	"clfn":		"redshift-data",
	"descfn":	"describe_statement",
	"topkey":	"Statement",
	"key":		"Id",
	"filterid":	"Id"
}

aws_redshiftserverless_endpoint_access = {
	"clfn":		"redshift-serverless",
	"descfn":	"describe_endpoint_access",
	"topkey":	"EndpointAccess",
	"key":		"EndpointName",
	"filterid":	"EndpointName"
}

aws_redshiftserverless_resource_policy = {
	"clfn":		"redshift-serverless",
	"descfn":	"describe_resource_policies",
	"topkey":	"ResourcePolicies",
	"key":		"ResourcePolicyId",
	"filterid":	"ResourcePolicyId"
}

aws_redshiftserverless_snapshot = {
	"clfn":		"redshift-serverless",
	"descfn":	"describe_snapshots",
	"topkey":	"Snapshots",
	"key":		"SnapshotName",
	"filterid":	"SnapshotName"
}

aws_redshiftserverless_usage_limit = {
	"clfn":		"redshift-serverless",
	"descfn":	"describe_usage_limits",
	"topkey":	"UsageLimits",
	"key":		"UsageLimitId",
	"filterid":	"UsageLimitId"
}

aws_resourceexplorer2_index = {
	"clfn":		"resource-explorer-2",
	"descfn":	"list_indices",
	"topkey":	"Indices",
	"key":		"Name",
	"filterid":	"Name"
}

aws_resourceexplorer2_view = {
	"clfn":		"resource-explorer-2",
	"descfn":	"list_views",
	"topkey":	"Views",
	"key":		"Name",
	"filterid":	"Name"
}

aws_resourcegroups_group = {
	"clfn":		"resource-groups",
	"descfn":	"list_groups",
	"topkey":	"GroupIdentifiers",
	"key":		"GroupName",
	"filterid":	"GroupName"
}

aws_resourcegroups_resource = {
	"clfn":		"resource-groups",
	"descfn":	"list_resources",
	"topkey":	"ResourceIdentifiers",
	"key":		"ResourceArn",
	"filterid":	"ResourceArn"
}

aws_rolesanywhere_profile = {
	"clfn":		"rolesanywhere",
	"descfn":	"list_profiles",
	"topkey":	"Profiles",
	"key":		"ProfileName",
	"filterid":	"ProfileName"
}

aws_rolesanywhere_trust_anchor = {
	"clfn":		"rolesanywhere",
	"descfn":	"list_trust_anchors",
	"topkey":	"TrustAnchors",
	"key":		"TrustAnchorId",
	"filterid":	"TrustAnchorId"
}

aws_route = {
	"clfn":		"ec2",
	"descfn":	"describe_route_tables",
	"topkey":	"RouteTables",
	"key":		"RouteTableId",
	"filterid":	"RouteTableId"
}

aws_route53_cidr_collection = {
	"clfn":		"route53",
	"descfn":	"list_cidr_collections",
	"topkey":	"CidrCollections",
	"key":		"Id",
	"filterid":	"Id"
}

aws_route53_cidr_location = {
	"clfn":		"route53",
	"descfn":	"list_cidr_locations",
	"topkey":	"CidrLocations",
	"key":		"Id",
	"filterid":	"Id"
}

aws_route53_delegation_set = {
	"clfn":		"route53",
	"descfn":	"list_delegation_sets",
	"topkey":	"DelegationSets",
	"key":		"Id",
	"filterid":	"Id"
}

aws_route53_health_check = {
	"clfn":		"route53",
	"descfn":	"list_health_checks",
	"topkey":	"HealthChecks",
	"key":		"Id",
	"filterid":	"Id"
}

aws_route53_hosted_zone_dnssec = {
	"clfn":		"route53",
	"descfn":	"list_hosted_zone_dnssec",
	"topkey":	"HostedZoneDNSSEC",
	"key":		"Id",
	"filterid":	"Id"
}

aws_route53_key_signing_key = {
	"clfn":		"route53",
	"descfn":	"list_key_signing_keys",
	"topkey":	"KeySigningKeys",
	"key":		"Id",
	"filterid":	"Id"
}

aws_route53_query_log = {
	"clfn":		"route53",
	"descfn":	"list_query_logs",
	"topkey":	"QueryLogs",
	"key":		"Id",
	"filterid":	"Id"
}

aws_route53_record = {
	"clfn":		"route53",
	"descfn":	"list_resource_record_sets",
	"topkey":	"ResourceRecordSets",
	"key":		"Name",
	"filterid":	"Name"
}

aws_route53_resolver_config = {
	"clfn":		"route53",
	"descfn":	"list_resolver_configs",
	"topkey":	"ResolverConfigs",
	"key":		"Id",
	"filterid":	"Id"
}

aws_route53_resolver_dnssec_config = {
	"clfn":		"route53",
	"descfn":	"list_resolver_dnssec_configs",
	"topkey":	"ResolverDNSSECConfigs",
	"key":		"Id",
	"filterid":	"Id"
}

aws_route53_resolver_endpoint = {
	"clfn":		"route53",
	"descfn":	"list_resolver_endpoints",
	"topkey":	"ResolverEndpoints",
	"key":		"Id",
	"filterid":	"Id"
}

aws_route53_resolver_firewall_config = {
	"clfn":		"route53",
	"descfn":	"list_resolver_firewall_configs",
	"topkey":	"ResolverFirewallConfigs",
	"key":		"Id",
	"filterid":	"Id"
}

aws_route53_resolver_firewall_domain_list = {
	"clfn":		"route53",
	"descfn":	"list_resolver_firewall_domain_lists",
	"topkey":	"ResolverFirewallDomainLists",
	"key":		"Id",
	"filterid":	"Id"
}

aws_route53_resolver_firewall_rule = {
	"clfn":		"route53",
	"descfn":	"list_resolver_firewall_rules",
	"topkey":	"ResolverFirewallRules",
	"key":		"Id",
	"filterid":	"Id"
}

aws_route53_resolver_firewall_rule_group = {
	"clfn":		"route53",
	"descfn":	"list_resolver_firewall_rule_groups",
	"topkey":	"ResolverFirewallRuleGroups",
	"key":		"Id",
	"filterid":	"Id"
}

aws_route53_resolver_query_log_config = {
	"clfn":		"route53",
	"descfn":	"list_resolver_query_log_configs",
	"topkey":	"ResolverQueryLogConfigs",
	"key":		"Id",
	"filterid":	"Id"
}

aws_route53_resolver_query_log_config_association = {
	"clfn":		"route53",
	"descfn":	"list_resolver_query_log_config_associations",
	"topkey":	"ResolverQueryLogConfigAssociations",
	"key":		"Id",
	"filterid":	"Id"
}

aws_route53_resolver_rule = {
	"clfn":		"route53",
	"descfn":	"list_resolver_rules",
	"topkey":	"ResolverRules",
	"key":		"Id",
	"filterid":	"Id"
}

aws_route53_resolver_rule_association = {
	"clfn":		"route53",
	"descfn":	"list_resolver_rule_associations",
	"topkey":	"ResolverRuleAssociations",
	"key":		"Id",
	"filterid":	"Id"
}

aws_route53_traffic_policy = {
	"clfn":		"route53",
	"descfn":	"list_traffic_policies",
	"topkey":	"TrafficPolicies",
	"key":		"Id",
	"filterid":	"Id"
}

aws_route53_traffic_policy_instance = {
	"clfn":		"route53",
	"descfn":	"list_traffic_policy_instances",
	"topkey":	"TrafficPolicyInstances",
	"key":		"Id",
	"filterid":	"Id"
}

aws_route53_vpc_association_authorization = {
	"clfn":		"route53",
	"descfn":	"list_vpc_associations_authorization",
	"topkey":	"VPCAssociations",
	"key":		"Id",
	"filterid":	"Id"
}

aws_route53_zone = {
	"clfn":		"route53",
	"descfn":	"list_hosted_zones",
	"topkey":	"HostedZones",
	"key":		"Name",
	"filterid":	"Name"
}

aws_route53_zone_association = {
	"clfn":		"route53",
	"descfn":	"list_hosted_zone_associations",
	"topkey":	"HostedZoneAssociations",
	"key":		"Id",
	"filterid":	"Id"
}

aws_route53domains_registered_domain = {
	"clfn":		"route53domains",
	"descfn":	"list_domains",
	"topkey":	"Domains",
	"key":		"DomainName",
	"filterid":	"DomainName"
}

aws_route53recoverycontrolconfig_cluster = {
	"clfn":		"route53-recovery-control-config",
	"descfn":	"list_clusters",
	"topkey":	"Clusters",
	"key":		"ClusterArn",
	"filterid":	"ClusterArn"
}

aws_route53recoverycontrolconfig_control_panel = {
	"clfn":		"route53-recovery-control-config",
	"descfn":	"list_control_panels",
	"topkey":	"ControlPanels",
	"key":		"ControlPanelArn",
	"filterid":	"ControlPanelArn"
}

aws_route53recoverycontrolconfig_routing_control = {
	"clfn":		"route53-recovery-control-config",
	"descfn":	"list_routing_controls",
	"topkey":	"RoutingControls",
	"key":		"RoutingControlArn",
	"filterid":	"RoutingControlArn"
}

aws_route53recoverycontrolconfig_safety_rule = {
	"clfn":		"route53-recovery-control-config",
	"descfn":	"list_safety_rules",
	"topkey":	"SafetyRules",
	"key":		"SafetyRuleArn",
	"filterid":	"SafetyRuleArn"
}

aws_route53recoveryreadiness_cell = {
	"clfn":		"route53-recovery-readiness",
	"descfn":	"list_cells",
	"topkey":	"Cells",
	"key":		"CellArn",
	"filterid":	"CellArn"
}

aws_route53recoveryreadiness_readiness_check = {
	"clfn":		"route53-recovery-readiness",
	"descfn":	"list_readiness_checks",
	"topkey":	"ReadinessChecks",
	"key":		"ReadinessCheckArn",
	"filterid":	"ReadinessCheckArn"
}

aws_route53recoveryreadiness_recovery_group = {
	"clfn":		"route53-recovery-readiness",
	"descfn":	"list_recovery_groups",
	"topkey":	"RecoveryGroups",
	"key":		"RecoveryGroupArn",
	"filterid":	"RecoveryGroupArn"
}

aws_route53recoveryreadiness_resource_set = {
	"clfn":		"route53-recovery-readiness",
	"descfn":	"list_resource_sets",
	"topkey":	"ResourceSets",
	"key":		"ResourceSetArn",
	"filterid":	"ResourceSetArn"
}

aws_rum_app_monitor = {
	"clfn":		"rum",
	"descfn":	"list_app_monitors",
	"topkey":	"AppMonitors",
	"key":		"Name",
	"filterid":	"Name"
}

aws_rum_metrics_destination = {
	"clfn":		"rum",
	"descfn":	"list_metrics_destinations",
	"topkey":	"MetricsDestinations",
	"key":		"Name",
	"filterid":	"Name"
}

aws_s3_access_point = {
	"clfn":		"s3",
	"descfn":	"list_access_points",
	"topkey":	"AccessPoints",
	"key":		"Name",
	"filterid":	"Name"
}

aws_s3_account_public_access_block = {
	"clfn":		"s3",
	"descfn":	"get_public_access_block",
	"topkey":	"PublicAccessBlockConfiguration",
	"key":		"BlockPublicAcls",
	"filterid":	"BlockPublicAcls"
}

aws_s3_bucket = {
	"clfn":		"s3",
	"descfn":	"list_buckets",
	"topkey":	"Buckets",
	"key":		"Name",
	"filterid":	"Name"
}

aws_s3_bucket_accelerate_configuration = {
	"clfn":		"s3",
	"descfn":	"get_bucket_accelerate_configuration",
	"topkey":	"Status",
	"key":		"Status",
	"filterid":	"Status"
}

aws_s3_bucket_acl = {
	"clfn":		"s3",
	"descfn":	"get_bucket_acl",
	"topkey":	"Grants",
	"key":		"Grantee.DisplayName",
	"filterid":	"Grantee.DisplayName"
}

aws_s3_bucket_analytics_configuration = {
	"clfn":		"s3",
	"descfn":	"get_bucket_analytics_configuration",
	"topkey":	"AnalyticsConfiguration",
	"key":		"Id",
	"filterid":	"Id"
}

aws_s3_bucket_cors_configuration = {
	"clfn":		"s3",
	"descfn":	"get_bucket_cors_configuration",
	"topkey":	"CORSRules",
	"key":		"AllowedMethods",
	"filterid":	"AllowedMethods"
}

aws_s3_bucket_intelligent_tiering_configuration = {
	"clfn":		"s3",
	"descfn":	"get_bucket_intelligent_tiering_configuration",
	"topkey":	"IntelligentTieringConfiguration",
	"key":		"Id",
	"filterid":	"Id"
}

aws_s3_bucket_inventory = {
	"clfn":		"s3",
	"descfn":	"get_bucket_inventory_configuration",
	"topkey":	"InventoryConfiguration",
	"key":		"Id",
	"filterid":	"Id"
}

aws_s3_bucket_lifecycle_configuration = {
	"clfn":		"s3",
	"descfn":	"get_bucket_lifecycle_configuration",
	"topkey":	"Rules",
	"key":		"ID",
	"filterid":	"ID"
}

aws_s3_bucket_logging = {
	"clfn":		"s3",
	"descfn":	"get_bucket_logging",
	"topkey":	"LoggingEnabled",
	"key":		"TargetBucket",
	"filterid":	"TargetBucket"
}

aws_s3_bucket_metric = {
	"clfn":		"s3",
	"descfn":	"get_bucket_metrics_configuration",
	"topkey":	"MetricsConfiguration",
	"key":		"Id",
	"filterid":	"Id"
}

aws_s3_bucket_notification = {
	"clfn":		"s3",
	"descfn":	"get_bucket_notification_configuration",
	"topkey":	"TopicConfigurations",
	"key":		"Topic",
	"filterid":	"Topic"
}

aws_s3_bucket_object = {
	"clfn":		"s3",
	"descfn":	"get_object",
	"topkey":	"Body",
	"key":		"Body",
	"filterid":	"Body"
}

aws_s3_bucket_object_lock_configuration = {
	"clfn":		"s3",
	"descfn":	"get_object_lock_configuration",
	"topkey":	"ObjectLockConfiguration",
	"key":		"ObjectLockEnabled",
	"filterid":	"ObjectLockEnabled"
}




aws_s3_bucket_ownership_controls = {
	"clfn":		"s3",
	"descfn":	"get_bucket_ownership_controls",
	"topkey":	"OwnershipControls",
	"key":		"Rules",
	"filterid":	"Rules"
}

aws_s3_bucket_policy = {
	"clfn":		"s3",
	"descfn":	"get_bucket_policy",
	"topkey":	"Policy",
	"key":		"Policy",
	"filterid":	"Policy"
}

aws_s3_bucket_public_access_block = {
	"clfn":		"s3",
	"descfn":	"get_public_access_block",
	"topkey":	"PublicAccessBlockConfiguration",
	"key":		"BlockPublicAcls",
	"filterid":	"BlockPublicAcls"
}

aws_s3_bucket_replication_configuration = {
	"clfn":		"s3",
	"descfn":	"get_bucket_replication",
	"topkey":	"ReplicationConfiguration",
	"key":		"Role",
	"filterid":	"Role"
}

aws_s3_bucket_request_payment_configuration = {
	"clfn":		"s3",
	"descfn":	"get_bucket_request_payment",
	"topkey":	"Payer",
	"key":		"Payer",
	"filterid":	"Payer"
}

aws_s3_bucket_server_side_encryption_configuration = {
	"clfn":		"s3",
	"descfn":	"get_bucket_server_side_encryption_configuration",
	"topkey":	"Rules",
	"key":		"ApplyServerSideEncryptionByDefault.SSEAlgorithm",
	"filterid":	"ApplyServerSideEncryptionByDefault.SSEAlgorithm"
}

aws_s3_bucket_versioning = {
	"clfn":		"s3",
	"descfn":	"get_bucket_versioning",
	"topkey":	"Status",
	"key":		"Status",
	"filterid":	"Status"
}

aws_s3_bucket_website_configuration = {
	"clfn":		"s3",
	"descfn":	"get_bucket_website",
	"topkey":	"ErrorDocument",
	"key":		"Key",
	"filterid":	"Key"
}

aws_s3_directory_bucket = {
	"clfn":		"s3",
	"descfn":	"list_buckets",
	"topkey":	"Buckets",
	"key":		"Name",
	"filterid":	"Name"
}

aws_s3_object = {
	"clfn":		"s3",
	"descfn":	"get_object",
	"topkey":	"Body",
	"key":		"Body",
	"filterid":	"Body"
}

aws_s3_object_copy = {
	"clfn":		"s3",
	"descfn":	"get_object",
	"topkey":	"Body",
	"key":		"Body",
	"filterid":	"Body"
}

aws_s3control_access_grant = {
	"clfn":		"s3control",
	"descfn":	"list_access_grants",
	"topkey":	"AccessGrants",
	"key":		"Grantee.DisplayName",
	"filterid":	"Grantee.DisplayName"
}

aws_s3control_access_grants_instance = {
	"clfn":		"s3control",
	"descfn":	"list_access_grants",
	"topkey":	"AccessGrants",
	"key":		"Grantee.DisplayName",
	"filterid":	"Grantee.DisplayName"
}

aws_s3control_access_grants_instance_resource_policy = {
	"clfn":		"s3control",
	"descfn":	"list_access_grants",
	"topkey":	"AccessGrants",
	"key":		"Grantee.DisplayName",
	"filterid":	"Grantee.DisplayName"
}

aws_s3control_access_grants_location = {
	"clfn":		"s3control",
	"descfn":	"list_access_grants",
	"topkey":	"AccessGrants",
	"key":		"Grantee.DisplayName",
	"filterid":	"Grantee.DisplayName"
}

aws_s3control_access_point_policy = {
	"clfn":		"s3control",
	"descfn":	"get_access_point_policy",
	"topkey":	"Policy",
	"key":		"Policy",
	"filterid":	"Policy"
}

aws_s3control_bucket = {
	"clfn":		"s3control",
	"descfn":	"list_buckets",
	"topkey":	"Buckets",
	"key":		"Name",
	"filterid":	"Name"
}

aws_s3control_bucket_lifecycle_configuration = {
	"clfn":		"s3control",
	"descfn":	"get_bucket_lifecycle_configuration",
	"topkey":	"Rules",
	"key":		"ID",
	"filterid":	"ID"
}

aws_s3control_bucket_policy = {
	"clfn":		"s3control",
	"descfn":	"get_bucket_policy",
	"topkey":	"Policy",
	"key":		"Policy",
	"filterid":	"Policy"
}

aws_s3control_multi_region_access_point = {
	"clfn":		"s3control",
	"descfn":	"list_access_points",
	"topkey":	"AccessPoints",
	"key":		"Name",
	"filterid":	"Name"
}

aws_s3control_multi_region_access_point_policy = {
	"clfn":		"s3control",
	"descfn":	"list_access_points",
	"topkey":	"AccessPoints",
	"key":		"Name",
	"filterid":	"Name"
}

aws_s3control_object_lambda_access_point = {
	"clfn":		"s3control",
	"descfn":	"list_access_points",
	"topkey":	"AccessPoints",
	"key":		"Name",
	"filterid":	"Name"
}

aws_s3control_object_lambda_access_point_policy = {
	"clfn":		"s3control",
	"descfn":	"list_access_points",
	"topkey":	"AccessPoints",
	"key":		"Name",
	"filterid":	"Name"
}

aws_s3control_storage_lens_configuration = {
	"clfn":		"s3control",
	"descfn":	"get_storage_lens_configuration",
	"topkey":	"StorageLensConfiguration",
	"key":		"Id",
	"filterid":	"Id"
}

aws_s3outposts_endpoint = {
	"clfn":		"s3outposts",
	"descfn":	"list_endpoints",
	"topkey":	"Endpoints",
	"key":		"EndpointArn",
	"filterid":	"EndpointArn"
}

aws_sagemaker_app = {
	"clfn":		"sagemaker",
	"descfn":	"list_apps",
	"topkey":	"Apps",
	"key":		"AppArn",
	"filterid":	"AppArn"
}

aws_sagemaker_app_image_config = {
	"clfn":		"sagemaker",
	"descfn":	"list_app_image_configs",
	"topkey":	"AppImageConfigs",
	"key":		"AppImageConfigArn",
	"filterid":	"AppImageConfigArn"
}

aws_sagemaker_code_repository = {
	"clfn":		"sagemaker",
	"descfn":	"list_code_repositories",
	"topkey":	"CodeRepositories",
	"key":		"CodeRepositoryArn",
	"filterid":	"CodeRepositoryArn"
}

aws_sagemaker_data_quality_job_definition = {
	"clfn":		"sagemaker",
	"descfn":	"list_data_quality_job_definitions",
	"topkey":	"DataQualityJobDefinitions",
	"key":		"DataQualityJobDefinitionArn",
	"filterid":	"DataQualityJobDefinitionArn"
}

aws_sagemaker_device = {
	"clfn":		"sagemaker",
	"descfn":	"list_devices",
	"topkey":	"Devices",
	"key":		"DeviceArn",
	"filterid":	"DeviceArn"
}

aws_sagemaker_device_fleet = {
	"clfn":		"sagemaker",
	"descfn":	"list_device_fleets",
	"topkey":	"DeviceFleets",
	"key":		"DeviceFleetArn",
	"filterid":	"DeviceFleetArn"
}

aws_sagemaker_domain = {
	"clfn":		"sagemaker",
	"descfn":	"list_domains",
	"topkey":	"Domains",
	"key":		"DomainArn",
	"filterid":	"DomainArn"
}

aws_sagemaker_endpoint = {
	"clfn":		"sagemaker",
	"descfn":	"list_endpoints",
	"topkey":	"Endpoints",
	"key":		"EndpointArn",
	"filterid":	"EndpointArn"
}

aws_sagemaker_endpoint_configuration = {
	"clfn":		"sagemaker",
	"descfn":	"list_endpoint_configurations",
	"topkey":	"EndpointConfigurations",
	"key":		"EndpointConfigurationArn",
	"filterid":	"EndpointConfigurationArn"
}

aws_sagemaker_feature_group = {
	"clfn":		"sagemaker",
	"descfn":	"list_feature_groups",
	"topkey":	"FeatureGroups",
	"key":		"FeatureGroupArn",
	"filterid":	"FeatureGroupArn"
}

aws_sagemaker_flow_definition = {
	"clfn":		"sagemaker",
	"descfn":	"list_flow_definitions",
	"topkey":	"FlowDefinitions",
	"key":		"FlowDefinitionArn",
	"filterid":	"FlowDefinitionArn"
}

aws_sagemaker_human_task_ui = {
	"clfn":		"sagemaker",
	"descfn":	"list_human_task_uis",
	"topkey":	"HumanTaskUIs",
	"key":		"HumanTaskUiArn",
	"filterid":	"HumanTaskUiArn"
}

aws_sagemaker_image = {
	"clfn":		"sagemaker",
	"descfn":	"list_images",
	"topkey":	"Images",
	"key":		"ImageArn",
	"filterid":	"ImageArn"
}

aws_sagemaker_image_version = {
	"clfn":		"sagemaker",
	"descfn":	"list_image_versions",
	"topkey":	"ImageVersions",
	"key":		"ImageVersionArn",
	"filterid":	"ImageVersionArn"
}

aws_sagemaker_model = {
	"clfn":		"sagemaker",
	"descfn":	"list_models",
	"topkey":	"Models",
	"key":		"ModelArn",
	"filterid":	"ModelArn"
}

aws_sagemaker_model_package_group = {
	"clfn":		"sagemaker",
	"descfn":	"list_model_package_groups",
	"topkey":	"ModelPackageGroups",
	"key":		"ModelPackageGroupArn",
	"filterid":	"ModelPackageGroupArn"
}

aws_sagemaker_model_package_group_policy = {
	"clfn":		"sagemaker",
	"descfn":	"get_model_package_group_policy",
	"topkey":	"Policy",
	"key":		"Policy",
	"filterid":	"Policy"
}

aws_sagemaker_monitoring_schedule = {
	"clfn":		"sagemaker",
	"descfn":	"list_monitoring_schedules",
	"topkey":	"MonitoringSchedules",
	"key":		"MonitoringScheduleArn",
	"filterid":	"MonitoringScheduleArn"
}

aws_sagemaker_notebook_instance = {
	"clfn":		"sagemaker",
	"descfn":	"list_notebook_instances",
	"topkey":	"NotebookInstances",
	"key":		"NotebookInstanceArn",
	"filterid":	"NotebookInstanceArn"
}

aws_sagemaker_notebook_instance_lifecycle_configuration = {
	"clfn":		"sagemaker",
	"descfn":	"list_notebook_instance_lifecycle_configs",
	"topkey":	"NotebookInstanceLifecycleConfigs",
	"key":		"NotebookInstanceLifecycleConfigArn",
	"filterid":	"NotebookInstanceLifecycleConfigArn"
}

aws_sagemaker_pipeline = {
	"clfn":		"sagemaker",
	"descfn":	"list_pipelines",
	"topkey":	"Pipelines",
	"key":		"PipelineArn",
	"filterid":	"PipelineArn"
}

aws_sagemaker_project = {
	"clfn":		"sagemaker",
	"descfn":	"list_projects",
	"topkey":	"Projects",
	"key":		"ProjectArn",
	"filterid":	"ProjectArn"
}

aws_sagemaker_servicecatalog_portfolio_status = {
	"clfn":		"sagemaker",
	"descfn":	"get_service_catalog_portfolio_status",
	"topkey":	"Status",
	"key":		"Status",
	"filterid":	"Status"
}

aws_sagemaker_space = {
	"clfn":		"sagemaker",
	"descfn":	"list_spaces",
	"topkey":	"Spaces",
	"key":		"SpaceArn",
	"filterid":	"SpaceArn"
}

aws_sagemaker_studio_lifecycle_config = {
	"clfn":		"sagemaker",
	"descfn":	"list_studio_lifecycle_configs",
	"topkey":	"StudioLifecycleConfigs",
	"key":		"StudioLifecycleConfigArn",
	"filterid":	"StudioLifecycleConfigArn"
}

aws_sagemaker_user_profile = {
	"clfn":		"sagemaker",
	"descfn":	"list_user_profiles",
	"topkey":	"UserProfiles",
	"key":		"UserProfileArn",
	"filterid":	"UserProfileArn"
}

aws_sagemaker_workforce = {
	"clfn":		"sagemaker",
	"descfn":	"list_workforces",
	"topkey":	"Workforces",
	"key":		"WorkforceArn",
	"filterid":	"WorkforceArn"
}

aws_sagemaker_workteam = {
	"clfn":		"sagemaker",
	"descfn":	"list_workteams",
	"topkey":	"Workteams",
	"key":		"WorkteamArn",
	"filterid":	"WorkteamArn"
}

aws_scheduler_schedule = {
	"clfn":		"scheduler",
	"descfn":	"list_schedules",
	"topkey":	"Schedules",
	"key":		"ScheduleArn",
	"filterid":	"ScheduleArn"
}

aws_scheduler_schedule_group = {
	"clfn":		"scheduler",
	"descfn":	"list_schedule_groups",
	"topkey":	"ScheduleGroups",
	"key":		"ScheduleGroupArn",
	"filterid":	"ScheduleGroupArn"
}

aws_schemas_discoverer = {
	"clfn":		"schemas",
	"descfn":	"list_discoverers",
	"topkey":	"Discoverers",
	"key":		"DiscovererArn",
	"filterid":	"DiscovererArn"
}

aws_schemas_registry = {
	"clfn":		"schemas",
	"descfn":	"list_registries",
	"topkey":	"Registries",
	"key":		"RegistryArn",
	"filterid":	"RegistryArn"
}

aws_schemas_registry_policy = {
	"clfn":		"schemas",
	"descfn":	"get_registry_policy",
	"topkey":	"Policy",
	"key":		"Policy",
	"filterid":	"Policy"
}

aws_schemas_schema = {
	"clfn":		"schemas",
	"descfn":	"list_schemas",
	"topkey":	"Schemas",
	"key":		"SchemaArn",
	"filterid":	"SchemaArn"
}


aws_secretsmanager_secret_policy = {
	"clfn":		"secretsmanager",
	"descfn":	"get_secret_policy",
	"topkey":	"Policy",
	"key":		"Policy",
	"filterid":	"Policy"
}

aws_secretsmanager_secret_rotation = {
	"clfn":		"secretsmanager",
	"descfn":	"get_secret_rotation",
	"topkey":	"Rotation",
	"key":		"Rotation",
	"filterid":	"Rotation"
}

aws_secretsmanager_secret_version = {
	"clfn":		"secretsmanager",
	"descfn":	"list_secret_version_ids",
	"topkey":	"SecretVersions",
	"key":		"SecretVersionId",
	"filterid":	"SecretVersionId"
}

aws_security_group_rule = {
	"clfn":		"ec2",
	"descfn":	"describe_security_group_rules",
	"topkey":	"SecurityGroupRules",
	"key":		"RuleId",
	"filterid":	"RuleId"
}

aws_securityhub_account = {
	"clfn":		"securityhub",
	"descfn":	"describe_hub",
	"topkey":	"Hub",
	"key":		"HubArn",
	"filterid":	"HubArn"
}

aws_securityhub_action_target = {
	"clfn":		"securityhub",
	"descfn":	"describe_action_targets",
	"topkey":	"ActionTargets",
	"key":		"ActionTargetArn",
	"filterid":	"ActionTargetArn"
}

aws_securityhub_finding_aggregator = {
	"clfn":		"securityhub",
	"descfn":	"describe_finding_aggregators",
	"topkey":	"FindingAggregators",
	"key":		"FindingAggregatorArn",
	"filterid":	"FindingAggregatorArn"
}

aws_securityhub_insight = {
	"clfn":		"securityhub",
	"descfn":	"describe_insights",
	"topkey":	"Insights",
	"key":		"InsightArn",
	"filterid":	"InsightArn"
}

aws_securityhub_invite_accepter = {
	"clfn":		"securityhub",
	"descfn":	"describe_invite_accepters",
	"topkey":	"InviteAccepters",
	"key":		"InviteAccepterArn",
	"filterid":	"InviteAccepterArn"
}

aws_securityhub_member = {
	"clfn":		"securityhub",
	"descfn":	"describe_members",
	"topkey":	"Members",
	"key":		"MemberArn",
	"filterid":	"MemberArn"
}

aws_securityhub_organization_admin_account = {
	"clfn":		"securityhub",
	"descfn":	"describe_organization_admin_account",
	"topkey":	"AdminAccount",
	"key":		"AdminAccount",
	"filterid":	"AdminAccount"
}

aws_securityhub_organization_configuration = {
	"clfn":		"securityhub",
	"descfn":	"describe_organization_configuration",
	"topkey":	"OrganizationConfiguration",
	"key":		"OrganizationConfiguration",
	"filterid":	"OrganizationConfiguration"
}

aws_securityhub_product_subscription = {
	"clfn":		"securityhub",
	"descfn":	"describe_product_subscriptions",
	"topkey":	"ProductSubscriptions",
	"key":		"ProductSubscriptionArn",
	"filterid":	"ProductSubscriptionArn"
}

aws_securityhub_standards_control = {
	"clfn":		"securityhub",
	"descfn":	"describe_standards_controls",
	"topkey":	"StandardsControls",
	"key":		"StandardsControlArn",
	"filterid":	"StandardsControlArn"
}

aws_securityhub_standards_subscription = {
	"clfn":		"securityhub",
	"descfn":	"describe_standards_subscriptions",
	"topkey":	"StandardsSubscriptions",
	"key":		"StandardsSubscriptionArn",
	"filterid":	"StandardsSubscriptionArn"
}

aws_securitylake_data_lake = {
	"clfn":		"securitylake",
	"descfn":	"describe_data_lakes",
	"topkey":	"DataLakes",
	"key":		"DataLakeArn",
	"filterid":	"DataLakeArn"
}


aws_serverlessapplicationrepository_cloudformation_stack = {
	"clfn":		"serverlessrepo",
	"descfn":	"list_application_versions",
	"topkey":	"ApplicationVersions",
	"key":		"ApplicationVersionId",
	"filterid":	"ApplicationVersionId"
}

aws_service_discovery_http_namespace = {
	"clfn":		"servicediscovery",
	"descfn":	"list_http_namespaces",
	"topkey":	"HttpNamespaces",
	"key":		"HttpNamespaceArn",
	"filterid":	"HttpNamespaceArn"
}

aws_service_discovery_instance = {
	"clfn":		"servicediscovery",
	"descfn":	"list_instances",
	"topkey":	"Instances",
	"key":		"InstanceId",
	"filterid":	"InstanceId"
}

aws_service_discovery_private_dns_namespace = {
	"clfn":		"servicediscovery",
	"descfn":	"list_private_dns_namespaces",
	"topkey":	"PrivateDnsNamespaces",
	"key":		"PrivateDnsNamespaceArn",
	"filterid":	"PrivateDnsNamespaceArn"
}

aws_service_discovery_public_dns_namespace = {
	"clfn":		"servicediscovery",
	"descfn":	"list_public_dns_namespaces",
	"topkey":	"PublicDnsNamespaces",
	"key":		"PublicDnsNamespaceArn",
	"filterid":	"PublicDnsNamespaceArn"
}

aws_service_discovery_service = {
	"clfn":		"servicediscovery",
	"descfn":	"list_services",
	"topkey":	"Services",
	"key":		"ServiceArn",
	"filterid":	"ServiceArn"
}

aws_servicecatalog_budget_resource_association = {
	"clfn":		"servicecatalog",
	"descfn":	"list_budget_resource_associations",
	"topkey":	"BudgetResourceAssociations",
	"key":		"BudgetResourceAssociationId",
	"filterid":	"BudgetResourceAssociationId"
}

aws_servicecatalog_constraint = {
	"clfn":		"servicecatalog",
	"descfn":	"list_constraints",
	"topkey":	"Constraints",
	"key":		"ConstraintId",
	"filterid":	"ConstraintId"
}


aws_servicecatalog_organizations_access = {
	"clfn":		"servicecatalog",
	"descfn":	"list_organization_access",
	"topkey":	"OrganizationAccess",
	"key":		"Id",
	"filterid":	"Id"
}

aws_servicecatalog_portfolio = {
	"clfn":		"servicecatalog",
	"descfn":	"list_portfolios",
	"topkey":	"Portfolios",
	"key":		"Id",
	"filterid":	"Id"
}

aws_servicecatalog_portfolio_share = {
	"clfn":		"servicecatalog",
	"descfn":	"list_portfolio_shares",
	"topkey":	"PortfolioShares",
	"key":		"Id",
	"filterid":	"Id"
}

aws_servicecatalog_principal_portfolio_association = {
	"clfn":		"servicecatalog",
	"descfn":	"list_principal_portfolio_associations",
	"topkey":	"PrincipalPortfolioAssociations",
	"key":		"Id",
	"filterid":	"Id"
}

aws_servicecatalog_product = {
	"clfn":		"servicecatalog",
	"descfn":	"list_products",
	"topkey":	"Products",
	"key":		"Id",
	"filterid":	"Id"
}

aws_servicecatalog_product_portfolio_association = {
	"clfn":		"servicecatalog",
	"descfn":	"list_product_portfolio_associations",
	"topkey":	"ProductPortfolioAssociations",
	"key":		"Id",
	"filterid":	"Id"
}

aws_servicecatalog_provisioned_product = {
	"clfn":		"servicecatalog",
	"descfn":	"list_provisioned_products",
	"topkey":	"ProvisionedProducts",
	"key":		"Id",
	"filterid":	"Id"
}

aws_servicecatalog_provisioning_artifact = {
	"clfn":		"servicecatalog",
	"descfn":	"list_provisioning_artifacts",
	"topkey":	"ProvisioningArtifacts",
	"key":		"Id",
	"filterid":	"Id"
}


aws_servicecatalog_service_action = {
	"clfn":		"servicecatalog",
	"descfn":	"list_service_actions",
	"topkey":	"ServiceActions",
	"key":		"Id",
	"filterid":	"Id"
}

aws_servicecatalog_tag_option = {
	"clfn":		"servicecatalog",
	"descfn":	"list_tag_options",
	"topkey":	"TagOptions",
	"key":		"Id",
	"filterid":	"Id"
}

aws_servicecatalog_tag_option_resource_association = {
	"clfn":		"servicecatalog",
	"descfn":	"list_tag_option_resource_associations",
	"topkey":	"TagOptionResourceAssociations",
	"key":		"Id",
	"filterid":	"Id"
}

aws_servicequotas_service_quota = {
	"clfn":		"service-quotas",
	"descfn":	"list_service_quotas",
	"topkey":	"Quotas",
	"key":		"QuotaCode",
	"filterid":	"QuotaCode"
}

aws_servicequotas_template = {
	"clfn":		"service-quotas",
	"descfn":	"list_templates",
	"topkey":	"Templates",
	"key":		"TemplateId",
	"filterid":	"TemplateId"
}

aws_servicequotas_template_association = {
	"clfn":		"service-quotas",
	"descfn":	"list_template_associations",
	"topkey":	"TemplateAssociations",
	"key":		"TemplateAssociationId",
	"filterid":	"TemplateAssociationId"
}

aws_ses_active_receipt_rule_set = {
	"clfn":		"ses",
	"descfn":	"describe_active_receipt_rule_set",
	"topkey":	"Metadata",
	"key":		"Name",
	"filterid":	"Name"
}

aws_ses_configuration_set = {
	"clfn":		"ses",
	"descfn":	"describe_configuration_sets",
	"topkey":	"ConfigurationSets",
	"key":		"Name",
	"filterid":	"Name"
}

aws_ses_domain_dkim = {
	"clfn":		"ses",
	"descfn":	"describe_domain_dkim",
	"topkey":	"DkimAttributes",
	"key":		"DkimTokens",
	"filterid":	"DkimTokens"
}

aws_ses_domain_identity = {
	"clfn":		"ses",
	"descfn":	"describe_domain_identity",
	"topkey":	"DomainIdentities",
	"key":		"DomainIdentity",
	"filterid":	"DomainIdentity"
}

aws_ses_domain_identity_verification = {
	"clfn":		"ses",
	"descfn":	"describe_domain_identity_verification",
	"topkey":	"VerificationToken",
	"key":		"VerificationToken",
	"filterid":	"VerificationToken"
}

aws_ses_domain_mail_from = {
	"clfn":		"ses",
	"descfn":	"describe_domain_mail_from",
	"topkey":	"MailFromAttributes",
	"key":		"MailFromDomain",
	"filterid":	"MailFromDomain"
}

aws_ses_email_identity = {
	"clfn":		"ses",
	"descfn":	"describe_email_identity",
	"topkey":	"IdentityType",
	"key":		"IdentityType",
	"filterid":	"IdentityType"
}

aws_ses_event_destination = {
	"clfn":		"ses",
	"descfn":	"describe_event_destination",
	"topkey":	"EventDestination",
	"key":		"EventDestination",
	"filterid":	"EventDestination"
}

aws_ses_identity_notification_topic = {
	"clfn":		"ses",
	"descfn":	"describe_identity_notification_topic",
	"topkey":	"Identity",
	"key":		"Identity",
	"filterid":	"Identity"
}

aws_ses_identity_policy = {
	"clfn":		"ses",
	"descfn":	"describe_identity_policy",
	"topkey":	"Policy",
	"key":		"Policy",
	"filterid":	"Policy"
}

aws_ses_receipt_filter = {
	"clfn":		"ses",
	"descfn":	"describe_receipt_filter",
	"topkey":	"Filter",
	"key":		"Filter",
	"filterid":	"Filter"
}

aws_ses_receipt_rule = {
	"clfn":		"ses",
	"descfn":	"describe_receipt_rule",
	"topkey":	"Rule",
	"key":		"Rule",
	"filterid":	"Rule"
}

aws_ses_receipt_rule_set = {
	"clfn":		"ses",
	"descfn":	"describe_receipt_rule_set",
	"topkey":	"Metadata",
	"key":		"Name",
	"filterid":	"Name"
}

aws_ses_template = {
	"clfn":		"ses",
	"descfn":	"describe_template",
	"topkey":	"Template",
	"key":		"Template",
	"filterid":	"Template"
}

aws_sesv2_account_vdm_attributes = {
	"clfn":		"sesv2",
	"descfn":	"describe_account_vdm_attributes",
	"topkey":	"AccountVdmAttributes",
	"key":		"AccountVdmAttributes",
	"filterid":	"AccountVdmAttributes"
}

aws_sesv2_configuration_set = {
	"clfn":		"sesv2",
	"descfn":	"describe_configuration_set",
	"topkey":	"ConfigurationSet",
	"key":		"ConfigurationSet",
	"filterid":	"ConfigurationSet"
}

aws_sesv2_configuration_set_event_destination = {
	"clfn":		"sesv2",
	"descfn":	"describe_configuration_set_event_destination",
	"topkey":	"EventDestination",
	"key":		"EventDestination",
	"filterid":	"EventDestination"
}

aws_sesv2_contact_list = {
	"clfn":		"sesv2",
	"descfn":	"describe_contact_list",
	"topkey":	"ContactList",
	"key":		"ContactList",
	"filterid":	"ContactList"
}

aws_sesv2_dedicated_ip_assignment = {
	"clfn":		"sesv2",
	"descfn":	"describe_dedicated_ip_assignment",
	"topkey":	"DedicatedIpAssignment",
	"key":		"DedicatedIpAssignment",
	"filterid":	"DedicatedIpAssignment"
}

aws_sesv2_dedicated_ip_pool = {
	"clfn":		"sesv2",
	"descfn":	"describe_dedicated_ip_pool",
	"topkey":	"DedicatedIpPool",
	"key":		"DedicatedIpPool",
	"filterid":	"DedicatedIpPool"
}

aws_sesv2_email_identity = {
	"clfn":		"sesv2",
	"descfn":	"describe_email_identity",
	"topkey":	"EmailIdentity",
	"key":		"EmailIdentity",
	"filterid":	"EmailIdentity"
}

aws_sesv2_email_identity_feedback_attributes = {
	"clfn":		"sesv2",
	"descfn":	"describe_email_identity_feedback_attributes",
	"topkey":	"EmailIdentityFeedbackAttributes",
	"key":		"EmailIdentityFeedbackAttributes",
	"filterid":	"EmailIdentityFeedbackAttributes"
}

aws_sesv2_email_identity_mail_from_attributes = {
	"clfn":		"sesv2",
	"descfn":	"describe_email_identity_mail_from_attributes",
	"topkey":	"MailFromAttributes",
	"key":		"MailFromAttributes",
	"filterid":	"MailFromAttributes"
}

aws_sfn_activity = {
	"clfn":		"stepfunctions",
	"descfn":	"list_activities",
	"topkey":	"Activities",
	"key":		"ActivityArn",
	"filterid":	"ActivityArn"
}

aws_sfn_alias = {
	"clfn":		"stepfunctions",
	"descfn":	"list_aliases",
	"topkey":	"Aliases",
	"key":		"AliasArn",
	"filterid":	"AliasArn"
}

aws_sfn_state_machine = {
	"clfn":		"stepfunctions",
	"descfn":	"list_state_machines",
	"topkey":	"StateMachines",
	"key":		"StateMachineArn",
	"filterid":	"StateMachineArn"
}

aws_shield_application_layer_automatic_response = {
	"clfn":		"shield",
	"descfn":	"list_application_layer_automatic_response_associations",
	"topkey":	"ApplicationLayerAutomaticResponseAssociations",
	"key":		"Id",
	"filterid":	"Id"
}

aws_shield_drt_access_log_bucket_association = {
	"clfn":		"shield",
	"descfn":	"list_drt_access_log_bucket_associations",
	"topkey":	"DrtAccessLogBucketAssociations",
	"key":		"Id",
	"filterid":	"Id"
}

aws_shield_drt_access_role_arn_association = {
	"clfn":		"shield",
	"descfn":	"list_drt_access_role_arn_associations",
	"topkey":	"DrtAccessRoleArnAssociations",
	"key":		"Id",
	"filterid":	"Id"
}

aws_shield_protection = {
	"clfn":		"shield",
	"descfn":	"list_protections",
	"topkey":	"Protections",
	"key":		"Id",
	"filterid":	"Id"
}

aws_shield_protection_group = {
	"clfn":		"shield",
	"descfn":	"list_protection_groups",
	"topkey":	"ProtectionGroups",
	"key":		"Id",
	"filterid":	"Id"
}

aws_shield_protection_health_check_association = {
	"clfn":		"shield",
	"descfn":	"list_protection_health_check_associations",
	"topkey":	"ProtectionHealthCheckAssociations",
	"key":		"Id",
	"filterid":	"Id"
}

aws_signer_signing_job = {
	"clfn":		"signer",
	"descfn":	"list_signing_jobs",
	"topkey":	"Jobs",
	"key":		"JobId",
	"filterid":	"JobId"
}

aws_signer_signing_profile = {
	"clfn":		"signer",
	"descfn":	"list_signing_profiles",
	"topkey":	"Profiles",
	"key":		"ProfileName",
	"filterid":	"ProfileName"
}

aws_signer_signing_profile_permission = {
	"clfn":		"signer",
	"descfn":	"list_signing_profile_permissions",
	"topkey":	"Permissions",
	"key":		"ProfileName",
	"filterid":	"ProfileName"
}

aws_simpledb_domain = {
	"clfn":		"sdb",
	"descfn":	"list_domains",
	"topkey":	"DomainNames",
	"key":		"DomainName",
	"filterid":	"DomainName"
}

aws_snapshot_create_volume_permission = {
	"clfn":		"ec2",
	"descfn":	"describe_create_volume_permissions",
	"topkey":	"CreateVolumePermissions",
	"key":		"UserId",
	"filterid":	"UserId"
}

aws_sns_platform_application = {
	"clfn":		"sns",
	"descfn":	"list_platform_applications",
	"topkey":	"PlatformApplications",
	"key":		"PlatformApplicationArn",
	"filterid":	"PlatformApplicationArn"
}

aws_sns_sms_preferences = {
	"clfn":		"sns",
	"descfn":	"get_sms_preferences",
	"topkey":	"SMSPreferences",
	"key":		"SMSPreferences",
	"filterid":	"SMSPreferences"
}

aws_sns_topic = {
	"clfn":		"sns",
	"descfn":	"list_topics",
	"topkey":	"Topics",
	"key":		"TopicArn",
	"filterid":	"TopicArn"
}

aws_sns_topic_data_protection_policy = {
	"clfn":		"sns",
	"descfn":	"get_data_protection_policy",
	"topkey":	"DataProtectionPolicy",
	"key":		"DataProtectionPolicy",
	"filterid":	"DataProtectionPolicy"
}

aws_sns_topic_policy = {
	"clfn":		"sns",
	"descfn":	"get_topic_attributes",
	"topkey":	"Attributes",
	"key":		"Policy",
	"filterid":	"Policy"
}

aws_sns_topic_subscription = {
	"clfn":		"sns",
	"descfn":	"list_subscriptions_by_topic",
	"topkey":	"Subscriptions",
	"key":		"SubscriptionArn",
	"filterid":	"SubscriptionArn"
}

aws_spot_datafeed_subscription = {
	"clfn":		"ec2",
	"descfn":	"describe_spot_datafeed_subscription",
	"topkey":	"SpotDatafeedSubscription",
	"key":		"SpotDatafeedSubscription",
	"filterid":	"SpotDatafeedSubscription"
}

aws_spot_fleet_request = {
	"clfn":		"ec2",
	"descfn":	"describe_spot_fleet_requests",
	"topkey":	"SpotFleetRequestConfigs",
	"key":		"SpotFleetRequestId",
	"filterid":	"SpotFleetRequestId"
}

aws_spot_instance_request = {
	"clfn":		"ec2",
	"descfn":	"describe_spot_instance_requests",
	"topkey":	"SpotInstanceRequests",
	"key":		"SpotInstanceRequestId",
	"filterid":	"SpotInstanceRequestId"
}

aws_sqs_queue = {
	"clfn":		"sqs",
	"descfn":	"list_queues",
	"topkey":	"QueueUrls",
	"key":		"QueueUrl",
	"filterid":	"QueueUrl"
}

aws_sqs_queue_policy = {
	"clfn":		"sqs",
	"descfn":	"get_queue_attributes",
	"topkey":	"Attributes",
	"key":		"Policy",
	"filterid":	"Policy"
}

aws_sqs_queue_redrive_allow_policy = {
	"clfn":		"sqs",
	"descfn":	"get_queue_attributes",
	"topkey":	"Attributes",
	"key":		"RedrivePolicy",
	"filterid":	"RedrivePolicy"
}

aws_sqs_queue_redrive_policy = {
	"clfn":		"sqs",
	"descfn":	"get_queue_attributes",
	"topkey":	"Attributes",
	"key":		"RedrivePolicy",
	"filterid":	"RedrivePolicy"
}

aws_ssm_activation = {
	"clfn":		"ssm",
	"descfn":	"list_activations",
	"topkey":	"ActivationList",
	"key":		"ActivationId",
	"filterid":	"ActivationId"
}

aws_ssm_association = {
	"clfn":		"ssm",
	"descfn":	"list_associations",
	"topkey":	"AssociationList",
	"key":		"AssociationId",
	"filterid":	"AssociationId"
}

aws_ssm_default_patch_baseline = {
	"clfn":		"ssm",
	"descfn":	"get_default_patch_baseline",
	"topkey":	"Baseline",
	"key":		"BaselineId",
	"filterid":	"BaselineId"
}

aws_ssm_document = {
	"clfn":		"ssm",
	"descfn":	"list_documents",
	"topkey":	"DocumentIdentifiers",
	"key":		"Name",
	"filterid":	"Name"
}

aws_ssm_maintenance_window = {
	"clfn":		"ssm",
	"descfn":	"list_maintenance_windows",
	"topkey":	"WindowIdentities",
	"key":		"WindowId",
	"filterid":	"WindowId"
}

aws_ssm_maintenance_window_target = {
	"clfn":		"ssm",
	"descfn":	"list_targets_for_maintenance_window",
	"topkey":	"WindowTargetIds",
	"key":		"WindowTargetId",
	"filterid":	"WindowTargetId"
}

aws_ssm_maintenance_window_task = {
	"clfn":		"ssm",
	"descfn":	"list_tasks_for_maintenance_window",
	"topkey":	"TaskIds",
	"key":		"TaskId",
	"filterid":	"TaskId"
}


aws_ssm_parameter = {
	"clfn":		"ssm",
	"descfn":	"describe_parameters",
	"topkey":	"Parameters",
	"key":		"Name",
	"filterid":	"Name"
}

aws_ssm_patch_baseline = {
	"clfn":		"ssm",
	"descfn":	"list_patch_baselines",
	"topkey":	"BaselineIdentities",
	"key":		"BaselineId",
	"filterid":	"BaselineId"
}

aws_ssm_patch_group = {
	"clfn":		"ssm",
	"descfn":	"list_patch_groups",
	"topkey":	"PatchGroups",
	"key":		"PatchGroup",
	"filterid":	"PatchGroup"
}

aws_ssm_resource_data_sync = {
	"clfn":		"ssm",
	"descfn":	"list_resource_data_sync",
	"topkey":	"ResourceDataSyncItems",
	"key":		"SyncName",
	"filterid":	"SyncName"
}

aws_ssm_service_setting = {
	"clfn":		"ssm",
	"descfn":	"get_service_setting",
	"topkey":	"ServiceSetting",
	"key":		"SettingId",
	"filterid":	"SettingId"
}

aws_ssmcontacts_contact = {
	"clfn":		"ssm-contacts",
	"descfn":	"list_contacts",
	"topkey":	"Contacts",
	"key":		"Alias",
	"filterid":	"Alias"
}

aws_ssmcontacts_contact_channel = {
	"clfn":		"ssm-contacts",
	"descfn":	"list_contact_channels",
	"topkey":	"ContactChannels",
	"key":		"ChannelId",
	"filterid":	"ChannelId"
}

aws_ssmcontacts_plan = {
	"clfn":		"ssm-contacts",
	"descfn":	"list_plans",
	"topkey":	"Plans",
	"key":		"PlanId",
	"filterid":	"PlanId"
}

aws_ssmincidents_replication_set = {
	"clfn":		"ssm-incidents",
	"descfn":	"list_replication_sets",
	"topkey":	"ReplicationSets",
	"key":		"Arn",
	"filterid":	"Arn"
}

aws_ssmincidents_response_plan = {
	"clfn":		"ssm-incidents",
	"descfn":	"list_response_plans",
	"topkey":	"ResponsePlans",
	"key":		"Arn",
	"filterid":	"Arn"
}

aws_ssoadmin_account_assignment = {
	"clfn":		"sso-admin",
	"descfn":	"list_account_assignments",
	"topkey":	"AccountAssignments",
	"key":		"AccountAssignmentCreationTime",
	"filterid":	"AccountAssignmentCreationTime"
}

aws_ssoadmin_application = {
	"clfn":		"sso-admin",
	"descfn":	"list_applications",
	"topkey":	"Applications",
	"key":		"ApplicationId",
	"filterid":	"ApplicationId"
}

aws_ssoadmin_application_assignment = {
	"clfn":		"sso-admin",
	"descfn":	"list_application_assignments",
	"topkey":	"ApplicationAssignments",
	"key":		"AccountAssignmentCreationTime",
	"filterid":	"AccountAssignmentCreationTime"
}

aws_ssoadmin_application_assignment_configuration = {
	"clfn":		"sso-admin",
	"descfn":	"list_application_assignment_configurations",
	"topkey":	"ApplicationAssignmentConfigurations",
	"key":		"AccountAssignmentCreationTime",
	"filterid":	"AccountAssignmentCreationTime"
}

aws_ssoadmin_customer_managed_policy_attachment = {
	"clfn":		"sso-admin",
	"descfn":	"list_customer_managed_policy_attachments",
	"topkey":	"CustomerManagedPolicyAttachments",
	"key":		"AccountAssignmentCreationTime",
	"filterid":	"AccountAssignmentCreationTime"
}

aws_ssoadmin_instance_access_control_attributes = {
	"clfn":		"sso-admin",
	"descfn":	"list_instance_access_control_attribute_configuration",
	"topkey":	"InstanceAccessControlAttributeConfiguration",
	"key":		"AccountAssignmentCreationTime",
	"filterid":	"AccountAssignmentCreationTime"
}

aws_ssoadmin_managed_policy_attachment = {
	"clfn":		"sso-admin",
	"descfn":	"list_managed_policy_attachments",
	"topkey":	"ManagedPolicyAttachments",
	"key":		"AccountAssignmentCreationTime",
	"filterid":	"AccountAssignmentCreationTime"
}

aws_ssoadmin_permission_set = {
	"clfn":		"sso-admin",
	"descfn":	"list_permission_sets",
	"topkey":	"PermissionSets",
	"key":		"PermissionSetArn",
	"filterid":	"PermissionSetArn"
}

aws_ssoadmin_permission_set_inline_policy = {
	"clfn":		"sso-admin",
	"descfn":	"list_permission_set_inline_policies",
	"topkey":	"PermissionSetInlinePolicies",
	"key":		"PermissionSetArn",
	"filterid":	"PermissionSetArn"
}

aws_ssoadmin_permissions_boundary_attachment = {
	"clfn":		"sso-admin",
	"descfn":	"list_permissions_boundary_attachments",
	"topkey":	"PermissionsBoundaryAttachments",
	"key":		"AccountAssignmentCreationTime",
	"filterid":	"AccountAssignmentCreationTime"
}

aws_ssoadmin_trusted_token_issuer = {
	"clfn":		"sso-admin",
	"descfn":	"list_trusted_token_issuers",
	"topkey":	"TrustedTokenIssuers",
	"key":		"TrustedTokenIssuerId",
	"filterid":	"TrustedTokenIssuerId"
}

aws_storagegateway_cache = {
	"clfn":		"storagegateway",
	"descfn":	"describe_cache",
	"topkey":	"Cache",
	"key":		"CacheId",
	"filterid":	"CacheId"
}

aws_storagegateway_cached_iscsi_volume = {
	"clfn":		"storagegateway",
	"descfn":	"describe_cached_iscsi_volumes",
	"topkey":	"CachediSCSIVolumes",
	"key":		"VolumeARN",
	"filterid":	"VolumeARN"
}

aws_storagegateway_file_system_association = {
	"clfn":		"storagegateway",
	"descfn":	"describe_file_system_associations",
	"topkey":	"FileSystemAssociations",
	"key":		"FileSystemAssociationARN",
	"filterid":	"FileSystemAssociationARN"
}

aws_storagegateway_gateway = {
	"clfn":		"storagegateway",
	"descfn":	"describe_gateways",
	"topkey":	"Gateways",
	"key":		"GatewayARN",
	"filterid":	"GatewayARN"
}

aws_storagegateway_nfs_file_share = {
	"clfn":		"storagegateway",
	"descfn":	"describe_nfs_file_shares",
	"topkey":	"NFSFileShares",
	"key":		"NFSFileShareARN",
	"filterid":	"NFSFileShareARN"
}

aws_storagegateway_smb_file_share = {
	"clfn":		"storagegateway",
	"descfn":	"describe_smb_file_shares",
	"topkey":	"SMBFileShares",
	"key":		"SMBFileShareARN",
	"filterid":	"SMBFileShareARN"
}

aws_storagegateway_stored_iscsi_volume = {
	"clfn":		"storagegateway",
	"descfn":	"describe_stored_iscsi_volumes",
	"topkey":	"StorediSCSIVolumes",
	"key":		"VolumeARN",
	"filterid":	"VolumeARN"
}

aws_storagegateway_tape_pool = {
	"clfn":		"storagegateway",
	"descfn":	"describe_tape_pools",
	"topkey":	"TapePools",
	"key":		"PoolARN",
	"filterid":	"PoolARN"
}

aws_storagegateway_upload_buffer = {
	"clfn":		"storagegateway",
	"descfn":	"describe_upload_buffer",
	"topkey":	"UploadBuffer",
	"key":		"UploadBufferARN",
	"filterid":	"UploadBufferARN"
}

aws_storagegateway_working_storage = {
	"clfn":		"storagegateway",
	"descfn":	"describe_working_storage",
	"topkey":	"WorkingStorage",
	"key":		"WorkingStorageARN",
	"filterid":	"WorkingStorageARN"
}

aws_swf_domain = {
	"clfn":		"swf",
	"descfn":	"list_domains",
	"topkey":	"domainInfos",
	"key":		"name",
	"filterid":	"name"
}

aws_synthetics_canary = {
	"clfn":		"synthetics",
	"descfn":	"list_canaries",
	"topkey":	"Canaries",
	"key":		"Name",
	"filterid":	"Name"
}

aws_synthetics_group = {
	"clfn":		"synthetics",
	"descfn":	"list_canary_groups",
	"topkey":	"Groups",
	"key":		"Name",
	"filterid":	"Name"
}

aws_synthetics_group_association = {
	"clfn":		"synthetics",
	"descfn":	"list_group_associations",
	"topkey":	"GroupAssociations",
	"key":		"Name",
	"filterid":	"Name"
}

aws_timestreamwrite_database = {
	"clfn":		"timestream-write",
	"descfn":	"list_databases",
	"topkey":	"Databases",
	"key":		"DatabaseName",
	"filterid":	"DatabaseName"
}

aws_timestreamwrite_table = {
	"clfn":		"timestream-write",
	"descfn":	"list_tables",
	"topkey":	"Tables",
	"key":		"TableName",
	"filterid":	"TableName"
}

aws_transcribe_language_model = {
	"clfn":		"transcribe",
	"descfn":	"list_language_models",
	"topkey":	"LanguageModels",
	"key":		"LanguageCode",
	"filterid":	"LanguageCode"
}

aws_transcribe_medical_vocabulary = {
	"clfn":		"transcribe",
	"descfn":	"list_medical_vocabularies",
	"topkey":	"Vocabularies",
	"key":		"VocabularyName",
	"filterid":	"VocabularyName"
}

aws_transcribe_vocabulary = {
	"clfn":		"transcribe",
	"descfn":	"list_vocabularies",
	"topkey":	"Vocabularies",
	"key":		"VocabularyName",
	"filterid":	"VocabularyName"
}

aws_transcribe_vocabulary_filter = {
	"clfn":		"transcribe",
	"descfn":	"list_vocabulary_filters",
	"topkey":	"VocabularyFilters",
	"key":		"VocabularyFilterName",
	"filterid":	"VocabularyFilterName"
}

aws_transfer_access = {
	"clfn":		"transfer",
	"descfn":	"list_accesses",
	"topkey":	"Accesses",
	"key":		"AccessId",
	"filterid":	"AccessId"
}

aws_transfer_agreement = {
	"clfn":		"transfer",
	"descfn":	"list_agreements",
	"topkey":	"Agreements",
	"key":		"Arn",
	"filterid":	"Arn"
}

aws_transfer_certificate = {
	"clfn":		"transfer",
	"descfn":	"list_certificates",
	"topkey":	"Certificates",
	"key":		"Arn",
	"filterid":	"Arn"
}

aws_transfer_connector = {
	"clfn":		"transfer",
	"descfn":	"list_connectors",
	"topkey":	"Connectors",
	"key":		"Arn",
	"filterid":	"Arn"
}

aws_transfer_profile = {
	"clfn":		"transfer",
	"descfn":	"list_profiles",
	"topkey":	"Profiles",
	"key":		"Arn",
	"filterid":	"Arn"
}

aws_transfer_server = {
	"clfn":		"transfer",
	"descfn":	"list_servers",
	"topkey":	"Servers",
	"key":		"Arn",
	"filterid":	"Arn"
}

aws_transfer_ssh_key = {
	"clfn":		"transfer",
	"descfn":	"list_ssh_public_keys",
	"topkey":	"SshPublicKeys",
	"key":		"Arn",
	"filterid":	"Arn"
}

aws_transfer_tag = {
	"clfn":		"transfer",
	"descfn":	"list_tags",
	"topkey":	"Tags",
	"key":		"Key",
	"filterid":	"Key"
}

aws_transfer_user = {
	"clfn":		"transfer",
	"descfn":	"list_users",
	"topkey":	"Users",
	"key":		"Arn",
	"filterid":	"Arn"
}

aws_transfer_workflow = {
	"clfn":		"transfer",
	"descfn":	"list_workflows",
	"topkey":	"Workflows",
	"key":		"Arn",
	"filterid":	"Arn"
}

aws_verifiedaccess_endpoint = {
	"clfn":		"ec2",
	"descfn":	"list_endpoints",
	"topkey":	"Endpoints",
	"key":		"EndpointId",
	"filterid":	"EndpointId"
}

aws_verifiedaccess_group = {
	"clfn":		"ec2",
	"descfn":	"list_groups",
	"topkey":	"Groups",
	"key":		"GroupId",
	"filterid":	"GroupId"
}

aws_verifiedaccess_instance = {
	"clfn":		"ec2",
	"descfn":	"list_instances",
	"topkey":	"Instances",
	"key":		"InstanceId",
	"filterid":	"InstanceId"
}

aws_verifiedaccess_instance_logging_configuration = {
	"clfn":		"ec2",
	"descfn":	"list_instance_logging_configurations",
	"topkey":	"InstanceLoggingConfigurations",
	"key":		"InstanceId",
	"filterid":	"InstanceId"
}

aws_verifiedaccess_instance_trust_provider_attachment = {
	"clfn":		"ec2",
	"descfn":	"list_instance_trust_providers",
	"topkey":	"InstanceTrustProviders",
	"key":		"InstanceId",
	"filterid":	"InstanceId"
}

aws_verifiedaccess_trust_provider = {
	"clfn":		"ec2",
	"descfn":	"list_trust_providers",
	"topkey":	"TrustProviders",
	"key":		"TrustProviderId",
	"filterid":	"TrustProviderId"
}

aws_volume_attachment = {
	"clfn":		"ec2",
	"descfn":	"describe_volume_status",
	"topkey":	"VolumeStatuses",
	"key":		"VolumeId",
	"filterid":	"VolumeId"
}

aws_vpc_dhcp_options_association = {
	"clfn":		"ec2",
	"descfn":	"describe_dhcp_options_associations",
	"topkey":	"DhcpOptionsAssociations",
	"key":		"DhcpOptionsId",
	"filterid":	"DhcpOptionsId"
}

aws_vpc_endpoint_connection_accepter = {
	"clfn":		"ec2",
	"descfn":	"describe_vpc_endpoint_connection_accepters",
	"topkey":	"VpcEndpointConnectionAccepters",
	"key":		"VpcEndpointConnectionAccepterId",
	"filterid":	"VpcEndpointConnectionAccepterId"
}

aws_vpc_endpoint_connection_notification = {
	"clfn":		"ec2",
	"descfn":	"describe_vpc_endpoint_connection_notifications",
	"topkey":	"VpcEndpointConnectionNotifications",
	"key":		"VpcEndpointConnectionNotificationId",
	"filterid":	"VpcEndpointConnectionNotificationId"
}

aws_vpc_endpoint_policy = {
	"clfn":		"ec2",
	"descfn":	"describe_vpc_endpoint_service_policies",
	"topkey":	"Policies",
	"key":		"PolicyDocument",
	"filterid":	"PolicyDocument"
}

aws_vpc_endpoint_route_table_association = {
	"clfn":		"ec2",
	"descfn":	"describe_vpc_endpoint_route_table_associations",
	"topkey":	"RouteTableAssociations",
	"key":		"RouteTableAssociationId",
	"filterid":	"RouteTableAssociationId"
}

aws_vpc_endpoint_security_group_association = {
	"clfn":		"ec2",
	"descfn":	"describe_vpc_endpoint_security_group_associations",
	"topkey":	"SecurityGroupAssociations",
	"key":		"SecurityGroupId",
	"filterid":	"SecurityGroupId"
}

aws_vpc_endpoint_service = {
	"clfn":		"ec2",
	"descfn":	"describe_vpc_endpoint_services",
	"topkey":	"ServiceNames",
	"key":		"ServiceName",
	"filterid":	"ServiceName"
}

aws_vpc_endpoint_service_allowed_principal = {
	"clfn":		"ec2",
	"descfn":	"describe_vpc_endpoint_service_allowed_principals",
	"topkey":	"AllowedPrincipals",
	"key":		"Principal",
	"filterid":	"Principal"
}

aws_vpc_endpoint_subnet_association = {
	"clfn":		"ec2",
	"descfn":	"describe_vpc_endpoint_subnet_associations",
	"topkey":	"SubnetAssociations",
	"key":		"SubnetId",
	"filterid":	"SubnetId"
}

aws_vpc_ipam = {
	"clfn":		"ec2",
	"descfn":	"describe_ipams",
	"topkey":	"Ipams",
	"key":		"IpamId",
	"filterid":	"IpamId"
}

aws_vpc_ipam_organization_admin_account = {
	"clfn":		"ec2",
	"descfn":	"describe_ipam_organization_admin_accounts",
	"topkey":	"OrganizationAdminAccounts",
	"key":		"AccountId",
	"filterid":	"AccountId"
}

aws_vpc_ipam_pool = {
	"clfn":		"ec2",
	"descfn":	"describe_ipam_pools",
	"topkey":	"Pools",
	"key":		"PoolId",
	"filterid":	"PoolId"
}

aws_vpc_ipam_pool_cidr = {
	"clfn":		"ec2",
	"descfn":	"describe_ipam_pool_cidrs",
	"topkey":	"Cidrs",
	"key":		"Cidr",
	"filterid":	"Cidr"
}

aws_vpc_ipam_pool_cidr_allocation = {
	"clfn":		"ec2",
	"descfn":	"describe_ipam_pool_cidr_allocations",
	"topkey":	"Allocations",
	"key":		"AllocationId",
	"filterid":	"AllocationId"
}

aws_vpc_ipam_preview_next_cidr = {
	"clfn":		"ec2",
	"descfn":	"describe_ipam_preview_next_cidrs",
	"topkey":	"Cidrs",
	"key":		"Cidr",
	"filterid":	"Cidr"
}

aws_vpc_ipam_resource_discovery = {
	"clfn":		"ec2",
	"descfn":	"describe_ipam_resource_discoveries",
	"topkey":	"ResourceDiscoveries",
	"key":		"ResourceDiscoveryId",
	"filterid":	"ResourceDiscoveryId"
}

aws_vpc_ipam_resource_discovery_association = {
	"clfn":		"ec2",
	"descfn":	"describe_ipam_resource_discovery_associations",
	"topkey":	"ResourceDiscoveryAssociations",
	"key":		"ResourceDiscoveryAssociationId",
	"filterid":	"ResourceDiscoveryAssociationId"
}

aws_vpc_ipam_scope = {
	"clfn":		"ec2",
	"descfn":	"describe_ipam_scopes",
	"topkey":	"Scopes",
	"key":		"ScopeId",
	"filterid":	"ScopeId"
}

aws_vpc_ipv6_cidr_block_association = {
	"clfn":		"ec2",
	"descfn":	"describe_vpc_cidr_block_associations",
	"topkey":	"CidrBlockAssociations",
	"key":		"AssociationId",
	"filterid":	"AssociationId"
}

aws_vpc_network_performance_metric_subscription = {
	"clfn":		"ec2",
	"descfn":	"describe_network_insights_path_subscriptions",
	"topkey":	"NetworkInsightsPathSubscriptions",
	"key":		"NetworkInsightsPathSubscriptionId",
	"filterid":	"NetworkInsightsPathSubscriptionId"
}

aws_vpc_peering_connection = {
	"clfn":		"ec2",
	"descfn":	"describe_vpc_peering_connections",
	"topkey":	"VpcPeeringConnections",
	"key":		"VpcPeeringConnectionId",
	"filterid":	"VpcPeeringConnectionId"
}

aws_vpc_peering_connection_accepter = {
	"clfn":		"ec2",
	"descfn":	"describe_vpc_peering_connection_accepters",
	"topkey":	"VpcPeeringConnectionAccepters",
	"key":		"VpcPeeringConnectionId",
	"filterid":	"VpcPeeringConnectionId"
}

aws_vpc_peering_connection_options = {
	"clfn":		"ec2",
	"descfn":	"describe_vpc_peering_connection_options",
	"topkey":	"VpcPeeringConnectionOptions",
	"key":		"VpcPeeringConnectionId",
	"filterid":	"VpcPeeringConnectionId"
}

aws_vpc_security_group_egress_rule = {
	"clfn":		"ec2",
	"descfn":	"describe_security_group_rules",
	"topkey":	"SecurityGroupRules",
	"key":		"SecurityGroupRuleId",
	"filterid":	"SecurityGroupRuleId"
}

aws_vpc_security_group_ingress_rule = {
	"clfn":		"ec2",
	"descfn":	"describe_security_group_rules",
	"topkey":	"SecurityGroupRules",
	"key":		"SecurityGroupRuleId",
	"filterid":	"SecurityGroupRuleId"
}

aws_vpclattice_target_group_attachment = {
	"clfn":		"vpc-lattice",
	"descfn":	"list_target_group_attachments",
	"topkey":	"TargetGroupAttachments",
	"key":		"TargetGroupAttachmentId",
	"filterid":	"TargetGroupAttachmentId"
}

aws_vpn_connection = {
	"clfn":		"ec2",
	"descfn":	"describe_vpn_connections",
	"topkey":	"VpnConnections",
	"key":		"VpnConnectionId",
	"filterid":	"VpnConnectionId"
}

aws_vpn_connection_route = {
	"clfn":		"ec2",
	"descfn":	"describe_vpn_connection_routes",
	"topkey":	"VpnConnectionRoutes",
	"key":		"DestinationCidrBlock",
	"filterid":	"DestinationCidrBlock"
}

aws_vpn_gateway = {
	"clfn":		"ec2",
	"descfn":	"describe_vpn_gateways",
	"topkey":	"VpnGateways",
	"key":		"VpnGatewayId",
	"filterid":	"VpnGatewayId"
}

aws_vpn_gateway_attachment = {
	"clfn":		"ec2",
	"descfn":	"describe_vpn_gateway_attachments",
	"topkey":	"VpnGatewayAttachments",
	"key":		"VpnGatewayId",
	"filterid":	"VpnGatewayId"
}

aws_vpn_gateway_route_propagation = {
	"clfn":		"ec2",
	"descfn":	"describe_vpn_gateway_route_propagations",
	"topkey":	"VpnGatewayRoutePropagations",
	"key":		"VpnGatewayId",
	"filterid":	"VpnGatewayId"
}

aws_waf_byte_match_set = {
	"clfn":		"waf",
	"descfn":	"list_byte_match_sets",
	"topkey":	"ByteMatchSets",
	"key":		"ByteMatchSetId",
	"filterid":	"ByteMatchSetId"
}

aws_waf_geo_match_set = {
	"clfn":		"waf",
	"descfn":	"list_geo_match_sets",
	"topkey":	"GeoMatchSets",
	"key":		"GeoMatchSetId",
	"filterid":	"GeoMatchSetId"
}

aws_waf_ipset = {
	"clfn":		"waf",
	"descfn":	"list_ip_sets",
	"topkey":	"IPSets",
	"key":		"IPSetId",
	"filterid":	"IPSetId"
}

aws_waf_rate_based_rule = {
	"clfn":		"waf",
	"descfn":	"list_rate_based_rules",
	"topkey":	"RateBasedRules",
	"key":		"RuleId",
	"filterid":	"RuleId"
}

aws_waf_regex_match_set = {
	"clfn":		"waf",
	"descfn":	"list_regex_match_sets",
	"topkey":	"RegexMatchSets",
	"key":		"RegexMatchSetId",
	"filterid":	"RegexMatchSetId"
}

aws_waf_regex_pattern_set = {
	"clfn":		"waf",
	"descfn":	"list_regex_pattern_sets",
	"topkey":	"RegexPatternSets",
	"key":		"RegexPatternSetId",
	"filterid":	"RegexPatternSetId"
}

aws_waf_rule = {
	"clfn":		"waf",
	"descfn":	"list_rules",
	"topkey":	"Rules",
	"key":		"RuleId",
	"filterid":	"RuleId"
}

aws_waf_rule_group = {
	"clfn":		"waf",
	"descfn":	"list_rule_groups",
	"topkey":	"RuleGroups",
	"key":		"RuleGroupId",
	"filterid":	"RuleGroupId"
}

aws_waf_size_constraint_set = {
	"clfn":		"waf",
	"descfn":	"list_size_constraint_sets",
	"topkey":	"SizeConstraintSets",
	"key":		"SizeConstraintSetId",
	"filterid":	"SizeConstraintSetId"
}

aws_waf_sql_injection_match_set = {
	"clfn":		"waf",
	"descfn":	"list_sql_injection_match_sets",
	"topkey":	"SqlInjectionMatchSets",
	"key":		"SqlInjectionMatchSetId",
	"filterid":	"SqlInjectionMatchSetId"
}

aws_waf_web_acl = {
	"clfn":		"waf",
	"descfn":	"list_web_acls",
	"topkey":	"WebACLs",
	"key":		"WebACLId",
	"filterid":	"WebACLId"
}

aws_waf_xss_match_set = {
	"clfn":		"waf",
	"descfn":	"list_xss_match_sets",
	"topkey":	"XssMatchSets",
	"key":		"XssMatchSetId",
	"filterid":	"XssMatchSetId"
}

aws_wafregional_byte_match_set = {
	"clfn":		"waf-regional",
	"descfn":	"list_byte_match_sets",
	"topkey":	"ByteMatchSets",
	"key":		"ByteMatchSetId",
	"filterid":	"ByteMatchSetId"
}

aws_wafregional_geo_match_set = {
	"clfn":		"waf-regional",
	"descfn":	"list_geo_match_sets",
	"topkey":	"GeoMatchSets",
	"key":		"GeoMatchSetId",
	"filterid":	"GeoMatchSetId"
}

aws_wafregional_ipset = {
	"clfn":		"waf-regional",
	"descfn":	"list_ip_sets",
	"topkey":	"IPSets",
	"key":		"IPSetId",
	"filterid":	"IPSetId"
}

aws_wafregional_rate_based_rule = {
	"clfn":		"waf-regional",
	"descfn":	"list_rate_based_rules",
	"topkey":	"RateBasedRules",
	"key":		"RuleId",
	"filterid":	"RuleId"
}

aws_wafregional_regex_match_set = {
	"clfn":		"waf-regional",
	"descfn":	"list_regex_match_sets",
	"topkey":	"RegexMatchSets",
	"key":		"RegexMatchSetId",
	"filterid":	"RegexMatchSetId"
}

aws_wafregional_regex_pattern_set = {
	"clfn":		"waf-regional",
	"descfn":	"list_regex_pattern_sets",
	"topkey":	"RegexPatternSets",
	"key":		"RegexPatternSetId",
	"filterid":	"RegexPatternSetId"
}

aws_wafregional_rule = {
	"clfn":		"waf-regional",
	"descfn":	"list_rules",
	"topkey":	"Rules",
	"key":		"RuleId",
	"filterid":	"RuleId"
}

aws_wafregional_rule_group = {
	"clfn":		"waf-regional",
	"descfn":	"list_rule_groups",
	"topkey":	"RuleGroups",
	"key":		"RuleGroupId",
	"filterid":	"RuleGroupId"
}

aws_wafregional_size_constraint_set = {
	"clfn":		"waf-regional",
	"descfn":	"list_size_constraint_sets",
	"topkey":	"SizeConstraintSets",
	"key":		"SizeConstraintSetId",
	"filterid":	"SizeConstraintSetId"
}

aws_wafregional_sql_injection_match_set = {
	"clfn":		"waf-regional",
	"descfn":	"list_sql_injection_match_sets",
	"topkey":	"SqlInjectionMatchSets",
	"key":		"SqlInjectionMatchSetId",
	"filterid":	"SqlInjectionMatchSetId"
}

aws_wafregional_web_acl = {
	"clfn":		"waf-regional",
	"descfn":	"list_web_acls",
	"topkey":	"WebACLs",
	"key":		"WebACLId",
	"filterid":	"WebACLId"
}

aws_wafregional_web_acl_association = {
	"clfn":		"waf-regional",
	"descfn":	"list_web_acl_associations",
	"topkey":	"WebACLAssociations",
	"key":		"AssociationId",
	"filterid":	"AssociationId"
}

aws_wafregional_xss_match_set = {
	"clfn":		"waf-regional",
	"descfn":	"list_xss_match_sets",
	"topkey":	"XssMatchSets",
	"key":		"XssMatchSetId",
	"filterid":	"XssMatchSetId"
}

aws_wafv2_ip_set = {
	"clfn":		"wafv2",
	"descfn":	"list_ip_sets",
	"topkey":	"IPSets",
	"key":		"IPSetId",
	"filterid":	"IPSetId"
}

aws_wafv2_regex_pattern_set = {
	"clfn":		"wafv2",
	"descfn":	"list_regex_pattern_sets",
	"topkey":	"RegexPatternSets",
	"key":		"RegexPatternSetId",
	"filterid":	"RegexPatternSetId"
}

aws_wafv2_rule_group = {
	"clfn":		"wafv2",
	"descfn":	"list_rule_groups",
	"topkey":	"RuleGroups",
	"key":		"RuleGroupId",
	"filterid":	"RuleGroupId"
}

aws_wafv2_web_acl = {
	"clfn":		"wafv2",
	"descfn":	"list_web_acls",
	"topkey":	"WebACLs",
	"key":		"WebACLId",
	"filterid":	"WebACLId"
}

aws_wafv2_web_acl_association = {
	"clfn":		"wafv2",
	"descfn":	"list_web_acl_associations",
	"topkey":	"WebACLAssociations",
	"key":		"AssociationId",
	"filterid":	"AssociationId"
}

aws_wafv2_web_acl_logging_configuration = {
	"clfn":		"wafv2",
	"descfn":	"list_web_acl_logging_configurations",
	"topkey":	"WebACLLoggingConfigurations",
	"key":		"ResourceArn",
	"filterid":	"ResourceArn"
}

aws_worklink_fleet = {
	"clfn":		"worklink",
	"descfn":	"list_fleets",
	"topkey":	"Fleets",
	"key":		"FleetArn",
	"filterid":	"FleetArn"
}

aws_worklink_website_certificate_authority_association = {
	"clfn":		"worklink",
	"descfn":	"list_website_certificate_authority_associations",
	"topkey":	"WebsiteCertificateAuthorityAssociations",
	"key":		"AssociationId",
	"filterid":	"AssociationId"
}

aws_workspaces_connection_alias = {
	"clfn":		"workspaces",
	"descfn":	"list_connection_aliases",
	"topkey":	"ConnectionAliases",
	"key":		"ConnectionAliasId",
	"filterid":	"ConnectionAliasId"
}

aws_workspaces_directory = {
	"clfn":		"workspaces",
	"descfn":	"list_directories",
	"topkey":	"Directories",
	"key":		"DirectoryId",
	"filterid":	"DirectoryId"
}

aws_workspaces_ip_group = {
	"clfn":		"workspaces",
	"descfn":	"list_ip_groups",
	"topkey":	"IpGroups",
	"key":		"GroupId",
	"filterid":	"GroupId"
}

aws_workspaces_workspace = {
	"clfn":		"workspaces",
	"descfn":	"list_workspaces",
	"topkey":	"Workspaces",
	"key":		"WorkspaceId",
	"filterid":	"WorkspaceId"
}

aws_xray_encryption_config = {
	"clfn":		"xray",
	"descfn":	"get_encryption_config",
	"topkey":	"EncryptionConfig",
	"key":		"EncryptionConfigId",
	"filterid":	"EncryptionConfigId"
}

aws_xray_group = {
	"clfn":		"xray",
	"descfn":	"get_group",
	"topkey":	"Group",
	"key":		"GroupName",
	"filterid":	"GroupName"
}

aws_xray_sampling_rule = {
	"clfn":		"xray",
	"descfn":	"get_sampling_rules",
	"topkey":	"SamplingRuleRecords",
	"key":		"RuleName",
	"filterid":	"RuleArn"
}

aws_resources = {
	"aws_vpc": aws_vpc,
	"aws_vpc_ipv4_cidr_block_association": aws_vpc_ipv4_cidr_block_association,
	"aws_vpc_endpoint": aws_vpc_endpoint,
	"aws_subnet": aws_subnet,
	"aws_security_group": aws_security_group,
	"aws_internet_gateway": aws_internet_gateway,
	"aws_nat_gateway": aws_nat_gateway,
	"aws_network_acl": aws_network_acl,
	"aws_default_network_acl": aws_default_network_acl,
	"aws_route_table": aws_route_table,
	"aws_route_table_association": aws_route_table_association,
	"aws_default_route_table": aws_default_route_table,
	"aws_default_security_group": aws_default_security_group,
	"aws_vpc_dhcp_options": aws_vpc_dhcp_options,
	"aws_key_pair": aws_key_pair,
	"aws_launch_configuration": aws_launch_configuration,
	"aws_launch_template": aws_launch_template,
	"aws_vpc_ipv4_cidr_block_association": aws_vpc_ipv4_cidr_block_association,
	"aws_flow_log": aws_flow_log,
	"aws_iam_role": aws_iam_role,
	"aws_iam_policy": aws_iam_policy,
	"aws_iam_role_policy": aws_iam_role_policy,
	"aws_iam_role_policy_attachment": aws_iam_role_policy_attachment,
	"aws_iam_user": aws_iam_user,
	"aws_iam_instance_profile": aws_iam_instance_profile,
	"aws_vpclattice_access_log_subscription": aws_vpclattice_access_log_subscription,
	"aws_vpclattice_auth_policy": aws_vpclattice_auth_policy,
	"aws_vpclattice_listener": aws_vpclattice_listener,
	"aws_vpclattice_listener_rule": aws_vpclattice_listener_rule,
	"aws_vpclattice_resource_policy": aws_vpclattice_resource_policy,
	"aws_vpclattice_service": aws_vpclattice_service,
	"aws_vpclattice_service_network": aws_vpclattice_service_network,
	"aws_vpclattice_service_network_service_association": aws_vpclattice_service_network_service_association,
	"aws_vpclattice_service_network_vpc_association": aws_vpclattice_service_network_vpc_association,
	"aws_vpclattice_target_group": aws_vpclattice_target_group,
	"aws_eks_cluster": aws_eks_cluster,
	"aws_eks_fargate_profile": aws_eks_fargate_profile,
	"aws_eks_node_group": aws_eks_node_group,
	"aws_eks_addon": aws_eks_addon,
	"aws_eks_identity_provider_config": aws_eks_identity_provider_config,
    "aws_eks_pod_identity_association": aws_eks_pod_identity_association,
    "aws_eks_access_entry": aws_eks_access_entry,
    "aws_eks_access_policy_association": aws_eks_access_policy_association,
	"aws_kms_key": aws_kms_key,
	"aws_kms_alias": aws_kms_alias,
	"aws_ecs_cluster": aws_ecs_cluster,
	"aws_cloudwatch_log_group": aws_cloudwatch_log_group,
	"aws_config_config_rule": aws_config_config_rule,
	"aws_instance": aws_instance,
	"aws_lambda_function": aws_lambda_function,
	"aws_lambda_alias": aws_lambda_alias,
	"aws_lambda_permission": aws_lambda_permission,
	"aws_lambda_layer_version": aws_lambda_layer_version,
	"aws_lambda_function_event_invoke_config": aws_lambda_function_event_invoke_config,
	"aws_lambda_event_source_mapping": aws_lambda_event_source_mapping,
	"aws_lb": aws_lb,
	"aws_redshiftserverless_workgroup": aws_redshiftserverless_workgroup,
	"aws_redshiftserverless_namespace": aws_redshiftserverless_namespace,
	"aws_redshift_cluster": aws_redshift_cluster,
	"aws_redshift_subnet_group": aws_redshift_subnet_group,
	"aws_redshift_parameter_group": aws_redshift_parameter_group,
	"aws_rds_cluster": aws_rds_cluster,
	"aws_rds_cluster_parameter_group": aws_rds_cluster_parameter_group,
	"aws_rds_cluster_instance": aws_rds_cluster_instance,
	"aws_db_parameter_group": aws_db_parameter_group,
	"aws_db_subnet_group": aws_db_subnet_group,
	"aws_db_instance": aws_db_instance,
	"aws_db_event_subscription": aws_db_event_subscription,
	"aws_glue_crawler": aws_glue_crawler,
	"aws_glue_catalog_database": aws_glue_catalog_database,
	"aws_kinesis_stream": aws_kinesis_stream,
	"aws_secretsmanager_secret": aws_secretsmanager_secret,
	"aws_cloudwatch_event_rule": aws_cloudwatch_event_rule,
	"aws_accessanalyzer_analyzer": aws_accessanalyzer_analyzer,
	"aws_accessanalyzer_archive_rule": aws_accessanalyzer_archive_rule,
	"aws_account_alternate_contact": aws_account_alternate_contact,
	"aws_account_primary_contact": aws_account_primary_contact,
    "aws_acm_certificate": aws_acm_certificate,
	"aws_acm_certificate_validation": aws_acm_certificate_validation,
	"aws_acmpca_certificate": aws_acmpca_certificate,
	"aws_acmpca_certificate_authority": aws_acmpca_certificate_authority,
	"aws_acmpca_certificate_authority_certificate": aws_acmpca_certificate_authority_certificate,
	"aws_acmpca_permission": aws_acmpca_permission,
	"aws_acmpca_policy": aws_acmpca_policy,
	"aws_ami": aws_ami,
	"aws_ami_copy": aws_ami_copy,
	"aws_ami_from_instance": aws_ami_from_instance,
	"aws_ami_launch_permission": aws_ami_launch_permission,
	"aws_amplify_app": aws_amplify_app,
	"aws_amplify_backend_environment": aws_amplify_backend_environment,
	"aws_amplify_branch": aws_amplify_branch,
	"aws_amplify_domain_association": aws_amplify_domain_association,
	"aws_amplify_webhook": aws_amplify_webhook,
	"aws_api_gateway_account": aws_api_gateway_account,
	"aws_api_gateway_api_key": aws_api_gateway_api_key,
	"aws_api_gateway_authorizer": aws_api_gateway_authorizer,
	"aws_api_gateway_base_path_mapping": aws_api_gateway_base_path_mapping,
	"aws_api_gateway_client_certificate": aws_api_gateway_client_certificate,
	"aws_api_gateway_deployment": aws_api_gateway_deployment,
	"aws_api_gateway_documentation_part": aws_api_gateway_documentation_part,
	"aws_api_gateway_documentation_version": aws_api_gateway_documentation_version,
	"aws_api_gateway_domain_name": aws_api_gateway_domain_name,
	"aws_api_gateway_gateway_response": aws_api_gateway_gateway_response,
	"aws_api_gateway_integration": aws_api_gateway_integration,
	"aws_api_gateway_integration_response": aws_api_gateway_integration_response,
	"aws_api_gateway_method": aws_api_gateway_method,
	"aws_api_gateway_method_response": aws_api_gateway_method_response,
	"aws_api_gateway_method_settings": aws_api_gateway_method_settings,
	"aws_api_gateway_model": aws_api_gateway_model,
	"aws_api_gateway_request_validator": aws_api_gateway_request_validator,
	"aws_api_gateway_resource": aws_api_gateway_resource,
	"aws_api_gateway_rest_api": aws_api_gateway_rest_api,
	"aws_api_gateway_rest_api_policy": aws_api_gateway_rest_api_policy,
	"aws_api_gateway_stage": aws_api_gateway_stage,
	"aws_api_gateway_usage_plan": aws_api_gateway_usage_plan,
	"aws_api_gateway_usage_plan_key": aws_api_gateway_usage_plan_key,
	"aws_api_gateway_vpc_link": aws_api_gateway_vpc_link,
	"aws_apigatewayv2_api": aws_apigatewayv2_api,
	"aws_apigatewayv2_api_mapping": aws_apigatewayv2_api_mapping,
	"aws_apigatewayv2_authorizer": aws_apigatewayv2_authorizer,
	"aws_apigatewayv2_deployment": aws_apigatewayv2_deployment,
	"aws_apigatewayv2_domain_name": aws_apigatewayv2_domain_name,
	"aws_apigatewayv2_integration": aws_apigatewayv2_integration,
	"aws_apigatewayv2_integration_response": aws_apigatewayv2_integration_response,
	"aws_apigatewayv2_model": aws_apigatewayv2_model,
	"aws_apigatewayv2_route": aws_apigatewayv2_route,
	"aws_apigatewayv2_route_response": aws_apigatewayv2_route_response,
	"aws_apigatewayv2_stage": aws_apigatewayv2_stage,
	"aws_apigatewayv2_vpc_link": aws_apigatewayv2_vpc_link,
	"aws_app_cookie_stickiness_policy": aws_app_cookie_stickiness_policy,
	"aws_appautoscaling_policy": aws_appautoscaling_policy,
	"aws_appautoscaling_scheduled_action": aws_appautoscaling_scheduled_action,
	"aws_appautoscaling_target": aws_appautoscaling_target,
	"aws_appconfig_application": aws_appconfig_application,
	"aws_appconfig_configuration_profile": aws_appconfig_configuration_profile,
	"aws_appconfig_deployment": aws_appconfig_deployment,
	"aws_appconfig_deployment_strategy": aws_appconfig_deployment_strategy,
	"aws_appconfig_environment": aws_appconfig_environment,
	"aws_appconfig_extension_association": aws_appconfig_extension_association,
	"aws_appconfig_hosted_configuration_version": aws_appconfig_hosted_configuration_version,
	"aws_appflow_connector_profile": aws_appflow_connector_profile,
	"aws_appflow_flow": aws_appflow_flow,
	"aws_appintegrations_data_integration": aws_appintegrations_data_integration,
	"aws_appintegrations_event_integration": aws_appintegrations_event_integration,
	"aws_applicationinsights_application": aws_applicationinsights_application,
	"aws_appmesh_gateway_route": aws_appmesh_gateway_route,
	"aws_appmesh_mesh": aws_appmesh_mesh,
	"aws_appmesh_route": aws_appmesh_route,
	"aws_appmesh_virtual_gateway": aws_appmesh_virtual_gateway,
	"aws_appmesh_virtual_node": aws_appmesh_virtual_node,
	"aws_appmesh_virtual_router": aws_appmesh_virtual_router,
	"aws_appmesh_virtual_service": aws_appmesh_virtual_service,
	"aws_apprunner_auto_scaling_configuration_version": aws_apprunner_auto_scaling_configuration_version,
	"aws_apprunner_connection": aws_apprunner_connection,
	"aws_apprunner_custom_domain_association": aws_apprunner_custom_domain_association,
	"aws_apprunner_default_auto_scaling_configuration_version": aws_apprunner_default_auto_scaling_configuration_version,
	"aws_apprunner_observability_configuration": aws_apprunner_observability_configuration,
	"aws_apprunner_service": aws_apprunner_service,
	"aws_apprunner_vpc_connector": aws_apprunner_vpc_connector,
	"aws_apprunner_vpc_ingress_connection": aws_apprunner_vpc_ingress_connection,
	"aws_appstream_directory_config": aws_appstream_directory_config,
	"aws_appstream_fleet": aws_appstream_fleet,
	"aws_appstream_fleet_stack_association": aws_appstream_fleet_stack_association,
	"aws_appstream_image_builder": aws_appstream_image_builder,
	"aws_appstream_stack": aws_appstream_stack,
	"aws_appstream_user": aws_appstream_user,
	"aws_appstream_user_stack_association": aws_appstream_user_stack_association,
	"aws_appsync_api_cache": aws_appsync_api_cache,
	"aws_appsync_api_key": aws_appsync_api_key,
	"aws_appsync_datasource": aws_appsync_datasource,
	"aws_appsync_domain_name": aws_appsync_domain_name,
	"aws_appsync_domain_name_api_association": aws_appsync_domain_name_api_association,
	"aws_appsync_function": aws_appsync_function,
	"aws_appsync_graphql_api": aws_appsync_graphql_api,
	"aws_appsync_resolver": aws_appsync_resolver,
	"aws_appsync_type": aws_appsync_type,
	"aws_athena_data_catalog": aws_athena_data_catalog,
	"aws_athena_database": aws_athena_database,
	"aws_athena_named_query": aws_athena_named_query,
	"aws_athena_prepared_statement": aws_athena_prepared_statement,
	"aws_athena_workgroup": aws_athena_workgroup,
	"aws_auditmanager_account_registration": aws_auditmanager_account_registration,
	"aws_auditmanager_assessment": aws_auditmanager_assessment,
	"aws_auditmanager_assessment_delegation": aws_auditmanager_assessment_delegation,
	"aws_auditmanager_assessment_report": aws_auditmanager_assessment_report,
	"aws_auditmanager_control": aws_auditmanager_control,
	"aws_auditmanager_framework": aws_auditmanager_framework,
	"aws_auditmanager_framework_share": aws_auditmanager_framework_share,
	"aws_auditmanager_organization_admin_account_registration": aws_auditmanager_organization_admin_account_registration,
	"aws_autoscaling_attachment": aws_autoscaling_attachment,
	"aws_autoscaling_group": aws_autoscaling_group,
	"aws_autoscaling_group_tag": aws_autoscaling_group_tag,
	"aws_autoscaling_lifecycle_hook": aws_autoscaling_lifecycle_hook,
	"aws_autoscaling_notification": aws_autoscaling_notification,
	"aws_autoscaling_policy": aws_autoscaling_policy,
	"aws_autoscaling_schedule": aws_autoscaling_schedule,
	"aws_autoscaling_traffic_source_attachment": aws_autoscaling_traffic_source_attachment,
	"aws_autoscalingplans_scaling_plan": aws_autoscalingplans_scaling_plan,
	"aws_backup_framework": aws_backup_framework,
	"aws_backup_global_settings": aws_backup_global_settings,
	"aws_backup_plan": aws_backup_plan,
	"aws_backup_region_settings": aws_backup_region_settings,
	"aws_backup_report_plan": aws_backup_report_plan,
	"aws_backup_selection": aws_backup_selection,
	"aws_backup_vault": aws_backup_vault,
	"aws_backup_vault_lock_configuration": aws_backup_vault_lock_configuration,
	"aws_backup_vault_notifications": aws_backup_vault_notifications,
	"aws_backup_vault_policy": aws_backup_vault_policy,
	"aws_batch_compute_environment": aws_batch_compute_environment,
	"aws_batch_job_definition": aws_batch_job_definition,
	"aws_batch_job_queue": aws_batch_job_queue,
	"aws_batch_scheduling_policy": aws_batch_scheduling_policy,
	"aws_bedrock_model_invocation_logging_configuration": aws_bedrock_model_invocation_logging_configuration,
	"aws_budgets_budget": aws_budgets_budget,
	"aws_budgets_budget_action": aws_budgets_budget_action,
	"aws_ce_anomaly_monitor": aws_ce_anomaly_monitor,
	"aws_ce_anomaly_subscription": aws_ce_anomaly_subscription,
	"aws_ce_cost_allocation_tag": aws_ce_cost_allocation_tag,
	"aws_ce_cost_category": aws_ce_cost_category,
	"aws_chime_voice_connector": aws_chime_voice_connector,
	"aws_chime_voice_connector_group": aws_chime_voice_connector_group,
	"aws_chime_voice_connector_logging": aws_chime_voice_connector_logging,
	"aws_chime_voice_connector_origination": aws_chime_voice_connector_origination,
	"aws_chime_voice_connector_streaming": aws_chime_voice_connector_streaming,
	"aws_chime_voice_connector_termination": aws_chime_voice_connector_termination,
	"aws_chime_voice_connector_termination_credentials": aws_chime_voice_connector_termination_credentials,
	"aws_chimesdkmediapipelines_media_insights_pipeline_configuration": aws_chimesdkmediapipelines_media_insights_pipeline_configuration,
	"aws_chimesdkvoice_global_settings": aws_chimesdkvoice_global_settings,
	"aws_chimesdkvoice_sip_media_application": aws_chimesdkvoice_sip_media_application,
	"aws_chimesdkvoice_sip_rule": aws_chimesdkvoice_sip_rule,
	"aws_chimesdkvoice_voice_profile_domain": aws_chimesdkvoice_voice_profile_domain,
	"aws_cleanrooms_collaboration": aws_cleanrooms_collaboration,
	"aws_cleanrooms_configured_table": aws_cleanrooms_configured_table,
	"aws_cloud9_environment_ec2": aws_cloud9_environment_ec2,
	"aws_cloud9_environment_membership": aws_cloud9_environment_membership,
	"aws_cloudcontrolapi_resource": aws_cloudcontrolapi_resource,
	"aws_cloudformation_stack": aws_cloudformation_stack,
	"aws_cloudformation_stack_set": aws_cloudformation_stack_set,
	"aws_cloudformation_stack_set_instance": aws_cloudformation_stack_set_instance,
	"aws_cloudformation_type": aws_cloudformation_type,
	"aws_cloudfront_cache_policy": aws_cloudfront_cache_policy,
	"aws_cloudfront_continuous_deployment_policy": aws_cloudfront_continuous_deployment_policy,
	"aws_cloudfront_distribution": aws_cloudfront_distribution,
	"aws_cloudfront_field_level_encryption_config": aws_cloudfront_field_level_encryption_config,
	"aws_cloudfront_field_level_encryption_profile": aws_cloudfront_field_level_encryption_profile,
	"aws_cloudfront_function": aws_cloudfront_function,
	"aws_cloudfront_key_group": aws_cloudfront_key_group,
	"aws_cloudfront_monitoring_subscription": aws_cloudfront_monitoring_subscription,
	"aws_cloudfront_origin_access_control": aws_cloudfront_origin_access_control,
	"aws_cloudfront_origin_access_identity": aws_cloudfront_origin_access_identity,
	"aws_cloudfront_origin_request_policy": aws_cloudfront_origin_request_policy,
	"aws_cloudfront_public_key": aws_cloudfront_public_key,
	"aws_cloudfront_realtime_log_config": aws_cloudfront_realtime_log_config,
	"aws_cloudfront_response_headers_policy": aws_cloudfront_response_headers_policy,
	"aws_cloudhsm_v2_cluster": aws_cloudhsm_v2_cluster,
	"aws_cloudhsm_v2_hsm": aws_cloudhsm_v2_hsm,
	"aws_cloudsearch_domain": aws_cloudsearch_domain,
	"aws_cloudsearch_domain_service_access_policy": aws_cloudsearch_domain_service_access_policy,
	"aws_cloudtrail": aws_cloudtrail,
	"aws_cloudtrail_event_data_store": aws_cloudtrail_event_data_store,
	"aws_cloudwatch_composite_alarm": aws_cloudwatch_composite_alarm,
	"aws_cloudwatch_dashboard": aws_cloudwatch_dashboard,
	"aws_cloudwatch_event_api_destination": aws_cloudwatch_event_api_destination,
	"aws_cloudwatch_event_archive": aws_cloudwatch_event_archive,
	"aws_cloudwatch_event_bus": aws_cloudwatch_event_bus,
	"aws_cloudwatch_event_bus_policy": aws_cloudwatch_event_bus_policy,
	"aws_cloudwatch_event_connection": aws_cloudwatch_event_connection,
	"aws_cloudwatch_event_endpoint": aws_cloudwatch_event_endpoint,
	"aws_cloudwatch_event_permission": aws_cloudwatch_event_permission,
	"aws_cloudwatch_event_target": aws_cloudwatch_event_target,
	"aws_cloudwatch_log_data_protection_policy": aws_cloudwatch_log_data_protection_policy,
	"aws_cloudwatch_log_destination": aws_cloudwatch_log_destination,
	"aws_cloudwatch_log_destination_policy": aws_cloudwatch_log_destination_policy,
	"aws_cloudwatch_log_metric_filter": aws_cloudwatch_log_metric_filter,
	"aws_cloudwatch_log_resource_policy": aws_cloudwatch_log_resource_policy,
	"aws_cloudwatch_log_stream": aws_cloudwatch_log_stream,
	"aws_cloudwatch_log_subscription_filter": aws_cloudwatch_log_subscription_filter,
	"aws_cloudwatch_metric_alarm": aws_cloudwatch_metric_alarm,
	"aws_cloudwatch_metric_stream": aws_cloudwatch_metric_stream,
	"aws_cloudwatch_query_definition": aws_cloudwatch_query_definition,
	"aws_codeartifact_domain": aws_codeartifact_domain,
	"aws_codeartifact_domain_permissions_policy": aws_codeartifact_domain_permissions_policy,
	"aws_codeartifact_repository": aws_codeartifact_repository,
	"aws_codeartifact_repository_permissions_policy": aws_codeartifact_repository_permissions_policy,
	"aws_codebuild_project": aws_codebuild_project,
	"aws_codebuild_report_group": aws_codebuild_report_group,
	"aws_codebuild_resource_policy": aws_codebuild_resource_policy,
	"aws_codebuild_source_credential": aws_codebuild_source_credential,
	"aws_codebuild_webhook": aws_codebuild_webhook,
	"aws_codecatalyst_dev_environment": aws_codecatalyst_dev_environment,
	"aws_codecatalyst_project": aws_codecatalyst_project,
	"aws_codecatalyst_source_repository": aws_codecatalyst_source_repository,
	"aws_codecommit_approval_rule_template": aws_codecommit_approval_rule_template,
	"aws_codecommit_approval_rule_template_association": aws_codecommit_approval_rule_template_association,
	"aws_codecommit_repository": aws_codecommit_repository,
	"aws_codecommit_trigger": aws_codecommit_trigger,
	"aws_codedeploy_app": aws_codedeploy_app,
	"aws_codedeploy_deployment_config": aws_codedeploy_deployment_config,
	"aws_codedeploy_deployment_group": aws_codedeploy_deployment_group,
	"aws_codeguruprofiler_profiling_group": aws_codeguruprofiler_profiling_group,
	"aws_codegurureviewer_repository_association": aws_codegurureviewer_repository_association,
	"aws_codepipeline": aws_codepipeline,
	"aws_codepipeline_custom_action_type": aws_codepipeline_custom_action_type,
	"aws_codepipeline_webhook": aws_codepipeline_webhook,
	"aws_codestarconnections_connection": aws_codestarconnections_connection,
	"aws_codestarconnections_host": aws_codestarconnections_host,
	"aws_codestarnotifications_notification_rule": aws_codestarnotifications_notification_rule,
	"aws_cognito_identity_pool": aws_cognito_identity_pool,
	"aws_cognito_identity_pool_provider_principal_tag": aws_cognito_identity_pool_provider_principal_tag,
	"aws_cognito_identity_pool_roles_attachment": aws_cognito_identity_pool_roles_attachment,
	"aws_cognito_identity_provider": aws_cognito_identity_provider,
	"aws_cognito_managed_user_pool_client": aws_cognito_managed_user_pool_client,
	"aws_cognito_resource_server": aws_cognito_resource_server,
	"aws_cognito_risk_configuration": aws_cognito_risk_configuration,
	"aws_cognito_user": aws_cognito_user,
	"aws_cognito_user_group": aws_cognito_user_group,
	"aws_cognito_user_in_group": aws_cognito_user_in_group,
	"aws_cognito_user_pool": aws_cognito_user_pool,
	"aws_cognito_user_pool_client": aws_cognito_user_pool_client,
	"aws_cognito_user_pool_domain": aws_cognito_user_pool_domain,
	"aws_cognito_user_pool_ui_customization": aws_cognito_user_pool_ui_customization,
	"aws_comprehend_document_classifier": aws_comprehend_document_classifier,
	"aws_comprehend_entity_recognizer": aws_comprehend_entity_recognizer,
	"aws_config_aggregate_authorization": aws_config_aggregate_authorization,
	"aws_config_configuration_aggregator": aws_config_configuration_aggregator,
	"aws_config_configuration_recorder": aws_config_configuration_recorder,
	"aws_config_configuration_recorder_status": aws_config_configuration_recorder_status,
	"aws_config_conformance_pack": aws_config_conformance_pack,
	"aws_config_delivery_channel": aws_config_delivery_channel,
	"aws_config_organization_conformance_pack": aws_config_organization_conformance_pack,
	"aws_config_organization_custom_policy_rule": aws_config_organization_custom_policy_rule,
	"aws_config_organization_custom_rule": aws_config_organization_custom_rule,
	"aws_config_organization_managed_rule": aws_config_organization_managed_rule,
	"aws_config_remediation_configuration": aws_config_remediation_configuration,
	"aws_connect_bot_association": aws_connect_bot_association,
	"aws_connect_contact_flow": aws_connect_contact_flow,
	"aws_connect_contact_flow_module": aws_connect_contact_flow_module,
	"aws_connect_hours_of_operation": aws_connect_hours_of_operation,
	"aws_connect_instance": aws_connect_instance,
	"aws_connect_instance_storage_config": aws_connect_instance_storage_config,
	"aws_connect_lambda_function_association": aws_connect_lambda_function_association,
	"aws_connect_phone_number": aws_connect_phone_number,
	"aws_connect_queue": aws_connect_queue,
	"aws_connect_quick_connect": aws_connect_quick_connect,
	"aws_connect_routing_profile": aws_connect_routing_profile,
	"aws_connect_security_profile": aws_connect_security_profile,
	"aws_connect_user": aws_connect_user,
	"aws_connect_user_hierarchy_group": aws_connect_user_hierarchy_group,
	"aws_connect_user_hierarchy_structure": aws_connect_user_hierarchy_structure,
	"aws_connect_vocabulary": aws_connect_vocabulary,
	"aws_controltower_control": aws_controltower_control,
	"aws_cur_report_definition": aws_cur_report_definition,
	"aws_customer_gateway": aws_customer_gateway,
	"aws_customerprofiles_domain": aws_customerprofiles_domain,
	"aws_customerprofiles_profile": aws_customerprofiles_profile,
	"aws_dataexchange_data_set": aws_dataexchange_data_set,
	"aws_dataexchange_revision": aws_dataexchange_revision,
	"aws_datapipeline_pipeline": aws_datapipeline_pipeline,
	"aws_datapipeline_pipeline_definition": aws_datapipeline_pipeline_definition,
	"aws_datasync_agent": aws_datasync_agent,
	"aws_datasync_location_azure_blob": aws_datasync_location_azure_blob,
	"aws_datasync_location_efs": aws_datasync_location_efs,
	"aws_datasync_location_fsx_lustre_file_system": aws_datasync_location_fsx_lustre_file_system,
	"aws_datasync_location_fsx_ontap_file_system": aws_datasync_location_fsx_ontap_file_system,
	"aws_datasync_location_fsx_openzfs_file_system": aws_datasync_location_fsx_openzfs_file_system,
	"aws_datasync_location_fsx_windows_file_system": aws_datasync_location_fsx_windows_file_system,
	"aws_datasync_location_hdfs": aws_datasync_location_hdfs,
	"aws_datasync_location_nfs": aws_datasync_location_nfs,
	"aws_datasync_location_object_storage": aws_datasync_location_object_storage,
	"aws_datasync_location_s3": aws_datasync_location_s3,
	"aws_datasync_location_smb": aws_datasync_location_smb,
	"aws_datasync_task": aws_datasync_task,
	"aws_dax_cluster": aws_dax_cluster,
	"aws_dax_parameter_group": aws_dax_parameter_group,
	"aws_dax_subnet_group": aws_dax_subnet_group,
	"aws_db_cluster_snapshot": aws_db_cluster_snapshot,
	"aws_db_instance": aws_db_instance,
	"aws_db_instance_automated_backups_replication": aws_db_instance_automated_backups_replication,
	"aws_db_instance_role_association": aws_db_instance_role_association,
	"aws_db_option_group": aws_db_option_group,
	"aws_db_proxy": aws_db_proxy,
	"aws_db_proxy_default_target_group": aws_db_proxy_default_target_group,
	"aws_db_proxy_endpoint": aws_db_proxy_endpoint,
	"aws_db_proxy_target": aws_db_proxy_target,
	"aws_db_snapshot": aws_db_snapshot,
	"aws_db_snapshot_copy": aws_db_snapshot_copy,
	"aws_default_vpc_dhcp_options": aws_default_vpc_dhcp_options,
	"aws_detective_graph": aws_detective_graph,
	"aws_detective_invitation_accepter": aws_detective_invitation_accepter,
	"aws_detective_member": aws_detective_member,
	"aws_detective_organization_admin_account": aws_detective_organization_admin_account,
	"aws_detective_organization_configuration": aws_detective_organization_configuration,
	"aws_devicefarm_device_pool": aws_devicefarm_device_pool,
	"aws_devicefarm_instance_profile": aws_devicefarm_instance_profile,
	"aws_devicefarm_network_profile": aws_devicefarm_network_profile,
	"aws_devicefarm_project": aws_devicefarm_project,
	"aws_devicefarm_test_grid_project": aws_devicefarm_test_grid_project,
	"aws_devicefarm_upload": aws_devicefarm_upload,
	"aws_directory_service_conditional_forwarder": aws_directory_service_conditional_forwarder,
	"aws_directory_service_directory": aws_directory_service_directory,
	"aws_directory_service_log_subscription": aws_directory_service_log_subscription,
	"aws_directory_service_radius_settings": aws_directory_service_radius_settings,
	"aws_directory_service_region": aws_directory_service_region,
	"aws_directory_service_shared_directory": aws_directory_service_shared_directory,
	"aws_directory_service_trust": aws_directory_service_trust,
	"aws_dlm_lifecycle_policy": aws_dlm_lifecycle_policy,
	"aws_dms_certificate": aws_dms_certificate,
	"aws_dms_endpoint": aws_dms_endpoint,
	"aws_dms_event_subscription": aws_dms_event_subscription,
	"aws_dms_replication_config": aws_dms_replication_config,
	"aws_dms_replication_instance": aws_dms_replication_instance,
	"aws_dms_replication_subnet_group": aws_dms_replication_subnet_group,
	"aws_dms_replication_task": aws_dms_replication_task,
	"aws_dms_s3_endpoint": aws_dms_s3_endpoint,
	"aws_docdb_cluster": aws_docdb_cluster,
	"aws_docdb_cluster_instance": aws_docdb_cluster_instance,
	"aws_docdb_cluster_parameter_group": aws_docdb_cluster_parameter_group,
	"aws_docdb_cluster_snapshot": aws_docdb_cluster_snapshot,
	"aws_docdb_event_subscription": aws_docdb_event_subscription,
	"aws_docdb_global_cluster": aws_docdb_global_cluster,
	"aws_docdb_subnet_group": aws_docdb_subnet_group,
	"aws_docdbelastic_cluster": aws_docdbelastic_cluster,
	"aws_dx_bgp_peer": aws_dx_bgp_peer,
	"aws_dx_connection": aws_dx_connection,
	"aws_dx_connection_association": aws_dx_connection_association,
	"aws_dx_connection_confirmation": aws_dx_connection_confirmation,
	"aws_dx_gateway": aws_dx_gateway,
	"aws_dx_gateway_association": aws_dx_gateway_association,
	"aws_dx_gateway_association_proposal": aws_dx_gateway_association_proposal,
	"aws_dx_hosted_connection": aws_dx_hosted_connection,
	"aws_dx_hosted_private_virtual_interface": aws_dx_hosted_private_virtual_interface,
	"aws_dx_hosted_private_virtual_interface_accepter": aws_dx_hosted_private_virtual_interface_accepter,
	"aws_dx_hosted_public_virtual_interface": aws_dx_hosted_public_virtual_interface,
	"aws_dx_hosted_public_virtual_interface_accepter": aws_dx_hosted_public_virtual_interface_accepter,
	"aws_dx_hosted_transit_virtual_interface": aws_dx_hosted_transit_virtual_interface,
	"aws_dx_hosted_transit_virtual_interface_accepter": aws_dx_hosted_transit_virtual_interface_accepter,
	"aws_dx_lag": aws_dx_lag,
	"aws_dx_macsec_key_association": aws_dx_macsec_key_association,
	"aws_dx_private_virtual_interface": aws_dx_private_virtual_interface,
	"aws_dx_public_virtual_interface": aws_dx_public_virtual_interface,
	"aws_dx_transit_virtual_interface": aws_dx_transit_virtual_interface,
	"aws_dynamodb_contributor_insights": aws_dynamodb_contributor_insights,
	"aws_dynamodb_global_table": aws_dynamodb_global_table,
	"aws_dynamodb_kinesis_streaming_destination": aws_dynamodb_kinesis_streaming_destination,
	"aws_dynamodb_table": aws_dynamodb_table,
	"aws_dynamodb_table_item": aws_dynamodb_table_item,
	"aws_dynamodb_table_replica": aws_dynamodb_table_replica,
	"aws_dynamodb_tag": aws_dynamodb_tag,
	"aws_ebs_default_kms_key": aws_ebs_default_kms_key,
	"aws_ebs_encryption_by_default": aws_ebs_encryption_by_default,
	"aws_ebs_snapshot": aws_ebs_snapshot,
	"aws_ebs_snapshot_copy": aws_ebs_snapshot_copy,
	"aws_ebs_snapshot_import": aws_ebs_snapshot_import,
	"aws_ebs_volume": aws_ebs_volume,
	"aws_ec2_availability_zone_group": aws_ec2_availability_zone_group,
	"aws_ec2_capacity_reservation": aws_ec2_capacity_reservation,
	"aws_ec2_carrier_gateway": aws_ec2_carrier_gateway,
	"aws_ec2_client_vpn_authorization_rule": aws_ec2_client_vpn_authorization_rule,
	"aws_ec2_client_vpn_endpoint": aws_ec2_client_vpn_endpoint,
	"aws_ec2_client_vpn_network_association": aws_ec2_client_vpn_network_association,
	"aws_ec2_client_vpn_route": aws_ec2_client_vpn_route,
	"aws_ec2_fleet": aws_ec2_fleet,
	"aws_ec2_host": aws_ec2_host,
	"aws_ec2_image_block_public_access": aws_ec2_image_block_public_access,
	"aws_ec2_instance_connect_endpoint": aws_ec2_instance_connect_endpoint,
	"aws_ec2_instance_state": aws_ec2_instance_state,
	"aws_ec2_local_gateway_route": aws_ec2_local_gateway_route,
	"aws_ec2_local_gateway_route_table_vpc_association": aws_ec2_local_gateway_route_table_vpc_association,
	"aws_ec2_managed_prefix_list": aws_ec2_managed_prefix_list,
	"aws_ec2_managed_prefix_list_entry": aws_ec2_managed_prefix_list_entry,
	"aws_ec2_subnet_cidr_reservation": aws_ec2_subnet_cidr_reservation,
	"aws_ec2_tag": aws_ec2_tag,
	"aws_ec2_traffic_mirror_filter": aws_ec2_traffic_mirror_filter,
	"aws_ec2_traffic_mirror_filter_rule": aws_ec2_traffic_mirror_filter_rule,
	"aws_ec2_traffic_mirror_session": aws_ec2_traffic_mirror_session,
	"aws_ec2_traffic_mirror_target": aws_ec2_traffic_mirror_target,
	"aws_ec2_transit_gateway": aws_ec2_transit_gateway,
	"aws_ec2_transit_gateway_connect": aws_ec2_transit_gateway_connect,
	"aws_ec2_transit_gateway_connect_peer": aws_ec2_transit_gateway_connect_peer,
	"aws_ec2_transit_gateway_multicast_domain": aws_ec2_transit_gateway_multicast_domain,
	"aws_ec2_transit_gateway_multicast_domain_association": aws_ec2_transit_gateway_multicast_domain_association,
	"aws_ec2_transit_gateway_multicast_group_member": aws_ec2_transit_gateway_multicast_group_member,
	"aws_ec2_transit_gateway_multicast_group_source": aws_ec2_transit_gateway_multicast_group_source,
	"aws_ec2_transit_gateway_peering_attachment": aws_ec2_transit_gateway_peering_attachment,
	"aws_ec2_transit_gateway_peering_attachment_accepter": aws_ec2_transit_gateway_peering_attachment_accepter,
	"aws_ec2_transit_gateway_policy_table": aws_ec2_transit_gateway_policy_table,
	"aws_ec2_transit_gateway_policy_table_association": aws_ec2_transit_gateway_policy_table_association,
	"aws_ec2_transit_gateway_prefix_list_reference": aws_ec2_transit_gateway_prefix_list_reference,
	"aws_ec2_transit_gateway_route": aws_ec2_transit_gateway_route,
	"aws_ec2_transit_gateway_route_table": aws_ec2_transit_gateway_route_table,
	"aws_ec2_transit_gateway_route_table_association": aws_ec2_transit_gateway_route_table_association,
	"aws_ec2_transit_gateway_vpc_attachment": aws_ec2_transit_gateway_vpc_attachment,
	"aws_ec2_transit_gateway_vpc_attachment_accepter": aws_ec2_transit_gateway_vpc_attachment_accepter,
	"aws_ecr_lifecycle_policy": aws_ecr_lifecycle_policy,
	"aws_ecr_pull_through_cache_rule": aws_ecr_pull_through_cache_rule,
	"aws_ecr_registry_policy": aws_ecr_registry_policy,
	"aws_ecr_registry_scanning_configuration": aws_ecr_registry_scanning_configuration,
	"aws_ecr_replication_configuration": aws_ecr_replication_configuration,
	"aws_ecr_repository": aws_ecr_repository,
	"aws_ecr_repository_policy": aws_ecr_repository_policy,
	"aws_ecrpublic_repository": aws_ecrpublic_repository,
	"aws_ecrpublic_repository_policy": aws_ecrpublic_repository_policy,
	"aws_ecs_account_setting_default": aws_ecs_account_setting_default,
	"aws_ecs_capacity_provider": aws_ecs_capacity_provider,
	"aws_ecs_cluster_capacity_providers": aws_ecs_cluster_capacity_providers,
	"aws_ecs_service": aws_ecs_service,
	"aws_ecs_tag": aws_ecs_tag,
	"aws_ecs_task_definition": aws_ecs_task_definition,
	"aws_ecs_task_set": aws_ecs_task_set,
	"aws_efs_access_point": aws_efs_access_point,
	"aws_efs_backup_policy": aws_efs_backup_policy,
	"aws_efs_file_system": aws_efs_file_system,
	"aws_efs_file_system_policy": aws_efs_file_system_policy,
	"aws_efs_mount_target": aws_efs_mount_target,
	"aws_efs_replication_configuration": aws_efs_replication_configuration,
	"aws_egress_only_internet_gateway": aws_egress_only_internet_gateway,
	"aws_eip": aws_eip,
	"aws_eip_association": aws_eip_association,
	"aws_elastic_beanstalk_application": aws_elastic_beanstalk_application,
	"aws_elastic_beanstalk_application_version": aws_elastic_beanstalk_application_version,
	"aws_elastic_beanstalk_configuration_template": aws_elastic_beanstalk_configuration_template,
	"aws_elastic_beanstalk_environment": aws_elastic_beanstalk_environment,
	"aws_elasticache_cluster": aws_elasticache_cluster,
	"aws_elasticache_global_replication_group": aws_elasticache_global_replication_group,
	"aws_elasticache_parameter_group": aws_elasticache_parameter_group,
	"aws_elasticache_replication_group": aws_elasticache_replication_group,
	"aws_elasticache_subnet_group": aws_elasticache_subnet_group,
	"aws_elasticache_user": aws_elasticache_user,
	"aws_elasticache_user_group": aws_elasticache_user_group,
	"aws_elasticache_user_group_association": aws_elasticache_user_group_association,
	"aws_elasticsearch_domain": aws_elasticsearch_domain,
	"aws_elasticsearch_domain_policy": aws_elasticsearch_domain_policy,
	"aws_elasticsearch_vpc_endpoint": aws_elasticsearch_vpc_endpoint,
	"aws_elastictranscoder_pipeline": aws_elastictranscoder_pipeline,
	"aws_elastictranscoder_preset": aws_elastictranscoder_preset,
	"aws_elb": aws_elb,
	"aws_elb_attachment": aws_elb_attachment,
	"aws_emr_block_public_access_configuration": aws_emr_block_public_access_configuration,
	"aws_emr_cluster": aws_emr_cluster,
	"aws_emr_instance_fleet": aws_emr_instance_fleet,
	"aws_emr_instance_group": aws_emr_instance_group,
	"aws_emr_managed_scaling_policy": aws_emr_managed_scaling_policy,
	"aws_emr_security_configuration": aws_emr_security_configuration,
	"aws_emr_studio": aws_emr_studio,
	"aws_emr_studio_session_mapping": aws_emr_studio_session_mapping,
	"aws_emrcontainers_job_template": aws_emrcontainers_job_template,
	"aws_emrcontainers_virtual_cluster": aws_emrcontainers_virtual_cluster,
	"aws_emrserverless_application": aws_emrserverless_application,
	"aws_evidently_feature": aws_evidently_feature,
	"aws_evidently_launch": aws_evidently_launch,
	"aws_evidently_project": aws_evidently_project,
	"aws_evidently_segment": aws_evidently_segment,
	"aws_finspace_kx_cluster": aws_finspace_kx_cluster,
	"aws_finspace_kx_database": aws_finspace_kx_database,
	"aws_finspace_kx_dataview": aws_finspace_kx_dataview,
	"aws_finspace_kx_environment": aws_finspace_kx_environment,
	"aws_finspace_kx_scaling_group": aws_finspace_kx_scaling_group,
	"aws_finspace_kx_user": aws_finspace_kx_user,
	"aws_finspace_kx_volume": aws_finspace_kx_volume,
	"aws_fis_experiment_template": aws_fis_experiment_template,
	"aws_fms_admin_account": aws_fms_admin_account,
	"aws_fms_policy": aws_fms_policy,
	"aws_fsx_backup": aws_fsx_backup,
	"aws_fsx_data_repository_association": aws_fsx_data_repository_association,
	"aws_fsx_file_cache": aws_fsx_file_cache,
	"aws_fsx_lustre_file_system": aws_fsx_lustre_file_system,
	"aws_fsx_ontap_file_system": aws_fsx_ontap_file_system,
	"aws_fsx_ontap_storage_virtual_machine": aws_fsx_ontap_storage_virtual_machine,
	"aws_fsx_ontap_volume": aws_fsx_ontap_volume,
	"aws_fsx_openzfs_file_system": aws_fsx_openzfs_file_system,
	"aws_fsx_openzfs_snapshot": aws_fsx_openzfs_snapshot,
	"aws_fsx_openzfs_volume": aws_fsx_openzfs_volume,
	"aws_fsx_windows_file_system": aws_fsx_windows_file_system,
	"aws_gamelift_alias": aws_gamelift_alias,
	"aws_gamelift_build": aws_gamelift_build,
	"aws_gamelift_fleet": aws_gamelift_fleet,
	"aws_gamelift_game_server_group": aws_gamelift_game_server_group,
	"aws_gamelift_game_session_queue": aws_gamelift_game_session_queue,
	"aws_gamelift_script": aws_gamelift_script,
	"aws_glacier_vault": aws_glacier_vault,
	"aws_glacier_vault_lock": aws_glacier_vault_lock,
	"aws_globalaccelerator_accelerator": aws_globalaccelerator_accelerator,
	"aws_globalaccelerator_custom_routing_accelerator": aws_globalaccelerator_custom_routing_accelerator,
	"aws_globalaccelerator_custom_routing_endpoint_group": aws_globalaccelerator_custom_routing_endpoint_group,
	"aws_globalaccelerator_custom_routing_listener": aws_globalaccelerator_custom_routing_listener,
	"aws_globalaccelerator_endpoint_group": aws_globalaccelerator_endpoint_group,
	"aws_globalaccelerator_listener": aws_globalaccelerator_listener,
	"aws_glue_catalog_table": aws_glue_catalog_table,
	"aws_glue_classifier": aws_glue_classifier,
	"aws_glue_connection": aws_glue_connection,
	"aws_glue_data_catalog_encryption_settings": aws_glue_data_catalog_encryption_settings,
	"aws_glue_data_quality_ruleset": aws_glue_data_quality_ruleset,
	"aws_glue_dev_endpoint": aws_glue_dev_endpoint,
	"aws_glue_job": aws_glue_job,
	"aws_glue_ml_transform": aws_glue_ml_transform,
	"aws_glue_partition": aws_glue_partition,
	"aws_glue_partition_index": aws_glue_partition_index,
	"aws_glue_registry": aws_glue_registry,
	"aws_glue_resource_policy": aws_glue_resource_policy,
	"aws_glue_schema": aws_glue_schema,
	"aws_glue_security_configuration": aws_glue_security_configuration,
	"aws_glue_trigger": aws_glue_trigger,
	"aws_glue_user_defined_function": aws_glue_user_defined_function,
	"aws_glue_workflow": aws_glue_workflow,
	"aws_grafana_license_association": aws_grafana_license_association,
	"aws_grafana_role_association": aws_grafana_role_association,
	"aws_grafana_workspace": aws_grafana_workspace,
	"aws_grafana_workspace_api_key": aws_grafana_workspace_api_key,
	"aws_grafana_workspace_saml_configuration": aws_grafana_workspace_saml_configuration,
	"aws_guardduty_detector": aws_guardduty_detector,
	"aws_guardduty_detector_feature": aws_guardduty_detector_feature,
	"aws_guardduty_filter": aws_guardduty_filter,
	"aws_guardduty_invite_accepter": aws_guardduty_invite_accepter,
	"aws_guardduty_ipset": aws_guardduty_ipset,
	"aws_guardduty_member": aws_guardduty_member,
	"aws_guardduty_organization_admin_account": aws_guardduty_organization_admin_account,
	"aws_guardduty_organization_configuration": aws_guardduty_organization_configuration,
	"aws_guardduty_organization_configuration_feature": aws_guardduty_organization_configuration_feature,
	"aws_guardduty_publishing_destination": aws_guardduty_publishing_destination,
	"aws_guardduty_threatintelset": aws_guardduty_threatintelset,
	"aws_iam_access_key": aws_iam_access_key,
	"aws_iam_account_alias": aws_iam_account_alias,
	"aws_iam_account_password_policy": aws_iam_account_password_policy,
	"aws_iam_group": aws_iam_group,
	"aws_iam_group_membership": aws_iam_group_membership,
	"aws_iam_group_policy": aws_iam_group_policy,
	"aws_iam_group_policy_attachment": aws_iam_group_policy_attachment,
	"aws_iam_openid_connect_provider": aws_iam_openid_connect_provider,
	"aws_iam_policy": aws_iam_policy,
	"aws_iam_policy_attachment": aws_iam_policy_attachment,
	"aws_iam_saml_provider": aws_iam_saml_provider,
	"aws_iam_security_token_service_preferences": aws_iam_security_token_service_preferences,
	"aws_iam_server_certificate": aws_iam_server_certificate,
	"aws_iam_service_linked_role": aws_iam_service_linked_role,
	"aws_iam_service_specific_credential": aws_iam_service_specific_credential,
	"aws_iam_signing_certificate": aws_iam_signing_certificate,
	"aws_iam_user_group_membership": aws_iam_user_group_membership,
	"aws_iam_user_login_profile": aws_iam_user_login_profile,
	"aws_iam_user_policy": aws_iam_user_policy,
	"aws_iam_user_policy_attachment": aws_iam_user_policy_attachment,
	"aws_iam_user_ssh_key": aws_iam_user_ssh_key,
	"aws_iam_virtual_mfa_device": aws_iam_virtual_mfa_device,
	"aws_identitystore_group": aws_identitystore_group,
	"aws_identitystore_group_membership": aws_identitystore_group_membership,
	"aws_identitystore_user": aws_identitystore_user,
	"aws_imagebuilder_component": aws_imagebuilder_component,
	"aws_imagebuilder_container_recipe": aws_imagebuilder_container_recipe,
	"aws_imagebuilder_distribution_configuration": aws_imagebuilder_distribution_configuration,
	"aws_imagebuilder_image": aws_imagebuilder_image,
	"aws_imagebuilder_image_pipeline": aws_imagebuilder_image_pipeline,
	"aws_imagebuilder_image_recipe": aws_imagebuilder_image_recipe,
	"aws_imagebuilder_infrastructure_configuration": aws_imagebuilder_infrastructure_configuration,
	"aws_inspector2_delegated_admin_account": aws_inspector2_delegated_admin_account,
	"aws_inspector2_enabler": aws_inspector2_enabler,
	"aws_inspector2_member_association": aws_inspector2_member_association,
	"aws_inspector2_organization_configuration": aws_inspector2_organization_configuration,
	"aws_inspector_assessment_target": aws_inspector_assessment_target,
	"aws_inspector_assessment_template": aws_inspector_assessment_template,
	"aws_inspector_resource_group": aws_inspector_resource_group,
	"aws_internet_gateway_attachment": aws_internet_gateway_attachment,
	"aws_internetmonitor_monitor": aws_internetmonitor_monitor,
	"aws_iot_authorizer": aws_iot_authorizer,
	"aws_iot_billing_group": aws_iot_billing_group,
	"aws_iot_ca_certificate": aws_iot_ca_certificate,
	"aws_iot_certificate": aws_iot_certificate,
	"aws_iot_domain_configuration": aws_iot_domain_configuration,
	"aws_iot_event_configurations": aws_iot_event_configurations,
	"aws_iot_indexing_configuration": aws_iot_indexing_configuration,
	"aws_iot_logging_options": aws_iot_logging_options,
	"aws_iot_policy": aws_iot_policy,
	"aws_iot_policy_attachment": aws_iot_policy_attachment,
	"aws_iot_provisioning_template": aws_iot_provisioning_template,
	"aws_iot_role_alias": aws_iot_role_alias,
	"aws_iot_thing": aws_iot_thing,
	"aws_iot_thing_group": aws_iot_thing_group,
	"aws_iot_thing_group_membership": aws_iot_thing_group_membership,
	"aws_iot_thing_principal_attachment": aws_iot_thing_principal_attachment,
	"aws_iot_thing_type": aws_iot_thing_type,
	"aws_iot_topic_rule": aws_iot_topic_rule,
	"aws_iot_topic_rule_destination": aws_iot_topic_rule_destination,
	"aws_ivs_channel": aws_ivs_channel,
	"aws_ivs_playback_key_pair": aws_ivs_playback_key_pair,
	"aws_ivs_recording_configuration": aws_ivs_recording_configuration,
	"aws_ivschat_logging_configuration": aws_ivschat_logging_configuration,
	"aws_ivschat_room": aws_ivschat_room,
	"aws_kendra_data_source": aws_kendra_data_source,
	"aws_kendra_experience": aws_kendra_experience,
	"aws_kendra_faq": aws_kendra_faq,
	"aws_kendra_index": aws_kendra_index,
	"aws_kendra_query_suggestions_block_list": aws_kendra_query_suggestions_block_list,
	"aws_kendra_thesaurus": aws_kendra_thesaurus,
	"aws_keyspaces_keyspace": aws_keyspaces_keyspace,
	"aws_keyspaces_table": aws_keyspaces_table,
	"aws_kinesis_analytics_application": aws_kinesis_analytics_application,
	"aws_kinesis_firehose_delivery_stream": aws_kinesis_firehose_delivery_stream,
	"aws_kinesis_stream_consumer": aws_kinesis_stream_consumer,
	"aws_kinesis_video_stream": aws_kinesis_video_stream,
	"aws_kinesisanalyticsv2_application": aws_kinesisanalyticsv2_application,
	"aws_kinesisanalyticsv2_application_snapshot": aws_kinesisanalyticsv2_application_snapshot,
	"aws_kms_ciphertext": aws_kms_ciphertext,
	"aws_kms_custom_key_store": aws_kms_custom_key_store,
	"aws_kms_external_key": aws_kms_external_key,
	"aws_kms_grant": aws_kms_grant,
	"aws_kms_key_policy": aws_kms_key_policy,
	"aws_kms_replica_external_key": aws_kms_replica_external_key,
	"aws_kms_replica_key": aws_kms_replica_key,
	"aws_lakeformation_data_lake_settings": aws_lakeformation_data_lake_settings,
	"aws_lakeformation_lf_tag": aws_lakeformation_lf_tag,
	"aws_lakeformation_permissions": aws_lakeformation_permissions,
	"aws_lakeformation_resource": aws_lakeformation_resource,
	"aws_lakeformation_resource_lf_tags": aws_lakeformation_resource_lf_tags,
	"aws_lambda_code_signing_config": aws_lambda_code_signing_config,
	"aws_lambda_function_url": aws_lambda_function_url,
	"aws_lambda_invocation": aws_lambda_invocation,
	"aws_lambda_layer_version_permission": aws_lambda_layer_version_permission,
	"aws_lambda_provisioned_concurrency_config": aws_lambda_provisioned_concurrency_config,
	"aws_lb_cookie_stickiness_policy": aws_lb_cookie_stickiness_policy,
	"aws_lb_listener": aws_lb_listener,
	"aws_lb_listener_certificate": aws_lb_listener_certificate,
	"aws_lb_listener_rule": aws_lb_listener_rule,
	"aws_lb_ssl_negotiation_policy": aws_lb_ssl_negotiation_policy,
	"aws_lb_target_group": aws_lb_target_group,
	"aws_lb_target_group_attachment": aws_lb_target_group_attachment,
	"aws_lb_trust_store": aws_lb_trust_store,
	"aws_lb_trust_store_revocation": aws_lb_trust_store_revocation,
	"aws_lex_bot": aws_lex_bot,
	"aws_lex_bot_alias": aws_lex_bot_alias,
	"aws_lex_intent": aws_lex_intent,
	"aws_lex_slot_type": aws_lex_slot_type,
	"aws_lexv2models_bot": aws_lexv2models_bot,
	"aws_lexv2models_bot_locale": aws_lexv2models_bot_locale,
	"aws_lexv2models_bot_version": aws_lexv2models_bot_version,
	"aws_licensemanager_association": aws_licensemanager_association,
	"aws_licensemanager_grant": aws_licensemanager_grant,
	"aws_licensemanager_grant_accepter": aws_licensemanager_grant_accepter,
	"aws_licensemanager_license_configuration": aws_licensemanager_license_configuration,
	"aws_lightsail_bucket": aws_lightsail_bucket,
	"aws_lightsail_bucket_access_key": aws_lightsail_bucket_access_key,
	"aws_lightsail_bucket_resource_access": aws_lightsail_bucket_resource_access,
	"aws_lightsail_certificate": aws_lightsail_certificate,
	"aws_lightsail_container_service": aws_lightsail_container_service,
	"aws_lightsail_container_service_deployment_version": aws_lightsail_container_service_deployment_version,
	"aws_lightsail_database": aws_lightsail_database,
	"aws_lightsail_disk": aws_lightsail_disk,
	"aws_lightsail_disk_attachment": aws_lightsail_disk_attachment,
	"aws_lightsail_distribution": aws_lightsail_distribution,
	"aws_lightsail_domain": aws_lightsail_domain,
	"aws_lightsail_domain_entry": aws_lightsail_domain_entry,
	"aws_lightsail_instance": aws_lightsail_instance,
	"aws_lightsail_instance_public_ports": aws_lightsail_instance_public_ports,
	"aws_lightsail_key_pair": aws_lightsail_key_pair,
	"aws_lightsail_lb": aws_lightsail_lb,
	"aws_lightsail_lb_attachment": aws_lightsail_lb_attachment,
	"aws_lightsail_lb_certificate": aws_lightsail_lb_certificate,
	"aws_lightsail_lb_certificate_attachment": aws_lightsail_lb_certificate_attachment,
	"aws_lightsail_lb_https_redirection_policy": aws_lightsail_lb_https_redirection_policy,
	"aws_lightsail_lb_stickiness_policy": aws_lightsail_lb_stickiness_policy,
	"aws_lightsail_static_ip": aws_lightsail_static_ip,
	"aws_lightsail_static_ip_attachment": aws_lightsail_static_ip_attachment,
	"aws_load_balancer_backend_server_policy": aws_load_balancer_backend_server_policy,
	"aws_load_balancer_listener_policy": aws_load_balancer_listener_policy,
	"aws_load_balancer_policy": aws_load_balancer_policy,
	"aws_location_geofence_collection": aws_location_geofence_collection,
	"aws_location_map": aws_location_map,
	"aws_location_place_index": aws_location_place_index,
	"aws_location_route_calculator": aws_location_route_calculator,
	"aws_location_tracker": aws_location_tracker,
	"aws_location_tracker_association": aws_location_tracker_association,
	"aws_macie2_account": aws_macie2_account,
	"aws_macie2_classification_export_configuration": aws_macie2_classification_export_configuration,
	"aws_macie2_classification_job": aws_macie2_classification_job,
	"aws_macie2_custom_data_identifier": aws_macie2_custom_data_identifier,
	"aws_macie2_findings_filter": aws_macie2_findings_filter,
	"aws_macie2_invitation_accepter": aws_macie2_invitation_accepter,
	"aws_macie2_member": aws_macie2_member,
	"aws_macie2_organization_admin_account": aws_macie2_organization_admin_account,
	"aws_main_route_table_association": aws_main_route_table_association,
	"aws_media_convert_queue": aws_media_convert_queue,
	"aws_media_package_channel": aws_media_package_channel,
	"aws_media_store_container": aws_media_store_container,
	"aws_media_store_container_policy": aws_media_store_container_policy,
	"aws_medialive_channel": aws_medialive_channel,
	"aws_medialive_input": aws_medialive_input,
	"aws_medialive_input_security_group": aws_medialive_input_security_group,
	"aws_medialive_multiplex": aws_medialive_multiplex,
	"aws_medialive_multiplex_program": aws_medialive_multiplex_program,
	"aws_memorydb_acl": aws_memorydb_acl,
	"aws_memorydb_cluster": aws_memorydb_cluster,
	"aws_memorydb_parameter_group": aws_memorydb_parameter_group,
	"aws_memorydb_snapshot": aws_memorydb_snapshot,
	"aws_memorydb_subnet_group": aws_memorydb_subnet_group,
	"aws_memorydb_user": aws_memorydb_user,
	"aws_mq_broker": aws_mq_broker,
	"aws_mq_configuration": aws_mq_configuration,
	"aws_msk_cluster": aws_msk_cluster,
	"aws_msk_cluster_policy": aws_msk_cluster_policy,
	"aws_msk_configuration": aws_msk_configuration,
	"aws_msk_replicator": aws_msk_replicator,
	"aws_msk_scram_secret_association": aws_msk_scram_secret_association,
	"aws_msk_serverless_cluster": aws_msk_serverless_cluster,
	"aws_msk_vpc_connection": aws_msk_vpc_connection,
	"aws_mskconnect_connector": aws_mskconnect_connector,
	"aws_mskconnect_custom_plugin": aws_mskconnect_custom_plugin,
	"aws_mskconnect_worker_configuration": aws_mskconnect_worker_configuration,
	"aws_mwaa_environment": aws_mwaa_environment,
	"aws_neptune_cluster": aws_neptune_cluster,
	"aws_neptune_cluster_endpoint": aws_neptune_cluster_endpoint,
	"aws_neptune_cluster_instance": aws_neptune_cluster_instance,
	"aws_neptune_cluster_parameter_group": aws_neptune_cluster_parameter_group,
	"aws_neptune_cluster_snapshot": aws_neptune_cluster_snapshot,
	"aws_neptune_event_subscription": aws_neptune_event_subscription,
	"aws_neptune_global_cluster": aws_neptune_global_cluster,
	"aws_neptune_parameter_group": aws_neptune_parameter_group,
	"aws_neptune_subnet_group": aws_neptune_subnet_group,
	"aws_network_acl_association": aws_network_acl_association,
	"aws_network_acl_rule": aws_network_acl_rule,
	"aws_network_interface_attachment": aws_network_interface_attachment,
	"aws_network_interface_sg_attachment": aws_network_interface_sg_attachment,
	"aws_networkfirewall_firewall": aws_networkfirewall_firewall,
	"aws_networkfirewall_firewall_policy": aws_networkfirewall_firewall_policy,
	"aws_networkfirewall_logging_configuration": aws_networkfirewall_logging_configuration,
	"aws_networkfirewall_resource_policy": aws_networkfirewall_resource_policy,
	"aws_networkfirewall_rule_group": aws_networkfirewall_rule_group,
	"aws_networkmanager_attachment_accepter": aws_networkmanager_attachment_accepter,
	"aws_networkmanager_connect_attachment": aws_networkmanager_connect_attachment,
	"aws_networkmanager_connect_peer": aws_networkmanager_connect_peer,
	"aws_networkmanager_connection": aws_networkmanager_connection,
	"aws_networkmanager_core_network": aws_networkmanager_core_network,
	"aws_networkmanager_core_network_policy_attachment": aws_networkmanager_core_network_policy_attachment,
	"aws_networkmanager_customer_gateway_association": aws_networkmanager_customer_gateway_association,
	"aws_networkmanager_device": aws_networkmanager_device,
	"aws_networkmanager_global_network": aws_networkmanager_global_network,
	"aws_networkmanager_link": aws_networkmanager_link,
	"aws_networkmanager_link_association": aws_networkmanager_link_association,
	"aws_networkmanager_site": aws_networkmanager_site,
	"aws_networkmanager_site_to_site_vpn_attachment": aws_networkmanager_site_to_site_vpn_attachment,
	"aws_networkmanager_transit_gateway_connect_peer_association": aws_networkmanager_transit_gateway_connect_peer_association,
	"aws_networkmanager_transit_gateway_peering": aws_networkmanager_transit_gateway_peering,
	"aws_networkmanager_transit_gateway_registration": aws_networkmanager_transit_gateway_registration,
	"aws_networkmanager_transit_gateway_route_table_attachment": aws_networkmanager_transit_gateway_route_table_attachment,
	"aws_networkmanager_vpc_attachment": aws_networkmanager_vpc_attachment,
	"aws_oam_link": aws_oam_link,
	"aws_oam_sink": aws_oam_sink,
	"aws_oam_sink_policy": aws_oam_sink_policy,
	"aws_opensearch_domain": aws_opensearch_domain,
	"aws_opensearch_domain_policy": aws_opensearch_domain_policy,
	"aws_opensearch_domain_saml_options": aws_opensearch_domain_saml_options,
	"aws_opensearch_inbound_connection_accepter": aws_opensearch_inbound_connection_accepter,
	"aws_opensearch_outbound_connection": aws_opensearch_outbound_connection,
	"aws_opensearch_package": aws_opensearch_package,
	"aws_opensearch_package_association": aws_opensearch_package_association,
	"aws_opensearch_vpc_endpoint": aws_opensearch_vpc_endpoint,
	"aws_opensearchserverless_access_policy": aws_opensearchserverless_access_policy,
	"aws_opensearchserverless_collection": aws_opensearchserverless_collection,
	"aws_opensearchserverless_lifecycle_policy": aws_opensearchserverless_lifecycle_policy,
	"aws_opensearchserverless_security_config": aws_opensearchserverless_security_config,
	"aws_opensearchserverless_security_policy": aws_opensearchserverless_security_policy,
	"aws_opensearchserverless_vpc_endpoint": aws_opensearchserverless_vpc_endpoint,
	"aws_opsworks_application": aws_opsworks_application,
	"aws_opsworks_custom_layer": aws_opsworks_custom_layer,
	"aws_opsworks_ecs_cluster_layer": aws_opsworks_ecs_cluster_layer,
	"aws_opsworks_ganglia_layer": aws_opsworks_ganglia_layer,
	"aws_opsworks_haproxy_layer": aws_opsworks_haproxy_layer,
	"aws_opsworks_instance": aws_opsworks_instance,
	"aws_opsworks_java_app_layer": aws_opsworks_java_app_layer,
	"aws_opsworks_memcached_layer": aws_opsworks_memcached_layer,
	"aws_opsworks_mysql_layer": aws_opsworks_mysql_layer,
	"aws_opsworks_nodejs_app_layer": aws_opsworks_nodejs_app_layer,
	"aws_opsworks_permission": aws_opsworks_permission,
	"aws_opsworks_php_app_layer": aws_opsworks_php_app_layer,
	"aws_opsworks_rails_app_layer": aws_opsworks_rails_app_layer,
	"aws_opsworks_rds_db_instance": aws_opsworks_rds_db_instance,
	"aws_opsworks_stack": aws_opsworks_stack,
	"aws_opsworks_static_web_layer": aws_opsworks_static_web_layer,
	"aws_opsworks_user_profile": aws_opsworks_user_profile,
	"aws_organizations_account": aws_organizations_account,
	"aws_organizations_delegated_administrator": aws_organizations_delegated_administrator,
	"aws_organizations_organization": aws_organizations_organization,
	"aws_organizations_organizational_unit": aws_organizations_organizational_unit,
	"aws_organizations_policy": aws_organizations_policy,
	"aws_organizations_policy_attachment": aws_organizations_policy_attachment,
	"aws_organizations_resource_policy": aws_organizations_resource_policy,
	"aws_pinpoint_adm_channel": aws_pinpoint_adm_channel,
	"aws_pinpoint_apns_channel": aws_pinpoint_apns_channel,
	"aws_pinpoint_apns_sandbox_channel": aws_pinpoint_apns_sandbox_channel,
	"aws_pinpoint_apns_voip_channel": aws_pinpoint_apns_voip_channel,
	"aws_pinpoint_apns_voip_sandbox_channel": aws_pinpoint_apns_voip_sandbox_channel,
	"aws_pinpoint_app": aws_pinpoint_app,
	"aws_pinpoint_baidu_channel": aws_pinpoint_baidu_channel,
	"aws_pinpoint_email_channel": aws_pinpoint_email_channel,
	"aws_pinpoint_event_stream": aws_pinpoint_event_stream,
	"aws_pinpoint_gcm_channel": aws_pinpoint_gcm_channel,
	"aws_pinpoint_sms_channel": aws_pinpoint_sms_channel,
	"aws_pipes_pipe": aws_pipes_pipe,
	"aws_placement_group": aws_placement_group,
	"aws_prometheus_alert_manager_definition": aws_prometheus_alert_manager_definition,
	"aws_prometheus_rule_group_namespace": aws_prometheus_rule_group_namespace,
	"aws_prometheus_workspace": aws_prometheus_workspace,
	"aws_proxy_protocol_policy": aws_proxy_protocol_policy,
	"aws_qldb_ledger": aws_qldb_ledger,
	"aws_qldb_stream": aws_qldb_stream,
	"aws_quicksight_account_subscription": aws_quicksight_account_subscription,
	"aws_quicksight_analysis": aws_quicksight_analysis,
	"aws_quicksight_dashboard": aws_quicksight_dashboard,
	"aws_quicksight_data_set": aws_quicksight_data_set,
	"aws_quicksight_data_source": aws_quicksight_data_source,
	"aws_quicksight_folder": aws_quicksight_folder,
	"aws_quicksight_folder_membership": aws_quicksight_folder_membership,
	"aws_quicksight_group": aws_quicksight_group,
	"aws_quicksight_group_membership": aws_quicksight_group_membership,
	"aws_quicksight_iam_policy_assignment": aws_quicksight_iam_policy_assignment,
	"aws_quicksight_ingestion": aws_quicksight_ingestion,
	"aws_quicksight_namespace": aws_quicksight_namespace,
	"aws_quicksight_refresh_schedule": aws_quicksight_refresh_schedule,
	"aws_quicksight_template": aws_quicksight_template,
	"aws_quicksight_template_alias": aws_quicksight_template_alias,
	"aws_quicksight_theme": aws_quicksight_theme,
	"aws_quicksight_user": aws_quicksight_user,
	"aws_quicksight_vpc_connection": aws_quicksight_vpc_connection,
	"aws_ram_principal_association": aws_ram_principal_association,
	"aws_ram_resource_association": aws_ram_resource_association,
	"aws_ram_resource_share": aws_ram_resource_share,
	"aws_ram_resource_share_accepter": aws_ram_resource_share_accepter,
	"aws_ram_sharing_with_organization": aws_ram_sharing_with_organization,
	"aws_rbin_rule": aws_rbin_rule,
	"aws_rds_cluster_activity_stream": aws_rds_cluster_activity_stream,
	"aws_rds_cluster_endpoint": aws_rds_cluster_endpoint,
	"aws_rds_cluster_role_association": aws_rds_cluster_role_association,
	"aws_rds_custom_db_engine_version": aws_rds_custom_db_engine_version,
	"aws_rds_export_task": aws_rds_export_task,
	"aws_rds_global_cluster": aws_rds_global_cluster,
	"aws_rds_reserved_instance": aws_rds_reserved_instance,
	"aws_redshift_authentication_profile": aws_redshift_authentication_profile,
	"aws_redshift_cluster_iam_roles": aws_redshift_cluster_iam_roles,
	"aws_redshift_cluster_snapshot": aws_redshift_cluster_snapshot,
	"aws_redshift_endpoint_access": aws_redshift_endpoint_access,
	"aws_redshift_endpoint_authorization": aws_redshift_endpoint_authorization,
	"aws_redshift_event_subscription": aws_redshift_event_subscription,
	"aws_redshift_hsm_client_certificate": aws_redshift_hsm_client_certificate,
	"aws_redshift_hsm_configuration": aws_redshift_hsm_configuration,
	"aws_redshift_partner": aws_redshift_partner,
	"aws_redshift_resource_policy": aws_redshift_resource_policy,
	"aws_redshift_scheduled_action": aws_redshift_scheduled_action,
	"aws_redshift_snapshot_copy_grant": aws_redshift_snapshot_copy_grant,
	"aws_redshift_snapshot_schedule": aws_redshift_snapshot_schedule,
	"aws_redshift_snapshot_schedule_association": aws_redshift_snapshot_schedule_association,
	"aws_redshift_usage_limit": aws_redshift_usage_limit,
	"aws_redshiftdata_statement": aws_redshiftdata_statement,
	"aws_redshiftserverless_endpoint_access": aws_redshiftserverless_endpoint_access,
	"aws_redshiftserverless_resource_policy": aws_redshiftserverless_resource_policy,
	"aws_redshiftserverless_snapshot": aws_redshiftserverless_snapshot,
	"aws_redshiftserverless_usage_limit": aws_redshiftserverless_usage_limit,
	"aws_resourceexplorer2_index": aws_resourceexplorer2_index,
	"aws_resourceexplorer2_view": aws_resourceexplorer2_view,
	"aws_resourcegroups_group": aws_resourcegroups_group,
	"aws_resourcegroups_resource": aws_resourcegroups_resource,
	"aws_rolesanywhere_profile": aws_rolesanywhere_profile,
	"aws_rolesanywhere_trust_anchor": aws_rolesanywhere_trust_anchor,
	"aws_route": aws_route,
	"aws_route53_cidr_collection": aws_route53_cidr_collection,
	"aws_route53_cidr_location": aws_route53_cidr_location,
	"aws_route53_delegation_set": aws_route53_delegation_set,
	"aws_route53_health_check": aws_route53_health_check,
	"aws_route53_hosted_zone_dnssec": aws_route53_hosted_zone_dnssec,
	"aws_route53_key_signing_key": aws_route53_key_signing_key,
	"aws_route53_query_log": aws_route53_query_log,
	"aws_route53_record": aws_route53_record,
	"aws_route53_resolver_config": aws_route53_resolver_config,
	"aws_route53_resolver_dnssec_config": aws_route53_resolver_dnssec_config,
	"aws_route53_resolver_endpoint": aws_route53_resolver_endpoint,
	"aws_route53_resolver_firewall_config": aws_route53_resolver_firewall_config,
	"aws_route53_resolver_firewall_domain_list": aws_route53_resolver_firewall_domain_list,
	"aws_route53_resolver_firewall_rule": aws_route53_resolver_firewall_rule,
	"aws_route53_resolver_firewall_rule_group": aws_route53_resolver_firewall_rule_group,
	"aws_route53_resolver_query_log_config": aws_route53_resolver_query_log_config,
	"aws_route53_resolver_query_log_config_association": aws_route53_resolver_query_log_config_association,
	"aws_route53_resolver_rule": aws_route53_resolver_rule,
	"aws_route53_resolver_rule_association": aws_route53_resolver_rule_association,
	"aws_route53_traffic_policy": aws_route53_traffic_policy,
	"aws_route53_traffic_policy_instance": aws_route53_traffic_policy_instance,
	"aws_route53_vpc_association_authorization": aws_route53_vpc_association_authorization,
	"aws_route53_zone": aws_route53_zone,
	"aws_route53_zone_association": aws_route53_zone_association,
	"aws_route53domains_registered_domain": aws_route53domains_registered_domain,
	"aws_route53recoverycontrolconfig_cluster": aws_route53recoverycontrolconfig_cluster,
	"aws_route53recoverycontrolconfig_control_panel": aws_route53recoverycontrolconfig_control_panel,
	"aws_route53recoverycontrolconfig_routing_control": aws_route53recoverycontrolconfig_routing_control,
	"aws_route53recoverycontrolconfig_safety_rule": aws_route53recoverycontrolconfig_safety_rule,
	"aws_route53recoveryreadiness_cell": aws_route53recoveryreadiness_cell,
	"aws_route53recoveryreadiness_readiness_check": aws_route53recoveryreadiness_readiness_check,
	"aws_route53recoveryreadiness_recovery_group": aws_route53recoveryreadiness_recovery_group,
	"aws_route53recoveryreadiness_resource_set": aws_route53recoveryreadiness_resource_set,
	"aws_rum_app_monitor": aws_rum_app_monitor,
	"aws_rum_metrics_destination": aws_rum_metrics_destination,
	"aws_s3_access_point": aws_s3_access_point,
	"aws_s3_account_public_access_block": aws_s3_account_public_access_block,
	"aws_s3_bucket": aws_s3_bucket,
	"aws_s3_bucket_accelerate_configuration": aws_s3_bucket_accelerate_configuration,
	"aws_s3_bucket_acl": aws_s3_bucket_acl,
	"aws_s3_bucket_analytics_configuration": aws_s3_bucket_analytics_configuration,
	"aws_s3_bucket_cors_configuration": aws_s3_bucket_cors_configuration,
	"aws_s3_bucket_intelligent_tiering_configuration": aws_s3_bucket_intelligent_tiering_configuration,
	"aws_s3_bucket_inventory": aws_s3_bucket_inventory,
	"aws_s3_bucket_lifecycle_configuration": aws_s3_bucket_lifecycle_configuration,
	"aws_s3_bucket_logging": aws_s3_bucket_logging,
	"aws_s3_bucket_metric": aws_s3_bucket_metric,
	"aws_s3_bucket_notification": aws_s3_bucket_notification,
	"aws_s3_bucket_object": aws_s3_bucket_object,
	"aws_s3_bucket_object_lock_configuration": aws_s3_bucket_object_lock_configuration,
	"aws_s3_bucket_ownership_controls": aws_s3_bucket_ownership_controls,
	"aws_s3_bucket_policy": aws_s3_bucket_policy,
	"aws_s3_bucket_public_access_block": aws_s3_bucket_public_access_block,
	"aws_s3_bucket_replication_configuration": aws_s3_bucket_replication_configuration,
	"aws_s3_bucket_request_payment_configuration": aws_s3_bucket_request_payment_configuration,
	"aws_s3_bucket_server_side_encryption_configuration": aws_s3_bucket_server_side_encryption_configuration,
	"aws_s3_bucket_versioning": aws_s3_bucket_versioning,
	"aws_s3_bucket_website_configuration": aws_s3_bucket_website_configuration,
	"aws_s3_directory_bucket": aws_s3_directory_bucket,
	"aws_s3_object": aws_s3_object,
	"aws_s3_object_copy": aws_s3_object_copy,
	"aws_s3control_access_grant": aws_s3control_access_grant,
	"aws_s3control_access_grants_instance": aws_s3control_access_grants_instance,
	"aws_s3control_access_grants_instance_resource_policy": aws_s3control_access_grants_instance_resource_policy,
	"aws_s3control_access_grants_location": aws_s3control_access_grants_location,
	"aws_s3control_access_point_policy": aws_s3control_access_point_policy,
	"aws_s3control_bucket": aws_s3control_bucket,
	"aws_s3control_bucket_lifecycle_configuration": aws_s3control_bucket_lifecycle_configuration,
	"aws_s3control_bucket_policy": aws_s3control_bucket_policy,
	"aws_s3control_multi_region_access_point": aws_s3control_multi_region_access_point,
	"aws_s3control_multi_region_access_point_policy": aws_s3control_multi_region_access_point_policy,
	"aws_s3control_object_lambda_access_point": aws_s3control_object_lambda_access_point,
	"aws_s3control_object_lambda_access_point_policy": aws_s3control_object_lambda_access_point_policy,
	"aws_s3control_storage_lens_configuration": aws_s3control_storage_lens_configuration,
	"aws_s3outposts_endpoint": aws_s3outposts_endpoint,
	"aws_sagemaker_app": aws_sagemaker_app,
	"aws_sagemaker_app_image_config": aws_sagemaker_app_image_config,
	"aws_sagemaker_code_repository": aws_sagemaker_code_repository,
	"aws_sagemaker_data_quality_job_definition": aws_sagemaker_data_quality_job_definition,
	"aws_sagemaker_device": aws_sagemaker_device,
	"aws_sagemaker_device_fleet": aws_sagemaker_device_fleet,
	"aws_sagemaker_domain": aws_sagemaker_domain,
	"aws_sagemaker_endpoint": aws_sagemaker_endpoint,
	"aws_sagemaker_endpoint_configuration": aws_sagemaker_endpoint_configuration,
	"aws_sagemaker_feature_group": aws_sagemaker_feature_group,
	"aws_sagemaker_flow_definition": aws_sagemaker_flow_definition,
	"aws_sagemaker_human_task_ui": aws_sagemaker_human_task_ui,
	"aws_sagemaker_image": aws_sagemaker_image,
	"aws_sagemaker_image_version": aws_sagemaker_image_version,
	"aws_sagemaker_model": aws_sagemaker_model,
	"aws_sagemaker_model_package_group": aws_sagemaker_model_package_group,
	"aws_sagemaker_model_package_group_policy": aws_sagemaker_model_package_group_policy,
	"aws_sagemaker_monitoring_schedule": aws_sagemaker_monitoring_schedule,
	"aws_sagemaker_notebook_instance": aws_sagemaker_notebook_instance,
	"aws_sagemaker_notebook_instance_lifecycle_configuration": aws_sagemaker_notebook_instance_lifecycle_configuration,
	"aws_sagemaker_pipeline": aws_sagemaker_pipeline,
	"aws_sagemaker_project": aws_sagemaker_project,
	"aws_sagemaker_servicecatalog_portfolio_status": aws_sagemaker_servicecatalog_portfolio_status,
	"aws_sagemaker_space": aws_sagemaker_space,
	"aws_sagemaker_studio_lifecycle_config": aws_sagemaker_studio_lifecycle_config,
	"aws_sagemaker_user_profile": aws_sagemaker_user_profile,
	"aws_sagemaker_workforce": aws_sagemaker_workforce,
	"aws_sagemaker_workteam": aws_sagemaker_workteam,
	"aws_scheduler_schedule": aws_scheduler_schedule,
	"aws_scheduler_schedule_group": aws_scheduler_schedule_group,
	"aws_schemas_discoverer": aws_schemas_discoverer,
	"aws_schemas_registry": aws_schemas_registry,
	"aws_schemas_registry_policy": aws_schemas_registry_policy,
	"aws_schemas_schema": aws_schemas_schema,
	"aws_secretsmanager_secret_policy": aws_secretsmanager_secret_policy,
	"aws_secretsmanager_secret_rotation": aws_secretsmanager_secret_rotation,
	"aws_secretsmanager_secret_version": aws_secretsmanager_secret_version,
	"aws_security_group_rule": aws_security_group_rule,
	"aws_securityhub_account": aws_securityhub_account,
	"aws_securityhub_action_target": aws_securityhub_action_target,
	"aws_securityhub_finding_aggregator": aws_securityhub_finding_aggregator,
	"aws_securityhub_insight": aws_securityhub_insight,
	"aws_securityhub_invite_accepter": aws_securityhub_invite_accepter,
	"aws_securityhub_member": aws_securityhub_member,
	"aws_securityhub_organization_admin_account": aws_securityhub_organization_admin_account,
	"aws_securityhub_organization_configuration": aws_securityhub_organization_configuration,
	"aws_securityhub_product_subscription": aws_securityhub_product_subscription,
	"aws_securityhub_standards_control": aws_securityhub_standards_control,
	"aws_securityhub_standards_subscription": aws_securityhub_standards_subscription,
	"aws_securitylake_data_lake": aws_securitylake_data_lake,
	"aws_serverlessapplicationrepository_cloudformation_stack": aws_serverlessapplicationrepository_cloudformation_stack,
	"aws_service_discovery_http_namespace": aws_service_discovery_http_namespace,
	"aws_service_discovery_instance": aws_service_discovery_instance,
	"aws_service_discovery_private_dns_namespace": aws_service_discovery_private_dns_namespace,
	"aws_service_discovery_public_dns_namespace": aws_service_discovery_public_dns_namespace,
	"aws_service_discovery_service": aws_service_discovery_service,
	"aws_servicecatalog_budget_resource_association": aws_servicecatalog_budget_resource_association,
	"aws_servicecatalog_constraint": aws_servicecatalog_constraint,
	"aws_servicecatalog_organizations_access": aws_servicecatalog_organizations_access,
	"aws_servicecatalog_portfolio": aws_servicecatalog_portfolio,
	"aws_servicecatalog_portfolio_share": aws_servicecatalog_portfolio_share,
	"aws_servicecatalog_principal_portfolio_association": aws_servicecatalog_principal_portfolio_association,
	"aws_servicecatalog_product": aws_servicecatalog_product,
	"aws_servicecatalog_product_portfolio_association": aws_servicecatalog_product_portfolio_association,
	"aws_servicecatalog_provisioned_product": aws_servicecatalog_provisioned_product,
	"aws_servicecatalog_provisioning_artifact": aws_servicecatalog_provisioning_artifact,
	"aws_servicecatalog_service_action": aws_servicecatalog_service_action,
	"aws_servicecatalog_tag_option": aws_servicecatalog_tag_option,
	"aws_servicecatalog_tag_option_resource_association": aws_servicecatalog_tag_option_resource_association,
	"aws_servicequotas_service_quota": aws_servicequotas_service_quota,
	"aws_servicequotas_template": aws_servicequotas_template,
	"aws_servicequotas_template_association": aws_servicequotas_template_association,
	"aws_ses_active_receipt_rule_set": aws_ses_active_receipt_rule_set,
	"aws_ses_configuration_set": aws_ses_configuration_set,
	"aws_ses_domain_dkim": aws_ses_domain_dkim,
	"aws_ses_domain_identity": aws_ses_domain_identity,
	"aws_ses_domain_identity_verification": aws_ses_domain_identity_verification,
	"aws_ses_domain_mail_from": aws_ses_domain_mail_from,
	"aws_ses_email_identity": aws_ses_email_identity,
	"aws_ses_event_destination": aws_ses_event_destination,
	"aws_ses_identity_notification_topic": aws_ses_identity_notification_topic,
	"aws_ses_identity_policy": aws_ses_identity_policy,
	"aws_ses_receipt_filter": aws_ses_receipt_filter,
	"aws_ses_receipt_rule": aws_ses_receipt_rule,
	"aws_ses_receipt_rule_set": aws_ses_receipt_rule_set,
	"aws_ses_template": aws_ses_template,
	"aws_sesv2_account_vdm_attributes": aws_sesv2_account_vdm_attributes,
	"aws_sesv2_configuration_set": aws_sesv2_configuration_set,
	"aws_sesv2_configuration_set_event_destination": aws_sesv2_configuration_set_event_destination,
	"aws_sesv2_contact_list": aws_sesv2_contact_list,
	"aws_sesv2_dedicated_ip_assignment": aws_sesv2_dedicated_ip_assignment,
	"aws_sesv2_dedicated_ip_pool": aws_sesv2_dedicated_ip_pool,
	"aws_sesv2_email_identity": aws_sesv2_email_identity,
	"aws_sesv2_email_identity_feedback_attributes": aws_sesv2_email_identity_feedback_attributes,
	"aws_sesv2_email_identity_mail_from_attributes": aws_sesv2_email_identity_mail_from_attributes,
	"aws_sfn_activity": aws_sfn_activity,
	"aws_sfn_alias": aws_sfn_alias,
	"aws_sfn_state_machine": aws_sfn_state_machine,
	"aws_shield_application_layer_automatic_response": aws_shield_application_layer_automatic_response,
	"aws_shield_drt_access_log_bucket_association": aws_shield_drt_access_log_bucket_association,
	"aws_shield_drt_access_role_arn_association": aws_shield_drt_access_role_arn_association,
	"aws_shield_protection": aws_shield_protection,
	"aws_shield_protection_group": aws_shield_protection_group,
	"aws_shield_protection_health_check_association": aws_shield_protection_health_check_association,
	"aws_signer_signing_job": aws_signer_signing_job,
	"aws_signer_signing_profile": aws_signer_signing_profile,
	"aws_signer_signing_profile_permission": aws_signer_signing_profile_permission,
	"aws_simpledb_domain": aws_simpledb_domain,
	"aws_snapshot_create_volume_permission": aws_snapshot_create_volume_permission,
	"aws_sns_platform_application": aws_sns_platform_application,
	"aws_sns_sms_preferences": aws_sns_sms_preferences,
	"aws_sns_topic": aws_sns_topic,
	"aws_sns_topic_data_protection_policy": aws_sns_topic_data_protection_policy,
	"aws_sns_topic_policy": aws_sns_topic_policy,
	"aws_sns_topic_subscription": aws_sns_topic_subscription,
	"aws_spot_datafeed_subscription": aws_spot_datafeed_subscription,
	"aws_spot_fleet_request": aws_spot_fleet_request,
	"aws_spot_instance_request": aws_spot_instance_request,
	"aws_sqs_queue": aws_sqs_queue,
	"aws_sqs_queue_policy": aws_sqs_queue_policy,
	"aws_sqs_queue_redrive_allow_policy": aws_sqs_queue_redrive_allow_policy,
	"aws_sqs_queue_redrive_policy": aws_sqs_queue_redrive_policy,
	"aws_ssm_activation": aws_ssm_activation,
	"aws_ssm_association": aws_ssm_association,
	"aws_ssm_default_patch_baseline": aws_ssm_default_patch_baseline,
	"aws_ssm_document": aws_ssm_document,
	"aws_ssm_maintenance_window": aws_ssm_maintenance_window,
	"aws_ssm_maintenance_window_target": aws_ssm_maintenance_window_target,
	"aws_ssm_maintenance_window_task": aws_ssm_maintenance_window_task,
	"aws_ssm_parameter": aws_ssm_parameter,
	"aws_ssm_patch_baseline": aws_ssm_patch_baseline,
	"aws_ssm_patch_group": aws_ssm_patch_group,
	"aws_ssm_resource_data_sync": aws_ssm_resource_data_sync,
	"aws_ssm_service_setting": aws_ssm_service_setting,
	"aws_ssmcontacts_contact": aws_ssmcontacts_contact,
	"aws_ssmcontacts_contact_channel": aws_ssmcontacts_contact_channel,
	"aws_ssmcontacts_plan": aws_ssmcontacts_plan,
	"aws_ssmincidents_replication_set": aws_ssmincidents_replication_set,
	"aws_ssmincidents_response_plan": aws_ssmincidents_response_plan,
	"aws_ssoadmin_account_assignment": aws_ssoadmin_account_assignment,
	"aws_ssoadmin_application": aws_ssoadmin_application,
	"aws_ssoadmin_application_assignment": aws_ssoadmin_application_assignment,
	"aws_ssoadmin_application_assignment_configuration": aws_ssoadmin_application_assignment_configuration,
	"aws_ssoadmin_customer_managed_policy_attachment": aws_ssoadmin_customer_managed_policy_attachment,
	"aws_ssoadmin_instance_access_control_attributes": aws_ssoadmin_instance_access_control_attributes,
	"aws_ssoadmin_managed_policy_attachment": aws_ssoadmin_managed_policy_attachment,
	"aws_ssoadmin_permission_set": aws_ssoadmin_permission_set,
	"aws_ssoadmin_permission_set_inline_policy": aws_ssoadmin_permission_set_inline_policy,
	"aws_ssoadmin_permissions_boundary_attachment": aws_ssoadmin_permissions_boundary_attachment,
	"aws_ssoadmin_trusted_token_issuer": aws_ssoadmin_trusted_token_issuer,
	"aws_storagegateway_cache": aws_storagegateway_cache,
	"aws_storagegateway_cached_iscsi_volume": aws_storagegateway_cached_iscsi_volume,
	"aws_storagegateway_file_system_association": aws_storagegateway_file_system_association,
	"aws_storagegateway_gateway": aws_storagegateway_gateway,
	"aws_storagegateway_nfs_file_share": aws_storagegateway_nfs_file_share,
	"aws_storagegateway_smb_file_share": aws_storagegateway_smb_file_share,
	"aws_storagegateway_stored_iscsi_volume": aws_storagegateway_stored_iscsi_volume,
	"aws_storagegateway_tape_pool": aws_storagegateway_tape_pool,
	"aws_storagegateway_upload_buffer": aws_storagegateway_upload_buffer,
	"aws_storagegateway_working_storage": aws_storagegateway_working_storage,
	"aws_swf_domain": aws_swf_domain,
	"aws_synthetics_canary": aws_synthetics_canary,
	"aws_synthetics_group": aws_synthetics_group,
	"aws_synthetics_group_association": aws_synthetics_group_association,
	"aws_timestreamwrite_database": aws_timestreamwrite_database,
	"aws_timestreamwrite_table": aws_timestreamwrite_table,
	"aws_transcribe_language_model": aws_transcribe_language_model,
	"aws_transcribe_medical_vocabulary": aws_transcribe_medical_vocabulary,
	"aws_transcribe_vocabulary": aws_transcribe_vocabulary,
	"aws_transcribe_vocabulary_filter": aws_transcribe_vocabulary_filter,
	"aws_transfer_access": aws_transfer_access,
	"aws_transfer_agreement": aws_transfer_agreement,
	"aws_transfer_certificate": aws_transfer_certificate,
	"aws_transfer_connector": aws_transfer_connector,
	"aws_transfer_profile": aws_transfer_profile,
	"aws_transfer_server": aws_transfer_server,
	"aws_transfer_ssh_key": aws_transfer_ssh_key,
	"aws_transfer_tag": aws_transfer_tag,
	"aws_transfer_user": aws_transfer_user,
	"aws_transfer_workflow": aws_transfer_workflow,
	"aws_verifiedaccess_endpoint": aws_verifiedaccess_endpoint,
	"aws_verifiedaccess_group": aws_verifiedaccess_group,
	"aws_verifiedaccess_instance": aws_verifiedaccess_instance,
	"aws_verifiedaccess_instance_logging_configuration": aws_verifiedaccess_instance_logging_configuration,
	"aws_verifiedaccess_instance_trust_provider_attachment": aws_verifiedaccess_instance_trust_provider_attachment,
	"aws_verifiedaccess_trust_provider": aws_verifiedaccess_trust_provider,
	"aws_volume_attachment": aws_volume_attachment,
	"aws_vpc_dhcp_options_association": aws_vpc_dhcp_options_association,
	"aws_vpc_endpoint_connection_accepter": aws_vpc_endpoint_connection_accepter,
	"aws_vpc_endpoint_connection_notification": aws_vpc_endpoint_connection_notification,
	"aws_vpc_endpoint_policy": aws_vpc_endpoint_policy,
	"aws_vpc_endpoint_route_table_association": aws_vpc_endpoint_route_table_association,
	"aws_vpc_endpoint_security_group_association": aws_vpc_endpoint_security_group_association,
	"aws_vpc_endpoint_service": aws_vpc_endpoint_service,
	"aws_vpc_endpoint_service_allowed_principal": aws_vpc_endpoint_service_allowed_principal,
	"aws_vpc_endpoint_subnet_association": aws_vpc_endpoint_subnet_association,
	"aws_vpc_ipam": aws_vpc_ipam,
	"aws_vpc_ipam_organization_admin_account": aws_vpc_ipam_organization_admin_account,
	"aws_vpc_ipam_pool": aws_vpc_ipam_pool,
	"aws_vpc_ipam_pool_cidr": aws_vpc_ipam_pool_cidr,
	"aws_vpc_ipam_pool_cidr_allocation": aws_vpc_ipam_pool_cidr_allocation,
	"aws_vpc_ipam_preview_next_cidr": aws_vpc_ipam_preview_next_cidr,
	"aws_vpc_ipam_resource_discovery": aws_vpc_ipam_resource_discovery,
	"aws_vpc_ipam_resource_discovery_association": aws_vpc_ipam_resource_discovery_association,
	"aws_vpc_ipam_scope": aws_vpc_ipam_scope,
	"aws_vpc_ipv6_cidr_block_association": aws_vpc_ipv6_cidr_block_association,
	"aws_vpc_network_performance_metric_subscription": aws_vpc_network_performance_metric_subscription,
	"aws_vpc_peering_connection": aws_vpc_peering_connection,
	"aws_vpc_peering_connection_accepter": aws_vpc_peering_connection_accepter,
	"aws_vpc_peering_connection_options": aws_vpc_peering_connection_options,
	"aws_vpc_security_group_egress_rule": aws_vpc_security_group_egress_rule,
	"aws_vpc_security_group_ingress_rule": aws_vpc_security_group_ingress_rule,
	"aws_vpclattice_target_group_attachment": aws_vpclattice_target_group_attachment,
	"aws_vpn_connection": aws_vpn_connection,
	"aws_vpn_connection_route": aws_vpn_connection_route,
	"aws_vpn_gateway": aws_vpn_gateway,
	"aws_vpn_gateway_attachment": aws_vpn_gateway_attachment,
	"aws_vpn_gateway_route_propagation": aws_vpn_gateway_route_propagation,
	"aws_waf_byte_match_set": aws_waf_byte_match_set,
	"aws_waf_geo_match_set": aws_waf_geo_match_set,
	"aws_waf_ipset": aws_waf_ipset,
	"aws_waf_rate_based_rule": aws_waf_rate_based_rule,
	"aws_waf_regex_match_set": aws_waf_regex_match_set,
	"aws_waf_regex_pattern_set": aws_waf_regex_pattern_set,
	"aws_waf_rule": aws_waf_rule,
	"aws_waf_rule_group": aws_waf_rule_group,
	"aws_waf_size_constraint_set": aws_waf_size_constraint_set,
	"aws_waf_sql_injection_match_set": aws_waf_sql_injection_match_set,
	"aws_waf_web_acl": aws_waf_web_acl,
	"aws_waf_xss_match_set": aws_waf_xss_match_set,
	"aws_wafregional_byte_match_set": aws_wafregional_byte_match_set,
	"aws_wafregional_geo_match_set": aws_wafregional_geo_match_set,
	"aws_wafregional_ipset": aws_wafregional_ipset,
	"aws_wafregional_rate_based_rule": aws_wafregional_rate_based_rule,
	"aws_wafregional_regex_match_set": aws_wafregional_regex_match_set,
	"aws_wafregional_regex_pattern_set": aws_wafregional_regex_pattern_set,
	"aws_wafregional_rule": aws_wafregional_rule,
	"aws_wafregional_rule_group": aws_wafregional_rule_group,
	"aws_wafregional_size_constraint_set": aws_wafregional_size_constraint_set,
	"aws_wafregional_sql_injection_match_set": aws_wafregional_sql_injection_match_set,
	"aws_wafregional_web_acl": aws_wafregional_web_acl,
	"aws_wafregional_web_acl_association": aws_wafregional_web_acl_association,
	"aws_wafregional_xss_match_set": aws_wafregional_xss_match_set,
	"aws_wafv2_ip_set": aws_wafv2_ip_set,
	"aws_wafv2_regex_pattern_set": aws_wafv2_regex_pattern_set,
	"aws_wafv2_rule_group": aws_wafv2_rule_group,
	"aws_wafv2_web_acl": aws_wafv2_web_acl,
	"aws_wafv2_web_acl_association": aws_wafv2_web_acl_association,
	"aws_wafv2_web_acl_logging_configuration": aws_wafv2_web_acl_logging_configuration,
	"aws_worklink_fleet": aws_worklink_fleet,
	"aws_worklink_website_certificate_authority_association": aws_worklink_website_certificate_authority_association,
	"aws_workspaces_connection_alias": aws_workspaces_connection_alias,
	"aws_workspaces_directory": aws_workspaces_directory,
	"aws_workspaces_ip_group": aws_workspaces_ip_group,
	"aws_workspaces_workspace": aws_workspaces_workspace,
	"aws_xray_encryption_config": aws_xray_encryption_config,
	"aws_xray_group": aws_xray_group,
	"aws_xray_sampling_rule": aws_xray_sampling_rule
}

