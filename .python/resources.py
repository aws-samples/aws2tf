import aws_dict

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
    clfn=aws_dict.aws_resources[type]['clfn']
    descfn=aws_dict.aws_resources[type]['descfn']
    topkey=aws_dict.aws_resources[type]['topkey']
    key=aws_dict.aws_resources[type]['key']
    filterid=aws_dict.aws_resources[type]['filterid']

    print("type:",type,"id:",id,"clfn:",clfn,"descfn:",descfn,"topkey:",topkey,"key:",key,"filterid:",filterid)


    if type == "aws_vpc_ipv4_cidr_block_association": 
        clfn="ec2";descfn="describe_vpcs";topkey='Vpcs';key="VpcId";filterid=key
    
    elif type == "aws_vpc_endpoint": 
        if id is not None and "vpc-" in id: filterid="VpcId"
    
    elif type in "aws_subnet":
        if id is not None and "vpc-" in id: filterid="VpcId"

    elif type == "aws_security_group": 
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
        return clfn,descfn,topkey,key,filterid
     
    elif type == "aws_route_table": 
        clfn="ec2";descfn="describe_route_tables";topkey="RouteTables";key="RouteTableId";filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"    

    elif type == "aws_route_table_association":
        clfn="ec2";descfn="describe_route_tables";topkey="RouteTables";key=".Associations.0.SubnetId";filterid=key
        if id is not None and "vpc-" in id: filterid=".Associations.0.VpcId" 
        if id is not None and "subnet-" in id: filterid=".Associations.0.SubnetId" 
        return clfn,descfn,topkey,key,filterid



    elif type == "aws_default_route_table":
        clfn="ec2";descfn="describe_route_tables";topkey="RouteTables";key="RouteTableId";filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"
        return clfn,descfn,topkey,key,filterid

    elif type == "aws_default_security_group":
        clfn="ec2";descfn="describe_security_groups";topkey="SecurityGroups";key="GroupId";filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"

    elif type == "aws_default_subnet":
        clfn="ec2";descfn="describe_subnets";topkey="Subnets";key="SubnetId";filterid=key
        if id is not None and "vpc-" in id: filterid="VpcId"

    elif type == "aws_default_vpc": 
        clfn="ec2";descfn="describe_vpcs";topkey="Vpcs";key="VpcId";filterid=KeyError

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

    elif type == "aws_iam_role_policy": 
        clfn="iam";descfn="list_role_policies";topkey="PolicyNames";key="PolicyNames";filterid="RoleName"

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

### get from dict



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


    return clfn,descfn,topkey,key,filterid
