notimplemented = {
    #
    # ========================================
    # DEPRECATED/LEGACY SERVICES
    # These services have been deprecated, discontinued, or replaced
    # Testing these resources is not recommended
    # ========================================
    #
	"aws_waf_byte_match_set": True,  ### Deprecated - use WAFv2
	"aws_waf_geo_match_set": True,  ### Deprecated - use WAFv2
	"aws_waf_ipset": True,  ### Deprecated - use WAFv2
	"aws_waf_rate_based_rule": True,  ### Deprecated - use WAFv2
	"aws_waf_regex_match_set": True,  ### Deprecated - use WAFv2
	"aws_waf_regex_pattern_set": True,  ### Deprecated - use WAFv2
	"aws_waf_rule": True,  ### Deprecated - use WAFv2
	"aws_waf_rule_group": True,  ### Deprecated - use WAFv2
	"aws_waf_size_constraint_set": True,  ### Deprecated - use WAFv2
	"aws_waf_sql_injection_match_set": True,  ### Deprecated - use WAFv2
	"aws_waf_xss_match_set": True,  ### Deprecated - use WAFv2
	"aws_wafregional_byte_match_set": True,  ### Deprecated - use WAFv2
	"aws_wafregional_geo_match_set": True,  ### Deprecated - use WAFv2
	"aws_wafregional_ipset": True,  ### Deprecated - use WAFv2
	"aws_wafregional_rate_based_rule": True,  ### Deprecated - use WAFv2
	"aws_wafregional_regex_match_set": True,  ### Deprecated - use WAFv2
	"aws_wafregional_regex_pattern_set": True,  ### Deprecated - use WAFv2
	"aws_wafregional_rule": True,  ### Deprecated - use WAFv2
	"aws_wafregional_rule_group": True,  ### Deprecated - use WAFv2
	"aws_wafregional_size_constraint_set": True,  ### Deprecated - use WAFv2
	"aws_wafregional_sql_injection_match_set": True,  ### Deprecated - use WAFv2
	"aws_wafregional_web_acl": True,  ### Deprecated - use WAFv2
	"aws_wafregional_web_acl_association": True,  ### Deprecated - use WAFv2
	"aws_wafregional_xss_match_set": True,  ### Deprecated - use WAFv2
    "aws_cloudsearch_domain": True,  ### Legacy - use OpenSearch
    "aws_cloudsearch_domain_service_access_policy": True,  ### Legacy - use OpenSearch
    "aws_datapipeline_pipeline": True,  ### Deprecated - use Glue/Step Functions
    "aws_datapipeline_pipeline_definition": True,  ### Deprecated - use Glue/Step Functions
    "aws_elastictranscoder_preset": True,  ### Deprecated - use MediaConvert
    "aws_glacier_vault_lock": True,  ### Rebranded as S3 Glacier
    "aws_inspector2_delegated_admin_account": True,  ### Deprecated - use Inspector v2
    "aws_inspector2_filter": True,  ### Deprecated - use Inspector v2
    "aws_inspector2_member_association": True,  ### Deprecated - use Inspector v2
    "aws_inspector_assessment_target": True,  ### Deprecated - use Inspector v2
    "aws_inspector_assessment_template": True,  ### Deprecated - use Inspector v2
    "aws_opsworks_application": True,  ### Being phased out
    "aws_opsworks_custom_layer": True,  ### Being phased out
    "aws_opsworks_instance": True,  ### Being phased out
    "aws_opsworks_php_app_layer": True,  ### Being phased out
    "aws_opsworks_stack": True,  ### Being phased out
    "aws_opsworks_static_web_layer": True,  ### Being phased out
    "aws_simpledb_domain": True,  ### Legacy - use DynamoDB
    "aws_wafv2_api_key": True,  ### Deprecated - use WAFv2
    "aws_wafv2_web_acl_rule_group_association": True,  ### Deprecated - use WAFv2
    "aws_worklink_fleet": True, ### Service discontinued (Dec 2021)
    #
    # ========================================
    # ACTIVE SERVICES
    # ========================================
    #
    "aws_network_acl_rule": True, ### ? worth doing
    "aws_auditmanager_account_registration": True,  ### TODO
    "aws_cognito_user_pool_domain": True,  ### TODO  
    "aws_datasync_location_s3": True,  ### TODO
    "aws_dax_cluster": True,  ### TODO

    "aws_iot_thing_group": True,  ### TODO
    "aws_lightsail_database": True,  ### TODO
    "aws_macie2_classification_job": True,  ### TODO
    "aws_memorydb_cluster": True,   ### TODO
    "aws_mskconnect_connector": True,  ### TODO
    "aws_networkfirewall_resource_policy": True, ### TODO
    "aws_opensearch_inbound_connection_accepter": True,  ### TODO
    "aws_redshiftserverless_resource_policy": True,  ### Requires snapshot (which requires namespace/workgroup) - complex and expensive
    "aws_s3_directory_bucket": True, ### TODO
    "aws_sagemaker_feature_group": True,  ### TODO
    #"aws_sagemaker_pipeline": True,  ### TODO
    #"aws_sagemaker_servicecatalog_portfolio_status": True, ### TODO
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
    "aws_appstream_directory_config": True,  ### Requires Active Directory setup
    "aws_appstream_fleet_stack_association": True,  ### Composite ID format
    #"aws_appstream_stack": True,
    "aws_appstream_user_stack_association": True,  ### Composite ID format
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
    #"aws_cloudwatch_composite_alarm": True,
    #"aws_cloudwatch_dashboard": True,
    #"aws_cloudwatch_event_api_destination": True,
    #"aws_cloudwatch_event_archive": True,
    #"aws_cloudwatch_event_bus_policy": True,
    #"aws_cloudwatch_event_connection": True,
    "aws_cloudwatch_event_endpoint": True,  # Requires multi-region setup - too complex
    "aws_cloudwatch_event_permission": True,
    #
    #"aws_cloudwatch_log_data_protection_policy": True,
    #"aws_cloudwatch_log_destination_policy": True,
    "aws_cloudwatch_log_metric_filter": True,
    #"aws_cloudwatch_log_resource_policy": True,
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
    "aws_ec2_local_gateway_route": True,  ### Requires AWS Outposts hardware + Composite ID: lgw-rtb-id_cidr
    #"aws_ec2_subnet_cidr_reservation": True,  ### Composite ID: subnet-id:reservation-id
    #
    "aws_elasticache_user_group_association": True,
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
    #
    "aws_glue_partition_index": True,
    "aws_glue_resource_policy": True,
    "aws_glue_user_defined_function": True,
    #
    "aws_guardduty_invite_accepter": True,
    "aws_guardduty_organization_configuration": True,
    #
    #
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
    #"aws_opensearchserverless_access_policy": True,
    #"aws_opensearchserverless_collection": True,
    #"aws_opensearchserverless_lifecycle_policy": True,
    "aws_opensearchserverless_security_config": True,  ### Requires valid SAML IdP metadata with certificates
    #"aws_opensearchserverless_security_policy": True,
    #
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
    #"aws_redshiftserverless_endpoint_access": True,  ### Requires workgroup, VPC, subnets - complex and expensive
    #"aws_redshiftserverless_snapshot": True,  ### Requires namespace and workgroup - complex and expensive
    #"aws_redshiftserverless_usage_limit": True,  ### Requires workgroup - complex and expensive
    "aws_resourceexplorer2_index": True,

    "aws_rolesanywhere_profile": True,
    "aws_rolesanywhere_trust_anchor": True,
    #
    #"aws_route53_resolver_config": True,
    #"aws_route53_resolver_dnssec_config": True,
    #"aws_route53_resolver_endpoint": True,
    #"aws_route53_resolver_firewall_config": True,
    #"aws_route53_resolver_firewall_domain_list": True,
    #"aws_route53_resolver_firewall_rule": True,  ### Composite ID format: rule_group_id:domain_list_id
    #"aws_route53_resolver_firewall_rule_group": True,
    #"aws_route53_resolver_query_log_config": True,
    #"aws_route53_resolver_query_log_config_association": True,
    #"aws_route53_resolver_rule": True,
    #"aws_route53_resolver_rule_association": True,
    #
    "aws_rum_app_monitor": True,
    "aws_rum_metrics_destination": True,
    #
    "aws_s3_bucket_cors_configuration": True,
    "aws_s3_bucket_server_side_encryption_configuration": True,

    "aws_s3control_bucket": True,
    #
    #"aws_sagemaker_code_repository": True,
    "aws_sagemaker_data_quality_job_definition": True,  ### Requires S3 buckets, IAM roles, data quality baselines - complex setup
    "aws_sagemaker_device": True,  ### Composite ID: fleet-name/device-name + requires IoT device fleet
    "aws_sagemaker_device_fleet": True,  ### Creation timeout - takes 10+ minutes to create IoT infrastructure
    "aws_sagemaker_endpoint_configuration": True,  ### Requires ML models - complex setup

    #"aws_sagemaker_flow_definition": True,  ### Requires S3 buckets, IAM roles, human task UI - complex setup
    #"aws_sagemaker_human_task_ui": True,  ### Requires HTML template for human review interface
    #"aws_sagemaker_model_package_group": True,
    #"aws_sagemaker_monitoring_schedule": True,  ### Requires endpoint, baseline, S3 buckets - complex setup
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
    "aws_signer_signing_job": True,  ### Requires complex handler - destination must be reconstructed from signedObject
#    "aws_signer_signing_profile": True,
#    "aws_signer_signing_profile_permission": True,
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
#	"aws_api_gateway_api_key": True,
#	"aws_api_gateway_base_path_mapping": True,
#	"aws_api_gateway_client_certificate": True,
#	"aws_api_gateway_documentation_part": True,
	#"aws_api_gateway_documentation_version": True,
	"aws_api_gateway_domain_name": True,  ### Requires ACM certificate and domain ownership
	#"aws_api_gateway_gateway_response": True,
	"aws_api_gateway_integration": True,  ### Composite ID: REST-API-ID/RESOURCE-ID/HTTP-METHOD
	"aws_api_gateway_integration_response": True,  ### Composite ID: REST-API-ID/RESOURCE-ID/HTTP-METHOD/STATUS-CODE
	"aws_api_gateway_method_response": True,  ### Composite ID: REST-API-ID/RESOURCE-ID/HTTP-METHOD/STATUS-CODE
	#"aws_api_gateway_method_settings": True,
#	"aws_api_gateway_model": True,
#	"aws_api_gateway_request_validator": True,
	#"aws_api_gateway_rest_api_policy": True,
	#"aws_api_gateway_usage_plan": True,
	#"aws_api_gateway_usage_plan_key": True,
	#"aws_api_gateway_vpc_link": True,
### old WAF
    #
    "aws_auditmanager_account_registration": True,
	"aws_auditmanager_assessment_delegation": True,
	"aws_auditmanager_assessment_report": True,
	"aws_auditmanager_control": True,
	"aws_auditmanager_framework": True,
	"aws_auditmanager_framework_share": True,
	"aws_auditmanager_organization_admin_account_registration": True,
    #

    "aws_timestreamwrite_database": True, ### region
    "aws_timestreamwrite_table": True, ### region
    #
    # New resources added from aws_dict_extended.py
    #
    #"aws_bedrockagentcore_agent_runtime": True,  ### TODO 6.27.0 - Requires container image in ECR - too complex for automated testing
    "aws_bedrockagentcore_agent_runtime_endpoint": True,  ### TODO 6.27.0 - Composite ID
    "aws_bedrockagentcore_api_key_credential_provider": True,  ### TODO 6.27.0 - API key is sensitive and not returned by API - cannot import
    #"aws_bedrockagentcore_browser": True,  ### TODO 6.27.0 - Requires complex setup - too complex for automated testing
    #"aws_bedrockagentcore_code_interpreter": True,  ### TODO 6.27.0 - Requires complex setup - too complex for automated testing
    #"aws_bedrockagentcore_gateway": True,  ### TODO 6.27.0 - Requires complex setup - too complex for automated testing
    "aws_bedrockagentcore_gateway_target": True,  ### TODO 6.27.0 - Composite ID
    #"aws_bedrockagentcore_memory": True,  ### TODO 6.27.0 - Requires complex setup - too complex for automated testing
    "aws_bedrockagentcore_memory_strategy": True,  ### TODO 6.27.0 - API method missing (list_memory_strategies)
    "aws_bedrockagentcore_oauth2_credential_provider": True,  ### TODO 6.27.0 - Requires complex setup - too complex for automated testing
    #"aws_bedrockagentcore_token_vault_cmk": True,  ### TODO 6.27.0 - Requires complex setup - too complex for automated testing
    #"aws_bedrockagentcore_workload_identity": True,  ### TODO 6.27.0 - Requires complex setup - too complex for automated testing
    "aws_cloudwatch_contributor_managed_insight_rule": True,  ### TODO 6.27.0 - Composite ID format
    "aws_controltower_baseline": True,  ### TODO 6.27.0
    "aws_dataexchange_event_action": True,  ### TODO 6.27.0
    "aws_dataexchange_revision_assets": True,  ### TODO 6.27.0
    "aws_devopsguru_event_sources_config": True,  ### TODO 6.27.0
    "aws_devopsguru_notification_channel": True,  ### TODO 6.27.0
    "aws_devopsguru_resource_collection": True,  ### TODO 6.27.0
    "aws_devopsguru_service_integration": True,  ### TODO 6.27.0
    "aws_directory_service_shared_directory_accepter": True,  ### TODO 6.27.0
    "aws_drs_replication_configuration_template": True,  ### TODO 6.27.0
    "aws_dsql_cluster": True,  ### TODO 6.27.0
    "aws_dsql_cluster_peering": True,  ### TODO 6.27.0
    "aws_dynamodb_table_export": True,  ### TODO 6.27.0
    #"aws_ec2_allowed_images_settings": True,  ### TODO 6.27.0
    #"aws_ec2_default_credit_specification": True,  ### TODO 6.27.0
    "aws_ec2_transit_gateway_default_route_table_association": True,  ### Cannot import - no import section in Terraform docs
    "aws_ec2_transit_gateway_default_route_table_propagation": True,  ### Cannot import - no import section in Terraform docs
    #"aws_ecr_account_setting": True,  ### TODO 6.27.0
    #"aws_ecr_repository_creation_template": True,  ### TODO 6.27.0
    #"aws_ecs_express_gateway_service": True,  ### TODO 6.27.0
    "aws_eks_capability": True,  ### TODO 6.27.0
    "aws_fis_target_account_configuration": True,  ### TODO 6.27.0
    "aws_fsx_s3_access_point_attachment": True,  ### TODO 6.27.0
    "aws_guardduty_member_detector_feature": True,  ### TODO 6.27.0
    "aws_iam_group_policies_exclusive": True,  ### TODO 6.27.0
    "aws_iam_group_policy_attachments_exclusive": True,  ### TODO 6.27.0
    "aws_iam_outbound_web_identity_federation": True,  ### TODO 6.27.0
    "aws_iam_role_policies_exclusive": True,  ### TODO 6.27.0
    "aws_iam_role_policy_attachments_exclusive": True,  ### TODO 6.27.0
    "aws_iam_user_policies_exclusive": True,  ### TODO 6.27.0
    "aws_iam_user_policy_attachments_exclusive": True,  ### TODO 6.27.0
    "aws_imagebuilder_lifecycle_policy": True,  ### TODO 6.27.0
    "aws_imagebuilder_workflow": True,  ### TODO 6.27.0

    "aws_invoicing_invoice_unit": True,  ### TODO 6.27.0
    "aws_kinesis_resource_policy": True,  ### TODO 6.27.0
    "aws_lakeformation_data_cells_filter": True,  ### TODO 6.27.0
    "aws_lakeformation_identity_center_configuration": True,  ### TODO 6.27.0
    "aws_lakeformation_lf_tag_expression": True,  ### TODO 6.27.0
    "aws_lakeformation_opt_in": True,  ### TODO 6.27.0
    "aws_lakeformation_resource_lf_tag": True,  ### TODO 6.27.0
#    "aws_lambda_function_recursion_config": True,  ### TODO 6.27.0
    "aws_lambda_runtime_management_config": True,  ### TODO 6.27.0
    "aws_m2_application": True,  ### TODO 6.27.0
    "aws_m2_deployment": True,  ### TODO 6.27.0
    "aws_m2_environment": True,  ### TODO 6.27.0
    "aws_macie2_organization_configuration": True,  ### TODO 6.27.0
    "aws_media_packagev2_channel_group": True,  ### TODO 6.27.0
    "aws_memorydb_multi_region_cluster": True,  ### TODO 6.27.0
    "aws_msk_single_scram_secret_association": True,  ### TODO 6.27.0
    "aws_nat_gateway_eip_association": True,  ### TODO 6.27.0
    "aws_neptunegraph_graph": True,  ### TODO 6.27.0
    "aws_network_interface_permission": True,  ### TODO 6.27.0
    "aws_networkfirewall_firewall_transit_gateway_attachment_accepter": True,  ### TODO 6.27.0
    "aws_networkfirewall_tls_inspection_configuration": True,  ### TODO 6.27.0
    "aws_networkfirewall_vpc_endpoint_association": True,  ### TODO 6.27.0
    "aws_networkflowmonitor_monitor": True,  ### TODO 6.27.0 - AWS API limitation - get_monitor does not return scopeArn
    #"aws_networkflowmonitor_scope": True,  ### TODO 6.27.0
    "aws_networkmanager_dx_gateway_attachment": True,  ### TODO 6.27.0
    "aws_networkmonitor_monitor": True,  ### TODO 6.27.0
    "aws_networkmonitor_probe": True,  ### TODO 6.27.0
    "aws_notifications_channel_association": True,  ### TODO 6.27.0
    "aws_notifications_event_rule": True,  ### TODO 6.27.0
    "aws_notifications_notification_configuration": True,  ### TODO 6.27.0
    "aws_notifications_notification_hub": True,  ### TODO 6.27.0
    "aws_notificationscontacts_email_contact": True,  ### TODO 6.27.0
    "aws_observabilityadmin_centralization_rule_for_organization": True,  ### TODO 6.27.0
    "aws_odb_cloud_autonomous_vm_cluster": True,  ### TODO 6.27.0
    "aws_odb_cloud_exadata_infrastructure": True,  ### TODO 6.27.0
    "aws_odb_cloud_vm_cluster": True,  ### TODO 6.27.0
    "aws_odb_network": True,  ### TODO 6.27.0
    "aws_odb_network_peering_connection": True,  ### TODO 6.27.0
    "aws_opensearch_authorize_vpc_endpoint_access": True,  ### TODO 6.27.0
    "aws_organizations_tag": True,  ### TODO 6.27.0
    "aws_osis_pipeline": True,  ### TODO 6.27.0
    "aws_paymentcryptography_key": True,  ### TODO 6.27.0
    "aws_paymentcryptography_key_alias": True,  ### TODO 6.27.0
    "aws_pinpoint_email_template": True,  ### TODO 6.27.0
    "aws_pinpointsmsvoicev2_configuration_set": True,  ### TODO 6.27.0
    "aws_pinpointsmsvoicev2_opt_out_list": True,  ### TODO 6.27.0
    "aws_pinpointsmsvoicev2_phone_number": True,  ### TODO 6.27.0
#    "aws_prometheus_query_logging_configuration": True,  ### TODO 6.27.0
#    "aws_prometheus_resource_policy": True,  ### TODO 6.27.0
    "aws_prometheus_scraper": True,  ### TODO 6.27.0
#    "aws_prometheus_workspace_configuration": True,  ### TODO 6.27.0
    "aws_qbusiness_application": True,  ### TODO 6.27.0
    "aws_quicksight_account_settings": True,  ### TODO 6.27.0
    "aws_quicksight_custom_permissions": True,  ### TODO 6.27.0
    "aws_quicksight_ip_restriction": True,  ### TODO 6.27.0
    "aws_quicksight_key_registration": True,  ### TODO 6.27.0
    "aws_quicksight_role_custom_permission": True,  ### TODO 6.27.0
    "aws_quicksight_role_membership": True,  ### TODO 6.27.0
    "aws_rds_instance_state": True,  ### TODO 6.27.0
    "aws_rds_shard_group": True,  ### TODO 6.27.0
    "aws_resiliencehub_resiliency_policy": True,  ### TODO 6.27.0
    "aws_s3control_directory_bucket_access_point_scope": True,  ### TODO 6.27.0
    #"aws_s3tables_table_bucket_replication": True,  ### TODO 6.27.0
    #"aws_s3tables_table_policy": True,  ### TODO 6.27.0
    #"aws_s3tables_table_replication": True,  ### TODO 6.27.0
    # "aws_s3vectors_index": True,  ### TODO 6.27.0 - Testing enabled
    # "aws_s3vectors_vector_bucket": True,  ### TODO 6.27.0 - Testing enabled
    # "aws_s3vectors_vector_bucket_policy": True,  ### TODO 6.27.0 - Testing enabled
    "aws_sagemaker_mlflow_tracking_server": True,  ### TODO 6.27.0
    "aws_securityhub_standards_control_association": True,  ### TODO 6.27.0
    "aws_securitylake_aws_log_source": True,  ### TODO 6.27.0 - Requires Security Lake enabled
    "aws_securitylake_custom_log_source": True,  ### TODO 6.27.0 - Requires Security Lake enabled
    "aws_securitylake_data_lake": True,  ### TODO 6.27.0 - Access Denied - requires account-level setup
    "aws_securitylake_subscriber": True,  ### TODO 6.27.0 - Requires Security Lake enabled
    "aws_securitylake_subscriber_notification": True,  ### TODO 6.27.0 - Requires Security Lake enabled
    "aws_servicecatalogappregistry_application": True,  ### TODO 6.27.0
    "aws_servicecatalogappregistry_attribute_group": True,  ### TODO 6.27.0
    "aws_servicecatalogappregistry_attribute_group_association": True,  ### TODO 6.27.0
    "aws_sesv2_account_suppression_attributes": True,  ### TODO 6.27.0
    "aws_sesv2_email_identity_policy": True,  ### TODO 6.27.0
    "aws_sesv2_tenant": True,  ### TODO 6.27.0
    "aws_shield_proactive_engagement": True,  ### TODO 6.27.0
    "aws_shield_subscription": True,  ### TODO 6.27.0
    "aws_ssmcontacts_rotation": True,  ### TODO 6.27.0
    "aws_ssmquicksetup_configuration_manager": True,  ### TODO 6.27.0
    "aws_ssoadmin_application_access_scope": True,  ### TODO 6.27.0
    "aws_timestreaminfluxdb_db_cluster": True,  ### TODO 6.27.0
    "aws_timestreaminfluxdb_db_instance": True,  ### TODO 6.27.0
    "aws_timestreamquery_scheduled_query": True,  ### TODO 6.27.0
    "aws_transfer_host_key": True,  ### TODO 6.27.0
    "aws_transfer_web_app": True,  ### TODO 6.27.0
    "aws_transfer_web_app_customization": True,  ### TODO 6.27.0
    "aws_verifiedpermissions_identity_source": True,  ### TODO 6.27.0
    "aws_verifiedpermissions_policy": True,  ### TODO 6.27.0
    "aws_verifiedpermissions_policy_store": True,  ### TODO 6.27.0
    "aws_verifiedpermissions_policy_template": True,  ### TODO 6.27.0
    "aws_verifiedpermissions_schema": True,  ### TODO 6.27.0
    #"aws_vpc_block_public_access_exclusion": True,  ### TODO 6.27.0
    #"aws_vpc_block_public_access_options": True,  ### TODO 6.27.0
    #"aws_vpc_encryption_control": True,  ### TODO 6.27.0
    #"aws_vpc_endpoint_private_dns": True,  ### TODO 6.27.0
    "aws_vpc_endpoint_service_private_dns_verification": True,  ### TODO 6.27.0
    #"aws_vpc_route_server": True,  ### TODO 6.27.0
    "aws_vpc_route_server_association": True,  ### TODO 6.27.0
    #"aws_vpc_route_server_endpoint": True,  ### TODO 6.27.0
    #"aws_vpc_route_server_peer": True,  ### TODO 6.27.0
    "aws_vpc_route_server_propagation": True,  ### TODO 6.27.0
    "aws_vpc_route_server_vpc_association": True,  ### TODO 6.27.0
    "aws_vpc_security_group_vpc_association": True,  ### TODO 6.27.0
    "aws_vpclattice_domain_verification": True,  ### TODO 6.27.0
    "aws_vpn_concentrator": True,  ### TODO 6.27.0


    #"aws_workspacesweb_browser_settings": True,  ### TODO 6.27.0
    "aws_workspacesweb_browser_settings_association": True,  ### TODO 6.27.0
    #"aws_workspacesweb_data_protection_settings": True,  ### TODO 6.27.0
    "aws_workspacesweb_data_protection_settings_association": True,  ### TODO 6.27.0
    #"aws_workspacesweb_identity_provider": True,  ### TODO 6.27.0
    #"aws_workspacesweb_ip_access_settings": True,  ### TODO 6.27.0
    "aws_workspacesweb_ip_access_settings_association": True,  ### TODO 6.27.0
    # "aws_workspacesweb_network_settings": True,  ### TODO 6.27.0
    "aws_workspacesweb_network_settings_association": True,  ### TODO 6.27.0
    # "aws_workspacesweb_portal": True,  ### TODO 6.27.0
    #"aws_workspacesweb_session_logger": True,  ### TODO 6.27.0
    "aws_workspacesweb_session_logger_association": True,  ### TODO 6.27.0
    #"aws_workspacesweb_trust_store": True,  ### TODO 6.27.0
    "aws_workspacesweb_trust_store_association": True,  ### TODO 6.27.0
    #"aws_workspacesweb_user_access_logging_settings": True,  ### TODO 6.27.0
    "aws_workspacesweb_user_access_logging_settings_association": True,  ### TODO 6.27.0
#    "aws_workspacesweb_user_settings": True,  ### TODO 6.27.0
}
