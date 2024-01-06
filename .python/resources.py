def resource_types(type):
    if type == "net":
        #net=["aws_vpc","aws_subnet","aws_route_table"]
        net=["aws_vpc","aws_vpc_dhcp_options","aws_subnet","aws_internet_gateway","aws_nat_gateway","aws_route_table","aws_route_table_association","aws_vpc_endpoint","aws_security_group"]
        # call aws_route_table_association from subnet and igw
        return net
    elif type == "iam": return ["aws_iam_role","aws_iam_policy"]
    #elif type == "iam": return ["aws_iam_policy"]
    #
    # "aws_iam_role_policy_attachment" - called from iam_role
    #
    #elif type == "iam": return ["aws_iam_role","aws_iam_role_policy_attachment","aws_iam_policy"]
    #elif type == "iam": return ["aws_iam_role","aws_iam_role_policy","aws_iam_policy","aws_iam_role_policy_attachment"]
    elif type == "lattice": return ["aws_vpclattice_service_network"]
    elif type == "eks": return ["aws_eks_cluster"]
    elif type == "kms": return ["aws_kms_key"]

    elif type =="test": return ["aws_api_gateway_resource","aws_api_gateway_rest_api" \
    ,"aws_appautoscaling_policy","aws_appautoscaling_target" \
    ,"aws_appmesh_gateway_route","aws_appmesh_mesh","aws_appmesh_route","aws_appmesh_virtual_gateway"\
    ,"aws_appmesh_virtual_node","aws_appmesh_virtual_router","aws_appmesh_virtual_service", \
    "aws_appstream_fleet","aws_appstream_image_builder","aws_appstream_stack","aws_appstream_user" \
    ,"aws_athena_named_query","aws_athena_workgroup" \
    ,"aws_autoscaling_group","aws_autoscaling_lifecycle_hook" \
    ,"aws_cloud9_environment_ec2" \
    ,"aws_cloudformation_stack","aws_cloudfront_distribution" \
    ,"aws_cloudtrail"\
    ,"aws_cloudwatch_event_bus","aws_cloudwatch_event_rule","aws_cloudwatch_event_target"\
    ,"aws_cloudwatch_log_group","aws_cloudwatch_metric_alarm"\
    ,"aws_codeartifact_domain","aws_codeartifact_repository","aws_codebuild_project"\
    ,"aws_codecommit_repository","aws_codepipeline"\
    ,"aws_codestarnotifications_notification_rule"\
    ,"aws_cognito_identity_pool","aws_cognito_identity_pool_roles_attachment"\
    ,"aws_cognito_user_pool","aws_cognito_user_pool_client","aws_config_config_rule"\
    ,"aws_config_configuration_recorder","aws_config_configuration_recorder_status"\
    ,"aws_config_delivery_channel"\
    ,"aws_customer_gateway"\
    ,"aws_db_event_subscription","aws_db_instance","aws_db_parameter_group","aws_db_subnet_group"\
    ,"aws_default_network_acl"\
    ,"aws_directory_service_directory","aws_dms_endpoint","aws_dms_replication_instance","aws_dms_replication_task"\
    ,"aws_dynamodb_table"\
    ,"aws_ec2_client_vpn_endpoint","aws_ec2_client_vpn_network_association","aws_ec2_host"\
    ,"aws_ec2_transit_gateway","aws_ec2_transit_gateway_route","aws_ec2_transit_gateway_route_table"\
    ,"aws_ec2_transit_gateway_vpc_attachment"\
    ,"aws_ec2_transit_gateway_vpn_attachment"\
    ,"aws_ecr_repository"\
    ,"aws_ecs_capacity_provider","aws_ecs_cluster","aws_ecs_cluster_capacity_providers"\
    ,"aws_ecs_service","aws_ecs_task_definition"\
    ,"aws_efs_access_point","aws_efs_file_system","aws_efs_file_system_policy","aws_efs_mount_target"\
    ,"aws_eip"\
    ,"aws_eks_cluster","aws_eks_fargate_profile","aws_eks_identity_provider_config","aws_eks_node_group"\
    ,"aws_emr_cluster","aws_emr_instance_group","aws_emr_managed_scaling_policy","aws_emr_security_configuration"\
    ,"aws_flow_log"\
    ,"aws_glue_catalog_database","aws_glue_catalog_table","aws_glue_connection","aws_glue_crawler"\
    ,"aws_glue_job","aws_glue_partition","aws_iam_access_key","aws_iam_group","aws_iam_instance_profile"\
    ,"aws_iam_policy","aws_iam_role","aws_iam_role_policy","aws_iam_role_policy_attachment"\
    ,"aws_iam_service_linked_role","aws_iam_user","aws_iam_user_group_membership","aws_iam_user_policy_attachment"\
    ,"aws_instance"\
    ,"aws_internet_gateway"\
    ,"aws_key_pair"\
    ,"aws_kinesis_firehose_delivery_stream","aws_kinesis_stream"\
    ,"aws_kms_alias","aws_kms_key"\
    ,"aws_lakeformation_data_lake_settings","aws_lakeformation_permissions","aws_lakeformation_resource"\
    ,"aws_lambda_alias","aws_lambda_event_source_mapping","aws_lambda_function","aws_lambda_function_event_invoke_config"\
    ,"aws_lambda_layer_version","aws_lambda_permission"\
    ,"aws_launch_configuration","aws_launch_template"\
    ,"aws_lb","aws_lb_listener","aws_lb_listener_rule","aws_lb_target_group"\
    ,"aws_network_acl"\
    ,"aws_network_interface"\
    ,"aws_organizations_account","aws_organizations_organization","aws_organizations_organizational_unit"\
    ,"aws_organizations_policy","aws_organizations_policy_attachment"\
    ,"aws_ram_principal_association","aws_ram_resource_share"\
    ,"aws_rds_cluster","aws_rds_cluster_instance","aws_rds_cluster_parameter_group"\
    ,"aws_redshift_cluster","aws_redshift_subnet_group"\
    ,"aws_route53_zone"\
    ,"aws_s3_access_point"\
    ,"aws_sagemaker_app","aws_sagemaker_app_image_config","aws_sagemaker_domain","aws_sagemaker_image"\
    ,"aws_sagemaker_image_version","aws_sagemaker_model","aws_sagemaker_notebook_instance"\
    ,"aws_sagemaker_studio_lifecycle_config","aws_sagemaker_user_profile"\
    ,"aws_secretsmanager_secret","aws_secretsmanager_secret_version"\
    ,"aws_security_group","aws_security_group_rule"\
    ,"aws_service_discovery_private_dns_namespace","aws_service_discovery_service"\
    ,"aws_servicecatalog_constraint","aws_servicecatalog_portfolio"\
    ,"aws_servicecatalog_principal_portfolio_association","aws_servicecatalog_product"\
    ,"aws_servicecatalog_product_portfolio_association"\
    ,"aws_sfn_state_machine"\
    ,"aws_sns_topic","aws_sns_topic_policy","aws_sns_topic_subscription"\
    ,"aws_spot_fleet_request"\
    ,"aws_sqs_queue"\
    ,"aws_ssm_association","aws_ssm_document","aws_ssm_parameter"\
    ,"aws_ssoadmin_managed_policy_attachment","aws_ssoadmin_permission_set","aws_ssoadmin_permission_set_inline_policy" \
    ,"aws_vpc_endpoint_service"\
    ,"aws_vpc_peering_connection" \
    ,"aws_vpclattice_access_log_subscription","aws_vpclattice_auth_policy" \
    ,"aws_vpclattice_resource_policy" \
    ,"aws_vpclattice_target_group_attachment","aws_vpn_connection"]


    elif type =="done": return ["aws_acm_certificate","aws_api_gateway_resource","aws_api_gateway_rest_api" \
    ,"aws_appautoscaling_policy","aws_appautoscaling_target", \
    "aws_appmesh_gateway_route","aws_appmesh_mesh","aws_appmesh_route","aws_appmesh_virtual_gateway"\
    ,"aws_appmesh_virtual_node","aws_appmesh_virtual_router","aws_appmesh_virtual_service", \
    "aws_appstream_fleet","aws_appstream_image_builder","aws_appstream_stack","aws_appstream_user" \
    ,"aws_athena_named_query","aws_athena_workgroup" \
    ,"aws_autoscaling_group","aws_autoscaling_lifecycle_hook" \
    ,"aws_cloud9_environment_ec2" \
    ,"aws_cloudformation_stack","aws_cloudfront_distribution" \
    ,"aws_cloudtrail"\
    ,"aws_cloudwatch_event_bus","aws_cloudwatch_event_rule","aws_cloudwatch_event_target"\
    ,"aws_cloudwatch_log_group","aws_cloudwatch_metric_alarm"\
    ,"aws_codeartifact_domain","aws_codeartifact_repository","aws_codebuild_project"\
    ,"aws_codecommit_repository","aws_codepipeline"\
    ,"aws_codestarnotifications_notification_rule"\
    ,"aws_cognito_identity_pool","aws_cognito_identity_pool_roles_attachment"\
    ,"aws_cognito_user_pool","aws_cognito_user_pool_client","aws_config_config_rule"\
    ,"aws_config_configuration_recorder","aws_config_configuration_recorder_status"\
    ,"aws_config_delivery_channel"\
    ,"aws_customer_gateway"\
    ,"aws_db_event_subscription","aws_db_instance","aws_db_parameter_group","aws_db_subnet_group"\
    ,"aws_default_network_acl"\
    ,"aws_directory_service_directory","aws_dms_endpoint","aws_dms_replication_instance","aws_dms_replication_task"\
    ,"aws_dynamodb_table"\
    ,"aws_ec2_client_vpn_endpoint","aws_ec2_client_vpn_network_association","aws_ec2_host"\
    ,"aws_ec2_transit_gateway","aws_ec2_transit_gateway_route","aws_ec2_transit_gateway_route_table"\
    ,"aws_ec2_transit_gateway_vpc_attachment"\
    ,"aws_ec2_transit_gateway_vpn_attachment"\
    ,"aws_ecr_repository"\
    ,"aws_ecs_capacity_provider","aws_ecs_cluster","aws_ecs_cluster_capacity_providers"\
    ,"aws_ecs_service","aws_ecs_task_definition"\
    ,"aws_efs_access_point","aws_efs_file_system","aws_efs_file_system_policy","aws_efs_mount_target"\
    ,"aws_eip"\
    ,"aws_eks_cluster","aws_eks_fargate_profile","aws_eks_identity_provider_config","aws_eks_node_group"\
    ,"aws_emr_cluster","aws_emr_instance_group","aws_emr_managed_scaling_policy","aws_emr_security_configuration"\
    ,"aws_flow_log"\
    ,"aws_glue_catalog_database","aws_glue_catalog_table","aws_glue_connection","aws_glue_crawler"\
    ,"aws_glue_job","aws_glue_partition","aws_iam_access_key","aws_iam_group","aws_iam_instance_profile"\
    ,"aws_iam_policy","aws_iam_role","aws_iam_role_policy","aws_iam_role_policy_attachment"\
    ,"aws_iam_service_linked_role","aws_iam_user","aws_iam_user_group_membership","aws_iam_user_policy_attachment"\
    ,"aws_instance"\
    ,"aws_internet_gateway"\
    ,"aws_key_pair"\
    ,"aws_kinesis_firehose_delivery_stream","aws_kinesis_stream"\
    ,"aws_kms_alias","aws_kms_key"\
    ,"aws_lakeformation_data_lake_settings","aws_lakeformation_permissions","aws_lakeformation_resource"\
    ,"aws_lambda_alias","aws_lambda_event_source_mapping","aws_lambda_function","aws_lambda_function_event_invoke_config"\
    ,"aws_lambda_layer_version","aws_lambda_permission"\
    ,"aws_launch_configuration","aws_launch_template"\
    ,"aws_lb","aws_lb_listener","aws_lb_listener_rule","aws_lb_target_group"\
    ,"aws_nat_gateway"\
    ,"aws_network_acl"\
    ,"aws_network_interface"\
    ,"aws_organizations_account","aws_organizations_organization","aws_organizations_organizational_unit"\
    ,"aws_organizations_policy","aws_organizations_policy_attachment"\
    ,"aws_ram_principal_association","aws_ram_resource_share"\
    ,"aws_rds_cluster","aws_rds_cluster_instance","aws_rds_cluster_parameter_group"\
    ,"aws_redshift_cluster","aws_redshift_subnet_group"\
    ,"aws_route53_zone"\
    ,"aws_route_table","aws_route_table_association"\
    ,"aws_s3_access_point"\
    ,"aws_s3_bucket"\
    ,"aws_s3_bucket_acl","aws_s3_bucket_lifecycle_configuration","aws_s3_bucket_logging","aws_s3_bucket_policy"\
    ,"aws_s3_bucket_server_side_encryption_configuration","aws_s3_bucket_versioning","aws_s3_bucket_website_configuration"\
    ,"aws_sagemaker_app","aws_sagemaker_app_image_config","aws_sagemaker_domain","aws_sagemaker_image"\
    ,"aws_sagemaker_image_version","aws_sagemaker_model","aws_sagemaker_notebook_instance"\
    ,"aws_sagemaker_studio_lifecycle_config","aws_sagemaker_user_profile"\
    ,"aws_secretsmanager_secret","aws_secretsmanager_secret_version"\
    ,"aws_security_group","aws_security_group_rule"\
    ,"aws_service_discovery_private_dns_namespace","aws_service_discovery_service"\
    ,"aws_servicecatalog_constraint","aws_servicecatalog_portfolio"\
    ,"aws_servicecatalog_principal_portfolio_association","aws_servicecatalog_product"\
    ,"aws_servicecatalog_product_portfolio_association"\
    ,"aws_sfn_state_machine"\
    ,"aws_sns_topic","aws_sns_topic_policy","aws_sns_topic_subscription"\
    ,"aws_spot_fleet_request"\
    ,"aws_sqs_queue"\
    ,"aws_ssm_association","aws_ssm_document","aws_ssm_parameter"\
    ,"aws_ssoadmin_managed_policy_attachment","aws_ssoadmin_permission_set","aws_ssoadmin_permission_set_inline_policy" \
    ,"aws_vpc","aws_vpc_dhcp_options","aws_vpc_endpoint","aws_vpc_endpoint_service"\
    ,"aws_vpc_ipv4_cidr_block_association","aws_vpc_peering_connection" \
    ,"aws_vpclattice_access_log_subscription","aws_vpclattice_auth_policy","aws_vpclattice_listener"\
    ,"aws_vpclattice_listener_rule","aws_vpclattice_resource_policy","aws_vpclattice_service"\
    ,"aws_vpclattice_service_network","aws_vpclattice_service_network_service_association"\
    ,"aws_vpclattice_service_network_vpc_association","aws_vpclattice_target_group"\
    ,"aws_vpclattice_target_group_attachment","aws_vpn_connection"]

    else:
        same=[type]
        return same


# problematic: "aws_network_acl"
# Error: use the `aws_default_network_acl` resource instead

# 5x returns:
# boto3.client('ec2') - so for example ec2
# the describe function - like describe-vpcs
# from the response -the top level key - like Vpcs
# the primary filter for the API call - either direct to describe call - or as part of filter Name=""
# finally - in the response what the primary id field is vpc-id 

##########################################################################################################

def resource_data(type,id):
    clfn=None;descfn=None;topkey=None;key=None;filterid=None

    if type=="aws_acm_certificate": 
        clfn="acm";descfn="list_certificates";topkey='CertificateSummaryList';key="CertificateArn";filterid=key
        
    elif type == "aws_vpc": 
        clfn="ec2";descfn="describe_vpcs";topkey='Vpcs';key="VpcId";filterid=key
    elif type == "aws_vpc_ipv4_cidr_block_association": 
        clfn="ec2";descfn="describe_vpcs";topkey='Vpcs';key="VpcId";filterid=key
    
    elif type == "aws_vpc_endpoint": 
        clfn="ec2";descfn="describe_vpc_endpoints";topkey="VpcEndpoints";key="VpcEndpointId";filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"
    
    elif type in "aws_subnet":
        clfn="ec2";descfn="describe_subnets";topkey="Subnets";key="SubnetId";filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"

    elif type == "aws_security_group": 
        clfn="ec2";descfn="describe_security_groups";topkey="SecurityGroups";key="GroupId";filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"         

    elif type == "aws_internet_gateway": 
        clfn="ec2";descfn="describe_internet_gateways";topkey="InternetGateways";key="InternetGatewayId";filterid=key
        if id is not None and "vpc-" in id: filterid=".Attachments.0.VpcId"  

    elif type == "aws_nat_gateway": 
        clfn="ec2";descfn="describe_nat_gateways";topkey="NatGateways";key="NatGatewayId";filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"           

    elif type == "aws_network_acl": 
        clfn="ec2";descfn="describe_network_acls";topkey="NetworkAcls";key="NetworkAclId";filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId" 
 
    elif type == "aws_default_network_acl": 
        clfn="ec2";descfn="describe_network_acls";topkey="NetworkAcls";key="NetworkAclId";filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId" 
     
    elif type == "aws_route_table": 
        clfn="ec2";descfn="describe_route_tables";topkey="RouteTables";key="RouteTableId";filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"    

    elif type == "aws_route_table_association":
        clfn="ec2";descfn="describe_route_tables";topkey="RouteTables";key=".Associations.0.SubnetId";filterid=key
        if id is not None and "vpc-" in id: filterid=".Associations.0.VpcId" 
        if id is not None and "subnet-" in id: filterid=".Associations.0.SubnetId" 

    elif type == "aws_default_network_acl": 
        clfn="ec2";descfn="describe_network_acls";topkey="NetworkAcls";key="NetworkAclId";filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"

    elif type == "aws_default_route_table":
        clfn="ec2";descfn="describe_route_tables";topkey="RouteTables";key="RouteTableId";filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"

    elif type == "aws_default_security_group":
        clfn="ec2";descfn="describe_security_groups";topkey="SecurityGroups";key="GroupId";filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"

    elif type == "aws_default_subnet":
        clfn="ec2";descfn="describe_subnets";topkey="Subnets";key="SubnetId";filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"

    elif type == "aws_default_vpc": clfn="ec2";descfn="describe_vpcs";topkey="Vpcs";key="VpcId";filterid=KeyError

    elif type == "aws_default_internet_gateway":
        clfn="ec2";descfn="describe_internet_gateways";topkey="InternetGateways";key="InternetGatewayId";filterid=key
        if id is not None and "vpc-" in id: filterid="attachment.vpc-id"

    elif type == "aws_vpc_dhcp_options": 
        clfn="ec2";descfn="describe_dhcp_options";topkey="DhcpOptions";key="DhcpOptionsId";filterid=""


    elif type == "aws_image":
        clfn="ec2";descfn="describe_images";topkey="Images";key="ImageId";filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"

    elif type == "aws_key_pair":
        clfn="ec2";descfn="describe_key_pairs";topkey="KeyPairs";key="KeyName";filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"

    elif type == "aws_launch_configuration":
        clfn="autoscaling";descfn="describe_launch_configurations";topkey="LaunchConfigurations";key="LaunchConfigurationName";filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"

    elif type == "aws_launch_template":
        clfn="ec2";descfn="describe_launch_templates";topkey="LaunchTemplates";key="LaunchTemplateNames";filterid=key
        if id is not None and "lt-" in id: filterid="LaunchTemplateIds"

    elif type == "aws_vpc_ipv4_cidr_block_association":
        clfn="ec2";descfn="describe_vpc_cidr_block_association_sets";topkey="VpcId";key="AssociationId";filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"

    elif type == "aws_flow_log":
        clfn="ec2";descfn="describe_flow_logs";topkey="FlowLogs";key="FlowLogId";filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"

    elif type == "aws_iam_role":
        clfn="iam";descfn="list_roles";topkey="Roles";key="RoleName";filterid=key
        if id is not None and "arn:aws:iam::" in id: filterid="Arn"

    elif type == "aws_iam_policy":
        clfn="iam";descfn="list_policies";topkey="Policies";key="PolicyName";filterid=key 
        if id is not None and "arn:aws:iam::" in id: filterid="Arn"

    elif type == "aws_iam_role_policy": clfn="iam";descfn="list_role_policies";topkey="PolicyNames";key="PolicyNames";filterid="RoleName"

    elif type == "aws_iam_role_policy_attachment":
        clfn="iam";descfn="list_attached_role_policies";topkey="AttachedPolicies";key="PolicyName";filterid="RoleName" 
        if id is not None: filterid="RoleName"

    elif type == "aws_iam_user":
        clfn="iam";descfn="list_users";topkey="Users";key="UserName";filterid=key 
        if id is not None and "arn:aws:iam::" in id: filterid="Arn"

    elif type == "aws_iam_instance_profile": 
        clfn="iam";descfn="get_instance_profile";topkey="InstanceProfile";key="InstanceProfileName";filterid=key 
        

    ## Lattice
    ##
    elif type == "aws_vpclattice_access_log_subscription":
        clfn="vpc-lattice";descfn="list_access_log_subscriptions";topkey="items";key="id";filterid="name"  
        if id is not None and "sn-" in id: filterid=key 
    ##
    elif type == "aws_vpclattice_auth_policy": 
        clfn="vpc-lattice";descfn="get_auth_policy";topkey="items";key="id";filterid=key 

    elif type == "aws_vpclattice_listener":
        clfn="vpc-lattice";descfn="list_listeners";topkey="items";key="id";filterid="name"  
        if id is not None and "sn-" in id: filterid=key

    elif type == "aws_vpclattice_listener_rule":
        clfn="vpc-lattice";descfn="list_rules";topkey="items";key="id";filterid="name"  
        if id is not None and "sn-" in id: filterid=key
    ##
    elif type == "aws_vpclattice_resource_policy":  
        clfn="vpc-lattice";descfn="list_resource_policies";topkey="items";key="id";filterid="name"  
        if id is not None and "sn-" in id: filterid=key
    ##
    elif type == "aws_vpclattice_service":
        clfn="vpc-lattice"; descfn="list_services";topkey="items";key="id";filterid="name"  # no filter on list-users so use jq like filter
        if id is not None and "sn-" in id: filterid=key
    ##
    elif type == "aws_vpclattice_service_network":
        clfn="vpc-lattice";descfn="list_service_networks";topkey="items";key="id";filterid="name" 
        if id is not None and "sn-" in id: filterid=key
    ##
    elif type == "aws_vpclattice_service_network_service_association":
        clfn="vpc-lattice";descfn="list_service_network_service_associations";topkey="items";key="id";filterid="name"  
        if id is not None and "sn-" in id: filterid=key
    ##
    elif type == "aws_vpclattice_service_network_vpc_association":
        clfn="vpc-lattice";descfn="list_service_network_vpc_associations";topkey="items";key="id";filterid="name"  
        if id is not None and "sn-" in id: filterid=key   

    elif type == "aws_vpclattice_target_group": 
        clfn="vpc-lattice";descfn="list_target_groups";topkey="items";key="id";filterid="name"  
        if id is not None and "tg-" in id: filterid=key

### EKS
    elif type == "aws_eks_cluster": 
        clfn="eks";descfn="list_clusters";topkey="clusters";key="name";filterid=key  
    elif type == "aws_eks_fargate_profile": 
        clfn="eks"; descfn="list_fargate_profiles"; topkey="fargateProfileNames"; key="clusterName";filterid=key  
    elif type == "aws_eks_node_group": 
        clfn="eks";descfn="list_nodegroups";topkey="nodegroups";key="clusterName";filterid=key  
    elif type == "aws_eks_addon": 
        clfn="eks";descfn="list_addons";topkey="addons";key="clusterName";filterid=key  
    elif type == "aws_eks_identity_provider_config": 
        clfn="eks";descfn="list_identity_provider_configs";topkey="identityProviderConfigs";key="clusterName";filterid=key
### KMS
    elif type == "aws_kms_key": 
        clfn="kms";descfn="list_keys";topkey="Keys";key="KeyId";filterid="KeyArn"
    elif type == "aws_kms_alias": 
        clfn="kms";descfn="list_aliases";topkey="Aliases";key="TargetKeyId";filterid="AliasName" 

### ECS

    elif type == "aws_ecs_cluster": 
        clfn="ecs";descfn="list_clusters";topkey="clusterArns";key="clusterArn";filterid=key  
###         

    elif type == "aws_cloudwatch_log_group": 
        clfn="logs";descfn="describe_log_groups";topkey="logGroups";key="logGroupName";filterid=key
    elif type == "aws_config_config_rule": 
        clfn="config";descfn="describe_config_rules";topkey="ConfigRules";key="ConfigRuleName";filterid=key
    elif type == "aws_instance": 
        clfn="ec2";descfn="describe_instances";topkey="Reservations";key="InstanceId";filterid=key
    elif type == "aws_lambda_function": 
        clfn="lambda";descfn="list_functions";topkey="Functions";key="FunctionName";filterid=key
    elif type == "aws_lambda_alias": 
        clfn="lambda";descfn="list_aliases";topkey="Aliases";key="FunctionName";filterid=key
    elif type == "aws_lambda_permission": 
        clfn="lambda";descfn="get_policy";topkey="Policy";key="FunctionName";filterid=key
    elif type == "aws_lambda_layer_version": 
        clfn="lambda";descfn="list_layer_versions";topkey="LayerVersions";key="LayerName";filterid=key
    elif type == "aws_lambda_function_event_invoke_config": 
        clfn="lambda";descfn="list_function_event_invoke_configs";topkey="FunctionEventInvokeConfigs";key="FunctionName";filterid=key
    elif type == "aws_lambda_event_source_mapping": 
        clfn="lambda";descfn="list_event_source_mappings";topkey="EventSourceMappings";key="FunctionName";filterid=key

    elif type == "aws_lb": 
        clfn="elbv2";descfn="describe_load_balancers";topkey="LoadBalancers";key="Names";filterid=key

   

    elif type == "aws_redshiftserverless_workgroup": 
        clfn="redshift-serverless";descfn="get_workgroup";topkey="workgroup";key="workgroupName";filterid=key
    elif type == "aws_redshiftserverless_namespace": 
        clfn="redshift-serverless";descfn="get_namespace";topkey="namespace";key="namespaceName";filterid=key
    elif type == "aws_redshift_cluster": 
        clfn="redshift";descfn="describe_clusters";topkey="Clusters";key="ClusterIdentifier";filterid=key
    elif type == "aws_redshift_subnet_group": 
        clfn="redshift";descfn="describe_cluster_subnet_groups";topkey="ClusterSubnetGroups";key="ClusterSubnetGroupName";filterid=key
    
    elif type == "aws_redshift_parameter_group": 
        clfn="redshift";descfn="describe_cluster_parameter_groups";topkey="ParameterGroups";key="ParameterGroupName";filterid=key
    
    
    elif type == "aws_rds_cluster": 
        clfn="rds";descfn="describe_db_clusters";topkey="DBClusters";key="DBClusterIdentifier";filterid=key
    elif type == "aws_rds_cluster_parameter_group": 
        clfn="rds";descfn="describe_db_cluster_parameter_groups";topkey="DBClusterParameterGroups";key="DBClusterParameterGroupName";filterid=key

    elif type == "aws_rds_cluster_instance": 
        clfn="rds";descfn="describe_db_instances";topkey="DBInstances";key="DBInstanceIdentifier";filterid=key
    
    elif type == "aws_db_parameter_group": 
        clfn="rds";descfn="describe_db_parameter_groups";topkey="DBParameterGroups";key="DBParameterGroupName";filterid=key
    
    elif type == "aws_db_subnet_group": 
        clfn="rds";descfn="describe_db_subnet_groups";topkey="DBSubnetGroups";key="DBSubnetGroupName";filterid=key
    elif type == "aws_db_instance": 
        clfn="rds";descfn="describe_db_instances";topkey="DBInstances";key="DBInstanceIdentifier";filterid=key
    elif type == "aws_db_event_subscription": 
        clfn="rds";descfn="describe_event_subscriptions";topkey="EventSubscriptionsList";key="SubscriptionName";filterid=key
    elif type == "aws_glue_crawler": 
        clfn="glue";descfn="get_crawlers";topkey="Crawlers";key="Name";filterid=key
    elif type == "aws_glue_catalog_database": 
        clfn="glue";descfn="get_databases";topkey="DatabaseList";key="Name";filterid=key

    elif type == "aws_kinesis_stream": 
        clfn="kinesis";descfn="list_streams";topkey="StreamSummaries";key="StreamName";filterid=key
    elif type == "aws_secretsmanager_secret": 
        clfn="secretsmanager";descfn="list_secrets";topkey="SecretList";key="ARN";filterid=key

    elif type == "aws_cloudwatch_event_rule": 
        clfn="events";descfn="list_rules";topkey="Rules";key="Name";filterid=key


## START AUTOGEN: 

    elif type == "aws_accessanalyzer_analyzer":
        clfn="accessanalyzer";descfn="list_analyzers";topkey='AnalyzerList';key="Name";filterid=key
    elif type == "aws_accessanalyzer_archive_rule":
        clfn="accessanalyzer";descfn="list_archive_rules";topkey='ArchiveRules';key="RuleName";filterid=key
    elif type == "aws_account_alternate_contact":
        clfn="organizations";descfn="describe_account";topkey='Account';key="Id";filterid=key
    elif type == "aws_account_primary_contact":
        clfn="organizations";descfn="describe_account";topkey='Account';key="Id";filterid=key
    #elif type == "aws_acm_certificate":
    #    clfn="acm";descfn="list_certificates";topkey='CertificateSummaryList';key="CertificateArn";filterid=key
    elif type == "aws_acm_certificate_validation":
        clfn="acm";descfn="list_certificates";topkey='CertificateSummaryList';key="CertificateArn";filterid=key
    elif type == "aws_acmpca_certificate":
        clfn="acm-pca";descfn="list_certificates";topkey='CertificateAuthorityList';key="Arn";filterid=key
    elif type == "aws_acmpca_certificate_authority":
        clfn="acm-pca";descfn="list_certificate_authorities";topkey='CertificateAuthorities';key="Arn";filterid=key
    elif type == "aws_acmpca_certificate_authority_certificate":
        clfn="acm-pca";descfn="list_certificate_authorities";topkey='CertificateAuthorities';key="Arn";filterid=key
    elif type == "aws_acmpca_permission":
        clfn="acm-pca";descfn="list_permissions";topkey='Permissions';key="Permission";filterid=key
    elif type == "aws_acmpca_policy":
        clfn="acm-pca";descfn="list_policies";topkey='Policies';key="PolicyId";filterid=key
    elif type == "aws_ami":
        clfn="ec2";descfn="describe_images";topkey='Images';key="ImageId";filterid=key
    elif type == "aws_ami_copy":
        clfn="ec2";descfn="describe_images";topkey='Images';key="ImageId";filterid=key
    elif type == "aws_ami_from_instance":
        clfn="ec2";descfn="describe_images";topkey='Images';key="ImageId";filterid=key
    elif type == "aws_ami_launch_permission":
        clfn="ec2";descfn="describe_images";topkey='Images';key="ImageId";filterid=key
    elif type == "aws_amplify_app":
        clfn="amplify";descfn="list_apps";topkey='apps';key="appId";filterid=key
    elif type == "aws_amplify_backend_environment":
        clfn="amplify";descfn="list_backend_environments";topkey='backendEnvironments';key="environmentName";filterid=key
    elif type == "aws_amplify_branch":
        clfn="amplify";descfn="list_branches";topkey='branches';key="branchName";filterid=key
    elif type == "aws_amplify_domain_association":
        clfn="amplify";descfn="list_domain_associations";topkey='domainAssociations';key="domainName";filterid=key
    elif type == "aws_amplify_webhook":
        clfn="amplify";descfn="list_webhooks";topkey='webhooks';key="webhookName";filterid=key
    elif type == "aws_api_gateway_account":
        clfn="apigateway";descfn="get_account";topkey='account';key="cloudwatchRoleArn";filterid=key
    elif type == "aws_api_gateway_api_key":
        clfn="apigateway";descfn="get_api_keys";topkey='items';key="id";filterid=key
    elif type == "aws_api_gateway_authorizer":
        clfn="apigateway";descfn="get_authorizers";topkey='items';key="id";filterid=key
    elif type == "aws_api_gateway_base_path_mapping":
        clfn="apigateway";descfn="get_base_path_mappings";topkey='items';key="id";filterid=key
    elif type == "aws_api_gateway_client_certificate":
        clfn="apigateway";descfn="get_client_certificates";topkey='items';key="clientCertificateId";filterid=key
    elif type == "aws_api_gateway_deployment":
        clfn="apigateway";descfn="get_deployments";topkey='items';key="id";filterid=key
    elif type == "aws_api_gateway_documentation_part":
        clfn="apigateway";descfn="get_documentation_parts";topkey='items';key="id";filterid=key
    elif type == "aws_api_gateway_documentation_version":
        clfn="apigateway";descfn="get_documentation_versions";topkey='items';key="version";filterid=key
    elif type == "aws_api_gateway_domain_name":
        clfn="apigateway";descfn="get_domain_names";topkey='items';key="domainName";filterid=key
    elif type == "aws_api_gateway_gateway_response":
        clfn="apigateway";descfn="get_gateway_responses";topkey='items';key="responseType";filterid=key
    elif type == "aws_api_gateway_integration":
        clfn="apigateway";descfn="get_integrations";topkey='items';key="id";filterid=key
    elif type == "aws_api_gateway_integration_response":
        clfn="apigateway";descfn="get_integration_responses";topkey='items';key="id";filterid=key
    elif type == "aws_api_gateway_method":
        clfn="apigateway";descfn="get_methods";topkey='items';key="httpMethod";filterid=key
    elif type == "aws_api_gateway_method_response":
        clfn="apigateway";descfn="get_method_responses";topkey='items';key="httpMethod";filterid=key
    elif type == "aws_api_gateway_method_settings":
        clfn="apigateway";descfn="get_method_settings";topkey='items';key="httpMethod";filterid=key
    elif type == "aws_api_gateway_model":
        clfn="apigateway";descfn="get_models";topkey='items';key="id";filterid=key
    elif type == "aws_api_gateway_request_validator":
        clfn="apigateway";descfn="get_request_validators";topkey='items';key="id";filterid=key
    elif type == "aws_api_gateway_resource":
        clfn="apigateway";descfn="get_resources";topkey='items';key="id";filterid=key
    elif type == "aws_api_gateway_rest_api":
        clfn="apigateway";descfn="get_rest_apis";topkey='items';key="id";filterid=key
    elif type == "aws_api_gateway_rest_api_policy":
        clfn="apigateway";descfn="get_rest_api_policy";topkey='policy';key="id";filterid=key
    elif type == "aws_api_gateway_stage":
        clfn="apigateway";descfn="get_stages";topkey='items';key="stageName";filterid=key
    elif type == "aws_api_gateway_usage_plan":
        clfn="apigateway";descfn="get_usage_plans";topkey='items';key="id";filterid=key
    elif type == "aws_api_gateway_usage_plan_key":
        clfn="apigateway";descfn="get_usage_plan_keys";topkey='items';key="id";filterid=key
    elif type == "aws_api_gateway_vpc_link":
        clfn="apigateway";descfn="get_vpc_links";topkey='items';key="id";filterid=key
    elif type == "aws_apigatewayv2_api":
        clfn="apigatewayv2";descfn="get_apis";topkey='Items';key="ApiId";filterid=key
    elif type == "aws_apigatewayv2_api_mapping":
        clfn="apigatewayv2";descfn="get_api_mappings";topkey='Items';key="ApiMappingId";filterid=key
    elif type == "aws_apigatewayv2_authorizer":
        clfn="apigatewayv2";descfn="get_authorizers";topkey='Items';key="AuthorizerId";filterid=key
    elif type == "aws_apigatewayv2_deployment":
        clfn="apigatewayv2";descfn="get_deployments";topkey='Items';key="DeploymentId";filterid=key
    elif type == "aws_apigatewayv2_domain_name":
        clfn="apigatewayv2";descfn="get_domain_names";topkey='Items';key="DomainNameId";filterid=key
    elif type == "aws_apigatewayv2_integration":
        clfn="apigatewayv2";descfn="get_integrations";topkey='Items';key="IntegrationId";filterid=key
    elif type == "aws_apigatewayv2_integration_response":
        clfn="apigatewayv2";descfn="get_integration_responses";topkey='Items';key="IntegrationResponseId";filterid=key
    elif type == "aws_apigatewayv2_model":
        clfn="apigatewayv2";descfn="get_models";topkey='Items';key="ModelId";filterid=key
    elif type == "aws_apigatewayv2_route":
        clfn="apigatewayv2";descfn="get_routes";topkey='Items';key="RouteId";filterid=key
    elif type == "aws_apigatewayv2_route_response":
        clfn="apigatewayv2";descfn="get_route_responses";topkey='Items';key="RouteResponseId";filterid=key
    elif type == "aws_apigatewayv2_stage":
        clfn="apigatewayv2";descfn="get_stages";topkey='Items';key="StageName";filterid=key
    elif type == "aws_apigatewayv2_vpc_link":
        clfn="apigatewayv2";descfn="get_vpc_links";topkey='Items';key="VpcLinkId";filterid=key
    elif type == "aws_app_cookie_stickiness_policy":
        clfn="elb";descfn="describe_load_balancers";topkey='LoadBalancerDescriptions';key="AppCookieStickinessPolicyNames";filterid=key
    elif type == "aws_appautoscaling_policy":
        clfn="appautoscaling";descfn="describe_scaling_policies";topkey='ScalingPolicies';key="PolicyName";filterid=key
    elif type == "aws_appautoscaling_scheduled_action":
        clfn="appautoscaling";descfn="describe_scheduled_actions";topkey='ScheduledActions';key="ScheduledActionName";filterid=key
    elif type == "aws_appautoscaling_target":
        clfn="appautoscaling";descfn="describe_scaling_targets";topkey='ScalingTargets';key="ResourceId";filterid=key
    elif type == "aws_appconfig_application":
        clfn="appconfig";descfn="list_applications";topkey='Items';key="Id";filterid=key
    elif type == "aws_appconfig_configuration_profile":
        clfn="appconfig";descfn="list_configuration_profiles";topkey='Items';key="Id";filterid=key
    elif type == "aws_appconfig_deployment":
        clfn="appconfig";descfn="list_deployments";topkey='Items';key="Id";filterid=key
    elif type == "aws_appconfig_deployment_strategy":
        clfn="appconfig";descfn="list_deployment_strategies";topkey='Items';key="Id";filterid=key
    elif type == "aws_appconfig_environment":
        clfn="appconfig";descfn="list_environments";topkey='Items';key="Id";filterid=key
    elif type == "aws_appconfig_extension":
        clfn="appconfig";descfn="list_extensions";topkey='Items';key="Id";filterid=key
    elif type == "aws_appconfig_extension_association":
        clfn="appconfig";descfn="list_extension_associations";topkey='Items';key="Id";filterid=key
    elif type == "aws_appconfig_hosted_configuration_version":
        clfn="appconfig";descfn="list_hosted_configuration_versions";topkey='Items';key="Id";filterid=key
    elif type == "aws_appflow_connector_profile":
        clfn="appflow";descfn="list_connector_profiles";topkey='ConnectorProfileDetailsList';key="ConnectorProfileName";filterid=key
    elif type == "aws_appflow_flow":
        clfn="appflow";descfn="list_flows";topkey='Flows';key="FlowName";filterid=key
    elif type == "aws_appintegrations_data_integration":
        clfn="appintegrations";descfn="list_data_integrations";topkey='DataIntegrations';key="Name";filterid=key
    elif type == "aws_appintegrations_event_integration":
        clfn="appintegrations";descfn="list_event_integrations";topkey='EventIntegrations';key="Name";filterid=key
    elif type == "aws_applicationinsights_application":
        clfn="applicationinsights";descfn="list_applications";topkey='ApplicationInfoList';key="Name";filterid=key
    elif type == "aws_appmesh_gateway_route":
        clfn="appmesh";descfn="list_gateway_routes";topkey='GatewayRoutes';key="GatewayRouteName";filterid=key
    elif type == "aws_appmesh_mesh":
        clfn="appmesh";descfn="list_meshes";topkey='Meshes';key="MeshName";filterid=key
    elif type == "aws_appmesh_route":
        clfn="appmesh";descfn="list_routes";topkey='Routes';key="RouteName";filterid=key
    elif type == "aws_appmesh_virtual_gateway":
        clfn="appmesh";descfn="list_virtual_gateways";topkey='VirtualGateways';key="VirtualGatewayName";filterid=key
    elif type == "aws_appmesh_virtual_node":
        clfn="appmesh";descfn="list_virtual_nodes";topkey='VirtualNodes';key="VirtualNodeName";filterid=key
    elif type == "aws_appmesh_virtual_router":
        clfn="appmesh";descfn="list_virtual_routers";topkey='VirtualRouters';key="VirtualRouterName";filterid=key
    elif type == "aws_appmesh_virtual_service":
        clfn="appmesh";descfn="list_virtual_services";topkey='VirtualServices';key="VirtualServiceName";filterid=key
    elif type == "aws_apprunner_auto_scaling_configuration_version":
        clfn="apprunner";descfn="list_auto_scaling_configuration_versions";topkey='AutoScalingConfigurationVersions';key="AutoScalingConfigurationVersionArn";filterid=key
    elif type == "aws_apprunner_connection":
        clfn="apprunner";descfn="list_connections";topkey='Connections';key="ConnectionArn";filterid=key
    elif type == "aws_apprunner_custom_domain_association":
        clfn="apprunner";descfn="list_custom_domain_associations";topkey='CustomDomainAssociations';key="CustomDomainAssociationArn";filterid=key
    elif type == "aws_apprunner_default_auto_scaling_configuration_version":
        clfn="apprunner";descfn="list_default_auto_scaling_configurations";topkey='DefaultAutoScalingConfigurations';key="DefaultAutoScalingConfigurationArn";filterid=key
    elif type == "aws_apprunner_observability_configuration":
        clfn="apprunner";descfn="list_observability_configurations";topkey='ObservabilityConfigurations';key="ObservabilityConfigurationArn";filterid=key
    elif type == "aws_apprunner_service":
        clfn="apprunner";descfn="list_services";topkey='Services';key="ServiceArn";filterid=key
    elif type == "aws_apprunner_vpc_connector":
        clfn="apprunner";descfn="list_vpc_connectors";topkey='VpcConnectors';key="VpcConnectorArn";filterid=key
    elif type == "aws_apprunner_vpc_ingress_connection":
        clfn="apprunner";descfn="list_vpc_ingress_connections";topkey='VpcIngressConnections';key="VpcIngressConnectionArn";filterid=key
    elif type == "aws_appstream_directory_config":
        clfn="appstream";descfn="list_directory_configs";topkey='DirectoryConfigs';key="DirectoryName";filterid=key
    elif type == "aws_appstream_fleet":
        clfn="appstream";descfn="list_fleets";topkey='Fleets';key="Name";filterid=key
    elif type == "aws_appstream_fleet_stack_association":
        clfn="appstream";descfn="list_fleet_stack_associations";topkey='FleetStackAssociations';key="FleetName";filterid=key
    elif type == "aws_appstream_image_builder":
        clfn="appstream";descfn="list_image_builders";topkey='ImageBuilders';key="Name";filterid=key
    elif type == "aws_appstream_stack":
        clfn="appstream";descfn="list_stacks";topkey='Stacks';key="Name";filterid=key
    elif type == "aws_appstream_user":
        clfn="appstream";descfn="list_users";topkey='Users';key="UserName";filterid=key
    elif type == "aws_appstream_user_stack_association":
        clfn="appstream";descfn="list_user_stack_associations";topkey='UserStackAssociations';key="UserName";filterid=key
    elif type == "aws_appsync_api_cache":
        clfn="appsync";descfn="list_api_caches";topkey='ApiCaches';key="ApiCacheName";filterid=key
    elif type == "aws_appsync_api_key":
        clfn="appsync";descfn="list_api_keys";topkey='ApiKeys';key="ApiKeyId";filterid=key
    elif type == "aws_appsync_datasource":
        clfn="appsync";descfn="list_data_sources";topkey='DataSources';key="DataSourceName";filterid=key
    elif type == "aws_appsync_domain_name":
        clfn="appsync";descfn="list_domain_names";topkey='DomainNames';key="DomainName";filterid=key
    elif type == "aws_appsync_domain_name_api_association":
        clfn="appsync";descfn="list_domain_name_api_associations";topkey='DomainNameApiAssociations';key="DomainName";filterid=key
    elif type == "aws_appsync_function":
        clfn="appsync";descfn="list_functions";topkey='Functions';key="FunctionId";filterid=key
    elif type == "aws_appsync_graphql_api":
        clfn="appsync";descfn="list_graphql_apis";topkey='GraphqlApis';key="ApiId";filterid=key
    elif type == "aws_appsync_resolver":
        clfn="appsync";descfn="list_resolvers";topkey='Resolvers';key="ResolverArn";filterid=key
    elif type == "aws_appsync_type":
        clfn="appsync";descfn="list_types";topkey='Types';key="TypeName";filterid=key
    elif type == "aws_athena_data_catalog":
        clfn="athena";descfn="list_data_catalogs";topkey='DataCatalogs';key="Name";filterid=key
    elif type == "aws_athena_database":
        clfn="athena";descfn="list_databases";topkey='Databases';key="Name";filterid=key
    elif type == "aws_athena_named_query":
        clfn="athena";descfn="list_named_queries";topkey='NamedQueries';key="NamedQueryId";filterid=key
    elif type == "aws_athena_prepared_statement":
        clfn="athena";descfn="list_prepared_statements";topkey='PreparedStatements';key="PreparedStatementName";filterid=key
    elif type == "aws_athena_workgroup":
        clfn="athena";descfn="list_work_groups";topkey='WorkGroups';key="Name";filterid=key
    elif type == "aws_auditmanager_account_registration":
        clfn="auditmanager";descfn="list_account_registrations";topkey='AccountRegistrations';key="Id";filterid=key
    elif type == "aws_auditmanager_assessment":
        clfn="auditmanager";descfn="list_assessments";topkey='Assessments';key="Id";filterid=key
    elif type == "aws_auditmanager_assessment_delegation":
        clfn="auditmanager";descfn="list_assessment_delegations";topkey='AssessmentDelegations';key="Id";filterid=key
    elif type == "aws_auditmanager_assessment_report":
        clfn="auditmanager";descfn="list_assessment_reports";topkey='AssessmentReports';key="Id";filterid=key
    elif type == "aws_auditmanager_control":
        clfn="auditmanager";descfn="list_controls";topkey='Controls';key="Id";filterid=key
    elif type == "aws_auditmanager_framework":
        clfn="auditmanager";descfn="list_frameworks";topkey='Frameworks';key="Id";filterid=key
    elif type == "aws_auditmanager_framework_share":
        clfn="auditmanager";descfn="list_framework_shares";topkey='FrameworkShares';key="Id";filterid=key
    elif type == "aws_auditmanager_organization_admin_account_registration":
        clfn="auditmanager";descfn="list_organization_admin_accounts";topkey='OrganizationAdminAccounts';key="Id";filterid=key
    elif type == "aws_autoscaling_attachment":
        clfn="autoscaling";descfn="list_attachments";topkey='Attachments';key="AttachmentName";filterid=key
    elif type == "aws_autoscaling_group":
        clfn="autoscaling";descfn="list_groups";topkey='Groups';key="AutoScalingGroupName";filterid=key
    elif type == "aws_autoscaling_group_tag":
        clfn="autoscaling";descfn="list_tags";topkey='Tags';key="ResourceId";filterid=key
    elif type == "aws_autoscaling_lifecycle_hook":
        clfn="autoscaling";descfn="list_lifecycle_hooks";topkey='LifecycleHooks';key="LifecycleHookName";filterid=key
    elif type == "aws_autoscaling_notification":
        clfn="autoscaling";descfn="list_notifications";topkey='Notifications';key="TopicARN";filterid=key
    elif type == "aws_autoscaling_policy":
        clfn="autoscaling";descfn="list_policies";topkey='Policies';key="PolicyName";filterid=key
    elif type == "aws_autoscaling_schedule":
        clfn="autoscaling";descfn="list_schedules";topkey='Schedules';key="ScheduleName";filterid=key
    elif type == "aws_autoscaling_traffic_source_attachment":
        clfn="autoscaling";descfn="list_traffic_source_attachments";topkey='TrafficSourceAttachments';key="TrafficSourceAttachmentName";filterid=key
    elif type == "aws_autoscalingplans_scaling_plan":
        clfn="autoscalingplans";descfn="list_scaling_plans";topkey='ScalingPlans';key="ScalingPlanName";filterid=key
    elif type == "aws_backup_framework":
        clfn="backup";descfn="list_frameworks";topkey='Frameworks';key="FrameworkName";filterid=key
    elif type == "aws_backup_global_settings":
        clfn="backup";descfn="list_global_settings";topkey='GlobalSettings';key="GlobalSettingsName";filterid=key
    elif type == "aws_backup_plan":
        clfn="backup";descfn="list_plans";topkey='Plans';key="PlanName";filterid=key
    elif type == "aws_backup_region_settings":
        clfn="backup";descfn="list_region_settings";topkey='RegionSettings';key="RegionSettingsName";filterid=key
    elif type == "aws_backup_report_plan":
        clfn="backup";descfn="list_report_plans";topkey='ReportPlans';key="ReportPlanName";filterid=key
    elif type == "aws_backup_selection":
        clfn="backup";descfn="list_selections";topkey='Selections';key="SelectionName";filterid=key
    elif type == "aws_backup_vault":
        clfn="backup";descfn="list_vaults";topkey='Vaults';key="VaultName";filterid=key
    elif type == "aws_backup_vault_lock_configuration":
        clfn="backup";descfn="list_vault_lock_configuration";topkey='VaultLockConfiguration';key="VaultLockConfigurationName";filterid=key
    elif type == "aws_backup_vault_notifications":
        clfn="backup";descfn="list_vault_notifications";topkey='VaultNotifications';key="VaultNotificationsName";filterid=key
    elif type == "aws_backup_vault_policy":
        clfn="backup";descfn="list_vault_policies";topkey='VaultPolicies';key="VaultName";filterid=key
    elif type == "aws_batch_compute_environment":
        clfn="batch";descfn="list_compute_environments";topkey='ComputeEnvironments';key="ComputeEnvironmentName";filterid=key
    elif type == "aws_batch_job_definition":
        clfn="batch";descfn="list_job_definitions";topkey='JobDefinitions';key="JobDefinitionName";filterid=key
    elif type == "aws_batch_job_queue":
        clfn="batch";descfn="list_job_queues";topkey='JobQueues';key="JobQueueName";filterid=key
    elif type == "aws_batch_scheduling_policy":
        clfn="batch";descfn="list_scheduling_policies";topkey='SchedulingPolicies';key="SchedulingPolicyName";filterid=key
    elif type == "aws_bedrock_model_invocation_logging_configuration":
        clfn="bedrock";descfn="list_model_invocation_logging_configurations";topkey='ModelInvocationLoggingConfigurations';key="ModelInvocationLoggingConfigurationName";filterid=key
    elif type == "aws_billing_service_account":
        clfn="billing";descfn="list_service_accounts";topkey='ServiceAccounts';key="ServiceAccountId";filterid=key
    elif type == "aws_budgets_budget":
        clfn="budgets";descfn="list_budgets";topkey='Budgets';key="BudgetName";filterid=key
    elif type == "aws_budgets_budget_action":
        clfn="budgets";descfn="list_budget_actions";topkey='BudgetActions';key="ActionId";filterid=key
    elif type == "aws_caller_identity":
        clfn="sts";descfn="get_caller_identity";topkey='UserId';key="UserId";filterid=key
    elif type == "aws_canonical_user_id":
        clfn="sts";descfn="get_caller_identity";topkey='UserId';key="UserId";filterid=key
    elif type == "aws_ce_anomaly_monitor":
        clfn="ce";descfn="list_anomaly_monitors";topkey='AnomalyMonitors';key="MonitorName";filterid=key
    elif type == "aws_ce_anomaly_subscription":
        clfn="ce";descfn="list_anomaly_subscriptions";topkey='AnomalySubscriptions';key="SubscriptionName";filterid=key
    elif type == "aws_ce_cost_allocation_tag":
        clfn="ce";descfn="list_cost_allocation_tags";topkey='CostAllocationTags';key="CostAllocationTagKey";filterid=key
    elif type == "aws_ce_cost_category":
        clfn="ce";descfn="list_cost_categories";topkey='CostCategories';key="CostCategoryArn";filterid=key
    elif type == "aws_chime_voice_connector":
        clfn="chime";descfn="list_voice_connectors";topkey='VoiceConnectors';key="Name";filterid=key
    elif type == "aws_chime_voice_connector_group":
        clfn="chime";descfn="list_voice_connector_groups";topkey='VoiceConnectorGroups';key="Name";filterid=key
    elif type == "aws_chime_voice_connector_logging":
        clfn="chime";descfn="list_voice_connector_logging_configurations";topkey='VoiceConnectorLoggingConfigurations';key="VoiceConnectorName";filterid=key
    elif type == "aws_chime_voice_connector_origination":
        clfn="chime";descfn="list_voice_connector_origination_configurations";topkey='VoiceConnectorOriginationConfigurations';key="VoiceConnectorName";filterid=key
    elif type == "aws_chime_voice_connector_streaming":
        clfn="chime";descfn="list_voice_connector_streaming_configurations";topkey='VoiceConnectorStreamingConfigurations';key="VoiceConnectorName";filterid=key
    elif type == "aws_chime_voice_connector_termination":
        clfn="chime";descfn="list_voice_connector_termination_configurations";topkey='VoiceConnectorTerminationConfigurations';key="VoiceConnectorName";filterid=key
    elif type == "aws_chime_voice_connector_termination_credentials":
        clfn="chime";descfn="list_voice_connector_termination_credentials";topkey='VoiceConnectorTerminationCredentials';key="Name";filterid=key
    elif type == "aws_chimesdkmediapipelines_media_insights_pipeline_configuration":
        clfn="chimesdkmediapipelines";descfn="list_media_insights_pipelines";topkey='MediaInsightsPipelines';key="Name";filterid=key
    elif type == "aws_chimesdkvoice_global_settings":
        clfn="chimesdkvoice";descfn="list_global_settings";topkey='GlobalSettings';key="GlobalSettingsName";filterid=key
    elif type == "aws_chimesdkvoice_sip_media_application":
        clfn="chimesdkvoice";descfn="list_sip_media_applications";topkey='SipMediaApplications';key="Name";filterid=key
    elif type == "aws_chimesdkvoice_sip_rule":
        clfn="chimesdkvoice";descfn="list_sip_rules";topkey='SipRules';key="Name";filterid=key
    elif type == "aws_chimesdkvoice_voice_profile_domain":
        clfn="chimesdkvoice";descfn="list_voice_profile_domains";topkey='VoiceProfileDomains';key="Name";filterid=key
    elif type == "aws_cleanrooms_collaboration":
        clfn="cleanrooms";descfn="list_collaborations";topkey='Collaborations';key="CollaborationId";filterid=key
    elif type == "aws_cleanrooms_configured_table":
        clfn="cleanrooms";descfn="list_configured_tables";topkey='ConfiguredTables';key="ConfiguredTableName";filterid=key
    elif type == "aws_cloud9_environment_ec2":
        clfn="cloud9";descfn="list_environments";topkey='Environments';key="Name";filterid=key
    elif type == "aws_cloud9_environment_membership":
        clfn="cloud9";descfn="list_environment_memberships";topkey='Memberships';key="Id";filterid=key
    elif type == "aws_cloudcontrolapi_resource":
        clfn="cloudcontrolapi";descfn="list_resources";topkey='Resources';key="Identifier";filterid=key
    elif type == "aws_cloudformation_stack":
        clfn="cloudformation";descfn="list_stacks";topkey='Stacks';key="StackName";filterid=key
    elif type == "aws_cloudformation_stack_set":
        clfn="cloudformation";descfn="list_stack_sets";topkey='StackSets';key="StackSetName";filterid=key
    elif type == "aws_cloudformation_stack_set_instance":
        clfn="cloudformation";descfn="list_stack_set_instances";topkey='StackSetInstances';key="Id";filterid=key
    elif type == "aws_cloudformation_type":
        clfn="cloudformation";descfn="list_types";topkey='Types';key="Arn";filterid=key
    elif type == "aws_cloudfront_cache_policy":
        clfn="cloudfront";descfn="list_cache_policies";topkey='CachePolicies';key="CachePolicyId";filterid=key
    elif type == "aws_cloudfront_continuous_deployment_policy":
        clfn="cloudfront";descfn="list_continuous_deployment_policies";topkey='ContinuousDeploymentPolicies';key="ContinuousDeploymentPolicyId";filterid=key
    elif type == "aws_cloudfront_distribution":
        clfn="cloudfront";descfn="list_distributions";topkey='Distributions';key="Id";filterid=key
    elif type == "aws_cloudfront_field_level_encryption_config":
        clfn="cloudfront";descfn="list_field_level_encryption_configs";topkey='FieldLevelEncryptionConfigs';key="Id";filterid=key
    elif type == "aws_cloudfront_field_level_encryption_profile":
        clfn="cloudfront";descfn="list_field_level_encryption_profiles";topkey='FieldLevelEncryptionProfiles';key="Id";filterid=key
    elif type == "aws_cloudfront_function":
        clfn="cloudfront";descfn="list_functions";topkey='Functions';key="FunctionId";filterid=key
    elif type == "aws_cloudfront_key_group":
        clfn="cloudfront";descfn="list_key_groups";topkey='KeyGroups';key="KeyGroupId";filterid=key
    elif type == "aws_cloudfront_monitoring_subscription":
        clfn="cloudfront";descfn="list_monitoring_subscriptions";topkey='MonitoringSubscriptions';key="Id";filterid=key
    elif type == "aws_cloudfront_origin_access_control":
        clfn="cloudfront";descfn="list_origin_access_controls";topkey='OriginAccessControls';key="Id";filterid=key
    elif type == "aws_cloudfront_origin_access_identities":
        clfn="cloudfront";descfn="list_origin_access_identities";topkey='OriginAccessIdentities';key="Id";filterid=key
    elif type == "aws_cloudfront_origin_access_identity":
        clfn="cloudfront";descfn="list_origin_access_identities";topkey='OriginAccessIdentities';key="Id";filterid=key
    elif type == "aws_cloudfront_origin_request_policy":
        clfn="cloudfront";descfn="list_origin_request_policies";topkey='OriginRequestPolicies';key="Id";filterid=key
    elif type == "aws_cloudfront_public_key":
        clfn="cloudfront";descfn="list_public_keys";topkey='PublicKeys';key="Id";filterid=key
    elif type == "aws_cloudfront_realtime_log_config":
        clfn="cloudfront";descfn="list_realtime_log_configs";topkey='RealtimeLogConfigs';key="Id";filterid=key
    elif type == "aws_cloudfront_response_headers_policy":
        clfn="cloudfront";descfn="list_response_headers_policies";topkey='ResponseHeadersPolicies';key="Id";filterid=key
    elif type == "aws_cloudhsm_v2_cluster":
        clfn="cloudhsmv2";descfn="list_clusters";topkey='Clusters';key="ClusterId";filterid=key
    elif type == "aws_cloudhsm_v2_hsm":
        clfn="cloudhsmv2";descfn="list_hsms";topkey='Hsms';key="HsmId";filterid=key
    elif type == "aws_cloudsearch_domain":
        clfn="cloudsearch";descfn="list_domains";topkey='DomainNames';key="DomainName";filterid=key
    elif type == "aws_cloudsearch_domain_service_access_policy":
        clfn="cloudsearch";descfn="list_domain_service_access_policies";topkey='DomainServiceAccessPolicies';key="DomainName";filterid=key
    elif type == "aws_cloudtrail":
        clfn="cloudtrail";descfn="list_trails";topkey='Trails';key="Name";filterid=key
    elif type == "aws_cloudtrail_event_data_store":
        clfn="cloudtrail";descfn="list_event_data_stores";topkey='EventDataStores';key="Name";filterid=key
    elif type == "aws_cloudwatch_composite_alarm":
        clfn="cloudwatch";descfn="list_composite_alarms";topkey='CompositeAlarms';key="AlarmName";filterid=key
    elif type == "aws_cloudwatch_dashboard":
        clfn="cloudwatch";descfn="list_dashboards";topkey='Dashboards';key="DashboardName";filterid=key
    elif type == "aws_cloudwatch_event_api_destination":
        clfn="cloudwatch";descfn="list_api_destinations";topkey='ApiDestinations';key="Name";filterid=key
    elif type == "aws_cloudwatch_event_archive":
        clfn="cloudwatch";descfn="list_archives";topkey='Archives';key="ArchiveName";filterid=key
    elif type == "aws_cloudwatch_event_bus":
        clfn="cloudwatch";descfn="list_event_buses";topkey='EventBusNames';key="Name";filterid=key
    elif type == "aws_cloudwatch_event_bus_policy":
        clfn="cloudwatch";descfn="list_event_bus_policies";topkey='EventBusPolicies';key="Name";filterid=key
    elif type == "aws_cloudwatch_event_connection":
        clfn="cloudwatch";descfn="list_connections";topkey='Connections';key="Name";filterid=key
    elif type == "aws_cloudwatch_event_endpoint":
        clfn="cloudwatch";descfn="list_endpoints";topkey='Endpoints';key="Name";filterid=key
    elif type == "aws_cloudwatch_event_permission":
        clfn="cloudwatch";descfn="list_permissions";topkey='Permissions';key="Name";filterid=key
    #elif type == "aws_cloudwatch_event_rule":
    #    clfn="cloudwatch";descfn="list_rules";topkey='Rules';key="Name";filterid=key
    elif type == "aws_cloudwatch_event_source":
        clfn="cloudwatch";descfn="list_sources";topkey='Sources';key="Name";filterid=key
    elif type == "aws_cloudwatch_event_target":
        clfn="cloudwatch";descfn="list_targets";topkey='Targets';key="Name";filterid=key
    elif type == "aws_cloudwatch_log_data_protection_policy":
        clfn="cloudwatch";descfn="list_data_protection_policies";topkey='DataProtectionPolicies';key="Name";filterid=key
    elif type == "aws_cloudwatch_log_destination":
        clfn="cloudwatch";descfn="list_destinations";topkey='Destinations';key="DestinationName";filterid=key
    elif type == "aws_cloudwatch_log_destination_policy":
        clfn="cloudwatch";descfn="list_destination_policies";topkey='DestinationPolicies';key="DestinationName";filterid=key
    #elif type == "aws_cloudwatch_log_group":
    #    clfn="cloudwatch";descfn="list_log_groups";topkey='LogGroups';key="LogGroupName";filterid=key
    elif type == "aws_cloudwatch_log_metric_filter":
        clfn="cloudwatch";descfn="list_metric_filters";topkey='MetricFilters';key="Name";filterid=key
    elif type == "aws_cloudwatch_log_resource_policy":
        clfn="cloudwatch";descfn="list_resource_policies";topkey='ResourcePolicies';key="Name";filterid=key
    elif type == "aws_cloudwatch_log_stream":
        clfn="cloudwatch";descfn="list_log_streams";topkey='LogStreams';key="LogStreamName";filterid=key
    elif type == "aws_cloudwatch_log_subscription_filter":
        clfn="cloudwatch";descfn="list_subscription_filters";topkey='SubscriptionFilters';key="Name";filterid=key
    elif type == "aws_cloudwatch_metric_alarm":
        clfn="cloudwatch";descfn="list_alarms";topkey='MetricAlarms';key="AlarmName";filterid=key
    elif type == "aws_cloudwatch_metric_stream":
        clfn="cloudwatch";descfn="list_metric_streams";topkey='MetricStreams';key="Name";filterid=key
    elif type == "aws_cloudwatch_query_definition":
        clfn="cloudwatch";descfn="list_query_definitions";topkey='QueryDefinitions';key="Name";filterid=key
    elif type == "aws_codeartifact_domain":
        clfn="codeartifact";descfn="list_domains";topkey='Domains';key="Name";filterid=key
    elif type == "aws_codeartifact_domain_permissions_policy":
        clfn="codeartifact";descfn="list_domain_permissions_policies";topkey='DomainPermissionsPolicies';key="Name";filterid=key
    elif type == "aws_codeartifact_repository":
        clfn="codeartifact";descfn="list_repositories";topkey='Repositories';key="Name";filterid=key
    elif type == "aws_codeartifact_repository_permissions_policy":
        clfn="codeartifact";descfn="list_repository_permissions_policies";topkey='RepositoryPermissionsPolicies';key="Name";filterid=key
    elif type == "aws_codebuild_project":
        clfn="codebuild";descfn="list_projects";topkey='Projects';key="Name";filterid=key
    elif type == "aws_codebuild_report_group":
        clfn="codebuild";descfn="list_report_groups";topkey='ReportGroups';key="Name";filterid=key
    elif type == "aws_codebuild_resource_policy":
        clfn="codebuild";descfn="list_resource_policies";topkey='ResourcePolicies';key="Name";filterid=key
    elif type == "aws_codebuild_source_credential":
        clfn="codebuild";descfn="list_source_credentials";topkey='SourceCredentialsInfos';key="Arn";filterid=key
    elif type == "aws_codebuild_webhook":
        clfn="codebuild";descfn="list_webhooks";topkey='Webhooks';key="Name";filterid=key
    elif type == "aws_codecatalyst_dev_environment":
        clfn="codecatalyst";descfn="list_dev_environments";topkey='DevEnvironments';key="Id";filterid=key
    elif type == "aws_codecatalyst_project":
        clfn="codecatalyst";descfn="list_projects";topkey='Projects';key="Id";filterid=key
    elif type == "aws_codecatalyst_source_repository":
        clfn="codecatalyst";descfn="list_source_repositories";topkey='SourceRepositories';key="Id";filterid=key
    elif type == "aws_codecommit_approval_rule_template":
        clfn="codecommit";descfn="list_approval_rule_templates";topkey='ApprovalRuleTemplates';key="Name";filterid=key
    elif type == "aws_codecommit_approval_rule_template_association":
        clfn="codecommit";descfn="list_associated_approval_rule_templates";topkey='AssociatedApprovalRuleTemplates';key="Name";filterid=key
    elif type == "aws_codecommit_repository":
        clfn="codecommit";descfn="list_repositories";topkey='Repositories';key="Name";filterid=key
    elif type == "aws_codecommit_trigger":
        clfn="codecommit";descfn="list_repository_triggers";topkey='RepositoryTriggers';key="Name";filterid=key
    elif type == "aws_codedeploy_app":
        clfn="codedeploy";descfn="list_apps";topkey='Apps';key="Name";filterid=key
    elif type == "aws_codedeploy_deployment_config":
        clfn="codedeploy";descfn="list_deployment_configs";topkey='DeploymentConfigs';key="Name";filterid=key
    elif type == "aws_codedeploy_deployment_group":
        clfn="codedeploy";descfn="list_deployment_groups";topkey='DeploymentGroups';key="Name";filterid=key
    elif type == "aws_codeguruprofiler_profiling_group":
        clfn="codeguruprofiler";descfn="list_profiling_groups";topkey='ProfilingGroups';key="Name";filterid=key
    elif type == "aws_codegurureviewer_repository_association":
        clfn="codegurureviewer";descfn="list_repository_associations";topkey='RepositoryAssociations';key="Name";filterid=key
    elif type == "aws_codepipeline":
        clfn="codepipeline";descfn="list_pipelines";topkey='Pipelines';key="Name";filterid=key
    elif type == "aws_codepipeline_custom_action_type":
        clfn="codepipeline";descfn="list_custom_action_types";topkey='CustomActionTypes';key="Category";filterid=key
    elif type == "aws_codepipeline_webhook":
        clfn="codepipeline";descfn="list_webhooks";topkey='Webhooks';key="Name";filterid=key
    elif type == "aws_codestarconnections_connection":
        clfn="codestarconnections";descfn="list_connections";topkey='Connections';key="ConnectionName";filterid=key
    elif type == "aws_codestarconnections_host":
        clfn="codestarconnections";descfn="list_hosts";topkey='Hosts';key="Name";filterid=key
    elif type == "aws_codestarnotifications_notification_rule":
        clfn="codestarnotifications";descfn="list_notification_rules";topkey='NotificationRules';key="Name";filterid=key
    elif type == "aws_cognito_identity_pool":
        clfn="cognito";descfn="list_identity_pools";topkey='IdentityPools';key="IdentityPoolName";filterid=key
    elif type == "aws_cognito_identity_pool_provider_principal_tag":
        clfn="cognito";descfn="list_identity_pool_roles";topkey='IdentityPoolRoles';key="IdentityPoolId";filterid=key
    elif type == "aws_cognito_identity_pool_roles_attachment":
        clfn="cognito";descfn="list_identity_pool_roles_attachments";topkey='IdentityPoolRolesAttachments';key="IdentityPoolId";filterid=key
    elif type == "aws_cognito_identity_provider":
        clfn="cognito";descfn="list_identity_providers";topkey='IdentityProviders';key="ProviderName";filterid=key
    elif type == "aws_cognito_managed_user_pool_client":
        clfn="cognito";descfn="list_user_pool_clients";topkey='UserPoolClients';key="ClientName";filterid=key
    elif type == "aws_cognito_resource_server":
        clfn="cognito";descfn="list_resource_servers";topkey='ResourceServers';key="Identifier";filterid=key
    elif type == "aws_cognito_risk_configuration":
        clfn="cognito";descfn="list_risk_configurations";topkey='RiskConfigurations';key="Id";filterid=key
    elif type == "aws_cognito_user":
        clfn="cognito";descfn="list_users";topkey='Users';key="Username";filterid=key
    elif type == "aws_cognito_user_group":
        clfn="cognito";descfn="list_user_groups";topkey='UserGroups';key="GroupName";filterid=key
    elif type == "aws_cognito_user_in_group":
        clfn="cognito";descfn="list_users_in_group";topkey='UsersInGroup';key="Username";filterid=key
    elif type == "aws_cognito_user_pool":
        clfn="cognito";descfn="list_user_pools";topkey='UserPools';key="Name";filterid=key
    elif type == "aws_cognito_user_pool_client":
        clfn="cognito";descfn="list_user_pool_clients";topkey='UserPoolClients';key="ClientName";filterid=key
    elif type == "aws_cognito_user_pool_domain":
        clfn="cognito";descfn="list_user_pool_domains";topkey='UserPoolDomains';key="Domain";filterid=key
    elif type == "aws_cognito_user_pool_ui_customization":
        clfn="cognito";descfn="list_user_pool_uis";topkey='UserPoolUis';key="UserPoolId";filterid=key
    elif type == "aws_comprehend_document_classifier":
        clfn="comprehend";descfn="list_document_classifiers";topkey='DocumentClassifiers';key="DocumentClassifierArn";filterid=key
    elif type == "aws_comprehend_entity_recognizer":
        clfn="comprehend";descfn="list_entity_recognizers";topkey='EntityRecognizers';key="EntityRecognizerArn";filterid=key
    elif type == "aws_config_aggregate_authorization":
        clfn="config";descfn="list_aggregate_authorizations";topkey='AggregateAuthorizations';key="AuthorizationName";filterid=key
    #elif type == "aws_config_config_rule":
    #    clfn="config";descfn="list_config_rules";topkey='ConfigRules';key="ConfigRuleName";filterid=key
    elif type == "aws_config_configuration_aggregator":
        clfn="config";descfn="list_configuration_aggregators";topkey='ConfigurationAggregators';key="ConfigurationAggregatorName";filterid=key
    elif type == "aws_config_configuration_recorder":
        clfn="config";descfn="list_configuration_recorders";topkey='ConfigurationRecorders';key="name";filterid=key
    elif type == "aws_config_configuration_recorder_status":
        clfn="config";descfn="list_configuration_recorder_status";topkey='ConfigurationRecorderStatus';key="name";filterid=key
    elif type == "aws_config_conformance_pack":
        clfn="config";descfn="list_conformance_packs";topkey='ConformancePackNames';key="ConformancePackName";filterid=key
    elif type == "aws_config_delivery_channel":
        clfn="config";descfn="list_delivery_channels";topkey='DeliveryChannels';key="name";filterid=key
    elif type == "aws_config_organization_conformance_pack":
        clfn="config";descfn="list_organization_conformance_packs";topkey='OrganizationConformancePackNames';key="ConformancePackName";filterid=key
    elif type == "aws_config_organization_custom_policy_rule":
        clfn="config";descfn="list_organization_custom_policy_rules";topkey='OrganizationCustomPolicyRules';key="PolicyRuleName";filterid=key
    elif type == "aws_config_organization_custom_rule":
        clfn="config";descfn="list_organization_custom_rules";topkey='OrganizationCustomRules';key="PolicyRuleName";filterid=key
    elif type == "aws_config_organization_managed_rule":
        clfn="config";descfn="list_organization_managed_rules";topkey='OrganizationManagedRules';key="PolicyRuleName";filterid=key
    elif type == "aws_config_remediation_configuration":
        clfn="config";descfn="list_remediation_configurations";topkey='RemediationConfigurations';key="ConfigRuleName";filterid=key
    elif type == "aws_connect_bot_association":
        clfn="connect";descfn="list_bot_associations";topkey='BotAssociations';key="Name";filterid=key
    elif type == "aws_connect_contact_flow":
        clfn="connect";descfn="list_contact_flows";topkey='ContactFlows';key="Name";filterid=key
    elif type == "aws_connect_contact_flow_module":
        clfn="connect";descfn="list_contact_flow_modules";topkey='ContactFlowModules';key="Name";filterid=key
    elif type == "aws_connect_hours_of_operation":
        clfn="connect";descfn="list_hours_of_operations";topkey='HoursOfOperations';key="Name";filterid=key
    elif type == "aws_connect_instance":
        clfn="connect";descfn="list_instances";topkey='Instances';key="Id";filterid=key
    elif type == "aws_connect_instance_storage_config":
        clfn="connect";descfn="list_instance_storage_configs";topkey='InstanceStorageConfigs';key="InstanceId";filterid=key
    elif type == "aws_connect_lambda_function_association":
        clfn="connect";descfn="list_lambda_function_associations";topkey='LambdaFunctionAssociations';key="InstanceId";filterid=key
    elif type == "aws_connect_phone_number":
        clfn="connect";descfn="list_phone_numbers";topkey='PhoneNumbers';key="PhoneNumber";filterid=key
    elif type == "aws_connect_queue":
        clfn="connect";descfn="list_queues";topkey='Queues';key="Id";filterid=key
    elif type == "aws_connect_quick_connect":
        clfn="connect";descfn="list_quick_connects";topkey='QuickConnects';key="Id";filterid=key
    elif type == "aws_connect_routing_profile":
        clfn="connect";descfn="list_routing_profiles";topkey='RoutingProfiles';key="Id";filterid=key
    elif type == "aws_connect_security_profile":
        clfn="connect";descfn="list_security_profiles";topkey='SecurityProfiles';key="Id";filterid=key
    elif type == "aws_connect_user":
        clfn="connect";descfn="list_users";topkey='Users';key="Id";filterid=key
    elif type == "aws_connect_user_hierarchy_group":
        clfn="connect";descfn="list_user_hierarchy_groups";topkey='UserHierarchyGroups';key="Id";filterid=key
    elif type == "aws_connect_user_hierarchy_structure":
        clfn="connect";descfn="list_user_hierarchy_structures";topkey='UserHierarchyStructures';key="Id";filterid=key
    elif type == "aws_connect_vocabulary":
        clfn="connect";descfn="list_vocabularies";topkey='Vocabularies';key="Id";filterid=key
    elif type == "aws_controltower_control":
        clfn="controltower";descfn="list_controls";topkey='Controls';key="Id";filterid=key
    elif type == "aws_cur_report_definition":
        clfn="cur";descfn="list_report_definitions";topkey='ReportDefinitions';key="ReportName";filterid=key
    elif type == "aws_customer_gateway":
        clfn="ec2";descfn="describe_customer_gateways";topkey='CustomerGateways';key="CustomerGatewayId";filterid=key
    elif type == "aws_customerprofiles_domain":
        clfn="customerprofiles";descfn="list_domains";topkey='Domains';key="DomainName";filterid=key
    elif type == "aws_customerprofiles_profile":
        clfn="customerprofiles";descfn="list_profiles";topkey='Profiles';key="ProfileArn";filterid=key
    elif type == "aws_dataexchange_data_set":
        clfn="dataexchange";descfn="list_data_sets";topkey='DataSets';key="Id";filterid=key
    elif type == "aws_dataexchange_revision":
        clfn="dataexchange";descfn="list_revisions";topkey='Revisions';key="Id";filterid=key
    elif type == "aws_datapipeline_pipeline":
        clfn="datapipeline";descfn="list_pipelines";topkey='Pipelines';key="Name";filterid=key
    elif type == "aws_datapipeline_pipeline_definition":
        clfn="datapipeline";descfn="list_pipeline_definition";topkey='PipelineDefinition';key="Name";filterid=key
    elif type == "aws_datasync_agent":
        clfn="datasync";descfn="list_agents";topkey='Agents';key="AgentArn";filterid=key
    elif type == "aws_datasync_location_azure_blob":
        clfn="datasync";descfn="list_location_s3";topkey='Locations';key="LocationArn";filterid=key
    elif type == "aws_datasync_location_efs":
        clfn="datasync";descfn="list_location_efs";topkey='Locations';key="LocationArn";filterid=key
    elif type == "aws_datasync_location_fsx_lustre_file_system":
        clfn="datasync";descfn="list_location_fsx_lustre";topkey='Locations';key="LocationArn";filterid=key
    elif type == "aws_datasync_location_fsx_ontap_file_system":
        clfn="datasync";descfn="list_location_fsx_ontap";topkey='Locations';key="LocationArn";filterid=key
    elif type == "aws_datasync_location_fsx_openzfs_file_system":
        clfn="datasync";descfn="list_location_fsx_openzfs";topkey='Locations';key="LocationArn";filterid=key
    elif type == "aws_datasync_location_fsx_windows_file_system":
        clfn="datasync";descfn="list_location_fsx_windows";topkey='Locations';key="LocationArn";filterid=key
    elif type == "aws_datasync_location_hdfs":
        clfn="datasync";descfn="list_location_hdfs";topkey='Locations';key="LocationArn";filterid=key
    elif type == "aws_datasync_location_nfs":
        clfn="datasync";descfn="list_location_nfs";topkey='Locations';key="LocationArn";filterid=key
    elif type == "aws_datasync_location_object_storage":
        clfn="datasync";descfn="list_location_object_storage";topkey='Locations';key="LocationArn";filterid=key
    elif type == "aws_datasync_location_s3":
        clfn="datasync";descfn="list_location_s3";topkey='Locations';key="LocationArn";filterid=key
    elif type == "aws_datasync_location_smb":
        clfn="datasync";descfn="list_location_smb";topkey='Locations';key="LocationArn";filterid=key
    elif type == "aws_datasync_task":
        clfn="datasync";descfn="list_tasks";topkey='Tasks';key="TaskArn";filterid=key
    elif type == "aws_dax_cluster":
        clfn="dax";descfn="list_clusters";topkey='Clusters';key="ClusterName";filterid=key
    elif type == "aws_dax_parameter_group":
        clfn="dax";descfn="list_parameter_groups";topkey='ParameterGroups';key="ParameterGroupName";filterid=key
    elif type == "aws_dax_subnet_group":
        clfn="dax";descfn="list_subnet_groups";topkey='SubnetGroups';key="SubnetGroupName";filterid=key
    elif type == "aws_db_cluster_snapshot":
        clfn="rds";descfn="describe_db_cluster_snapshots";topkey='DBClusterSnapshots';key="DBClusterSnapshotIdentifier";filterid=key
    elif type == "aws_db_event_categories":
        clfn="rds";descfn="describe_event_categories";topkey='EventCategoriesMapList';key="SourceType";filterid=key
    #elif type == "aws_db_event_subscription":
    #    clfn="rds";descfn="describe_event_subscriptions";topkey='EventSubscriptionsList';key="SubscriptionName";filterid=key
    elif type == "aws_db_instance":
        clfn="rds";descfn="describe_db_instances";topkey='DBInstances';key="DBInstanceIdentifier";filterid=key
    elif type == "aws_db_instance_automated_backups_replication":
        clfn="rds";descfn="describe_db_instance_automated_backups";topkey='DBInstanceAutomatedBackups';key="DBInstanceArn";filterid=key
    elif type == "aws_db_instance_role_association":
        clfn="rds";descfn="describe_db_instance_role_associations";topkey='DBInstanceRoleAssociations';key="DBInstanceArn";filterid=key
    #elif type == "aws_db_instances":
    #    clfn="rds";descfn="describe_db_instances";topkey='DBInstances';key="DBInstanceIdentifier";filterid=key
    elif type == "aws_db_option_group":
        clfn="rds";descfn="describe_option_groups";topkey='OptionGroupsList';key="OptionGroupName";filterid=key
    #elif type == "aws_db_parameter_group":
    #    clfn="rds";descfn="describe_db_parameter_groups";topkey='DBParameterGroups';key="DBParameterGroupName";filterid=key
    elif type == "aws_db_proxy":
        clfn="rds";descfn="describe_db_proxies";topkey='DBProxies';key="DBProxyName";filterid=key
    elif type == "aws_db_proxy_default_target_group":
        clfn="rds";descfn="describe_db_proxy_default_target_groups";topkey='DBProxyDefaultTargetGroups';key="DBProxyName";filterid=key
    elif type == "aws_db_proxy_endpoint":
        clfn="rds";descfn="describe_db_proxy_endpoints";topkey='DBProxyEndpoints';key="DBProxyEndpointName";filterid=key
    elif type == "aws_db_proxy_target":
        clfn="rds";descfn="describe_db_proxy_targets";topkey='DBProxyTargets';key="TargetGroupName";filterid=key
    elif type == "aws_db_snapshot":
        clfn="rds";descfn="describe_db_snapshots";topkey='DBSnapshots';key="DBSnapshotIdentifier";filterid=key
    elif type == "aws_db_snapshot_copy":
        clfn="rds";descfn="describe_db_snapshot_attributes";topkey='DBSnapshotAttributesResult';key="DBSnapshotIdentifier";filterid=key
    #elif type == "aws_db_subnet_group":
    #    clfn="rds";descfn="describe_db_subnet_groups";topkey='DBSubnetGroups';key="DBSubnetGroupName";filterid=key
    #elif type == "aws_default_network_acl":
    #    clfn="ec2";descfn="describe_network_acls";topkey='NetworkAcls';key="NetworkAclId";filterid=key
    #elif type == "aws_default_route_table":
    #    clfn="ec2";descfn="describe_route_tables";topkey='RouteTables';key="RouteTableId";filterid=key
    #elif type == "aws_default_security_group":
    #    clfn="ec2";descfn="describe_security_groups";topkey='SecurityGroups';key="GroupId";filterid=key
    #elif type == "aws_default_subnet":
    #    clfn="ec2";descfn="describe_subnets";topkey='Subnets';key="SubnetId";filterid=key
    elif type == "aws_default_tags":
        clfn="ec2";descfn="describe_tags";topkey='Tags';key="ResourceId";filterid=key
    #elif type == "aws_default_vpc":
    #    clfn="ec2";descfn="describe_vpcs";topkey='Vpcs';key="VpcId";filterid=key
    elif type == "aws_default_vpc_dhcp_options":
        clfn="ec2";descfn="describe_vpc_dhcp_options";topkey='VpcDhcpOptions';key="VpcDhcpOptionsId";filterid=key
    elif type == "aws_detective_graph":
        clfn="detective";descfn="list_graphs";topkey='Graphs';key="GraphArn";filterid=key
    elif type == "aws_detective_invitation_accepter":
        clfn="detective";descfn="list_invitation_accepters";topkey='InvitationAccepters';key="GraphArn";filterid=key
    elif type == "aws_detective_member":
        clfn="detective";descfn="list_members";topkey='Members';key="GraphArn";filterid=key
    elif type == "aws_detective_organization_admin_account":
        clfn="detective";descfn="list_organization_admin_accounts";topkey='OrganizationAdminAccounts';key="GraphArn";filterid=key
    elif type == "aws_detective_organization_configuration":
        clfn="detective";descfn="list_organization_configurations";topkey='OrganizationConfigurations';key="GraphArn";filterid=key
    elif type == "aws_devicefarm_device_pool":
        clfn="devicefarm";descfn="list_device_pools";topkey='DevicePools';key="Arn";filterid=key
    elif type == "aws_devicefarm_instance_profile":
        clfn="devicefarm";descfn="list_instance_profiles";topkey='InstanceProfiles';key="Arn";filterid=key
    elif type == "aws_devicefarm_network_profile":
        clfn="devicefarm";descfn="list_network_profiles";topkey='NetworkProfiles';key="Arn";filterid=key
    elif type == "aws_devicefarm_project":
        clfn="devicefarm";descfn="list_projects";topkey='Projects';key="Arn";filterid=key
    elif type == "aws_devicefarm_test_grid_project":
        clfn="devicefarm";descfn="list_test_grid_projects";topkey='TestGridProjects';key="Arn";filterid=key
    elif type == "aws_devicefarm_upload":
        clfn="devicefarm";descfn="list_uploads";topkey='Uploads';key="Arn";filterid=key
    elif type == "aws_directory_service_conditional_forwarder":
        clfn="ds";descfn="list_conditional_forwarders";topkey='ConditionalForwarders';key="DirectoryId";filterid=key
    elif type == "aws_directory_service_directory":
        clfn="ds";descfn="list_directories";topkey='DirectoryDescriptions';key="DirectoryId";filterid=key
    elif type == "aws_directory_service_log_subscription":
        clfn="ds";descfn="list_log_subscriptions";topkey='LogSubscriptions';key="DirectoryId";filterid=key
    elif type == "aws_directory_service_radius_settings":
        clfn="ds";descfn="list_radius_settings";topkey='RadiusSettings';key="DirectoryId";filterid=key
    elif type == "aws_directory_service_region":
        clfn="ds";descfn="list_regions";topkey='Regions';key="DirectoryId";filterid=key
    elif type == "aws_directory_service_shared_directory":
        clfn="ds";descfn="list_shared_directories";topkey='SharedDirectories';key="SharedDirectoryId";filterid=key
    elif type == "aws_directory_service_shared_directory_acceptor":
        clfn="ds";descfn="list_accepted_shared_directories";topkey='AcceptedSharedDirectories';key="SharedDirectoryId";filterid=key
    elif type == "aws_directory_service_trust":
        clfn="ds";descfn="list_trusts";topkey='Trusts';key="TrustId";filterid=key
    elif type == "aws_dlm_lifecycle_policy":
        clfn="dlm";descfn="list_policies";topkey='Policies';key="PolicyId";filterid=key
    elif type == "aws_dms_certificate":
        clfn="dms";descfn="describe_certificates";topkey='Certificates';key="CertificateIdentifier";filterid=key
    elif type == "aws_dms_endpoint":
        clfn="dms";descfn="describe_endpoints";topkey='Endpoints';key="EndpointIdentifier";filterid=key
    elif type == "aws_dms_event_subscription":
        clfn="dms";descfn="describe_event_subscriptions";topkey='EventSubscriptionsList';key="SubscriptionName";filterid=key
    elif type == "aws_dms_replication_config":
        clfn="dms";descfn="describe_replication_configs";topkey='ReplicationConfigs';key="ReplicationConfigIdentifier";filterid=key
    elif type == "aws_dms_replication_instance":
        clfn="dms";descfn="describe_replication_instances";topkey='ReplicationInstances';key="ReplicationInstanceIdentifier";filterid=key
    elif type == "aws_dms_replication_subnet_group":
        clfn="dms";descfn="describe_replication_subnet_groups";topkey='ReplicationSubnetGroups';key="ReplicationSubnetGroupIdentifier";filterid=key
    elif type == "aws_dms_replication_task":
        clfn="dms";descfn="describe_replication_tasks";topkey='ReplicationTasks';key="ReplicationTaskIdentifier";filterid=key
    elif type == "aws_dms_s3_endpoint":
        clfn="dms";descfn="describe_s3_endpoints";topkey='S3Endpoints';key="EndpointIdentifier";filterid=key
    elif type == "aws_docdb_cluster":
        clfn="docdb";descfn="describe_db_clusters";topkey='DBClusters';key="DBClusterIdentifier";filterid=key
    elif type == "aws_docdb_cluster_instance":
        clfn="docdb";descfn="describe_db_cluster_instances";topkey='DBClusterInstances';key="DBClusterIdentifier";filterid=key
    elif type == "aws_docdb_cluster_parameter_group":
        clfn="docdb";descfn="describe_db_cluster_parameter_groups";topkey='DBClusterParameterGroups';key="DBClusterParameterGroupName";filterid=key
    elif type == "aws_docdb_cluster_snapshot":
        clfn="docdb";descfn="describe_db_cluster_snapshots";topkey='DBClusterSnapshots';key="DBClusterSnapshotIdentifier";filterid=key
    elif type == "aws_docdb_event_subscription":
        clfn="docdb";descfn="describe_event_subscriptions";topkey='EventSubscriptionsList';key="SubscriptionName";filterid=key
    elif type == "aws_docdb_global_cluster":
        clfn="docdb";descfn="describe_global_clusters";topkey='GlobalClusters';key="GlobalClusterIdentifier";filterid=key
    elif type == "aws_docdb_subnet_group":
        clfn="docdb";descfn="describe_db_subnet_groups";topkey='DBSubnetGroups';key="DBSubnetGroupName";filterid=key
    elif type == "aws_docdbelastic_cluster":
        clfn="docdbelastic";descfn="describe_clusters";topkey='Clusters';key="ClusterName";filterid=key
    elif type == "aws_dx_bgp_peer":
        clfn="directconnect";descfn="describe_bgp_peers";topkey='BgpPeers';key="BgpPeerId";filterid=key
    elif type == "aws_dx_connection":
        clfn="directconnect";descfn="describe_connections";topkey='Connections';key="ConnectionId";filterid=key
    elif type == "aws_dx_connection_association":
        clfn="directconnect";descfn="describe_connection_associations";topkey='ConnectionAssociations';key="ConnectionId";filterid=key
    elif type == "aws_dx_connection_confirmation":
        clfn="directconnect";descfn="describe_confirmations";topkey='Confirmations';key="ConfirmationToken";filterid=key
    elif type == "aws_dx_gateway":
        clfn="directconnect";descfn="describe_gateways";topkey='Gateways';key="GatewayId";filterid=key
    elif type == "aws_dx_gateway_association":
        clfn="directconnect";descfn="describe_gateway_associations";topkey='GatewayAssociations';key="GatewayId";filterid=key
    elif type == "aws_dx_gateway_association_proposal":
        clfn="directconnect";descfn="describe_gateway_association_proposals";topkey='GatewayAssociationProposals';key="GatewayId";filterid=key
    elif type == "aws_dx_hosted_connection":
        clfn="directconnect";descfn="describe_gateway_association_proposals";topkey='GatewayAssociationProposals';key="ProposalId";filterid=key
    elif type == "aws_dx_hosted_private_virtual_interface":
        clfn="directconnect";descfn="describe_hosted_private_virtual_interfaces";topkey='VirtualInterfaces';key="VirtualInterfaceId";filterid=key
    elif type == "aws_dx_hosted_private_virtual_interface_accepter":
        clfn="directconnect";descfn="describe_hosted_private_virtual_interfaces";topkey='VirtualInterfaces';key="VirtualInterfaceId";filterid=key
    elif type == "aws_dx_hosted_public_virtual_interface":
        clfn="directconnect";descfn="describe_hosted_public_virtual_interfaces";topkey='VirtualInterfaces';key="VirtualInterfaceId";filterid=key
    elif type == "aws_dx_hosted_public_virtual_interface_accepter":
        clfn="directconnect";descfn="describe_hosted_public_virtual_interfaces";topkey='VirtualInterfaces';key="VirtualInterfaceId";filterid=key
    elif type == "aws_dx_hosted_transit_virtual_interface":
        clfn="directconnect";descfn="describe_hosted_transit_virtual_interfaces";topkey='VirtualInterfaces';key="VirtualInterfaceId";filterid=key
    elif type == "aws_dx_hosted_transit_virtual_interface_accepter":
        clfn="directconnect";descfn="describe_hosted_transit_virtual_interfaces";topkey='VirtualInterfaces';key="VirtualInterfaceId";filterid=key
    elif type == "aws_dx_lag":
        clfn="directconnect";descfn="describe_lags";topkey='Lags';key="LagId";filterid=key
    elif type == "aws_dx_macsec_key_association":
        clfn="directconnect";descfn="describe_macsec_key_associations";topkey='MacsecKeyAssociations';key="AssociationId";filterid=key
    elif type == "aws_dx_private_virtual_interface":
        clfn="directconnect";descfn="describe_private_virtual_interfaces";topkey='VirtualInterfaces';key="VirtualInterfaceId";filterid=key
    elif type == "aws_dx_public_virtual_interface":
        clfn="directconnect";descfn="describe_public_virtual_interfaces";topkey='VirtualInterfaces';key="VirtualInterfaceId";filterid=key
    elif type == "aws_dx_transit_virtual_interface":
        clfn="directconnect";descfn="describe_transit_virtual_interfaces";topkey='VirtualInterfaces';key="VirtualInterfaceId";filterid=key
    elif type == "aws_dynamodb_contributor_insights":
        clfn="dynamodb";descfn="describe_contributor_insights";topkey='ContributorInsightsList';key="ContributorInsightsArn";filterid=key
    elif type == "aws_dynamodb_global_table":
        clfn="dynamodb";descfn="describe_global_tables";topkey='GlobalTables';key="GlobalTableName";filterid=key
    elif type == "aws_dynamodb_kinesis_streaming_destination":
        clfn="dynamodb";descfn="describe_kinesis_streaming_destination";topkey='KinesisStreamingDestination';key="TableName";filterid=key
    elif type == "aws_dynamodb_table":
        clfn="dynamodb";descfn="describe_table";topkey='Table';key="TableName";filterid=key
    elif type == "aws_dynamodb_table_item":
        clfn="dynamodb";descfn="describe_table";topkey='Table';key="TableName";filterid=key
    elif type == "aws_dynamodb_table_replica":
        clfn="dynamodb";descfn="describe_table_replica_auto_scaling";topkey='TableReplicaAutoScalingDescription';key="TableName";filterid=key
    elif type == "aws_dynamodb_tag":
        clfn="dynamodb";descfn="list_tags_of_resource";topkey='Tags';key="Key";filterid=key
    elif type == "aws_ebs_default_kms_key":
        clfn="ebs";descfn="describe_default_kms_key";topkey='DefaultKmsKeyId';key="DefaultKmsKeyId";filterid=key
    elif type == "aws_ebs_encryption_by_default":
        clfn="ebs";descfn="describe_ebs_encryption_by_default";topkey='EbsEncryptionByDefault';key="EbsEncryptionByDefault";filterid=key
    elif type == "aws_ebs_snapshot":
        clfn="ebs";descfn="describe_snapshots";topkey='Snapshots';key="SnapshotId";filterid=key
    elif type == "aws_ebs_snapshot_copy":
        clfn="ebs";descfn="describe_snapshot_copy_grants";topkey='SnapshotCopyGrants';key="SnapshotCopyGrantName";filterid=key
    elif type == "aws_ebs_snapshot_import":
        clfn="ebs";descfn="describe_snapshot_import_tasks";topkey='SnapshotTasks';key="SnapshotTaskIdentifier";filterid=key
    elif type == "aws_ebs_volume":
        clfn="ebs";descfn="describe_volumes";topkey='Volumes';key="VolumeId";filterid=key
    elif type == "aws_ec2_availability_zone_group":
        clfn="ec2";descfn="describe_availability_zone_groups";topkey='AvailabilityZoneGroups';key="GroupName";filterid=key
    elif type == "aws_ec2_capacity_reservation":
        clfn="ec2";descfn="describe_capacity_reservations";topkey='CapacityReservations';key="CapacityReservationId";filterid=key
    elif type == "aws_ec2_carrier_gateway":
        clfn="ec2";descfn="describe_carrier_gateways";topkey='CarrierGateways';key="CarrierGatewayId";filterid=key
    elif type == "aws_ec2_client_vpn_authorization_rule":
        clfn="ec2";descfn="describe_client_vpn_authorization_rules";topkey='AuthorizationRules';key="ClientVpnEndpointId";filterid=key
    elif type == "aws_ec2_client_vpn_endpoint":
        clfn="ec2";descfn="describe_client_vpn_endpoints";topkey='ClientVpnEndpoints';key="ClientVpnEndpointId";filterid=key
    elif type == "aws_ec2_client_vpn_network_association":
        clfn="ec2";descfn="describe_client_vpn_network_associations";topkey='Associations';key="ClientVpnEndpointId";filterid=key
    elif type == "aws_ec2_client_vpn_route":
        clfn="ec2";descfn="describe_client_vpn_routes";topkey='Routes';key="ClientVpnEndpointId";filterid=key
    elif type == "aws_ec2_coip_pool":
        clfn="ec2";descfn="describe_coip_pools";topkey='CoipPools';key="CoipPoolId";filterid=key
    elif type == "aws_ec2_fleet":
        clfn="ec2";descfn="describe_fleets";topkey='Fleets';key="FleetId";filterid=key
    elif type == "aws_ec2_host":
        clfn="ec2";descfn="describe_hosts";topkey='Hosts';key="HostId";filterid=key
    elif type == "aws_ec2_image_block_public_access":
        clfn="ec2";descfn="describe_image_attribute";topkey='ImageAttribute';key="ImageId";filterid=key
    elif type == "aws_ec2_instance_connect_endpoint":
        clfn="ec2";descfn="describe_instance_connect_endpoints";topkey='InstanceConnectEndpoints';key="InstanceConnectEndpointId";filterid=key
    elif type == "aws_ec2_instance_state":
        clfn="ec2";descfn="describe_instance_status";topkey='InstanceStatuses';key="InstanceId";filterid=key
    #elif type == "aws_ec2_local_gateway":
    #    clfn="ec2";descfn="describe_local_gateways";topkey='LocalGateways';key="LocalGatewayId";filterid=key
    elif type == "aws_ec2_local_gateway_route":
        clfn="ec2";descfn="describe_local_gateway_routes";topkey='LocalGatewayRoutes';key="LocalGatewayRouteTableId";filterid=key
    #elif type == "aws_ec2_local_gateway_route_table":
    #    clfn="ec2";descfn="describe_local_gateway_route_tables";topkey='LocalGatewayRouteTables';key="LocalGatewayRouteTableId";filterid=key
    elif type == "aws_ec2_local_gateway_route_table_vpc_association":
        clfn="ec2";descfn="describe_local_gateway_route_tables";topkey='LocalGatewayRouteTables';key="LocalGatewayRouteTableId";filterid=key
    #elif type == "aws_ec2_local_gateway_route_tables":
    #    clfn="ec2";descfn="describe_local_gateway_route_tables";topkey='LocalGatewayRouteTables';key="LocalGatewayRouteTableId";filterid=key
    #elif type == "aws_ec2_local_gateway_virtual_interface":
    #    clfn="ec2";descfn="describe_local_gateway_virtual_interfaces";topkey='LocalGatewayVirtualInterfaces';key="LocalGatewayVirtualInterfaceId";filterid=key
    elif type == "aws_ec2_managed_prefix_list":
        clfn="ec2";descfn="describe_managed_prefix_lists";topkey='PrefixLists';key="PrefixListId";filterid=key
    elif type == "aws_ec2_managed_prefix_list_entry":
        clfn="ec2";descfn="describe_managed_prefix_list_entries";topkey='Entries';key="PrefixListId";filterid=key
    elif type == "aws_ec2_managed_prefix_lists":
        clfn="ec2";descfn="describe_managed_prefix_lists";topkey='PrefixLists';key="PrefixListId";filterid=key
    elif type == "aws_ec2_subnet_cidr_reservation":
        clfn="ec2";descfn="describe_subnet_cidr_reservations";topkey='SubnetCidrReservations';key="SubnetCidrReservationId";filterid=key
    elif type == "aws_ec2_tag":
        clfn="ec2";descfn="describe_tags";topkey='Tags';key="ResourceId";filterid=key
    elif type == "aws_ec2_traffic_mirror_filter":
        clfn="ec2";descfn="describe_traffic_mirror_filters";topkey='TrafficMirrorFilters';key="TrafficMirrorFilterId";filterid=key
    elif type == "aws_ec2_traffic_mirror_filter_rule":
        clfn="ec2";descfn="describe_traffic_mirror_filter_rules";topkey='TrafficMirrorFilterRules';key="TrafficMirrorFilterRuleId";filterid=key
    elif type == "aws_ec2_traffic_mirror_session":
        clfn="ec2";descfn="describe_traffic_mirror_sessions";topkey='TrafficMirrorSessions';key="TrafficMirrorSessionId";filterid=key
    elif type == "aws_ec2_traffic_mirror_target":
        clfn="ec2";descfn="describe_traffic_mirror_targets";topkey='TrafficMirrorTargets';key="TrafficMirrorTargetId";filterid=key
    elif type == "aws_ec2_transit_gateway":
        clfn="ec2";descfn="describe_transit_gateways";topkey='TransitGateways';key="TransitGatewayId";filterid=key
    elif type == "aws_ec2_transit_gateway_attachment":
        clfn="ec2";descfn="describe_transit_gateway_attachments";topkey='TransitGatewayAttachments';key="TransitGatewayAttachmentId";filterid=key
    elif type == "aws_ec2_transit_gateway_attachments":
        clfn="ec2";descfn="describe_transit_gateway_attachments";topkey='TransitGatewayAttachments';key="TransitGatewayAttachmentId";filterid=key
    elif type == "aws_ec2_transit_gateway_connect":
        clfn="ec2";descfn="describe_transit_gateway_connects";topkey='TransitGatewayConnects';key="TransitGatewayConnectId";filterid=key
    elif type == "aws_ec2_transit_gateway_connect_peer":
        clfn="ec2";descfn="describe_transit_gateway_connect_peers";topkey='TransitGatewayConnectPeers';key="TransitGatewayConnectPeerId";filterid=key
    elif type == "aws_ec2_transit_gateway_dx_gateway_attachment":
        clfn="ec2";descfn="describe_transit_gateway_dx_gateway_attachments";topkey='TransitGatewayDxGatewayAttachments';key="TransitGatewayDxGatewayAttachmentId";filterid=key
    elif type == "aws_ec2_transit_gateway_multicast_domain":
        clfn="ec2";descfn="describe_transit_gateway_multicast_domains";topkey='TransitGatewayMulticastDomains';key="TransitGatewayMulticastDomainId";filterid=key
    elif type == "aws_ec2_transit_gateway_multicast_domain_association":
        clfn="ec2";descfn="describe_transit_gateway_multicast_domains";topkey='TransitGatewayMulticastDomains';key="TransitGatewayMulticastDomainId";filterid=key
    elif type == "aws_ec2_transit_gateway_multicast_group_member":
        clfn="ec2";descfn="describe_transit_gateway_multicast_groups";topkey='TransitGatewayMulticastGroups';key="TransitGatewayMulticastGroupId";filterid=key
    elif type == "aws_ec2_transit_gateway_multicast_group_source":
        clfn="ec2";descfn="describe_transit_gateway_multicast_groups";topkey='TransitGatewayMulticastGroups';key="TransitGatewayMulticastGroupId";filterid=key
    elif type == "aws_ec2_transit_gateway_peering_attachment":
        clfn="ec2";descfn="describe_transit_gateway_peering_attachments";topkey='TransitGatewayPeeringAttachments';key="TransitGatewayPeeringAttachmentId";filterid=key
    elif type == "aws_ec2_transit_gateway_peering_attachment_accepter":
        clfn="ec2";descfn="describe_transit_gateway_peering_attachments";topkey='TransitGatewayPeeringAttachments';key="TransitGatewayPeeringAttachmentId";filterid=key
    elif type == "aws_ec2_transit_gateway_policy_table":
        clfn="ec2";descfn="describe_transit_gateway_policy_tables";topkey='TransitGatewayPolicyTables';key="TransitGatewayPolicyTableId";filterid=key
    elif type == "aws_ec2_transit_gateway_policy_table_association":
        clfn="ec2";descfn="describe_transit_gateway_policy_table_associations";topkey='TransitGatewayPolicyTableAssociations';key="TransitGatewayPolicyTableAssociationId";filterid=key
    elif type == "aws_ec2_transit_gateway_prefix_list_reference":
        clfn="ec2";descfn="describe_transit_gateway_prefix_list_references";topkey='TransitGatewayPrefixListReferences';key="TransitGatewayPrefixListReferenceId";filterid=key
    elif type == "aws_ec2_transit_gateway_route":
        clfn="ec2";descfn="describe_transit_gateway_routes";topkey='TransitGatewayRoutes';key="TransitGatewayRouteId";filterid=key
    elif type == "aws_ec2_transit_gateway_route_table":
        clfn="ec2";descfn="describe_transit_gateway_route_tables";topkey='TransitGatewayRouteTables';key="TransitGatewayRouteTableId";filterid=key
    elif type == "aws_ec2_transit_gateway_route_table_association":
        clfn="ec2";descfn="describe_transit_gateway_route_table_associations";topkey='TransitGatewayRouteTableAssociations';key="TransitGatewayRouteTableAssociationId";filterid=key
    elif type == "aws_ec2_transit_gateway_route_table_propropagation":
        clfn="ec2";descfn="describe_transit_gateway_route_table_propagations";topkey='TransitGatewayRouteTablePropagations';key="TransitGatewayRouteTablePropagationId";filterid=key
    #elif type == "aws_ec2_transit_gateway_route_table_routes":
    #    clfn="ec2";descfn="describe_transit_gateway_route_tables";topkey='TransitGatewayRouteTables';key="TransitGatewayRouteTableId";filterid=key
    # elif type == "aws_ec2_transit_gateway_route_tables":
    #     clfn="ec2";descfn="describe_transit_gateway_route_tables";topkey='TransitGatewayRouteTables';key="TransitGatewayRouteTableId";filterid=key
    elif type == "aws_ec2_transit_gateway_vpc_attachment":
        clfn="ec2";descfn="describe_transit_gateway_vpc_attachments";topkey='TransitGatewayVpcAttachments';key="TransitGatewayVpcAttachmentId";filterid=key
    elif type == "aws_ec2_transit_gateway_vpc_attachment_accepter":
        clfn="ec2";descfn="describe_transit_gateway_vpc_attachments";topkey='TransitGatewayVpcAttachments';key="TransitGatewayVpcAttachmentId";filterid=key
    elif type == "aws_ec2_transit_gateway_vpc_attachments":
        clfn="ec2";descfn="describe_transit_gateway_vpc_attachments";topkey='TransitGatewayVpcAttachments';key="TransitGatewayVpcAttachmentId";filterid=key
    elif type == "aws_ec2_transit_gateway_vpn_attachment":
        clfn="ec2";descfn="describe_transit_gateway_vpn_attachments";topkey='TransitGatewayVpnAttachments';key="TransitGatewayVpnAttachmentId";filterid=key
    elif type == "aws_ecr_authorization_token":
        clfn="ecr";descfn="describe_authorization_tokens";topkey='authorizationTokens';key="authorizationTokenId";filterid=key
    elif type == "aws_ecr_image":
        clfn="ecr";descfn="describe_images";topkey='images';key="imageId";filterid=key
    elif type == "aws_ecr_lifecycle_policy":
        clfn="ecr";descfn="describe_lifecycle_policy";topkey='lifecyclePolicyText';key="lifecyclePolicyText";filterid=key
    elif type == "aws_ecr_pull_through_cache_rule":
        clfn="ecr";descfn="describe_pull_through_cache_rules";topkey='pullThroughCacheRules';key="registryId";filterid=key
    elif type == "aws_ecr_registry_policy":
        clfn="ecr";descfn="describe_registry_policy";topkey='registryPolicyText';key="registryPolicyText";filterid=key
    elif type == "aws_ecr_registry_scanning_configuration":
        clfn="ecr";descfn="describe_registry_scanning_configuration";topkey='registryScanningConfiguration';key="registryScanningConfiguration";filterid=key
    elif type == "aws_ecr_replication_configuration":
        clfn="ecr";descfn="describe_replication_configuration";topkey='replicationConfiguration';key="replicationConfiguration";filterid=key
    elif type == "aws_ecr_repositories":
        clfn="ecr";descfn="describe_repositories";topkey='repositories';key="repositoryName";filterid=key
    elif type == "aws_ecr_repository":
        clfn="ecr";descfn="describe_repositories";topkey='repositories';key="repositoryName";filterid=key
    elif type == "aws_ecr_repository_policy":
        clfn="ecr";descfn="describe_repository_policy";topkey='policyText';key="policyText";filterid=key
    elif type == "aws_ecrpublic_authorization_token":
        clfn="ecr";descfn="describe_authorization_tokens";topkey='authorizationTokens';key="authorizationTokenId";filterid=key
    elif type == "aws_ecrpublic_repository":
        clfn="ecr";descfn="describe_repositories";topkey='repositories';key="repositoryName";filterid=key
    elif type == "aws_ecrpublic_repository_policy":
        clfn="ecr";descfn="describe_repository_policy";topkey='policyText';key="policyText";filterid=key
    elif type == "aws_ecs_account_setting_default":
        clfn="ecs";descfn="describe_account_settings";topkey='settings';key="name";filterid=key
    elif type == "aws_ecs_capacity_provider":
        clfn="ecs";descfn="describe_capacity_providers";topkey='capacityProviders';key="name";filterid=key
    #elif type == "aws_ecs_cluster":
    #    clfn="ecs";descfn="describe_clusters";topkey='clusters';key="clusterName";filterid=key
    elif type == "aws_ecs_cluster_capacity_providers":
        clfn="ecs";descfn="describe_clusters";topkey='clusters';key="clusterName";filterid=key
    elif type == "aws_ecs_container_definition":
        clfn="ecs";descfn="describe_container_definitions";topkey='containerDefinitions';key="name";filterid=key
    elif type == "aws_ecs_service":
        clfn="ecs";descfn="describe_services";topkey='services';key="serviceName";filterid=key
    elif type == "aws_ecs_tag":
        clfn="ecs";descfn="list_tags_for_resource";topkey='tags';key="key";filterid=key
    elif type == "aws_ecs_task_definition":
        clfn="ecs";descfn="describe_task_definition";topkey='taskDefinition';key="taskDefinitionArn";filterid=key
    elif type == "aws_ecs_task_execution":
        clfn="ecs";descfn="describe_task_execution";topkey='task';key="taskArn";filterid=key
    elif type == "aws_ecs_task_set":
        clfn="ecs";descfn="describe_task_sets";topkey='taskSets';key="id";filterid=key
    elif type == "aws_efs_access_point":
        clfn="efs";descfn="describe_access_points";topkey='AccessPoints';key="AccessPointId";filterid=key
    elif type == "aws_efs_backup_policy":
        clfn="efs";descfn="describe_backup_policy";topkey='BackupPolicy';key="BackupPolicy";filterid=key
    elif type == "aws_efs_file_system":
        clfn="efs";descfn="describe_file_systems";topkey='FileSystems';key="FileSystemId";filterid=key
    elif type == "aws_efs_file_system_policy":
        clfn="efs";descfn="describe_file_system_policy";topkey='Policy';key="Policy";filterid=key
    elif type == "aws_efs_mount_target":
        clfn="efs";descfn="describe_mount_targets";topkey='MountTargets';key="MountTargetId";filterid=key
    elif type == "aws_efs_replication_configuration":
        clfn="efs";descfn="describe_replication_configuration";topkey='ReplicationConfiguration';key="ReplicationConfiguration";filterid=key
    elif type == "aws_egress_only_internet_gateway":
        clfn="ec2";descfn="describe_egress_only_internet_gateways";topkey='EgressOnlyInternetGateways';key="EgressOnlyInternetGatewayId";filterid=key
    elif type == "aws_eip":
        clfn="ec2";descfn="describe_addresses";topkey='Addresses';key="PublicIp";filterid=key
    elif type == "aws_eip_association":
        clfn="ec2";descfn="describe_addresses";topkey='Addresses';key="PublicIp";filterid=key
    #elif type == "aws_eks_addon":
    #    clfn="eks";descfn="describe_addon_versions";topkey='addonVersions';key="addonVersion";filterid=key
    elif type == "aws_eks_addon_version":
        clfn="eks";descfn="describe_addon_versions";topkey='addonVersions';key="addonVersion";filterid=key
    #elif type == "aws_eks_cluster":
    #    clfn="eks";descfn="describe_cluster";topkey='cluster';key="name";filterid=key
    elif type == "aws_eks_cluster_auth":
        clfn="eks";descfn="describe_cluster";topkey='cluster';key="name";filterid=key
    #elif type == "aws_eks_fargate_profile":
    #    clfn="eks";descfn="describe_fargate_profiles";topkey='fargateProfiles';key="fargateProfileName";filterid=key
    #elif type == "aws_eks_identity_provider_config":
    #    clfn="eks";descfn="describe_identity_provider_config";topkey='identityProviderConfig';key="identityProviderConfigName";filterid=key
    #elif type == "aws_eks_node_group":
    #    clfn="eks";descfn="describe_nodegroup";topkey='nodegroup';key="nodegroupName";filterid=key
    elif type == "aws_eks_pod_identity_association":
        clfn="eks";descfn="describe_pod_identity_association";topkey='podIdentity';key="podIdentityArn";filterid=key
    elif type == "aws_elastic_beanstalk_application":
        clfn="elasticbeanstalk";descfn="describe_applications";topkey='Applications';key="ApplicationName";filterid=key
    elif type == "aws_elastic_beanstalk_application_version":
        clfn="elasticbeanstalk";descfn="describe_application_versions";topkey='ApplicationVersions';key="VersionLabel";filterid=key
    elif type == "aws_elastic_beanstalk_configuration_template":
        clfn="elasticbeanstalk";descfn="describe_configuration_settings";topkey='ConfigurationSettings';key="ApplicationName";filterid=key
    elif type == "aws_elastic_beanstalk_environment":
        clfn="elasticbeanstalk";descfn="describe_environments";topkey='Environments';key="EnvironmentName";filterid=key
    elif type == "aws_elastic_beanstalk_hosted_zone":
        clfn="elasticbeanstalk";descfn="describe_configuration_settings";topkey='ConfigurationSettings';key="ApplicationName";filterid=key
    elif type == "aws_elastic_beanstalk_solution_stack":
        clfn="elasticbeanstalk";descfn="describe_solution_stacks";topkey='SolutionStacks';key="SolutionStackName";filterid=key
    elif type == "aws_elasticache_cluster":
        clfn="elasticache";descfn="describe_cache_clusters";topkey='CacheClusters';key="CacheClusterId";filterid=key
    elif type == "aws_elasticache_global_replication_group":
        clfn="elasticache";descfn="describe_global_replication_groups";topkey='GlobalReplicationGroups';key="GlobalReplicationGroupId";filterid=key
    elif type == "aws_elasticache_parameter_group":
        clfn="elasticache";descfn="describe_cache_parameter_groups";topkey='CacheParameterGroups';key="CacheParameterGroupName";filterid=key
    elif type == "aws_elasticache_replication_group":
        clfn="elasticache";descfn="describe_replication_groups";topkey='ReplicationGroups';key="ReplicationGroupId";filterid=key
    elif type == "aws_elasticache_subnet_group":
        clfn="elasticache";descfn="describe_cache_subnet_groups";topkey='CacheSubnetGroups';key="CacheSubnetGroupName";filterid=key
    elif type == "aws_elasticache_user":
        clfn="elasticache";descfn="describe_users";topkey='Users';key="UserId";filterid=key
    elif type == "aws_elasticache_user_group":
        clfn="elasticache";descfn="describe_user_groups";topkey='UserGroups';key="UserGroupId";filterid=key
    elif type == "aws_elasticache_user_group_association":
        clfn="elasticache";descfn="describe_user_group_memberships";topkey='UserGroupMemberships';key="UserGroupId";filterid=key
    elif type == "aws_elasticsearch_domain":
        clfn="es";descfn="describe_elasticsearch_domains";topkey='DomainStatusList';key="DomainName";filterid=key
    elif type == "aws_elasticsearch_domain_policy":
        clfn="es";descfn="describe_elasticsearch_domain_policy";topkey='Policy';key="Policy";filterid=key
    #elif type == "aws_elasticsearch_domain_saml_options":
    elif type == "aws_elasticsearch_vpc_endpoint":
        clfn="es";descfn="describe_vpc_endpoints";topkey='VpcEndpoints';key="VpcEndpointId";filterid=key
    elif type == "aws_elastictranscoder_pipeline":
        clfn="elastictranscoder";descfn="list_pipelines";topkey='Pipelines';key="Id";filterid=key
    elif type == "aws_elastictranscoder_preset":
        clfn="elastictranscoder";descfn="list_presets";topkey='Presets';key="Id";filterid=key
    elif type == "aws_elb":
        clfn="elb";descfn="describe_load_balancers";topkey='LoadBalancerDescriptions';key="LoadBalancerName";filterid=key
    elif type == "aws_elb_attachment":
        clfn="elb";descfn="describe_load_balancer_attributes";topkey='LoadBalancerAttributes';key="LoadBalancerName";filterid=key
    elif type == "aws_elb_hosted_zone_id":
        clfn="elb";descfn="describe_load_balancers";topkey='LoadBalancerDescriptions';key="LoadBalancerName";filterid=key
    elif type == "aws_elb_service_account":
        clfn="elb";descfn="describe_load_balancers";topkey='LoadBalancerDescriptions';key="LoadBalancerName";filterid=key
    elif type == "aws_emr_block_public_access_configuration":
        clfn="emr";descfn="describe_block_public_access_configurations";topkey='BlockPublicAccessConfigurations';key="Id";filterid=key
    elif type == "aws_emr_cluster":
        clfn="emr";descfn="describe_cluster";topkey='Cluster';key="Id";filterid=key
    elif type == "aws_emr_instance_fleet":
        clfn="emr";descfn="describe_instance_fleets";topkey='InstanceFleets';key="Id";filterid=key
    elif type == "aws_emr_instance_group":
        clfn="emr";descfn="describe_instance_groups";topkey='InstanceGroups';key="Id";filterid=key
    elif type == "aws_emr_managed_scaling_policy":
        clfn="emr";descfn="describe_managed_scaling_policies";topkey='ManagedScalingPolicies';key="Id";filterid=key
    elif type == "aws_emr_release_labels":
        clfn="emr";descfn="describe_release_labels";topkey='ReleaseLabels';key="Id";filterid=key
    elif type == "aws_emr_security_configuration":
        clfn="emr";descfn="describe_security_configurations";topkey='SecurityConfigurations';key="Name";filterid=key
    elif type == "aws_emr_studio":
        clfn="emr";descfn="describe_studios";topkey='Studios';key="Id";filterid=key
    elif type == "aws_emr_studio_session_mapping":
        clfn="emr";descfn="describe_studio_session_mappings";topkey='SessionMappings';key="Id";filterid=key
    elif type == "aws_emr_supported_instance_types":
        clfn="emr";descfn="list_supported_instance_types";topkey='SupportedInstanceTypes';key="InstanceType";filterid=key
    elif type == "aws_emrcontainers_job_template":
        clfn="emrcontainers";descfn="list_job_templates";topkey='JobTemplates';key="Id";filterid=key
    elif type == "aws_emrcontainers_virtual_cluster":
        clfn="emrcontainers";descfn="list_virtual_clusters";topkey='VirtualClusters';key="Id";filterid=key
    elif type == "aws_emrserverless_application":
        clfn="emrserverless";descfn="list_applications";topkey='Applications';key="Id";filterid=key
    elif type == "aws_evidently_feature":
        clfn="evidently";descfn="list_features";topkey='Features';key="Name";filterid=key
    elif type == "aws_evidently_launch":
        clfn="evidently";descfn="list_launches";topkey='Launches';key="Name";filterid=key
    elif type == "aws_evidently_project":
        clfn="evidently";descfn="list_projects";topkey='Projects';key="Name";filterid=key
    elif type == "aws_evidently_segment":
        clfn="evidently";descfn="list_segments";topkey='Segments';key="Name";filterid=key
    elif type == "aws_finspace_kx_cluster":
        clfn="finspace";descfn="list_clusters";topkey='Clusters';key="ClusterId";filterid=key
    elif type == "aws_finspace_kx_database":
        clfn="finspace";descfn="list_databases";topkey='Databases';key="DatabaseId";filterid=key
    elif type == "aws_finspace_kx_dataview":
        clfn="finspace";descfn="list_data_views";topkey='DataViews';key="DataViewId";filterid=key
    elif type == "aws_finspace_kx_environment":
        clfn="finspace";descfn="list_environments";topkey='Environments';key="EnvironmentId";filterid=key
    elif type == "aws_finspace_kx_scaling_group":
        clfn="finspace";descfn="list_scaling_groups";topkey='ScalingGroups';key="ScalingGroupId";filterid=key
    elif type == "aws_finspace_kx_user":
        clfn="finspace";descfn="list_users";topkey='Users';key="UserId";filterid=key
    elif type == "aws_finspace_kx_volume":
        clfn="finspace";descfn="list_volumes";topkey='Volumes';key="VolumeId";filterid=key
    elif type == "aws_fis_experiment_template":
        clfn="fis";descfn="list_experiment_templates";topkey='ExperimentTemplates';key="Id";filterid=key
    #elif type == "aws_flow_log":
    #    clfn="ec2";descfn="describe_flow_logs";topkey='FlowLogs';key="FlowLogId";filterid=key
    elif type == "aws_fms_admin_account":
        clfn="fms";descfn="list_admin_accounts";topkey='AdminAccounts';key="AdminAccountId";filterid=key
    elif type == "aws_fms_policy":
        clfn="fms";descfn="list_policies";topkey='PolicyList';key="PolicyId";filterid=key
    elif type == "aws_fsx_backup":
        clfn="fsx";descfn="describe_backups";topkey='Backups';key="BackupId";filterid=key
    elif type == "aws_fsx_data_repository_association":
        clfn="fsx";descfn="describe_data_repository_associations";topkey='DataRepositoryAssociations';key="AssociationId";filterid=key
    elif type == "aws_fsx_file_cache":
        clfn="fsx";descfn="describe_file_caches";topkey='FileCaches';key="FileCacheId";filterid=key
    elif type == "aws_fsx_lustre_file_system":
        clfn="fsx";descfn="describe_file_systems";topkey='FileSystems';key="FileSystemId";filterid=key
    elif type == "aws_fsx_ontap_file_system":
        clfn="fsx";descfn="describe_file_systems";topkey='FileSystems';key="FileSystemId";filterid=key
    elif type == "aws_fsx_ontap_storage_virtual_machine":
        clfn="fsx";descfn="describe_storage_virtual_machines";topkey='StorageVirtualMachines';key="StorageVirtualMachineId";filterid=key
    elif type == "aws_fsx_ontap_storage_virtual_machines":
        clfn="fsx";descfn="describe_storage_virtual_machines";topkey='StorageVirtualMachines';key="StorageVirtualMachineId";filterid=key
    elif type == "aws_fsx_ontap_volume":
        clfn="fsx";descfn="describe_volumes";topkey='Volumes';key="VolumeId";filterid=key
    elif type == "aws_fsx_openzfs_file_system":
        clfn="fsx";descfn="describe_file_systems";topkey='FileSystems';key="FileSystemId";filterid=key
    elif type == "aws_fsx_openzfs_snapshot":
        clfn="fsx";descfn="describe_snapshots";topkey='Snapshots';key="SnapshotId";filterid=key
    elif type == "aws_fsx_openzfs_volume":
        clfn="fsx";descfn="describe_volumes";topkey='Volumes';key="VolumeId";filterid=key
    elif type == "aws_fsx_windows_file_system":
        clfn="fsx";descfn="describe_file_systems";topkey='FileSystems';key="FileSystemId";filterid=key
    elif type == "aws_gamelift_alias":
        clfn="gamelift";descfn="list_aliases";topkey='Aliases';key="AliasId";filterid=key
    elif type == "aws_gamelift_build":
        clfn="gamelift";descfn="list_builds";topkey='Builds';key="BuildId";filterid=key
    elif type == "aws_gamelift_fleet":
        clfn="gamelift";descfn="list_fleets";topkey='Fleets';key="FleetId";filterid=key
    elif type == "aws_gamelift_game_server_group":
        clfn="gamelift";descfn="list_game_server_groups";topkey='GameServerGroups';key="GameServerGroupId";filterid=key
    elif type == "aws_gamelift_game_session_queue":
        clfn="gamelift";descfn="list_game_session_queues";topkey='GameSessionQueues';key="GameSessionQueueName";filterid=key
    elif type == "aws_gamelift_script":
        clfn="gamelift";descfn="list_scripts";topkey='Scripts';key="ScriptId";filterid=key
    elif type == "aws_glacier_vault":
        clfn="glacier";descfn="list_vaults";topkey='VaultList';key="VaultName";filterid=key
    elif type == "aws_glacier_vault_lock":
        clfn="glacier";descfn="list_vault_locks";topkey='VaultLockList';key="VaultLockId";filterid=key
    elif type == "aws_globalaccelerator_accelerator":
        clfn="globalaccelerator";descfn="list_accelerators";topkey='Accelerators';key="AcceleratorArn";filterid=key
    elif type == "aws_globalaccelerator_custom_routing_accelerator":
        clfn="globalaccelerator";descfn="list_accelerators";topkey='Accelerators';key="AcceleratorArn";filterid=key
    elif type == "aws_globalaccelerator_custom_routing_endpoint_group":
        clfn="globalaccelerator";descfn="list_endpoint_groups";topkey='EndpointGroups';key="EndpointGroupArn";filterid=key
    elif type == "aws_globalaccelerator_custom_routing_listener":
        clfn="globalaccelerator";descfn="list_listeners";topkey='Listeners';key="ListenerArn";filterid=key
    elif type == "aws_globalaccelerator_endpoint_group":
        clfn="globalaccelerator";descfn="list_endpoint_groups";topkey='EndpointGroups';key="EndpointGroupArn";filterid=key
    elif type == "aws_globalaccelerator_listener":
        clfn="globalaccelerator";descfn="list_listeners";topkey='Listeners';key="ListenerArn";filterid=key
    #elif type == "aws_glue_catalog_database":
    #    clfn="glue";descfn="list_databases";topkey='DatabaseList';key="Name";filterid=key
    elif type == "aws_glue_catalog_table":
        clfn="glue";descfn="list_tables";topkey='TableList';key="Name";filterid=key
    elif type == "aws_glue_classifier":
        clfn="glue";descfn="list_classifiers";topkey='Classifiers';key="Name";filterid=key
    elif type == "aws_glue_connection":
        clfn="glue";descfn="list_connections";topkey='ConnectionList';key="Name";filterid=key
    #elif type == "aws_glue_crawler":
    #    clfn="glue";descfn="list_crawlers";topkey='CrawlerNames';key="Name";filterid=key
    elif type == "aws_glue_data_catalog_encryption_settings":
        clfn="glue";descfn="get_data_catalog_encryption_settings";topkey='DataCatalogEncryptionSettings';key="CatalogId";filterid=key
    elif type == "aws_glue_data_quality_ruleset":
        clfn="glue";descfn="list_data_quality_rulesets";topkey='RulesetNames';key="Name";filterid=key
    elif type == "aws_glue_dev_endpoint":
        clfn="glue";descfn="list_dev_endpoints";topkey='DevEndpoints';key="EndpointName";filterid=key
    elif type == "aws_glue_job":
        clfn="glue";descfn="list_jobs";topkey='JobNames';key="Name";filterid=key
    elif type == "aws_glue_ml_transform":
        clfn="glue";descfn="list_ml_transforms";topkey='TransformIds';key="TransformId";filterid=key
    elif type == "aws_glue_partition":
        clfn="glue";descfn="list_partitions";topkey='Partitions';key="PartitionValues";filterid=key
    elif type == "aws_glue_partition_index":
        clfn="glue";descfn="list_partition_indexes";topkey='PartitionIndexNames';key="Name";filterid=key
    elif type == "aws_glue_registry":
        clfn="glue";descfn="list_registries";topkey='Registries';key="RegistryId";filterid=key
    elif type == "aws_glue_resource_policy":
        clfn="glue";descfn="list_resource_policies";topkey='ResourcePolicies';key="PolicyHash";filterid=key
    elif type == "aws_glue_schema":
        clfn="glue";descfn="list_schemas";topkey='Schemas';key="SchemaId";filterid=key
    elif type == "aws_glue_script":
        clfn="glue";descfn="list_scripts";topkey='Scripts';key="ScriptId";filterid=key
    elif type == "aws_glue_security_configuration":
        clfn="glue";descfn="list_security_configurations";topkey='SecurityConfigurations';key="Name";filterid=key
    elif type == "aws_glue_trigger":
        clfn="glue";descfn="list_triggers";topkey='Triggers';key="Name";filterid=key
    elif type == "aws_glue_user_defined_function":
        clfn="glue";descfn="list_user_defined_functions";topkey='UserDefinedFunctionNames';key="Name";filterid=key
    elif type == "aws_glue_workflow":
        clfn="glue";descfn="list_workflows";topkey='Workflows';key="Name";filterid=key
    elif type == "aws_grafana_license_association":
        clfn="grafana";descfn="list_license_associations";topkey='LicenseAssociations';key="LicenseAssociationArn";filterid=key
    elif type == "aws_grafana_role_association":
        clfn="grafana";descfn="list_role_associations";topkey='RoleAssociations';key="RoleAssociationArn";filterid=key
    elif type == "aws_grafana_workspace":
        clfn="grafana";descfn="list_workspaces";topkey='Workspaces';key="WorkspaceId";filterid=key
    elif type == "aws_grafana_workspace_api_key":
        clfn="grafana";descfn="list_workspace_api_keys";topkey='ApiKeys';key="KeyId";filterid=key
    elif type == "aws_grafana_workspace_saml_configuration":
        clfn="grafana";descfn="list_workspace_saml_configurations";topkey='SamlConfigurations';key="SamlConfigurationId";filterid=key
    elif type == "aws_guardduty_detector":
        clfn="guardduty";descfn="list_detectors";topkey='DetectorIds';key="DetectorId";filterid=key
    elif type == "aws_guardduty_detector_feature":
        clfn="guardduty";descfn="list_detector_features";topkey='DetectorFeatures';key="DetectorFeatureName";filterid=key
    elif type == "aws_guardduty_filter":
        clfn="guardduty";descfn="list_filters";topkey='FilterNames';key="FilterName";filterid=key
    elif type == "aws_guardduty_finding_ids":
        clfn="guardduty";descfn="list_findings";topkey='FindingIds';key="FindingId";filterid=key
    elif type == "aws_guardduty_invite_accepter":
        clfn="guardduty";descfn="list_invitation_accepters";topkey='InvitationAccepters';key="InvitationAccepterId";filterid=key
    elif type == "aws_guardduty_ipset":
        clfn="guardduty";descfn="list_ip_sets";topkey='IpSetIds';key="IpSetId";filterid=key
    elif type == "aws_guardduty_member":
        clfn="guardduty";descfn="list_members";topkey='Members';key="MemberId";filterid=key
    elif type == "aws_guardduty_organization_admin_account":
        clfn="guardduty";descfn="list_organization_admin_accounts";topkey='AdminAccounts';key="AdminAccountId";filterid=key
    elif type == "aws_guardduty_organization_configuration":
        clfn="guardduty";descfn="list_organization_configurations";topkey='OrganizationConfigurations';key="OrganizationConfigurationId";filterid=key
    elif type == "aws_guardduty_organization_configuration_feature":
        clfn="guardduty";descfn="list_organization_configuration_features";topkey='OrganizationConfigurationFeatures';key="OrganizationConfigurationFeature";filterid=key
    elif type == "aws_guardduty_publishing_destination":
        clfn="guardduty";descfn="list_publishing_destinations";topkey='PublishingDestinations';key="DestinationId";filterid=key
    elif type == "aws_guardduty_threatintelset":
        clfn="guardduty";descfn="list_threat_intel_sets";topkey='ThreatIntelSetIds';key="ThreatIntelSetId";filterid=key
    elif type == "aws_iam_access_key":
        clfn="iam";descfn="list_access_keys";topkey='AccessKeyMetadata';key="AccessKeyId";filterid=key
    elif type == "aws_iam_access_keys":
        clfn="iam";descfn="list_access_keys";topkey='AccessKeyMetadata';key="AccessKeyId";filterid=key
    elif type == "aws_iam_account_alias":
        clfn="iam";descfn="list_account_aliases";topkey='AccountAliases';key="AccountAlias";filterid=key
    elif type == "aws_iam_account_password_policy":
        clfn="iam";descfn="get_account_password_policy";topkey='PasswordPolicy';key="PasswordPolicy";filterid=key
    elif type == "aws_iam_group":
        clfn="iam";descfn="list_groups";topkey='Groups';key="GroupName";filterid=key
    elif type == "aws_iam_group_membership":
        clfn="iam";descfn="get_group";topkey='Group';key="GroupName";filterid=key
    elif type == "aws_iam_group_policy":
        clfn="iam";descfn="list_groups_for_user";topkey='Groups';key="GroupName";filterid=key
    elif type == "aws_iam_group_policy_attachment":
        clfn="iam";descfn="get_group_policy";topkey='GroupPolicy';key="GroupName";filterid=key
    #elif type == "aws_iam_instance_profile":
    #    clfn="iam";descfn="list_instance_profiles";topkey='InstanceProfiles';key="InstanceProfileName";filterid=key
    #elif type == "aws_iam_instance_profiles":
    #    clfn="iam";descfn="list_instance_profiles";topkey='InstanceProfiles';key="InstanceProfileName";filterid=key
    elif type == "aws_iam_openid_connect_provider":
        clfn="iam";descfn="list_open_id_connect_providers";topkey='OpenIDConnectProviderList';key="Arn";filterid=key
    elif type == "aws_iam_policy":
        clfn="iam";descfn="list_policies";topkey='Policies';key="PolicyName";filterid=key
    elif type == "aws_iam_policy_attachment":
        clfn="iam";descfn="get_policy";topkey='Policy';key="PolicyArn";filterid=key
    elif type == "aws_iam_policy_document":
        clfn="iam";descfn="get_policy_version";topkey='PolicyVersion';key="PolicyArn";filterid=key
    elif type == "aws_iam_principal_policy_simulation":
        clfn="iam";descfn="simulate_principal_policy";topkey='EvaluationResults';key="EvaluationResultIdentifier";filterid=key
    #elif type == "aws_iam_role":
    #    clfn="iam";descfn="list_roles";topkey='Roles';key="RoleName";filterid=key
    #elif type == "aws_iam_role_policy":
    #    clfn="iam";descfn="list_role_policies";topkey='PolicyNames';key="PolicyName";filterid=key
    #elif type == "aws_iam_role_policy_attachment":
    #    clfn="iam";descfn="get_role_policy";topkey='Policy';key="RoleName";filterid=key
    elif type == "aws_iam_saml_provider":
        clfn="iam";descfn="list_saml_providers";topkey='SAMLProviderList';key="Arn";filterid=key
    elif type == "aws_iam_security_token_service_preferences":
        clfn="iam";descfn="get_account_token_version";topkey='AccountTokenVersion';key="AccountTokenVersion";filterid=key
    elif type == "aws_iam_server_certificate":
        clfn="iam";descfn="list_server_certificates";topkey='ServerCertificateMetadataList';key="ServerCertificateName";filterid=key
    elif type == "aws_iam_service_linked_role":
        clfn="iam";descfn="list_service_linked_roles";topkey='ServiceLinkedRoles';key="Arn";filterid=key
    elif type == "aws_iam_service_specific_credential":
        clfn="iam";descfn="list_service_specific_credentials";topkey='ServiceSpecificCredentials';key="ServiceSpecificCredentialId";filterid=key
    elif type == "aws_iam_session_context":
        clfn="iam";descfn="get_session_context";topkey='SessionContext';key="SessionContextKey";filterid=key
    elif type == "aws_iam_signing_certificate":
        clfn="iam";descfn="list_signing_certificates";topkey='Certificates';key="CertificateId";filterid=key
    #elif type == "aws_iam_user":
    #    clfn="iam";descfn="list_users";topkey='Users';key="UserName";filterid=key
    elif type == "aws_iam_user_group_membership":
        clfn="iam";descfn="get_user_group_membership";topkey='Groups';key="GroupName";filterid=key
    elif type == "aws_iam_user_login_profile":
        clfn="iam";descfn="get_login_profile";topkey='LoginProfile';key="UserName";filterid=key
    elif type == "aws_iam_user_policy":
        clfn="iam";descfn="list_user_policies";topkey='PolicyNames';key="PolicyName";filterid=key
    elif type == "aws_iam_user_policy_attachment":
        clfn="iam";descfn="get_user_policy";topkey='Policy';key="UserName";filterid=key
    elif type == "aws_iam_user_ssh_key":
        clfn="iam";descfn="list_ssh_public_keys";topkey='SSHPublicKeys';key="SSHPublicKeyId";filterid=key
    elif type == "aws_iam_users":
        clfn="iam";descfn="list_users";topkey='Users';key="UserName";filterid=key
    elif type == "aws_iam_virtual_mfa_device":
        clfn="iam";descfn="list_virtual_mfa_devices";topkey='VirtualMFADevices';key="SerialNumber";filterid=key
    elif type == "aws_identitystore_group":
        clfn="identitystore";descfn="list_groups";topkey='Groups';key="GroupId";filterid=key
    elif type == "aws_identitystore_group_membership":
        clfn="identitystore";descfn="list_group_memberships";topkey='GroupMemberships';key="GroupId";filterid=key
    elif type == "aws_identitystore_user":
        clfn="identitystore";descfn="list_users";topkey='Users';key="UserId";filterid=key
    elif type == "aws_imagebuilder_component":
        clfn="imagebuilder";descfn="list_components";topkey='Components';key="ComponentArn";filterid=key
    elif type == "aws_imagebuilder_components":
        clfn="imagebuilder";descfn="list_components";topkey='Components';key="ComponentArn";filterid=key
    elif type == "aws_imagebuilder_container_recipe":
        clfn="imagebuilder";descfn="list_container_recipes";topkey='ContainerRecipes';key="ContainerRecipeArn";filterid=key
    elif type == "aws_imagebuilder_container_recipes":
        clfn="imagebuilder";descfn="list_container_recipes";topkey='ContainerRecipes';key="ContainerRecipeArn";filterid=key
    elif type == "aws_imagebuilder_distribution_configuration":
        clfn="imagebuilder";descfn="list_distribution_configurations";topkey='DistributionConfigurations';key="DistributionConfigurationArn";filterid=key
    elif type == "aws_imagebuilder_distribution_configurations":
        clfn="imagebuilder";descfn="list_distribution_configurations";topkey='DistributionConfigurations';key="DistributionConfigurationArn";filterid=key
    elif type == "aws_imagebuilder_image":
        clfn="imagebuilder";descfn="list_images";topkey='Images';key="ImageArn";filterid=key
    elif type == "aws_imagebuilder_image_pipeline":
        clfn="imagebuilder";descfn="list_image_pipelines";topkey='ImagePipelines';key="ImagePipelineArn";filterid=key
    elif type == "aws_imagebuilder_image_pipelines":
        clfn="imagebuilder";descfn="list_image_pipelines";topkey='ImagePipelines';key="ImagePipelineArn";filterid=key
    elif type == "aws_imagebuilder_image_recipe":
        clfn="imagebuilder";descfn="list_image_recipes";topkey='ImageRecipes';key="ImageRecipeArn";filterid=key
    elif type == "aws_imagebuilder_image_recipes":
        clfn="imagebuilder";descfn="list_image_recipes";topkey='ImageRecipes';key="ImageRecipeArn";filterid=key
    elif type == "aws_imagebuilder_infrastructure_configuration":
        clfn="imagebuilder";descfn="list_infrastructure_configurations";topkey='InfrastructureConfigurations';key="InfrastructureConfigurationArn";filterid=key
    elif type == "aws_imagebuilder_infrastructure_configurations":
        clfn="imagebuilder";descfn="list_infrastructure_configurations";topkey='InfrastructureConfigurations';key="InfrastructureConfigurationArn";filterid=key
    elif type == "aws_inspector2_delegated_admin_account":
        clfn="inspector2";descfn="list_delegated_admin_accounts";topkey='DelegatedAdminAccounts';key="AccountId";filterid=key
    elif type == "aws_inspector2_enabler":
        clfn="inspector2";descfn="list_enablers";topkey='Enablers';key="Name";filterid=key
    elif type == "aws_inspector2_member_association":
        clfn="inspector2";descfn="list_member_associations";topkey='MemberAssociations';key="AccountId";filterid=key
    elif type == "aws_inspector2_organization_configuration":
        clfn="inspector2";descfn="list_organization_configurations";topkey='OrganizationConfigurations';key="OrganizationConfigurationArn";filterid=key
    elif type == "aws_inspector_assessment_target":
        clfn="inspector";descfn="list_assessment_targets";topkey='AssessmentTargets';key="Name";filterid=key
    elif type == "aws_inspector_assessment_template":
        clfn="inspector";descfn="list_assessment_templates";topkey='AssessmentTemplates';key="Name";filterid=key
    elif type == "aws_inspector_resource_group":
        clfn="inspector";descfn="list_resource_groups";topkey='ResourceGroups';key="Name";filterid=key
    elif type == "aws_inspector_rules_packages":
        clfn="inspector";descfn="list_rules_packages";topkey='RulesPackages';key="Name";filterid=key
    #elif type == "aws_instance":
    #    clfn="ec2";descfn="describe_instances";topkey='Reservations';key="Instances";filterid=key
    #elif type == "aws_internet_gateway":
    #    clfn="ec2";descfn="describe_internet_gateways";topkey='InternetGateways';key="InternetGatewayId";filterid=key
    elif type == "aws_internet_gateway_attachment":
        clfn="ec2";descfn="describe_internet_gateway_attachments";topkey='InternetGatewayAttachments';key="InternetGatewayId";filterid=key
    elif type == "aws_internetmonitor_monitor":
        clfn="internetmonitor";descfn="list_monitors";topkey='Monitors';key="MonitorId";filterid=key
    elif type == "aws_iot_authorizer":
        clfn="iot";descfn="list_authorizers";topkey='Authorizers';key="AuthorizerName";filterid=key
    elif type == "aws_iot_billing_group":
        clfn="iot";descfn="list_billing_groups";topkey='BillingGroups';key="BillingGroupName";filterid=key
    elif type == "aws_iot_ca_certificate":
        clfn="iot";descfn="list_ca_certificates";topkey='CACertificates';key="Id";filterid=key
    elif type == "aws_iot_certificate":
        clfn="iot";descfn="list_certificates";topkey='Certificates';key="CertificateId";filterid=key
    elif type == "aws_iot_domain_configuration":
        clfn="iot";descfn="list_domain_configurations";topkey='DomainConfigurations';key="DomainConfigurationName";filterid=key
    elif type == "aws_iot_endpoint":
        clfn="iot";descfn="list_endpoints";topkey='Endpoints';key="EndpointAddress";filterid=key
    elif type == "aws_iot_event_configurations":
        clfn="iot";descfn="list_event_configurations";topkey='EventConfigurations';key="EventConfigurationName";filterid=key
    elif type == "aws_iot_indexing_configuration":
        clfn="iot";descfn="list_indexing_configurations";topkey='IndexingConfigurations';key="IndexingConfigurationName";filterid=key
    elif type == "aws_iot_logging_options":
        clfn="iot";descfn="describe_logging_options";topkey='LoggingOptions';key="roleArn";filterid=key
    elif type == "aws_iot_policy":
        clfn="iot";descfn="list_policies";topkey='policies';key="policyName";filterid=key
    elif type == "aws_iot_policy_attachment":
        clfn="iot";descfn="list_policies";topkey='Policies';key="PolicyName";filterid=key
    elif type == "aws_iot_provisioning_template":
        clfn="iot";descfn="list_provisioning_templates";topkey='ProvisioningTemplates';key="TemplateName";filterid=key
    elif type == "aws_iot_registration_code":
        clfn="iot";descfn="list_registration_code";topkey='RegistrationCode';key="RegistrationCode";filterid=key
    elif type == "aws_iot_role_alias":
        clfn="iot";descfn="list_role_aliases";topkey='RoleAliases';key="RoleAliasName";filterid=key
    elif type == "aws_iot_thing":
        clfn="iot";descfn="list_things";topkey='things';key="thingName";filterid=key
    elif type == "aws_iot_thing_group":
        clfn="iot";descfn="list_thing_groups";topkey='ThingGroups';key="ThingGroupName";filterid=key
    elif type == "aws_iot_thing_group_membership":
        clfn="iot";descfn="list_thing_group_memberships";topkey='ThingGroupMemberships';key="ThingGroupName";filterid=key
    elif type == "aws_iot_thing_principal_attachment":
        clfn="iot";descfn="list_thing_principal_attachments";topkey='ThingPrincipalAttachments';key="ThingName";filterid=key
    elif type == "aws_iot_thing_type":
        clfn="iot";descfn="list_thing_types";topkey='ThingTypes';key="ThingTypeName";filterid=key
    elif type == "aws_iot_topic_rule":
        clfn="iot";descfn="list_topic_rules";topkey='rules';key="ruleName";filterid=key
    elif type == "aws_iot_topic_rule_destination":
        clfn="iot";descfn="list_topic_rule_destinations";topkey='destinations';key="destinationName";filterid=key
    elif type == "aws_ip_ranges":
        clfn="ec2";descfn="describe_managed_prefix_lists";topkey='PrefixLists';key="PrefixListId";filterid=key
    elif type == "aws_ivs_channel":
        clfn="ivs";descfn="list_channels";topkey='Channels';key="arn";filterid=key
    elif type == "aws_ivs_playback_key_pair":
        clfn="ivs";descfn="list_playback_key_pairs";topkey='PlaybackKeyPairs';key="arn";filterid=key
    elif type == "aws_ivs_recording_configuration":
        clfn="ivs";descfn="list_recording_configurations";topkey='RecordingConfigurations';key="arn";filterid=key
    elif type == "aws_ivs_stream_key":
        clfn="ivs";descfn="list_stream_keys";topkey='StreamKeys';key="arn";filterid=key
    elif type == "aws_ivschat_logging_configuration":
        clfn="ivschat";descfn="list_logging_configurations";topkey='LoggingConfigurations';key="arn";filterid=key
    elif type == "aws_ivschat_room":
        clfn="ivschat";descfn="list_rooms";topkey='Rooms';key="arn";filterid=key
    elif type == "aws_kendra_data_source":
        clfn="kendra";descfn="list_data_sources";topkey='DataSources';key="Id";filterid=key
    elif type == "aws_kendra_experience":
        clfn="kendra";descfn="list_experiences";topkey='Experiences';key="Id";filterid=key
    elif type == "aws_kendra_faq":
        clfn="kendra";descfn="list_faqs";topkey='Faqs';key="Id";filterid=key
    elif type == "aws_kendra_index":
        clfn="kendra";descfn="list_indices";topkey='Indices';key="Id";filterid=key
    elif type == "aws_kendra_query_suggestions_block_list":
        clfn="kendra";descfn="list_query_suggestions_block_lists";topkey='QuerySuggestionsBlockLists';key="Id";filterid=key
    elif type == "aws_kendra_thesaurus":
        clfn="kendra";descfn="list_thesauri";topkey='Thesauri';key="Id";filterid=key
    #elif type == "aws_key_pair":
    #    clfn="ec2";descfn="describe_key_pairs";topkey='KeyPairs';key="KeyName";filterid=key
    elif type == "aws_keyspaces_keyspace":
        clfn="keyspaces";descfn="list_keyspaces";topkey='Keyspaces';key="Name";filterid=key
    elif type == "aws_keyspaces_table":
        clfn="keyspaces";descfn="list_tables";topkey='Tables';key="Name";filterid=key
    elif type == "aws_kinesis_analytics_application":
        clfn="kinesisanalytics";descfn="list_applications";topkey='ApplicationSummaries';key="ApplicationName";filterid=key
    elif type == "aws_kinesis_firehose_delivery_stream":
        clfn="firehose";descfn="list_delivery_streams";topkey='DeliveryStreamNames';key="DeliveryStreamName";filterid=key
    #elif type == "aws_kinesis_stream":
    #    clfn="kinesis";descfn="list_streams";topkey='StreamNames';key="StreamName";filterid=key
    elif type == "aws_kinesis_stream_consumer":
        clfn="kinesis";descfn="list_stream_consumers";topkey='Consumers';key="ConsumerName";filterid=key
    elif type == "aws_kinesis_video_stream":
        clfn="kinesisvideo";descfn="list_streams";topkey='StreamNames';key="StreamName";filterid=key
    elif type == "aws_kinesisanalyticsv2_application":
        clfn="kinesisanalyticsv2";descfn="list_applications";topkey='ApplicationSummaries';key="ApplicationName";filterid=key
    elif type == "aws_kinesisanalyticsv2_application_snapshot":
        clfn="kinesisanalyticsv2";descfn="list_application_snapshots";topkey='ApplicationSnapshots';key="SnapshotName";filterid=key
    #elif type == "aws_kms_alias":
    #    clfn="kms";descfn="list_aliases";topkey='Aliases';key="AliasName";filterid=key
    elif type == "aws_kms_ciphertext":
        clfn="kms";descfn="list_grants";topkey='Grants';key="GrantId";filterid=key
    elif type == "aws_kms_custom_key_store":
        clfn="kms";descfn="list_custom_key_stores";topkey='CustomKeyStores';key="CustomKeyStoreId";filterid=key
    elif type == "aws_kms_external_key":
        clfn="kms";descfn="list_external_keys";topkey='ExternalKeys';key="KeyId";filterid=key
    elif type == "aws_kms_grant":
        clfn="kms";descfn="list_grants";topkey='Grants';key="GrantId";filterid=key
    #elif type == "aws_kms_key":
    #    clfn="kms";descfn="list_keys";topkey='Keys';key="KeyId";filterid=key
    elif type == "aws_kms_key_policy":
        clfn="kms";descfn="list_key_policies";topkey='PolicyNames';key="PolicyName";filterid=key
    elif type == "aws_kms_public_key":
        clfn="kms";descfn="list_public_keys";topkey='PublicKeys';key="KeyId";filterid=key
    elif type == "aws_kms_replica_external_key":
        clfn="kms";descfn="list_replica_keys";topkey='ReplicaKeys';key="KeyId";filterid=key
    elif type == "aws_kms_replica_key":
        clfn="kms";descfn="list_replica_keys";topkey='ReplicaKeys';key="KeyId";filterid=key
    elif type == "aws_kms_secret":
        clfn="kms";descfn="list_secrets";topkey='SecretList';key="SecretId";filterid=key
    elif type == "aws_kms_secrets":
        clfn="kms";descfn="list_secrets";topkey='SecretList';key="SecretId";filterid=key
    elif type == "aws_lakeformation_data_lake_settings":
        clfn="lakeformation";descfn="list_data_lake_settings";topkey='DataLakeSettings';key="DataLakeSettingsId";filterid=key
    elif type == "aws_lakeformation_lf_tag":
        clfn="lakeformation";descfn="list_lf_tags";topkey='LFTags';key="LFTagKey";filterid=key
    elif type == "aws_lakeformation_permissions":
        clfn="lakeformation";descfn="list_permissions";topkey='Permissions';key="Principal";filterid=key
    elif type == "aws_lakeformation_resource":
        clfn="lakeformation";descfn="list_resources";topkey='ResourceInfoList';key="ResourceArn";filterid=key
    elif type == "aws_lakeformation_resource_lf_tags":
        clfn="lakeformation";descfn="list_resource_lf_tags";topkey='LFTags';key="LFTagKey";filterid=key
    #elif type == "aws_lambda_alias":
    #    clfn="lambda";descfn="list_aliases";topkey='Aliases';key="Name";filterid=key
    elif type == "aws_lambda_code_signing_config":
        clfn="lambda";descfn="list_code_signing_configs";topkey='CodeSigningConfigs';key="CodeSigningConfigArn";filterid=key
    #elif type == "aws_lambda_event_source_mapping":
    #    clfn="lambda";descfn="list_event_source_mappings";topkey='EventSourceMappings';key="UUID";filterid=key
    #elif type == "aws_lambda_function":
    #    clfn="lambda";descfn="list_functions";topkey='Functions';key="FunctionName";filterid=key
    #elif type == "aws_lambda_function_event_invoke_config":
    #    clfn="lambda";descfn="list_function_event_invoke_configs";topkey='FunctionEventInvokeConfigs';key="FunctionName";filterid=key
    elif type == "aws_lambda_function_url":
        clfn="lambda";descfn="list_function_url_configs";topkey='FunctionUrlConfigs';key="FunctionName";filterid=key
    elif type == "aws_lambda_functions":
        clfn="lambda";descfn="list_functions";topkey='Functions';key="FunctionName";filterid=key
    elif type == "aws_lambda_invocation":
        clfn="lambda";descfn="list_functions";topkey='Functions';key="FunctionName";filterid=key
    #elif type == "aws_lambda_layer_version":
    #    clfn="lambda";descfn="list_layer_versions";topkey='LayerVersions';key="LayerName";filterid=key
    elif type == "aws_lambda_layer_version_permission":
        clfn="lambda";descfn="list_layer_version_permissions";topkey='LayerVersionPermissions';key="LayerName";filterid=key
    #elif type == "aws_lambda_permission":
    #    clfn="lambda";descfn="list_functions";topkey='Functions';key="FunctionName";filterid=key
    elif type == "aws_lambda_provisioned_concurrency_config":
        clfn="lambda";descfn="list_provisioned_concurrency_configs";topkey='ProvisionedConcurrencyConfigs';key="FunctionName";filterid=key
    #elif type == "aws_launch_configuration":
    #    clfn="autoscaling";descfn="describe_launch_configurations";topkey='LaunchConfigurations';key="LaunchConfigurationName";filterid=key
    #elif type == "aws_launch_template":
    #    clfn="ec2";descfn="describe_launch_templates";topkey='LaunchTemplates';key="LaunchTemplateId";filterid=key
    #elif type == "aws_lb":
    #    clfn="elbv2";descfn="describe_load_balancers";topkey='LoadBalancers';key="LoadBalancerArn";filterid=key
    elif type == "aws_lb_cookie_stickiness_policy":
        clfn="elbv2";descfn="describe_load_balancer_policies";topkey='PolicyDescriptions';key="PolicyName";filterid=key
    elif type == "aws_lb_hosted_zone_id":
        clfn="elbv2";descfn="describe_load_balancers";topkey='LoadBalancers';key="LoadBalancerArn";filterid=key
    elif type == "aws_lb_listener":
        clfn="elbv2";descfn="describe_listeners";topkey='Listeners';key="ListenerArn";filterid=key
    elif type == "aws_lb_listener_certificate":
        clfn="elbv2";descfn="describe_listener_certificates";topkey='Certificates';key="CertificateArn";filterid=key
    elif type == "aws_lb_listener_rule":
        clfn="elbv2";descfn="describe_rules";topkey='Rules';key="RuleArn";filterid=key
    elif type == "aws_lb_ssl_negotiation_policy":
        clfn="elbv2";descfn="describe_ssl_policies";topkey='SslPolicies';key="SslPolicyName";filterid=key
    elif type == "aws_lb_target_group":
        clfn="elbv2";descfn="describe_target_groups";topkey='TargetGroups';key="TargetGroupArn";filterid=key
    elif type == "aws_lb_target_group_attachment":
        clfn="elbv2";descfn="describe_target_group_attributes";topkey='Attributes';key="Key";filterid=key
    elif type == "aws_lb_trust_store":
        clfn="elbv2";descfn="describe_load_balancer_attributes";topkey='Attributes';key="Key";filterid=key
    elif type == "aws_lb_trust_store_revocation":
        clfn="elbv2";descfn="describe_load_balancer_attributes";topkey='Attributes';key="Key";filterid=key
    elif type == "aws_lbs":
        clfn="elbv2";descfn="describe_load_balancers";topkey='LoadBalancers';key="LoadBalancerArn";filterid=key
    elif type == "aws_lex_bot":
        clfn="lex";descfn="get_bots";topkey='bots';key="name";filterid=key
    elif type == "aws_lex_bot_alias":
        clfn="lex";descfn="get_bot_aliases";topkey='aliases';key="name";filterid=key
    elif type == "aws_lex_intent":
        clfn="lex";descfn="get_intents";topkey='intents';key="name";filterid=key
    elif type == "aws_lex_slot_type":
        clfn="lex";descfn="get_slot_types";topkey='slotTypes';key="name";filterid=key
    elif type == "aws_lexv2models_bot":
        clfn="lexv2";descfn="list_bots";topkey='bots';key="name";filterid=key
    elif type == "aws_lexv2models_bot_locale":
        clfn="lexv2";descfn="list_bot_locales";topkey='botLocales';key="name";filterid=key
    elif type == "aws_lexv2models_bot_version":
        clfn="lexv2";descfn="list_bot_versions";topkey='botVersions';key="name";filterid=key
    elif type == "aws_licensemanager_association":
        clfn="licensemanager";descfn="list_associations";topkey='Associations';key="LicenseConfigurationArn";filterid=key
    elif type == "aws_licensemanager_grant":
        clfn="licensemanager";descfn="list_grants";topkey='Grants';key="GrantArn";filterid=key
    elif type == "aws_licensemanager_grant_accepter":
        clfn="licensemanager";descfn="list_grant_accepters";topkey='GrantAccepters';key="GrantId";filterid=key
    elif type == "aws_licensemanager_grants":
        clfn="licensemanager";descfn="list_grants";topkey='Grants';key="GrantArn";filterid=key
    elif type == "aws_licensemanager_license_configuration":
        clfn="licensemanager";descfn="list_license_configurations";topkey='LicenseConfigurations';key="LicenseConfigurationArn";filterid=key
    elif type == "aws_licensemanager_received_license":
        clfn="licensemanager";descfn="list_received_licenses";topkey='ReceivedLicenses';key="LicenseId";filterid=key
    elif type == "aws_licensemanager_received_licenses":
        clfn="licensemanager";descfn="list_received_licenses";topkey='ReceivedLicenses';key="LicenseId";filterid=key
    elif type == "aws_lightsail_bucket":
        clfn="lightsail";descfn="get_buckets";topkey='Buckets';key="name";filterid=key
    elif type == "aws_lightsail_bucket_access_key":
        clfn="lightsail";descfn="get_bucket_access_keys";topkey='AccessKeys';key="name";filterid=key
    elif type == "aws_lightsail_bucket_resource_access":
        clfn="lightsail";descfn="get_bucket_resources";topkey='Buckets';key="name";filterid=key
    elif type == "aws_lightsail_certificate":
        clfn="lightsail";descfn="get_certificates";topkey='Certificates';key="name";filterid=key
    elif type == "aws_lightsail_container_service":
        clfn="lightsail";descfn="get_container_services";topkey='ContainerServices';key="name";filterid=key
    elif type == "aws_lightsail_container_service_deployment_version":
        clfn="lightsail";descfn="get_container_service_deployments";topkey='Deployments';key="name";filterid=key
    elif type == "aws_lightsail_database":
        clfn="lightsail";descfn="get_databases";topkey='Databases';key="name";filterid=key
    elif type == "aws_lightsail_disk":
        clfn="lightsail";descfn="get_disks";topkey='Disks';key="name";filterid=key
    elif type == "aws_lightsail_disk_attachment":
        clfn="lightsail";descfn="get_disk_attachments";topkey='DiskAttachments';key="name";filterid=key
    elif type == "aws_lightsail_distribution":
        clfn="lightsail";descfn="get_distributions";topkey='Distributions';key="name";filterid=key
    elif type == "aws_lightsail_domain":
        clfn="lightsail";descfn="get_domains";topkey='Domains';key="name";filterid=key
    elif type == "aws_lightsail_domain_entry":
        clfn="lightsail";descfn="get_domain_entries";topkey='DomainEntries';key="name";filterid=key
    elif type == "aws_lightsail_instance":
        clfn="lightsail";descfn="get_instances";topkey='Instances';key="name";filterid=key
    elif type == "aws_lightsail_instance_public_ports":
        clfn="lightsail";descfn="get_instance_public_ports";topkey='PublicPorts';key="name";filterid=key
    elif type == "aws_lightsail_key_pair":
        clfn="lightsail";descfn="get_instance_public_ports";topkey='PortInfo';key="name";filterid=key
    elif type == "aws_lightsail_lb":
        clfn="lightsail";descfn="get_key_pairs";topkey='KeyPairs';key="name";filterid=key
    elif type == "aws_lightsail_lb_attachment":
        clfn="lightsail";descfn="get_load_balancers";topkey='LoadBalancers';key="name";filterid=key
    elif type == "aws_lightsail_lb_certificate":
        clfn="lightsail";descfn="get_key_pairs";topkey='KeyPairs';key="name";filterid=key
    elif type == "aws_lightsail_lb_certificate_attachment":
        clfn="lightsail";descfn="get_load_balancer_certificates";topkey='Certificates';key="name";filterid=key
    elif type == "aws_lightsail_lb_https_redirection_policy":
        clfn="lightsail";descfn="get_key_pairs";topkey='KeyPairs';key="name";filterid=key
    elif type == "aws_lightsail_lb_stickiness_policy":
        clfn="lightsail";descfn="get_load_balancer_https_redirection_policies";topkey='HttpsRedirectPolicies';key="name";filterid=key
    elif type == "aws_lightsail_static_ip":
        clfn="lightsail";descfn="get_key_pairs";topkey='KeyPairs';key="name";filterid=key
    elif type == "aws_lightsail_static_ip_attachment":
        clfn="lightsail";descfn="get_static_ips";topkey='StaticIps';key="name";filterid=key
    elif type == "aws_load_balancer_backend_server_policy":
        clfn="elbv2";descfn="describe_backend_server_policies";topkey='BackendServerDescriptions';key="PolicyName";filterid=key
    elif type == "aws_load_balancer_listener_policy":
        clfn="elbv2";descfn="describe_listeners";topkey='Listeners';key="PolicyNames";filterid=key
    elif type == "aws_load_balancer_policy":
        clfn="elbv2";descfn="describe_load_balancer_policies";topkey='Policies';key="PolicyName";filterid=key
    elif type == "aws_location_geofence_collection":
        clfn="location";descfn="list_geofence_collections";topkey='GeofenceCollections';key="CollectionName";filterid=key
    elif type == "aws_location_map":
        clfn="location";descfn="list_maps";topkey='Maps';key="MapName";filterid=key
    elif type == "aws_location_place_index":
        clfn="location";descfn="list_place_indexes";topkey='PlaceIndexes';key="IndexName";filterid=key
    elif type == "aws_location_route_calculator":
        clfn="location";descfn="list_route_calculators";topkey='RouteCalculators';key="CalculatorName";filterid=key
    elif type == "aws_location_tracker":
        clfn="location";descfn="list_trackers";topkey='Trackers';key="TrackerName";filterid=key
    elif type == "aws_location_tracker_association":
        clfn="location";descfn="list_tracker_associations";topkey='TrackerAssociations';key="TrackerName";filterid=key
    elif type == "aws_location_tracker_associations":
        clfn="location";descfn="list_tracker_associations";topkey='TrackerAssociations';key="TrackerName";filterid=key
    elif type == "aws_macie2_account":
        clfn="macie2";descfn="list_account_settings";topkey='AccountSettings';key="Name";filterid=key
    elif type == "aws_macie2_classification_export_configuration":
        clfn="macie2";descfn="list_classification_export_configurations";topkey='ClassificationExportConfigurations';key="Id";filterid=key
    elif type == "aws_macie2_classification_job":
        clfn="macie2";descfn="list_classification_jobs";topkey='ClassificationJobs';key="Id";filterid=key
    elif type == "aws_macie2_custom_data_identifier":
        clfn="macie2";descfn="list_custom_data_identifiers";topkey='CustomDataIdentifiers';key="Id";filterid=key
    elif type == "aws_macie2_findings_filter":
        clfn="macie2";descfn="list_findings_filters";topkey='FindingsFilters';key="Name";filterid=key
    elif type == "aws_macie2_invitation_accepter":
        clfn="macie2";descfn="list_invitations";topkey='Invitations';key="AccountId";filterid=key
    elif type == "aws_macie2_member":
        clfn="macie2";descfn="list_invitation_accepters";topkey='InvitationAccepters';key="AccountId";filterid=key
    elif type == "aws_macie2_organization_admin_account":
        clfn="macie2";descfn="list_members";topkey='Members';key="AccountId";filterid=key
    elif type == "aws_main_route_table_association":
        clfn="ec2";descfn="describe_route_tables";topkey='RouteTables';key="Associations[].Main";filterid=key
    elif type == "aws_media_convert_queue":
        clfn="mediaconvert";descfn="list_queues";topkey='Queues';key="Name";filterid=key
    elif type == "aws_media_package_channel":
        clfn="mediapackage";descfn="list_channels";topkey='Channels';key="Id";filterid=key
    elif type == "aws_media_store_container":
        clfn="mediastore";descfn="list_containers";topkey='Containers';key="Name";filterid=key
    elif type == "aws_media_store_container_policy":
        clfn="mediastore";descfn="list_container_policies";topkey='ContainerPolicies';key="Policy";filterid=key
    elif type == "aws_medialive_channel":
        clfn="medialive";descfn="list_channels";topkey='Channels';key="Id";filterid=key
    elif type == "aws_medialive_input":
        clfn="medialive";descfn="list_inputs";topkey='Inputs';key="Id";filterid=key
    elif type == "aws_medialive_input_security_group":
        clfn="medialive";descfn="list_input_security_groups";topkey='InputSecurityGroups';key="Id";filterid=key
    elif type == "aws_medialive_multiplex":
        clfn="medialive";descfn="list_multiplexes";topkey='Multiplexes';key="Id";filterid=key
    elif type == "aws_medialive_multiplex_program":
        clfn="medialive";descfn="list_multiplex_programs";topkey='MultiplexPrograms';key="Id";filterid=key
    elif type == "aws_memorydb_acl":
        clfn="memorydb";descfn="list_acls";topkey='ACLs';key="Name";filterid=key
    elif type == "aws_memorydb_cluster":
        clfn="memorydb";descfn="list_clusters";topkey='Clusters';key="Name";filterid=key
    elif type == "aws_memorydb_parameter_group":
        clfn="memorydb";descfn="list_parameter_groups";topkey='ParameterGroups';key="Name";filterid=key
    elif type == "aws_memorydb_snapshot":
        clfn="memorydb";descfn="list_snapshots";topkey='Snapshots';key="Name";filterid=key
    elif type == "aws_memorydb_subnet_group":
        clfn="memorydb";descfn="list_subnet_groups";topkey='SubnetGroups';key="Name";filterid=key
    elif type == "aws_memorydb_user":
        clfn="memorydb";descfn="list_users";topkey='Users';key="Name";filterid=key
    elif type == "aws_mq_broker":
        clfn="mq";descfn="list_brokers";topkey='BrokerSummaries';key="BrokerName";filterid=key
    elif type == "aws_mq_broker_instance_type_offerings":
        clfn="mq";descfn="list_instance_type_offerings";topkey='InstanceTypeOfferings';key="InstanceType";filterid=key
    elif type == "aws_mq_configuration":
        clfn="mq";descfn="list_configurations";topkey='Configurations';key="Name";filterid=key
    elif type == "aws_msk_broker_nodes":
        clfn="msk";descfn="list_nodes";topkey='Nodes';key="NodeId";filterid=key
    elif type == "aws_msk_cluster":
        clfn="msk";descfn="list_clusters";topkey='Clusters';key="ClusterName";filterid=key
    elif type == "aws_msk_cluster_policy":
        clfn="msk";descfn="list_cluster_policies";topkey='ClusterPolicies';key="PolicyName";filterid=key
    elif type == "aws_msk_configuration":
        clfn="msk";descfn="list_configurations";topkey='Configurations';key="Arn";filterid=key
    elif type == "aws_msk_kafka_version":
        clfn="msk";descfn="list_kafka_versions";topkey='KafkaVersions';key="Version";filterid=key
    elif type == "aws_msk_replicator":
        clfn="msk";descfn="list_replicators";topkey='Replicators';key="ReplicatorName";filterid=key
    elif type == "aws_msk_scram_secret_association":
        clfn="msk";descfn="list_scram_secrets";topkey='ScramSecrets';key="ClusterArn";filterid=key
    elif type == "aws_msk_serverless_cluster":
        clfn="msk";descfn="list_serverless_clusters";topkey='ServerlessClusters';key="ClusterName";filterid=key
    elif type == "aws_msk_vpc_connection":
        clfn="msk";descfn="list_vpc_connections";topkey='VpcConnections';key="VpcConnectionName";filterid=key
    elif type == "aws_mskconnect_connector":
        clfn="mskconnect";descfn="list_connectors";topkey='Connectors';key="Name";filterid=key
    elif type == "aws_mskconnect_custom_plugin":
        clfn="mskconnect";descfn="list_custom_plugins";topkey='CustomPlugins';key="Name";filterid=key
    elif type == "aws_mskconnect_worker_configuration":
        clfn="mskconnect";descfn="list_worker_configurations";topkey='WorkerConfigurations';key="Name";filterid=key
    elif type == "aws_mwaa_environment":
        clfn="mwaa";descfn="list_environments";topkey='Environments';key="Name";filterid=key
    #elif type == "aws_nat_gateway":
    #    clfn="ec2";descfn="describe_nat_gateways";topkey='NatGateways';key="NatGatewayId";filterid=key
    #elif type == "aws_nat_gateways":
    #    clfn="ec2";descfn="describe_nat_gateways";topkey='NatGateways';key="NatGatewayId";filterid=key
    elif type == "aws_neptune_cluster":
        clfn="neptune";descfn="describe_db_clusters";topkey='DBClusters';key="DBClusterIdentifier";filterid=key
    elif type == "aws_neptune_cluster_endpoint":
        clfn="neptune";descfn="describe_db_cluster_endpoints";topkey='DBClusterEndpoints';key="Endpoint";filterid=key
    elif type == "aws_neptune_cluster_instance":
        clfn="neptune";descfn="describe_db_cluster_instances";topkey='DBClusterInstances';key="DBInstanceIdentifier";filterid=key
    elif type == "aws_neptune_cluster_parameter_group":
        clfn="neptune";descfn="describe_db_cluster_parameter_groups";topkey='DBClusterParameterGroups';key="DBClusterParameterGroupName";filterid=key
    elif type == "aws_neptune_cluster_snapshot":
        clfn="neptune";descfn="describe_db_cluster_snapshots";topkey='DBClusterSnapshots';key="DBClusterSnapshotIdentifier";filterid=key
    elif type == "aws_neptune_engine_version":
        clfn="neptune";descfn="describe_db_engine_versions";topkey='DBEngineVersions';key="Engine";filterid=key
    elif type == "aws_neptune_event_subscription":
        clfn="neptune";descfn="describe_event_subscriptions";topkey='EventSubscriptions';key="SubscriptionName";filterid=key
    elif type == "aws_neptune_global_cluster":
        clfn="neptune";descfn="describe_global_clusters";topkey='GlobalClusters';key="GlobalClusterIdentifier";filterid=key
    elif type == "aws_neptune_orderable_db_instance":
        clfn="neptune";descfn="describe_orderable_db_instance_options";topkey='OrderableDBInstanceOptions';key="Engine";filterid=key
    elif type == "aws_neptune_parameter_group":
        clfn="neptune";descfn="describe_db_parameter_groups";topkey='DBParameterGroups';key="DBParameterGroupName";filterid=key
    elif type == "aws_neptune_subnet_group":
        clfn="neptune";descfn="describe_db_subnet_groups";topkey='DBSubnetGroups';key="DBSubnetGroupName";filterid=key
    #elif type == "aws_network_acl":
    #    clfn="ec2";descfn="describe_network_acls";topkey='NetworkAcls';key="NetworkAclId";filterid=key
    elif type == "aws_network_acl_association":
        clfn="ec2";descfn="describe_network_acls";topkey='NetworkAcls';key="NetworkAclId";filterid=key
    elif type == "aws_network_acl_rule":
        clfn="ec2";descfn="describe_network_acls";topkey='NetworkAcls';key="NetworkAclId";filterid=key
    elif type == "aws_network_acls":
        clfn="ec2";descfn="describe_network_acls";topkey='NetworkAcls';key="NetworkAclId";filterid=key
    elif type == "aws_network_interface":
        clfn="ec2";descfn="describe_network_interfaces";topkey='NetworkInterfaces';key="NetworkInterfaceId";filterid=key
    elif type == "aws_network_interface_attachment":
        clfn="ec2";descfn="describe_network_interfaces";topkey='NetworkInterfaces';key="NetworkInterfaceId";filterid=key
    elif type == "aws_network_interface_sg_attachment":
        clfn="ec2";descfn="describe_network_interfaces";topkey='NetworkInterfaces';key="NetworkInterfaceId";filterid=key
    elif type == "aws_network_interfaces":
        clfn="ec2";descfn="describe_network_interfaces";topkey='NetworkInterfaces';key="NetworkInterfaceId";filterid=key
    elif type == "aws_networkfirewall_firewall":
        clfn="network-firewall";descfn="list_firewalls";topkey='Firewalls';key="FirewallArn";filterid=key
    elif type == "aws_networkfirewall_firewall_policy":
        clfn="network-firewall";descfn="list_firewall_policies";topkey='FirewallPolicies';key="FirewallPolicyArn";filterid=key
    elif type == "aws_networkfirewall_logging_configuration":
        clfn="network-firewall";descfn="list_logging_configurations";topkey='LoggingConfigurations';key="FirewallArn";filterid=key
    elif type == "aws_networkfirewall_resource_policy":
        clfn="network-firewall";descfn="list_resource_policies";topkey='ResourcePolicies';key="ResourceArn";filterid=key
    elif type == "aws_networkfirewall_rule_group":
        clfn="network-firewall";descfn="list_rule_groups";topkey='RuleGroups';key="RuleGroupArn";filterid=key
    elif type == "aws_networkmanager_attachment_accepter":
        clfn="networkmanager";descfn="list_attachment_accepters";topkey='AttachmentAccepters';key="AttachmentId";filterid=key
    elif type == "aws_networkmanager_connect_attachment":
        clfn="networkmanager";descfn="list_connect_attachments";topkey='ConnectAttachments';key="AttachmentId";filterid=key
    elif type == "aws_networkmanager_connect_peer":
        clfn="networkmanager";descfn="list_connect_peers";topkey='ConnectPeers';key="ConnectPeerId";filterid=key
    elif type == "aws_networkmanager_connection":
        clfn="networkmanager";descfn="list_connections";topkey='Connections';key="ConnectionId";filterid=key
    elif type == "aws_networkmanager_connections":
        clfn="networkmanager";descfn="list_connections";topkey='Connections';key="ConnectionId";filterid=key
    elif type == "aws_networkmanager_core_network":
        clfn="networkmanager";descfn="list_core_networks";topkey='CoreNetworks';key="CoreNetworkId";filterid=key
    elif type == "aws_networkmanager_core_network_policy_attachment":
        clfn="networkmanager";descfn="list_core_network_policy_attachments";topkey='CoreNetworkPolicyAttachments';key="CoreNetworkPolicyAttachmentId";filterid=key
    elif type == "aws_networkmanager_core_network_policy_documument":
        clfn="networkmanager";descfn="list_core_network_policy_documents";topkey='CoreNetworkPolicyDocuments';key="CoreNetworkPolicyDocumentId";filterid=key
    elif type == "aws_networkmanager_customer_gateway_association":
        clfn="networkmanager";descfn="list_customer_gateway_associations";topkey='CustomerGatewayAssociations';key="CustomerGatewayAssociationId";filterid=key
    elif type == "aws_networkmanager_device":
        clfn="networkmanager";descfn="list_devices";topkey='Devices';key="DeviceId";filterid=key
    elif type == "aws_networkmanager_devices":
        clfn="networkmanager";descfn="list_devices";topkey='Devices';key="DeviceId";filterid=key
    elif type == "aws_networkmanager_global_network":
        clfn="networkmanager";descfn="list_global_networks";topkey='GlobalNetworks';key="GlobalNetworkId";filterid=key
    elif type == "aws_networkmanager_global_networks":
        clfn="networkmanager";descfn="list_global_networks";topkey='GlobalNetworks';key="GlobalNetworkId";filterid=key
    elif type == "aws_networkmanager_link":
        clfn="networkmanager";descfn="list_links";topkey='Links';key="LinkId";filterid=key
    elif type == "aws_networkmanager_link_association":
        clfn="networkmanager";descfn="list_link_associations";topkey='LinkAssociations';key="LinkAssociationId";filterid=key
    elif type == "aws_networkmanager_links":
        clfn="networkmanager";descfn="list_links";topkey='Links';key="LinkId";filterid=key
    elif type == "aws_networkmanager_site":
        clfn="networkmanager";descfn="list_sites";topkey='Sites';key="SiteId";filterid=key
    elif type == "aws_networkmanager_site_to_site_vpn_attachment":
        clfn="networkmanager";descfn="list_site_to_site_vpn_attachments";topkey='SiteToSiteVpnAttachments';key="SiteToSiteVpnAttachmentId";filterid=key
    elif type == "aws_networkmanager_sites":
        clfn="networkmanager";descfn="list_sites";topkey='Sites';key="SiteId";filterid=key
    elif type == "aws_networkmanager_transit_gateway_connect_peer_association":
        clfn="networkmanager";descfn="list_transit_gateway_connect_peers";topkey='TransitGatewayConnectPeers';key="TransitGatewayConnectPeerId";filterid=key
    elif type == "aws_networkmanager_transit_gateway_peering":
        clfn="networkmanager";descfn="list_transit_gateway_peerings";topkey='TransitGatewayPeerings';key="TransitGatewayPeeringId";filterid=key
    elif type == "aws_networkmanager_transit_gateway_registration":
        clfn="networkmanager";descfn="list_transit_gateway_registrations";topkey='TransitGatewayRegistrations';key="TransitGatewayRegistrationId";filterid=key
    elif type == "aws_networkmanager_transit_gateway_route_table_attachment":
        clfn="networkmanager";descfn="list_transit_gateway_route_tables";topkey='TransitGatewayRouteTables';key="TransitGatewayRouteTableId";filterid=key
    elif type == "aws_networkmanager_vpc_attachment":
        clfn="networkmanager";descfn="list_vpc_attachments";topkey='VpcAttachments';key="VpcAttachmentId";filterid=key
    elif type == "aws_oam_link":
        clfn="networkmanager";descfn="list_links";topkey='Links';key="LinkId";filterid=key
    elif type == "aws_oam_sink":
        clfn="networkmanager";descfn="list_links";topkey='Links';key="LinkId";filterid=key
    elif type == "aws_oam_sink_policy":
        clfn="networkmanager";descfn="list_links";topkey='Links';key="LinkId";filterid=key
    elif type == "aws_opensearch_domain":
        clfn="opensearch";descfn="list_domain_names";topkey='DomainNames';key="DomainName";filterid=key
    elif type == "aws_opensearch_domain_policy":
        clfn="opensearch";descfn="list_domain_names";topkey='DomainNames';key="DomainName";filterid=key
    elif type == "aws_opensearch_domain_saml_options":
        clfn="opensearch";descfn="list_domain_names";topkey='DomainNames';key="DomainName";filterid=key
    elif type == "aws_opensearch_inbound_connection_accepter":
        clfn="opensearch";descfn="list_inbound_connection_accepters";topkey='InboundConnectionAccepters';key="ConnectionId";filterid=key
    elif type == "aws_opensearch_outbound_connection":
        clfn="opensearch";descfn="list_inbound_connection_accepters";topkey='InboundConnectionAccepters';key="InboundConnectionId";filterid=key
    elif type == "aws_opensearch_package":
        clfn="opensearch";descfn="list_packages";topkey='Packages';key="PackageID";filterid=key
    elif type == "aws_opensearch_package_association":
        clfn="opensearch";descfn="list_packages";topkey='Packages';key="PackageID";filterid=key
    elif type == "aws_opensearch_vpc_endpoint":
        clfn="opensearch";descfn="list_vpc_endpoints";topkey='VpcEndpoints';key="VpcEndpointId";filterid=key
    elif type == "aws_opensearchserverless_access_policy":
        clfn="opensearch";descfn="list_access_policies";topkey='AccessPolicies';key="PolicyId";filterid=key
    elif type == "aws_opensearchserverless_collection":
        clfn="opensearch";descfn="list_collections";topkey='Collections';key="CollectionId";filterid=key
    elif type == "aws_opensearchserverless_lifecycle_policy":
        clfn="opensearch";descfn="list_lifecycle_policies";topkey='LifecyclePolicies';key="PolicyId";filterid=key
    elif type == "aws_opensearchserverless_security_config":
        clfn="opensearch";descfn="list_security_configs";topkey='SecurityConfigs';key="SecurityConfigId";filterid=key
    elif type == "aws_opensearchserverless_security_policy":
        clfn="opensearch";descfn="list_security_policies";topkey='SecurityPolicies';key="PolicyId";filterid=key
    elif type == "aws_opensearchserverless_vpc_endpoint":
        clfn="opensearch";descfn="list_vpc_endpoints";topkey='VpcEndpoints';key="VpcEndpointId";filterid=key
    elif type == "aws_opsworks_application":
        clfn="opsworks";descfn="list_applications";topkey='Applications';key="ApplicationId";filterid=key
    elif type == "aws_opsworks_custom_layer":
        clfn="opsworks";descfn="list_custom_layers";topkey='CustomLayers';key="LayerId";filterid=key
    elif type == "aws_opsworks_ecs_cluster_layer":
        clfn="opsworks";descfn="list_ecs_cluster_layers";topkey='EcsClusterLayers';key="LayerId";filterid=key
    elif type == "aws_opsworks_ganglia_layer":
        clfn="opsworks";descfn="list_ganglia_layers";topkey='GangliaLayers';key="LayerId";filterid=key
    elif type == "aws_opsworks_haproxy_layer":
        clfn="opsworks";descfn="list_haproxy_layers";topkey='HaproxyLayers';key="LayerId";filterid=key
    elif type == "aws_opsworks_instance":
        clfn="opsworks";descfn="list_instances";topkey='Instances';key="InstanceId";filterid=key
    elif type == "aws_opsworks_java_app_layer":
        clfn="opsworks";descfn="list_java_app_layers";topkey='JavaAppLayers';key="LayerId";filterid=key
    elif type == "aws_opsworks_memcached_layer":
        clfn="opsworks";descfn="list_memcached_layers";topkey='MemcachedLayers';key="LayerId";filterid=key
    elif type == "aws_opsworks_mysql_layer":
        clfn="opsworks";descfn="list_mysql_layers";topkey='MysqlLayers';key="LayerId";filterid=key
    elif type == "aws_opsworks_nodejs_app_layer":
        clfn="opsworks";descfn="list_nodejs_app_layers";topkey='NodejsAppLayers';key="LayerId";filterid=key
    elif type == "aws_opsworks_permission":
        clfn="opsworks";descfn="list_permissions";topkey='Permissions';key="PermissionId";filterid=key
    elif type == "aws_opsworks_php_app_layer":
        clfn="opsworks";descfn="list_php_app_layers";topkey='PhpAppLayers';key="LayerId";filterid=key
    elif type == "aws_opsworks_rails_app_layer":
        clfn="opsworks";descfn="list_rails_app_layers";topkey='RailsAppLayers';key="LayerId";filterid=key
    elif type == "aws_opsworks_rds_db_instance":
        clfn="opsworks";descfn="list_rds_db_instances";topkey='RdsDbInstances';key="DbInstanceArn";filterid=key
    elif type == "aws_opsworks_stack":
        clfn="opsworks";descfn="list_stacks";topkey='Stacks';key="StackId";filterid=key
    elif type == "aws_opsworks_static_web_layer":
        clfn="opsworks";descfn="list_static_web_layers";topkey='StaticWebLayers';key="LayerId";filterid=key
    elif type == "aws_opsworks_user_profile":
        clfn="opsworks";descfn="list_user_profiles";topkey='UserProfiles';key="IamUserArn";filterid=key
    elif type == "aws_organizations_account":
        clfn="organizations";descfn="list_accounts";topkey='Accounts';key="Id";filterid=key
    elif type == "aws_organizations_delegated_administrator":
        clfn="organizations";descfn="list_delegated_administrators";topkey='DelegatedAdministrators';key="Id";filterid=key
    elif type == "aws_organizations_delegated_administrators":
        clfn="organizations";descfn="list_delegated_administrators";topkey='DelegatedAdministrators';key="Id";filterid=key
    elif type == "aws_organizations_delegated_services":
        clfn="organizations";descfn="list_delegated_services";topkey='DelegatedServices';key="ServicePrincipal";filterid=key
    elif type == "aws_organizations_organization":
        clfn="organizations";descfn="list_organizations";topkey='Organization';key="Id";filterid=key
    elif type == "aws_organizations_organizational_unit":
        clfn="organizations";descfn="list_organizational_units";topkey='OrganizationalUnits';key="Id";filterid=key
    elif type == "aws_organizations_organizational_unit_child_accounts":
        clfn="organizations";descfn="list_organizational_units";topkey='OrganizationalUnits';key="Id";filterid=key
    elif type == "aws_organizations_organizational_unit_descendant_accounts":
        clfn="organizations";descfn="list_organizational_units";topkey='OrganizationalUnits';key="Id";filterid=key
    elif type == "aws_organizations_organizational_units":
        clfn="organizations";descfn="list_organizational_units";topkey='OrganizationalUnits';key="Id";filterid=key
    elif type == "aws_organizations_policies":
        clfn="organizations";descfn="list_policies";topkey='Policies';key="Id";filterid=key
    elif type == "aws_organizations_policies_for_target":
        clfn="organizations";descfn="list_policies";topkey='Policies';key="Id";filterid=key
    elif type == "aws_organizations_policy":
        clfn="organizations";descfn="list_policies";topkey='Policies';key="Id";filterid=key
    elif type == "aws_organizations_policy_attachment":
        clfn="organizations";descfn="list_policy_attachments";topkey='PolicyAttachments';key="Id";filterid=key
    elif type == "aws_organizations_resource_policy":
        clfn="organizations";descfn="list_resource_policies";topkey='ResourcePolicies';key="Id";filterid=key
    elif type == "aws_organizations_resource_tags":
        clfn="organizations";descfn="list_resource_tags";topkey='ResourceTags';key="Id";filterid=key
    elif type == "aws_outposts_asset":
        clfn="outposts";descfn="list_assets";topkey='Assets';key="Id";filterid=key
    elif type == "aws_outposts_assets":
        clfn="outposts";descfn="list_assets";topkey='Assets';key="Id";filterid=key
    elif type == "aws_outposts_outpost":
        clfn="outposts";descfn="list_outposts";topkey='Outposts';key="Id";filterid=key
    elif type == "aws_outposts_outpost_instance_type":
        clfn="outposts";descfn="list_outpost_instance_types";topkey='OutpostInstanceTypes';key="Id";filterid=key
    elif type == "aws_outposts_outpost_instance_types":
        clfn="outposts";descfn="list_outpost_instance_types";topkey='OutpostInstanceTypes';key="Id";filterid=key
    elif type == "aws_outposts_outposts":
        clfn="outposts";descfn="list_outposts";topkey='Outposts';key="Id";filterid=key
    elif type == "aws_outposts_site":
        clfn="outposts";descfn="list_sites";topkey='Sites';key="Id";filterid=key
    elif type == "aws_outposts_sites":
        clfn="outposts";descfn="list_sites";topkey='Sites';key="Id";filterid=key
    elif type == "aws_partition":
        clfn="sts";descfn="get_partition";topkey='Partition';key="Partition";filterid=key
    elif type == "aws_pinpoint_adm_channel":
        clfn="pinpoint";descfn="list_adm_channels";topkey='AdmChannels';key="Id";filterid=key
    elif type == "aws_pinpoint_apns_channel":
        clfn="pinpoint";descfn="list_apns_channels";topkey='ApnsChannels';key="Id";filterid=key
    elif type == "aws_pinpoint_apns_sandbox_channel":
        clfn="pinpoint";descfn="list_apns_sandbox_channels";topkey='ApnsSandboxChannels';key="Id";filterid=key
    elif type == "aws_pinpoint_apns_voip_channel":
        clfn="pinpoint";descfn="list_apns_voip_channels";topkey='ApnsVoipChannels';key="Id";filterid=key
    elif type == "aws_pinpoint_apns_voip_sandbox_channel":
        clfn="pinpoint";descfn="list_apns_voip_sandbox_channels";topkey='ApnsVoipSandboxChannels';key="Id";filterid=key
    elif type == "aws_pinpoint_app":
        clfn="pinpoint";descfn="list_apps";topkey='Apps';key="Id";filterid=key
    elif type == "aws_pinpoint_baidu_channel":
        clfn="pinpoint";descfn="list_baidu_channels";topkey='BaiduChannels';key="Id";filterid=key
    elif type == "aws_pinpoint_email_channel":
        clfn="pinpoint";descfn="list_email_channels";topkey='EmailChannels';key="Id";filterid=key
    elif type == "aws_pinpoint_event_stream":
        clfn="pinpoint";descfn="list_event_streams";topkey='EventStreams';key="Id";filterid=key
    elif type == "aws_pinpoint_gcm_channel":
        clfn="pinpoint";descfn="list_gcm_channels";topkey='GcmChannels';key="Id";filterid=key
    elif type == "aws_pinpoint_sms_channel":
        clfn="pinpoint";descfn="list_sms_channels";topkey='SmsChannels';key="Id";filterid=key
    elif type == "aws_pipes_pipe":
        clfn="pipes";descfn="list_pipes";topkey='Pipes';key="Name";filterid=key
    elif type == "aws_placement_group":
        clfn="ec2";descfn="describe_placement_groups";topkey='PlacementGroups';key="GroupName";filterid=key
    elif type == "aws_polly_voices":
        clfn="polly";descfn="describe_voices";topkey='Voices';key="Id";filterid=key
    elif type == "aws_prefix_list":
        clfn="ec2";descfn="describe_prefix_lists";topkey='PrefixLists';key="PrefixListId";filterid=key
    elif type == "aws_pricing_product":
        clfn="pricing";descfn="describe_services";topkey='Services';key="ServiceCode";filterid=key
    elif type == "aws_prometheus_alert_manager_definition":
        clfn="prometheus";descfn="list_alertmanager_definition";topkey='AlertmanagerDefinition';key="Name";filterid=key
    elif type == "aws_prometheus_rule_group_namespace":
        clfn="prometheus";descfn="list_rule_group_namespaces";topkey='RuleGroupNamespaces';key="Name";filterid=key
    elif type == "aws_prometheus_workspace":
        clfn="prometheus";descfn="list_workspaces";topkey='Workspaces';key="Name";filterid=key
    elif type == "aws_proxy_protocol_policy":
        clfn="wafv2";descfn="list_proxy_protocol_policies";topkey='ProxyProtocolPolicies';key="Name";filterid=key
    elif type == "aws_qldb_ledger":
        clfn="qldb";descfn="list_ledgers";topkey='Ledgers';key="Name";filterid=key
    elif type == "aws_qldb_stream":
        clfn="qldb";descfn="list_streams";topkey='Streams';key="Name";filterid=key
    elif type == "aws_quicksight_account_subscription":
        clfn="quicksight";descfn="list_account_subscriptions";topkey='AccountSubscriptions';key="SubscriptionId";filterid=key
    elif type == "aws_quicksight_analysis":
        clfn="quicksight";descfn="list_analyses";topkey='Analyses';key="AnalysisId";filterid=key
    elif type == "aws_quicksight_dashboard":
        clfn="quicksight";descfn="list_dashboards";topkey='Dashboards';key="DashboardId";filterid=key
    elif type == "aws_quicksight_data_set":
        clfn="quicksight";descfn="list_data_sets";topkey='DataSets';key="DataSetId";filterid=key
    elif type == "aws_quicksight_data_source":
        clfn="quicksight";descfn="list_data_sources";topkey='DataSources';key="DataSourceId";filterid=key
    elif type == "aws_quicksight_folder":
        clfn="quicksight";descfn="list_folders";topkey='Folders';key="FolderId";filterid=key
    elif type == "aws_quicksight_folder_membership":
        clfn="quicksight";descfn="list_folder_memberships";topkey='FolderMemberships';key="FolderMembershipId";filterid=key
    elif type == "aws_quicksight_group":
        clfn="quicksight";descfn="list_groups";topkey='Groups';key="GroupName";filterid=key
    elif type == "aws_quicksight_group_membership":
        clfn="quicksight";descfn="list_group_memberships";topkey='GroupMemberships';key="GroupMembershipId";filterid=key
    elif type == "aws_quicksight_iam_policy_assignment":
        clfn="quicksight";descfn="list_iam_policy_assignments";topkey='IamPolicyAssignments';key="AssignmentName";filterid=key
    elif type == "aws_quicksight_ingestion":
        clfn="quicksight";descfn="list_ingestions";topkey='Ingestions';key="IngestionId";filterid=key
    elif type == "aws_quicksight_namespace":
        clfn="quicksight";descfn="list_namespaces";topkey='Namespaces';key="Namespace";filterid=key
    elif type == "aws_quicksight_refresh_schedule":
        clfn="quicksight";descfn="list_refresh_schedules";topkey='RefreshSchedules';key="ScheduleId";filterid=key
    elif type == "aws_quicksight_template":
        clfn="quicksight";descfn="list_templates";topkey='Templates';key="TemplateId";filterid=key
    elif type == "aws_quicksight_template_alias":
        clfn="quicksight";descfn="list_template_aliases";topkey='TemplateAliases';key="AliasName";filterid=key
    elif type == "aws_quicksight_theme":
        clfn="quicksight";descfn="list_themes";topkey='Themes';key="ThemeId";filterid=key
    elif type == "aws_quicksight_user":
        clfn="quicksight";descfn="list_users";topkey='Users';key="UserName";filterid=key
    elif type == "aws_quicksight_vpc_connection":
        clfn="quicksight";descfn="list_vpc_connections";topkey='VpcConnections';key="VpcConnectionId";filterid=key
    elif type == "aws_ram_principal_association":
        clfn="ram";descfn="list_principal_associations";topkey="PrincipalAssociations";key="PrincipalAssociationId";filterid=key
    elif type == "aws_ram_resource_association":
        clfn="ram";descfn="list_resource_associations";topkey="ResourceAssociations";key="ResourceAssociationId";filterid=key
    elif type == "aws_ram_resource_share":
        clfn="ram";descfn="list_resource_shares";topkey="ResourceShares";key="ResourceShareArn";filterid=key
    elif type == "aws_ram_resource_share_accepter":
        clfn="ram";descfn="list_resource_share_accepters";topkey="ResourceShareAccepters";key="ResourceShareAccepterArn";filterid=key
    elif type == "aws_ram_sharing_with_organization":
        clfn="ram";descfn="list_sharing_accounts";topkey="AccountIds";key="AccountId";filterid=key    
    elif type == "aws_rbin_rule":
        clfn="route53resolver";descfn="list_resolver_rules";topkey="ResolverRules";key="Id";filterid=key
    elif type == "aws_rds_certificate":
        clfn="rds";descfn="describe_certificates";topkey="Certificates";key="CertificateIdentifier";filterid=key
    #elif type == "aws_rds_cluster": 
    #    clfn="rds";descfn="describe_db_clusters";topkey="DBClusters";key="DBClusterIdentifier";filterid=key
    elif type == "aws_rds_cluster_activity_stream": 
        clfn="rds";descfn="describe_db_cluster_activity_stream";topkey="ActivityStream";key="ActivityStreamId";filterid=key
    elif type == "aws_rds_cluster_endpoint":
        clfn="rds";descfn="describe_db_cluster_endpoints";topkey="DBClusterEndpoints";key="DBClusterEndpointIdentifier";filterid=key
    #elif type == "aws_rds_cluster_instance":
    #    clfn="rds";descfn="describe_db_cluster_instances";topkey="DBClusterInstances";key="DBInstanceIdentifier";filterid=key
    #elif type == "aws_rds_cluster_parameter_group":
    #    clfn="rds";descfn="describe_db_cluster_parameter_groups";topkey="DBClusterParameterGroups";key="DBClusterParameterGroupName";filterid=key
    elif type == "aws_rds_cluster_role_association":
        clfn="rds";descfn="describe_db_cluster_role_associations";topkey="DBClusterRoleAssociations";key="DBClusterRoleAssociationId";filterid=key
    elif type == "aws_rds_clusters":
        clfn="rds";descfn="describe_db_clusters";topkey="DBClusters";key="DBClusterIdentifier";filterid=key
    elif type == "aws_rds_custom_db_engine_version": 
        clfn="rds";descfn="describe_custom_db_engine_versions";topkey="CustomDBEngineVersions";key="EngineVersion";filterid=key
    elif type == "aws_rds_engine_version":
        clfn="rds";descfn="describe_db_engine_versions";topkey="DBEngineVersions";key="EngineVersion";filterid=key
    elif type == "aws_rds_export_task":
        clfn="rds";descfn="describe_export_tasks";topkey="ExportTasks";key="ExportTaskIdentifier";filterid=key
    elif type == "aws_rds_global_cluster":
        clfn="rds";descfn="describe_global_clusters";topkey="GlobalClusters";key="GlobalClusterIdentifier";filterid=key
    elif type == "aws_rds_orderable_db_instance":
        clfn="rds";descfn="describe_orderable_db_instance_options";topkey="OrderableDBInstanceOptions";key="Engine";filterid=key
    elif type == "aws_rds_reserved_instance":
        clfn="rds";descfn="describe_reserved_db_instances";topkey="ReservedDBInstances";key="ReservedDBInstanceId";filterid=key
    elif type == "aws_rds_reserved_instance_offering":
        clfn="rds";descfn="describe_reserved_db_instance_offerings";topkey="ReservedDBInstanceOfferings";key="ReservedDBInstancesOfferingId";filterid=key
    elif type == "aws_redshift_authentication_profile":
        clfn="redshift";descfn="describe_authentication_profiles";topkey="AuthenticationProfiles";key="AuthenticationProfileName";filterid=key
    #elif type == "aws_redshift_cluster":
    #    clfn="redshift";descfn="describe_clusters";topkey="Clusters";key="ClusterIdentifier";filterid=key
    elif type == "aws_redshift_cluster_credentials":
        clfn="redshift";descfn="describe_cluster_credentials";topkey="ClusterCredentials";key="DbUser";filterid=key
    elif type == "aws_redshift_cluster_iam_roles":
        clfn="redshift";descfn="describe_cluster_iam_roles";topkey="ClusterIamRoles";key="ClusterIdentifier";filterid=key
    elif type == "aws_redshift_cluster_snapshot":
        clfn="redshift";descfn="describe_cluster_snapshots";topkey="Snapshots";key="SnapshotIdentifier";filterid=key
    elif type == "aws_redshift_endpoint_access":
        clfn="redshift";descfn="describe_endpoint_access";topkey="EndpointAccess";key="EndpointName";filterid=key
    elif type == "aws_redshift_endpoint_authorization":
        clfn="redshift";descfn="describe_endpoint_authorization";topkey="EndpointAuthorization";key="EndpointName";filterid=key
    elif type == "aws_redshift_event_subscription":
        clfn="redshift";descfn="describe_event_subscriptions";topkey="EventSubscriptionsList";key="SubscriptionName";filterid=key
    elif type == "aws_redshift_hsm_client_certificate":
        clfn="redshift";descfn="describe_hsm_client_certificates";topkey="HsmClientCertificates";key="HsmClientCertificateIdentifier";filterid=key
    elif type == "aws_redshift_hsm_configuration":
        clfn="redshift";descfn="describe_hsm_configurations";topkey="HsmConfigurations";key="HsmConfigurationIdentifier";filterid=key
    elif type == "aws_redshift_orderable_cluster":
        clfn="redshift";descfn="describe_orderable_cluster_options";topkey="OrderableClusterOptions";key="ClusterType";filterid=key
    #elif type == "aws_redshift_parameter_group":
    #    clfn="redshift";descfn="describe_cluster_parameters";topkey="Parameters";key="ParameterName";filterid=key
    elif type == "aws_redshift_partner":
        clfn="redshift";descfn="describe_partners";topkey="Partners";key="PartnerName";filterid=key
    elif type == "aws_redshift_resource_policy":
        clfn="redshift";descfn="describe_resource_policies";topkey="ResourcePolicies";key="ResourcePolicyId";filterid=key
    elif type == "aws_redshift_scheduled_action":
        clfn="redshift";descfn="describe_scheduled_actions";topkey="ScheduledActions";key="ScheduledActionName";filterid=key
    elif type == "aws_redshift_service_account":
        clfn="redshift";descfn="describe_service_accounts";topkey="ServiceAccounts";key="ServiceAccountName";filterid=key
    elif type == "aws_redshift_snapshot_copy_grant":
        clfn="redshift";descfn="describe_snapshot_copy_grants";topkey="SnapshotCopyGrants";key="SnapshotCopyGrantName";filterid=key
    elif type == "aws_redshift_snapshot_schedule":
        clfn="redshift";descfn="describe_snapshot_schedules";topkey="SnapshotSchedules";key="ScheduleIdentifier";filterid=key
    elif type == "aws_redshift_snapshot_schedule_association":
        clfn="redshift";descfn="describe_snapshot_schedule_associations";topkey="SnapshotScheduleAssociations";key="ScheduleAssociationId";filterid=key
    #elif type == "aws_redshift_subnet_group":
    #    clfn="redshift";descfn="describe_cluster_subnet_groups";topkey="ClusterSubnetGroups";key="ClusterSubnetGroupName";filterid=key
    elif type == "aws_redshift_usage_limit":
        clfn="redshift";descfn="describe_usage_limits";topkey="UsageLimits";key="UsageLimitId";filterid=key
    elif type == "aws_redshiftdata_statement":
        clfn="redshift-data";descfn="describe_statement";topkey="Statement";key="Id";filterid=key
    elif type == "aws_redshiftserverless_credentials":
        clfn="redshift-serverless";descfn="describe_credentials";topkey="Credentials";key="Name";filterid=key
    elif type == "aws_redshiftserverless_endpoint_access":
        clfn="redshift-serverless";descfn="describe_endpoint_access";topkey="EndpointAccess";key="EndpointName";filterid=key
    #elif type == "aws_redshiftserverless_namespace":
    #    clfn="redshift-serverless";descfn="describe_namespaces";topkey="Namespaces";key="NamespaceName";filterid=key
    elif type == "aws_redshiftserverless_resource_policy":
        clfn="redshift-serverless";descfn="describe_resource_policies";topkey="ResourcePolicies";key="ResourcePolicyId";filterid=key
    elif type == "aws_redshiftserverless_snapshot":
        clfn="redshift-serverless";descfn="describe_snapshots";topkey="Snapshots";key="SnapshotName";filterid=key
    elif type == "aws_redshiftserverless_usage_limit":
        clfn="redshift-serverless";descfn="describe_usage_limits";topkey="UsageLimits";key="UsageLimitId";filterid=key
    #elif type == "aws_redshiftserverless_workgroup":
    #    clfn="redshift-serverless";descfn="describe_workgroups";topkey="Workgroups";key="WorkgroupName";filterid=key
    elif type == "aws_region":
        clfn="ec2";descfn="describe_regions";topkey="Regions";key="RegionName";filterid=key
    elif type == "aws_regions":
        clfn="ec2";descfn="describe_regions";topkey="Regions";key="RegionName";filterid=key
    elif type == "aws_resourceexplorer2_index":
        clfn="resource-explorer2";descfn="list_indices";topkey="Indices";key="Name";filterid=key
    elif type == "aws_resourceexplorer2_view":
        clfn="resource-explorer2";descfn="list_views";topkey="Views";key="Name";filterid=key
    elif type == "aws_resourcegroups_group":
        clfn="resource-groups";descfn="list_groups";topkey="GroupIdentifiers";key="GroupName";filterid=key
    elif type == "aws_resourcegroups_resource":
        clfn="resource-groups";descfn="list_resources";topkey="ResourceIdentifiers";key="ResourceArn";filterid=key
    elif type == "aws_resourcegroupstaggingapi_resources":
        clfn="resourcegroupstaggingapi";descfn="get_resources";topkey="ResourceTagMappingList";key="ResourceARN";filterid=key
    elif type == "aws_rolesanywhere_profile":
        clfn="rolesanywhere";descfn="list_profiles";topkey="Profiles";key="ProfileName";filterid=key
    elif type == "aws_rolesanywhere_trust_anchor":
        clfn="rolesanywhere";descfn="list_trust_anchors";topkey="TrustAnchors";key="TrustAnchorId";filterid=key
    elif type == "aws_route":
        clfn="ec2";descfn="describe_route_tables";topkey="RouteTables";key="RouteTableId";filterid=key
    elif type == "aws_route53_cidr_collection":
        clfn="route53";descfn="list_cidr_collections";topkey="CidrCollections";key="Id";filterid=key
    elif type == "aws_route53_cidr_location":
        clfn="route53";descfn="list_cidr_locations";topkey="CidrLocations";key="Id";filterid=key
    elif type == "aws_route53_delegation_set":
        clfn="route53";descfn="list_delegation_sets";topkey="DelegationSets";key="Id";filterid=key
    elif type == "aws_route53_health_check":
        clfn="route53";descfn="list_health_checks";topkey="HealthChecks";key="Id";filterid=key
    elif type == "aws_route53_hosted_zone_dnssec":
        clfn="route53";descfn="list_hosted_zone_dnssec";topkey="HostedZoneDNSSEC";key="Id";filterid=key
    elif type == "aws_route53_key_signing_key":
        clfn="route53";descfn="list_key_signing_keys";topkey="KeySigningKeys";key="Id";filterid=key
    elif type == "aws_route53_query_log":
        clfn="route53";descfn="list_query_logs";topkey="QueryLogs";key="Id";filterid=key
    elif type == "aws_route53_record":
        clfn="route53";descfn="list_resource_record_sets";topkey="ResourceRecordSets";key="Name";filterid=key
    elif type == "aws_route53_resolver_config":
        clfn="route53";descfn="list_resolver_configs";topkey="ResolverConfigs";key="Id";filterid=key
    elif type == "aws_route53_resolver_dnssec_config":
        clfn="route53";descfn="list_resolver_dnssec_configs";topkey="ResolverDNSSECConfigs";key="Id";filterid=key
    elif type == "aws_route53_resolver_endpoint":
        clfn="route53";descfn="list_resolver_endpoints";topkey="ResolverEndpoints";key="Id";filterid=key
    elif type == "aws_route53_resolver_firewall_config":
        clfn="route53";descfn="list_resolver_firewall_configs";topkey="ResolverFirewallConfigs";key="Id";filterid=key
    elif type == "aws_route53_resolver_firewall_domain_list":
        clfn="route53";descfn="list_resolver_firewall_domain_lists";topkey="ResolverFirewallDomainLists";key="Id";filterid=key
    elif type == "aws_route53_resolver_firewall_rule":
        clfn="route53";descfn="list_resolver_firewall_rules";topkey="ResolverFirewallRules";key="Id";filterid=key
    elif type == "aws_route53_resolver_firewall_rule_group":
        clfn="route53";descfn="list_resolver_firewall_rule_groups";topkey="ResolverFirewallRuleGroups";key="Id";filterid=key
    elif type == "aws_route53_resolver_firewall_rule_groups":
        clfn="route53";descfn="list_resolver_firewall_rule_groups";topkey="ResolverFirewallRuleGroups";key="Id";filterid=key
    elif type == "aws_route53_resolver_firewall_rules":
        clfn="route53";descfn="list_resolver_firewall_rules";topkey="ResolverFirewallRules";key="Id";filterid=key
    elif type == "aws_route53_resolver_query_log_config":
        clfn="route53";descfn="list_resolver_query_log_configs";topkey="ResolverQueryLogConfigs";key="Id";filterid=key
    elif type == "aws_route53_resolver_query_log_config_association":
        clfn="route53";descfn="list_resolver_query_log_config_associations";topkey="ResolverQueryLogConfigAssociations";key="Id";filterid=key
    elif type == "aws_route53_resolver_rule":
        clfn="route53";descfn="list_resolver_rules";topkey="ResolverRules";key="Id";filterid=key
    elif type == "aws_route53_resolver_rule_association":
        clfn="route53";descfn="list_resolver_rule_associations";topkey="ResolverRuleAssociations";key="Id";filterid=key
    elif type == "aws_route53_resolver_rules":
        clfn="route53";descfn="list_resolver_rules";topkey="ResolverRules";key="Id";filterid=key
    elif type == "aws_route53_traffic_policy":
        clfn="route53";descfn="list_traffic_policies";topkey="TrafficPolicies";key="Id";filterid=key
    elif type == "aws_route53_traffic_policy_document":
        clfn="route53";descfn="list_traffic_policy_documents";topkey="TrafficPolicyDocuments";key="Id";filterid=key
    elif type == "aws_route53_traffic_policy_instance":
        clfn="route53";descfn="list_traffic_policy_instances";topkey="TrafficPolicyInstances";key="Id";filterid=key
    elif type == "aws_route53_vpc_association_authorization":
        clfn="route53";descfn="list_vpc_associations_authorization";topkey="VPCAssociations";key="Id";filterid=key
    elif type == "aws_route53_zone":
        clfn="route53";descfn="list_hosted_zones";topkey="HostedZones";key="Name";filterid=key
    elif type == "aws_route53_zone_association":
        clfn="route53";descfn="list_hosted_zone_associations";topkey="HostedZoneAssociations";key="Id";filterid=key
    elif type == "aws_route53domains_registered_domain":
        clfn="route53domains";descfn="list_domains";topkey="Domains";key="DomainName";filterid=key
    elif type == "aws_route53recoverycontrolconfig_cluster":
        clfn="route53recoverycontrolconfig";descfn="list_clusters";topkey="Clusters";key="ClusterArn";filterid=key
    elif type == "aws_route53recoverycontrolconfig_control_panel":
        clfn="route53recoverycontrolconfig";descfn="list_control_panels";topkey="ControlPanels";key="ControlPanelArn";filterid=key
    elif type == "aws_route53recoverycontrolconfig_routing_control":
        clfn="route53recoverycontrolconfig";descfn="list_routing_controls";topkey="RoutingControls";key="RoutingControlArn";filterid=key
    elif type == "aws_route53recoverycontrolconfig_safety_rule":
        clfn="route53recoverycontrolconfig";descfn="list_safety_rules";topkey="SafetyRules";key="SafetyRuleArn";filterid=key
    elif type == "aws_route53recoveryreadiness_cell":
        clfn="route53recoveryreadiness";descfn="list_cells";topkey="Cells";key="CellArn";filterid=key
    elif type == "aws_route53recoveryreadiness_readiness_check":
        clfn="route53recoveryreadiness";descfn="list_readiness_checks";topkey="ReadinessChecks";key="ReadinessCheckArn";filterid=key
    elif type == "aws_route53recoveryreadiness_recovery_group":
        clfn="route53recoveryreadiness";descfn="list_recovery_groups";topkey="RecoveryGroups";key="RecoveryGroupArn";filterid=key
    elif type == "aws_route53recoveryreadiness_resource_set":
        clfn="route53recoveryreadiness";descfn="list_resource_sets";topkey="ResourceSets";key="ResourceSetArn";filterid=key
    #elif type == "aws_route_table":
    #    clfn="ec2";descfn="describe_route_tables";topkey="RouteTables";key="RouteTableId";filterid=key
    #elif type == "aws_route_table_association":
    #    clfn="ec2";descfn="describe_route_tables";topkey="Associations";key="RouteTableAssociationId";filterid=key
    #elif type == "aws_route_tables":
    #    clfn="ec2";descfn="describe_route_tables";topkey="RouteTables";key="RouteTableId";filterid=key
    elif type == "aws_rum_app_monitor":
        clfn="rum";descfn="list_app_monitors";topkey="AppMonitors";key="Name";filterid=key
    elif type == "aws_rum_metrics_destination":
        clfn="rum";descfn="list_metrics_destinations";topkey="MetricsDestinations";key="Name";filterid=key
    elif type == "aws_s3_access_point":
        clfn="s3";descfn="list_access_points";topkey="AccessPoints";key="Name";filterid=key
    elif type == "aws_s3_account_public_access_block":
        clfn="s3";descfn="get_public_access_block";topkey="PublicAccessBlockConfiguration";key="BlockPublicAcls";filterid=key
    elif type == "aws_s3_bucket":
        clfn="s3";descfn="list_buckets";topkey="Buckets";key="Name";filterid=key
    elif type == "aws_s3_bucket_accelerate_configuration":
        clfn="s3";descfn="get_bucket_accelerate_configuration";topkey="Status";key="Status";filterid=key
    elif type == "aws_s3_bucket_acl":
        clfn="s3";descfn="get_bucket_acl";topkey="Grants";key="Grantee.DisplayName";filterid=key
    elif type == "aws_s3_bucket_analytics_configuration":
        clfn="s3";descfn="get_bucket_analytics_configuration";topkey="AnalyticsConfiguration";key="Id";filterid=key
    elif type == "aws_s3_bucket_cors_configuration":
        clfn="s3";descfn="get_bucket_cors_configuration";topkey="CORSRules";key="AllowedMethods";filterid=key
    elif type == "aws_s3_bucket_intelligent_tiering_configuration":
        clfn="s3";descfn="get_bucket_intelligent_tiering_configuration";topkey="IntelligentTieringConfiguration";key="Id";filterid=key
    elif type == "aws_s3_bucket_inventory":
        clfn="s3";descfn="get_bucket_inventory_configuration";topkey="InventoryConfiguration";key="Id";filterid=key
    elif type == "aws_s3_bucket_lifecycle_configuration":
        clfn="s3";descfn="get_bucket_lifecycle_configuration";topkey="Rules";key="ID";filterid=key
    elif type == "aws_s3_bucket_logging":
        clfn="s3";descfn="get_bucket_logging";topkey="LoggingEnabled";key="TargetBucket";filterid=key
    elif type == "aws_s3_bucket_metric":
        clfn="s3";descfn="get_bucket_metrics_configuration";topkey="MetricsConfiguration";key="Id";filterid=key
    elif type == "aws_s3_bucket_notification":
        clfn="s3";descfn="get_bucket_notification_configuration";topkey="TopicConfigurations";key="Topic";filterid=key
    elif type == "aws_s3_bucket_object":
        clfn="s3";descfn="get_object";topkey="Body";key="Body";filterid=key
    elif type == "aws_s3_bucket_object_lock_configuration":
        clfn="s3";descfn="get_object_lock_configuration";topkey="ObjectLockConfiguration";key="ObjectLockEnabled";filterid=key
    elif type == "aws_s3_bucket_objects":
        clfn="s3";descfn="list_objects";topkey="Contents";key="Key";filterid=key
    elif type == "aws_s3_bucket_ownership_controls":
        clfn="s3";descfn="get_bucket_ownership_controls";topkey="OwnershipControls";key="Rules";filterid=key
    elif type == "aws_s3_bucket_policy":
        clfn="s3";descfn="get_bucket_policy";topkey="Policy";key="Policy";filterid=key
    elif type == "aws_s3_bucket_public_access_block":
        clfn="s3";descfn="get_public_access_block";topkey="PublicAccessBlockConfiguration";key="BlockPublicAcls";filterid=key
    elif type == "aws_s3_bucket_replication_configuration":
        clfn="s3";descfn="get_bucket_replication";topkey="ReplicationConfiguration";key="Role";filterid=key
    elif type == "aws_s3_bucket_request_payment_configuration":
        clfn="s3";descfn="get_bucket_request_payment";topkey="Payer";key="Payer";filterid=key
    elif type == "aws_s3_bucket_server_side_encryption_configuration":
        clfn="s3";descfn="get_bucket_server_side_encryption_configuration";topkey="Rules";key="ApplyServerSideEncryptionByDefault.SSEAlgorithm";filterid=key
    elif type == "aws_s3_bucket_versioning":
        clfn="s3";descfn="get_bucket_versioning";topkey="Status";key="Status";filterid=key
    elif type == "aws_s3_bucket_website_configuration":
        clfn="s3";descfn="get_bucket_website";topkey="ErrorDocument";key="Key";filterid=key
    elif type == "aws_s3_directory_bucket":
        clfn="s3";descfn="list_buckets";topkey="Buckets";key="Name";filterid=key
    elif type == "aws_s3_directory_buckets":
        clfn="s3";descfn="list_buckets";topkey="Buckets";key="Name";filterid=key
    elif type == "aws_s3_object":
        clfn="s3";descfn="get_object";topkey="Body";key="Body";filterid=key
    elif type == "aws_s3_object_copy":
        clfn="s3";descfn="get_object";topkey="Body";key="Body";filterid=key
    elif type == "aws_s3_objects":
        clfn="s3";descfn="list_objects";topkey="Contents";key="Key";filterid=key
    elif type == "aws_s3control_access_grant":
        clfn="s3control";descfn="list_access_grants";topkey="AccessGrants";key="Grantee.DisplayName";filterid=key
    elif type == "aws_s3control_access_grants_instance":
        clfn="s3control";descfn="list_access_grants";topkey="AccessGrants";key="Grantee.DisplayName";filterid=key
    elif type == "aws_s3control_access_grants_instance_resource_policy":
        clfn="s3control";descfn="list_access_grants";topkey="AccessGrants";key="Grantee.DisplayName";filterid=key
    elif type == "aws_s3control_access_grants_location":
        clfn="s3control";descfn="list_access_grants";topkey="AccessGrants";key="Grantee.DisplayName";filterid=key
    elif type == "aws_s3control_access_point_policy":
        clfn="s3control";descfn="get_access_point_policy";topkey="Policy";key="Policy";filterid=key
    elif type == "aws_s3control_bucket":
        clfn="s3control";descfn="list_buckets";topkey="Buckets";key="Name";filterid=key
    elif type == "aws_s3control_bucket_lifecycle_configuration":
        clfn="s3control";descfn="get_bucket_lifecycle_configuration";topkey="Rules";key="ID";filterid=key
    elif type == "aws_s3control_bucket_policy":
        clfn="s3control";descfn="get_bucket_policy";topkey="Policy";key="Policy";filterid=key
    elif type == "aws_s3control_multi_region_access_point":
        clfn="s3control";descfn="list_access_points";topkey="AccessPoints";key="Name";filterid=key
    elif type == "aws_s3control_multi_region_access_point_policy":
        clfn="s3control";descfn="list_access_points";topkey="AccessPoints";key="Name";filterid=key
    elif type == "aws_s3control_object_lambda_access_point":
        clfn="s3control";descfn="list_access_points";topkey="AccessPoints";key="Name";filterid=key
    elif type == "aws_s3control_object_lambda_access_point_policy":
        clfn="s3control";descfn="list_access_points";topkey="AccessPoints";key="Name";filterid=key
    elif type == "aws_s3control_storage_lens_configuration":
        clfn="s3control";descfn="get_storage_lens_configuration";topkey="StorageLensConfiguration";key="Id";filterid=key
    elif type == "aws_s3outposts_endpoint":
        clfn="s3outposts";descfn="list_endpoints";topkey="Endpoints";key="EndpointArn";filterid=key
    elif type == "aws_sagemaker_app":
        clfn="sagemaker";descfn="list_apps";topkey="Apps";key="AppArn";filterid=key
    elif type == "aws_sagemaker_app_image_config":
        clfn="sagemaker";descfn="list_app_image_configs";topkey="AppImageConfigs";key="AppImageConfigArn";filterid=key
    elif type == "aws_sagemaker_code_repository":
        clfn="sagemaker";descfn="list_code_repositories";topkey="CodeRepositories";key="CodeRepositoryArn";filterid=key
    elif type == "aws_sagemaker_data_quality_job_definition":
        clfn="sagemaker";descfn="list_data_quality_job_definitions";topkey="DataQualityJobDefinitions";key="DataQualityJobDefinitionArn";filterid=key
    elif type == "aws_sagemaker_device":
        clfn="sagemaker";descfn="list_devices";topkey="Devices";key="DeviceArn";filterid=key
    elif type == "aws_sagemaker_device_fleet":
        clfn="sagemaker";descfn="list_device_fleets";topkey="DeviceFleets";key="DeviceFleetArn";filterid=key
    elif type == "aws_sagemaker_domain":
        clfn="sagemaker";descfn="list_domains";topkey="Domains";key="DomainArn";filterid=key
    elif type == "aws_sagemaker_endpoint":
        clfn="sagemaker";descfn="list_endpoints";topkey="Endpoints";key="EndpointArn";filterid=key
    elif type == "aws_sagemaker_endpoint_configuration":
        clfn="sagemaker";descfn="list_endpoint_configurations";topkey="EndpointConfigurations";key="EndpointConfigurationArn";filterid=key
    elif type == "aws_sagemaker_feature_group":
        clfn="sagemaker";descfn="list_feature_groups";topkey="FeatureGroups";key="FeatureGroupArn";filterid=key
    elif type == "aws_sagemaker_flow_definition":
        clfn="sagemaker";descfn="list_flow_definitions";topkey="FlowDefinitions";key="FlowDefinitionArn";filterid=key
    elif type == "aws_sagemaker_human_task_ui":
        clfn="sagemaker";descfn="list_human_task_uis";topkey="HumanTaskUIs";key="HumanTaskUiArn";filterid=key
    elif type == "aws_sagemaker_image":
        clfn="sagemaker";descfn="list_images";topkey="Images";key="ImageArn";filterid=key
    elif type == "aws_sagemaker_image_version":
        clfn="sagemaker";descfn="list_image_versions";topkey="ImageVersions";key="ImageVersionArn";filterid=key
    elif type == "aws_sagemaker_model":
        clfn="sagemaker";descfn="list_models";topkey="Models";key="ModelArn";filterid=key
    elif type == "aws_sagemaker_model_package_group":
        clfn="sagemaker";descfn="list_model_package_groups";topkey="ModelPackageGroups";key="ModelPackageGroupArn";filterid=key
    elif type == "aws_sagemaker_model_package_group_policy":
        clfn="sagemaker";descfn="get_model_package_group_policy";topkey="Policy";key="Policy";filterid=key
    elif type == "aws_sagemaker_monitoring_schedule":
        clfn="sagemaker";descfn="list_monitoring_schedules";topkey="MonitoringSchedules";key="MonitoringScheduleArn";filterid=key
    elif type == "aws_sagemaker_notebook_instance":
        clfn="sagemaker";descfn="list_notebook_instances";topkey="NotebookInstances";key="NotebookInstanceArn";filterid=key
    elif type == "aws_sagemaker_notebook_instance_lifecycle_configuration":
        clfn="sagemaker";descfn="list_notebook_instance_lifecycle_configs";topkey="NotebookInstanceLifecycleConfigs";key="NotebookInstanceLifecycleConfigArn";filterid=key
    elif type == "aws_sagemaker_pipeline":
        clfn="sagemaker";descfn="list_pipelines";topkey="Pipelines";key="PipelineArn";filterid=key
    elif type == "aws_sagemaker_prebuilt_ecr_image":
        clfn="sagemaker";descfn="list_prebuilt_ecr_images";topkey="PrebuiltEcrImages";key="PrebuiltEcrImageArn";filterid=key
    elif type == "aws_sagemaker_project":
        clfn="sagemaker";descfn="list_projects";topkey="Projects";key="ProjectArn";filterid=key
    elif type == "aws_sagemaker_servicecatalog_portfolio_status":
        clfn="sagemaker";descfn="get_service_catalog_portfolio_status";topkey="Status";key="Status";filterid=key
    elif type == "aws_sagemaker_space":
        clfn="sagemaker";descfn="list_spaces";topkey="Spaces";key="SpaceArn";filterid=key
    elif type == "aws_sagemaker_studio_lifecycle_config":
        clfn="sagemaker";descfn="list_studio_lifecycle_configs";topkey="StudioLifecycleConfigs";key="StudioLifecycleConfigArn";filterid=key
    elif type == "aws_sagemaker_user_profile":
        clfn="sagemaker";descfn="list_user_profiles";topkey="UserProfiles";key="UserProfileArn";filterid=key
    elif type == "aws_sagemaker_workforce":
        clfn="sagemaker";descfn="list_workforces";topkey="Workforces";key="WorkforceArn";filterid=key
    elif type == "aws_sagemaker_workteam":
        clfn="sagemaker";descfn="list_workteams";topkey="Workteams";key="WorkteamArn";filterid=key
    elif type == "aws_scheduler_schedule":
        clfn="scheduler";descfn="list_schedules";topkey="Schedules";key="ScheduleArn";filterid=key
    elif type == "aws_scheduler_schedule_group":
        clfn="scheduler";descfn="list_schedule_groups";topkey="ScheduleGroups";key="ScheduleGroupArn";filterid=key
    elif type == "aws_schemas_discoverer":
        clfn="schemas";descfn="list_discoverers";topkey="Discoverers";key="DiscovererArn";filterid=key
    elif type == "aws_schemas_registry":
        clfn="schemas";descfn="list_registries";topkey="Registries";key="RegistryArn";filterid=key
    elif type == "aws_schemas_registry_policy":
        clfn="schemas";descfn="get_registry_policy";topkey="Policy";key="Policy";filterid=key
    elif type == "aws_schemas_schema":
        clfn="schemas";descfn="list_schemas";topkey="Schemas";key="SchemaArn";filterid=key
    elif type == "aws_secretsmanager_random_password":
        clfn="secretsmanager";descfn="get_random_password";topkey="RandomPassword";key="RandomPassword";filterid=key
    #elif type == "aws_secretsmanager_secret":
    #    clfn="secretsmanager";descfn="list_secrets";topkey="Secrets";key="SecretArn";filterid=key
    elif type == "aws_secretsmanager_secret_policy":
        clfn="secretsmanager";descfn="get_secret_policy";topkey="Policy";key="Policy";filterid=key
    elif type == "aws_secretsmanager_secret_rotation":
        clfn="secretsmanager";descfn="get_secret_rotation";topkey="Rotation";key="Rotation";filterid=key
    elif type == "aws_secretsmanager_secret_version":
        clfn="secretsmanager";descfn="list_secret_version_ids";topkey="SecretVersions";key="SecretVersionId";filterid=key
    #elif type == "aws_secretsmanager_secrets":
    #    clfn="secretsmanager";descfn="list_secrets";topkey="Secrets";key="SecretArn";filterid=key
    #elif type == "aws_security_group":
    #    clfn="ec2";descfn="describe_security_groups";topkey="SecurityGroups";key="GroupId";filterid=key
    elif type == "aws_security_group_rule":
        clfn="ec2";descfn="describe_security_group_rules";topkey="SecurityGroupRules";key="RuleId";filterid=key
    elif type == "aws_security_groups":
        clfn="ec2";descfn="describe_security_groups";topkey="SecurityGroups";key="GroupId";filterid=key
    elif type == "aws_securityhub_account":
        clfn="securityhub";descfn="describe_hub";topkey="Hub";key="HubArn";filterid=key
    elif type == "aws_securityhub_action_target":
        clfn="securityhub";descfn="describe_action_targets";topkey="ActionTargets";key="ActionTargetArn";filterid=key
    elif type == "aws_securityhub_finding_aggregator":
        clfn="securityhub";descfn="describe_finding_aggregators";topkey="FindingAggregators";key="FindingAggregatorArn";filterid=key
    elif type == "aws_securityhub_insight":
        clfn="securityhub";descfn="describe_insights";topkey="Insights";key="InsightArn";filterid=key
    elif type == "aws_securityhub_invite_accepter":
        clfn="securityhub";descfn="describe_invite_accepters";topkey="InviteAccepters";key="InviteAccepterArn";filterid=key
    elif type == "aws_securityhub_member":
        clfn="securityhub";descfn="describe_members";topkey="Members";key="MemberArn";filterid=key
    elif type == "aws_securityhub_organization_admin_account":
        clfn="securityhub";descfn="describe_organization_admin_account";topkey="AdminAccount";key="AdminAccount";filterid=key
    elif type == "aws_securityhub_organization_configuration":
        clfn="securityhub";descfn="describe_organization_configuration";topkey="OrganizationConfiguration";key="OrganizationConfiguration";filterid=key
    elif type == "aws_securityhub_product_subscription":
        clfn="securityhub";descfn="describe_product_subscriptions";topkey="ProductSubscriptions";key="ProductSubscriptionArn";filterid=key
    elif type == "aws_securityhub_standards_control":
        clfn="securityhub";descfn="describe_standards_controls";topkey="StandardsControls";key="StandardsControlArn";filterid=key
    elif type == "aws_securityhub_standards_subscription":
        clfn="securityhub";descfn="describe_standards_subscriptions";topkey="StandardsSubscriptions";key="StandardsSubscriptionArn";filterid=key
    elif type == "aws_securitylake_data_lake":
        clfn="securitylake";descfn="describe_data_lakes";topkey="DataLakes";key="DataLakeArn";filterid=key
    elif type == "aws_serverlessapplicationrepository_application":
        clfn="serverlessrepo";descfn="list_applications";topkey="Applications";key="ApplicationId";filterid=key
    elif type == "aws_serverlessapplicationrepository_cloudformation_stack":
        clfn="serverlessrepo";descfn="list_application_versions";topkey="ApplicationVersions";key="ApplicationVersionId";filterid=key
    elif type == "aws_service_discovery_http_namespace":
        clfn="servicediscovery";descfn="list_http_namespaces";topkey="HttpNamespaces";key="HttpNamespaceArn";filterid=key
    elif type == "aws_service_discovery_instance":
        clfn="servicediscovery";descfn="list_instances";topkey="Instances";key="InstanceId";filterid=key
    elif type == "aws_service_discovery_private_dns_namespace":
        clfn="servicediscovery";descfn="list_private_dns_namespaces";topkey="PrivateDnsNamespaces";key="PrivateDnsNamespaceArn";filterid=key
    elif type == "aws_service_discovery_public_dns_namespace":
        clfn="servicediscovery";descfn="list_public_dns_namespaces";topkey="PublicDnsNamespaces";key="PublicDnsNamespaceArn";filterid=key
    elif type == "aws_service_discovery_service":
        clfn="servicediscovery";descfn="list_services";topkey="Services";key="ServiceArn";filterid=key
    elif type == "aws_servicecatalog_budget_resource_association":
        clfn="servicecatalog";descfn="list_budget_resource_associations";topkey="BudgetResourceAssociations";key="BudgetResourceAssociationId";filterid=key
    elif type == "aws_servicecatalog_constraint":
        clfn="servicecatalog";descfn="list_constraints";topkey="Constraints";key="ConstraintId";filterid=key
    elif type == "aws_servicecatalog_launch_paths":
        clfn="servicecatalog";descfn="list_launch_paths";topkey="LaunchPaths";key="Id";filterid=key
    elif type == "aws_servicecatalog_organizations_access":
        clfn="servicecatalog";descfn="list_organization_access";topkey="OrganizationAccess";key="Id";filterid=key
    elif type == "aws_servicecatalog_portfolio":
        clfn="servicecatalog";descfn="list_portfolios";topkey="Portfolios";key="Id";filterid=key
    elif type == "aws_servicecatalog_portfolio_constraints":
        clfn="servicecatalog";descfn="list_portfolio_constraints";topkey="PortfolioConstraints";key="Id";filterid=key
    elif type == "aws_servicecatalog_portfolio_share":
        clfn="servicecatalog";descfn="list_portfolio_shares";topkey="PortfolioShares";key="Id";filterid=key
    elif type == "aws_servicecatalog_principal_portfolio_association":
        clfn="servicecatalog";descfn="list_principal_portfolio_associations";topkey="PrincipalPortfolioAssociations";key="Id";filterid=key
    elif type == "aws_servicecatalog_product":
        clfn="servicecatalog";descfn="list_products";topkey="Products";key="Id";filterid=key
    elif type == "aws_servicecatalog_product_portfolio_association":
        clfn="servicecatalog";descfn="list_product_portfolio_associations";topkey="ProductPortfolioAssociations";key="Id";filterid=key
    elif type == "aws_servicecatalog_provisioned_product":
        clfn="servicecatalog";descfn="list_provisioned_products";topkey="ProvisionedProducts";key="Id";filterid=key
    elif type == "aws_servicecatalog_provisioning_artifact":
        clfn="servicecatalog";descfn="list_provisioning_artifacts";topkey="ProvisioningArtifacts";key="Id";filterid=key
    elif type == "aws_servicecatalog_provisioning_artifacts":
        clfn="servicecatalog";descfn="list_provisioning_artifacts";topkey="ProvisioningArtifacts";key="Id";filterid=key
    elif type == "aws_servicecatalog_service_action":
        clfn="servicecatalog";descfn="list_service_actions";topkey="ServiceActions";key="Id";filterid=key
    elif type == "aws_servicecatalog_tag_option":
        clfn="servicecatalog";descfn="list_tag_options";topkey="TagOptions";key="Id";filterid=key
    elif type == "aws_servicecatalog_tag_option_resource_association":
        clfn="servicecatalog";descfn="list_tag_option_resource_associations";topkey="TagOptionResourceAssociations";key="Id";filterid=key
    elif type == "aws_servicequotas_service":
        clfn="servicequotas";descfn="list_services";topkey="Services";key="ServiceCode";filterid=key
    elif type == "aws_servicequotas_service_quota":
        clfn="servicequotas";descfn="list_service_quotas";topkey="Quotas";key="QuotaCode";filterid=key
    elif type == "aws_servicequotas_template":
        clfn="servicequotas";descfn="list_templates";topkey="Templates";key="TemplateId";filterid=key
    elif type == "aws_servicequotas_template_association":
        clfn="servicequotas";descfn="list_template_associations";topkey="TemplateAssociations";key="TemplateAssociationId";filterid=key
    elif type == "aws_servicequotas_templates":
        clfn="servicequotas";descfn="list_templates";topkey="Templates";key="TemplateId";filterid=key
    elif type == "aws_ses_active_receipt_rule_set":
        clfn="ses";descfn="describe_active_receipt_rule_set";topkey="Metadata";key="Name";filterid=key
    elif type == "aws_ses_configuration_set":
        clfn="ses";descfn="describe_configuration_sets";topkey="ConfigurationSets";key="Name";filterid=key
    elif type == "aws_ses_domain_dkim":
        clfn="ses";descfn="describe_domain_dkim";topkey="DkimAttributes";key="DkimTokens";filterid=key
    elif type == "aws_ses_domain_identity":
        clfn="ses";descfn="describe_domain_identity";topkey="DomainIdentities";key="DomainIdentity";filterid=key
    elif type == "aws_ses_domain_identity_verification":
        clfn="ses";descfn="describe_domain_identity_verification";topkey="VerificationToken";key="VerificationToken";filterid=key
    elif type == "aws_ses_domain_mail_from":
        clfn="ses";descfn="describe_domain_mail_from";topkey="MailFromAttributes";key="MailFromDomain";filterid=key
    elif type == "aws_ses_email_identity":
        clfn="ses";descfn="describe_email_identity";topkey="IdentityType";key="IdentityType";filterid=key
    elif type == "aws_ses_event_destination":
        clfn="ses";descfn="describe_event_destination";topkey="EventDestination";key="EventDestination";filterid=key
    elif type == "aws_ses_identity_notification_topic":
        clfn="ses";descfn="describe_identity_notification_topic";topkey="Identity";key="Identity";filterid=key
    elif type == "aws_ses_identity_policy":
        clfn="ses";descfn="describe_identity_policy";topkey="Policy";key="Policy";filterid=key
    elif type == "aws_ses_receipt_filter":
        clfn="ses";descfn="describe_receipt_filter";topkey="Filter";key="Filter";filterid=key
    elif type == "aws_ses_receipt_rule":
        clfn="ses";descfn="describe_receipt_rule";topkey="Rule";key="Rule";filterid=key
    elif type == "aws_ses_receipt_rule_set":
        clfn="ses";descfn="describe_receipt_rule_set";topkey="Metadata";key="Name";filterid=key
    elif type == "aws_ses_template":
        clfn="ses";descfn="describe_template";topkey="Template";key="Template";filterid=key
    elif type == "aws_sesv2_account_vdm_attributes":
        clfn="sesv2";descfn="describe_account_vdm_attributes";topkey="AccountVdmAttributes";key="AccountVdmAttributes";filterid=key
    elif type == "aws_sesv2_configuration_set":
        clfn="sesv2";descfn="describe_configuration_set";topkey="ConfigurationSet";key="ConfigurationSet";filterid=key
    elif type == "aws_sesv2_configuration_set_event_destination":
        clfn="sesv2";descfn="describe_configuration_set_event_destination";topkey="EventDestination";key="EventDestination";filterid=key
    elif type == "aws_sesv2_contact_list":
        clfn="sesv2";descfn="describe_contact_list";topkey="ContactList";key="ContactList";filterid=key
    elif type == "aws_sesv2_dedicated_ip_assignment":
        clfn="sesv2";descfn="describe_dedicated_ip_assignment";topkey="DedicatedIpAssignment";key="DedicatedIpAssignment";filterid=key
    elif type == "aws_sesv2_dedicated_ip_pool":
        clfn="sesv2";descfn="describe_dedicated_ip_pool";topkey="DedicatedIpPool";key="DedicatedIpPool";filterid=key
    elif type == "aws_sesv2_email_identity":
        clfn="sesv2";descfn="describe_email_identity";topkey="EmailIdentity";key="EmailIdentity";filterid=key
    elif type == "aws_sesv2_email_identity_feedback_attributes":
        clfn="sesv2";descfn="describe_email_identity_feedback_attributes";topkey="EmailIdentityFeedbackAttributes";key="EmailIdentityFeedbackAttributes";filterid=key
    elif type == "aws_sesv2_email_identity_mail_from_attributes":
        clfn="sesv2";descfn="describe_email_identity_mail_from_attributes";topkey="MailFromAttributes";key="MailFromAttributes";filterid=key
    elif type == "aws_sfn_activity":
        clfn="stepfunctions";descfn="list_activities";topkey="Activities";key="ActivityArn";filterid=key
    elif type == "aws_sfn_alias":
        clfn="stepfunctions";descfn="list_aliases";topkey="Aliases";key="AliasArn";filterid=key
    elif type == "aws_sfn_state_machine":
        clfn="stepfunctions";descfn="list_state_machines";topkey="StateMachines";key="StateMachineArn";filterid=key
    elif type == "aws_sfn_state_machine_versions":
        clfn="stepfunctions";descfn="list_state_machine_versions";topkey="Versions";key="Version";filterid=key
    elif type == "aws_shield_application_layer_automatic_response":
        clfn="shield";descfn="list_application_layer_automatic_response_associations";topkey="ApplicationLayerAutomaticResponseAssociations";key="Id";filterid=key
    elif type == "aws_shield_drt_access_log_bucket_association":
        clfn="shield";descfn="list_drt_access_log_bucket_associations";topkey="DrtAccessLogBucketAssociations";key="Id";filterid=key
    elif type == "aws_shield_drt_access_role_arn_association":
        clfn="shield";descfn="list_drt_access_role_arn_associations";topkey="DrtAccessRoleArnAssociations";key="Id";filterid=key
    elif type == "aws_shield_protection":
        clfn="shield";descfn="list_protections";topkey="Protections";key="Id";filterid=key
    elif type == "aws_shield_protection_group":
        clfn="shield";descfn="list_protection_groups";topkey="ProtectionGroups";key="Id";filterid=key
    elif type == "aws_shield_protection_health_check_association":
        clfn="shield";descfn="list_protection_health_check_associations";topkey="ProtectionHealthCheckAssociations";key="Id";filterid=key
    elif type == "aws_signer_signing_job":
        clfn="signer";descfn="list_signing_jobs";topkey="Jobs";key="JobId";filterid=key
    elif type == "aws_signer_signing_profile":
        clfn="signer";descfn="list_signing_profiles";topkey="Profiles";key="ProfileName";filterid=key
    elif type == "aws_signer_signing_profile_permission":
        clfn="signer";descfn="list_signing_profile_permissions";topkey="Permissions";key="ProfileName";filterid=key
    elif type == "aws_simpledb_domain":
        clfn="simpledb";descfn="list_domains";topkey="DomainNames";key="DomainName";filterid=key
    elif type == "aws_snapshot_create_volume_permission":
        clfn="ec2";descfn="describe_create_volume_permissions";topkey="CreateVolumePermissions";key="UserId";filterid=key
    elif type == "aws_sns_platform_application":
        clfn="sns";descfn="list_platform_applications";topkey="PlatformApplications";key="PlatformApplicationArn";filterid=key
    elif type == "aws_sns_sms_preferences":
        clfn="sns";descfn="get_sms_preferences";topkey="SMSPreferences";key="SMSPreferences";filterid=key
    elif type == "aws_sns_topic":
        clfn="sns";descfn="list_topics";topkey="Topics";key="TopicArn";filterid=key
    elif type == "aws_sns_topic_data_protection_policy":
        clfn="sns";descfn="get_data_protection_policy";topkey="DataProtectionPolicy";key="DataProtectionPolicy";filterid=key
    elif type == "aws_sns_topic_policy":
        clfn="sns";descfn="get_topic_attributes";topkey="Attributes";key="Policy";filterid=key
    elif type == "aws_sns_topic_subscription":
        clfn="sns";descfn="list_subscriptions_by_topic";topkey="Subscriptions";key="SubscriptionArn";filterid=key
    elif type == "aws_spot_datafeed_subscription":
        clfn="ec2";descfn="describe_spot_datafeed_subscription";topkey="SpotDatafeedSubscription";key="SpotDatafeedSubscription";filterid=key
    elif type == "aws_spot_fleet_request":
        clfn="ec2";descfn="describe_spot_fleet_requests";topkey="SpotFleetRequestConfigs";key="SpotFleetRequestId";filterid=key
    elif type == "aws_spot_instance_request":
        clfn="ec2";descfn="describe_spot_instance_requests";topkey="SpotInstanceRequests";key="SpotInstanceRequestId";filterid=key
    elif type == "aws_sqs_queue":
        clfn="sqs";descfn="list_queues";topkey="QueueUrls";key="QueueUrl";filterid=key
    elif type == "aws_sqs_queue_policy":
        clfn="sqs";descfn="get_queue_attributes";topkey="Attributes";key="Policy";filterid=key
    elif type == "aws_sqs_queue_redrive_allow_policy":
        clfn="sqs";descfn="get_queue_attributes";topkey="Attributes";key="RedrivePolicy";filterid=key
    elif type == "aws_sqs_queue_redrive_policy":
        clfn="sqs";descfn="get_queue_attributes";topkey="Attributes";key="RedrivePolicy";filterid=key
    elif type == "aws_sqs_queues":
        clfn="sqs";descfn="list_queues";topkey="QueueUrls";key="QueueUrl";filterid=key
    elif type == "aws_ssm_activation":
        clfn="ssm";descfn="list_activations";topkey="ActivationList";key="ActivationId";filterid=key
    elif type == "aws_ssm_association":
        clfn="ssm";descfn="list_associations";topkey="AssociationList";key="AssociationId";filterid=key
    elif type == "aws_ssm_default_patch_baseline":
        clfn="ssm";descfn="get_default_patch_baseline";topkey="Baseline";key="BaselineId";filterid=key
    elif type == "aws_ssm_document":
        clfn="ssm";descfn="list_documents";topkey="DocumentIdentifiers";key="Name";filterid=key
    elif type == "aws_ssm_instances":
        clfn="ssm";descfn="list_associations";topkey="AssociationList";key="InstanceId";filterid=key
    elif type == "aws_ssm_maintenance_window":
        clfn="ssm";descfn="list_maintenance_windows";topkey="WindowIdentities";key="WindowId";filterid=key
    elif type == "aws_ssm_maintenance_window_target":
        clfn="ssm";descfn="list_targets_for_maintenance_window";topkey="WindowTargetIds";key="WindowTargetId";filterid=key
    elif type == "aws_ssm_maintenance_window_task":
        clfn="ssm";descfn="list_tasks_for_maintenance_window";topkey="TaskIds";key="TaskId";filterid=key
    elif type == "aws_ssm_maintenance_windows":
        clfn="ssm";descfn="list_maintenance_windows";topkey="WindowIdentities";key="WindowId";filterid=key
    elif type == "aws_ssm_parameter":
        clfn="ssm";descfn="describe_parameters";topkey="Parameters";key="Name";filterid=key
    elif type == "aws_ssm_parameters_by_path":
        clfn="ssm";descfn="describe_parameters";topkey="Parameters";key="Name";filterid=key
    elif type == "aws_ssm_patch_baseline":
        clfn="ssm";descfn="list_patch_baselines";topkey="BaselineIdentities";key="BaselineId";filterid=key
    elif type == "aws_ssm_patch_group":
        clfn="ssm";descfn="list_patch_groups";topkey="PatchGroups";key="PatchGroup";filterid=key
    elif type == "aws_ssm_resource_data_sync":
        clfn="ssm";descfn="list_resource_data_sync";topkey="ResourceDataSyncItems";key="SyncName";filterid=key
    elif type == "aws_ssm_service_setting":
        clfn="ssm";descfn="get_service_setting";topkey="ServiceSetting";key="SettingId";filterid=key
    elif type == "aws_ssmcontacts_contact":
        clfn="ssmcontacts";descfn="list_contacts";topkey="Contacts";key="Alias";filterid=key
    elif type == "aws_ssmcontacts_contact_channel":
        clfn="ssmcontacts";descfn="list_contact_channels";topkey="ContactChannels";key="ChannelId";filterid=key
    elif type == "aws_ssmcontacts_plan":
        clfn="ssmcontacts";descfn="list_plans";topkey="Plans";key="PlanId";filterid=key
    elif type == "aws_ssmincidents_replication_set":
        clfn="ssmincidents";descfn="list_replication_sets";topkey="ReplicationSets";key="Arn";filterid=key
    elif type == "aws_ssmincidents_response_plan":
        clfn="ssmincidents";descfn="list_response_plans";topkey="ResponsePlans";key="Arn";filterid=key
    elif type == "aws_ssoadmin_account_assignment":
        clfn="ssoadmin";descfn="list_account_assignments";topkey="AccountAssignments";key="AccountAssignmentCreationTime";filterid=key
    elif type == "aws_ssoadmin_application":
        clfn="ssoadmin";descfn="list_applications";topkey="Applications";key="ApplicationId";filterid=key
    elif type == "aws_ssoadmin_application_assignment":
        clfn="ssoadmin";descfn="list_application_assignments";topkey="ApplicationAssignments";key="AccountAssignmentCreationTime";filterid=key
    elif type == "aws_ssoadmin_application_assignment_configuration":
        clfn="ssoadmin";descfn="list_application_assignment_configurations";topkey="ApplicationAssignmentConfigurations";key="AccountAssignmentCreationTime";filterid=key
    elif type == "aws_ssoadmin_application_assignments":
        clfn="ssoadmin";descfn="list_application_assignments";topkey="ApplicationAssignments";key="AccountAssignmentCreationTime";filterid=key
    elif type == "aws_ssoadmin_application_providers":
        clfn="ssoadmin";descfn="list_application_providers";topkey="ApplicationProviders";key="ApplicationProviderId";filterid=key
    elif type == "aws_ssoadmin_customer_managed_policy_attachment":
        clfn="ssoadmin";descfn="list_customer_managed_policy_attachments";topkey="CustomerManagedPolicyAttachments";key="AccountAssignmentCreationTime";filterid=key
    elif type == "aws_ssoadmin_instance_access_control_attributes":
        clfn="ssoadmin";descfn="list_instance_access_control_attribute_configuration";topkey="InstanceAccessControlAttributeConfiguration";key="AccountAssignmentCreationTime";filterid=key
    elif type == "aws_ssoadmin_instances":
        clfn="ssoadmin";descfn="list_instances";topkey="Instances";key="InstanceArn";filterid=key
    elif type == "aws_ssoadmin_managed_policy_attachment":
        clfn="ssoadmin";descfn="list_managed_policy_attachments";topkey="ManagedPolicyAttachments";key="AccountAssignmentCreationTime";filterid=key
    elif type == "aws_ssoadmin_permission_set":
        clfn="ssoadmin";descfn="list_permission_sets";topkey="PermissionSets";key="PermissionSetArn";filterid=key
    elif type == "aws_ssoadmin_permission_set_inline_policy":
        clfn="ssoadmin";descfn="list_permission_set_inline_policies";topkey="PermissionSetInlinePolicies";key="PermissionSetArn";filterid=key
    elif type == "aws_ssoadmin_permissions_boundary_attachment":
        clfn="ssoadmin";descfn="list_permissions_boundary_attachments";topkey="PermissionsBoundaryAttachments";key="AccountAssignmentCreationTime";filterid=key
    elif type == "aws_ssoadmin_principal_application_assignments":
        clfn="ssoadmin";descfn="list_principal_application_assignments";topkey="PrincipalApplicationAssignments";key="AccountAssignmentCreationTime";filterid=key
    elif type == "aws_ssoadmin_trusted_token_issuer":
        clfn="ssoadmin";descfn="list_trusted_token_issuers";topkey="TrustedTokenIssuers";key="TrustedTokenIssuerId";filterid=key
    elif type == "aws_storagegateway_cache":
        clfn="storagegateway";descfn="describe_cache";topkey="Cache";key="CacheId";filterid=key
    elif type == "aws_storagegateway_cached_iscsi_volume":
        clfn="storagegateway";descfn="describe_cached_iscsi_volumes";topkey="CachediSCSIVolumes";key="VolumeARN";filterid=key
    elif type == "aws_storagegateway_file_system_association":
        clfn="storagegateway";descfn="describe_file_system_associations";topkey="FileSystemAssociations";key="FileSystemAssociationARN";filterid=key
    elif type == "aws_storagegateway_gateway":
        clfn="storagegateway";descfn="describe_gateways";topkey="Gateways";key="GatewayARN";filterid=key
    elif type == "aws_storagegateway_local_disk":
        clfn="storagegateway";descfn="describe_local_disks";topkey="Disks";key="DiskARN";filterid=key
    elif type == "aws_storagegateway_nfs_file_share":
        clfn="storagegateway";descfn="describe_nfs_file_shares";topkey="NFSFileShares";key="NFSFileShareARN";filterid=key
    elif type == "aws_storagegateway_smb_file_share":
        clfn="storagegateway";descfn="describe_smb_file_shares";topkey="SMBFileShares";key="SMBFileShareARN";filterid=key
    elif type == "aws_storagegateway_stored_iscsi_volume":
        clfn="storagegateway";descfn="describe_stored_iscsi_volumes";topkey="StorediSCSIVolumes";key="VolumeARN";filterid=key
    elif type == "aws_storagegateway_tape_pool":
        clfn="storagegateway";descfn="describe_tape_pools";topkey="TapePools";key="PoolARN";filterid=key
    elif type == "aws_storagegateway_upload_buffer":
        clfn="storagegateway";descfn="describe_upload_buffer";topkey="UploadBuffer";key="UploadBufferARN";filterid=key
    elif type == "aws_storagegateway_working_storage":
        clfn="storagegateway";descfn="describe_working_storage";topkey="WorkingStorage";key="WorkingStorageARN";filterid=key
    #elif type == "aws_subnet":
    #    clfn="ec2";descfn="describe_subnets";topkey="Subnets";key="SubnetId";filterid=key
    elif type == "aws_swf_domain":
        clfn="swf";descfn="list_domains";topkey="domainInfos";key="name";filterid=key
    elif type == "aws_synthetics_canary":
        clfn="synthetics";descfn="list_canaries";topkey="Canaries";key="Name";filterid=key
    elif type == "aws_synthetics_group":
        clfn="synthetics";descfn="list_canary_groups";topkey="Groups";key="Name";filterid=key
    elif type == "aws_synthetics_group_association":
        clfn="synthetics";descfn="list_group_associations";topkey="GroupAssociations";key="Name";filterid=key
    elif type == "aws_timestreamwrite_database":
        clfn="timestreamwrite";descfn="list_databases";topkey="Databases";key="DatabaseName";filterid=key
    elif type == "aws_timestreamwrite_table":
        clfn="timestreamwrite";descfn="list_tables";topkey="Tables";key="TableName";filterid=key
    elif type == "aws_transcribe_language_model":
        clfn="transcribe";descfn="list_language_models";topkey="LanguageModels";key="LanguageCode";filterid=key
    elif type == "aws_transcribe_medical_vocabulary":
        clfn="transcribe";descfn="list_medical_vocabularies";topkey="Vocabularies";key="VocabularyName";filterid=key
    elif type == "aws_transcribe_vocabulary":
        clfn="transcribe";descfn="list_vocabularies";topkey="Vocabularies";key="VocabularyName";filterid=key
    elif type == "aws_transcribe_vocabulary_filter":
        clfn="transcribe";descfn="list_vocabulary_filters";topkey="VocabularyFilters";key="VocabularyFilterName";filterid=key
    elif type == "aws_transfer_access":
        clfn="transfer";descfn="list_accesses";topkey="Accesses";key="AccessId";filterid=key
    elif type == "aws_transfer_agreement":
        clfn="transfer";descfn="list_agreements";topkey="Agreements";key="Arn";filterid=key
    elif type == "aws_transfer_certificate":
        clfn="transfer";descfn="list_certificates";topkey="Certificates";key="Arn";filterid=key
    elif type == "aws_transfer_connector":
        clfn="transfer";descfn="list_connectors";topkey="Connectors";key="Arn";filterid=key
    elif type == "aws_transfer_profile":
        clfn="transfer";descfn="list_profiles";topkey="Profiles";key="Arn";filterid=key
    elif type == "aws_transfer_server":
        clfn="transfer";descfn="list_servers";topkey="Servers";key="Arn";filterid=key
    elif type == "aws_transfer_ssh_key":
        clfn="transfer";descfn="list_ssh_public_keys";topkey="SshPublicKeys";key="Arn";filterid=key
    elif type == "aws_transfer_tag":
        clfn="transfer";descfn="list_tags";topkey="Tags";key="Key";filterid=key
    elif type == "aws_transfer_user":
        clfn="transfer";descfn="list_users";topkey="Users";key="Arn";filterid=key
    elif type == "aws_transfer_workflow":
        clfn="transfer";descfn="list_workflows";topkey="Workflows";key="Arn";filterid=key
    elif type == "aws_verifiedaccess_endpoint":
        clfn="verifiedaccess";descfn="list_endpoints";topkey="Endpoints";key="EndpointId";filterid=key
    elif type == "aws_verifiedaccess_group":
        clfn="verifiedaccess";descfn="list_groups";topkey="Groups";key="GroupId";filterid=key
    elif type == "aws_verifiedaccess_instance":
        clfn="verifiedaccess";descfn="list_instances";topkey="Instances";key="InstanceId";filterid=key
    elif type == "aws_verifiedaccess_instance_logging_configuration":
        clfn="verifiedaccess";descfn="list_instance_logging_configurations";topkey="InstanceLoggingConfigurations";key="InstanceId";filterid=key
    elif type == "aws_verifiedaccess_instance_trust_provider_attachment":
        clfn="verifiedaccess";descfn="list_instance_trust_providers";topkey="InstanceTrustProviders";key="InstanceId";filterid=key
    elif type == "aws_verifiedaccess_trust_provider":
        clfn="verifiedaccess";descfn="list_trust_providers";topkey="TrustProviders";key="TrustProviderId";filterid=key
    elif type == "aws_volume_attachment":
        clfn="ec2";descfn="describe_volume_status";topkey="VolumeStatuses";key="VolumeId";filterid=key
    #elif type == "aws_vpc":
    #    clfn="ec2";descfn="describe_vpcs";topkey="Vpcs";key="VpcId";filterid=key
    #elif type == "aws_vpc_dhcp_options":
    #    clfn="ec2";descfn="describe_dhcp_options";topkey="DhcpOptions";key="DhcpOptionsId";filterid=key
    elif type == "aws_vpc_dhcp_options_association":
        clfn="ec2";descfn="describe_dhcp_options_associations";topkey="DhcpOptionsAssociations";key="DhcpOptionsId";filterid=key
    #elif type == "aws_vpc_endpoint":
    #    clfn="ec2";descfn="describe_vpc_endpoints";topkey="VpcEndpoints";key="VpcEndpointId";filterid=key
    elif type == "aws_vpc_endpoint_connection_accepter":
        clfn="ec2";descfn="describe_vpc_endpoint_connection_accepters";topkey="VpcEndpointConnectionAccepters";key="VpcEndpointConnectionAccepterId";filterid=key
    elif type == "aws_vpc_endpoint_connection_notification":
        clfn="ec2";descfn="describe_vpc_endpoint_connection_notifications";topkey="VpcEndpointConnectionNotifications";key="VpcEndpointConnectionNotificationId";filterid=key
    elif type == "aws_vpc_endpoint_policy":
        clfn="ec2";descfn="describe_vpc_endpoint_service_policies";topkey="Policies";key="PolicyDocument";filterid=key
    elif type == "aws_vpc_endpoint_route_table_association":
        clfn="ec2";descfn="describe_vpc_endpoint_route_table_associations";topkey="RouteTableAssociations";key="RouteTableAssociationId";filterid=key
    elif type == "aws_vpc_endpoint_security_group_association":
        clfn="ec2";descfn="describe_vpc_endpoint_security_group_associations";topkey="SecurityGroupAssociations";key="SecurityGroupId";filterid=key
    elif type == "aws_vpc_endpoint_service":
        clfn="ec2";descfn="describe_vpc_endpoint_services";topkey="ServiceNames";key="ServiceName";filterid=key
    elif type == "aws_vpc_endpoint_service_allowed_principal":
        clfn="ec2";descfn="describe_vpc_endpoint_service_allowed_principals";topkey="AllowedPrincipals";key="Principal";filterid=key
    elif type == "aws_vpc_endpoint_subnet_association":
        clfn="ec2";descfn="describe_vpc_endpoint_subnet_associations";topkey="SubnetAssociations";key="SubnetId";filterid=key
    elif type == "aws_vpc_ipam":
        clfn="ec2";descfn="describe_ipams";topkey="Ipams";key="IpamId";filterid=key
    elif type == "aws_vpc_ipam_organization_admin_account":
        clfn="ec2";descfn="describe_ipam_organization_admin_accounts";topkey="OrganizationAdminAccounts";key="AccountId";filterid=key
    elif type == "aws_vpc_ipam_pool":
        clfn="ec2";descfn="describe_ipam_pools";topkey="Pools";key="PoolId";filterid=key
    elif type == "aws_vpc_ipam_pool_cidr":
        clfn="ec2";descfn="describe_ipam_pool_cidrs";topkey="Cidrs";key="Cidr";filterid=key
    elif type == "aws_vpc_ipam_pool_cidr_allocation":
        clfn="ec2";descfn="describe_ipam_pool_cidr_allocations";topkey="Allocations";key="AllocationId";filterid=key
    elif type == "aws_vpc_ipam_preview_next_cidr":
        clfn="ec2";descfn="describe_ipam_preview_next_cidrs";topkey="Cidrs";key="Cidr";filterid=key
    elif type == "aws_vpc_ipam_resource_discovery":
        clfn="ec2";descfn="describe_ipam_resource_discoveries";topkey="ResourceDiscoveries";key="ResourceDiscoveryId";filterid=key
    elif type == "aws_vpc_ipam_resource_discovery_association":
        clfn="ec2";descfn="describe_ipam_resource_discovery_associations";topkey="ResourceDiscoveryAssociations";key="ResourceDiscoveryAssociationId";filterid=key
    elif type == "aws_vpc_ipam_scope":
        clfn="ec2";descfn="describe_ipam_scopes";topkey="Scopes";key="ScopeId";filterid=key
    #elif type == "aws_vpc_ipv4_cidr_block_association":
    #    clfn="ec2";descfn="describe_vpc_cidr_block_associations";topkey="CidrBlockAssociations";key="AssociationId";filterid=key
    elif type == "aws_vpc_ipv6_cidr_block_association":
        clfn="ec2";descfn="describe_vpc_cidr_block_associations";topkey="CidrBlockAssociations";key="AssociationId";filterid=key
    elif type == "aws_vpc_network_performance_metric_subscription":
        clfn="ec2";descfn="describe_network_insights_path_subscriptions";topkey="NetworkInsightsPathSubscriptions";key="NetworkInsightsPathSubscriptionId";filterid=key
    elif type == "aws_vpc_peering_connection":
        clfn="ec2";descfn="describe_vpc_peering_connections";topkey="VpcPeeringConnections";key="VpcPeeringConnectionId";filterid=key
    elif type == "aws_vpc_peering_connection_accepter":
        clfn="ec2";descfn="describe_vpc_peering_connection_accepters";topkey="VpcPeeringConnectionAccepters";key="VpcPeeringConnectionId";filterid=key
    elif type == "aws_vpc_peering_connection_options":
        clfn="ec2";descfn="describe_vpc_peering_connection_options";topkey="VpcPeeringConnectionOptions";key="VpcPeeringConnectionId";filterid=key
    elif type == "aws_vpc_security_group_egress_rule":
        clfn="ec2";descfn="describe_security_group_rules";topkey="SecurityGroupRules";key="SecurityGroupRuleId";filterid=key
    elif type == "aws_vpc_security_group_ingress_rule":
        clfn="ec2";descfn="describe_security_group_rules";topkey="SecurityGroupRules";key="SecurityGroupRuleId";filterid=key
    #elif type == "aws_vpclattice_access_log_subscription":
    #    clfn="vpclattice";descfn="list_access_log_subscriptions";topkey="AccessLogSubscriptions";key="AccessLogSubscriptionId";filterid=key
    #elif type == "aws_vpclattice_auth_policy":
    #    clfn="vpclattice";descfn="list_auth_policies";topkey="AuthPolicies";key="AuthPolicyId";filterid=key
    #elif type == "aws_vpclattice_listener":
    #    clfn="vpclattice";descfn="list_listeners";topkey="Listeners";key="ListenerId";filterid=key
    #elif type == "aws_vpclattice_listener_rule":
    #    clfn="vpclattice";descfn="list_listener_rules";topkey="ListenerRules";key="ListenerRuleId";filterid=key
    #elif type == "aws_vpclattice_resource_policy":
    #    clfn="vpclattice";descfn="list_resource_policies";topkey="ResourcePolicies";key="ResourcePolicyId";filterid=key
    #elif type == "aws_vpclattice_service":
    #    clfn="vpclattice";descfn="list_services";topkey="Services";key="ServiceId";filterid=key
    #elif type == "aws_vpclattice_service_network":
    #    clfn="vpclattice";descfn="list_service_networks";topkey="ServiceNetworks";key="ServiceNetworkId";filterid=key
    #elif type == "aws_vpclattice_service_network_service_association":
    #    clfn="vpclattice";descfn="list_service_network_service_associations";topkey="ServiceNetworkServiceAssociations";key="ServiceNetworkServiceAssociationId";filterid=key
    #elif type == "aws_vpclattice_service_network_vpc_association":
    #    clfn="vpclattice";descfn="list_service_network_vpc_associations";topkey="ServiceNetworkVpcAssociations";key="ServiceNetworkVpcAssociationId";filterid=key
    #elif type == "aws_vpclattice_target_group":
    #    clfn="vpclattice";descfn="list_target_groups";topkey="TargetGroups";key="TargetGroupId";filterid=key
    elif type == "aws_vpclattice_target_group_attachment":
        clfn="vpclattice";descfn="list_target_group_attachments";topkey="TargetGroupAttachments";key="TargetGroupAttachmentId";filterid=key
    elif type == "aws_vpn_connection":
        clfn="ec2";descfn="describe_vpn_connections";topkey="VpnConnections";key="VpnConnectionId";filterid=key
    elif type == "aws_vpn_connection_route":
        clfn="ec2";descfn="describe_vpn_connection_routes";topkey="VpnConnectionRoutes";key="DestinationCidrBlock";filterid=key
    elif type == "aws_vpn_gateway":
        clfn="ec2";descfn="describe_vpn_gateways";topkey="VpnGateways";key="VpnGatewayId";filterid=key
    elif type == "aws_vpn_gateway_attachment":
        clfn="ec2";descfn="describe_vpn_gateway_attachments";topkey="VpnGatewayAttachments";key="VpnGatewayId";filterid=key
    elif type == "aws_vpn_gateway_route_propagation":
        clfn="ec2";descfn="describe_vpn_gateway_route_propagations";topkey="VpnGatewayRoutePropagations";key="VpnGatewayId";filterid=key
    elif type == "aws_waf_byte_match_set":
        clfn="waf";descfn="list_byte_match_sets";topkey="ByteMatchSets";key="ByteMatchSetId";filterid=key
    elif type == "aws_waf_geo_match_set":
        clfn="waf";descfn="list_geo_match_sets";topkey="GeoMatchSets";key="GeoMatchSetId";filterid=key
    elif type == "aws_waf_ipset":
        clfn="waf";descfn="list_ip_sets";topkey="IPSets";key="IPSetId";filterid=key
    elif type == "aws_waf_rate_based_rule":
        clfn="waf";descfn="list_rate_based_rules";topkey="RateBasedRules";key="RuleId";filterid=key
    elif type == "aws_waf_regex_match_set":
        clfn="waf";descfn="list_regex_match_sets";topkey="RegexMatchSets";key="RegexMatchSetId";filterid=key
    elif type == "aws_waf_regex_pattern_set":
        clfn="waf";descfn="list_regex_pattern_sets";topkey="RegexPatternSets";key="RegexPatternSetId";filterid=key
    elif type == "aws_waf_rule":
        clfn="waf";descfn="list_rules";topkey="Rules";key="RuleId";filterid=key
    elif type == "aws_waf_rule_group":
        clfn="waf";descfn="list_rule_groups";topkey="RuleGroups";key="RuleGroupId";filterid=key
    elif type == "aws_waf_size_constraint_set":
        clfn="waf";descfn="list_size_constraint_sets";topkey="SizeConstraintSets";key="SizeConstraintSetId";filterid=key
    elif type == "aws_waf_sql_injection_match_set":
        clfn="waf";descfn="list_sql_injection_match_sets";topkey="SqlInjectionMatchSets";key="SqlInjectionMatchSetId";filterid=key
    elif type == "aws_waf_web_acl":
        clfn="waf";descfn="list_web_acls";topkey="WebACLs";key="WebACLId";filterid=key
    elif type == "aws_waf_xss_match_set":
        clfn="waf";descfn="list_xss_match_sets";topkey="XssMatchSets";key="XssMatchSetId";filterid=key
    elif type == "aws_wafregional_byte_match_set":
        clfn="wafregional";descfn="list_byte_match_sets";topkey="ByteMatchSets";key="ByteMatchSetId";filterid=key
    elif type == "aws_wafregional_geo_match_set":
        clfn="wafregional";descfn="list_geo_match_sets";topkey="GeoMatchSets";key="GeoMatchSetId";filterid=key
    elif type == "aws_wafregional_ipset":
        clfn="wafregional";descfn="list_ip_sets";topkey="IPSets";key="IPSetId";filterid=key
    elif type == "aws_wafregional_rate_based_rule":
        clfn="wafregional";descfn="list_rate_based_rules";topkey="RateBasedRules";key="RuleId";filterid=key
    elif type == "aws_wafregional_regex_match_set":
        clfn="wafregional";descfn="list_regex_match_sets";topkey="RegexMatchSets";key="RegexMatchSetId";filterid=key
    elif type == "aws_wafregional_regex_pattern_set":
        clfn="wafregional";descfn="list_regex_pattern_sets";topkey="RegexPatternSets";key="RegexPatternSetId";filterid=key
    elif type == "aws_wafregional_rule":
        clfn="wafregional";descfn="list_rules";topkey="Rules";key="RuleId";filterid=key
    elif type == "aws_wafregional_rule_group":
        clfn="wafregional";descfn="list_rule_groups";topkey="RuleGroups";key="RuleGroupId";filterid=key
    elif type == "aws_wafregional_size_constraint_set":
        clfn="wafregional";descfn="list_size_constraint_sets";topkey="SizeConstraintSets";key="SizeConstraintSetId";filterid=key
    elif type == "aws_wafregional_sql_injection_match_set":
        clfn="wafregional";descfn="list_sql_injection_match_sets";topkey="SqlInjectionMatchSets";key="SqlInjectionMatchSetId";filterid=key
    elif type == "aws_wafregional_web_acl":
        clfn="wafregional";descfn="list_web_acls";topkey="WebACLs";key="WebACLId";filterid=key
    elif type == "aws_wafregional_web_acl_association":
        clfn="wafregional";descfn="list_web_acl_associations";topkey="WebACLAssociations";key="AssociationId";filterid=key
    elif type == "aws_wafregional_xss_match_set":
        clfn="wafregional";descfn="list_xss_match_sets";topkey="XssMatchSets";key="XssMatchSetId";filterid=key
    elif type == "aws_wafv2_ip_set":
        clfn="wafv2";descfn="list_ip_sets";topkey="IPSets";key="IPSetId";filterid=key
    elif type == "aws_wafv2_regex_pattern_set":
        clfn="wafv2";descfn="list_regex_pattern_sets";topkey="RegexPatternSets";key="RegexPatternSetId";filterid=key
    elif type == "aws_wafv2_rule_group":
        clfn="wafv2";descfn="list_rule_groups";topkey="RuleGroups";key="RuleGroupId";filterid=key
    elif type == "aws_wafv2_web_acl":
        clfn="wafv2";descfn="list_web_acls";topkey="WebACLs";key="WebACLId";filterid=key
    elif type == "aws_wafv2_web_acl_association":
        clfn="wafv2";descfn="list_web_acl_associations";topkey="WebACLAssociations";key="AssociationId";filterid=key
    elif type == "aws_wafv2_web_acl_logging_configuration":
        clfn="wafv2";descfn="list_web_acl_logging_configurations";topkey="WebACLLoggingConfigurations";key="ResourceArn";filterid=key
    elif type == "aws_worklink_fleet":
        clfn="worklink";descfn="list_fleets";topkey="Fleets";key="FleetArn";filterid=key
    elif type == "aws_worklink_website_certificate_authority_association":
        clfn="worklink";descfn="list_website_certificate_authority_associations";topkey="WebsiteCertificateAuthorityAssociations";key="AssociationId";filterid=key
    elif type == "aws_workspaces_connection_alias":
        clfn="workspaces";descfn="list_connection_aliases";topkey="ConnectionAliases";key="ConnectionAliasId";filterid=key
    elif type == "aws_workspaces_directory":
        clfn="workspaces";descfn="list_directories";topkey="Directories";key="DirectoryId";filterid=key
    elif type == "aws_workspaces_ip_group":
        clfn="workspaces";descfn="list_ip_groups";topkey="IpGroups";key="GroupId";filterid=key
    elif type == "aws_workspaces_workspace":
        clfn="workspaces";descfn="list_workspaces";topkey="Workspaces";key="WorkspaceId";filterid=key
    elif type == "aws_xray_encryption_config":
        clfn="xray";descfn="get_encryption_config";topkey="EncryptionConfig";key="EncryptionConfigId";filterid=key
    elif type == "aws_xray_group":
        clfn="xray";descfn="get_group";topkey="Group";key="GroupName";filterid=key
    elif type == "aws_xray_sampling_rule":
        clfn="xray";descfn="get_sampling_rules";topkey="SamplingRuleRecords";key="SamplingRuleRecord";filterid=key
    ## END AUTOGEN ##






    return clfn,descfn,topkey,key,filterid
