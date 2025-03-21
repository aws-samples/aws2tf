notimplemented = {
    "aws_network_acl_rule": True, ### ? worth doing
    "aws_auditmanager_account_registration": True,  ### TODO
    "aws_cognito_user_pool_domain": True,  ### TODO  
    "aws_datasync_location_s3": True,  ### TODO
    "aws_dax_cluster": True,  ### TODO
    "aws_inspector_assessment_target": True,  ### TODO
    "aws_iot_thing_group": True,  ### TODO
    "aws_lightsail_database": True,  ### TODO
    "aws_macie2_classification_job": True,  ### TODO
    "aws_memorydb_cluster": True,   ### TODO
    "aws_mskconnect_connector": True,  ### TODO
    "aws_networkfirewall_resource_policy": True, ### TODO
    "aws_opensearch_inbound_connection_accepter": True,  ### TODO
    "aws_redshiftserverless_resource_policy": True,  ### TODO
    "aws_s3_directory_bucket": True, ### TODO
    "aws_sagemaker_feature_group": True,  ### TODO
    "aws_sagemaker_pipeline": True,  ### TODO
    "aws_sagemaker_servicecatalog_portfolio_status": True, ### TODO
    "aws_securitylake_data_lake": True,  ### TODO
    "aws_auditmanager_assessment": True,   ### TODO
    "aws_ce_cost_allocation_tag": True, ### TODO
    "aws_ce_cost_allocation_tag": True, ### TODO
    "aws_cloudformation_stack": True, #### ? not handled well in Terraform 
    #
    # Many of these need to be done.
    #

    #
    "aws_apprunner_observability_configuration": True,
    #
    "aws_appstream_directory_config": True,
    "aws_appstream_fleet_stack_association": True,
    "aws_appstream_stack": True,
    "aws_appstream_user_stack_association": True,
    "aws_appsync_api_cache": True,
    "aws_appsync_domain_name_api_association": True,
    "aws_appsync_graphql_api": True,
    #"aws_athena_data_catalog": True,
    #
    "aws_auditmanager_assessment_delegation": True,
    "aws_auditmanager_framework": True,
    "aws_auditmanager_framework_share": True,
    "aws_auditmanager_organization_admin_account_registration": True,
    #
    "aws_backup_global_settings": True,
    "aws_budgets_budget": True,
    "aws_budgets_budget_action": True,
    #
    "aws_ce_anomaly_monitor": True,
    "aws_ce_anomaly_subscription": True,
    "aws_ce_cost_category": True,
    #
    "aws_chime_voice_connector_logging": True,
    "aws_chime_voice_connector_origination": True,
    "aws_chime_voice_connector_streaming": True,
    "aws_chime_voice_connector_termination": True,
    "aws_chimesdkmediapipelines_media_insights_pipeline_configuration": True,
    "aws_chimesdkvoice_global_settings": True,
    #
    "aws_cloudformation_stack_set_instance": True,
    "aws_cloudfront_monitoring_subscription": True,
    #
    "aws_cloudsearch_domain": True,
    "aws_cloudsearch_domain_service_access_policy": True,
    "aws_cloudwatch_composite_alarm": True,
    "aws_cloudwatch_dashboard": True,
    "aws_cloudwatch_event_api_destination": True,
    "aws_cloudwatch_event_archive": True,
    "aws_cloudwatch_event_bus_policy": True,
    "aws_cloudwatch_event_connection": True,
    "aws_cloudwatch_event_endpoint": True,
    "aws_cloudwatch_event_permission": True,
    #
    "aws_cloudwatch_log_data_protection_policy": True,
    "aws_cloudwatch_log_destination_policy": True,
    "aws_cloudwatch_log_metric_filter": True,
    "aws_cloudwatch_log_resource_policy": True,
    "aws_cloudwatch_log_subscription_filter": True,
    #
    "aws_codeartifact_domain_permissions_policy": True,
    "aws_codeartifact_repository_permissions_policy": True,
    "aws_codebuild_report_group": True,
    "aws_codebuild_resource_policy": True,
    "aws_codebuild_webhook": True,
    "aws_codecommit_approval_rule_template_association": True,
    "aws_codedeploy_app": True,
    "aws_codedeploy_deployment_config": True,
    #
    "aws_codepipeline_custom_action_type": True,
    "aws_codepipeline_webhook": True,
    #
    "aws_cognito_identity_pool_provider_principal_tag": True,
    "aws_cognito_risk_configuration": True,

    "aws_cognito_user_pool_ui_customization": True,
    #
    "aws_comprehend_document_classifier": True,
    "aws_comprehend_entity_recognizer": True,
    #
    "aws_connect_user_hierarchy_group": True,
    "aws_connect_user_hierarchy_structure": True,
    "aws_connect_contact_flow_module": True,
    #
    "aws_controltower_control": True,
    #
    "aws_cur_report_definition": True,
    "aws_dataexchange_revision": True,
    "aws_datapipeline_pipeline": True,
    "aws_datapipeline_pipeline_definition": True,
    #
    "aws_datasync_location_azure_blob": True,
    "aws_datasync_location_efs": True,
    "aws_datasync_location_fsx_lustre_file_system": True,
    "aws_datasync_location_fsx_ontap_file_system": True,
    "aws_datasync_location_fsx_openzfs_file_system": True,
    "aws_datasync_location_fsx_windows_file_system": True,
    "aws_datasync_location_hdfs": True,
    "aws_datasync_location_nfs": True,
    "aws_datasync_location_object_storage": True,
    "aws_datasync_location_smb": True,

    "aws_dax_parameter_group": True,
    "aws_dax_subnet_group": True,
    #
    "aws_db_proxy_default_target_group": True,
    "aws_default_vpc_dhcp_options": True,
    #
    "aws_detective_invitation_accepter": True,
    "aws_detective_organization_configuration": True,
    #
    "aws_devicefarm_device_pool": True,
	"aws_devicefarm_instance_profile": True,
	"aws_devicefarm_network_profile": True,
	"aws_devicefarm_project": True,
	"aws_devicefarm_test_grid_project": True,
	"aws_devicefarm_upload": True,
    #
    "aws_directory_service_conditional_forwarder": True,
    "aws_directory_service_radius_settings": True,
    "aws_directory_service_region": True,
    "aws_directory_service_shared_directory": True,
    "aws_directory_service_trust": True,
    #
    "aws_dlm_lifecycle_policy": True,
    "aws_dms_s3_endpoint": True,
    "aws_docdbelastic_cluster": True,
    #
    "aws_dx_gateway": True,
    "aws_dx_gateway_association": True,
    "aws_dx_gateway_association_proposal": True,
    "aws_dx_hosted_private_virtual_interface": True,
    "aws_dx_hosted_private_virtual_interface_accepter": True,
    "aws_dx_hosted_public_virtual_interface": True,
    "aws_dx_hosted_public_virtual_interface_accepter": True,
    "aws_dx_hosted_transit_virtual_interface": True,
    "aws_dx_hosted_transit_virtual_interface_accepter": True,
    "aws_dx_private_virtual_interface": True,
    "aws_dx_public_virtual_interface": True,
    "aws_dx_transit_virtual_interface": True,
    #
    "aws_dynamodb_global_table": True,
    "aws_ec2_local_gateway_route": True,
    "aws_ec2_subnet_cidr_reservation": True,
    #
    "aws_elasticache_user_group_association": True,
    "aws_elastictranscoder_preset": True,
    #
    "aws_emr_studio": True,
    "aws_emr_studio_session_mapping": True,
    "aws_emrcontainers_job_template": True,
    "aws_emrcontainers_virtual_cluster": True,
    "aws_emrserverless_application": True,
    #
    "aws_evidently_project": True,
    "aws_evidently_segment": True,
    #
    "aws_finspace_kx_cluster": True,
    "aws_finspace_kx_database": True,
    "aws_finspace_kx_dataview": True,
    "aws_finspace_kx_environment": True,
    "aws_finspace_kx_scaling_group": True,
    "aws_finspace_kx_user": True,
    "aws_finspace_kx_volume": True,
    #
    "aws_fms_admin_account": True,
    "aws_fms_policy": True,
    #
    "aws_gamelift_fleet": True,
    "aws_gamelift_game_session_queue": True,
    "aws_glacier_vault_lock": True,
    #
    "aws_glue_partition_index": True,
    "aws_glue_resource_policy": True,
    "aws_glue_user_defined_function": True,
    #
    "aws_guardduty_invite_accepter": True,
    "aws_guardduty_organization_configuration": True,
    #
    "aws_inspector2_delegated_admin_account": True,
    "aws_inspector2_member_association": True,
    #
    "aws_inspector_assessment_template": True,
    "aws_internet_gateway_attachment": True,
    #
    "aws_iot_authorizer": True,
    "aws_iot_billing_group": True,
    "aws_iot_domain_configuration": True,
    "aws_iot_event_configurations": True,
    "aws_iot_provisioning_template": True,
    "aws_iot_role_alias": True,
    #

    "aws_iot_thing_group_membership": True,
    "aws_iot_thing_type": True,
    "aws_iot_topic_rule_destination": True,
    #
    "aws_ivs_channel": True,
    "aws_ivs_playback_key_pair": True,
    "aws_ivs_recording_configuration": True,
    "aws_ivschat_logging_configuration": True,
    "aws_ivschat_room": True,
    #
    "aws_keyspaces_keyspace": True,
    #
    "aws_kinesis_video_stream": True,
    #
    "aws_kms_external_key": True,
    "aws_kms_replica_external_key": True,
    "aws_kms_replica_key": True,
    #
    "aws_licensemanager_association": True,
    "aws_licensemanager_grant": True,
    "aws_licensemanager_grant_accepter": True,
    #
    "aws_lightsail_bucket_resource_access": True,
    "aws_lightsail_disk": True,
    "aws_lightsail_disk_attachment": True,
    "aws_lightsail_domain_entry": True,
    "aws_lightsail_instance": True,
    "aws_lightsail_lb": True,
    "aws_lightsail_lb_attachment": True,
    "aws_lightsail_lb_certificate": True,
    "aws_lightsail_lb_certificate_attachment": True,
    "aws_lightsail_lb_https_redirection_policy": True,
    "aws_lightsail_lb_stickiness_policy": True,
    #
    "aws_location_geofence_collection": True,
    "aws_location_map": True,
    "aws_location_place_index": True,
    "aws_location_route_calculator": True,
    "aws_location_tracker": True,
    "aws_location_tracker_association": True,
    #
    "aws_macie2_account": True,
    "aws_macie2_classification_export_configuration": True,
    "aws_macie2_custom_data_identifier": True,
    "aws_macie2_findings_filter": True,
    "aws_macie2_invitation_accepter": True,
    "aws_macie2_member": True,
    "aws_macie2_organization_admin_account": True,
    #
    "aws_media_store_container_policy": True,
    #
    "aws_memorydb_acl": True,
    "aws_memorydb_parameter_group": True,
    "aws_memorydb_snapshot": True,
    "aws_memorydb_subnet_group": True,
    "aws_memorydb_user": True,
    #
    "aws_mskconnect_custom_plugin": True,
    "aws_mskconnect_worker_configuration": True,
    #
    "aws_neptune_cluster_instance": True,
    "aws_neptune_event_subscription": True,
    "aws_networkfirewall_logging_configuration": True,
    #
    "aws_networkmanager_connect_attachment": True,
    "aws_networkmanager_connection": True,
    "aws_networkmanager_core_network_policy_attachment": True,
    "aws_networkmanager_customer_gateway_association": True,
    #"aws_networkmanager_device": True,
    #"aws_networkmanager_global_network": True,
    "aws_networkmanager_link": True,
    "aws_networkmanager_link_association": True,
    #"aws_networkmanager_site": True,
    "aws_networkmanager_site_to_site_vpn_attachment": True,
    "aws_networkmanager_transit_gateway_connect_peer_association": True,
    "aws_networkmanager_transit_gateway_peering": True,
    #"aws_networkmanager_transit_gateway_registration": True,
    "aws_networkmanager_transit_gateway_route_table_attachment": True,
    "aws_networkmanager_vpc_attachment": True,
    #
    "aws_oam_link": True,
    "aws_oam_sink": True,
    "aws_oam_sink_policy": True,
    #
    "aws_opensearch_outbound_connection": True,
    "aws_opensearch_package": True,
    #
    "aws_opensearchserverless_access_policy": True,
    "aws_opensearchserverless_collection": True,
    "aws_opensearchserverless_lifecycle_policy": True,
    "aws_opensearchserverless_security_config": True,
    "aws_opensearchserverless_security_policy": True,
    #
    "aws_opsworks_application": True,
    "aws_opsworks_custom_layer": True,
    "aws_opsworks_instance": True,
    "aws_opsworks_php_app_layer": True,
    "aws_opsworks_stack": True,
    "aws_opsworks_static_web_layer": True,
    #
    "aws_pinpoint_adm_channel": True,
    "aws_pinpoint_apns_channel": True,
    "aws_pinpoint_apns_sandbox_channel": True,
    "aws_pinpoint_apns_voip_channel": True,
    "aws_pinpoint_apns_voip_sandbox_channel": True,
    "aws_pinpoint_app": True,
    "aws_pinpoint_baidu_channel": True,
    "aws_pinpoint_email_channel": True,
    "aws_pinpoint_event_stream": True,
    "aws_pinpoint_gcm_channel": True,
    "aws_pinpoint_sms_channel": True,
    #
    "aws_quicksight_folder_membership": True,
    #
    "aws_ram_resource_share_accepter": True,
    "aws_ram_sharing_with_organization": True,
    #
    "aws_rbin_rule": True,
    #
    "aws_redshiftserverless_endpoint_access": True,
    "aws_redshiftserverless_snapshot": True,
    "aws_redshiftserverless_usage_limit": True,
    "aws_resourceexplorer2_index": True,

    "aws_rolesanywhere_profile": True,
    "aws_rolesanywhere_trust_anchor": True,
    #
    "aws_route53_resolver_config": True,
    "aws_route53_resolver_dnssec_config": True,
    "aws_route53_resolver_endpoint": True,
    "aws_route53_resolver_firewall_config": True,
    "aws_route53_resolver_firewall_domain_list": True,
    "aws_route53_resolver_firewall_rule": True,
    "aws_route53_resolver_firewall_rule_group": True,
    "aws_route53_resolver_query_log_config": True,
    "aws_route53_resolver_query_log_config_association": True,
    "aws_route53_resolver_rule": True,
    "aws_route53_resolver_rule_association": True,
    #
    "aws_rum_app_monitor": True,
    "aws_rum_metrics_destination": True,
    #
    "aws_s3_bucket_cors_configuration": True,
    "aws_s3_bucket_server_side_encryption_configuration": True,

    "aws_s3control_bucket": True,
    #
    "aws_sagemaker_code_repository": True,
    "aws_sagemaker_data_quality_job_definition": True,
    "aws_sagemaker_device": True,  
    "aws_sagemaker_device_fleet": True,
    "aws_sagemaker_endpoint_configuration": True,

    "aws_sagemaker_flow_definition": True,
    "aws_sagemaker_human_task_ui": True,
    "aws_sagemaker_model_package_group": True,
    "aws_sagemaker_monitoring_schedule": True,
    #
    "aws_schemas_registry_policy": True,
    #
    "aws_securityhub_finding_aggregator": True,
    "aws_securityhub_insight": True,
    "aws_securityhub_invite_accepter": True,
    "aws_securityhub_member": True,
    "aws_securityhub_organization_admin_account": True,
    "aws_securityhub_product_subscription": True,
    "aws_securityhub_standards_subscription": True,
    #
    "aws_servicecatalog_budget_resource_association": True,
    "aws_servicecatalog_portfolio_share": True,
    "aws_servicecatalog_provisioned_product": True,
    "aws_servicecatalog_tag_option": True,
    "aws_servicecatalog_tag_option_resource_association": True,
    "aws_servicequotas_template": True,
    "aws_servicequotas_template_association": True,
    #
    "aws_ses_configuration_set": True,
    "aws_ses_domain_dkim": True,
    "aws_ses_domain_identity": True,
    "aws_ses_domain_mail_from": True,
    "aws_ses_email_identity": True,
    "aws_ses_event_destination": True,
    "aws_ses_identity_notification_topic": True,
    "aws_ses_identity_policy": True,
    "aws_ses_receipt_filter": True,
    "aws_ses_template": True,
    #
    "aws_sesv2_account_vdm_attributes": True,
    "aws_sesv2_configuration_set": True,
    "aws_sesv2_configuration_set_event_destination": True,
    "aws_sesv2_contact_list": True,
    "aws_sesv2_dedicated_ip_assignment": True,
    "aws_sesv2_dedicated_ip_pool": True,
    "aws_sesv2_email_identity": True,
    "aws_sesv2_email_identity_feedback_attributes": True,
    "aws_sesv2_email_identity_mail_from_attributes": True,
    #
    "aws_shield_protection": True,
    "aws_shield_protection_health_check_association": True,
    #
    "aws_signer_signing_job": True,
    "aws_signer_signing_profile": True,
    "aws_signer_signing_profile_permission": True,
    "aws_simpledb_domain": True,
    #
    "aws_ssm_resource_data_sync": True,
    #
    "aws_ssoadmin_application_assignment_configuration": True,
    "aws_ssoadmin_customer_managed_policy_attachment": True,
    "aws_ssoadmin_instance_access_control_attributes": True,
    "aws_ssoadmin_permissions_boundary_attachment": True,
    #
    "aws_storagegateway_gateway": True,
    "aws_storagegateway_tape_pool": True,
    #
    "aws_synthetics_canary": True,
    "aws_synthetics_group": True,
    "aws_synthetics_group_association": True,
    #
    "aws_transfer_ssh_key": True,
    "aws_transfer_tag": True,
# apigateway stuff
	"aws_api_gateway_api_key": True,
	"aws_api_gateway_base_path_mapping": True,
	"aws_api_gateway_client_certificate": True,
	"aws_api_gateway_documentation_part": True,
	"aws_api_gateway_documentation_version": True,
	"aws_api_gateway_domain_name": True,
	"aws_api_gateway_gateway_response": True,
	"aws_api_gateway_integration": True,
	"aws_api_gateway_integration_response": True,
	"aws_api_gateway_method_response": True,
	"aws_api_gateway_method_settings": True,
	"aws_api_gateway_model": True,
	"aws_api_gateway_request_validator": True,
	"aws_api_gateway_rest_api_policy": True,
	"aws_api_gateway_usage_plan": True,
	"aws_api_gateway_usage_plan_key": True,
	"aws_api_gateway_vpc_link": True,
### old WAF
	"aws_waf_byte_match_set": True,
	"aws_waf_geo_match_set": True,
	"aws_waf_ipset": True,
	"aws_waf_rate_based_rule": True,
	"aws_waf_regex_match_set": True,
	"aws_waf_regex_pattern_set": True,
	"aws_waf_rule": True,
	"aws_waf_rule_group": True,
	"aws_waf_size_constraint_set": True,
	"aws_waf_sql_injection_match_set": True,
	"aws_waf_xss_match_set": True,
	"aws_wafregional_byte_match_set": True,
	"aws_wafregional_geo_match_set": True,
	"aws_wafregional_ipset": True,
	"aws_wafregional_rate_based_rule": True,
	"aws_wafregional_regex_match_set": True,
	"aws_wafregional_regex_pattern_set": True,
	"aws_wafregional_rule": True,
	"aws_wafregional_rule_group": True,
	"aws_wafregional_size_constraint_set": True,
	"aws_wafregional_sql_injection_match_set": True,
	"aws_wafregional_web_acl": True,
	"aws_wafregional_web_acl_association": True,
	"aws_wafregional_xss_match_set": True,
    #
    "aws_auditmanager_account_registration": True,
	"aws_auditmanager_assessment_delegation": True,
	"aws_auditmanager_assessment_report": True,
	"aws_auditmanager_control": True,
	"aws_auditmanager_framework": True,
	"aws_auditmanager_framework_share": True,
	"aws_auditmanager_organization_admin_account_registration": True,
    #
    "aws_worklink_fleet": True, ### region  
    "aws_timestreamwrite_database": True, ### region
    "aws_timestreamwrite_table": True, ### region

}
