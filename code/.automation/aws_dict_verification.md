# AWS Dictionary Verification Report

**Generated:** Sat 17 Jan 2026 13:31:10 GMT

**Total Resources:** 1611

## Summary

- ✅ Valid: 989
- ⚠️  Warnings: 473
- ❌ Errors: 149

## ❌ Errors

These resources have critical issues that prevent them from working:

### `aws_finspace_kx_cluster`

- **Client:** `finspace-data`
- **Method:** `list_clusters`

**Issues:**
- Invalid method: Method 'list_clusters' not found on client 'finspace-data'

### `aws_finspace_kx_database`

- **Client:** `finspace-data`
- **Method:** `list_databases`

**Issues:**
- Invalid method: Method 'list_databases' not found on client 'finspace-data'

### `aws_finspace_kx_scaling_group`

- **Client:** `finspace-data`
- **Method:** `list_scaling_groups`

**Issues:**
- Invalid method: Method 'list_scaling_groups' not found on client 'finspace-data'

### `aws_finspace_kx_volume`

- **Client:** `finspace-data`
- **Method:** `list_volumes`

**Issues:**
- Invalid method: Method 'list_volumes' not found on client 'finspace-data'

### `aws_load_balancer_policy`

- **Client:** `elbv2`
- **Method:** `describe_load_balancer_policy_types`

**Issues:**
- Invalid method: Method 'describe_load_balancer_policy_types' not found on client 'elbv2'

### `aws_macie2_classification_export_configuration`

- **Client:** `macie2`
- **Method:** `list_classification_export_configurations`

**Issues:**
- Invalid method: Method 'list_classification_export_configurations' not found on client 'macie2'

### `aws_macie2_classification_job`

- **Client:** `macie2`
- **Method:** `list_jobs`

**Issues:**
- Invalid method: Method 'list_jobs' not found on client 'macie2'

### `aws_macie2_member`

- **Client:** `macie2`
- **Method:** `list_invitation_accepters`

**Issues:**
- Invalid method: Method 'list_invitation_accepters' not found on client 'macie2'

### `aws_msk_cluster_policy`

- **Client:** `kafka`
- **Method:** `list_cluster_policies`

**Issues:**
- Invalid method: Method 'list_cluster_policies' not found on client 'kafka'

### `aws_neptune_cluster_instance`

- **Client:** `neptune`
- **Method:** `describe_db_cluster_instances`

**Issues:**
- Invalid method: Method 'describe_db_cluster_instances' not found on client 'neptune'

### `aws_networkfirewall_logging_configuration`

- **Client:** `network-firewall`
- **Method:** `list_logging_configurations`

**Issues:**
- Invalid method: Method 'list_logging_configurations' not found on client 'network-firewall'

### `aws_networkfirewall_resource_policy`

- **Client:** `network-firewall`
- **Method:** `list_resource_policies`

**Issues:**
- Invalid method: Method 'list_resource_policies' not found on client 'network-firewall'

### `aws_networkmanager_attachment_accepter`

- **Client:** `networkmanager`
- **Method:** `list_attachment_accepters`

**Issues:**
- Invalid method: Method 'list_attachment_accepters' not found on client 'networkmanager'

### `aws_networkmanager_connect_attachment`

- **Client:** `networkmanager`
- **Method:** `list_connect_attachments`

**Issues:**
- Invalid method: Method 'list_connect_attachments' not found on client 'networkmanager'

### `aws_networkmanager_connection`

- **Client:** `networkmanager`
- **Method:** `list_connections`

**Issues:**
- Invalid method: Method 'list_connections' not found on client 'networkmanager'

### `aws_networkmanager_core_network_policy_attachment`

- **Client:** `networkmanager`
- **Method:** `list_core_network_policy_attachments`

**Issues:**
- Invalid method: Method 'list_core_network_policy_attachments' not found on client 'networkmanager'

### `aws_networkmanager_customer_gateway_association`

- **Client:** `networkmanager`
- **Method:** `list_customer_gateway_associations`

**Issues:**
- Invalid method: Method 'list_customer_gateway_associations' not found on client 'networkmanager'

### `aws_networkmanager_link`

- **Client:** `networkmanager`
- **Method:** `list_links`

**Issues:**
- Invalid method: Method 'list_links' not found on client 'networkmanager'

### `aws_networkmanager_link_association`

- **Client:** `networkmanager`
- **Method:** `list_link_associations`

**Issues:**
- Invalid method: Method 'list_link_associations' not found on client 'networkmanager'

### `aws_networkmanager_site_to_site_vpn_attachment`

- **Client:** `networkmanager`
- **Method:** `list_site_to_site_vpn_attachments`

**Issues:**
- Invalid method: Method 'list_site_to_site_vpn_attachments' not found on client 'networkmanager'

### `aws_networkmanager_transit_gateway_connect_peer_association`

- **Client:** `networkmanager`
- **Method:** `list_transit_gateway_connect_peers`

**Issues:**
- Invalid method: Method 'list_transit_gateway_connect_peers' not found on client 'networkmanager'

### `aws_networkmanager_transit_gateway_peering`

- **Client:** `networkmanager`
- **Method:** `list_transit_gateway_peerings`

**Issues:**
- Invalid method: Method 'list_transit_gateway_peerings' not found on client 'networkmanager'

### `aws_networkmanager_transit_gateway_route_table_attachment`

- **Client:** `networkmanager`
- **Method:** `list_transit_gateway_route_tables`

**Issues:**
- Invalid method: Method 'list_transit_gateway_route_tables' not found on client 'networkmanager'

### `aws_networkmanager_vpc_attachment`

- **Client:** `networkmanager`
- **Method:** `list_vpc_attachments`

**Issues:**
- Invalid method: Method 'list_vpc_attachments' not found on client 'networkmanager'

### `aws_networkmonitor_probe`

- **Client:** `networkmonitor`
- **Method:** `list_monitor_probes`

**Issues:**
- Invalid method: Method 'list_monitor_probes' not found on client 'networkmonitor'

### `aws_oam_link`

- **Client:** `networkmanager`
- **Method:** `list_links`

**Issues:**
- Invalid method: Method 'list_links' not found on client 'networkmanager'

### `aws_oam_sink`

- **Client:** `networkmanager`
- **Method:** `list_links`

**Issues:**
- Invalid method: Method 'list_links' not found on client 'networkmanager'

### `aws_oam_sink_policy`

- **Client:** `networkmanager`
- **Method:** `list_links`

**Issues:**
- Invalid method: Method 'list_links' not found on client 'networkmanager'

### `aws_opensearch_inbound_connection_accepter`

- **Client:** `opensearch`
- **Method:** `list_inbound_connection_accepters`

**Issues:**
- Invalid method: Method 'list_inbound_connection_accepters' not found on client 'opensearch'

### `aws_opensearch_outbound_connection`

- **Client:** `opensearch`
- **Method:** `list_inbound_connection_accepters`

**Issues:**
- Invalid method: Method 'list_inbound_connection_accepters' not found on client 'opensearch'

### `aws_opensearch_package`

- **Client:** `opensearch`
- **Method:** `list_packages`

**Issues:**
- Invalid method: Method 'list_packages' not found. Similar methods: list_packages_for_domain

### `aws_opensearch_package_association`

- **Client:** `opensearch`
- **Method:** `list_packages`

**Issues:**
- Invalid method: Method 'list_packages' not found. Similar methods: list_packages_for_domain

### `aws_opsworks_application`

- **Client:** `opsworks`
- **Method:** `list_applications`

**Issues:**
- Invalid client: Unknown service: opsworks

### `aws_opsworks_custom_layer`

- **Client:** `opsworks`
- **Method:** `list_custom_layers`

**Issues:**
- Invalid client: Unknown service: opsworks

### `aws_opsworks_ecs_cluster_layer`

- **Client:** `opsworks`
- **Method:** `describe_ecs_clusters`

**Issues:**
- Invalid client: Unknown service: opsworks

### `aws_opsworks_ganglia_layer`

- **Client:** `opsworks`
- **Method:** `list_ganglia_layers`

**Issues:**
- Invalid client: Unknown service: opsworks

### `aws_opsworks_haproxy_layer`

- **Client:** `opsworks`
- **Method:** `list_haproxy_layers`

**Issues:**
- Invalid client: Unknown service: opsworks

### `aws_opsworks_instance`

- **Client:** `opsworks`
- **Method:** `list_instances`

**Issues:**
- Invalid client: Unknown service: opsworks

### `aws_opsworks_java_app_layer`

- **Client:** `opsworks`
- **Method:** `list_java_app_layers`

**Issues:**
- Invalid client: Unknown service: opsworks

### `aws_opsworks_memcached_layer`

- **Client:** `opsworks`
- **Method:** `list_memcached_layers`

**Issues:**
- Invalid client: Unknown service: opsworks

### `aws_opsworks_mysql_layer`

- **Client:** `opsworks`
- **Method:** `list_mysql_layers`

**Issues:**
- Invalid client: Unknown service: opsworks

### `aws_opsworks_nodejs_app_layer`

- **Client:** `opsworks`
- **Method:** `list_nodejs_app_layers`

**Issues:**
- Invalid client: Unknown service: opsworks

### `aws_opsworks_permission`

- **Client:** `opsworks`
- **Method:** `list_permissions`

**Issues:**
- Invalid client: Unknown service: opsworks

### `aws_opsworks_php_app_layer`

- **Client:** `opsworks`
- **Method:** `list_php_app_layers`

**Issues:**
- Invalid client: Unknown service: opsworks

### `aws_opsworks_rails_app_layer`

- **Client:** `opsworks`
- **Method:** `list_rails_app_layers`

**Issues:**
- Invalid client: Unknown service: opsworks

### `aws_opsworks_rds_db_instance`

- **Client:** `opsworks`
- **Method:** `list_rds_db_instances`

**Issues:**
- Invalid client: Unknown service: opsworks

### `aws_opsworks_stack`

- **Client:** `opsworks`
- **Method:** `list_stacks`

**Issues:**
- Invalid client: Unknown service: opsworks

### `aws_opsworks_static_web_layer`

- **Client:** `opsworks`
- **Method:** `list_static_web_layers`

**Issues:**
- Invalid client: Unknown service: opsworks

### `aws_opsworks_user_profile`

- **Client:** `opsworks`
- **Method:** `list_user_profiles`

**Issues:**
- Invalid client: Unknown service: opsworks

### `aws_pinpoint_adm_channel`

- **Client:** `pinpoint`
- **Method:** `list_adm_channels`

**Issues:**
- Invalid method: Method 'list_adm_channels' not found on client 'pinpoint'

### `aws_pinpoint_apns_channel`

- **Client:** `pinpoint`
- **Method:** `list_apns_channels`

**Issues:**
- Invalid method: Method 'list_apns_channels' not found on client 'pinpoint'

### `aws_pinpoint_apns_sandbox_channel`

- **Client:** `pinpoint`
- **Method:** `list_apns_sandbox_channels`

**Issues:**
- Invalid method: Method 'list_apns_sandbox_channels' not found on client 'pinpoint'

### `aws_pinpoint_apns_voip_channel`

- **Client:** `pinpoint`
- **Method:** `list_apns_voip_channels`

**Issues:**
- Invalid method: Method 'list_apns_voip_channels' not found on client 'pinpoint'

### `aws_pinpoint_apns_voip_sandbox_channel`

- **Client:** `pinpoint`
- **Method:** `list_apns_voip_sandbox_channels`

**Issues:**
- Invalid method: Method 'list_apns_voip_sandbox_channels' not found on client 'pinpoint'

### `aws_pinpoint_app`

- **Client:** `pinpoint`
- **Method:** `list_apps`

**Issues:**
- Invalid method: Method 'list_apps' not found on client 'pinpoint'

### `aws_pinpoint_baidu_channel`

- **Client:** `pinpoint`
- **Method:** `list_baidu_channels`

**Issues:**
- Invalid method: Method 'list_baidu_channels' not found on client 'pinpoint'

### `aws_pinpoint_email_channel`

- **Client:** `pinpoint`
- **Method:** `list_email_channels`

**Issues:**
- Invalid method: Method 'list_email_channels' not found on client 'pinpoint'

### `aws_pinpoint_email_template`

- **Client:** `pinpoint-email`
- **Method:** `list_email_templates`

**Issues:**
- Invalid method: Method 'list_email_templates' not found on client 'pinpoint-email'

### `aws_pinpoint_event_stream`

- **Client:** `pinpoint`
- **Method:** `list_event_streams`

**Issues:**
- Invalid method: Method 'list_event_streams' not found on client 'pinpoint'

### `aws_pinpoint_gcm_channel`

- **Client:** `pinpoint`
- **Method:** `list_gcm_channels`

**Issues:**
- Invalid method: Method 'list_gcm_channels' not found on client 'pinpoint'

### `aws_pinpoint_sms_channel`

- **Client:** `pinpoint`
- **Method:** `list_sms_channels`

**Issues:**
- Invalid method: Method 'list_sms_channels' not found on client 'pinpoint'

### `aws_proxy_protocol_policy`

- **Client:** `wafv2`
- **Method:** `list_proxy_protocol_policies`

**Issues:**
- Invalid method: Method 'list_proxy_protocol_policies' not found on client 'wafv2'

### `aws_qldb_ledger`

- **Client:** `qldb`
- **Method:** `list_ledgers`

**Issues:**
- Invalid client: Unknown service: qldb

### `aws_qldb_stream`

- **Client:** `qldb`
- **Method:** `list_streams`

**Issues:**
- Invalid client: Unknown service: qldb

### `aws_quicksight_account_subscription`

- **Client:** `quicksight`
- **Method:** `list_account_subscriptions`

**Issues:**
- Invalid method: Method 'list_account_subscriptions' not found on client 'quicksight'

### `aws_quicksight_folder_membership`

- **Client:** `quicksight`
- **Method:** `list_folder_memberships`

**Issues:**
- Invalid method: Method 'list_folder_memberships' not found. Similar methods: list_folder_members

### `aws_quicksight_key_registration`

- **Client:** `quicksight`
- **Method:** `list_key_registrations`

**Issues:**
- Invalid method: Method 'list_key_registrations' not found on client 'quicksight'

### `aws_ram_resource_share_accepter`

- **Client:** `ram`
- **Method:** `list_resource_share_accepters`

**Issues:**
- Invalid method: Method 'list_resource_share_accepters' not found on client 'ram'

### `aws_ram_sharing_with_organization`

- **Client:** `ram`
- **Method:** `list_sharing_accounts`

**Issues:**
- Invalid method: Method 'list_sharing_accounts' not found on client 'ram'

### `aws_rbin_rule`

- **Client:** `rbin`
- **Method:** `list_resolver_rules`

**Issues:**
- Invalid method: Method 'list_resolver_rules' not found on client 'rbin'

### `aws_redshiftserverless_resource_policy`

- **Client:** `redshift-serverless`
- **Method:** `describe_resource_policies`

**Issues:**
- Invalid method: Method 'describe_resource_policies' not found on client 'redshift-serverless'

### `aws_resourceexplorer2_index`

- **Client:** `resource-explorer-2`
- **Method:** `list_indices`

**Issues:**
- Invalid method: Method 'list_indices' not found on client 'resource-explorer-2'

### `aws_resourcegroups_resource`

- **Client:** `resource-groups`
- **Method:** `list_resources`

**Issues:**
- Invalid method: Method 'list_resources' not found on client 'resource-groups'

### `aws_route53_resolver_firewall_rule`

- **Client:** `route53resolver`
- **Method:** `list_resolver_firewall_rules`

**Issues:**
- Invalid method: Method 'list_resolver_firewall_rules' not found on client 'route53resolver'

### `aws_rum_metrics_destination`

- **Client:** `rum`
- **Method:** `list_metrics_destinations`

**Issues:**
- Invalid method: Method 'list_metrics_destinations' not found on client 'rum'

### `aws_s3control_bucket`

- **Client:** `s3control`
- **Method:** `list_buckets`

**Issues:**
- Invalid method: Method 'list_buckets' not found on client 's3control'

### `aws_sagemaker_endpoint_configuration`

- **Client:** `sagemaker`
- **Method:** `list_endpoint_configurations`

**Issues:**
- Invalid method: Method 'list_endpoint_configurations' not found on client 'sagemaker'

### `aws_sagemaker_servicecatalog_portfolio_status`

- **Client:** `sagemaker`
- **Method:** `get_service_catalog_portfolio_status`

**Issues:**
- Invalid method: Method 'get_service_catalog_portfolio_status' not found on client 'sagemaker'

### `aws_schemas_registry_policy`

- **Client:** `schemas`
- **Method:** `get_registry_policy`

**Issues:**
- Invalid method: Method 'get_registry_policy' not found on client 'schemas'

### `aws_securityhub_finding_aggregator`

- **Client:** `securityhub`
- **Method:** `describe_finding_aggregators`

**Issues:**
- Invalid method: Method 'describe_finding_aggregators' not found on client 'securityhub'

### `aws_securityhub_insight`

- **Client:** `securityhub`
- **Method:** `describe_insights`

**Issues:**
- Invalid method: Method 'describe_insights' not found on client 'securityhub'

### `aws_securityhub_invite_accepter`

- **Client:** `securityhub`
- **Method:** `describe_invite_accepters`

**Issues:**
- Invalid method: Method 'describe_invite_accepters' not found on client 'securityhub'

### `aws_securityhub_member`

- **Client:** `securityhub`
- **Method:** `describe_members`

**Issues:**
- Invalid method: Method 'describe_members' not found on client 'securityhub'

### `aws_securityhub_organization_admin_account`

- **Client:** `securityhub`
- **Method:** `describe_organization_admin_account`

**Issues:**
- Invalid method: Method 'describe_organization_admin_account' not found on client 'securityhub'

### `aws_securityhub_product_subscription`

- **Client:** `securityhub`
- **Method:** `describe_product_subscriptions`

**Issues:**
- Invalid method: Method 'describe_product_subscriptions' not found on client 'securityhub'

### `aws_securityhub_standards_subscription`

- **Client:** `securityhub`
- **Method:** `describe_standards_subscriptions`

**Issues:**
- Invalid method: Method 'describe_standards_subscriptions' not found. Similar methods: describe_standards

### `aws_securitylake_data_lake`

- **Client:** `securitylake`
- **Method:** `describe_data_lakes`

**Issues:**
- Invalid method: Method 'describe_data_lakes' not found on client 'securitylake'

### `aws_servicecatalog_budget_resource_association`

- **Client:** `servicecatalog`
- **Method:** `list_budget_resource_associations`

**Issues:**
- Invalid method: Method 'list_budget_resource_associations' not found on client 'servicecatalog'

### `aws_servicecatalog_organizations_access`

- **Client:** `servicecatalog`
- **Method:** `list_organization_access`

**Issues:**
- Invalid method: Method 'list_organization_access' not found on client 'servicecatalog'

### `aws_servicecatalog_portfolio_share`

- **Client:** `servicecatalog`
- **Method:** `list_portfolio_shares`

**Issues:**
- Invalid method: Method 'list_portfolio_shares' not found on client 'servicecatalog'

### `aws_servicecatalog_principal_portfolio_association`

- **Client:** `servicecatalog`
- **Method:** `list_principal_portfolio_associations`

**Issues:**
- Invalid method: Method 'list_principal_portfolio_associations' not found on client 'servicecatalog'

### `aws_servicecatalog_product_portfolio_association`

- **Client:** `servicecatalog`
- **Method:** `list_product_portfolio_associations`

**Issues:**
- Invalid method: Method 'list_product_portfolio_associations' not found on client 'servicecatalog'

### `aws_servicecatalog_provisioned_product`

- **Client:** `servicecatalog`
- **Method:** `list_provisioned_products`

**Issues:**
- Invalid method: Method 'list_provisioned_products' not found on client 'servicecatalog'

### `aws_servicecatalog_tag_option_resource_association`

- **Client:** `servicecatalog`
- **Method:** `list_tag_option_resource_associations`

**Issues:**
- Invalid method: Method 'list_tag_option_resource_associations' not found on client 'servicecatalog'

### `aws_servicecatalogappregistry_attribute_group_association`

- **Client:** `servicecatalog-appregistry`
- **Method:** `list_attribute_group_associations`

**Issues:**
- Invalid method: Method 'list_attribute_group_associations' not found on client 'servicecatalog-appregistry'

### `aws_servicequotas_template`

- **Client:** `service-quotas`
- **Method:** `list_templates`

**Issues:**
- Invalid method: Method 'list_templates' not found on client 'service-quotas'

### `aws_servicequotas_template_association`

- **Client:** `service-quotas`
- **Method:** `list_template_associations`

**Issues:**
- Invalid method: Method 'list_template_associations' not found on client 'service-quotas'

### `aws_ses_configuration_set`

- **Client:** `ses`
- **Method:** `describe_configuration_sets`

**Issues:**
- Invalid method: Method 'describe_configuration_sets' not found. Similar methods: describe_configuration_set

### `aws_ses_domain_dkim`

- **Client:** `ses`
- **Method:** `describe_domain_dkim`

**Issues:**
- Invalid method: Method 'describe_domain_dkim' not found on client 'ses'

### `aws_ses_domain_identity`

- **Client:** `ses`
- **Method:** `describe_domain_identity`

**Issues:**
- Invalid method: Method 'describe_domain_identity' not found on client 'ses'

### `aws_ses_domain_identity_verification`

- **Client:** `ses`
- **Method:** `describe_domain_identity_verification`

**Issues:**
- Invalid method: Method 'describe_domain_identity_verification' not found on client 'ses'

### `aws_ses_domain_mail_from`

- **Client:** `ses`
- **Method:** `describe_domain_mail_from`

**Issues:**
- Invalid method: Method 'describe_domain_mail_from' not found on client 'ses'

### `aws_ses_email_identity`

- **Client:** `ses`
- **Method:** `describe_email_identity`

**Issues:**
- Invalid method: Method 'describe_email_identity' not found on client 'ses'

### `aws_ses_event_destination`

- **Client:** `ses`
- **Method:** `describe_event_destination`

**Issues:**
- Invalid method: Method 'describe_event_destination' not found on client 'ses'

### `aws_ses_identity_notification_topic`

- **Client:** `ses`
- **Method:** `describe_identity_notification_topic`

**Issues:**
- Invalid method: Method 'describe_identity_notification_topic' not found on client 'ses'

### `aws_ses_identity_policy`

- **Client:** `ses`
- **Method:** `describe_identity_policy`

**Issues:**
- Invalid method: Method 'describe_identity_policy' not found on client 'ses'

### `aws_ses_receipt_filter`

- **Client:** `ses`
- **Method:** `describe_receipt_filter`

**Issues:**
- Invalid method: Method 'describe_receipt_filter' not found on client 'ses'

### `aws_ses_template`

- **Client:** `ses`
- **Method:** `describe_template`

**Issues:**
- Invalid method: Method 'describe_template' not found on client 'ses'

### `aws_shield_application_layer_automatic_response`

- **Client:** `shield`
- **Method:** `list_application_layer_automatic_response_associations`

**Issues:**
- Invalid method: Method 'list_application_layer_automatic_response_associations' not found on client 'shield'

### `aws_shield_drt_access_log_bucket_association`

- **Client:** `shield`
- **Method:** `list_drt_access_log_bucket_associations`

**Issues:**
- Invalid method: Method 'list_drt_access_log_bucket_associations' not found on client 'shield'

### `aws_shield_drt_access_role_arn_association`

- **Client:** `shield`
- **Method:** `list_drt_access_role_arn_associations`

**Issues:**
- Invalid method: Method 'list_drt_access_role_arn_associations' not found on client 'shield'

### `aws_shield_protection_health_check_association`

- **Client:** `shield`
- **Method:** `list_protection_health_check_associations`

**Issues:**
- Invalid method: Method 'list_protection_health_check_associations' not found on client 'shield'

### `aws_snapshot_create_volume_permission`

- **Client:** `ec2`
- **Method:** `describe_create_volume_permissions`

**Issues:**
- Invalid method: Method 'describe_create_volume_permissions' not found. Similar methods: create_volume

### `aws_sns_sms_preferences`

- **Client:** `sns`
- **Method:** `get_sms_preferences`

**Issues:**
- Invalid method: Method 'get_sms_preferences' not found on client 'sns'

### `aws_ssm_patch_group`

- **Client:** `ssm`
- **Method:** `list_patch_groups`

**Issues:**
- Invalid method: Method 'list_patch_groups' not found on client 'ssm'

### `aws_ssmquicksetup_configuration_manager`

- **Client:** `ssmquicksetup`
- **Method:** `list_configuration_managers`

**Issues:**
- Invalid client: Unknown service: ssmquicksetup

### `aws_ssoadmin_application_assignment_configuration`

- **Client:** `sso-admin`
- **Method:** `list_application_assignment_configurations`

**Issues:**
- Invalid method: Method 'list_application_assignment_configurations' not found on client 'sso-admin'

### `aws_ssoadmin_customer_managed_policy_attachment`

- **Client:** `sso-admin`
- **Method:** `list_customer_managed_policy_attachments`

**Issues:**
- Invalid method: Method 'list_customer_managed_policy_attachments' not found on client 'sso-admin'

### `aws_ssoadmin_instance_access_control_attributes`

- **Client:** `sso-admin`
- **Method:** `list_instance_access_control_attribute_configuration`

**Issues:**
- Invalid method: Method 'list_instance_access_control_attribute_configuration' not found on client 'sso-admin'

### `aws_ssoadmin_managed_policy_attachment`

- **Client:** `sso-admin`
- **Method:** `list_managed_policy_attachments`

**Issues:**
- Invalid method: Method 'list_managed_policy_attachments' not found on client 'sso-admin'

### `aws_ssoadmin_permission_set_inline_policy`

- **Client:** `sso-admin`
- **Method:** `list_permission_set_inline_policies`

**Issues:**
- Invalid method: Method 'list_permission_set_inline_policies' not found on client 'sso-admin'

### `aws_ssoadmin_permissions_boundary_attachment`

- **Client:** `sso-admin`
- **Method:** `list_permissions_boundary_attachments`

**Issues:**
- Invalid method: Method 'list_permissions_boundary_attachments' not found on client 'sso-admin'

### `aws_storagegateway_gateway`

- **Client:** `storagegateway`
- **Method:** `describe_gateways`

**Issues:**
- Invalid method: Method 'describe_gateways' not found on client 'storagegateway'

### `aws_storagegateway_tape_pool`

- **Client:** `storagegateway`
- **Method:** `describe_tape_pools`

**Issues:**
- Invalid method: Method 'describe_tape_pools' not found on client 'storagegateway'

### `aws_synthetics_canary`

- **Client:** `synthetics`
- **Method:** `list_canaries`

**Issues:**
- Invalid method: Method 'list_canaries' not found on client 'synthetics'

### `aws_synthetics_group`

- **Client:** `synthetics`
- **Method:** `list_canary_groups`

**Issues:**
- Invalid method: Method 'list_canary_groups' not found on client 'synthetics'

### `aws_synthetics_group_association`

- **Client:** `synthetics`
- **Method:** `list_group_associations`

**Issues:**
- Invalid method: Method 'list_group_associations' not found on client 'synthetics'

### `aws_transfer_ssh_key`

- **Client:** `transfer`
- **Method:** `list_ssh_public_keys`

**Issues:**
- Invalid method: Method 'list_ssh_public_keys' not found on client 'transfer'

### `aws_transfer_tag`

- **Client:** `transfer`
- **Method:** `list_tags`

**Issues:**
- Invalid method: Method 'list_tags' not found. Similar methods: list_tags_for_resource

### `aws_vpc_dhcp_options_association`

- **Client:** `ec2`
- **Method:** `describe_dhcp_options_associations`

**Issues:**
- Invalid method: Method 'describe_dhcp_options_associations' not found. Similar methods: describe_dhcp_options

### `aws_vpc_endpoint_service_allowed_principal`

- **Client:** `ec2`
- **Method:** `describe_vpc_endpoint_service_allowed_principals`

**Issues:**
- Invalid method: Method 'describe_vpc_endpoint_service_allowed_principals' not found on client 'ec2'

### `aws_vpc_endpoint_subnet_association`

- **Client:** `ec2`
- **Method:** `describe_vpc_endpoint_subnet_associations`

**Issues:**
- Invalid method: Method 'describe_vpc_endpoint_subnet_associations' not found on client 'ec2'

### `aws_vpc_ipam_organization_admin_account`

- **Client:** `ec2`
- **Method:** `describe_ipam_organization_admin_accounts`

**Issues:**
- Invalid method: Method 'describe_ipam_organization_admin_accounts' not found on client 'ec2'

### `aws_vpc_ipam_preview_next_cidr`

- **Client:** `ec2`
- **Method:** `describe_ipam_preview_next_cidrs`

**Issues:**
- Invalid method: Method 'describe_ipam_preview_next_cidrs' not found on client 'ec2'

### `aws_vpc_network_performance_metric_subscription`

- **Client:** `ec2`
- **Method:** `describe_network_insights_path_subscriptions`

**Issues:**
- Invalid method: Method 'describe_network_insights_path_subscriptions' not found on client 'ec2'

### `aws_vpc_route_server_association`

- **Client:** `ec2`
- **Method:** `describe_route_server_associations`

**Issues:**
- Invalid method: Method 'describe_route_server_associations' not found on client 'ec2'

### `aws_vpc_route_server_propagation`

- **Client:** `ec2`
- **Method:** `describe_route_server_propagations`

**Issues:**
- Invalid method: Method 'describe_route_server_propagations' not found on client 'ec2'

### `aws_vpc_route_server_vpc_association`

- **Client:** `ec2`
- **Method:** `describe_route_server_vpc_associations`

**Issues:**
- Invalid method: Method 'describe_route_server_vpc_associations' not found on client 'ec2'

### `aws_vpclattice_resource_configuration`

- **Client:** `vpc-lattice`
- **Method:** `list_resource_configurations`

**Issues:**
- Invalid method: Method 'list_resource_configurations' not found on client 'vpc-lattice'

### `aws_vpclattice_resource_gateway`

- **Client:** `vpc-lattice`
- **Method:** `list_resource_gateways`

**Issues:**
- Invalid method: Method 'list_resource_gateways' not found on client 'vpc-lattice'

### `aws_vpclattice_service_network_resource_association`

- **Client:** `vpc-lattice`
- **Method:** `list_service_network_resource_associations`

**Issues:**
- Invalid method: Method 'list_service_network_resource_associations' not found on client 'vpc-lattice'

### `aws_vpclattice_target_group_attachment`

- **Client:** `vpc-lattice`
- **Method:** `list_target_group_attachments`

**Issues:**
- Invalid method: Method 'list_target_group_attachments' not found on client 'vpc-lattice'

### `aws_vpn_connection_route`

- **Client:** `ec2`
- **Method:** `describe_vpn_connection_routes`

**Issues:**
- Invalid method: Method 'describe_vpn_connection_routes' not found on client 'ec2'

### `aws_vpn_gateway_attachment`

- **Client:** `ec2`
- **Method:** `describe_vpn_gateway_attachments`

**Issues:**
- Invalid method: Method 'describe_vpn_gateway_attachments' not found on client 'ec2'

### `aws_vpn_gateway_route_propagation`

- **Client:** `ec2`
- **Method:** `describe_vpn_gateway_route_propagations`

**Issues:**
- Invalid method: Method 'describe_vpn_gateway_route_propagations' not found on client 'ec2'

### `aws_wafregional_web_acl_association`

- **Client:** `waf-regional`
- **Method:** `list_web_acl_associations`

**Issues:**
- Invalid method: Method 'list_web_acl_associations' not found on client 'waf-regional'

### `aws_worklink_fleet`

- **Client:** `worklink`
- **Method:** `list_fleets`

**Issues:**
- Invalid client: Unknown service: worklink

### `aws_worklink_website_certificate_authority_association`

- **Client:** `worklink`
- **Method:** `list_website_certificate_authorities`

**Issues:**
- Invalid client: Unknown service: worklink

### `aws_xray_resource_policy`

- **Client:** `xray`
- **Method:** `get_resource_policy`

**Issues:**
- Invalid method: Method 'get_resource_policy' not found on client 'xray'

## ⚠️  Warnings

These resources may have minor issues or require special handling:

### `aws_account_alternate_contact`

- **Client:** `organizations`
- **Method:** `describe_account`

**Warnings:**
- Method 'describe_account' is not pageable (may need direct API call)

### `aws_account_primary_contact`

- **Client:** `organizations`
- **Method:** `describe_account`

**Warnings:**
- Method 'describe_account' is not pageable (may need direct API call)

### `aws_account_region`

- **Client:** `ec2`
- **Method:** `describe_regions`

**Warnings:**
- Method 'describe_regions' is not pageable (may need direct API call)

### `aws_acmpca_certificate`

- **Client:** `acm-pca`
- **Method:** `get_certificate`

**Warnings:**
- Method 'get_certificate' is not pageable (may need direct API call)

### `aws_acmpca_policy`

- **Client:** `acm-pca`
- **Method:** `get_policy`

**Warnings:**
- Method 'get_policy' is not pageable (may need direct API call)

### `aws_ami_launch_permission`

- **Client:** `ec2`
- **Method:** `describe_image_attribute`

**Warnings:**
- Method 'describe_image_attribute' is not pageable (may need direct API call)

### `aws_amplify_backend_environment`

- **Client:** `amplify`
- **Method:** `list_backend_environments`

**Warnings:**
- Method 'list_backend_environments' is not pageable (may need direct API call)

### `aws_amplify_webhook`

- **Client:** `amplify`
- **Method:** `list_webhooks`

**Warnings:**
- Method 'list_webhooks' is not pageable (may need direct API call)

### `aws_api_gateway_account`

- **Client:** `apigateway`
- **Method:** `get_account`

**Warnings:**
- Method 'get_account' is not pageable (may need direct API call)

### `aws_api_gateway_domain_name_access_association`

- **Client:** `apigateway`
- **Method:** `get_domain_name_access_associations`

**Warnings:**
- Method 'get_domain_name_access_associations' is not pageable (may need direct API call)

### `aws_api_gateway_integration`

- **Client:** `apigateway`
- **Method:** `get_integration`

**Warnings:**
- Method 'get_integration' is not pageable (may need direct API call)

### `aws_api_gateway_integration_response`

- **Client:** `apigateway`
- **Method:** `get_integration_response`

**Warnings:**
- Method 'get_integration_response' is not pageable (may need direct API call)

### `aws_api_gateway_method`

- **Client:** `apigateway`
- **Method:** `get_method`

**Warnings:**
- Method 'get_method' is not pageable (may need direct API call)

### `aws_api_gateway_method_response`

- **Client:** `apigateway`
- **Method:** `get_method_response`

**Warnings:**
- Method 'get_method_response' is not pageable (may need direct API call)

### `aws_api_gateway_method_settings`

- **Client:** `apigateway`
- **Method:** `get_stage`

**Warnings:**
- Method 'get_stage' is not pageable (may need direct API call)

### `aws_api_gateway_rest_api_policy`

- **Client:** `apigateway`
- **Method:** `get_rest_api`

**Warnings:**
- Method 'get_rest_api' is not pageable (may need direct API call)

### `aws_api_gateway_stage`

- **Client:** `apigateway`
- **Method:** `get_stages`

**Warnings:**
- Method 'get_stages' is not pageable (may need direct API call)

### `aws_apigatewayv2_api_mapping`

- **Client:** `apigatewayv2`
- **Method:** `get_api_mappings`

**Warnings:**
- Method 'get_api_mappings' is not pageable (may need direct API call)

### `aws_apigatewayv2_vpc_link`

- **Client:** `apigatewayv2`
- **Method:** `get_vpc_links`

**Warnings:**
- Method 'get_vpc_links' is not pageable (may need direct API call)

### `aws_appflow_connector_profile`

- **Client:** `appflow`
- **Method:** `describe_connector_profiles`

**Warnings:**
- Method 'describe_connector_profiles' is not pageable (may need direct API call)

### `aws_appflow_flow`

- **Client:** `appflow`
- **Method:** `list_flows`

**Warnings:**
- Method 'list_flows' is not pageable (may need direct API call)

### `aws_applicationinsights_application`

- **Client:** `application-insights`
- **Method:** `list_applications`

**Warnings:**
- Method 'list_applications' is not pageable (may need direct API call)

### `aws_apprunner_auto_scaling_configuration_version`

- **Client:** `apprunner`
- **Method:** `describe_auto_scaling_configuration`

**Warnings:**
- Method 'describe_auto_scaling_configuration' is not pageable (may need direct API call)

### `aws_apprunner_connection`

- **Client:** `apprunner`
- **Method:** `list_connections`

**Warnings:**
- Method 'list_connections' is not pageable (may need direct API call)

### `aws_apprunner_custom_domain_association`

- **Client:** `apprunner`
- **Method:** `describe_custom_domains`

**Warnings:**
- Method 'describe_custom_domains' is not pageable (may need direct API call)

### `aws_apprunner_default_auto_scaling_configuration_version`

- **Client:** `apprunner`
- **Method:** `describe_auto_scaling_configuration`

**Warnings:**
- Method 'describe_auto_scaling_configuration' is not pageable (may need direct API call)

### `aws_apprunner_deployment`

- **Client:** `apprunner`
- **Method:** `list_operations`

**Warnings:**
- Method 'list_operations' is not pageable (may need direct API call)

### `aws_apprunner_observability_configuration`

- **Client:** `apprunner`
- **Method:** `list_observability_configurations`

**Warnings:**
- Method 'list_observability_configurations' is not pageable (may need direct API call)

### `aws_apprunner_service`

- **Client:** `apprunner`
- **Method:** `list_services`

**Warnings:**
- Method 'list_services' is not pageable (may need direct API call)

### `aws_apprunner_vpc_connector`

- **Client:** `apprunner`
- **Method:** `list_vpc_connectors`

**Warnings:**
- Method 'list_vpc_connectors' is not pageable (may need direct API call)

### `aws_apprunner_vpc_ingress_connection`

- **Client:** `apprunner`
- **Method:** `list_vpc_ingress_connections`

**Warnings:**
- Method 'list_vpc_ingress_connections' is not pageable (may need direct API call)

### `aws_appsync_api_cache`

- **Client:** `appsync`
- **Method:** `get_api_cache`

**Warnings:**
- Method 'get_api_cache' is not pageable (may need direct API call)

### `aws_appsync_domain_name_api_association`

- **Client:** `appsync`
- **Method:** `get_domain_name`

**Warnings:**
- Method 'get_domain_name' is not pageable (may need direct API call)

### `aws_athena_capacity_reservation`

- **Client:** `athena`
- **Method:** `list_capacity_reservations`

**Warnings:**
- Method 'list_capacity_reservations' is not pageable (may need direct API call)

### `aws_athena_prepared_statement`

- **Client:** `athena`
- **Method:** `list_prepared_statements`

**Warnings:**
- Method 'list_prepared_statements' is not pageable (may need direct API call)

### `aws_athena_workgroup`

- **Client:** `athena`
- **Method:** `get_work_group`

**Warnings:**
- Method 'get_work_group' is not pageable (may need direct API call)

### `aws_auditmanager_account_registration`

- **Client:** `auditmanager`
- **Method:** `get_account_status`

**Warnings:**
- Method 'get_account_status' is not pageable (may need direct API call)

### `aws_auditmanager_assessment`

- **Client:** `auditmanager`
- **Method:** `list_assessments`

**Warnings:**
- Method 'list_assessments' is not pageable (may need direct API call)

### `aws_auditmanager_assessment_delegation`

- **Client:** `auditmanager`
- **Method:** `get_delegations`

**Warnings:**
- Method 'get_delegations' is not pageable (may need direct API call)

### `aws_auditmanager_assessment_report`

- **Client:** `auditmanager`
- **Method:** `list_assessment_reports`

**Warnings:**
- Method 'list_assessment_reports' is not pageable (may need direct API call)

### `aws_auditmanager_control`

- **Client:** `auditmanager`
- **Method:** `list_controls`

**Warnings:**
- Method 'list_controls' is not pageable (may need direct API call)

### `aws_auditmanager_framework`

- **Client:** `auditmanager`
- **Method:** `list_assessment_frameworks`

**Warnings:**
- Method 'list_assessment_frameworks' is not pageable (may need direct API call)

### `aws_auditmanager_framework_share`

- **Client:** `auditmanager`
- **Method:** `list_assessment_framework_share_requests`

**Warnings:**
- Method 'list_assessment_framework_share_requests' is not pageable (may need direct API call)

### `aws_auditmanager_organization_admin_account_registration`

- **Client:** `auditmanager`
- **Method:** `get_organization_admin_account`

**Warnings:**
- Method 'get_organization_admin_account' is not pageable (may need direct API call)

### `aws_autoscaling_lifecycle_hook`

- **Client:** `autoscaling`
- **Method:** `describe_lifecycle_hooks`

**Warnings:**
- Method 'describe_lifecycle_hooks' is not pageable (may need direct API call)

### `aws_autoscaling_traffic_source_attachment`

- **Client:** `autoscaling`
- **Method:** `describe_traffic_sources`

**Warnings:**
- Method 'describe_traffic_sources' is not pageable (may need direct API call)

### `aws_backup_framework`

- **Client:** `backup`
- **Method:** `list_frameworks`

**Warnings:**
- Method 'list_frameworks' is not pageable (may need direct API call)

### `aws_backup_global_settings`

- **Client:** `backup`
- **Method:** `describe_global_settings`

**Warnings:**
- Method 'describe_global_settings' is not pageable (may need direct API call)

### `aws_backup_region_settings`

- **Client:** `backup`
- **Method:** `describe_region_settings`

**Warnings:**
- Method 'describe_region_settings' is not pageable (may need direct API call)

### `aws_backup_report_plan`

- **Client:** `backup`
- **Method:** `list_report_plans`

**Warnings:**
- Method 'list_report_plans' is not pageable (may need direct API call)

### `aws_backup_vault_lock_configuration`

- **Client:** `backup`
- **Method:** `describe_backup_vault`

**Warnings:**
- Method 'describe_backup_vault' is not pageable (may need direct API call)

### `aws_backup_vault_notifications`

- **Client:** `backup`
- **Method:** `get_backup_vault_notifications`

**Warnings:**
- Method 'get_backup_vault_notifications' is not pageable (may need direct API call)

### `aws_backup_vault_policy`

- **Client:** `backup`
- **Method:** `get_backup_vault_access_policy`

**Warnings:**
- Method 'get_backup_vault_access_policy' is not pageable (may need direct API call)

### `aws_bedrock_model_invocation_logging_configuration`

- **Client:** `bedrock`
- **Method:** `get_model_invocation_logging_configuration`

**Warnings:**
- Method 'get_model_invocation_logging_configuration' is not pageable (may need direct API call)

### `aws_bedrockagentcore_token_vault_cmk`

- **Client:** `bedrock-agentcore-control`
- **Method:** `get_token_vault`

**Warnings:**
- Method 'get_token_vault' is not pageable (may need direct API call)

### `aws_chime_voice_connector`

- **Client:** `chime-sdk-voice`
- **Method:** `list_voice_connectors`

**Warnings:**
- Method 'list_voice_connectors' is not pageable (may need direct API call)

### `aws_chime_voice_connector_group`

- **Client:** `chime-sdk-voice`
- **Method:** `list_voice_connector_groups`

**Warnings:**
- Method 'list_voice_connector_groups' is not pageable (may need direct API call)

### `aws_chime_voice_connector_logging`

- **Client:** `chime-sdk-voice`
- **Method:** `get_voice_connector_logging_configuration`

**Warnings:**
- Method 'get_voice_connector_logging_configuration' is not pageable (may need direct API call)

### `aws_chime_voice_connector_origination`

- **Client:** `chime-sdk-voice`
- **Method:** `get_voice_connector_origination`

**Warnings:**
- Method 'get_voice_connector_origination' is not pageable (may need direct API call)

### `aws_chime_voice_connector_streaming`

- **Client:** `chime-sdk-voice`
- **Method:** `get_voice_connector_streaming_configuration`

**Warnings:**
- Method 'get_voice_connector_streaming_configuration' is not pageable (may need direct API call)

### `aws_chime_voice_connector_termination`

- **Client:** `chime-sdk-voice`
- **Method:** `get_voice_connector_termination`

**Warnings:**
- Method 'get_voice_connector_termination' is not pageable (may need direct API call)

### `aws_chime_voice_connector_termination_credentials`

- **Client:** `chime-sdk-voice`
- **Method:** `list_voice_connector_termination_credentials`

**Warnings:**
- Method 'list_voice_connector_termination_credentials' is not pageable (may need direct API call)

### `aws_chimesdkmediapipelines_media_insights_pipeline_configuration`

- **Client:** `chime-sdk-media-pipelines`
- **Method:** `list_media_insights_pipeline_configurations`

**Warnings:**
- Method 'list_media_insights_pipeline_configurations' is not pageable (may need direct API call)

### `aws_chimesdkvoice_global_settings`

- **Client:** `chime-sdk-voice`
- **Method:** `get_global_settings`

**Warnings:**
- Method 'get_global_settings' is not pageable (may need direct API call)

### `aws_chimesdkvoice_voice_profile_domain`

- **Client:** `chime-sdk-voice`
- **Method:** `list_voice_profile_domains`

**Warnings:**
- Method 'list_voice_profile_domains' is not pageable (may need direct API call)

### `aws_cloudfront_cache_policy`

- **Client:** `cloudfront`
- **Method:** `list_cache_policies`

**Warnings:**
- Method 'list_cache_policies' is not pageable (may need direct API call)

### `aws_cloudfront_continuous_deployment_policy`

- **Client:** `cloudfront`
- **Method:** `list_continuous_deployment_policies`

**Warnings:**
- Method 'list_continuous_deployment_policies' is not pageable (may need direct API call)

### `aws_cloudfront_field_level_encryption_config`

- **Client:** `cloudfront`
- **Method:** `list_field_level_encryption_configs`

**Warnings:**
- Method 'list_field_level_encryption_configs' is not pageable (may need direct API call)

### `aws_cloudfront_field_level_encryption_profile`

- **Client:** `cloudfront`
- **Method:** `list_field_level_encryption_profiles`

**Warnings:**
- Method 'list_field_level_encryption_profiles' is not pageable (may need direct API call)

### `aws_cloudfront_function`

- **Client:** `cloudfront`
- **Method:** `list_functions`

**Warnings:**
- Method 'list_functions' is not pageable (may need direct API call)

### `aws_cloudfront_key_group`

- **Client:** `cloudfront`
- **Method:** `list_key_groups`

**Warnings:**
- Method 'list_key_groups' is not pageable (may need direct API call)

### `aws_cloudfront_monitoring_subscription`

- **Client:** `cloudfront`
- **Method:** `get_monitoring_subscription`

**Warnings:**
- Method 'get_monitoring_subscription' is not pageable (may need direct API call)

### `aws_cloudfront_realtime_log_config`

- **Client:** `cloudfront`
- **Method:** `list_realtime_log_configs`

**Warnings:**
- Method 'list_realtime_log_configs' is not pageable (may need direct API call)

### `aws_cloudfront_response_headers_policy`

- **Client:** `cloudfront`
- **Method:** `list_response_headers_policies`

**Warnings:**
- Method 'list_response_headers_policies' is not pageable (may need direct API call)

### `aws_cloudfront_vpc_origin`

- **Client:** `cloudfront`
- **Method:** `list_vpc_origins`

**Warnings:**
- Method 'list_vpc_origins' is not pageable (may need direct API call)

### `aws_cloudsearch_domain`

- **Client:** `cloudsearch`
- **Method:** `describe_domains`

**Warnings:**
- Method 'describe_domains' is not pageable (may need direct API call)

### `aws_cloudsearch_domain_service_access_policy`

- **Client:** `cloudsearch`
- **Method:** `describe_service_access_policies`

**Warnings:**
- Method 'describe_service_access_policies' is not pageable (may need direct API call)

### `aws_cloudtrail_event_data_store`

- **Client:** `cloudtrail`
- **Method:** `list_event_data_stores`

**Warnings:**
- Method 'list_event_data_stores' is not pageable (may need direct API call)

### `aws_cloudwatch_contributor_insight_rule`

- **Client:** `cloudwatch`
- **Method:** `describe_insight_rules`

**Warnings:**
- Method 'describe_insight_rules' is not pageable (may need direct API call)

### `aws_cloudwatch_contributor_managed_insight_rule`

- **Client:** `cloudwatch`
- **Method:** `describe_insight_rules`

**Warnings:**
- Method 'describe_insight_rules' is not pageable (may need direct API call)

### `aws_cloudwatch_event_api_destination`

- **Client:** `events`
- **Method:** `list_api_destinations`

**Warnings:**
- Method 'list_api_destinations' is not pageable (may need direct API call)

### `aws_cloudwatch_event_archive`

- **Client:** `events`
- **Method:** `list_archives`

**Warnings:**
- Method 'list_archives' is not pageable (may need direct API call)

### `aws_cloudwatch_event_bus`

- **Client:** `events`
- **Method:** `list_event_buses`

**Warnings:**
- Method 'list_event_buses' is not pageable (may need direct API call)

### `aws_cloudwatch_event_bus_policy`

- **Client:** `events`
- **Method:** `describe_event_bus`

**Warnings:**
- Method 'describe_event_bus' is not pageable (may need direct API call)

### `aws_cloudwatch_event_connection`

- **Client:** `events`
- **Method:** `list_connections`

**Warnings:**
- Method 'list_connections' is not pageable (may need direct API call)

### `aws_cloudwatch_event_endpoint`

- **Client:** `events`
- **Method:** `list_endpoints`

**Warnings:**
- Method 'list_endpoints' is not pageable (may need direct API call)

### `aws_cloudwatch_event_permission`

- **Client:** `events`
- **Method:** `describe_event_bus`

**Warnings:**
- Method 'describe_event_bus' is not pageable (may need direct API call)

### `aws_cloudwatch_log_account_policy`

- **Client:** `logs`
- **Method:** `describe_account_policies`

**Warnings:**
- Method 'describe_account_policies' is not pageable (may need direct API call)

### `aws_cloudwatch_log_data_protection_policy`

- **Client:** `logs`
- **Method:** `get_data_protection_policy`

**Warnings:**
- Method 'get_data_protection_policy' is not pageable (may need direct API call)

### `aws_cloudwatch_log_delivery_destination_policy`

- **Client:** `logs`
- **Method:** `get_delivery_destination_policy`

**Warnings:**
- Method 'get_delivery_destination_policy' is not pageable (may need direct API call)

### `aws_cloudwatch_log_index_policy`

- **Client:** `logs`
- **Method:** `describe_index_policies`

**Warnings:**
- Method 'describe_index_policies' is not pageable (may need direct API call)

### `aws_cloudwatch_log_transformer`

- **Client:** `logs`
- **Method:** `get_transformer`

**Warnings:**
- Method 'get_transformer' is not pageable (may need direct API call)

### `aws_cloudwatch_metric_stream`

- **Client:** `cloudwatch`
- **Method:** `list_metric_streams`

**Warnings:**
- Method 'list_metric_streams' is not pageable (may need direct API call)

### `aws_cloudwatch_query_definition`

- **Client:** `logs`
- **Method:** `describe_query_definitions`

**Warnings:**
- Method 'describe_query_definitions' is not pageable (may need direct API call)

### `aws_codeartifact_domain_permissions_policy`

- **Client:** `codeartifact`
- **Method:** `get_domain_permissions_policy`

**Warnings:**
- Method 'get_domain_permissions_policy' is not pageable (may need direct API call)

### `aws_codeartifact_repository_permissions_policy`

- **Client:** `codeartifact`
- **Method:** `get_repository_permissions_policy`

**Warnings:**
- Method 'get_repository_permissions_policy' is not pageable (may need direct API call)

### `aws_codebuild_fleet`

- **Client:** `codebuild`
- **Method:** `list_fleets`

**Warnings:**
- Method 'list_fleets' is not pageable (may need direct API call)

### `aws_codebuild_project`

- **Client:** `codebuild`
- **Method:** `list_projects`

**Warnings:**
- Missing 'key' field

### `aws_codebuild_resource_policy`

- **Client:** `codebuild`
- **Method:** `get_resource_policy`

**Warnings:**
- Method 'get_resource_policy' is not pageable (may need direct API call)

### `aws_codebuild_source_credential`

- **Client:** `codebuild`
- **Method:** `list_source_credentials`

**Warnings:**
- Method 'list_source_credentials' is not pageable (may need direct API call)

### `aws_codebuild_webhook`

- **Client:** `codebuild`
- **Method:** `batch_get_projects`

**Warnings:**
- Method 'batch_get_projects' is not pageable (may need direct API call)

### `aws_codecommit_approval_rule_template`

- **Client:** `codecommit`
- **Method:** `list_approval_rule_templates`

**Warnings:**
- Method 'list_approval_rule_templates' is not pageable (may need direct API call)

### `aws_codecommit_approval_rule_template_association`

- **Client:** `codecommit`
- **Method:** `list_associated_approval_rule_templates_for_repository`

**Warnings:**
- Method 'list_associated_approval_rule_templates_for_repository' is not pageable (may need direct API call)

### `aws_codecommit_trigger`

- **Client:** `codecommit`
- **Method:** `get_repository_triggers`

**Warnings:**
- Method 'get_repository_triggers' is not pageable (may need direct API call)

### `aws_codeconnections_connection`

- **Client:** `codeconnections`
- **Method:** `list_connections`

**Warnings:**
- Method 'list_connections' is not pageable (may need direct API call)

### `aws_codeconnections_host`

- **Client:** `codeconnections`
- **Method:** `list_hosts`

**Warnings:**
- Method 'list_hosts' is not pageable (may need direct API call)

### `aws_codeguruprofiler_profiling_group`

- **Client:** `codeguruprofiler`
- **Method:** `list_profiling_groups`

**Warnings:**
- Method 'list_profiling_groups' is not pageable (may need direct API call)

### `aws_codestarconnections_connection`

- **Client:** `codestar-connections`
- **Method:** `list_connections`

**Warnings:**
- Method 'list_connections' is not pageable (may need direct API call)

### `aws_codestarconnections_host`

- **Client:** `codestar-connections`
- **Method:** `list_hosts`

**Warnings:**
- Method 'list_hosts' is not pageable (may need direct API call)

### `aws_cognito_identity_pool_provider_principal_tag`

- **Client:** `cognito-identity`
- **Method:** `get_principal_tag_attribute_map`

**Warnings:**
- Method 'get_principal_tag_attribute_map' is not pageable (may need direct API call)

### `aws_cognito_identity_pool_roles_attachment`

- **Client:** `cognito-identity`
- **Method:** `get_identity_pool_roles`

**Warnings:**
- Method 'get_identity_pool_roles' is not pageable (may need direct API call)

### `aws_cognito_log_delivery_configuration`

- **Client:** `cognito-idp`
- **Method:** `get_log_delivery_configuration`

**Warnings:**
- Method 'get_log_delivery_configuration' is not pageable (may need direct API call)

### `aws_cognito_managed_login_branding`

- **Client:** `cognito-idp`
- **Method:** `describe_managed_login_branding`

**Warnings:**
- Method 'describe_managed_login_branding' is not pageable (may need direct API call)

### `aws_cognito_risk_configuration`

- **Client:** `cognito-idp`
- **Method:** `describe_risk_configuration`

**Warnings:**
- Method 'describe_risk_configuration' is not pageable (may need direct API call)

### `aws_cognito_user_pool_domain`

- **Client:** `cognito-idp`
- **Method:** `describe_user_pool_domain`

**Warnings:**
- Method 'describe_user_pool_domain' is not pageable (may need direct API call)

### `aws_cognito_user_pool_ui_customization`

- **Client:** `cognito-idp`
- **Method:** `get_ui_customization`

**Warnings:**
- Method 'get_ui_customization' is not pageable (may need direct API call)

### `aws_computeoptimizer_enrollment_status`

- **Client:** `compute-optimizer`
- **Method:** `get_enrollment_status`

**Warnings:**
- Method 'get_enrollment_status' is not pageable (may need direct API call)

### `aws_config_configuration_recorder`

- **Client:** `config`
- **Method:** `describe_configuration_recorders`

**Warnings:**
- Method 'describe_configuration_recorders' is not pageable (may need direct API call)

### `aws_config_configuration_recorder_status`

- **Client:** `config`
- **Method:** `describe_configuration_recorder_status`

**Warnings:**
- Method 'describe_configuration_recorder_status' is not pageable (may need direct API call)

### `aws_config_delivery_channel`

- **Client:** `config`
- **Method:** `describe_delivery_channels`

**Warnings:**
- Method 'describe_delivery_channels' is not pageable (may need direct API call)

### `aws_config_remediation_configuration`

- **Client:** `config`
- **Method:** `describe_remediation_configurations`

**Warnings:**
- Method 'describe_remediation_configurations' is not pageable (may need direct API call)

### `aws_connect_lambda_function_association`

- **Client:** `connect`
- **Method:** `list_lambda_functions`

**Warnings:**
- Missing 'key' field

### `aws_connect_user_hierarchy_structure`

- **Client:** `connect`
- **Method:** `describe_user_hierarchy_structure`

**Warnings:**
- Method 'describe_user_hierarchy_structure' is not pageable (may need direct API call)

### `aws_costoptimizationhub_enrollment_status`

- **Client:** `cost-optimization-hub`
- **Method:** `get_preferences`

**Warnings:**
- Method 'get_preferences' is not pageable (may need direct API call)

### `aws_costoptimizationhub_preferences`

- **Client:** `cost-optimization-hub`
- **Method:** `get_preferences`

**Warnings:**
- Method 'get_preferences' is not pageable (may need direct API call)

### `aws_customer_gateway`

- **Client:** `ec2`
- **Method:** `describe_customer_gateways`

**Warnings:**
- Method 'describe_customer_gateways' is not pageable (may need direct API call)

### `aws_customerprofiles_domain`

- **Client:** `customer-profiles`
- **Method:** `list_domains`

**Warnings:**
- Method 'list_domains' is not pageable (may need direct API call)

### `aws_customerprofiles_profile`

- **Client:** `customer-profiles`
- **Method:** `search_profiles`

**Warnings:**
- Method 'search_profiles' is not pageable (may need direct API call)

### `aws_datapipeline_pipeline_definition`

- **Client:** `datapipeline`
- **Method:** `get_pipeline_definition`

**Warnings:**
- Method 'get_pipeline_definition' is not pageable (may need direct API call)

### `aws_db_snapshot_copy`

- **Client:** `rds`
- **Method:** `describe_db_snapshot_attributes`

**Warnings:**
- Method 'describe_db_snapshot_attributes' is not pageable (may need direct API call)

### `aws_detective_graph`

- **Client:** `detective`
- **Method:** `list_graphs`

**Warnings:**
- Method 'list_graphs' is not pageable (may need direct API call)

### `aws_detective_invitation_accepter`

- **Client:** `detective`
- **Method:** `list_invitations`

**Warnings:**
- Method 'list_invitations' is not pageable (may need direct API call)

### `aws_detective_member`

- **Client:** `detective`
- **Method:** `list_members`

**Warnings:**
- Method 'list_members' is not pageable (may need direct API call)

### `aws_detective_organization_admin_account`

- **Client:** `detective`
- **Method:** `list_organization_admin_accounts`

**Warnings:**
- Method 'list_organization_admin_accounts' is not pageable (may need direct API call)

### `aws_detective_organization_configuration`

- **Client:** `detective`
- **Method:** `describe_organization_configuration`

**Warnings:**
- Method 'describe_organization_configuration' is not pageable (may need direct API call)

### `aws_devicefarm_test_grid_project`

- **Client:** `devicefarm`
- **Method:** `list_test_grid_projects`

**Warnings:**
- Method 'list_test_grid_projects' is not pageable (may need direct API call)

### `aws_devopsguru_event_sources_config`

- **Client:** `devops-guru`
- **Method:** `describe_event_sources_config`

**Warnings:**
- Method 'describe_event_sources_config' is not pageable (may need direct API call)

### `aws_devopsguru_service_integration`

- **Client:** `devops-guru`
- **Method:** `describe_service_integration`

**Warnings:**
- Method 'describe_service_integration' is not pageable (may need direct API call)

### `aws_directory_service_conditional_forwarder`

- **Client:** `ds`
- **Method:** `describe_conditional_forwarders`

**Warnings:**
- Method 'describe_conditional_forwarders' is not pageable (may need direct API call)

### `aws_dlm_lifecycle_policy`

- **Client:** `dlm`
- **Method:** `get_lifecycle_policies`

**Warnings:**
- Method 'get_lifecycle_policies' is not pageable (may need direct API call)

### `aws_dms_replication_config`

- **Client:** `dms`
- **Method:** `describe_replication_configs`

**Warnings:**
- Method 'describe_replication_configs' is not pageable (may need direct API call)

### `aws_dx_bgp_peer`

- **Client:** `directconnect`
- **Method:** `describe_virtual_interfaces`

**Warnings:**
- Method 'describe_virtual_interfaces' is not pageable (may need direct API call)

### `aws_dx_connection`

- **Client:** `directconnect`
- **Method:** `describe_connections`

**Warnings:**
- Method 'describe_connections' is not pageable (may need direct API call)

### `aws_dx_connection_association`

- **Client:** `directconnect`
- **Method:** `describe_connections`

**Warnings:**
- Method 'describe_connections' is not pageable (may need direct API call)

### `aws_dx_connection_confirmation`

- **Client:** `directconnect`
- **Method:** `describe_connections`

**Warnings:**
- Method 'describe_connections' is not pageable (may need direct API call)

### `aws_dx_gateway_association_proposal`

- **Client:** `directconnect`
- **Method:** `describe_direct_connect_gateway_association_proposals`

**Warnings:**
- Method 'describe_direct_connect_gateway_association_proposals' is not pageable (may need direct API call)
- Missing 'topkey' field

### `aws_dx_hosted_connection`

- **Client:** `directconnect`
- **Method:** `describe_connections`

**Warnings:**
- Method 'describe_connections' is not pageable (may need direct API call)

### `aws_dx_hosted_private_virtual_interface`

- **Client:** `directconnect`
- **Method:** `describe_virtual_interfaces`

**Warnings:**
- Method 'describe_virtual_interfaces' is not pageable (may need direct API call)

### `aws_dx_hosted_private_virtual_interface_accepter`

- **Client:** `directconnect`
- **Method:** `describe_virtual_interfaces`

**Warnings:**
- Method 'describe_virtual_interfaces' is not pageable (may need direct API call)

### `aws_dx_hosted_public_virtual_interface`

- **Client:** `directconnect`
- **Method:** `describe_virtual_interfaces`

**Warnings:**
- Method 'describe_virtual_interfaces' is not pageable (may need direct API call)

### `aws_dx_hosted_public_virtual_interface_accepter`

- **Client:** `directconnect`
- **Method:** `describe_virtual_interfaces`

**Warnings:**
- Method 'describe_virtual_interfaces' is not pageable (may need direct API call)

### `aws_dx_hosted_transit_virtual_interface`

- **Client:** `directconnect`
- **Method:** `describe_virtual_interfaces`

**Warnings:**
- Method 'describe_virtual_interfaces' is not pageable (may need direct API call)

### `aws_dx_hosted_transit_virtual_interface_accepter`

- **Client:** `directconnect`
- **Method:** `describe_virtual_interfaces`

**Warnings:**
- Method 'describe_virtual_interfaces' is not pageable (may need direct API call)

### `aws_dx_lag`

- **Client:** `directconnect`
- **Method:** `describe_lags`

**Warnings:**
- Method 'describe_lags' is not pageable (may need direct API call)

### `aws_dx_macsec_key_association`

- **Client:** `directconnect`
- **Method:** `describe_connections`

**Warnings:**
- Method 'describe_connections' is not pageable (may need direct API call)

### `aws_dx_private_virtual_interface`

- **Client:** `directconnect`
- **Method:** `describe_virtual_interfaces`

**Warnings:**
- Method 'describe_virtual_interfaces' is not pageable (may need direct API call)

### `aws_dx_public_virtual_interface`

- **Client:** `directconnect`
- **Method:** `describe_virtual_interfaces`

**Warnings:**
- Method 'describe_virtual_interfaces' is not pageable (may need direct API call)

### `aws_dx_transit_virtual_interface`

- **Client:** `directconnect`
- **Method:** `describe_virtual_interfaces`

**Warnings:**
- Method 'describe_virtual_interfaces' is not pageable (may need direct API call)

### `aws_dynamodb_contributor_insights`

- **Client:** `dynamodb`
- **Method:** `describe_contributor_insights`

**Warnings:**
- Method 'describe_contributor_insights' is not pageable (may need direct API call)

### `aws_dynamodb_global_table`

- **Client:** `dynamodb`
- **Method:** `list_global_tables`

**Warnings:**
- Method 'list_global_tables' is not pageable (may need direct API call)

### `aws_dynamodb_kinesis_streaming_destination`

- **Client:** `dynamodb`
- **Method:** `describe_kinesis_streaming_destination`

**Warnings:**
- Method 'describe_kinesis_streaming_destination' is not pageable (may need direct API call)

### `aws_dynamodb_resource_policy`

- **Client:** `dynamodb`
- **Method:** `get_resource_policy`

**Warnings:**
- Method 'get_resource_policy' is not pageable (may need direct API call)

### `aws_dynamodb_table`

- **Client:** `dynamodb`
- **Method:** `describe_table`

**Warnings:**
- Method 'describe_table' is not pageable (may need direct API call)

### `aws_dynamodb_table_export`

- **Client:** `dynamodb`
- **Method:** `list_exports`

**Warnings:**
- Method 'list_exports' is not pageable (may need direct API call)

### `aws_dynamodb_table_item`

- **Client:** `dynamodb`
- **Method:** `describe_table`

**Warnings:**
- Method 'describe_table' is not pageable (may need direct API call)

### `aws_dynamodb_table_replica`

- **Client:** `dynamodb`
- **Method:** `describe_table_replica_auto_scaling`

**Warnings:**
- Method 'describe_table_replica_auto_scaling' is not pageable (may need direct API call)

### `aws_ebs_default_kms_key`

- **Client:** `ec2`
- **Method:** `get_ebs_default_kms_key_id`

**Warnings:**
- Method 'get_ebs_default_kms_key_id' is not pageable (may need direct API call)

### `aws_ebs_encryption_by_default`

- **Client:** `ec2`
- **Method:** `get_ebs_encryption_by_default`

**Warnings:**
- Method 'get_ebs_encryption_by_default' is not pageable (may need direct API call)

### `aws_ebs_snapshot_block_public_access`

- **Client:** `ec2`
- **Method:** `get_snapshot_block_public_access_state`

**Warnings:**
- Method 'get_snapshot_block_public_access_state' is not pageable (may need direct API call)

### `aws_ec2_allowed_images_settings`

- **Client:** `ec2`
- **Method:** `get_allowed_images_settings`

**Warnings:**
- Method 'get_allowed_images_settings' is not pageable (may need direct API call)

### `aws_ec2_availability_zone_group`

- **Client:** `ec2`
- **Method:** `describe_availability_zones`

**Warnings:**
- Method 'describe_availability_zones' is not pageable (may need direct API call)

### `aws_ec2_image_block_public_access`

- **Client:** `ec2`
- **Method:** `describe_image_attribute`

**Warnings:**
- Method 'describe_image_attribute' is not pageable (may need direct API call)

### `aws_ec2_instance_metadata_defaults`

- **Client:** `ec2`
- **Method:** `get_instance_metadata_defaults`

**Warnings:**
- Method 'get_instance_metadata_defaults' is not pageable (may need direct API call)

### `aws_ec2_serial_console_access`

- **Client:** `ec2`
- **Method:** `get_serial_console_access_status`

**Warnings:**
- Method 'get_serial_console_access_status' is not pageable (may need direct API call)

### `aws_ec2_transit_gateway_policy_table`

- **Client:** `ec2`
- **Method:** `get_transit_gateway_policy_table_entries`

**Warnings:**
- Method 'get_transit_gateway_policy_table_entries' is not pageable (may need direct API call)

### `aws_ec2_transit_gateway_route`

- **Client:** `ec2`
- **Method:** `search_transit_gateway_routes`

**Warnings:**
- Method 'search_transit_gateway_routes' is not pageable (may need direct API call)

### `aws_ecr_account_setting`

- **Client:** `ecr`
- **Method:** `get_account_setting`

**Warnings:**
- Method 'get_account_setting' is not pageable (may need direct API call)

### `aws_ecr_lifecycle_policy`

- **Client:** `ecr`
- **Method:** `get_lifecycle_policy`

**Warnings:**
- Method 'get_lifecycle_policy' is not pageable (may need direct API call)
- Missing 'topkey' field

### `aws_ecr_registry_policy`

- **Client:** `ecr`
- **Method:** `get_registry_policy`

**Warnings:**
- Method 'get_registry_policy' is not pageable (may need direct API call)
- Missing 'topkey' field

### `aws_ecr_registry_scanning_configuration`

- **Client:** `ecr`
- **Method:** `get_registry_scanning_configuration`

**Warnings:**
- Method 'get_registry_scanning_configuration' is not pageable (may need direct API call)
- Missing 'topkey' field

### `aws_ecr_replication_configuration`

- **Client:** `ecr`
- **Method:** `get_registry_policy`

**Warnings:**
- Method 'get_registry_policy' is not pageable (may need direct API call)
- Missing 'topkey' field

### `aws_ecr_repository_policy`

- **Client:** `ecr`
- **Method:** `get_repository_policy`

**Warnings:**
- Method 'get_repository_policy' is not pageable (may need direct API call)

### `aws_ecrpublic_repository_policy`

- **Client:** `ecr-public`
- **Method:** `get_repository_policy`

**Warnings:**
- Method 'get_repository_policy' is not pageable (may need direct API call)
- Missing 'topkey' field

### `aws_ecs_capacity_provider`

- **Client:** `ecs`
- **Method:** `describe_capacity_providers`

**Warnings:**
- Method 'describe_capacity_providers' is not pageable (may need direct API call)

### `aws_ecs_cluster_capacity_providers`

- **Client:** `ecs`
- **Method:** `describe_capacity_providers`

**Warnings:**
- Method 'describe_capacity_providers' is not pageable (may need direct API call)

### `aws_ecs_tag`

- **Client:** `ecs`
- **Method:** `list_tags_for_resource`

**Warnings:**
- Method 'list_tags_for_resource' is not pageable (may need direct API call)

### `aws_ecs_task_definition`

- **Client:** `ecs`
- **Method:** `describe_task_definition`

**Warnings:**
- Method 'describe_task_definition' is not pageable (may need direct API call)

### `aws_ecs_task_set`

- **Client:** `ecs`
- **Method:** `describe_task_sets`

**Warnings:**
- Method 'describe_task_sets' is not pageable (may need direct API call)

### `aws_efs_backup_policy`

- **Client:** `efs`
- **Method:** `describe_backup_policy`

**Warnings:**
- Method 'describe_backup_policy' is not pageable (may need direct API call)

### `aws_efs_file_system_policy`

- **Client:** `efs`
- **Method:** `describe_file_system_policy`

**Warnings:**
- Method 'describe_file_system_policy' is not pageable (may need direct API call)

### `aws_eip`

- **Client:** `ec2`
- **Method:** `describe_addresses`

**Warnings:**
- Method 'describe_addresses' is not pageable (may need direct API call)

### `aws_eip_association`

- **Client:** `ec2`
- **Method:** `describe_addresses`

**Warnings:**
- Method 'describe_addresses' is not pageable (may need direct API call)

### `aws_eip_domain_name`

- **Client:** `ec2`
- **Method:** `describe_addresses`

**Warnings:**
- Method 'describe_addresses' is not pageable (may need direct API call)

### `aws_eks_capability`

- **Client:** `eks`
- **Method:** `describe_cluster`

**Warnings:**
- Method 'describe_cluster' is not pageable (may need direct API call)

### `aws_elastic_beanstalk_application`

- **Client:** `elasticbeanstalk`
- **Method:** `describe_applications`

**Warnings:**
- Method 'describe_applications' is not pageable (may need direct API call)

### `aws_elastic_beanstalk_configuration_template`

- **Client:** `elasticbeanstalk`
- **Method:** `describe_configuration_settings`

**Warnings:**
- Method 'describe_configuration_settings' is not pageable (may need direct API call)

### `aws_elasticsearch_domain`

- **Client:** `es`
- **Method:** `describe_elasticsearch_domains`

**Warnings:**
- Method 'describe_elasticsearch_domains' is not pageable (may need direct API call)

### `aws_elasticsearch_domain_policy`

- **Client:** `es`
- **Method:** `describe_elasticsearch_domain_config`

**Warnings:**
- Method 'describe_elasticsearch_domain_config' is not pageable (may need direct API call)

### `aws_elasticsearch_domain_saml_options`

- **Client:** `es`
- **Method:** `describe_elasticsearch_domain`

**Warnings:**
- Method 'describe_elasticsearch_domain' is not pageable (may need direct API call)

### `aws_elasticsearch_vpc_endpoint`

- **Client:** `es`
- **Method:** `describe_vpc_endpoints`

**Warnings:**
- Method 'describe_vpc_endpoints' is not pageable (may need direct API call)

### `aws_elb_attachment`

- **Client:** `elb`
- **Method:** `describe_load_balancer_attributes`

**Warnings:**
- Method 'describe_load_balancer_attributes' is not pageable (may need direct API call)

### `aws_emr_block_public_access_configuration`

- **Client:** `emr`
- **Method:** `get_block_public_access_configuration`

**Warnings:**
- Method 'get_block_public_access_configuration' is not pageable (may need direct API call)

### `aws_emr_managed_scaling_policy`

- **Client:** `emr`
- **Method:** `get_managed_scaling_policy`

**Warnings:**
- Method 'get_managed_scaling_policy' is not pageable (may need direct API call)

### `aws_finspace_kx_environment`

- **Client:** `finspace`
- **Method:** `list_environments`

**Warnings:**
- Method 'list_environments' is not pageable (may need direct API call)

### `aws_fms_resource_set`

- **Client:** `fms`
- **Method:** `list_resource_sets`

**Warnings:**
- Method 'list_resource_sets' is not pageable (may need direct API call)

### `aws_fsx_data_repository_association`

- **Client:** `fsx`
- **Method:** `describe_data_repository_associations`

**Warnings:**
- Method 'describe_data_repository_associations' is not pageable (may need direct API call)

### `aws_fsx_file_cache`

- **Client:** `fsx`
- **Method:** `describe_file_caches`

**Warnings:**
- Method 'describe_file_caches' is not pageable (may need direct API call)

### `aws_glacier_vault_lock`

- **Client:** `glacier`
- **Method:** `get_vault_lock`

**Warnings:**
- Method 'get_vault_lock' is not pageable (may need direct API call)

### `aws_glue_data_catalog_encryption_settings`

- **Client:** `glue`
- **Method:** `get_data_catalog_encryption_settings`

**Warnings:**
- Method 'get_data_catalog_encryption_settings' is not pageable (may need direct API call)

### `aws_glue_data_quality_ruleset`

- **Client:** `glue`
- **Method:** `list_data_quality_rulesets`

**Warnings:**
- Method 'list_data_quality_rulesets' is not pageable (may need direct API call)

### `aws_glue_dev_endpoint`

- **Client:** `glue`
- **Method:** `list_dev_endpoints`

**Warnings:**
- Method 'list_dev_endpoints' is not pageable (may need direct API call)

### `aws_glue_ml_transform`

- **Client:** `glue`
- **Method:** `list_ml_transforms`

**Warnings:**
- Method 'list_ml_transforms' is not pageable (may need direct API call)

### `aws_glue_resource_policy`

- **Client:** `glue`
- **Method:** `get_resource_policy`

**Warnings:**
- Method 'get_resource_policy' is not pageable (may need direct API call)

### `aws_glue_trigger`

- **Client:** `glue`
- **Method:** `get_trigger`

**Warnings:**
- Method 'get_trigger' is not pageable (may need direct API call)

### `aws_grafana_license_association`

- **Client:** `grafana`
- **Method:** `describe_workspace`

**Warnings:**
- Method 'describe_workspace' is not pageable (may need direct API call)

### `aws_grafana_workspace_saml_configuration`

- **Client:** `grafana`
- **Method:** `describe_workspace_authentication`

**Warnings:**
- Method 'describe_workspace_authentication' is not pageable (may need direct API call)

### `aws_guardduty_detector_feature`

- **Client:** `guardduty`
- **Method:** `get_detector`

**Warnings:**
- Method 'get_detector' is not pageable (may need direct API call)

### `aws_guardduty_malware_protection_plan`

- **Client:** `guardduty`
- **Method:** `list_malware_protection_plans`

**Warnings:**
- Method 'list_malware_protection_plans' is not pageable (may need direct API call)

### `aws_guardduty_member_detector_feature`

- **Client:** `guardduty`
- **Method:** `get_member_detectors`

**Warnings:**
- Method 'get_member_detectors' is not pageable (may need direct API call)

### `aws_guardduty_organization_configuration`

- **Client:** `guardduty`
- **Method:** `describe_organization_configuration`

**Warnings:**
- Method 'describe_organization_configuration' is not pageable (may need direct API call)

### `aws_guardduty_organization_configuration_feature`

- **Client:** `guardduty`
- **Method:** `describe_organization_configuration`

**Warnings:**
- Method 'describe_organization_configuration' is not pageable (may need direct API call)

### `aws_guardduty_publishing_destination`

- **Client:** `guardduty`
- **Method:** `list_publishing_destinations`

**Warnings:**
- Method 'list_publishing_destinations' is not pageable (may need direct API call)

### `aws_iam_account_password_policy`

- **Client:** `iam`
- **Method:** `get_account_password_policy`

**Warnings:**
- Method 'get_account_password_policy' is not pageable (may need direct API call)

### `aws_iam_instance_profile`

- **Client:** `iam`
- **Method:** `get_instance_profile`

**Warnings:**
- Method 'get_instance_profile' is not pageable (may need direct API call)

### `aws_iam_openid_connect_provider`

- **Client:** `iam`
- **Method:** `list_open_id_connect_providers`

**Warnings:**
- Method 'list_open_id_connect_providers' is not pageable (may need direct API call)

### `aws_iam_organizations_features`

- **Client:** `iam`
- **Method:** `get_organizations_access_report`

**Warnings:**
- Method 'get_organizations_access_report' is not pageable (may need direct API call)

### `aws_iam_outbound_web_identity_federation`

- **Client:** `iam`
- **Method:** `list_open_id_connect_providers`

**Warnings:**
- Method 'list_open_id_connect_providers' is not pageable (may need direct API call)

### `aws_iam_policy_attachment`

- **Client:** `iam`
- **Method:** `get_policy`

**Warnings:**
- Method 'get_policy' is not pageable (may need direct API call)

### `aws_iam_saml_provider`

- **Client:** `iam`
- **Method:** `list_saml_providers`

**Warnings:**
- Method 'list_saml_providers' is not pageable (may need direct API call)

### `aws_iam_security_token_service_preferences`

- **Client:** `iam`
- **Method:** `get_account_summary`

**Warnings:**
- Method 'get_account_summary' is not pageable (may need direct API call)

### `aws_iam_service_specific_credential`

- **Client:** `iam`
- **Method:** `list_service_specific_credentials`

**Warnings:**
- Method 'list_service_specific_credentials' is not pageable (may need direct API call)

### `aws_iam_user_login_profile`

- **Client:** `iam`
- **Method:** `get_login_profile`

**Warnings:**
- Method 'get_login_profile' is not pageable (may need direct API call)

### `aws_inspector2_enabler`

- **Client:** `inspector2`
- **Method:** `batch_get_account_status`

**Warnings:**
- Method 'batch_get_account_status' is not pageable (may need direct API call)

### `aws_inspector2_organization_configuration`

- **Client:** `inspector2`
- **Method:** `describe_organization_configuration`

**Warnings:**
- Method 'describe_organization_configuration' is not pageable (may need direct API call)

### `aws_iot_event_configurations`

- **Client:** `iot`
- **Method:** `describe_event_configurations`

**Warnings:**
- Method 'describe_event_configurations' is not pageable (may need direct API call)

### `aws_iot_indexing_configuration`

- **Client:** `iot`
- **Method:** `get_indexing_configuration`

**Warnings:**
- Method 'get_indexing_configuration' is not pageable (may need direct API call)

### `aws_iot_logging_options`

- **Client:** `iot`
- **Method:** `get_v2_logging_options`

**Warnings:**
- Method 'get_v2_logging_options' is not pageable (may need direct API call)

### `aws_ivschat_logging_configuration`

- **Client:** `ivschat`
- **Method:** `list_logging_configurations`

**Warnings:**
- Method 'list_logging_configurations' is not pageable (may need direct API call)

### `aws_ivschat_room`

- **Client:** `ivschat`
- **Method:** `list_rooms`

**Warnings:**
- Method 'list_rooms' is not pageable (may need direct API call)

### `aws_kendra_data_source`

- **Client:** `kendra`
- **Method:** `list_data_sources`

**Warnings:**
- Method 'list_data_sources' is not pageable (may need direct API call)

### `aws_kendra_experience`

- **Client:** `kendra`
- **Method:** `list_experiences`

**Warnings:**
- Method 'list_experiences' is not pageable (may need direct API call)

### `aws_kendra_faq`

- **Client:** `kendra`
- **Method:** `list_faqs`

**Warnings:**
- Method 'list_faqs' is not pageable (may need direct API call)

### `aws_kendra_index`

- **Client:** `kendra`
- **Method:** `list_indices`

**Warnings:**
- Method 'list_indices' is not pageable (may need direct API call)

### `aws_kendra_query_suggestions_block_list`

- **Client:** `kendra`
- **Method:** `list_query_suggestions_block_lists`

**Warnings:**
- Method 'list_query_suggestions_block_lists' is not pageable (may need direct API call)

### `aws_kendra_thesaurus`

- **Client:** `kendra`
- **Method:** `list_thesauri`

**Warnings:**
- Method 'list_thesauri' is not pageable (may need direct API call)

### `aws_key_pair`

- **Client:** `ec2`
- **Method:** `describe_key_pairs`

**Warnings:**
- Method 'describe_key_pairs' is not pageable (may need direct API call)

### `aws_kinesis_analytics_application`

- **Client:** `kinesisanalytics`
- **Method:** `list_applications`

**Warnings:**
- Method 'list_applications' is not pageable (may need direct API call)

### `aws_kinesis_firehose_delivery_stream`

- **Client:** `firehose`
- **Method:** `list_delivery_streams`

**Warnings:**
- Method 'list_delivery_streams' is not pageable (may need direct API call)

### `aws_kinesis_resource_policy`

- **Client:** `kinesis`
- **Method:** `get_resource_policy`

**Warnings:**
- Method 'get_resource_policy' is not pageable (may need direct API call)

### `aws_lakeformation_data_lake_settings`

- **Client:** `lakeformation`
- **Method:** `get_data_lake_settings`

**Warnings:**
- Method 'get_data_lake_settings' is not pageable (may need direct API call)

### `aws_lakeformation_identity_center_configuration`

- **Client:** `lakeformation`
- **Method:** `describe_lake_formation_identity_center_configuration`

**Warnings:**
- Method 'describe_lake_formation_identity_center_configuration' is not pageable (may need direct API call)

### `aws_lakeformation_opt_in`

- **Client:** `lakeformation`
- **Method:** `get_data_lake_settings`

**Warnings:**
- Method 'get_data_lake_settings' is not pageable (may need direct API call)

### `aws_lakeformation_permissions`

- **Client:** `lakeformation`
- **Method:** `list_permissions`

**Warnings:**
- Method 'list_permissions' is not pageable (may need direct API call)

### `aws_lakeformation_resource`

- **Client:** `lakeformation`
- **Method:** `list_resources`

**Warnings:**
- Method 'list_resources' is not pageable (may need direct API call)

### `aws_lakeformation_resource_lf_tags`

- **Client:** `lakeformation`
- **Method:** `get_resource_lf_tags`

**Warnings:**
- Method 'get_resource_lf_tags' is not pageable (may need direct API call)

### `aws_lambda_function_recursion_config`

- **Client:** `lambda`
- **Method:** `get_function_recursion_config`

**Warnings:**
- Method 'get_function_recursion_config' is not pageable (may need direct API call)

### `aws_lambda_permission`

- **Client:** `lambda`
- **Method:** `get_policy`

**Warnings:**
- Method 'get_policy' is not pageable (may need direct API call)

### `aws_lambda_runtime_management_config`

- **Client:** `lambda`
- **Method:** `get_runtime_management_config`

**Warnings:**
- Method 'get_runtime_management_config' is not pageable (may need direct API call)

### `aws_lb_target_group_attachment`

- **Client:** `elbv2`
- **Method:** `describe_target_group_attributes`

**Warnings:**
- Method 'describe_target_group_attributes' is not pageable (may need direct API call)

### `aws_lb_trust_store`

- **Client:** `elbv2`
- **Method:** `describe_load_balancer_attributes`

**Warnings:**
- Method 'describe_load_balancer_attributes' is not pageable (may need direct API call)

### `aws_lb_trust_store_revocation`

- **Client:** `elbv2`
- **Method:** `describe_load_balancer_attributes`

**Warnings:**
- Method 'describe_load_balancer_attributes' is not pageable (may need direct API call)

### `aws_lexv2models_bot`

- **Client:** `lexv2-models`
- **Method:** `list_bots`

**Warnings:**
- Method 'list_bots' is not pageable (may need direct API call)

### `aws_lexv2models_bot_locale`

- **Client:** `lexv2-models`
- **Method:** `list_bot_locales`

**Warnings:**
- Method 'list_bot_locales' is not pageable (may need direct API call)

### `aws_lexv2models_bot_version`

- **Client:** `lexv2-models`
- **Method:** `list_bot_versions`

**Warnings:**
- Method 'list_bot_versions' is not pageable (may need direct API call)

### `aws_lexv2models_intent`

- **Client:** `lexv2-models`
- **Method:** `list_intents`

**Warnings:**
- Method 'list_intents' is not pageable (may need direct API call)

### `aws_lexv2models_slot`

- **Client:** `lexv2-models`
- **Method:** `list_slots`

**Warnings:**
- Method 'list_slots' is not pageable (may need direct API call)

### `aws_lexv2models_slot_type`

- **Client:** `lexv2-models`
- **Method:** `list_slot_types`

**Warnings:**
- Method 'list_slot_types' is not pageable (may need direct API call)

### `aws_licensemanager_grant`

- **Client:** `license-manager`
- **Method:** `list_received_grants`

**Warnings:**
- Method 'list_received_grants' is not pageable (may need direct API call)

### `aws_licensemanager_grant_accepter`

- **Client:** `license-manager`
- **Method:** `list_received_grants`

**Warnings:**
- Method 'list_received_grants' is not pageable (may need direct API call)

### `aws_lightsail_bucket`

- **Client:** `lightsail`
- **Method:** `get_buckets`

**Warnings:**
- Method 'get_buckets' is not pageable (may need direct API call)

### `aws_lightsail_bucket_access_key`

- **Client:** `lightsail`
- **Method:** `get_bucket_access_keys`

**Warnings:**
- Method 'get_bucket_access_keys' is not pageable (may need direct API call)

### `aws_lightsail_bucket_resource_access`

- **Client:** `lightsail`
- **Method:** `get_buckets`

**Warnings:**
- Method 'get_buckets' is not pageable (may need direct API call)

### `aws_lightsail_certificate`

- **Client:** `lightsail`
- **Method:** `get_certificates`

**Warnings:**
- Method 'get_certificates' is not pageable (may need direct API call)

### `aws_lightsail_container_service`

- **Client:** `lightsail`
- **Method:** `get_container_services`

**Warnings:**
- Method 'get_container_services' is not pageable (may need direct API call)

### `aws_lightsail_container_service_deployment_version`

- **Client:** `lightsail`
- **Method:** `get_container_service_deployments`

**Warnings:**
- Method 'get_container_service_deployments' is not pageable (may need direct API call)

### `aws_lightsail_distribution`

- **Client:** `lightsail`
- **Method:** `get_distributions`

**Warnings:**
- Method 'get_distributions' is not pageable (may need direct API call)

### `aws_lightsail_instance_public_ports`

- **Client:** `lightsail`
- **Method:** `get_instance_port_states`

**Warnings:**
- Method 'get_instance_port_states' is not pageable (may need direct API call)

### `aws_lightsail_lb_certificate_attachment`

- **Client:** `lightsail`
- **Method:** `get_load_balancer_tls_certificates`

**Warnings:**
- Method 'get_load_balancer_tls_certificates' is not pageable (may need direct API call)

### `aws_macie2_account`

- **Client:** `macie2`
- **Method:** `get_macie_session`

**Warnings:**
- Method 'get_macie_session' is not pageable (may need direct API call)

### `aws_macie2_organization_configuration`

- **Client:** `macie2`
- **Method:** `describe_organization_configuration`

**Warnings:**
- Method 'describe_organization_configuration' is not pageable (may need direct API call)

### `aws_media_store_container_policy`

- **Client:** `mediastore`
- **Method:** `get_container_policy`

**Warnings:**
- Method 'get_container_policy' is not pageable (may need direct API call)

### `aws_mq_configuration`

- **Client:** `mq`
- **Method:** `list_configurations`

**Warnings:**
- Method 'list_configurations' is not pageable (may need direct API call)

### `aws_networkfirewall_firewall_transit_gateway_attachment_accepter`

- **Client:** `network-firewall`
- **Method:** `describe_firewall`

**Warnings:**
- Method 'describe_firewall' is not pageable (may need direct API call)

### `aws_networkfirewall_vpc_endpoint_association`

- **Client:** `network-firewall`
- **Method:** `describe_firewall`

**Warnings:**
- Method 'describe_firewall' is not pageable (may need direct API call)

### `aws_opensearch_authorize_vpc_endpoint_access`

- **Client:** `opensearch`
- **Method:** `list_vpc_endpoint_access`

**Warnings:**
- Method 'list_vpc_endpoint_access' is not pageable (may need direct API call)

### `aws_opensearch_domain`

- **Client:** `opensearch`
- **Method:** `list_domain_names`

**Warnings:**
- Method 'list_domain_names' is not pageable (may need direct API call)

### `aws_opensearch_domain_policy`

- **Client:** `opensearch`
- **Method:** `list_domain_names`

**Warnings:**
- Method 'list_domain_names' is not pageable (may need direct API call)

### `aws_opensearch_domain_saml_options`

- **Client:** `opensearch`
- **Method:** `list_domain_names`

**Warnings:**
- Method 'list_domain_names' is not pageable (may need direct API call)

### `aws_opensearch_vpc_endpoint`

- **Client:** `opensearch`
- **Method:** `list_vpc_endpoints`

**Warnings:**
- Method 'list_vpc_endpoints' is not pageable (may need direct API call)

### `aws_opensearchserverless_access_policy`

- **Client:** `opensearchserverless`
- **Method:** `list_access_policies`

**Warnings:**
- Method 'list_access_policies' is not pageable (may need direct API call)

### `aws_opensearchserverless_collection`

- **Client:** `opensearchserverless`
- **Method:** `list_collections`

**Warnings:**
- Method 'list_collections' is not pageable (may need direct API call)

### `aws_opensearchserverless_lifecycle_policy`

- **Client:** `opensearchserverless`
- **Method:** `list_lifecycle_policies`

**Warnings:**
- Method 'list_lifecycle_policies' is not pageable (may need direct API call)

### `aws_opensearchserverless_security_config`

- **Client:** `opensearchserverless`
- **Method:** `list_security_configs`

**Warnings:**
- Method 'list_security_configs' is not pageable (may need direct API call)

### `aws_opensearchserverless_security_policy`

- **Client:** `opensearchserverless`
- **Method:** `list_security_policies`

**Warnings:**
- Method 'list_security_policies' is not pageable (may need direct API call)

### `aws_opensearchserverless_vpc_endpoint`

- **Client:** `opensearchserverless`
- **Method:** `list_vpc_endpoints`

**Warnings:**
- Method 'list_vpc_endpoints' is not pageable (may need direct API call)

### `aws_organizations_organization`

- **Client:** `organizations`
- **Method:** `describe_organization`

**Warnings:**
- Method 'describe_organization' is not pageable (may need direct API call)

### `aws_organizations_organizational_unit`

- **Client:** `organizations`
- **Method:** `describe_organizational_unit`

**Warnings:**
- Method 'describe_organizational_unit' is not pageable (may need direct API call)

### `aws_organizations_resource_policy`

- **Client:** `organizations`
- **Method:** `describe_resource_policy`

**Warnings:**
- Method 'describe_resource_policy' is not pageable (may need direct API call)

### `aws_osis_pipeline`

- **Client:** `osis`
- **Method:** `list_pipelines`

**Warnings:**
- Method 'list_pipelines' is not pageable (may need direct API call)

### `aws_placement_group`

- **Client:** `ec2`
- **Method:** `describe_placement_groups`

**Warnings:**
- Method 'describe_placement_groups' is not pageable (may need direct API call)

### `aws_prometheus_alert_manager_definition`

- **Client:** `amp`
- **Method:** `describe_alert_manager_definition`

**Warnings:**
- Method 'describe_alert_manager_definition' is not pageable (may need direct API call)

### `aws_prometheus_query_logging_configuration`

- **Client:** `amp`
- **Method:** `describe_workspace`

**Warnings:**
- Method 'describe_workspace' is not pageable (may need direct API call)

### `aws_prometheus_resource_policy`

- **Client:** `amp`
- **Method:** `describe_resource_policy`

**Warnings:**
- Method 'describe_resource_policy' is not pageable (may need direct API call)

### `aws_prometheus_workspace_configuration`

- **Client:** `amp`
- **Method:** `describe_workspace_configuration`

**Warnings:**
- Method 'describe_workspace_configuration' is not pageable (may need direct API call)

### `aws_quicksight_account_settings`

- **Client:** `quicksight`
- **Method:** `describe_account_settings`

**Warnings:**
- Method 'describe_account_settings' is not pageable (may need direct API call)

### `aws_quicksight_custom_permissions`

- **Client:** `quicksight`
- **Method:** `describe_custom_permissions`

**Warnings:**
- Method 'describe_custom_permissions' is not pageable (may need direct API call)

### `aws_quicksight_ip_restriction`

- **Client:** `quicksight`
- **Method:** `describe_ip_restriction`

**Warnings:**
- Method 'describe_ip_restriction' is not pageable (may need direct API call)

### `aws_quicksight_refresh_schedule`

- **Client:** `quicksight`
- **Method:** `list_refresh_schedules`

**Warnings:**
- Method 'list_refresh_schedules' is not pageable (may need direct API call)

### `aws_quicksight_role_custom_permission`

- **Client:** `quicksight`
- **Method:** `describe_role_custom_permission`

**Warnings:**
- Method 'describe_role_custom_permission' is not pageable (may need direct API call)

### `aws_quicksight_user_custom_permission`

- **Client:** `quicksight`
- **Method:** `describe_user`

**Warnings:**
- Method 'describe_user' is not pageable (may need direct API call)

### `aws_quicksight_vpc_connection`

- **Client:** `quicksight`
- **Method:** `list_vpc_connections`

**Warnings:**
- Method 'list_vpc_connections' is not pageable (may need direct API call)

### `aws_rds_shard_group`

- **Client:** `rds`
- **Method:** `describe_db_shard_groups`

**Warnings:**
- Method 'describe_db_shard_groups' is not pageable (may need direct API call)

### `aws_redshift_authentication_profile`

- **Client:** `redshift`
- **Method:** `describe_authentication_profiles`

**Warnings:**
- Method 'describe_authentication_profiles' is not pageable (may need direct API call)

### `aws_redshift_logging`

- **Client:** `redshift`
- **Method:** `describe_logging_status`

**Warnings:**
- Method 'describe_logging_status' is not pageable (may need direct API call)

### `aws_redshift_partner`

- **Client:** `redshift`
- **Method:** `describe_partners`

**Warnings:**
- Method 'describe_partners' is not pageable (may need direct API call)

### `aws_redshift_resource_policy`

- **Client:** `redshift`
- **Method:** `get_resource_policy`

**Warnings:**
- Method 'get_resource_policy' is not pageable (may need direct API call)

### `aws_redshiftdata_statement`

- **Client:** `redshift-data`
- **Method:** `describe_statement`

**Warnings:**
- Method 'describe_statement' is not pageable (may need direct API call)

### `aws_resiliencehub_resiliency_policy`

- **Client:** `resiliencehub`
- **Method:** `list_resiliency_policies`

**Warnings:**
- Method 'list_resiliency_policies' is not pageable (may need direct API call)

### `aws_route53_delegation_set`

- **Client:** `route53`
- **Method:** `list_reusable_delegation_sets`

**Warnings:**
- Method 'list_reusable_delegation_sets' is not pageable (may need direct API call)

### `aws_route53_hosted_zone_dnssec`

- **Client:** `route53`
- **Method:** `get_dnssec`

**Warnings:**
- Method 'get_dnssec' is not pageable (may need direct API call)

### `aws_route53_key_signing_key`

- **Client:** `route53`
- **Method:** `get_dnssec`

**Warnings:**
- Method 'get_dnssec' is not pageable (may need direct API call)

### `aws_route53_traffic_policy`

- **Client:** `route53`
- **Method:** `list_traffic_policies`

**Warnings:**
- Method 'list_traffic_policies' is not pageable (may need direct API call)

### `aws_route53_traffic_policy_instance`

- **Client:** `route53`
- **Method:** `list_traffic_policy_instances`

**Warnings:**
- Method 'list_traffic_policy_instances' is not pageable (may need direct API call)

### `aws_route53_vpc_association_authorization`

- **Client:** `route53`
- **Method:** `get_hosted_zone`

**Warnings:**
- Method 'get_hosted_zone' is not pageable (may need direct API call)

### `aws_route53_zone_association`

- **Client:** `route53`
- **Method:** `list_hosted_zones_by_vpc`

**Warnings:**
- Method 'list_hosted_zones_by_vpc' is not pageable (may need direct API call)

### `aws_route53domains_delegation_signer_record`

- **Client:** `route53domains`
- **Method:** `get_domain_detail`

**Warnings:**
- Method 'get_domain_detail' is not pageable (may need direct API call)

### `aws_s3_access_point`

- **Client:** `s3control`
- **Method:** `list_access_points`

**Warnings:**
- Method 'list_access_points' is not pageable (may need direct API call)

### `aws_s3_account_public_access_block`

- **Client:** `s3`
- **Method:** `get_public_access_block`

**Warnings:**
- Method 'get_public_access_block' is not pageable (may need direct API call)

### `aws_s3_bucket_abac`

- **Client:** `s3`
- **Method:** `get_bucket_abac`

**Warnings:**
- Method 'get_bucket_abac' is not pageable (may need direct API call)

### `aws_s3_bucket_accelerate_configuration`

- **Client:** `s3`
- **Method:** `get_bucket_accelerate_configuration`

**Warnings:**
- Method 'get_bucket_accelerate_configuration' is not pageable (may need direct API call)

### `aws_s3_bucket_acl`

- **Client:** `s3`
- **Method:** `get_bucket_acl`

**Warnings:**
- Method 'get_bucket_acl' is not pageable (may need direct API call)

### `aws_s3_bucket_analytics_configuration`

- **Client:** `s3`
- **Method:** `get_bucket_analytics_configuration`

**Warnings:**
- Method 'get_bucket_analytics_configuration' is not pageable (may need direct API call)

### `aws_s3_bucket_cors_configuration`

- **Client:** `s3`
- **Method:** `get_bucket_cors`

**Warnings:**
- Method 'get_bucket_cors' is not pageable (may need direct API call)

### `aws_s3_bucket_intelligent_tiering_configuration`

- **Client:** `s3`
- **Method:** `get_bucket_intelligent_tiering_configuration`

**Warnings:**
- Method 'get_bucket_intelligent_tiering_configuration' is not pageable (may need direct API call)

### `aws_s3_bucket_inventory`

- **Client:** `s3`
- **Method:** `get_bucket_inventory_configuration`

**Warnings:**
- Method 'get_bucket_inventory_configuration' is not pageable (may need direct API call)

### `aws_s3_bucket_inventory_configuration`

- **Client:** `s3`
- **Method:** `list_bucket_inventory_configurations`

**Warnings:**
- Method 'list_bucket_inventory_configurations' is not pageable (may need direct API call)

### `aws_s3_bucket_lifecycle_configuration`

- **Client:** `s3`
- **Method:** `get_bucket_lifecycle_configuration`

**Warnings:**
- Method 'get_bucket_lifecycle_configuration' is not pageable (may need direct API call)

### `aws_s3_bucket_logging`

- **Client:** `s3`
- **Method:** `get_bucket_logging`

**Warnings:**
- Method 'get_bucket_logging' is not pageable (may need direct API call)

### `aws_s3_bucket_metadata_configuration`

- **Client:** `s3`
- **Method:** `get_bucket_metadata_configuration`

**Warnings:**
- Method 'get_bucket_metadata_configuration' is not pageable (may need direct API call)

### `aws_s3_bucket_metric`

- **Client:** `s3`
- **Method:** `get_bucket_metrics_configuration`

**Warnings:**
- Method 'get_bucket_metrics_configuration' is not pageable (may need direct API call)

### `aws_s3_bucket_metrics_configuration`

- **Client:** `s3`
- **Method:** `list_bucket_metrics_configurations`

**Warnings:**
- Method 'list_bucket_metrics_configurations' is not pageable (may need direct API call)

### `aws_s3_bucket_notification`

- **Client:** `s3`
- **Method:** `get_bucket_notification_configuration`

**Warnings:**
- Method 'get_bucket_notification_configuration' is not pageable (may need direct API call)

### `aws_s3_bucket_object`

- **Client:** `s3`
- **Method:** `get_object`

**Warnings:**
- Method 'get_object' is not pageable (may need direct API call)

### `aws_s3_bucket_object_lock_configuration`

- **Client:** `s3`
- **Method:** `get_object_lock_configuration`

**Warnings:**
- Method 'get_object_lock_configuration' is not pageable (may need direct API call)

### `aws_s3_bucket_ownership_controls`

- **Client:** `s3`
- **Method:** `get_bucket_ownership_controls`

**Warnings:**
- Method 'get_bucket_ownership_controls' is not pageable (may need direct API call)

### `aws_s3_bucket_policy`

- **Client:** `s3`
- **Method:** `get_bucket_policy`

**Warnings:**
- Method 'get_bucket_policy' is not pageable (may need direct API call)

### `aws_s3_bucket_public_access_block`

- **Client:** `s3`
- **Method:** `get_public_access_block`

**Warnings:**
- Method 'get_public_access_block' is not pageable (may need direct API call)

### `aws_s3_bucket_replication_configuration`

- **Client:** `s3`
- **Method:** `get_bucket_replication`

**Warnings:**
- Method 'get_bucket_replication' is not pageable (may need direct API call)

### `aws_s3_bucket_request_payment_configuration`

- **Client:** `s3`
- **Method:** `get_bucket_request_payment`

**Warnings:**
- Method 'get_bucket_request_payment' is not pageable (may need direct API call)

### `aws_s3_bucket_server_side_encryption_configuration`

- **Client:** `s3`
- **Method:** `get_bucket_encryption`

**Warnings:**
- Method 'get_bucket_encryption' is not pageable (may need direct API call)

### `aws_s3_bucket_versioning`

- **Client:** `s3`
- **Method:** `get_bucket_versioning`

**Warnings:**
- Method 'get_bucket_versioning' is not pageable (may need direct API call)

### `aws_s3_bucket_website_configuration`

- **Client:** `s3`
- **Method:** `get_bucket_website`

**Warnings:**
- Method 'get_bucket_website' is not pageable (may need direct API call)

### `aws_s3_object`

- **Client:** `s3`
- **Method:** `get_object`

**Warnings:**
- Method 'get_object' is not pageable (may need direct API call)

### `aws_s3_object_copy`

- **Client:** `s3`
- **Method:** `get_object`

**Warnings:**
- Method 'get_object' is not pageable (may need direct API call)

### `aws_s3control_access_grant`

- **Client:** `s3control`
- **Method:** `list_access_grants`

**Warnings:**
- Method 'list_access_grants' is not pageable (may need direct API call)

### `aws_s3control_access_grants_instance`

- **Client:** `s3control`
- **Method:** `list_access_grants`

**Warnings:**
- Method 'list_access_grants' is not pageable (may need direct API call)

### `aws_s3control_access_grants_instance_resource_policy`

- **Client:** `s3control`
- **Method:** `list_access_grants`

**Warnings:**
- Method 'list_access_grants' is not pageable (may need direct API call)

### `aws_s3control_access_grants_location`

- **Client:** `s3control`
- **Method:** `list_access_grants`

**Warnings:**
- Method 'list_access_grants' is not pageable (may need direct API call)

### `aws_s3control_access_point_policy`

- **Client:** `s3control`
- **Method:** `get_access_point_policy`

**Warnings:**
- Method 'get_access_point_policy' is not pageable (may need direct API call)

### `aws_s3control_bucket_lifecycle_configuration`

- **Client:** `s3control`
- **Method:** `get_bucket_lifecycle_configuration`

**Warnings:**
- Method 'get_bucket_lifecycle_configuration' is not pageable (may need direct API call)

### `aws_s3control_bucket_policy`

- **Client:** `s3control`
- **Method:** `get_bucket_policy`

**Warnings:**
- Method 'get_bucket_policy' is not pageable (may need direct API call)

### `aws_s3control_directory_bucket_access_point_scope`

- **Client:** `s3control`
- **Method:** `get_access_point_policy_for_object_lambda`

**Warnings:**
- Method 'get_access_point_policy_for_object_lambda' is not pageable (may need direct API call)

### `aws_s3control_multi_region_access_point`

- **Client:** `s3control`
- **Method:** `list_access_points`

**Warnings:**
- Method 'list_access_points' is not pageable (may need direct API call)

### `aws_s3control_multi_region_access_point_policy`

- **Client:** `s3control`
- **Method:** `list_access_points`

**Warnings:**
- Method 'list_access_points' is not pageable (may need direct API call)

### `aws_s3control_object_lambda_access_point`

- **Client:** `s3control`
- **Method:** `list_access_points`

**Warnings:**
- Method 'list_access_points' is not pageable (may need direct API call)

### `aws_s3control_object_lambda_access_point_policy`

- **Client:** `s3control`
- **Method:** `list_access_points`

**Warnings:**
- Method 'list_access_points' is not pageable (may need direct API call)

### `aws_s3control_storage_lens_configuration`

- **Client:** `s3control`
- **Method:** `get_storage_lens_configuration`

**Warnings:**
- Method 'get_storage_lens_configuration' is not pageable (may need direct API call)

### `aws_s3tables_table_bucket_policy`

- **Client:** `s3tables`
- **Method:** `get_table_bucket_policy`

**Warnings:**
- Method 'get_table_bucket_policy' is not pageable (may need direct API call)

### `aws_s3tables_table_bucket_replication`

- **Client:** `s3tables`
- **Method:** `get_table_bucket_replication`

**Warnings:**
- Method 'get_table_bucket_replication' is not pageable (may need direct API call)

### `aws_s3tables_table_policy`

- **Client:** `s3tables`
- **Method:** `get_table_policy`

**Warnings:**
- Method 'get_table_policy' is not pageable (may need direct API call)

### `aws_s3vectors_vector_bucket_policy`

- **Client:** `s3vectors`
- **Method:** `get_vector_bucket_policy`

**Warnings:**
- Method 'get_vector_bucket_policy' is not pageable (may need direct API call)

### `aws_sagemaker_hub`

- **Client:** `sagemaker`
- **Method:** `list_hubs`

**Warnings:**
- Method 'list_hubs' is not pageable (may need direct API call)

### `aws_sagemaker_model_package_group_policy`

- **Client:** `sagemaker`
- **Method:** `get_model_package_group_policy`

**Warnings:**
- Method 'get_model_package_group_policy' is not pageable (may need direct API call)

### `aws_sagemaker_project`

- **Client:** `sagemaker`
- **Method:** `list_projects`

**Warnings:**
- Method 'list_projects' is not pageable (may need direct API call)

### `aws_secretsmanager_secret_policy`

- **Client:** `secretsmanager`
- **Method:** `get_resource_policy`

**Warnings:**
- Method 'get_resource_policy' is not pageable (may need direct API call)

### `aws_secretsmanager_secret_rotation`

- **Client:** `secretsmanager`
- **Method:** `describe_secret`

**Warnings:**
- Method 'describe_secret' is not pageable (may need direct API call)

### `aws_secretsmanager_secret_version`

- **Client:** `secretsmanager`
- **Method:** `list_secret_version_ids`

**Warnings:**
- Method 'list_secret_version_ids' is not pageable (may need direct API call)

### `aws_securityhub_account`

- **Client:** `securityhub`
- **Method:** `describe_hub`

**Warnings:**
- Method 'describe_hub' is not pageable (may need direct API call)

### `aws_securityhub_automation_rule`

- **Client:** `securityhub`
- **Method:** `list_automation_rules`

**Warnings:**
- Method 'list_automation_rules' is not pageable (may need direct API call)

### `aws_securityhub_organization_configuration`

- **Client:** `securityhub`
- **Method:** `describe_organization_configuration`

**Warnings:**
- Method 'describe_organization_configuration' is not pageable (may need direct API call)

### `aws_securitylake_subscriber_notification`

- **Client:** `securitylake`
- **Method:** `get_subscriber`

**Warnings:**
- Method 'get_subscriber' is not pageable (may need direct API call)

### `aws_servicecatalog_provisioning_artifact`

- **Client:** `servicecatalog`
- **Method:** `list_provisioning_artifacts`

**Warnings:**
- Method 'list_provisioning_artifacts' is not pageable (may need direct API call)

### `aws_ses_active_receipt_rule_set`

- **Client:** `ses`
- **Method:** `describe_active_receipt_rule_set`

**Warnings:**
- Method 'describe_active_receipt_rule_set' is not pageable (may need direct API call)

### `aws_ses_receipt_rule`

- **Client:** `ses`
- **Method:** `describe_receipt_rule`

**Warnings:**
- Method 'describe_receipt_rule' is not pageable (may need direct API call)

### `aws_ses_receipt_rule_set`

- **Client:** `ses`
- **Method:** `describe_receipt_rule_set`

**Warnings:**
- Method 'describe_receipt_rule_set' is not pageable (may need direct API call)

### `aws_sesv2_account_suppression_attributes`

- **Client:** `sesv2`
- **Method:** `get_account`

**Warnings:**
- Method 'get_account' is not pageable (may need direct API call)

### `aws_sesv2_account_vdm_attributes`

- **Client:** `sesv2`
- **Method:** `get_account`

**Warnings:**
- Method 'get_account' is not pageable (may need direct API call)

### `aws_sesv2_configuration_set`

- **Client:** `sesv2`
- **Method:** `list_configuration_sets`

**Warnings:**
- Method 'list_configuration_sets' is not pageable (may need direct API call)

### `aws_sesv2_configuration_set_event_destination`

- **Client:** `sesv2`
- **Method:** `get_configuration_set_event_destinations`

**Warnings:**
- Method 'get_configuration_set_event_destinations' is not pageable (may need direct API call)

### `aws_sesv2_contact_list`

- **Client:** `sesv2`
- **Method:** `list_contact_lists`

**Warnings:**
- Method 'list_contact_lists' is not pageable (may need direct API call)

### `aws_sesv2_dedicated_ip_assignment`

- **Client:** `sesv2`
- **Method:** `get_dedicated_ips`

**Warnings:**
- Method 'get_dedicated_ips' is not pageable (may need direct API call)

### `aws_sesv2_dedicated_ip_pool`

- **Client:** `sesv2`
- **Method:** `list_dedicated_ip_pools`

**Warnings:**
- Method 'list_dedicated_ip_pools' is not pageable (may need direct API call)

### `aws_sesv2_email_identity`

- **Client:** `sesv2`
- **Method:** `list_email_identities`

**Warnings:**
- Method 'list_email_identities' is not pageable (may need direct API call)

### `aws_sesv2_email_identity_feedback_attributes`

- **Client:** `sesv2`
- **Method:** `get_email_identity`

**Warnings:**
- Method 'get_email_identity' is not pageable (may need direct API call)

### `aws_sesv2_email_identity_mail_from_attributes`

- **Client:** `sesv2`
- **Method:** `get_email_identity`

**Warnings:**
- Method 'get_email_identity' is not pageable (may need direct API call)

### `aws_sesv2_email_identity_policy`

- **Client:** `sesv2`
- **Method:** `get_email_identity_policies`

**Warnings:**
- Method 'get_email_identity_policies' is not pageable (may need direct API call)

### `aws_sfn_alias`

- **Client:** `stepfunctions`
- **Method:** `list_state_machine_aliases`

**Warnings:**
- Method 'list_state_machine_aliases' is not pageable (may need direct API call)

### `aws_shield_proactive_engagement`

- **Client:** `shield`
- **Method:** `describe_emergency_contact_settings`

**Warnings:**
- Method 'describe_emergency_contact_settings' is not pageable (may need direct API call)

### `aws_shield_protection_group`

- **Client:** `shield`
- **Method:** `list_protection_groups`

**Warnings:**
- Method 'list_protection_groups' is not pageable (may need direct API call)

### `aws_shield_subscription`

- **Client:** `shield`
- **Method:** `describe_subscription`

**Warnings:**
- Method 'describe_subscription' is not pageable (may need direct API call)

### `aws_signer_signing_profile_permission`

- **Client:** `signer`
- **Method:** `list_profile_permissions`

**Warnings:**
- Method 'list_profile_permissions' is not pageable (may need direct API call)

### `aws_sns_topic_data_protection_policy`

- **Client:** `sns`
- **Method:** `get_data_protection_policy`

**Warnings:**
- Method 'get_data_protection_policy' is not pageable (may need direct API call)

### `aws_sns_topic_policy`

- **Client:** `sns`
- **Method:** `get_topic_attributes`

**Warnings:**
- Method 'get_topic_attributes' is not pageable (may need direct API call)

### `aws_spot_datafeed_subscription`

- **Client:** `ec2`
- **Method:** `describe_spot_datafeed_subscription`

**Warnings:**
- Method 'describe_spot_datafeed_subscription' is not pageable (may need direct API call)

### `aws_sqs_queue`

- **Client:** `sqs`
- **Method:** `list_queues`

**Warnings:**
- Missing 'key' field

### `aws_sqs_queue_policy`

- **Client:** `sqs`
- **Method:** `get_queue_attributes`

**Warnings:**
- Method 'get_queue_attributes' is not pageable (may need direct API call)

### `aws_sqs_queue_redrive_allow_policy`

- **Client:** `sqs`
- **Method:** `get_queue_attributes`

**Warnings:**
- Method 'get_queue_attributes' is not pageable (may need direct API call)

### `aws_sqs_queue_redrive_policy`

- **Client:** `sqs`
- **Method:** `get_queue_attributes`

**Warnings:**
- Method 'get_queue_attributes' is not pageable (may need direct API call)

### `aws_ssm_default_patch_baseline`

- **Client:** `ssm`
- **Method:** `get_default_patch_baseline`

**Warnings:**
- Method 'get_default_patch_baseline' is not pageable (may need direct API call)

### `aws_ssm_service_setting`

- **Client:** `ssm`
- **Method:** `get_service_setting`

**Warnings:**
- Method 'get_service_setting' is not pageable (may need direct API call)

### `aws_ssmcontacts_plan`

- **Client:** `ssm-contacts`
- **Method:** `get_contact`

**Warnings:**
- Method 'get_contact' is not pageable (may need direct API call)

### `aws_ssmincidents_replication_set`

- **Client:** `ssm-incidents`
- **Method:** `list_replication_sets`

**Warnings:**
- Missing 'key' field

### `aws_storagegateway_cache`

- **Client:** `storagegateway`
- **Method:** `describe_cache`

**Warnings:**
- Method 'describe_cache' is not pageable (may need direct API call)

### `aws_storagegateway_cached_iscsi_volume`

- **Client:** `storagegateway`
- **Method:** `describe_cached_iscsi_volumes`

**Warnings:**
- Method 'describe_cached_iscsi_volumes' is not pageable (may need direct API call)

### `aws_storagegateway_file_system_association`

- **Client:** `storagegateway`
- **Method:** `describe_file_system_associations`

**Warnings:**
- Method 'describe_file_system_associations' is not pageable (may need direct API call)

### `aws_storagegateway_nfs_file_share`

- **Client:** `storagegateway`
- **Method:** `describe_nfs_file_shares`

**Warnings:**
- Method 'describe_nfs_file_shares' is not pageable (may need direct API call)

### `aws_storagegateway_smb_file_share`

- **Client:** `storagegateway`
- **Method:** `describe_smb_file_shares`

**Warnings:**
- Method 'describe_smb_file_shares' is not pageable (may need direct API call)

### `aws_storagegateway_stored_iscsi_volume`

- **Client:** `storagegateway`
- **Method:** `describe_stored_iscsi_volumes`

**Warnings:**
- Method 'describe_stored_iscsi_volumes' is not pageable (may need direct API call)

### `aws_storagegateway_upload_buffer`

- **Client:** `storagegateway`
- **Method:** `describe_upload_buffer`

**Warnings:**
- Method 'describe_upload_buffer' is not pageable (may need direct API call)

### `aws_storagegateway_working_storage`

- **Client:** `storagegateway`
- **Method:** `describe_working_storage`

**Warnings:**
- Method 'describe_working_storage' is not pageable (may need direct API call)

### `aws_timestreamwrite_database`

- **Client:** `timestream-write`
- **Method:** `list_databases`

**Warnings:**
- Method 'list_databases' is not pageable (may need direct API call)

### `aws_timestreamwrite_table`

- **Client:** `timestream-write`
- **Method:** `list_tables`

**Warnings:**
- Method 'list_tables' is not pageable (may need direct API call)

### `aws_transcribe_language_model`

- **Client:** `transcribe`
- **Method:** `list_language_models`

**Warnings:**
- Method 'list_language_models' is not pageable (may need direct API call)

### `aws_transcribe_medical_vocabulary`

- **Client:** `transcribe`
- **Method:** `list_medical_vocabularies`

**Warnings:**
- Method 'list_medical_vocabularies' is not pageable (may need direct API call)

### `aws_transcribe_vocabulary`

- **Client:** `transcribe`
- **Method:** `list_vocabularies`

**Warnings:**
- Method 'list_vocabularies' is not pageable (may need direct API call)

### `aws_transcribe_vocabulary_filter`

- **Client:** `transcribe`
- **Method:** `list_vocabulary_filters`

**Warnings:**
- Method 'list_vocabulary_filters' is not pageable (may need direct API call)

### `aws_transfer_host_key`

- **Client:** `transfer`
- **Method:** `describe_server`

**Warnings:**
- Method 'describe_server' is not pageable (may need direct API call)

### `aws_transfer_web_app_customization`

- **Client:** `transfer`
- **Method:** `describe_web_app`

**Warnings:**
- Method 'describe_web_app' is not pageable (may need direct API call)

### `aws_verifiedpermissions_schema`

- **Client:** `verifiedpermissions`
- **Method:** `get_schema`

**Warnings:**
- Method 'get_schema' is not pageable (may need direct API call)

### `aws_vpc_block_public_access_exclusion`

- **Client:** `ec2`
- **Method:** `describe_vpc_block_public_access_exclusions`

**Warnings:**
- Method 'describe_vpc_block_public_access_exclusions' is not pageable (may need direct API call)

### `aws_vpc_block_public_access_options`

- **Client:** `ec2`
- **Method:** `describe_vpc_block_public_access_options`

**Warnings:**
- Method 'describe_vpc_block_public_access_options' is not pageable (may need direct API call)

### `aws_vpc_encryption_control`

- **Client:** `ec2`
- **Method:** `describe_vpc_encryption_controls`

**Warnings:**
- Method 'describe_vpc_encryption_controls' is not pageable (may need direct API call)

### `aws_vpclattice_auth_policy`

- **Client:** `vpc-lattice`
- **Method:** `get_auth_policy`

**Warnings:**
- Method 'get_auth_policy' is not pageable (may need direct API call)

### `aws_vpclattice_domain_verification`

- **Client:** `vpc-lattice`
- **Method:** `get_service_network_service_association`

**Warnings:**
- Method 'get_service_network_service_association' is not pageable (may need direct API call)

### `aws_vpclattice_resource_policy`

- **Client:** `vpc-lattice`
- **Method:** `get_resource_policy`

**Warnings:**
- Method 'get_resource_policy' is not pageable (may need direct API call)

### `aws_vpn_connection`

- **Client:** `ec2`
- **Method:** `describe_vpn_connections`

**Warnings:**
- Method 'describe_vpn_connections' is not pageable (may need direct API call)

### `aws_vpn_gateway`

- **Client:** `ec2`
- **Method:** `describe_vpn_gateways`

**Warnings:**
- Method 'describe_vpn_gateways' is not pageable (may need direct API call)

### `aws_wafregional_byte_match_set`

- **Client:** `waf-regional`
- **Method:** `list_byte_match_sets`

**Warnings:**
- Method 'list_byte_match_sets' is not pageable (may need direct API call)

### `aws_wafregional_geo_match_set`

- **Client:** `waf-regional`
- **Method:** `list_geo_match_sets`

**Warnings:**
- Method 'list_geo_match_sets' is not pageable (may need direct API call)

### `aws_wafregional_ipset`

- **Client:** `waf-regional`
- **Method:** `list_ip_sets`

**Warnings:**
- Method 'list_ip_sets' is not pageable (may need direct API call)

### `aws_wafregional_rate_based_rule`

- **Client:** `waf-regional`
- **Method:** `list_rate_based_rules`

**Warnings:**
- Method 'list_rate_based_rules' is not pageable (may need direct API call)

### `aws_wafregional_regex_match_set`

- **Client:** `waf-regional`
- **Method:** `list_regex_match_sets`

**Warnings:**
- Method 'list_regex_match_sets' is not pageable (may need direct API call)

### `aws_wafregional_regex_pattern_set`

- **Client:** `waf-regional`
- **Method:** `list_regex_pattern_sets`

**Warnings:**
- Method 'list_regex_pattern_sets' is not pageable (may need direct API call)

### `aws_wafregional_rule`

- **Client:** `waf-regional`
- **Method:** `list_rules`

**Warnings:**
- Method 'list_rules' is not pageable (may need direct API call)

### `aws_wafregional_rule_group`

- **Client:** `waf-regional`
- **Method:** `list_rule_groups`

**Warnings:**
- Method 'list_rule_groups' is not pageable (may need direct API call)

### `aws_wafregional_size_constraint_set`

- **Client:** `waf-regional`
- **Method:** `list_size_constraint_sets`

**Warnings:**
- Method 'list_size_constraint_sets' is not pageable (may need direct API call)

### `aws_wafregional_sql_injection_match_set`

- **Client:** `waf-regional`
- **Method:** `list_sql_injection_match_sets`

**Warnings:**
- Method 'list_sql_injection_match_sets' is not pageable (may need direct API call)

### `aws_wafregional_web_acl`

- **Client:** `waf-regional`
- **Method:** `list_web_acls`

**Warnings:**
- Method 'list_web_acls' is not pageable (may need direct API call)

### `aws_wafregional_xss_match_set`

- **Client:** `waf-regional`
- **Method:** `list_xss_match_sets`

**Warnings:**
- Method 'list_xss_match_sets' is not pageable (may need direct API call)

### `aws_wafv2_api_key`

- **Client:** `wafv2`
- **Method:** `list_api_keys`

**Warnings:**
- Method 'list_api_keys' is not pageable (may need direct API call)

### `aws_wafv2_ip_set`

- **Client:** `wafv2`
- **Method:** `list_ip_sets`

**Warnings:**
- Method 'list_ip_sets' is not pageable (may need direct API call)

### `aws_wafv2_regex_pattern_set`

- **Client:** `wafv2`
- **Method:** `list_regex_pattern_sets`

**Warnings:**
- Method 'list_regex_pattern_sets' is not pageable (may need direct API call)

### `aws_wafv2_rule_group`

- **Client:** `wafv2`
- **Method:** `list_rule_groups`

**Warnings:**
- Method 'list_rule_groups' is not pageable (may need direct API call)

### `aws_wafv2_web_acl`

- **Client:** `wafv2`
- **Method:** `list_web_acls`

**Warnings:**
- Method 'list_web_acls' is not pageable (may need direct API call)

### `aws_wafv2_web_acl_association`

- **Client:** `wafv2`
- **Method:** `list_resources_for_web_acl`

**Warnings:**
- Method 'list_resources_for_web_acl' is not pageable (may need direct API call)

### `aws_wafv2_web_acl_logging_configuration`

- **Client:** `wafv2`
- **Method:** `get_logging_configuration`

**Warnings:**
- Method 'get_logging_configuration' is not pageable (may need direct API call)

### `aws_wafv2_web_acl_rule_group_association`

- **Client:** `wafv2`
- **Method:** `list_resources_for_web_acl`

**Warnings:**
- Method 'list_resources_for_web_acl' is not pageable (may need direct API call)

### `aws_workspaces_connection_alias`

- **Client:** `workspaces`
- **Method:** `describe_connection_aliases`

**Warnings:**
- Method 'describe_connection_aliases' is not pageable (may need direct API call)

### `aws_workspacesweb_browser_settings`

- **Client:** `workspaces-web`
- **Method:** `list_browser_settings`

**Warnings:**
- Method 'list_browser_settings' is not pageable (may need direct API call)

### `aws_workspacesweb_browser_settings_association`

- **Client:** `workspaces-web`
- **Method:** `list_browser_settings`

**Warnings:**
- Method 'list_browser_settings' is not pageable (may need direct API call)

### `aws_workspacesweb_identity_provider`

- **Client:** `workspaces-web`
- **Method:** `list_identity_providers`

**Warnings:**
- Method 'list_identity_providers' is not pageable (may need direct API call)

### `aws_workspacesweb_ip_access_settings`

- **Client:** `workspaces-web`
- **Method:** `list_ip_access_settings`

**Warnings:**
- Method 'list_ip_access_settings' is not pageable (may need direct API call)

### `aws_workspacesweb_ip_access_settings_association`

- **Client:** `workspaces-web`
- **Method:** `list_ip_access_settings`

**Warnings:**
- Method 'list_ip_access_settings' is not pageable (may need direct API call)

### `aws_workspacesweb_network_settings`

- **Client:** `workspaces-web`
- **Method:** `list_network_settings`

**Warnings:**
- Method 'list_network_settings' is not pageable (may need direct API call)

### `aws_workspacesweb_network_settings_association`

- **Client:** `workspaces-web`
- **Method:** `list_network_settings`

**Warnings:**
- Method 'list_network_settings' is not pageable (may need direct API call)

### `aws_workspacesweb_portal`

- **Client:** `workspaces-web`
- **Method:** `list_portals`

**Warnings:**
- Method 'list_portals' is not pageable (may need direct API call)

### `aws_workspacesweb_trust_store`

- **Client:** `workspaces-web`
- **Method:** `list_trust_stores`

**Warnings:**
- Method 'list_trust_stores' is not pageable (may need direct API call)

### `aws_workspacesweb_trust_store_association`

- **Client:** `workspaces-web`
- **Method:** `list_trust_stores`

**Warnings:**
- Method 'list_trust_stores' is not pageable (may need direct API call)

### `aws_workspacesweb_user_access_logging_settings`

- **Client:** `workspaces-web`
- **Method:** `list_user_access_logging_settings`

**Warnings:**
- Method 'list_user_access_logging_settings' is not pageable (may need direct API call)

### `aws_workspacesweb_user_access_logging_settings_association`

- **Client:** `workspaces-web`
- **Method:** `list_user_access_logging_settings`

**Warnings:**
- Method 'list_user_access_logging_settings' is not pageable (may need direct API call)

### `aws_workspacesweb_user_settings`

- **Client:** `workspaces-web`
- **Method:** `list_user_settings`

**Warnings:**
- Method 'list_user_settings' is not pageable (may need direct API call)

### `aws_workspacesweb_user_settings_association`

- **Client:** `workspaces-web`
- **Method:** `list_user_settings`

**Warnings:**
- Method 'list_user_settings' is not pageable (may need direct API call)

### `aws_xray_encryption_config`

- **Client:** `xray`
- **Method:** `get_encryption_config`

**Warnings:**
- Method 'get_encryption_config' is not pageable (may need direct API call)

## ✅ Valid Resources

The following 989 resources passed all verification checks:

### accessanalyzer_analyzer

- `aws_accessanalyzer_analyzer`

### accessanalyzer_archive

- `aws_accessanalyzer_archive_rule`

### acm_certificate

- `aws_acm_certificate`
- `aws_acm_certificate_validation`

### acmpca_certificate

- `aws_acmpca_certificate_authority`
- `aws_acmpca_certificate_authority_certificate`

### acmpca_permission

- `aws_acmpca_permission`

### alb

- `aws_alb`

### ami

- `aws_ami`

### ami_copy

- `aws_ami_copy`

### ami_from

- `aws_ami_from_instance`

### amplify_app

- `aws_amplify_app`

### amplify_branch

- `aws_amplify_branch`

### amplify_domain

- `aws_amplify_domain_association`

### api_gateway

- `aws_api_gateway_api_key`
- `aws_api_gateway_authorizer`
- `aws_api_gateway_base_path_mapping`
- `aws_api_gateway_client_certificate`
- `aws_api_gateway_deployment`
- `aws_api_gateway_documentation_part`
- `aws_api_gateway_documentation_version`
- `aws_api_gateway_domain_name`
- `aws_api_gateway_gateway_response`
- `aws_api_gateway_model`
- `aws_api_gateway_request_validator`
- `aws_api_gateway_resource`
- `aws_api_gateway_rest_api`
- `aws_api_gateway_rest_api_put`
- `aws_api_gateway_usage_plan`
- `aws_api_gateway_usage_plan_key`
- `aws_api_gateway_vpc_link`

### apigatewayv2_api

- `aws_apigatewayv2_api`

### apigatewayv2_authorizer

- `aws_apigatewayv2_authorizer`

### apigatewayv2_deployment

- `aws_apigatewayv2_deployment`

### apigatewayv2_domain

- `aws_apigatewayv2_domain_name`

### apigatewayv2_integration

- `aws_apigatewayv2_integration`
- `aws_apigatewayv2_integration_response`

### apigatewayv2_model

- `aws_apigatewayv2_model`

### apigatewayv2_route

- `aws_apigatewayv2_route`
- `aws_apigatewayv2_route_response`

### apigatewayv2_stage

- `aws_apigatewayv2_stage`

### app_cookie

- `aws_app_cookie_stickiness_policy`

### appautoscaling_policy

- `aws_appautoscaling_policy`

### appautoscaling_scheduled

- `aws_appautoscaling_scheduled_action`

### appautoscaling_target

- `aws_appautoscaling_target`

### appconfig_application

- `aws_appconfig_application`

### appconfig_configuration

- `aws_appconfig_configuration_profile`

### appconfig_deployment

- `aws_appconfig_deployment`
- `aws_appconfig_deployment_strategy`

### appconfig_environment

- `aws_appconfig_environment`

### appconfig_extension

- `aws_appconfig_extension`
- `aws_appconfig_extension_association`

### appconfig_hosted

- `aws_appconfig_hosted_configuration_version`

### appfabric_app

- `aws_appfabric_app_authorization`
- `aws_appfabric_app_authorization_connection`
- `aws_appfabric_app_bundle`

### appfabric_ingestion

- `aws_appfabric_ingestion`
- `aws_appfabric_ingestion_destination`

### appintegrations_data

- `aws_appintegrations_data_integration`

### appintegrations_event

- `aws_appintegrations_event_integration`

### appmesh_gateway

- `aws_appmesh_gateway_route`

### appmesh_mesh

- `aws_appmesh_mesh`

### appmesh_route

- `aws_appmesh_route`

### appmesh_virtual

- `aws_appmesh_virtual_gateway`
- `aws_appmesh_virtual_node`
- `aws_appmesh_virtual_router`
- `aws_appmesh_virtual_service`

### appstream_directory

- `aws_appstream_directory_config`

### appstream_fleet

- `aws_appstream_fleet`
- `aws_appstream_fleet_stack_association`

### appstream_image

- `aws_appstream_image_builder`

### appstream_stack

- `aws_appstream_stack`

### appstream_user

- `aws_appstream_user`
- `aws_appstream_user_stack_association`

### appsync_api

- `aws_appsync_api`
- `aws_appsync_api_key`

### appsync_channel

- `aws_appsync_channel_namespace`

### appsync_datasource

- `aws_appsync_datasource`

### appsync_domain

- `aws_appsync_domain_name`

### appsync_function

- `aws_appsync_function`

### appsync_graphql

- `aws_appsync_graphql_api`

### appsync_resolver

- `aws_appsync_resolver`

### appsync_source

- `aws_appsync_source_api_association`

### appsync_type

- `aws_appsync_type`

### athena_data

- `aws_athena_data_catalog`

### athena_database

- `aws_athena_database`

### athena_named

- `aws_athena_named_query`

### autoscaling_attachment

- `aws_autoscaling_attachment`

### autoscaling_group

- `aws_autoscaling_group`
- `aws_autoscaling_group_tag`

### autoscaling_notification

- `aws_autoscaling_notification`

### autoscaling_policy

- `aws_autoscaling_policy`

### autoscaling_schedule

- `aws_autoscaling_schedule`

### autoscalingplans_scaling

- `aws_autoscalingplans_scaling_plan`

### backup_logically

- `aws_backup_logically_air_gapped_vault`

### backup_plan

- `aws_backup_plan`

### backup_restore

- `aws_backup_restore_testing_plan`
- `aws_backup_restore_testing_selection`

### backup_selection

- `aws_backup_selection`

### backup_vault

- `aws_backup_vault`

### batch_compute

- `aws_batch_compute_environment`

### batch_job

- `aws_batch_job_definition`
- `aws_batch_job_queue`

### batch_scheduling

- `aws_batch_scheduling_policy`

### bcmdataexports_export

- `aws_bcmdataexports_export`

### bedrock_custom

- `aws_bedrock_custom_model`

### bedrock_guardrail

- `aws_bedrock_guardrail`
- `aws_bedrock_guardrail_version`

### bedrock_inference

- `aws_bedrock_inference_profile`

### bedrock_provisioned

- `aws_bedrock_provisioned_model_throughput`

### bedrockagent_agent

- `aws_bedrockagent_agent`
- `aws_bedrockagent_agent_action_group`
- `aws_bedrockagent_agent_alias`
- `aws_bedrockagent_agent_collaborator`
- `aws_bedrockagent_agent_knowledge_base_association`

### bedrockagent_data

- `aws_bedrockagent_data_source`

### bedrockagent_flow

- `aws_bedrockagent_flow`

### bedrockagent_knowledge

- `aws_bedrockagent_knowledge_base`

### bedrockagent_prompt

- `aws_bedrockagent_prompt`

### bedrockagentcore_agent

- `aws_bedrockagentcore_agent_runtime`
- `aws_bedrockagentcore_agent_runtime_endpoint`

### bedrockagentcore_api

- `aws_bedrockagentcore_api_key_credential_provider`

### bedrockagentcore_browser

- `aws_bedrockagentcore_browser`

### bedrockagentcore_code

- `aws_bedrockagentcore_code_interpreter`

### bedrockagentcore_gateway

- `aws_bedrockagentcore_gateway`
- `aws_bedrockagentcore_gateway_target`

### bedrockagentcore_memory

- `aws_bedrockagentcore_memory`
- `aws_bedrockagentcore_memory_strategy`

### bedrockagentcore_oauth2

- `aws_bedrockagentcore_oauth2_credential_provider`

### bedrockagentcore_workload

- `aws_bedrockagentcore_workload_identity`

### billing_view

- `aws_billing_view`

### budgets_budget

- `aws_budgets_budget`
- `aws_budgets_budget_action`

### ce_anomaly

- `aws_ce_anomaly_monitor`
- `aws_ce_anomaly_subscription`

### ce_cost

- `aws_ce_cost_allocation_tag`
- `aws_ce_cost_category`

### chatbot_slack

- `aws_chatbot_slack_channel_configuration`

### chatbot_teams

- `aws_chatbot_teams_channel_configuration`

### chimesdkvoice_sip

- `aws_chimesdkvoice_sip_media_application`
- `aws_chimesdkvoice_sip_rule`

### cleanrooms_collaboration

- `aws_cleanrooms_collaboration`

### cleanrooms_configured

- `aws_cleanrooms_configured_table`

### cleanrooms_membership

- `aws_cleanrooms_membership`

### cloud9_environment

- `aws_cloud9_environment_ec2`
- `aws_cloud9_environment_membership`

### cloudcontrolapi_resource

- `aws_cloudcontrolapi_resource`

### cloudformation_stack

- `aws_cloudformation_stack`
- `aws_cloudformation_stack_instances`
- `aws_cloudformation_stack_set`
- `aws_cloudformation_stack_set_instance`

### cloudformation_type

- `aws_cloudformation_type`

### cloudfront_distribution

- `aws_cloudfront_distribution`

### cloudfront_key

- `aws_cloudfront_key_value_store`

### cloudfront_multitenant

- `aws_cloudfront_multitenant_distribution`

### cloudfront_origin

- `aws_cloudfront_origin_access_control`
- `aws_cloudfront_origin_access_identity`
- `aws_cloudfront_origin_request_policy`

### cloudfront_public

- `aws_cloudfront_public_key`

### cloudfront_trust

- `aws_cloudfront_trust_store`

### cloudfrontkeyvaluestore_key

- `aws_cloudfrontkeyvaluestore_key`

### cloudfrontkeyvaluestore_keys

- `aws_cloudfrontkeyvaluestore_keys_exclusive`

### cloudhsm_v2

- `aws_cloudhsm_v2_cluster`
- `aws_cloudhsm_v2_hsm`

### cloudtrail

- `aws_cloudtrail`

### cloudtrail_organization

- `aws_cloudtrail_organization_delegated_admin_account`

### cloudwatch_composite

- `aws_cloudwatch_composite_alarm`

### cloudwatch_dashboard

- `aws_cloudwatch_dashboard`

### cloudwatch_event

- `aws_cloudwatch_event_rule`
- `aws_cloudwatch_event_target`

### cloudwatch_internet

- `aws_cloudwatch_internet_monitor`

### cloudwatch_log

- `aws_cloudwatch_log_anomaly_detector`
- `aws_cloudwatch_log_delivery`
- `aws_cloudwatch_log_delivery_destination`
- `aws_cloudwatch_log_delivery_source`
- `aws_cloudwatch_log_destination`
- `aws_cloudwatch_log_destination_policy`
- `aws_cloudwatch_log_group`
- `aws_cloudwatch_log_metric_filter`
- `aws_cloudwatch_log_resource_policy`
- `aws_cloudwatch_log_stream`
- `aws_cloudwatch_log_subscription_filter`

### cloudwatch_metric

- `aws_cloudwatch_metric_alarm`

### codeartifact_domain

- `aws_codeartifact_domain`

### codeartifact_repository

- `aws_codeartifact_repository`

### codebuild_report

- `aws_codebuild_report_group`

### codecatalyst_dev

- `aws_codecatalyst_dev_environment`

### codecatalyst_project

- `aws_codecatalyst_project`

### codecatalyst_source

- `aws_codecatalyst_source_repository`

### codecommit_repository

- `aws_codecommit_repository`

### codedeploy_app

- `aws_codedeploy_app`

### codedeploy_deployment

- `aws_codedeploy_deployment_config`
- `aws_codedeploy_deployment_group`

### codegurureviewer_repository

- `aws_codegurureviewer_repository_association`

### codepipeline

- `aws_codepipeline`

### codepipeline_custom

- `aws_codepipeline_custom_action_type`

### codepipeline_webhook

- `aws_codepipeline_webhook`

### codestarnotifications_notification

- `aws_codestarnotifications_notification_rule`

### cognito_identity

- `aws_cognito_identity_pool`
- `aws_cognito_identity_provider`

### cognito_managed

- `aws_cognito_managed_user_pool_client`

### cognito_resource

- `aws_cognito_resource_server`

### cognito_user

- `aws_cognito_user`
- `aws_cognito_user_group`
- `aws_cognito_user_in_group`
- `aws_cognito_user_pool`
- `aws_cognito_user_pool_client`

### comprehend_document

- `aws_comprehend_document_classifier`

### comprehend_entity

- `aws_comprehend_entity_recognizer`

### computeoptimizer_recommendation

- `aws_computeoptimizer_recommendation_preferences`

### config_aggregate

- `aws_config_aggregate_authorization`

### config_config

- `aws_config_config_rule`

### config_configuration

- `aws_config_configuration_aggregator`

### config_conformance

- `aws_config_conformance_pack`

### config_organization

- `aws_config_organization_conformance_pack`
- `aws_config_organization_custom_policy_rule`
- `aws_config_organization_custom_rule`
- `aws_config_organization_managed_rule`

### config_retention

- `aws_config_retention_configuration`

### connect_bot

- `aws_connect_bot_association`

### connect_contact

- `aws_connect_contact_flow`
- `aws_connect_contact_flow_module`

### connect_hours

- `aws_connect_hours_of_operation`

### connect_instance

- `aws_connect_instance`
- `aws_connect_instance_storage_config`

### connect_phone

- `aws_connect_phone_number`
- `aws_connect_phone_number_contact_flow_association`

### connect_queue

- `aws_connect_queue`

### connect_quick

- `aws_connect_quick_connect`

### connect_routing

- `aws_connect_routing_profile`

### connect_security

- `aws_connect_security_profile`

### connect_user

- `aws_connect_user`
- `aws_connect_user_hierarchy_group`

### connect_vocabulary

- `aws_connect_vocabulary`

### controltower_baseline

- `aws_controltower_baseline`

### controltower_control

- `aws_controltower_control`

### controltower_landing

- `aws_controltower_landing_zone`

### cur_report

- `aws_cur_report_definition`

### dataexchange_data

- `aws_dataexchange_data_set`

### dataexchange_event

- `aws_dataexchange_event_action`

### dataexchange_revision

- `aws_dataexchange_revision`
- `aws_dataexchange_revision_assets`

### datapipeline_pipeline

- `aws_datapipeline_pipeline`

### datasync_agent

- `aws_datasync_agent`

### datasync_location

- `aws_datasync_location_azure_blob`
- `aws_datasync_location_efs`
- `aws_datasync_location_fsx_lustre_file_system`
- `aws_datasync_location_fsx_ontap_file_system`
- `aws_datasync_location_fsx_openzfs_file_system`
- `aws_datasync_location_fsx_windows_file_system`
- `aws_datasync_location_hdfs`
- `aws_datasync_location_nfs`
- `aws_datasync_location_object_storage`
- `aws_datasync_location_s3`
- `aws_datasync_location_smb`

### datasync_task

- `aws_datasync_task`

### datazone_asset

- `aws_datazone_asset_type`

### datazone_domain

- `aws_datazone_domain`

### datazone_environment

- `aws_datazone_environment`
- `aws_datazone_environment_blueprint_configuration`
- `aws_datazone_environment_profile`

### datazone_form

- `aws_datazone_form_type`

### datazone_glossary

- `aws_datazone_glossary`
- `aws_datazone_glossary_term`

### datazone_project

- `aws_datazone_project`

### datazone_user

- `aws_datazone_user_profile`

### dax_cluster

- `aws_dax_cluster`

### dax_parameter

- `aws_dax_parameter_group`

### dax_subnet

- `aws_dax_subnet_group`

### db_cluster

- `aws_db_cluster_snapshot`

### db_event

- `aws_db_event_subscription`

### db_instance

- `aws_db_instance`
- `aws_db_instance_automated_backups_replication`
- `aws_db_instance_role_association`

### db_option

- `aws_db_option_group`

### db_parameter

- `aws_db_parameter_group`

### db_proxy

- `aws_db_proxy`
- `aws_db_proxy_default_target_group`
- `aws_db_proxy_endpoint`
- `aws_db_proxy_target`

### db_snapshot

- `aws_db_snapshot`

### db_subnet

- `aws_db_subnet_group`

### default_network

- `aws_default_network_acl`

### default_route

- `aws_default_route_table`

### default_security

- `aws_default_security_group`

### default_subnet

- `aws_default_subnet`

### default_vpc

- `aws_default_vpc`
- `aws_default_vpc_dhcp_options`

### devicefarm_device

- `aws_devicefarm_device_pool`

### devicefarm_instance

- `aws_devicefarm_instance_profile`

### devicefarm_network

- `aws_devicefarm_network_profile`

### devicefarm_project

- `aws_devicefarm_project`

### devicefarm_upload

- `aws_devicefarm_upload`

### devopsguru_notification

- `aws_devopsguru_notification_channel`

### devopsguru_resource

- `aws_devopsguru_resource_collection`

### directory_service

- `aws_directory_service_directory`
- `aws_directory_service_log_subscription`
- `aws_directory_service_radius_settings`
- `aws_directory_service_region`
- `aws_directory_service_shared_directory`
- `aws_directory_service_shared_directory_accepter`
- `aws_directory_service_trust`

### dms_certificate

- `aws_dms_certificate`

### dms_endpoint

- `aws_dms_endpoint`

### dms_event

- `aws_dms_event_subscription`

### dms_replication

- `aws_dms_replication_instance`
- `aws_dms_replication_subnet_group`
- `aws_dms_replication_task`

### dms_s3

- `aws_dms_s3_endpoint`

### docdb_cluster

- `aws_docdb_cluster`
- `aws_docdb_cluster_instance`
- `aws_docdb_cluster_parameter_group`
- `aws_docdb_cluster_snapshot`
- `aws_docdb_cluster_snapshot_copy`

### docdb_event

- `aws_docdb_event_subscription`

### docdb_global

- `aws_docdb_global_cluster`

### docdb_subnet

- `aws_docdb_subnet_group`

### docdbelastic_cluster

- `aws_docdbelastic_cluster`

### drs_replication

- `aws_drs_replication_configuration_template`

### dsql_cluster

- `aws_dsql_cluster`
- `aws_dsql_cluster_peering`

### dx_gateway

- `aws_dx_gateway`
- `aws_dx_gateway_association`

### dynamodb_tag

- `aws_dynamodb_tag`

### ebs_fast

- `aws_ebs_fast_snapshot_restore`

### ebs_snapshot

- `aws_ebs_snapshot`
- `aws_ebs_snapshot_copy`
- `aws_ebs_snapshot_import`

### ebs_volume

- `aws_ebs_volume`

### ec2_capacity

- `aws_ec2_capacity_block_reservation`
- `aws_ec2_capacity_reservation`
- `aws_ec2_capacity_reservation_fleet`

### ec2_carrier

- `aws_ec2_carrier_gateway`

### ec2_client

- `aws_ec2_client_vpn_authorization_rule`
- `aws_ec2_client_vpn_endpoint`
- `aws_ec2_client_vpn_network_association`
- `aws_ec2_client_vpn_route`

### ec2_default

- `aws_ec2_default_credit_specification`

### ec2_fleet

- `aws_ec2_fleet`

### ec2_host

- `aws_ec2_host`

### ec2_instance

- `aws_ec2_instance_connect_endpoint`
- `aws_ec2_instance_state`

### ec2_local

- `aws_ec2_local_gateway_route`
- `aws_ec2_local_gateway_route_table`
- `aws_ec2_local_gateway_route_table_virtual_interface_group_association`
- `aws_ec2_local_gateway_route_table_vpc_association`

### ec2_managed

- `aws_ec2_managed_prefix_list`
- `aws_ec2_managed_prefix_list_entry`

### ec2_network

- `aws_ec2_network_insights_analysis`
- `aws_ec2_network_insights_path`

### ec2_subnet

- `aws_ec2_subnet_cidr_reservation`

### ec2_tag

- `aws_ec2_tag`

### ec2_traffic

- `aws_ec2_traffic_mirror_filter`
- `aws_ec2_traffic_mirror_filter_rule`
- `aws_ec2_traffic_mirror_session`
- `aws_ec2_traffic_mirror_target`

### ec2_transit

- `aws_ec2_transit_gateway`
- `aws_ec2_transit_gateway_connect`
- `aws_ec2_transit_gateway_connect_peer`
- `aws_ec2_transit_gateway_default_route_table_association`
- `aws_ec2_transit_gateway_default_route_table_propagation`
- `aws_ec2_transit_gateway_multicast_domain`
- `aws_ec2_transit_gateway_multicast_domain_association`
- `aws_ec2_transit_gateway_multicast_group_member`
- `aws_ec2_transit_gateway_multicast_group_source`
- `aws_ec2_transit_gateway_peering_attachment`
- `aws_ec2_transit_gateway_peering_attachment_accepter`
- `aws_ec2_transit_gateway_policy_table_association`
- `aws_ec2_transit_gateway_prefix_list_reference`
- `aws_ec2_transit_gateway_route_table`
- `aws_ec2_transit_gateway_route_table_association`
- `aws_ec2_transit_gateway_route_table_propagation`
- `aws_ec2_transit_gateway_vpc_attachment`
- `aws_ec2_transit_gateway_vpc_attachment_accepter`
- `aws_ec2_transit_gateway_vpn_attachment`

### ecr_pull

- `aws_ecr_pull_through_cache_rule`

### ecr_repository

- `aws_ecr_repository`
- `aws_ecr_repository_creation_template`

### ecrpublic_repository

- `aws_ecrpublic_repository`

### ecs_account

- `aws_ecs_account_setting_default`

### ecs_cluster

- `aws_ecs_cluster`

### ecs_express

- `aws_ecs_express_gateway_service`

### ecs_service

- `aws_ecs_service`

### efs_access

- `aws_efs_access_point`

### efs_file

- `aws_efs_file_system`

### efs_mount

- `aws_efs_mount_target`

### efs_replication

- `aws_efs_replication_configuration`

### egress_only

- `aws_egress_only_internet_gateway`

### eks_access

- `aws_eks_access_entry`
- `aws_eks_access_policy_association`

### eks_addon

- `aws_eks_addon`

### eks_cluster

- `aws_eks_cluster`

### eks_fargate

- `aws_eks_fargate_profile`

### eks_identity

- `aws_eks_identity_provider_config`

### eks_node

- `aws_eks_node_group`

### eks_pod

- `aws_eks_pod_identity_association`

### elastic_beanstalk

- `aws_elastic_beanstalk_application_version`
- `aws_elastic_beanstalk_environment`

### elasticache_cluster

- `aws_elasticache_cluster`

### elasticache_global

- `aws_elasticache_global_replication_group`

### elasticache_parameter

- `aws_elasticache_parameter_group`

### elasticache_replication

- `aws_elasticache_replication_group`

### elasticache_reserved

- `aws_elasticache_reserved_cache_node`

### elasticache_serverless

- `aws_elasticache_serverless_cache`

### elasticache_subnet

- `aws_elasticache_subnet_group`

### elasticache_user

- `aws_elasticache_user`
- `aws_elasticache_user_group`
- `aws_elasticache_user_group_association`

### elastictranscoder_pipeline

- `aws_elastictranscoder_pipeline`

### elastictranscoder_preset

- `aws_elastictranscoder_preset`

### elb

- `aws_elb`

### emr_cluster

- `aws_emr_cluster`

### emr_instance

- `aws_emr_instance_fleet`
- `aws_emr_instance_group`

### emr_security

- `aws_emr_security_configuration`

### emr_studio

- `aws_emr_studio`
- `aws_emr_studio_session_mapping`

### emrcontainers_job

- `aws_emrcontainers_job_template`

### emrcontainers_virtual

- `aws_emrcontainers_virtual_cluster`

### emrserverless_application

- `aws_emrserverless_application`

### evidently_feature

- `aws_evidently_feature`

### evidently_launch

- `aws_evidently_launch`

### evidently_project

- `aws_evidently_project`

### evidently_segment

- `aws_evidently_segment`

### finspace_kx

- `aws_finspace_kx_dataview`
- `aws_finspace_kx_user`

### fis_experiment

- `aws_fis_experiment_template`

### fis_target

- `aws_fis_target_account_configuration`

### flow_log

- `aws_flow_log`

### fms_admin

- `aws_fms_admin_account`

### fms_policy

- `aws_fms_policy`

### fsx_backup

- `aws_fsx_backup`

### fsx_lustre

- `aws_fsx_lustre_file_system`

### fsx_ontap

- `aws_fsx_ontap_file_system`
- `aws_fsx_ontap_storage_virtual_machine`
- `aws_fsx_ontap_volume`

### fsx_openzfs

- `aws_fsx_openzfs_file_system`
- `aws_fsx_openzfs_snapshot`
- `aws_fsx_openzfs_volume`

### fsx_s3

- `aws_fsx_s3_access_point_attachment`

### fsx_windows

- `aws_fsx_windows_file_system`

### gamelift_alias

- `aws_gamelift_alias`

### gamelift_build

- `aws_gamelift_build`

### gamelift_fleet

- `aws_gamelift_fleet`

### gamelift_game

- `aws_gamelift_game_server_group`
- `aws_gamelift_game_session_queue`

### gamelift_script

- `aws_gamelift_script`

### glacier_vault

- `aws_glacier_vault`

### globalaccelerator_accelerator

- `aws_globalaccelerator_accelerator`

### globalaccelerator_cross

- `aws_globalaccelerator_cross_account_attachment`

### globalaccelerator_custom

- `aws_globalaccelerator_custom_routing_accelerator`
- `aws_globalaccelerator_custom_routing_endpoint_group`
- `aws_globalaccelerator_custom_routing_listener`

### globalaccelerator_endpoint

- `aws_globalaccelerator_endpoint_group`

### globalaccelerator_listener

- `aws_globalaccelerator_listener`

### glue_catalog

- `aws_glue_catalog_database`
- `aws_glue_catalog_table`
- `aws_glue_catalog_table_optimizer`

### glue_classifier

- `aws_glue_classifier`

### glue_connection

- `aws_glue_connection`

### glue_crawler

- `aws_glue_crawler`

### glue_job

- `aws_glue_job`

### glue_partition

- `aws_glue_partition`
- `aws_glue_partition_index`

### glue_registry

- `aws_glue_registry`

### glue_schema

- `aws_glue_schema`

### glue_security

- `aws_glue_security_configuration`

### glue_user

- `aws_glue_user_defined_function`

### glue_workflow

- `aws_glue_workflow`

### grafana_role

- `aws_grafana_role_association`

### grafana_workspace

- `aws_grafana_workspace`
- `aws_grafana_workspace_api_key`
- `aws_grafana_workspace_service_account`
- `aws_grafana_workspace_service_account_token`

### guardduty_detector

- `aws_guardduty_detector`

### guardduty_filter

- `aws_guardduty_filter`

### guardduty_invite

- `aws_guardduty_invite_accepter`

### guardduty_ipset

- `aws_guardduty_ipset`

### guardduty_member

- `aws_guardduty_member`

### guardduty_organization

- `aws_guardduty_organization_admin_account`

### guardduty_threatintelset

- `aws_guardduty_threatintelset`

### iam_access

- `aws_iam_access_key`

### iam_account

- `aws_iam_account_alias`

### iam_group

- `aws_iam_group`
- `aws_iam_group_membership`
- `aws_iam_group_policies_exclusive`
- `aws_iam_group_policy`
- `aws_iam_group_policy_attachment`
- `aws_iam_group_policy_attachments_exclusive`

### iam_policy

- `aws_iam_policy`

### iam_role

- `aws_iam_role`
- `aws_iam_role_policies_exclusive`
- `aws_iam_role_policy`
- `aws_iam_role_policy_attachment`
- `aws_iam_role_policy_attachments_exclusive`

### iam_server

- `aws_iam_server_certificate`

### iam_service

- `aws_iam_service_linked_role`

### iam_signing

- `aws_iam_signing_certificate`

### iam_user

- `aws_iam_user`
- `aws_iam_user_group_membership`
- `aws_iam_user_policies_exclusive`
- `aws_iam_user_policy`
- `aws_iam_user_policy_attachment`
- `aws_iam_user_policy_attachments_exclusive`
- `aws_iam_user_ssh_key`

### iam_virtual

- `aws_iam_virtual_mfa_device`

### identitystore_group

- `aws_identitystore_group`
- `aws_identitystore_group_membership`

### identitystore_user

- `aws_identitystore_user`

### imagebuilder_component

- `aws_imagebuilder_component`

### imagebuilder_container

- `aws_imagebuilder_container_recipe`

### imagebuilder_distribution

- `aws_imagebuilder_distribution_configuration`

### imagebuilder_image

- `aws_imagebuilder_image`
- `aws_imagebuilder_image_pipeline`
- `aws_imagebuilder_image_recipe`

### imagebuilder_infrastructure

- `aws_imagebuilder_infrastructure_configuration`

### imagebuilder_lifecycle

- `aws_imagebuilder_lifecycle_policy`

### imagebuilder_workflow

- `aws_imagebuilder_workflow`

### inspector2_delegated

- `aws_inspector2_delegated_admin_account`

### inspector2_filter

- `aws_inspector2_filter`

### inspector2_member

- `aws_inspector2_member_association`

### inspector_assessment

- `aws_inspector_assessment_target`
- `aws_inspector_assessment_template`

### inspector_resource

- `aws_inspector_resource_group`

### instance

- `aws_instance`

### internet_gateway

- `aws_internet_gateway`
- `aws_internet_gateway_attachment`

### internetmonitor_monitor

- `aws_internetmonitor_monitor`

### invoicing_invoice

- `aws_invoicing_invoice_unit`

### iot_authorizer

- `aws_iot_authorizer`

### iot_billing

- `aws_iot_billing_group`

### iot_ca

- `aws_iot_ca_certificate`

### iot_certificate

- `aws_iot_certificate`

### iot_domain

- `aws_iot_domain_configuration`

### iot_policy

- `aws_iot_policy`
- `aws_iot_policy_attachment`

### iot_provisioning

- `aws_iot_provisioning_template`

### iot_role

- `aws_iot_role_alias`

### iot_thing

- `aws_iot_thing`
- `aws_iot_thing_group`
- `aws_iot_thing_group_membership`
- `aws_iot_thing_principal_attachment`
- `aws_iot_thing_type`

### iot_topic

- `aws_iot_topic_rule`
- `aws_iot_topic_rule_destination`

### ivs_channel

- `aws_ivs_channel`

### ivs_playback

- `aws_ivs_playback_key_pair`

### ivs_recording

- `aws_ivs_recording_configuration`

### keyspaces_keyspace

- `aws_keyspaces_keyspace`

### keyspaces_table

- `aws_keyspaces_table`

### kinesis_stream

- `aws_kinesis_stream`
- `aws_kinesis_stream_consumer`

### kinesis_video

- `aws_kinesis_video_stream`

### kinesisanalyticsv2_application

- `aws_kinesisanalyticsv2_application`
- `aws_kinesisanalyticsv2_application_snapshot`

### kms_alias

- `aws_kms_alias`

### kms_ciphertext

- `aws_kms_ciphertext`

### kms_custom

- `aws_kms_custom_key_store`

### kms_external

- `aws_kms_external_key`

### kms_grant

- `aws_kms_grant`

### kms_key

- `aws_kms_key`
- `aws_kms_key_policy`

### kms_replica

- `aws_kms_replica_external_key`
- `aws_kms_replica_key`

### lakeformation_data

- `aws_lakeformation_data_cells_filter`

### lakeformation_lf

- `aws_lakeformation_lf_tag`
- `aws_lakeformation_lf_tag_expression`

### lakeformation_resource

- `aws_lakeformation_resource_lf_tag`

### lambda_alias

- `aws_lambda_alias`

### lambda_capacity

- `aws_lambda_capacity_provider`

### lambda_code

- `aws_lambda_code_signing_config`

### lambda_event

- `aws_lambda_event_source_mapping`

### lambda_function

- `aws_lambda_function`
- `aws_lambda_function_event_invoke_config`
- `aws_lambda_function_url`

### lambda_invocation

- `aws_lambda_invocation`

### lambda_layer

- `aws_lambda_layer_version`
- `aws_lambda_layer_version_permission`

### lambda_provisioned

- `aws_lambda_provisioned_concurrency_config`

### launch_configuration

- `aws_launch_configuration`

### launch_template

- `aws_launch_template`

### lb

- `aws_lb`

### lb_cookie

- `aws_lb_cookie_stickiness_policy`

### lb_listener

- `aws_lb_listener`
- `aws_lb_listener_certificate`
- `aws_lb_listener_rule`

### lb_ssl

- `aws_lb_ssl_negotiation_policy`

### lb_target

- `aws_lb_target_group`

### lex_bot

- `aws_lex_bot`
- `aws_lex_bot_alias`

### lex_intent

- `aws_lex_intent`

### lex_slot

- `aws_lex_slot_type`

### licensemanager_association

- `aws_licensemanager_association`

### licensemanager_license

- `aws_licensemanager_license_configuration`

### lightsail_database

- `aws_lightsail_database`

### lightsail_disk

- `aws_lightsail_disk`
- `aws_lightsail_disk_attachment`

### lightsail_domain

- `aws_lightsail_domain`
- `aws_lightsail_domain_entry`

### lightsail_instance

- `aws_lightsail_instance`

### lightsail_key

- `aws_lightsail_key_pair`

### lightsail_lb

- `aws_lightsail_lb`
- `aws_lightsail_lb_attachment`
- `aws_lightsail_lb_certificate`
- `aws_lightsail_lb_https_redirection_policy`
- `aws_lightsail_lb_stickiness_policy`

### lightsail_static

- `aws_lightsail_static_ip`
- `aws_lightsail_static_ip_attachment`

### load_balancer

- `aws_load_balancer_backend_server_policy`
- `aws_load_balancer_listener_policy`

### location_geofence

- `aws_location_geofence_collection`

### location_map

- `aws_location_map`

### location_place

- `aws_location_place_index`

### location_route

- `aws_location_route_calculator`

### location_tracker

- `aws_location_tracker`
- `aws_location_tracker_association`

### m2_application

- `aws_m2_application`

### m2_deployment

- `aws_m2_deployment`

### m2_environment

- `aws_m2_environment`

### macie2_custom

- `aws_macie2_custom_data_identifier`

### macie2_findings

- `aws_macie2_findings_filter`

### macie2_invitation

- `aws_macie2_invitation_accepter`

### macie2_organization

- `aws_macie2_organization_admin_account`

### main_route

- `aws_main_route_table_association`

### media_convert

- `aws_media_convert_queue`

### media_package

- `aws_media_package_channel`

### media_packagev2

- `aws_media_packagev2_channel_group`

### media_store

- `aws_media_store_container`

### medialive_channel

- `aws_medialive_channel`

### medialive_input

- `aws_medialive_input`
- `aws_medialive_input_security_group`

### medialive_multiplex

- `aws_medialive_multiplex`
- `aws_medialive_multiplex_program`

### memorydb_acl

- `aws_memorydb_acl`

### memorydb_cluster

- `aws_memorydb_cluster`

### memorydb_multi

- `aws_memorydb_multi_region_cluster`

### memorydb_parameter

- `aws_memorydb_parameter_group`

### memorydb_snapshot

- `aws_memorydb_snapshot`

### memorydb_subnet

- `aws_memorydb_subnet_group`

### memorydb_user

- `aws_memorydb_user`

### mq_broker

- `aws_mq_broker`

### msk_cluster

- `aws_msk_cluster`

### msk_configuration

- `aws_msk_configuration`

### msk_replicator

- `aws_msk_replicator`

### msk_scram

- `aws_msk_scram_secret_association`

### msk_serverless

- `aws_msk_serverless_cluster`

### msk_single

- `aws_msk_single_scram_secret_association`

### msk_vpc

- `aws_msk_vpc_connection`

### mskconnect_connector

- `aws_mskconnect_connector`

### mskconnect_custom

- `aws_mskconnect_custom_plugin`

### mskconnect_worker

- `aws_mskconnect_worker_configuration`

### mwaa_environment

- `aws_mwaa_environment`

### nat_gateway

- `aws_nat_gateway`
- `aws_nat_gateway_eip_association`

### neptune_cluster

- `aws_neptune_cluster`
- `aws_neptune_cluster_endpoint`
- `aws_neptune_cluster_parameter_group`
- `aws_neptune_cluster_snapshot`

### neptune_event

- `aws_neptune_event_subscription`

### neptune_global

- `aws_neptune_global_cluster`

### neptune_parameter

- `aws_neptune_parameter_group`

### neptune_subnet

- `aws_neptune_subnet_group`

### neptunegraph_graph

- `aws_neptunegraph_graph`

### network_acl

- `aws_network_acl`
- `aws_network_acl_association`
- `aws_network_acl_rule`

### network_interface

- `aws_network_interface`
- `aws_network_interface_attachment`
- `aws_network_interface_permission`
- `aws_network_interface_sg_attachment`

### networkfirewall_firewall

- `aws_networkfirewall_firewall`
- `aws_networkfirewall_firewall_policy`

### networkfirewall_rule

- `aws_networkfirewall_rule_group`

### networkfirewall_tls

- `aws_networkfirewall_tls_inspection_configuration`

### networkflowmonitor_monitor

- `aws_networkflowmonitor_monitor`

### networkflowmonitor_scope

- `aws_networkflowmonitor_scope`

### networkmanager_connect

- `aws_networkmanager_connect_peer`

### networkmanager_core

- `aws_networkmanager_core_network`

### networkmanager_device

- `aws_networkmanager_device`

### networkmanager_dx

- `aws_networkmanager_dx_gateway_attachment`

### networkmanager_global

- `aws_networkmanager_global_network`

### networkmanager_site

- `aws_networkmanager_site`

### networkmanager_transit

- `aws_networkmanager_transit_gateway_registration`

### networkmonitor_monitor

- `aws_networkmonitor_monitor`

### notifications_channel

- `aws_notifications_channel_association`

### notifications_event

- `aws_notifications_event_rule`

### notifications_notification

- `aws_notifications_notification_configuration`
- `aws_notifications_notification_hub`

### notificationscontacts_email

- `aws_notificationscontacts_email_contact`

### observabilityadmin_centralization

- `aws_observabilityadmin_centralization_rule_for_organization`

### odb_cloud

- `aws_odb_cloud_autonomous_vm_cluster`
- `aws_odb_cloud_exadata_infrastructure`
- `aws_odb_cloud_vm_cluster`

### odb_network

- `aws_odb_network`
- `aws_odb_network_peering_connection`

### organizations_account

- `aws_organizations_account`

### organizations_delegated

- `aws_organizations_delegated_administrator`

### organizations_policy

- `aws_organizations_policy`
- `aws_organizations_policy_attachment`

### organizations_tag

- `aws_organizations_tag`

### paymentcryptography_key

- `aws_paymentcryptography_key`
- `aws_paymentcryptography_key_alias`

### pinpointsmsvoicev2_configuration

- `aws_pinpointsmsvoicev2_configuration_set`

### pinpointsmsvoicev2_opt

- `aws_pinpointsmsvoicev2_opt_out_list`

### pinpointsmsvoicev2_phone

- `aws_pinpointsmsvoicev2_phone_number`

### pipes_pipe

- `aws_pipes_pipe`

### prometheus_rule

- `aws_prometheus_rule_group_namespace`

### prometheus_scraper

- `aws_prometheus_scraper`

### prometheus_workspace

- `aws_prometheus_workspace`

### qbusiness_application

- `aws_qbusiness_application`

### quicksight_analysis

- `aws_quicksight_analysis`

### quicksight_dashboard

- `aws_quicksight_dashboard`

### quicksight_data

- `aws_quicksight_data_set`
- `aws_quicksight_data_source`

### quicksight_folder

- `aws_quicksight_folder`

### quicksight_group

- `aws_quicksight_group`
- `aws_quicksight_group_membership`

### quicksight_iam

- `aws_quicksight_iam_policy_assignment`

### quicksight_ingestion

- `aws_quicksight_ingestion`

### quicksight_namespace

- `aws_quicksight_namespace`

### quicksight_role

- `aws_quicksight_role_membership`

### quicksight_template

- `aws_quicksight_template`
- `aws_quicksight_template_alias`

### quicksight_theme

- `aws_quicksight_theme`

### quicksight_user

- `aws_quicksight_user`

### ram_principal

- `aws_ram_principal_association`

### ram_resource

- `aws_ram_resource_association`
- `aws_ram_resource_share`

### rds_certificate

- `aws_rds_certificate`

### rds_cluster

- `aws_rds_cluster`
- `aws_rds_cluster_activity_stream`
- `aws_rds_cluster_endpoint`
- `aws_rds_cluster_instance`
- `aws_rds_cluster_parameter_group`
- `aws_rds_cluster_role_association`
- `aws_rds_cluster_snapshot_copy`

### rds_custom

- `aws_rds_custom_db_engine_version`

### rds_export

- `aws_rds_export_task`

### rds_global

- `aws_rds_global_cluster`

### rds_instance

- `aws_rds_instance_state`

### rds_integration

- `aws_rds_integration`

### rds_reserved

- `aws_rds_reserved_instance`

### redshift_cluster

- `aws_redshift_cluster`
- `aws_redshift_cluster_iam_roles`
- `aws_redshift_cluster_snapshot`

### redshift_data

- `aws_redshift_data_share_authorization`
- `aws_redshift_data_share_consumer_association`

### redshift_endpoint

- `aws_redshift_endpoint_access`
- `aws_redshift_endpoint_authorization`

### redshift_event

- `aws_redshift_event_subscription`

### redshift_hsm

- `aws_redshift_hsm_client_certificate`
- `aws_redshift_hsm_configuration`

### redshift_integration

- `aws_redshift_integration`

### redshift_parameter

- `aws_redshift_parameter_group`

### redshift_scheduled

- `aws_redshift_scheduled_action`

### redshift_snapshot

- `aws_redshift_snapshot_copy`
- `aws_redshift_snapshot_copy_grant`
- `aws_redshift_snapshot_schedule`
- `aws_redshift_snapshot_schedule_association`

### redshift_subnet

- `aws_redshift_subnet_group`

### redshift_usage

- `aws_redshift_usage_limit`

### redshiftserverless_custom

- `aws_redshiftserverless_custom_domain_association`

### redshiftserverless_endpoint

- `aws_redshiftserverless_endpoint_access`

### redshiftserverless_namespace

- `aws_redshiftserverless_namespace`

### redshiftserverless_snapshot

- `aws_redshiftserverless_snapshot`

### redshiftserverless_usage

- `aws_redshiftserverless_usage_limit`

### redshiftserverless_workgroup

- `aws_redshiftserverless_workgroup`

### rekognition_collection

- `aws_rekognition_collection`

### rekognition_project

- `aws_rekognition_project`

### rekognition_stream

- `aws_rekognition_stream_processor`

### resourceexplorer2_view

- `aws_resourceexplorer2_view`

### resourcegroups_group

- `aws_resourcegroups_group`

### rolesanywhere_profile

- `aws_rolesanywhere_profile`

### rolesanywhere_trust

- `aws_rolesanywhere_trust_anchor`

### route

- `aws_route`

### route53_cidr

- `aws_route53_cidr_collection`
- `aws_route53_cidr_location`

### route53_health

- `aws_route53_health_check`

### route53_query

- `aws_route53_query_log`

### route53_record

- `aws_route53_record`

### route53_records

- `aws_route53_records_exclusive`

### route53_resolver

- `aws_route53_resolver_config`
- `aws_route53_resolver_dnssec_config`
- `aws_route53_resolver_endpoint`
- `aws_route53_resolver_firewall_config`
- `aws_route53_resolver_firewall_domain_list`
- `aws_route53_resolver_firewall_rule_group`
- `aws_route53_resolver_firewall_rule_group_association`
- `aws_route53_resolver_query_log_config`
- `aws_route53_resolver_query_log_config_association`
- `aws_route53_resolver_rule`
- `aws_route53_resolver_rule_association`

### route53_zone

- `aws_route53_zone`

### route53domains_domain

- `aws_route53domains_domain`

### route53domains_registered

- `aws_route53domains_registered_domain`

### route53profiles_association

- `aws_route53profiles_association`

### route53profiles_profile

- `aws_route53profiles_profile`

### route53profiles_resource

- `aws_route53profiles_resource_association`

### route53recoverycontrolconfig_cluster

- `aws_route53recoverycontrolconfig_cluster`

### route53recoverycontrolconfig_control

- `aws_route53recoverycontrolconfig_control_panel`

### route53recoverycontrolconfig_routing

- `aws_route53recoverycontrolconfig_routing_control`

### route53recoverycontrolconfig_safety

- `aws_route53recoverycontrolconfig_safety_rule`

### route53recoveryreadiness_cell

- `aws_route53recoveryreadiness_cell`

### route53recoveryreadiness_readiness

- `aws_route53recoveryreadiness_readiness_check`

### route53recoveryreadiness_recovery

- `aws_route53recoveryreadiness_recovery_group`

### route53recoveryreadiness_resource

- `aws_route53recoveryreadiness_resource_set`

### route_table

- `aws_route_table`
- `aws_route_table_association`

### rum_app

- `aws_rum_app_monitor`

### s3_bucket

- `aws_s3_bucket`

### s3_directory

- `aws_s3_directory_bucket`

### s3outposts_endpoint

- `aws_s3outposts_endpoint`

### s3tables_namespace

- `aws_s3tables_namespace`

### s3tables_table

- `aws_s3tables_table`
- `aws_s3tables_table_bucket`
- `aws_s3tables_table_replication`

### s3vectors_index

- `aws_s3vectors_index`

### s3vectors_vector

- `aws_s3vectors_vector_bucket`

### sagemaker_app

- `aws_sagemaker_app`
- `aws_sagemaker_app_image_config`

### sagemaker_code

- `aws_sagemaker_code_repository`

### sagemaker_data

- `aws_sagemaker_data_quality_job_definition`

### sagemaker_device

- `aws_sagemaker_device`
- `aws_sagemaker_device_fleet`

### sagemaker_domain

- `aws_sagemaker_domain`

### sagemaker_endpoint

- `aws_sagemaker_endpoint`

### sagemaker_feature

- `aws_sagemaker_feature_group`

### sagemaker_flow

- `aws_sagemaker_flow_definition`

### sagemaker_human

- `aws_sagemaker_human_task_ui`

### sagemaker_image

- `aws_sagemaker_image`
- `aws_sagemaker_image_version`

### sagemaker_mlflow

- `aws_sagemaker_mlflow_tracking_server`

### sagemaker_model

- `aws_sagemaker_model`
- `aws_sagemaker_model_package_group`

### sagemaker_monitoring

- `aws_sagemaker_monitoring_schedule`

### sagemaker_notebook

- `aws_sagemaker_notebook_instance`
- `aws_sagemaker_notebook_instance_lifecycle_configuration`

### sagemaker_pipeline

- `aws_sagemaker_pipeline`

### sagemaker_space

- `aws_sagemaker_space`

### sagemaker_studio

- `aws_sagemaker_studio_lifecycle_config`

### sagemaker_user

- `aws_sagemaker_user_profile`

### sagemaker_workforce

- `aws_sagemaker_workforce`

### sagemaker_workteam

- `aws_sagemaker_workteam`

### scheduler_schedule

- `aws_scheduler_schedule`
- `aws_scheduler_schedule_group`

### schemas_discoverer

- `aws_schemas_discoverer`

### schemas_registry

- `aws_schemas_registry`

### schemas_schema

- `aws_schemas_schema`

### secretsmanager_secret

- `aws_secretsmanager_secret`

### security_group

- `aws_security_group`
- `aws_security_group_rule`

### securityhub_action

- `aws_securityhub_action_target`

### securityhub_configuration

- `aws_securityhub_configuration_policy`
- `aws_securityhub_configuration_policy_association`

### securityhub_standards

- `aws_securityhub_standards_control`
- `aws_securityhub_standards_control_association`

### securitylake_aws

- `aws_securitylake_aws_log_source`

### securitylake_custom

- `aws_securitylake_custom_log_source`

### securitylake_subscriber

- `aws_securitylake_subscriber`

### serverlessapplicationrepository_cloudformation

- `aws_serverlessapplicationrepository_cloudformation_stack`

### service_discovery

- `aws_service_discovery_http_namespace`
- `aws_service_discovery_instance`
- `aws_service_discovery_private_dns_namespace`
- `aws_service_discovery_public_dns_namespace`
- `aws_service_discovery_service`

### servicecatalog_constraint

- `aws_servicecatalog_constraint`

### servicecatalog_portfolio

- `aws_servicecatalog_portfolio`

### servicecatalog_product

- `aws_servicecatalog_product`

### servicecatalog_service

- `aws_servicecatalog_service_action`

### servicecatalog_tag

- `aws_servicecatalog_tag_option`

### servicecatalogappregistry_application

- `aws_servicecatalogappregistry_application`

### servicecatalogappregistry_attribute

- `aws_servicecatalogappregistry_attribute_group`

### servicequotas_service

- `aws_servicequotas_service_quota`

### sesv2_tenant

- `aws_sesv2_tenant`

### sfn_activity

- `aws_sfn_activity`

### sfn_state

- `aws_sfn_state_machine`

### shield_protection

- `aws_shield_protection`

### signer_signing

- `aws_signer_signing_job`
- `aws_signer_signing_profile`

### simpledb_domain

- `aws_simpledb_domain`

### sns_platform

- `aws_sns_platform_application`

### sns_topic

- `aws_sns_topic`
- `aws_sns_topic_subscription`

### spot_fleet

- `aws_spot_fleet_request`

### spot_instance

- `aws_spot_instance_request`

### ssm_activation

- `aws_ssm_activation`

### ssm_association

- `aws_ssm_association`

### ssm_document

- `aws_ssm_document`

### ssm_maintenance

- `aws_ssm_maintenance_window`
- `aws_ssm_maintenance_window_target`
- `aws_ssm_maintenance_window_task`

### ssm_parameter

- `aws_ssm_parameter`

### ssm_patch

- `aws_ssm_patch_baseline`

### ssm_resource

- `aws_ssm_resource_data_sync`

### ssmcontacts_contact

- `aws_ssmcontacts_contact`
- `aws_ssmcontacts_contact_channel`

### ssmcontacts_rotation

- `aws_ssmcontacts_rotation`

### ssmincidents_response

- `aws_ssmincidents_response_plan`

### ssoadmin_account

- `aws_ssoadmin_account_assignment`

### ssoadmin_application

- `aws_ssoadmin_application`
- `aws_ssoadmin_application_access_scope`
- `aws_ssoadmin_application_assignment`

### ssoadmin_instances

- `aws_ssoadmin_instances`

### ssoadmin_permission

- `aws_ssoadmin_permission_set`

### ssoadmin_trusted

- `aws_ssoadmin_trusted_token_issuer`

### subnet

- `aws_subnet`

### swf_domain

- `aws_swf_domain`

### timestreaminfluxdb_db

- `aws_timestreaminfluxdb_db_cluster`
- `aws_timestreaminfluxdb_db_instance`

### timestreamquery_scheduled

- `aws_timestreamquery_scheduled_query`

### transfer_access

- `aws_transfer_access`

### transfer_agreement

- `aws_transfer_agreement`

### transfer_certificate

- `aws_transfer_certificate`

### transfer_connector

- `aws_transfer_connector`

### transfer_profile

- `aws_transfer_profile`

### transfer_server

- `aws_transfer_server`

### transfer_user

- `aws_transfer_user`

### transfer_web

- `aws_transfer_web_app`

### transfer_workflow

- `aws_transfer_workflow`

### verifiedaccess_endpoint

- `aws_verifiedaccess_endpoint`

### verifiedaccess_group

- `aws_verifiedaccess_group`

### verifiedaccess_instance

- `aws_verifiedaccess_instance`
- `aws_verifiedaccess_instance_logging_configuration`
- `aws_verifiedaccess_instance_trust_provider_attachment`

### verifiedaccess_trust

- `aws_verifiedaccess_trust_provider`

### verifiedpermissions_identity

- `aws_verifiedpermissions_identity_source`

### verifiedpermissions_policy

- `aws_verifiedpermissions_policy`
- `aws_verifiedpermissions_policy_store`
- `aws_verifiedpermissions_policy_template`

### volume_attachment

- `aws_volume_attachment`

### vpc

- `aws_vpc`

### vpc_dhcp

- `aws_vpc_dhcp_options`

### vpc_endpoint

- `aws_vpc_endpoint`
- `aws_vpc_endpoint_connection_accepter`
- `aws_vpc_endpoint_connection_notification`
- `aws_vpc_endpoint_policy`
- `aws_vpc_endpoint_private_dns`
- `aws_vpc_endpoint_route_table_association`
- `aws_vpc_endpoint_security_group_association`
- `aws_vpc_endpoint_service`
- `aws_vpc_endpoint_service_private_dns_verification`

### vpc_ipam

- `aws_vpc_ipam`
- `aws_vpc_ipam_pool`
- `aws_vpc_ipam_pool_cidr`
- `aws_vpc_ipam_pool_cidr_allocation`
- `aws_vpc_ipam_resource_discovery`
- `aws_vpc_ipam_resource_discovery_association`
- `aws_vpc_ipam_scope`

### vpc_ipv4

- `aws_vpc_ipv4_cidr_block_association`

### vpc_ipv6

- `aws_vpc_ipv6_cidr_block_association`

### vpc_peering

- `aws_vpc_peering_connection`
- `aws_vpc_peering_connection_accepter`
- `aws_vpc_peering_connection_options`

### vpc_route

- `aws_vpc_route_server`
- `aws_vpc_route_server_endpoint`
- `aws_vpc_route_server_peer`

### vpc_security

- `aws_vpc_security_group_egress_rule`
- `aws_vpc_security_group_ingress_rule`
- `aws_vpc_security_group_vpc_association`

### vpclattice_access

- `aws_vpclattice_access_log_subscription`

### vpclattice_listener

- `aws_vpclattice_listener`
- `aws_vpclattice_listener_rule`

### vpclattice_service

- `aws_vpclattice_service`
- `aws_vpclattice_service_network`
- `aws_vpclattice_service_network_service_association`
- `aws_vpclattice_service_network_vpc_association`

### vpclattice_target

- `aws_vpclattice_target_group`

### vpn_concentrator

- `aws_vpn_concentrator`

### waf_byte

- `aws_waf_byte_match_set`

### waf_geo

- `aws_waf_geo_match_set`

### waf_ipset

- `aws_waf_ipset`

### waf_rate

- `aws_waf_rate_based_rule`

### waf_regex

- `aws_waf_regex_match_set`
- `aws_waf_regex_pattern_set`

### waf_rule

- `aws_waf_rule`
- `aws_waf_rule_group`

### waf_size

- `aws_waf_size_constraint_set`

### waf_sql

- `aws_waf_sql_injection_match_set`

### waf_web

- `aws_waf_web_acl`

### waf_xss

- `aws_waf_xss_match_set`

### workspaces_directory

- `aws_workspaces_directory`

### workspaces_ip

- `aws_workspaces_ip_group`

### workspaces_workspace

- `aws_workspaces_workspace`

### workspacesweb_data

- `aws_workspacesweb_data_protection_settings`
- `aws_workspacesweb_data_protection_settings_association`

### workspacesweb_session

- `aws_workspacesweb_session_logger`
- `aws_workspacesweb_session_logger_association`

### xray_group

- `aws_xray_group`

### xray_sampling

- `aws_xray_sampling_rule`

## Verification Details

This verification checked:

1. **Client Name Validity:** Whether the boto3 client name exists
2. **Method Existence:** Whether the specified API method exists on the client
3. **Pagination Support:** Whether the method supports pagination (informational)
4. **Field Completeness:** Whether required fields (topkey, key) are present

**Note:** This verification does NOT test:
- Actual API calls (would require AWS credentials and permissions)
- Response structure validation (topkey correctness)
- Key field existence in API responses
- Filter ID validity

For complete validation, manual testing with actual AWS resources is required.
