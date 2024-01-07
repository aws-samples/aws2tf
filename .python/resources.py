from aws_resources import aws_dict

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
    
    if id is not None:
        if "vpc-" in id:
            if type == "aws_vpc_endpoint": filterid="VpcId";return clfn,descfn,topkey,key,filterid
            elif type in "aws_subnet": filterid="VpcId";return clfn,descfn,topkey,key,filterid
            elif type == "aws_security_group": filterid="VpcId" ;return clfn,descfn,topkey,key,filterid        
            elif type == "aws_internet_gateway": filterid=".Attachments.0.VpcId"  ;return clfn,descfn,topkey,key,filterid
            elif type == "aws_nat_gateway": filterid="VpcId"  ;return clfn,descfn,topkey,key,filterid         
            elif type == "aws_network_acl": filterid="VpcId" ;return clfn,descfn,topkey,key,filterid
            elif type == "aws_default_network_acl": filterid="VpcId" ;return clfn,descfn,topkey,key,filterid
            elif type == "aws_route_table": filterid="VpcId"  ;return clfn,descfn,topkey,key,filterid  
            elif type == "aws_route_table_association":filterid=".Associations.0.VpcId" ;return clfn,descfn,topkey,key,filterid
            elif type == "aws_default_route_table": filterid="VpcId";return clfn,descfn,topkey,key,filterid
            elif type == "aws_default_security_group": filterid="VpcId" ;return clfn,descfn,topkey,key,filterid
            elif type == "aws_default_subnet": filterid="VpcId" ;return clfn,descfn,topkey,key,filterid
            elif type == "aws_default_internet_gateway": filterid="attachment.vpc-id" ;return clfn,descfn,topkey,key,filterid
            elif type == "aws_image": filterid="VpcId" ;return clfn,descfn,topkey,key,filterid
            elif type == "aws_key_pair": filterid="VpcId" ;return clfn,descfn,topkey,key,filterid
            elif type == "aws_launch_configuration": filterid="VpcId" ;return clfn,descfn,topkey,key,filterid
            elif type == "aws_vpc_ipv4_cidr_block_association": filterid="VpcId" ;return clfn,descfn,topkey,key,filterid
            elif type == "aws_flow_log": filterid="VpcId" ;return clfn,descfn,topkey,key,filterid
 
        elif "arn:aws:iam::" in id:
            if type == "aws_iam_role": filterid="Arn" ;return clfn,descfn,topkey,key,filterid
            if type == "aws_iam_policy": filterid="Arn" ;return clfn,descfn,topkey,key,filterid
            if type == "aws_iam_user": filterid="Arn" ;return clfn,descfn,topkey,key,filterid

        elif "subnet-" in id:
            if type == "aws_route_table_association": filterid=".Associations.0.SubnetId" ;return clfn,descfn,topkey,key,filterid

        elif "lt-" in id:
            if type == "aws_launch_template":filterid="LaunchTemplateIds"; return clfn,descfn,topkey,key,filterid


    return clfn,descfn,topkey,key,filterid
