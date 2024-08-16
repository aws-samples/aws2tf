noimport = {
    ### this section no import - as per Terraform docs
    "aws_acm_certificate_validation": True,
    "aws_acmpca_certificate_authority_certificate": True,
    "aws_acmpca_permission": True,
    "aws_ami_copy": True,
    "aws_ami_from_instance": True,
    "aws_appautoscaling_scheduled_action": True,
    "aws_autoscaling_attachment": True,
    "aws_autoscaling_notification": True,
    "aws_autoscaling_traffic_source_attachment": True,
    "aws_cloud9_environment_ec2": True,
    "aws_cloudcontrolapi_resource": True,
    "aws_codecatalyst_dev_environment": True,
    "aws_codecommit_trigger": True,
    "aws_codegurureviewer_repository_association": True,
    "aws_cognito_user_in_group": True,
    "aws_default_route_table": True,
    "aws_detective_organization_admin_account": True,
    "aws_dx_bgp_peer": True,
    "aws_dx_connection_association": True,
    "aws_dx_connection_confirmation": True,
    "aws_dx_hosted_connection": True,
    "aws_dx_macsec_key_association": True,
    "aws_dynamodb_table_item": True,
    "aws_ebs_snapshot_copy": True,
    "aws_ebs_snapshot_import": True,
    "aws_ec2_image_block_public_access": True,
    "aws_ec2_transit_gateway_multicast_domain_association": True,
    "aws_ec2_transit_gateway_multicast_group_member": True,
    "aws_ec2_transit_gateway_multicast_group_source": True,
    "aws_elastic_beanstalk_application_version": True,
    "aws_elastic_beanstalk_configuration_template": True,
    "aws_elasticsearch_domain_policy": True,
    "aws_elb_attachment": True,
    "aws_grafana_role_association": True,
    "aws_grafana_workspace_api_key": True,
    "aws_guardduty_detector_feature": True,
    "aws_guardduty_organization_configuration_feature": True,
    "aws_iam_group_membership": True,
    "aws_iam_policy_attachment": True,
    "aws_iam_security_token_service_preferences": True,
    "aws_iam_service_specific_credential": True,
    "aws_inspector2_enabler": True,
    "aws_inspector2_organization_configuration": True,
    "aws_inspector_resource_group": True,
    "aws_iot_ca_certificate": True,
    "aws_iot_certificate": True,
    "aws_iot_indexing_configuration": True,
    "aws_iot_logging_options": True,
    "aws_iot_policy_attachment": True,
    "aws_iot_thing_principal_attachment": True,
    "aws_kms_ciphertext": True,
    #
    "aws_lakeformation_data_lake_settings": True,
    "aws_lakeformation_permissions": True,
    "aws_lakeformation_resource": True,
    "aws_lakeformation_resource_lf_tags": True,
    #
    "aws_lambda_invocation": True,
    "aws_lb_cookie_stickiness_policy": True,
    "aws_lb_ssl_negotiation_policy": True,
    "aws_lb_target_group_attachment": True,
    #
    "aws_lightsail_domain": True,
    "aws_lightsail_instance_public_ports": True,
    "aws_lightsail_key_pair": True,
    "aws_lightsail_static_ip": True,
    "aws_lightsail_static_ip_attachment": True,
    #
    "aws_load_balancer_backend_server_policy": True,
    "aws_load_balancer_listener_policy": True,
    "aws_load_balancer_policy": True,
    "aws_main_route_table_association": True,
    "aws_networkmanager_attachment_accepter": True,
    "aws_opensearch_domain_policy": True,
    "aws_opensearch_package_association": True,
    "aws_opsworks_ecs_cluster_layer": True,
    "aws_opsworks_ganglia_layer": True,
    "aws_opsworks_haproxy_layer": True,
    "aws_opsworks_java_app_layer": True,
    "aws_opsworks_memcached_layer": True,
    "aws_opsworks_mysql_layer": True,
    "aws_opsworks_nodejs_app_layer": True,
    "aws_opsworks_permission": True,
    "aws_opsworks_rails_app_layer": True,
    "aws_opsworks_rds_db_instance": True,
    "aws_opsworks_user_profile": True,
    "aws_proxy_protocol_policy": True,
    "aws_qldb_stream": True,
    "aws_quicksight_account_subscription": True,
    "aws_quicksight_user": True,
    "aws_resourcegroups_resource": True,
    "aws_s3_object_copy": True,
    "aws_securityhub_standards_control": True,
    "aws_servicecatalog_organizations_access": True,
    "aws_ses_domain_identity_verification": True,
    "aws_shield_application_layer_automatic_response": True,
    "aws_shield_drt_access_log_bucket_association": True,
    "aws_shield_drt_access_role_arn_association": True,
    "aws_snapshot_create_volume_permission": True,
    "aws_sns_sms_preferences": True,
    "aws_spot_instance_request": True,
    "aws_ssm_patch_group": True,
    "aws_verifiedaccess_group": True,
    "aws_vpc_endpoint_security_group_association": True,
    "aws_vpc_endpoint_service_allowed_principal": True,
    "aws_vpc_ipam_preview_next_cidr": True,
    "aws_vpc_network_performance_metric_subscription": True,
    "aws_vpclattice_target_group_attachment": True,
    "aws_vpn_connection_route": True,
    "aws_vpn_gateway_attachment": True,
    "aws_vpn_gateway_route_propagation": True,
    #
    # hand driven exclusions
    #
    "aws_wafregional_web_acl_association": True,    # get it from target rsource
    "aws_vpc_ipam_organization_admin_account": True,
    "aws_grafana_license_association": True,
    # via other resources
    "aws_api_gateway_method_response": True,
    "aws_api_gateway_method_settings": True,
    # API not available or other problems as described
    "aws_appintegrations_data_integration": True,
    "aws_appintegrations_event_integration": True,
    "aws_connect_instance": True,
    "aws_devicefarm_instance_profile": True,
    "aws_devicefarm_project": True,
    "aws_globalaccelerator_accelerator": True,
    "aws_globalaccelerator_custom_routing_accelerator": True,
    "aws_route53domains_registered_domain": True,
    "aws_route53recoverycontrolconfig_cluster": True,
    "aws_route53recoverycontrolconfig_control_panel": True,
    "aws_route53recoveryreadiness_cell": True,
    "aws_route53recoveryreadiness_readiness_check": True,
    "aws_route53recoveryreadiness_recovery_group": True,
    "aws_route53recoveryreadiness_resource_set": True,
    "aws_cloudwatch_query_definition": True,
    "aws_cloudfront_response_headers_policy": True, ### insufficient block errors on plan
    "aws_db_cluster_snapshot": True, ### id is too long
    "db_cluster_snapshot_identifier": True, ### only lowercase alphanumeric characters and hyphens allowed in id
    "aws_db_instance_role_association": True, ### an association
    "aws_vpc_endpoint_subnet_association": True, ### an association
    "aws_ec2_managed_prefix_list": True, ### max_entries issue
    "aws_docdb_cluster_snapshot": True,  ### id is too long
    "aws_ecr_replication_configuration": True, ### unsure how to get in 
    "aws_ec2_tag": True, ### only use when resources created outside of Terraform
    "aws_ec2_availability_zone_group": True, ### advanced resource not normally used
    "aws_ec2_managed_prefix_list_entry": True, ### normally use aws_ec2_managed_prefix_list
    "aws_fsx_data_repository_association": True, ### an association
    "aws_iam_account_password_policy": True, ### probably don't want to do in Terraform 
    "aws_imagebuilder_image": True, ### Problems importing with arn
    "aws_lightsail_distribution": True, ### us-east only  InvalidInputException
    "aws_lambda_layer_version_permission": True, ### import errors
    "aws_route": True, ### aws_route_table instead
    "aws_vpc_security_group_egress_rule": True, ### aws_security_group_rule
    "aws_vpc_security_group_ingress_rule": True, ### aws_security_group_rule
    "aws_volume_attachment": True, ### complex needed at all ?
    "aws_spot_datafeed_subscription": True, ### doesn't work
    "aws_ec2_transit_gateway_peering_attachment_accepter": True, ### unsure how to handle
    "aws_ec2_transit_gateway_vpc_attachment_accepter": True,  ### unsure how to handle
    "aws_network_interface_attachment": True, ### problematic
    "aws_network_interface_sg_attachment": True, ### problematic
    "aws_network_acl_association": True, ### problematic
    "aws_iam_access_key": True, ### probably should not import
    "aws_cleanrooms_collaboration": True, ### permission complexities
    "aws_backup_framework": True, ### complex config blocks
    "aws_config_conformance_pack": True, ### assume pre-defined by AWS
    "aws_codebuild_source_credential": True, ### questionble if we shpould get this or not
    "aws_default_network_acl": True, ### don't get default acl
    "aws_ec2_client_vpn_network_association": True, ### an association
    "aws_autoscaling_group_tag": True, ### don't think this is needed
    "aws_neptune_cluster_endpoint": True, # issues with import identifier
    "aws_rds_cluster_endpoint": True, # issues with import identifier
    "aws_rds_cluster_activity_stream": True, # issues with import identifier
    "aws_ebs_default_kms_key": True, # do we need to import ?
    "aws_rds_custom_db_engine_version": True, # import crashed provider
    "aws_glue_catalog_table": True,   # Error: setting storage_descriptor: Invalid address to set: []string{"storage_descriptor", "0", "additional_locations"}
    "aws_glue_partition": True # as child to glue table
} 