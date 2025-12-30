# AWS Terraform Resources NOT in aws_dict.py

This file lists Terraform AWS resources from the official provider documentation
that are NOT yet defined in `aws_dict.py`.

**Total Missing Resources:** 288
**Total Existing Resources:** 1317
**Total Master List Resources:** 1582
**Coverage:** 83.2%

---

## Summary by Service

| Service | Missing Resources |
|---------|------------------|
| account | 1 |
| alb | 1 |
| api | 2 |
| appconfig | 1 |
| appfabric | 5 |
| apprunner | 1 |
| appsync | 3 |
| athena | 1 |
| backup | 3 |
| bcmdataexports | 1 |
| bedrock | 4 |
| bedrockagent | 3 |
| bedrockagentcore | 12 |
| billing | 1 |
| chatbot | 2 |
| cleanrooms | 1 |
| cloudformation | 1 |
| cloudfront | 4 |
| cloudfrontkeyvaluestore | 2 |
| cloudtrail | 1 |
| cloudwatch | 10 |
| codebuild | 1 |
| codeconnections | 2 |
| cognito | 2 |
| computeoptimizer | 2 |
| config | 1 |
| connect | 1 |
| controltower | 2 |
| costoptimizationhub | 2 |
| dataexchange | 2 |
| default | 2 |
| devopsguru | 4 |
| directory | 1 |
| drs | 1 |
| dsql | 2 |
| dynamodb | 2 |
| ebs | 2 |
| ec2 | 10 |
| ecr | 2 |
| ecs | 1 |
| eip | 1 |
| eks | 1 |
| elasticache | 1 |
| elasticsearch | 1 |
| fis | 1 |
| fms | 1 |
| fsx | 1 |
| globalaccelerator | 1 |
| glue | 1 |
| grafana | 2 |
| guardduty | 2 |
| iam | 8 |
| imagebuilder | 2 |
| inspector2 | 1 |
| invoicing | 1 |
| kinesis | 1 |
| lakeformation | 5 |
| lambda | 3 |
| lexv2models | 3 |
| m2 | 3 |
| macie2 | 1 |
| media | 1 |
| memorydb | 1 |
| msk | 1 |
| nat | 1 |
| neptunegraph | 1 |
| network | 1 |
| networkfirewall | 3 |
| networkflowmonitor | 2 |
| networkmanager | 1 |
| networkmonitor | 2 |
| notifications | 4 |
| notificationscontacts | 1 |
| observabilityadmin | 1 |
| odb | 5 |
| opensearch | 1 |
| organizations | 1 |
| osis | 1 |
| paymentcryptography | 2 |
| pinpoint | 1 |
| pinpointsmsvoicev2 | 3 |
| prometheus | 4 |
| qbusiness | 1 |
| quicksight | 7 |
| rds | 5 |
| redshift | 5 |
| redshiftserverless | 1 |
| rekognition | 3 |
| resiliencehub | 1 |
| route53 | 2 |
| route53domains | 2 |
| route53profiles | 3 |
| s3 | 2 |
| s3control | 1 |
| s3tables | 4 |
| s3vectors | 3 |
| sagemaker | 2 |
| securityhub | 4 |
| securitylake | 4 |
| servicecatalogappregistry | 3 |
| sesv2 | 3 |
| shield | 2 |
| ssmcontacts | 1 |
| ssmquicksetup | 1 |
| ssoadmin | 1 |
| timestreaminfluxdb | 2 |
| timestreamquery | 1 |
| transfer | 3 |
| verifiedpermissions | 5 |
| vpc | 12 |
| vpclattice | 1 |
| vpn | 1 |
| wafv2 | 2 |
| workspacesweb | 18 |
| xray | 1 |

---

## All Missing Resources

These resources need to be added to `aws_dict.py` with:
- Terraform resource name
- Boto3 client name (clfn)
- Boto3 describe/list API method (descfn)
- Top-level key in API response (topkey)
- Resource identifier key (key)
- Filter ID (filterid)

| # | Terraform Resource | Service |
|---|-------------------|---------|
| 1 | `aws_account_region` | account |
| 2 | `aws_alb` | alb |
| 3 | `aws_api_gateway_domain_name_access_association` | api |
| 4 | `aws_api_gateway_rest_api_put` | api |
| 5 | `aws_appconfig_extension` | appconfig |
| 6 | `aws_appfabric_app_authorization` | appfabric |
| 7 | `aws_appfabric_app_authorization_connection` | appfabric |
| 8 | `aws_appfabric_app_bundle` | appfabric |
| 9 | `aws_appfabric_ingestion` | appfabric |
| 10 | `aws_appfabric_ingestion_destination` | appfabric |
| 11 | `aws_apprunner_deployment` | apprunner |
| 12 | `aws_appsync_api` | appsync |
| 13 | `aws_appsync_channel_namespace` | appsync |
| 14 | `aws_appsync_source_api_association` | appsync |
| 15 | `aws_athena_capacity_reservation` | athena |
| 16 | `aws_backup_logically_air_gapped_vault` | backup |
| 17 | `aws_backup_restore_testing_plan` | backup |
| 18 | `aws_backup_restore_testing_selection` | backup |
| 19 | `aws_bcmdataexports_export` | bcmdataexports |
| 20 | `aws_bedrock_custom_model` | bedrock |
| 21 | `aws_bedrock_guardrail_version` | bedrock |
| 22 | `aws_bedrock_inference_profile` | bedrock |
| 23 | `aws_bedrock_provisioned_model_throughput` | bedrock |
| 24 | `aws_bedrockagent_agent_collaborator` | bedrockagent |
| 25 | `aws_bedrockagent_flow` | bedrockagent |
| 26 | `aws_bedrockagent_prompt` | bedrockagent |
| 27 | `aws_bedrockagentcore_agent_runtime` | bedrockagentcore |
| 28 | `aws_bedrockagentcore_agent_runtime_endpoint` | bedrockagentcore |
| 29 | `aws_bedrockagentcore_api_key_credential_provider` | bedrockagentcore |
| 30 | `aws_bedrockagentcore_browser` | bedrockagentcore |
| 31 | `aws_bedrockagentcore_code_interpreter` | bedrockagentcore |
| 32 | `aws_bedrockagentcore_gateway` | bedrockagentcore |
| 33 | `aws_bedrockagentcore_gateway_target` | bedrockagentcore |
| 34 | `aws_bedrockagentcore_memory` | bedrockagentcore |
| 35 | `aws_bedrockagentcore_memory_strategy` | bedrockagentcore |
| 36 | `aws_bedrockagentcore_oauth2_credential_provider` | bedrockagentcore |
| 37 | `aws_bedrockagentcore_token_vault_cmk` | bedrockagentcore |
| 38 | `aws_bedrockagentcore_workload_identity` | bedrockagentcore |
| 39 | `aws_billing_view` | billing |
| 40 | `aws_chatbot_slack_channel_configuration` | chatbot |
| 41 | `aws_chatbot_teams_channel_configuration` | chatbot |
| 42 | `aws_cleanrooms_membership` | cleanrooms |
| 43 | `aws_cloudformation_stack_instances` | cloudformation |
| 44 | `aws_cloudfront_key_value_store` | cloudfront |
| 45 | `aws_cloudfront_multitenant_distribution` | cloudfront |
| 46 | `aws_cloudfront_trust_store` | cloudfront |
| 47 | `aws_cloudfront_vpc_origin` | cloudfront |
| 48 | `aws_cloudfrontkeyvaluestore_key` | cloudfrontkeyvaluestore |
| 49 | `aws_cloudfrontkeyvaluestore_keys_exclusive` | cloudfrontkeyvaluestore |
| 50 | `aws_cloudtrail_organization_delegated_admin_account` | cloudtrail |
| 51 | `aws_cloudwatch_contributor_insight_rule` | cloudwatch |
| 52 | `aws_cloudwatch_contributor_managed_insight_rule` | cloudwatch |
| 53 | `aws_cloudwatch_log_account_policy` | cloudwatch |
| 54 | `aws_cloudwatch_log_anomaly_detector` | cloudwatch |
| 55 | `aws_cloudwatch_log_delivery` | cloudwatch |
| 56 | `aws_cloudwatch_log_delivery_destination` | cloudwatch |
| 57 | `aws_cloudwatch_log_delivery_destination_policy` | cloudwatch |
| 58 | `aws_cloudwatch_log_delivery_source` | cloudwatch |
| 59 | `aws_cloudwatch_log_index_policy` | cloudwatch |
| 60 | `aws_cloudwatch_log_transformer` | cloudwatch |
| 61 | `aws_codebuild_fleet` | codebuild |
| 62 | `aws_codeconnections_connection` | codeconnections |
| 63 | `aws_codeconnections_host` | codeconnections |
| 64 | `aws_cognito_log_delivery_configuration` | cognito |
| 65 | `aws_cognito_managed_login_branding` | cognito |
| 66 | `aws_computeoptimizer_enrollment_status` | computeoptimizer |
| 67 | `aws_computeoptimizer_recommendation_preferences` | computeoptimizer |
| 68 | `aws_config_retention_configuration` | config |
| 69 | `aws_connect_phone_number_contact_flow_association` | connect |
| 70 | `aws_controltower_baseline` | controltower |
| 71 | `aws_controltower_landing_zone` | controltower |
| 72 | `aws_costoptimizationhub_enrollment_status` | costoptimizationhub |
| 73 | `aws_costoptimizationhub_preferences` | costoptimizationhub |
| 74 | `aws_dataexchange_event_action` | dataexchange |
| 75 | `aws_dataexchange_revision_assets` | dataexchange |
| 76 | `aws_default_subnet` | default |
| 77 | `aws_default_vpc` | default |
| 78 | `aws_devopsguru_event_sources_config` | devopsguru |
| 79 | `aws_devopsguru_notification_channel` | devopsguru |
| 80 | `aws_devopsguru_resource_collection` | devopsguru |
| 81 | `aws_devopsguru_service_integration` | devopsguru |
| 82 | `aws_directory_service_shared_directory_accepter` | directory |
| 83 | `aws_drs_replication_configuration_template` | drs |
| 84 | `aws_dsql_cluster` | dsql |
| 85 | `aws_dsql_cluster_peering` | dsql |
| 86 | `aws_dynamodb_resource_policy` | dynamodb |
| 87 | `aws_dynamodb_table_export` | dynamodb |
| 88 | `aws_ebs_fast_snapshot_restore` | ebs |
| 89 | `aws_ebs_snapshot_block_public_access` | ebs |
| 90 | `aws_ec2_allowed_images_settings` | ec2 |
| 91 | `aws_ec2_capacity_block_reservation` | ec2 |
| 92 | `aws_ec2_default_credit_specification` | ec2 |
| 93 | `aws_ec2_instance_metadata_defaults` | ec2 |
| 94 | `aws_ec2_network_insights_analysis` | ec2 |
| 95 | `aws_ec2_network_insights_path` | ec2 |
| 96 | `aws_ec2_serial_console_access` | ec2 |
| 97 | `aws_ec2_transit_gateway_default_route_table_association` | ec2 |
| 98 | `aws_ec2_transit_gateway_default_route_table_propagation` | ec2 |
| 99 | `aws_ec2_transit_gateway_route_table_propagation` | ec2 |
| 100 | `aws_ecr_account_setting` | ecr |
| 101 | `aws_ecr_repository_creation_template` | ecr |
| 102 | `aws_ecs_express_gateway_service` | ecs |
| 103 | `aws_eip_domain_name` | eip |
| 104 | `aws_eks_capability` | eks |
| 105 | `aws_elasticache_reserved_cache_node` | elasticache |
| 106 | `aws_elasticsearch_domain_saml_options` | elasticsearch |
| 107 | `aws_fis_target_account_configuration` | fis |
| 108 | `aws_fms_resource_set` | fms |
| 109 | `aws_fsx_s3_access_point_attachment` | fsx |
| 110 | `aws_globalaccelerator_cross_account_attachment` | globalaccelerator |
| 111 | `aws_glue_catalog_table_optimizer` | glue |
| 112 | `aws_grafana_workspace_service_account` | grafana |
| 113 | `aws_grafana_workspace_service_account_token` | grafana |
| 114 | `aws_guardduty_malware_protection_plan` | guardduty |
| 115 | `aws_guardduty_member_detector_feature` | guardduty |
| 116 | `aws_iam_group_policies_exclusive` | iam |
| 117 | `aws_iam_group_policy_attachments_exclusive` | iam |
| 118 | `aws_iam_organizations_features` | iam |
| 119 | `aws_iam_outbound_web_identity_federation` | iam |
| 120 | `aws_iam_role_policies_exclusive` | iam |
| 121 | `aws_iam_role_policy_attachments_exclusive` | iam |
| 122 | `aws_iam_user_policies_exclusive` | iam |
| 123 | `aws_iam_user_policy_attachments_exclusive` | iam |
| 124 | `aws_imagebuilder_lifecycle_policy` | imagebuilder |
| 125 | `aws_imagebuilder_workflow` | imagebuilder |
| 126 | `aws_inspector2_filter` | inspector2 |
| 127 | `aws_invoicing_invoice_unit` | invoicing |
| 128 | `aws_kinesis_resource_policy` | kinesis |
| 129 | `aws_lakeformation_data_cells_filter` | lakeformation |
| 130 | `aws_lakeformation_identity_center_configuration` | lakeformation |
| 131 | `aws_lakeformation_lf_tag_expression` | lakeformation |
| 132 | `aws_lakeformation_opt_in` | lakeformation |
| 133 | `aws_lakeformation_resource_lf_tag` | lakeformation |
| 134 | `aws_lambda_capacity_provider` | lambda |
| 135 | `aws_lambda_function_recursion_config` | lambda |
| 136 | `aws_lambda_runtime_management_config` | lambda |
| 137 | `aws_lexv2models_intent` | lexv2models |
| 138 | `aws_lexv2models_slot` | lexv2models |
| 139 | `aws_lexv2models_slot_type` | lexv2models |
| 140 | `aws_m2_application` | m2 |
| 141 | `aws_m2_deployment` | m2 |
| 142 | `aws_m2_environment` | m2 |
| 143 | `aws_macie2_organization_configuration` | macie2 |
| 144 | `aws_media_packagev2_channel_group` | media |
| 145 | `aws_memorydb_multi_region_cluster` | memorydb |
| 146 | `aws_msk_single_scram_secret_association` | msk |
| 147 | `aws_nat_gateway_eip_association` | nat |
| 148 | `aws_neptunegraph_graph` | neptunegraph |
| 149 | `aws_network_interface_permission` | network |
| 150 | `aws_networkfirewall_firewall_transit_gateway_attachment_accepter` | networkfirewall |
| 151 | `aws_networkfirewall_tls_inspection_configuration` | networkfirewall |
| 152 | `aws_networkfirewall_vpc_endpoint_association` | networkfirewall |
| 153 | `aws_networkflowmonitor_monitor` | networkflowmonitor |
| 154 | `aws_networkflowmonitor_scope` | networkflowmonitor |
| 155 | `aws_networkmanager_dx_gateway_attachment` | networkmanager |
| 156 | `aws_networkmonitor_monitor` | networkmonitor |
| 157 | `aws_networkmonitor_probe` | networkmonitor |
| 158 | `aws_notifications_channel_association` | notifications |
| 159 | `aws_notifications_event_rule` | notifications |
| 160 | `aws_notifications_notification_configuration` | notifications |
| 161 | `aws_notifications_notification_hub` | notifications |
| 162 | `aws_notificationscontacts_email_contact` | notificationscontacts |
| 163 | `aws_observabilityadmin_centralization_rule_for_organization` | observabilityadmin |
| 164 | `aws_odb_cloud_autonomous_vm_cluster` | odb |
| 165 | `aws_odb_cloud_exadata_infrastructure` | odb |
| 166 | `aws_odb_cloud_vm_cluster` | odb |
| 167 | `aws_odb_network` | odb |
| 168 | `aws_odb_network_peering_connection` | odb |
| 169 | `aws_opensearch_authorize_vpc_endpoint_access` | opensearch |
| 170 | `aws_organizations_tag` | organizations |
| 171 | `aws_osis_pipeline` | osis |
| 172 | `aws_paymentcryptography_key` | paymentcryptography |
| 173 | `aws_paymentcryptography_key_alias` | paymentcryptography |
| 174 | `aws_pinpoint_email_template` | pinpoint |
| 175 | `aws_pinpointsmsvoicev2_configuration_set` | pinpointsmsvoicev2 |
| 176 | `aws_pinpointsmsvoicev2_opt_out_list` | pinpointsmsvoicev2 |
| 177 | `aws_pinpointsmsvoicev2_phone_number` | pinpointsmsvoicev2 |
| 178 | `aws_prometheus_query_logging_configuration` | prometheus |
| 179 | `aws_prometheus_resource_policy` | prometheus |
| 180 | `aws_prometheus_scraper` | prometheus |
| 181 | `aws_prometheus_workspace_configuration` | prometheus |
| 182 | `aws_qbusiness_application` | qbusiness |
| 183 | `aws_quicksight_account_settings` | quicksight |
| 184 | `aws_quicksight_custom_permissions` | quicksight |
| 185 | `aws_quicksight_ip_restriction` | quicksight |
| 186 | `aws_quicksight_key_registration` | quicksight |
| 187 | `aws_quicksight_role_custom_permission` | quicksight |
| 188 | `aws_quicksight_role_membership` | quicksight |
| 189 | `aws_quicksight_user_custom_permission` | quicksight |
| 190 | `aws_rds_certificate` | rds |
| 191 | `aws_rds_cluster_snapshot_copy` | rds |
| 192 | `aws_rds_instance_state` | rds |
| 193 | `aws_rds_integration` | rds |
| 194 | `aws_rds_shard_group` | rds |
| 195 | `aws_redshift_data_share_authorization` | redshift |
| 196 | `aws_redshift_data_share_consumer_association` | redshift |
| 197 | `aws_redshift_integration` | redshift |
| 198 | `aws_redshift_logging` | redshift |
| 199 | `aws_redshift_snapshot_copy` | redshift |
| 200 | `aws_redshiftserverless_custom_domain_association` | redshiftserverless |
| 201 | `aws_rekognition_collection` | rekognition |
| 202 | `aws_rekognition_project` | rekognition |
| 203 | `aws_rekognition_stream_processor` | rekognition |
| 204 | `aws_resiliencehub_resiliency_policy` | resiliencehub |
| 205 | `aws_route53_records_exclusive` | route53 |
| 206 | `aws_route53_resolver_firewall_rule_group_association` | route53 |
| 207 | `aws_route53domains_delegation_signer_record` | route53domains |
| 208 | `aws_route53domains_domain` | route53domains |
| 209 | `aws_route53profiles_association` | route53profiles |
| 210 | `aws_route53profiles_profile` | route53profiles |
| 211 | `aws_route53profiles_resource_association` | route53profiles |
| 212 | `aws_s3_bucket_abac` | s3 |
| 213 | `aws_s3_bucket_metadata_configuration` | s3 |
| 214 | `aws_s3control_directory_bucket_access_point_scope` | s3control |
| 215 | `aws_s3tables_table_bucket_policy` | s3tables |
| 216 | `aws_s3tables_table_bucket_replication` | s3tables |
| 217 | `aws_s3tables_table_policy` | s3tables |
| 218 | `aws_s3tables_table_replication` | s3tables |
| 219 | `aws_s3vectors_index` | s3vectors |
| 220 | `aws_s3vectors_vector_bucket` | s3vectors |
| 221 | `aws_s3vectors_vector_bucket_policy` | s3vectors |
| 222 | `aws_sagemaker_hub` | sagemaker |
| 223 | `aws_sagemaker_mlflow_tracking_server` | sagemaker |
| 224 | `aws_securityhub_automation_rule` | securityhub |
| 225 | `aws_securityhub_configuration_policy` | securityhub |
| 226 | `aws_securityhub_configuration_policy_association` | securityhub |
| 227 | `aws_securityhub_standards_control_association` | securityhub |
| 228 | `aws_securitylake_aws_log_source` | securitylake |
| 229 | `aws_securitylake_custom_log_source` | securitylake |
| 230 | `aws_securitylake_subscriber` | securitylake |
| 231 | `aws_securitylake_subscriber_notification` | securitylake |
| 232 | `aws_servicecatalogappregistry_application` | servicecatalogappregistry |
| 233 | `aws_servicecatalogappregistry_attribute_group` | servicecatalogappregistry |
| 234 | `aws_servicecatalogappregistry_attribute_group_association` | servicecatalogappregistry |
| 235 | `aws_sesv2_account_suppression_attributes` | sesv2 |
| 236 | `aws_sesv2_email_identity_policy` | sesv2 |
| 237 | `aws_sesv2_tenant` | sesv2 |
| 238 | `aws_shield_proactive_engagement` | shield |
| 239 | `aws_shield_subscription` | shield |
| 240 | `aws_ssmcontacts_rotation` | ssmcontacts |
| 241 | `aws_ssmquicksetup_configuration_manager` | ssmquicksetup |
| 242 | `aws_ssoadmin_application_access_scope` | ssoadmin |
| 243 | `aws_timestreaminfluxdb_db_cluster` | timestreaminfluxdb |
| 244 | `aws_timestreaminfluxdb_db_instance` | timestreaminfluxdb |
| 245 | `aws_timestreamquery_scheduled_query` | timestreamquery |
| 246 | `aws_transfer_host_key` | transfer |
| 247 | `aws_transfer_web_app` | transfer |
| 248 | `aws_transfer_web_app_customization` | transfer |
| 249 | `aws_verifiedpermissions_identity_source` | verifiedpermissions |
| 250 | `aws_verifiedpermissions_policy` | verifiedpermissions |
| 251 | `aws_verifiedpermissions_policy_store` | verifiedpermissions |
| 252 | `aws_verifiedpermissions_policy_template` | verifiedpermissions |
| 253 | `aws_verifiedpermissions_schema` | verifiedpermissions |
| 254 | `aws_vpc_block_public_access_exclusion` | vpc |
| 255 | `aws_vpc_block_public_access_options` | vpc |
| 256 | `aws_vpc_encryption_control` | vpc |
| 257 | `aws_vpc_endpoint_private_dns` | vpc |
| 258 | `aws_vpc_endpoint_service_private_dns_verification` | vpc |
| 259 | `aws_vpc_route_server` | vpc |
| 260 | `aws_vpc_route_server_association` | vpc |
| 261 | `aws_vpc_route_server_endpoint` | vpc |
| 262 | `aws_vpc_route_server_peer` | vpc |
| 263 | `aws_vpc_route_server_propagation` | vpc |
| 264 | `aws_vpc_route_server_vpc_association` | vpc |
| 265 | `aws_vpc_security_group_vpc_association` | vpc |
| 266 | `aws_vpclattice_domain_verification` | vpclattice |
| 267 | `aws_vpn_concentrator` | vpn |
| 268 | `aws_wafv2_api_key` | wafv2 |
| 269 | `aws_wafv2_web_acl_rule_group_association` | wafv2 |
| 270 | `aws_workspacesweb_browser_settings` | workspacesweb |
| 271 | `aws_workspacesweb_browser_settings_association` | workspacesweb |
| 272 | `aws_workspacesweb_data_protection_settings` | workspacesweb |
| 273 | `aws_workspacesweb_data_protection_settings_association` | workspacesweb |
| 274 | `aws_workspacesweb_identity_provider` | workspacesweb |
| 275 | `aws_workspacesweb_ip_access_settings` | workspacesweb |
| 276 | `aws_workspacesweb_ip_access_settings_association` | workspacesweb |
| 277 | `aws_workspacesweb_network_settings` | workspacesweb |
| 278 | `aws_workspacesweb_network_settings_association` | workspacesweb |
| 279 | `aws_workspacesweb_portal` | workspacesweb |
| 280 | `aws_workspacesweb_session_logger` | workspacesweb |
| 281 | `aws_workspacesweb_session_logger_association` | workspacesweb |
| 282 | `aws_workspacesweb_trust_store` | workspacesweb |
| 283 | `aws_workspacesweb_trust_store_association` | workspacesweb |
| 284 | `aws_workspacesweb_user_access_logging_settings` | workspacesweb |
| 285 | `aws_workspacesweb_user_access_logging_settings_association` | workspacesweb |
| 286 | `aws_workspacesweb_user_settings` | workspacesweb |
| 287 | `aws_workspacesweb_user_settings_association` | workspacesweb |
| 288 | `aws_xray_resource_policy` | xray |

---

## Missing Resources by Service

### ACCOUNT (1 resources)

- `aws_account_region`

### ALB (1 resources)

- `aws_alb`

### API (2 resources)

- `aws_api_gateway_domain_name_access_association`
- `aws_api_gateway_rest_api_put`

### APPCONFIG (1 resources)

- `aws_appconfig_extension`

### APPFABRIC (5 resources)

- `aws_appfabric_app_authorization`
- `aws_appfabric_app_authorization_connection`
- `aws_appfabric_app_bundle`
- `aws_appfabric_ingestion`
- `aws_appfabric_ingestion_destination`

### APPRUNNER (1 resources)

- `aws_apprunner_deployment`

### APPSYNC (3 resources)

- `aws_appsync_api`
- `aws_appsync_channel_namespace`
- `aws_appsync_source_api_association`

### ATHENA (1 resources)

- `aws_athena_capacity_reservation`

### BACKUP (3 resources)

- `aws_backup_logically_air_gapped_vault`
- `aws_backup_restore_testing_plan`
- `aws_backup_restore_testing_selection`

### BCMDATAEXPORTS (1 resources)

- `aws_bcmdataexports_export`

### BEDROCK (4 resources)

- `aws_bedrock_custom_model`
- `aws_bedrock_guardrail_version`
- `aws_bedrock_inference_profile`
- `aws_bedrock_provisioned_model_throughput`

### BEDROCKAGENT (3 resources)

- `aws_bedrockagent_agent_collaborator`
- `aws_bedrockagent_flow`
- `aws_bedrockagent_prompt`

### BEDROCKAGENTCORE (12 resources)

- `aws_bedrockagentcore_agent_runtime`
- `aws_bedrockagentcore_agent_runtime_endpoint`
- `aws_bedrockagentcore_api_key_credential_provider`
- `aws_bedrockagentcore_browser`
- `aws_bedrockagentcore_code_interpreter`
- `aws_bedrockagentcore_gateway`
- `aws_bedrockagentcore_gateway_target`
- `aws_bedrockagentcore_memory`
- `aws_bedrockagentcore_memory_strategy`
- `aws_bedrockagentcore_oauth2_credential_provider`
- `aws_bedrockagentcore_token_vault_cmk`
- `aws_bedrockagentcore_workload_identity`

### BILLING (1 resources)

- `aws_billing_view`

### CHATBOT (2 resources)

- `aws_chatbot_slack_channel_configuration`
- `aws_chatbot_teams_channel_configuration`

### CLEANROOMS (1 resources)

- `aws_cleanrooms_membership`

### CLOUDFORMATION (1 resources)

- `aws_cloudformation_stack_instances`

### CLOUDFRONT (4 resources)

- `aws_cloudfront_key_value_store`
- `aws_cloudfront_multitenant_distribution`
- `aws_cloudfront_trust_store`
- `aws_cloudfront_vpc_origin`

### CLOUDFRONTKEYVALUESTORE (2 resources)

- `aws_cloudfrontkeyvaluestore_key`
- `aws_cloudfrontkeyvaluestore_keys_exclusive`

### CLOUDTRAIL (1 resources)

- `aws_cloudtrail_organization_delegated_admin_account`

### CLOUDWATCH (10 resources)

- `aws_cloudwatch_contributor_insight_rule`
- `aws_cloudwatch_contributor_managed_insight_rule`
- `aws_cloudwatch_log_account_policy`
- `aws_cloudwatch_log_anomaly_detector`
- `aws_cloudwatch_log_delivery`
- `aws_cloudwatch_log_delivery_destination`
- `aws_cloudwatch_log_delivery_destination_policy`
- `aws_cloudwatch_log_delivery_source`
- `aws_cloudwatch_log_index_policy`
- `aws_cloudwatch_log_transformer`

### CODEBUILD (1 resources)

- `aws_codebuild_fleet`

### CODECONNECTIONS (2 resources)

- `aws_codeconnections_connection`
- `aws_codeconnections_host`

### COGNITO (2 resources)

- `aws_cognito_log_delivery_configuration`
- `aws_cognito_managed_login_branding`

### COMPUTEOPTIMIZER (2 resources)

- `aws_computeoptimizer_enrollment_status`
- `aws_computeoptimizer_recommendation_preferences`

### CONFIG (1 resources)

- `aws_config_retention_configuration`

### CONNECT (1 resources)

- `aws_connect_phone_number_contact_flow_association`

### CONTROLTOWER (2 resources)

- `aws_controltower_baseline`
- `aws_controltower_landing_zone`

### COSTOPTIMIZATIONHUB (2 resources)

- `aws_costoptimizationhub_enrollment_status`
- `aws_costoptimizationhub_preferences`

### DATAEXCHANGE (2 resources)

- `aws_dataexchange_event_action`
- `aws_dataexchange_revision_assets`

### DEFAULT (2 resources)

- `aws_default_subnet`
- `aws_default_vpc`

### DEVOPSGURU (4 resources)

- `aws_devopsguru_event_sources_config`
- `aws_devopsguru_notification_channel`
- `aws_devopsguru_resource_collection`
- `aws_devopsguru_service_integration`

### DIRECTORY (1 resources)

- `aws_directory_service_shared_directory_accepter`

### DRS (1 resources)

- `aws_drs_replication_configuration_template`

### DSQL (2 resources)

- `aws_dsql_cluster`
- `aws_dsql_cluster_peering`

### DYNAMODB (2 resources)

- `aws_dynamodb_resource_policy`
- `aws_dynamodb_table_export`

### EBS (2 resources)

- `aws_ebs_fast_snapshot_restore`
- `aws_ebs_snapshot_block_public_access`

### EC2 (10 resources)

- `aws_ec2_allowed_images_settings`
- `aws_ec2_capacity_block_reservation`
- `aws_ec2_default_credit_specification`
- `aws_ec2_instance_metadata_defaults`
- `aws_ec2_network_insights_analysis`
- `aws_ec2_network_insights_path`
- `aws_ec2_serial_console_access`
- `aws_ec2_transit_gateway_default_route_table_association`
- `aws_ec2_transit_gateway_default_route_table_propagation`
- `aws_ec2_transit_gateway_route_table_propagation`

### ECR (2 resources)

- `aws_ecr_account_setting`
- `aws_ecr_repository_creation_template`

### ECS (1 resources)

- `aws_ecs_express_gateway_service`

### EIP (1 resources)

- `aws_eip_domain_name`

### EKS (1 resources)

- `aws_eks_capability`

### ELASTICACHE (1 resources)

- `aws_elasticache_reserved_cache_node`

### ELASTICSEARCH (1 resources)

- `aws_elasticsearch_domain_saml_options`

### FIS (1 resources)

- `aws_fis_target_account_configuration`

### FMS (1 resources)

- `aws_fms_resource_set`

### FSX (1 resources)

- `aws_fsx_s3_access_point_attachment`

### GLOBALACCELERATOR (1 resources)

- `aws_globalaccelerator_cross_account_attachment`

### GLUE (1 resources)

- `aws_glue_catalog_table_optimizer`

### GRAFANA (2 resources)

- `aws_grafana_workspace_service_account`
- `aws_grafana_workspace_service_account_token`

### GUARDDUTY (2 resources)

- `aws_guardduty_malware_protection_plan`
- `aws_guardduty_member_detector_feature`

### IAM (8 resources)

- `aws_iam_group_policies_exclusive`
- `aws_iam_group_policy_attachments_exclusive`
- `aws_iam_organizations_features`
- `aws_iam_outbound_web_identity_federation`
- `aws_iam_role_policies_exclusive`
- `aws_iam_role_policy_attachments_exclusive`
- `aws_iam_user_policies_exclusive`
- `aws_iam_user_policy_attachments_exclusive`

### IMAGEBUILDER (2 resources)

- `aws_imagebuilder_lifecycle_policy`
- `aws_imagebuilder_workflow`

### INSPECTOR2 (1 resources)

- `aws_inspector2_filter`

### INVOICING (1 resources)

- `aws_invoicing_invoice_unit`

### KINESIS (1 resources)

- `aws_kinesis_resource_policy`

### LAKEFORMATION (5 resources)

- `aws_lakeformation_data_cells_filter`
- `aws_lakeformation_identity_center_configuration`
- `aws_lakeformation_lf_tag_expression`
- `aws_lakeformation_opt_in`
- `aws_lakeformation_resource_lf_tag`

### LAMBDA (3 resources)

- `aws_lambda_capacity_provider`
- `aws_lambda_function_recursion_config`
- `aws_lambda_runtime_management_config`

### LEXV2MODELS (3 resources)

- `aws_lexv2models_intent`
- `aws_lexv2models_slot`
- `aws_lexv2models_slot_type`

### M2 (3 resources)

- `aws_m2_application`
- `aws_m2_deployment`
- `aws_m2_environment`

### MACIE2 (1 resources)

- `aws_macie2_organization_configuration`

### MEDIA (1 resources)

- `aws_media_packagev2_channel_group`

### MEMORYDB (1 resources)

- `aws_memorydb_multi_region_cluster`

### MSK (1 resources)

- `aws_msk_single_scram_secret_association`

### NAT (1 resources)

- `aws_nat_gateway_eip_association`

### NEPTUNEGRAPH (1 resources)

- `aws_neptunegraph_graph`

### NETWORK (1 resources)

- `aws_network_interface_permission`

### NETWORKFIREWALL (3 resources)

- `aws_networkfirewall_firewall_transit_gateway_attachment_accepter`
- `aws_networkfirewall_tls_inspection_configuration`
- `aws_networkfirewall_vpc_endpoint_association`

### NETWORKFLOWMONITOR (2 resources)

- `aws_networkflowmonitor_monitor`
- `aws_networkflowmonitor_scope`

### NETWORKMANAGER (1 resources)

- `aws_networkmanager_dx_gateway_attachment`

### NETWORKMONITOR (2 resources)

- `aws_networkmonitor_monitor`
- `aws_networkmonitor_probe`

### NOTIFICATIONS (4 resources)

- `aws_notifications_channel_association`
- `aws_notifications_event_rule`
- `aws_notifications_notification_configuration`
- `aws_notifications_notification_hub`

### NOTIFICATIONSCONTACTS (1 resources)

- `aws_notificationscontacts_email_contact`

### OBSERVABILITYADMIN (1 resources)

- `aws_observabilityadmin_centralization_rule_for_organization`

### ODB (5 resources)

- `aws_odb_cloud_autonomous_vm_cluster`
- `aws_odb_cloud_exadata_infrastructure`
- `aws_odb_cloud_vm_cluster`
- `aws_odb_network`
- `aws_odb_network_peering_connection`

### OPENSEARCH (1 resources)

- `aws_opensearch_authorize_vpc_endpoint_access`

### ORGANIZATIONS (1 resources)

- `aws_organizations_tag`

### OSIS (1 resources)

- `aws_osis_pipeline`

### PAYMENTCRYPTOGRAPHY (2 resources)

- `aws_paymentcryptography_key`
- `aws_paymentcryptography_key_alias`

### PINPOINT (1 resources)

- `aws_pinpoint_email_template`

### PINPOINTSMSVOICEV2 (3 resources)

- `aws_pinpointsmsvoicev2_configuration_set`
- `aws_pinpointsmsvoicev2_opt_out_list`
- `aws_pinpointsmsvoicev2_phone_number`

### PROMETHEUS (4 resources)

- `aws_prometheus_query_logging_configuration`
- `aws_prometheus_resource_policy`
- `aws_prometheus_scraper`
- `aws_prometheus_workspace_configuration`

### QBUSINESS (1 resources)

- `aws_qbusiness_application`

### QUICKSIGHT (7 resources)

- `aws_quicksight_account_settings`
- `aws_quicksight_custom_permissions`
- `aws_quicksight_ip_restriction`
- `aws_quicksight_key_registration`
- `aws_quicksight_role_custom_permission`
- `aws_quicksight_role_membership`
- `aws_quicksight_user_custom_permission`

### RDS (5 resources)

- `aws_rds_certificate`
- `aws_rds_cluster_snapshot_copy`
- `aws_rds_instance_state`
- `aws_rds_integration`
- `aws_rds_shard_group`

### REDSHIFT (5 resources)

- `aws_redshift_data_share_authorization`
- `aws_redshift_data_share_consumer_association`
- `aws_redshift_integration`
- `aws_redshift_logging`
- `aws_redshift_snapshot_copy`

### REDSHIFTSERVERLESS (1 resources)

- `aws_redshiftserverless_custom_domain_association`

### REKOGNITION (3 resources)

- `aws_rekognition_collection`
- `aws_rekognition_project`
- `aws_rekognition_stream_processor`

### RESILIENCEHUB (1 resources)

- `aws_resiliencehub_resiliency_policy`

### ROUTE53 (2 resources)

- `aws_route53_records_exclusive`
- `aws_route53_resolver_firewall_rule_group_association`

### ROUTE53DOMAINS (2 resources)

- `aws_route53domains_delegation_signer_record`
- `aws_route53domains_domain`

### ROUTE53PROFILES (3 resources)

- `aws_route53profiles_association`
- `aws_route53profiles_profile`
- `aws_route53profiles_resource_association`

### S3 (2 resources)

- `aws_s3_bucket_abac`
- `aws_s3_bucket_metadata_configuration`

### S3CONTROL (1 resources)

- `aws_s3control_directory_bucket_access_point_scope`

### S3TABLES (4 resources)

- `aws_s3tables_table_bucket_policy`
- `aws_s3tables_table_bucket_replication`
- `aws_s3tables_table_policy`
- `aws_s3tables_table_replication`

### S3VECTORS (3 resources)

- `aws_s3vectors_index`
- `aws_s3vectors_vector_bucket`
- `aws_s3vectors_vector_bucket_policy`

### SAGEMAKER (2 resources)

- `aws_sagemaker_hub`
- `aws_sagemaker_mlflow_tracking_server`

### SECURITYHUB (4 resources)

- `aws_securityhub_automation_rule`
- `aws_securityhub_configuration_policy`
- `aws_securityhub_configuration_policy_association`
- `aws_securityhub_standards_control_association`

### SECURITYLAKE (4 resources)

- `aws_securitylake_aws_log_source`
- `aws_securitylake_custom_log_source`
- `aws_securitylake_subscriber`
- `aws_securitylake_subscriber_notification`

### SERVICECATALOGAPPREGISTRY (3 resources)

- `aws_servicecatalogappregistry_application`
- `aws_servicecatalogappregistry_attribute_group`
- `aws_servicecatalogappregistry_attribute_group_association`

### SESV2 (3 resources)

- `aws_sesv2_account_suppression_attributes`
- `aws_sesv2_email_identity_policy`
- `aws_sesv2_tenant`

### SHIELD (2 resources)

- `aws_shield_proactive_engagement`
- `aws_shield_subscription`

### SSMCONTACTS (1 resources)

- `aws_ssmcontacts_rotation`

### SSMQUICKSETUP (1 resources)

- `aws_ssmquicksetup_configuration_manager`

### SSOADMIN (1 resources)

- `aws_ssoadmin_application_access_scope`

### TIMESTREAMINFLUXDB (2 resources)

- `aws_timestreaminfluxdb_db_cluster`
- `aws_timestreaminfluxdb_db_instance`

### TIMESTREAMQUERY (1 resources)

- `aws_timestreamquery_scheduled_query`

### TRANSFER (3 resources)

- `aws_transfer_host_key`
- `aws_transfer_web_app`
- `aws_transfer_web_app_customization`

### VERIFIEDPERMISSIONS (5 resources)

- `aws_verifiedpermissions_identity_source`
- `aws_verifiedpermissions_policy`
- `aws_verifiedpermissions_policy_store`
- `aws_verifiedpermissions_policy_template`
- `aws_verifiedpermissions_schema`

### VPC (12 resources)

- `aws_vpc_block_public_access_exclusion`
- `aws_vpc_block_public_access_options`
- `aws_vpc_encryption_control`
- `aws_vpc_endpoint_private_dns`
- `aws_vpc_endpoint_service_private_dns_verification`
- `aws_vpc_route_server`
- `aws_vpc_route_server_association`
- `aws_vpc_route_server_endpoint`
- `aws_vpc_route_server_peer`
- `aws_vpc_route_server_propagation`
- `aws_vpc_route_server_vpc_association`
- `aws_vpc_security_group_vpc_association`

### VPCLATTICE (1 resources)

- `aws_vpclattice_domain_verification`

### VPN (1 resources)

- `aws_vpn_concentrator`

### WAFV2 (2 resources)

- `aws_wafv2_api_key`
- `aws_wafv2_web_acl_rule_group_association`

### WORKSPACESWEB (18 resources)

- `aws_workspacesweb_browser_settings`
- `aws_workspacesweb_browser_settings_association`
- `aws_workspacesweb_data_protection_settings`
- `aws_workspacesweb_data_protection_settings_association`
- `aws_workspacesweb_identity_provider`
- `aws_workspacesweb_ip_access_settings`
- `aws_workspacesweb_ip_access_settings_association`
- `aws_workspacesweb_network_settings`
- `aws_workspacesweb_network_settings_association`
- `aws_workspacesweb_portal`
- `aws_workspacesweb_session_logger`
- `aws_workspacesweb_session_logger_association`
- `aws_workspacesweb_trust_store`
- `aws_workspacesweb_trust_store_association`
- `aws_workspacesweb_user_access_logging_settings`
- `aws_workspacesweb_user_access_logging_settings_association`
- `aws_workspacesweb_user_settings`
- `aws_workspacesweb_user_settings_association`

### XRAY (1 resources)

- `aws_xray_resource_policy`

---

## How to Add a Missing Resource

For each missing resource, follow these steps:

### 1. Find Terraform Documentation

URL format: `https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/<resource_name>`

Example: `https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/vpc`

### 2. Identify the AWS Service

Determine which AWS service this resource belongs to (e.g., EC2, S3, Lambda, RDS)

### 3. Find the Boto3 Client Name

The boto3 client name usually matches the service name in lowercase with hyphens.

Examples:
- EC2 → `ec2`
- S3 → `s3`
- Lambda → `lambda`
- RDS → `rds`
- API Gateway → `apigateway`
- API Gateway V2 → `apigatewayv2`

Reference: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html

### 4. Find the Boto3 API Method

Look for the appropriate `describe_*` or `list_*` method that returns all resources of this type.

Examples:
- VPCs → `describe_vpcs`
- Lambda Functions → `list_functions`
- RDS Instances → `describe_db_instances`
- S3 Buckets → `list_buckets`

### 5. Determine Response Structure

Call the API method and examine the response to find:
- **topkey**: The top-level key containing the list of resources
- **key**: The field that uniquely identifies each resource
- **filterid**: The parameter name used to filter by ID

### 6. Add Entry to aws_dict.py

Add the resource definition to `code/fixtf_aws_resources/aws_dict.py`:

```python
aws_vpc = {
    "clfn":     "ec2",              # boto3 client name
    "descfn":   "describe_vpcs",    # boto3 API method
    "topkey":   "Vpcs",             # top-level key in response
    "key":      "VpcId",            # resource identifier
    "filterid": "VpcId"             # filter parameter name
}
```

### Example: Adding aws_subnet

1. **Terraform docs**: https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/subnet
2. **AWS Service**: EC2
3. **Boto3 client**: `ec2`
4. **Boto3 method**: `describe_subnets`
5. **Response structure**:
   ```python
   {
       "Subnets": [
           {
               "SubnetId": "subnet-12345",
               ...
           }
       ]
   }
   ```
6. **Entry**:
   ```python
   aws_subnet = {
       "clfn":     "ec2",
       "descfn":   "describe_subnets",
       "topkey":   "Subnets",
       "key":      "SubnetId",
       "filterid": "SubnetId"
   }
   ```