# AWS Dictionary Verification Summary Report

**Source:** aws_dict_verification2.md
**Generated:** Sat Jan 17 15:00:41 GMT 2026

## Overall Statistics

- **Total Resources in aws_dict.py:** 1611
- **Resources Tested:** 1608
- **Resources Skipped:** 3

## Test Results

| Category | Count | Percentage |
|----------|-------|------------|
| ✅ Valid | 731 | 45.5% |
| ⚠️  Warnings | 158 | 9.8% |
| ❌ Errors | 127 | 7.9% |
| 🔒 Permission Errors | 20 | 1.2% |
| 🔴 API Errors | 572 | 35.6% |

## Error Type Breakdown

| Error Type | Count | Description |
|------------|-------|-------------|
| Requires Parameters | 230 | Resources needing parent IDs (needid_dict.py) |
| Method Not Found | 127 | Invalid boto3 method names |
| Incorrect topkey | 124 | Response structure mismatch |
| Missing key Field | 31 | Key field not in API response |
| Permission Denied | 20 | IAM permissions needed |
| Other API Errors | 572 | Various API failures |

## Priority Actions

### Priority 1: Fix Method Names (127 resources)

These resources have incorrect boto3 method names and need immediate correction:

- **Method:** `list_key_registrations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_vpn_gateway_attachments` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_principal_portfolio_associations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_configuration_sets` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_invitation_accepters` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_apns_voip_sandbox_channels` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_resolver_rules` - Used by: `aws_finspace_kx_cluster`
- **Method:** `get_service_catalog_portfolio_status` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_ssh_public_keys` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_baidu_channels` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_instance_access_control_attribute_configuration` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_transit_gateway_route_tables` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_apns_voip_channels` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_folder_memberships` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_templates` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_finding_aggregators` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_drt_access_log_bucket_associations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_core_network_policy_attachments` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_scaling_groups` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_domain_identity_verification` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_vpc_attachments` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_vpc_endpoint_subnet_associations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_site_to_site_vpn_attachments` - Used by: `aws_finspace_kx_cluster`
- **Method:** `get_sms_preferences` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_packages` - Used by: `aws_finspace_kx_cluster`, `aws_opensearch_package_association`
- **Method:** `describe_standards_subscriptions` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_web_acl_associations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_resolver_firewall_rules` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_indices` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_vpn_gateway_route_propagations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_template_associations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_apns_channels` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_organization_admin_account` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_domain_identity` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_email_identity` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_permissions_boundary_attachments` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_volumes` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_resources` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_product_portfolio_associations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_data_lakes` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_identity_notification_topic` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_product_subscriptions` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_insights` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_create_volume_permissions` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_customer_gateway_associations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_invite_accepters` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_receipt_filter` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_inbound_connection_accepters` - Used by: `aws_finspace_kx_cluster`, `aws_opensearch_outbound_connection`
- **Method:** `list_databases` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_sms_channels` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_transit_gateway_peerings` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_transit_gateway_connect_peers` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_drt_access_role_arn_associations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_resource_policies` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_resource_share_accepters` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_route_server_associations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_route_server_vpc_associations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_managed_policy_attachments` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_tape_pools` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_metrics_destinations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_template` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_adm_channels` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_resource_gateways` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_logging_configurations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_link_associations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_patch_groups` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_application_layer_automatic_response_associations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_identity_policy` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_account_subscriptions` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_connections` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_route_server_propagations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_dhcp_options_associations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `get_registry_policy` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_budget_resource_associations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_members` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_provisioned_products` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_email_channels` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_group_associations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_tag_option_resource_associations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_vpn_connection_routes` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_organization_access` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_attribute_group_associations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_permission_set_inline_policies` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_domain_dkim` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_links` - Used by: `aws_finspace_kx_cluster`, `aws_networkmanager_link_association`, `aws_oam_sink` and 1 more
- **Method:** `list_apns_sandbox_channels` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_connect_attachments` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_db_cluster_instances` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_network_insights_path_subscriptions` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_tags` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_ipam_organization_admin_accounts` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_protection_health_check_associations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_resource_policies` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_event_streams` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_monitor_probes` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_application_assignment_configurations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_gcm_channels` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_load_balancer_policy_types` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_portfolio_shares` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_cluster_policies` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_service_network_resource_associations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_apps` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_proxy_protocol_policies` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_canaries` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_buckets` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_sharing_accounts` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_event_destination` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_email_templates` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_domain_mail_from` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_endpoint_configurations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_ipam_preview_next_cidrs` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_classification_export_configurations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_gateways` - Used by: `aws_finspace_kx_cluster`
- **Method:** `describe_vpc_endpoint_service_allowed_principals` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_clusters` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_resource_configurations` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_target_group_attachments` - Used by: `aws_finspace_kx_cluster`
- **Method:** `get_resource_policy` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_canary_groups` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_attachment_accepters` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_customer_managed_policy_attachments` - Used by: `aws_finspace_kx_cluster`
- **Method:** `list_jobs` - Used by: `aws_finspace_kx_cluster`

### Priority 2: Fix topkey Values (124 resources)

These resources have incorrect topkey values:

- **topkey:** `CostCategories` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `Notifications` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `SnapshotCopyGrants` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `InvitationAccepters` - Used by: `aws_finspace_kx_cluster`, `aws_detective_organization_admin_account`
- **topkey:** `Distributions` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `Connectors` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `tokenVault` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `DelegatedAdminAccounts` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `Channels` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `Rooms` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `AssessmentTemplates` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `StaticIps` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `Clusters` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `RadiusSettings` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `BackendServerDescriptions` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `preferences` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `PlaceIndexes` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `KeyPairs` - Used by: `aws_finspace_kx_cluster`, `aws_lightsail_lb_https_redirection_policy`, `aws_lightsail_lb_stickiness_policy`
- **topkey:** `IndexingConfigurations` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `EntityRecognizers` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `DBInstanceRoleAssociations` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `S3Endpoints` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `ThingGroups` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `RateBasedRules` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `AppMonitors` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `StreamNames` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `clusterPeerings` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `memoryStrategies` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `Rules` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `GrantAccepters` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `RepositoryAssociations` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `Permissions` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `InternetGatewayAttachments` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `GlobalSettings` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `Baseline` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `SnapshotTasks` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `TagOptions` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `Confirmations` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `Maps` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `Hub` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `DomainNames` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `DataQualityJobDefinitions` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `CACertificates` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `Enablers` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `VirtualInterfaces` - Used by: `aws_finspace_kx_cluster`, `aws_dx_hosted_private_virtual_interface_accepter`, `aws_dx_hosted_public_virtual_interface` and 6 more
- **topkey:** `Attachments` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `Domains` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `UserGroupMemberships` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `Applications` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `AccountTokenVersion` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `GraphqlApis` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `Policies` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `ApiKeys` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `FeatureGroups` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `ThingTypes` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `MediaInsightsPipelines` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `Keyspaces` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `destinations` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `MemberAssociations` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `status` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `BlockPublicAccessConfigurations` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `GeofenceCollections` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `ProvisioningTemplates` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `Authorizers` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `LocalGatewayRoutes` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `Environments` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `BillingGroups` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `Profiles` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `CustomPlugins` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `RouteCalculators` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `HttpsRedirectPolicies` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `LoadBalancers` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `StreamProcessors` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `DataRepositoryAssociations` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `DomainEntries` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `DomainConfigurations` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `TrustAnchors` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `BgpPeers` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `OriginRequestPolicyList` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `DocumentClassifiers` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `Pipelines` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `AssessmentTargets` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `Buckets` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `VirtualClusters` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `OrganizationAdminAccounts` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `GatewayAssociationProposals` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `Trackers` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `EventSubscriptions` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `Invitations` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `MacsecKeyAssociations` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `LoggingConfigurations` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `RecordingConfigurations` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `PortInfo` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `QueueUrls` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `DevEndpoints` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `ResourceGroups` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `invoiceUnits` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `Policy` - Used by: `aws_finspace_kx_cluster`, `aws_cloudwatch_event_permission`
- **topkey:** `AccountRegistrations` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `loggingConfig` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `EventConfigurations` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `DiskAttachments` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `FleetStackAssociations` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `ConnectionAssociations` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `VpcDhcpOptions` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `JobTemplates` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `Certificates` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `WorkerConfigurations` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `items` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `Fleets` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `RoleAliases` - Used by: `aws_finspace_kx_cluster`
- **topkey:** `PlaybackKeyPairs` - Used by: `aws_finspace_kx_cluster`

### Priority 3: Fix key Fields (31 resources)

These resources have incorrect key field names:

- **key:** `ARN` - Used by: `aws_finspace_kx_cluster`
- **key:** `LaunchTemplateIds` - Used by: `aws_finspace_kx_cluster`
- **key:** `ServiceIntegration` - Used by: `aws_finspace_kx_cluster`
- **key:** `DataLakeSettings` - Used by: `aws_finspace_kx_cluster`
- **key:** `VdmAttributes` - Used by: `aws_finspace_kx_cluster`
- **key:** `SslPolicyName` - Used by: `aws_finspace_kx_cluster`
- **key:** `CatalogId` - Used by: `aws_finspace_kx_cluster`
- **key:** `AssociationId` - Used by: `aws_finspace_kx_cluster`
- **key:** `SuppressionAttributes` - Used by: `aws_finspace_kx_cluster`
- **key:** `ContinuousDeploymentPolicyId` - Used by: `aws_finspace_kx_cluster`
- **key:** `GlobalSettingsName` - Used by: `aws_finspace_kx_cluster`
- **key:** `DataLakeSettingsId` - Used by: `aws_finspace_kx_cluster`
- **key:** `CachePolicyId` - Used by: `aws_finspace_kx_cluster`
- **key:** `null` - Used by: `aws_finspace_kx_cluster`
- **key:** `UserProfileArn` - Used by: `aws_finspace_kx_cluster`
- **key:** `RuleName` - Used by: `aws_finspace_kx_cluster`
- **key:** `Arn` - Used by: `aws_finspace_kx_cluster`, `aws_sagemaker_user_profile`
- **key:** `Id` - Used by: `aws_finspace_kx_cluster`, `aws_cloudfront_field_level_encryption_profile`, `aws_cloudfront_function` and 7 more
- **key:** `EncryptionConfigId` - Used by: `aws_finspace_kx_cluster`
- **key:** `Name` - Used by: `aws_finspace_kx_cluster`
- **key:** `EventSources` - Used by: `aws_finspace_kx_cluster`

### Priority 4: Update needid_dict.py (478 resources)

These resources require parent IDs and should be documented in needid_dict.py:

**Parameter(s): ``**
- `aws_finspace_kx_cluster`
- `aws_appstream_user_stack_association`
- `aws_chatbot_slack_channel_configuration`
- `aws_cloudfrontkeyvaluestore_key`
- `aws_cloudwatch_log_stream`
- ... and 35 more

**Parameter(s): `AcceleratorArn`**
- `aws_globalaccelerator_custom_routing_listener`
- `aws_globalaccelerator_listener`

**Parameter(s): `AccountId`**
- `aws_account_alternate_contact`
- `aws_account_primary_contact`
- `aws_budgets_budget`

**Parameter(s): `AccountId, BudgetName`**
- `aws_budgets_budget_action`

**Parameter(s): `AccountId, ClusterIdentifier`**
- `aws_redshift_partner`

**Parameter(s): `ApiId`**
- `aws_apigatewayv2_authorizer`
- `aws_apigatewayv2_deployment`
- `aws_apigatewayv2_integration`
- `aws_apigatewayv2_model`
- `aws_apigatewayv2_route`
- ... and 1 more

**Parameter(s): `ApplicationArn`**
- `aws_ssoadmin_application_access_scope`
- `aws_ssoadmin_application_assignment`

**Parameter(s): `ApplicationId`**
- `aws_appconfig_configuration_profile`
- `aws_appconfig_environment`
- `aws_serverlessapplicationrepository_cloudformation_stack`

**Parameter(s): `ApplicationId, ConfigurationProfileId`**
- `aws_appconfig_hosted_configuration_version`

**Parameter(s): `ApplicationId, EnvironmentId`**
- `aws_appconfig_deployment`

**Parameter(s): `ApplicationName`**
- `aws_elastic_beanstalk_configuration_template`
- `aws_kinesisanalyticsv2_application_snapshot`

**Parameter(s): `Attribute, ImageId`**
- `aws_ami_launch_permission`
- `aws_ec2_image_block_public_access`

**Parameter(s): `AuthenticationType`**
- `aws_appstream_user`

**Parameter(s): `AutoScalingConfigurationArn`**
- `aws_apprunner_auto_scaling_configuration_version`
- `aws_apprunner_default_auto_scaling_configuration_version`

**Parameter(s): `AutoScalingGroupName`**
- `aws_autoscaling_lifecycle_hook`
- `aws_autoscaling_traffic_source_attachment`

**Parameter(s): `AwsAccountId`**
- `aws_quicksight_analysis`
- `aws_quicksight_dashboard`
- `aws_quicksight_data_set`
- `aws_quicksight_data_source`
- `aws_quicksight_folder`
- ... and 5 more

**Parameter(s): `AwsAccountId, CustomPermissionsName`**
- `aws_quicksight_custom_permissions`

**Parameter(s): `AwsAccountId, DataSetId`**
- `aws_quicksight_refresh_schedule`

**Parameter(s): `AwsAccountId, Namespace`**
- `aws_quicksight_group`
- `aws_quicksight_iam_policy_assignment`
- `aws_quicksight_user`

**Parameter(s): `AwsAccountId, TemplateId`**
- `aws_quicksight_template_alias`

**Parameter(s): `BackupPlanId`**
- `aws_backup_selection`

**Parameter(s): `BackupVaultName`**
- `aws_backup_vault_lock_configuration`
- `aws_backup_vault_notifications`
- `aws_backup_vault_policy`

**Parameter(s): `Bucket`**
- `aws_s3_bucket_abac`
- `aws_s3_bucket_accelerate_configuration`
- `aws_s3_bucket_acl`
- `aws_s3_bucket_cors_configuration`
- `aws_s3_bucket_inventory_configuration`
- ... and 14 more

**Parameter(s): `Bucket, Id`**
- `aws_s3_bucket_analytics_configuration`
- `aws_s3_bucket_intelligent_tiering_configuration`
- `aws_s3_bucket_inventory`
- `aws_s3_bucket_metric`

**Parameter(s): `Bucket, Key`**
- `aws_s3_bucket_object`
- `aws_s3_object`
- `aws_s3_object_copy`

**Parameter(s): `CatalogId, DatabaseName, TableName, Type`**
- `aws_glue_catalog_table_optimizer`

**Parameter(s): `CatalogName`**
- `aws_athena_database`

**Parameter(s): `CertificateAuthorityArn`**
- `aws_acmpca_permission`

**Parameter(s): `CertificateAuthorityArn, CertificateArn`**
- `aws_acmpca_certificate`

**Parameter(s): `ClientVpnEndpointId`**
- `aws_ec2_client_vpn_route`

**Parameter(s): `ClusterArn`**
- `aws_msk_scram_secret_association`
- `aws_msk_single_scram_secret_association`

**Parameter(s): `ClusterId`**
- `aws_emr_instance_fleet`
- `aws_emr_instance_group`
- `aws_emr_managed_scaling_policy`

**Parameter(s): `ClusterIdentifier`**
- `aws_redshift_logging`

**Parameter(s): `CollectionId`**
- `aws_route53_cidr_location`

**Parameter(s): `ConfigRuleNames`**
- `aws_config_remediation_configuration`

**Parameter(s): `ConfigurationSetName`**
- `aws_sesv2_configuration_set_event_destination`

**Parameter(s): `ContactId`**
- `aws_ssmcontacts_contact_channel`
- `aws_ssmcontacts_plan`

**Parameter(s): `ContainerName`**
- `aws_media_store_container_policy`

**Parameter(s): `ControlPanelArn`**
- `aws_route53recoverycontrolconfig_routing_control`
- `aws_route53recoverycontrolconfig_safety_rule`

**Parameter(s): `DBProxyName`**
- `aws_db_proxy_default_target_group`
- `aws_db_proxy_target`

**Parameter(s): `DBSnapshotIdentifier`**
- `aws_db_snapshot_copy`

**Parameter(s): `DataSetId`**
- `aws_dataexchange_revision`

**Parameter(s): `DataSetId, AwsAccountId`**
- `aws_quicksight_ingestion`

**Parameter(s): `DataSetId, RevisionId`**
- `aws_dataexchange_revision_assets`

**Parameter(s): `DatabaseName`**
- `aws_glue_catalog_table`

**Parameter(s): `DatabaseName, TableName`**
- `aws_glue_partition`
- `aws_glue_partition_index`

**Parameter(s): `DetectorId`**
- `aws_guardduty_detector_feature`
- `aws_guardduty_filter`
- `aws_guardduty_ipset`
- `aws_guardduty_member`
- `aws_guardduty_organization_configuration`
- ... and 3 more

**Parameter(s): `DetectorId, AccountIds`**
- `aws_guardduty_member_detector_feature`

**Parameter(s): `DirectoryId`**
- `aws_directory_service_conditional_forwarder`
- `aws_directory_service_region`

**Parameter(s): `DistributionId`**
- `aws_cloudfront_monitoring_subscription`

**Parameter(s): `Domain`**
- `aws_cognito_user_pool_domain`

**Parameter(s): `DomainName`**
- `aws_apigatewayv2_api_mapping`
- `aws_elasticsearch_domain_policy`
- `aws_elasticsearch_domain_saml_options`
- `aws_route53domains_delegation_signer_record`

**Parameter(s): `DomainNames`**
- `aws_elasticsearch_domain`

**Parameter(s): `EmailIdentity`**
- `aws_sesv2_email_identity_feedback_attributes`
- `aws_sesv2_email_identity_mail_from_attributes`
- `aws_sesv2_email_identity_policy`

**Parameter(s): `FileShareARNList`**
- `aws_storagegateway_nfs_file_share`
- `aws_storagegateway_smb_file_share`

**Parameter(s): `FileSystemAssociationARNList`**
- `aws_storagegateway_file_system_association`

**Parameter(s): `FileSystemId`**
- `aws_efs_backup_policy`
- `aws_efs_file_system_policy`

**Parameter(s): `Filter`**
- `aws_organizations_policy`

**Parameter(s): `FunctionName`**
- `aws_lambda_alias`
- `aws_lambda_function_event_invoke_config`
- `aws_lambda_function_recursion_config`
- `aws_lambda_function_url`
- `aws_lambda_permission`
- ... and 2 more

**Parameter(s): `GatewayARN`**
- `aws_storagegateway_cache`
- `aws_storagegateway_upload_buffer`
- `aws_storagegateway_working_storage`

**Parameter(s): `GlobalNetworkId`**
- `aws_networkmanager_site`
- `aws_networkmanager_transit_gateway_registration`

**Parameter(s): `GraphArn`**
- `aws_detective_member`
- `aws_detective_organization_configuration`

**Parameter(s): `GroupName`**
- `aws_iam_group_policies_exclusive`
- `aws_iam_group_policy`
- `aws_iam_group_policy_attachment`
- `aws_iam_group_policy_attachments_exclusive`
- `aws_iam_user_group_membership`

**Parameter(s): `GroupName, AwsAccountId, Namespace`**
- `aws_quicksight_group_membership`

**Parameter(s): `HostedZoneId`**
- `aws_route53_hosted_zone_dnssec`
- `aws_route53_key_signing_key`
- `aws_route53_record`
- `aws_route53_records_exclusive`

**Parameter(s): `Id`**
- `aws_redshiftdata_statement`
- `aws_route53_vpc_association_authorization`

**Parameter(s): `IdentityPoolId`**
- `aws_cognito_identity_pool_roles_attachment`

**Parameter(s): `IdentityPoolId, IdentityProviderName`**
- `aws_cognito_identity_pool_provider_principal_tag`

**Parameter(s): `IdentityStoreId`**
- `aws_identitystore_group`
- `aws_identitystore_user`

**Parameter(s): `IdentityStoreId, GroupId`**
- `aws_identitystore_group_membership`

**Parameter(s): `IndexId`**
- `aws_kendra_data_source`
- `aws_kendra_experience`
- `aws_kendra_faq`
- `aws_kendra_query_suggestions_block_list`
- `aws_kendra_thesaurus`

**Parameter(s): `InstanceArn`**
- `aws_ssoadmin_application`
- `aws_ssoadmin_permission_set`
- `aws_ssoadmin_trusted_token_issuer`

**Parameter(s): `InstanceId`**
- `aws_connect_contact_flow`
- `aws_connect_contact_flow_module`
- `aws_connect_hours_of_operation`
- `aws_connect_lambda_function_association`
- `aws_connect_phone_number`
- ... and 8 more

**Parameter(s): `InstanceId, LexVersion`**
- `aws_connect_bot_association`

**Parameter(s): `InstanceId, ResourceType`**
- `aws_connect_instance_storage_config`

**Parameter(s): `InstanceProfileName`**
- `aws_iam_instance_profile`

**Parameter(s): `IntegrationId, ApiId`**
- `aws_apigatewayv2_integration_response`

**Parameter(s): `IpamPoolId`**
- `aws_vpc_ipam_pool_cidr_allocation`

**Parameter(s): `JobId`**
- `aws_iam_organizations_features`

**Parameter(s): `KeyId`**
- `aws_kms_ciphertext`
- `aws_kms_grant`
- `aws_kms_key_policy`

**Parameter(s): `LayerName`**
- `aws_lambda_layer_version`
- `aws_lambda_layer_version_permission`

**Parameter(s): `LicenseConfigurationArn`**
- `aws_licensemanager_association`

**Parameter(s): `ListenerArn`**
- `aws_globalaccelerator_endpoint_group`

**Parameter(s): `LoadBalancerArn`**
- `aws_lb_trust_store`
- `aws_lb_trust_store_revocation`

**Parameter(s): `MaxResults`**
- `aws_cognito_identity_pool`
- `aws_cognito_user_pool`

**Parameter(s): `ModelPackageGroupName`**
- `aws_sagemaker_model_package_group_policy`

**Parameter(s): `MultiplexId`**
- `aws_medialive_multiplex_program`

**Parameter(s): `OwnerDirectoryId`**
- `aws_directory_service_shared_directory`
- `aws_directory_service_shared_directory_accepter`

**Parameter(s): `Pattern`**
- `aws_glue_user_defined_function`

**Parameter(s): `PolicyArn`**
- `aws_iam_policy_attachment`

**Parameter(s): `PolicyId`**
- `aws_organizations_policy_attachment`

**Parameter(s): `PoolId`**
- `aws_vpc_ipv6_cidr_block_association`

**Parameter(s): `PortfolioId`**
- `aws_servicecatalog_constraint`

**Parameter(s): `ProductId`**
- `aws_servicecatalog_provisioning_artifact`

**Parameter(s): `ProfileId`**
- `aws_route53profiles_resource_association`

**Parameter(s): `QueueUrl`**
- `aws_sqs_queue_redrive_allow_policy`
- `aws_sqs_queue_redrive_policy`

**Parameter(s): `RegistryName`**
- `aws_schemas_schema`

**Parameter(s): `ResourceARN`**
- `aws_kinesis_resource_policy`

**Parameter(s): `ResourceArn`**
- `aws_acmpca_policy`
- `aws_dynamodb_resource_policy`
- `aws_dynamodb_tag`
- `aws_redshift_resource_policy`
- `aws_sns_topic_data_protection_policy`
- ... and 1 more

**Parameter(s): `ResourceCollectionType`**
- `aws_devopsguru_resource_collection`

**Parameter(s): `RestoreTestingPlanName`**
- `aws_backup_restore_testing_selection`

**Parameter(s): `Role, AwsAccountId, Namespace`**
- `aws_quicksight_role_custom_permission`
- `aws_quicksight_role_membership`

**Parameter(s): `RoleName`**
- `aws_iam_role_policies_exclusive`
- `aws_iam_role_policy`
- `aws_iam_role_policy_attachment`
- `aws_iam_role_policy_attachments_exclusive`

**Parameter(s): `RouteId, ApiId`**
- `aws_apigatewayv2_route_response`

**Parameter(s): `Rule`**
- `aws_cloudwatch_event_target`

**Parameter(s): `RuleSetName`**
- `aws_ses_receipt_rule_set`

**Parameter(s): `RuleSetName, RuleName`**
- `aws_ses_receipt_rule`

**Parameter(s): `Scope`**
- `aws_wafv2_ip_set`
- `aws_wafv2_regex_pattern_set`
- `aws_wafv2_rule_group`
- `aws_wafv2_web_acl`

**Parameter(s): `SecretId`**
- `aws_secretsmanager_secret_policy`
- `aws_secretsmanager_secret_rotation`
- `aws_secretsmanager_secret_version`

**Parameter(s): `SecurityControlId`**
- `aws_securityhub_standards_control_association`

**Parameter(s): `ServerId`**
- `aws_transfer_access`
- `aws_transfer_agreement`
- `aws_transfer_host_key`
- `aws_transfer_user`

**Parameter(s): `ServiceArn`**
- `aws_apprunner_custom_domain_association`
- `aws_apprunner_deployment`

**Parameter(s): `ServiceCode`**
- `aws_servicequotas_service_quota`

**Parameter(s): `ServiceId`**
- `aws_service_discovery_instance`

**Parameter(s): `ServiceNamespace`**
- `aws_appautoscaling_policy`
- `aws_appautoscaling_scheduled_action`
- `aws_appautoscaling_target`

**Parameter(s): `SettingId`**
- `aws_ssm_service_setting`

**Parameter(s): `StackSetName`**
- `aws_cloudformation_stack_instances`
- `aws_cloudformation_stack_set_instance`

**Parameter(s): `StreamARN`**
- `aws_kinesis_stream_consumer`

**Parameter(s): `TableName`**
- `aws_dynamodb_kinesis_streaming_destination`
- `aws_dynamodb_table`
- `aws_dynamodb_table_item`
- `aws_dynamodb_table_replica`

**Parameter(s): `TopicArn`**
- `aws_sns_topic_policy`
- `aws_sns_topic_subscription`

**Parameter(s): `TransitGatewayPolicyTableId`**
- `aws_ec2_transit_gateway_policy_table_association`
- `aws_ec2_transit_gateway_route_table_association`

**Parameter(s): `TransitGatewayRouteTableId`**
- `aws_ec2_transit_gateway_prefix_list_reference`
- `aws_ec2_transit_gateway_route_table_propagation`

**Parameter(s): `TransitGatewayRouteTableId, Filters`**
- `aws_ec2_transit_gateway_route`

**Parameter(s): `TypeName`**
- `aws_cloudcontrolapi_resource`

**Parameter(s): `UserName`**
- `aws_iam_user_policy`
- `aws_iam_user_policy_attachment`
- `aws_iam_user_policy_attachments_exclusive`

**Parameter(s): `UserName, AwsAccountId, Namespace`**
- `aws_quicksight_user_custom_permission`

**Parameter(s): `UserPoolId`**
- `aws_cognito_identity_provider`
- `aws_cognito_log_delivery_configuration`
- `aws_cognito_managed_user_pool_client`
- `aws_cognito_resource_server`
- `aws_cognito_risk_configuration`
- ... and 4 more

**Parameter(s): `UserPoolId, GroupName`**
- `aws_cognito_user_in_group`

**Parameter(s): `UserPoolId, ManagedLoginBrandingId`**
- `aws_cognito_managed_login_branding`

**Parameter(s): `VPCId, VPCRegion`**
- `aws_route53_zone_association`

**Parameter(s): `VoiceConnectorId`**
- `aws_chime_voice_connector_origination`
- `aws_chime_voice_connector_streaming`
- `aws_chime_voice_connector_termination`
- `aws_chime_voice_connector_termination_credentials`

**Parameter(s): `VolumeARNs`**
- `aws_storagegateway_cached_iscsi_volume`
- `aws_storagegateway_stored_iscsi_volume`

**Parameter(s): `VpcEndpointIds`**
- `aws_elasticsearch_vpc_endpoint`

**Parameter(s): `WebACLArn`**
- `aws_wafv2_web_acl_association`
- `aws_wafv2_web_acl_rule_group_association`

**Parameter(s): `WebAppId`**
- `aws_transfer_web_app_customization`

**Parameter(s): `WindowId`**
- `aws_ssm_maintenance_window_target`
- `aws_ssm_maintenance_window_task`

**Parameter(s): `WorkGroup`**
- `aws_athena_prepared_statement`
- `aws_athena_workgroup`

**Parameter(s): `agentId`**
- `aws_bedrockagent_agent_alias`

**Parameter(s): `agentId, agentVersion`**
- `aws_bedrockagent_agent_action_group`
- `aws_bedrockagent_agent_collaborator`
- `aws_bedrockagent_agent_knowledge_base_association`

**Parameter(s): `agentRuntimeId`**
- `aws_bedrockagentcore_agent_runtime_endpoint`

**Parameter(s): `apiId`**
- `aws_appsync_api_key`
- `aws_appsync_channel_namespace`
- `aws_appsync_datasource`
- `aws_appsync_function`
- `aws_appsync_source_api_association`

**Parameter(s): `apiId, format`**
- `aws_appsync_type`

**Parameter(s): `apiId, typeName`**
- `aws_appsync_resolver`

**Parameter(s): `appBundleIdentifier`**
- `aws_appfabric_app_authorization`
- `aws_appfabric_app_authorization_connection`
- `aws_appfabric_ingestion`

**Parameter(s): `appBundleIdentifier, ingestionIdentifier`**
- `aws_appfabric_ingestion_destination`

**Parameter(s): `appId`**
- `aws_amplify_backend_environment`
- `aws_amplify_branch`
- `aws_amplify_domain_association`
- `aws_amplify_webhook`

**Parameter(s): `applicationId`**
- `aws_m2_deployment`

**Parameter(s): `applicationName`**
- `aws_codedeploy_deployment_group`

**Parameter(s): `arn`**
- `aws_devicefarm_device_pool`

**Parameter(s): `botId`**
- `aws_lexv2models_bot_version`

**Parameter(s): `botId, botVersion`**
- `aws_lexv2models_bot_locale`

**Parameter(s): `botId, botVersion, localeId`**
- `aws_lexv2models_intent`
- `aws_lexv2models_slot_type`

**Parameter(s): `botId, botVersion, localeId, intentId`**
- `aws_lexv2models_slot`

**Parameter(s): `botName`**
- `aws_lex_bot_alias`

**Parameter(s): `bucketName`**
- `aws_lightsail_bucket_access_key`

**Parameter(s): `cluster, service`**
- `aws_ecs_task_set`

**Parameter(s): `clusterName`**
- `aws_eks_addon`
- `aws_eks_fargate_profile`
- `aws_eks_identity_provider_config`
- `aws_eks_node_group`
- `aws_eks_pod_identity_association`

**Parameter(s): `clusterName, principalArn`**
- `aws_eks_access_policy_association`

**Parameter(s): `controlType`**
- `aws_auditmanager_control`

**Parameter(s): `deliveryDestinationName`**
- `aws_cloudwatch_log_delivery_destination_policy`

**Parameter(s): `domain`**
- `aws_codeartifact_domain_permissions_policy`

**Parameter(s): `domain, repository`**
- `aws_codeartifact_repository_permissions_policy`

**Parameter(s): `domainIdentifier`**
- `aws_datazone_environment_blueprint_configuration`
- `aws_datazone_environment_profile`
- `aws_datazone_project`

**Parameter(s): `domainIdentifier, managed, searchScope`**
- `aws_datazone_asset_type`
- `aws_datazone_form_type`

**Parameter(s): `domainIdentifier, projectIdentifier`**
- `aws_datazone_environment`

**Parameter(s): `domainIdentifier, searchScope`**
- `aws_datazone_glossary`
- `aws_datazone_glossary_term`

**Parameter(s): `domainIdentifier, userType`**
- `aws_datazone_user_profile`

**Parameter(s): `domainName`**
- `aws_api_gateway_base_path_mapping`
- `aws_appsync_domain_name_api_association`

**Parameter(s): `experimentTemplateId`**
- `aws_fis_target_account_configuration`

**Parameter(s): `frameworkType`**
- `aws_auditmanager_framework`

**Parameter(s): `gatewayIdentifier`**
- `aws_bedrockagentcore_gateway_target`

**Parameter(s): `instanceName`**
- `aws_lightsail_instance_public_ports`

**Parameter(s): `keyspaceName`**
- `aws_keyspaces_table`

**Parameter(s): `knowledgeBaseId`**
- `aws_bedrockagent_data_source`

**Parameter(s): `listenerIdentifier, serviceIdentifier`**
- `aws_vpclattice_listener_rule`

**Parameter(s): `loadBalancerName`**
- `aws_lightsail_lb_certificate_attachment`

**Parameter(s): `logGroupIdentifier`**
- `aws_cloudwatch_log_data_protection_policy`
- `aws_cloudwatch_log_transformer`

**Parameter(s): `logGroupIdentifiers`**
- `aws_cloudwatch_log_index_policy`

**Parameter(s): `maxResults`**
- `aws_finspace_kx_user`

**Parameter(s): `meshName`**
- `aws_appmesh_virtual_gateway`
- `aws_appmesh_virtual_node`
- `aws_appmesh_virtual_router`
- `aws_appmesh_virtual_service`

**Parameter(s): `meshName, virtualGatewayName`**
- `aws_appmesh_gateway_route`

**Parameter(s): `meshName, virtualRouterName`**
- `aws_appmesh_route`

**Parameter(s): `name`**
- `aws_ecr_account_setting`
- `aws_eks_capability`

**Parameter(s): `names`**
- `aws_codebuild_webhook`

**Parameter(s): `notificationConfigurationArn`**
- `aws_notifications_event_rule`

**Parameter(s): `pipelineId`**
- `aws_datapipeline_pipeline_definition`

**Parameter(s): `policyStoreId`**
- `aws_verifiedpermissions_identity_source`
- `aws_verifiedpermissions_policy`
- `aws_verifiedpermissions_policy_template`
- `aws_verifiedpermissions_schema`

**Parameter(s): `policyType`**
- `aws_cloudwatch_log_account_policy`

**Parameter(s): `project`**
- `aws_evidently_feature`
- `aws_evidently_launch`

**Parameter(s): `registrationStatus`**
- `aws_swf_domain`

**Parameter(s): `repositoryName`**
- `aws_codecommit_approval_rule_template_association`
- `aws_codecommit_trigger`
- `aws_ecr_lifecycle_policy`
- `aws_ecrpublic_repository_policy`

**Parameter(s): `requestType`**
- `aws_auditmanager_framework_share`

**Parameter(s): `resourceArn`**
- `aws_codebuild_resource_policy`
- `aws_ecs_tag`
- `aws_vpclattice_resource_policy`

**Parameter(s): `resourceIdentifier`**
- `aws_vpclattice_access_log_subscription`
- `aws_vpclattice_auth_policy`

**Parameter(s): `resourceOwner`**
- `aws_ram_principal_association`
- `aws_ram_resource_association`
- `aws_ram_resource_share`

**Parameter(s): `resourceType`**
- `aws_computeoptimizer_recommendation_preferences`

**Parameter(s): `restApiId`**
- `aws_api_gateway_authorizer`
- `aws_api_gateway_deployment`
- `aws_api_gateway_documentation_part`
- `aws_api_gateway_documentation_version`
- `aws_api_gateway_gateway_response`
- ... and 5 more

**Parameter(s): `restApiId, resourceId, httpMethod`**
- `aws_api_gateway_integration`
- `aws_api_gateway_method`

**Parameter(s): `restApiId, resourceId, httpMethod, statusCode`**
- `aws_api_gateway_integration_response`
- `aws_api_gateway_method_response`

**Parameter(s): `restApiId, stageName`**
- `aws_api_gateway_method_settings`

**Parameter(s): `serviceAccountId, workspaceId`**
- `aws_grafana_workspace_service_account_token`

**Parameter(s): `serviceIdentifier`**
- `aws_vpclattice_listener`

**Parameter(s): `serviceName`**
- `aws_lightsail_container_service_deployment_version`

**Parameter(s): `serviceNetworkServiceAssociationIdentifier`**
- `aws_vpclattice_domain_verification`

**Parameter(s): `spaceName`**
- `aws_codecatalyst_dev_environment`
- `aws_codecatalyst_project`

**Parameter(s): `spaceName, projectName`**
- `aws_codecatalyst_source_repository`

**Parameter(s): `stateMachineArn`**
- `aws_sfn_alias`

**Parameter(s): `subscriberId`**
- `aws_securitylake_subscriber_notification`

**Parameter(s): `tableBucketARN`**
- `aws_s3tables_table`
- `aws_s3tables_table_bucket_policy`
- `aws_s3tables_table_bucket_replication`

**Parameter(s): `tableBucketARN, namespace, name`**
- `aws_s3tables_table_policy`

**Parameter(s): `taskDefinition`**
- `aws_ecs_task_definition`

**Parameter(s): `thingName`**
- `aws_iot_thing_principal_attachment`

**Parameter(s): `type`**
- `aws_opensearchserverless_access_policy`
- `aws_opensearchserverless_lifecycle_policy`
- `aws_opensearchserverless_security_config`
- `aws_opensearchserverless_security_policy`

**Parameter(s): `usagePlanId`**
- `aws_api_gateway_usage_plan_key`

**Parameter(s): `workspaceId`**
- `aws_grafana_license_association`
- `aws_grafana_role_association`
- `aws_grafana_workspace_saml_configuration`
- `aws_grafana_workspace_service_account`
- `aws_prometheus_alert_manager_definition`
- ... and 4 more

### Priority 5: Grant IAM Permissions (20 resources)

These resources need IAM permissions. This is NOT an aws_dict.py issue.

### Priority 6: Investigate API Errors (572 resources)

These resources have various API errors that need investigation.

## Quick Stats

- **Success Rate:** 45.5% of tested resources are fully valid
- **Issues Requiring aws_dict.py Changes:** 282
- **Issues Requiring needid_dict.py Updates:** 478
- **Issues Requiring IAM Permissions:** 20
- **Issues Requiring Investigation:** 572

## Next Steps

1. **Fix method names** - Update descfn fields for resources with method_not_found errors
2. **Fix topkey values** - Update topkey fields based on actual API responses
3. **Fix key fields** - Update key fields based on actual API response structure
4. **Update needid_dict.py** - Add entries for resources requiring parent IDs
5. **Grant permissions** - Add IAM permissions for permission_denied errors
6. **Re-run verification** - Confirm all fixes work correctly

## Detailed Breakdown by Error Type

### Resources Requiring Parent IDs

These resources need to be added to needid_dict.py:

- `aws_account_alternate_contact` - Requires: `AccountId`
- `aws_account_primary_contact` - Requires: `AccountId`
- `aws_acmpca_certificate` - Requires: `CertificateAuthorityArn`, `CertificateArn`
- `aws_acmpca_permission` - Requires: `CertificateAuthorityArn`
- `aws_acmpca_policy` - Requires: `ResourceArn`
- `aws_ami_launch_permission` - Requires: `Attribute`, `ImageId`
- `aws_amplify_backend_environment` - Requires: `appId`
- `aws_amplify_branch` - Requires: `appId`
- `aws_amplify_domain_association` - Requires: `appId`
- `aws_amplify_webhook` - Requires: `appId`
- `aws_api_gateway_authorizer` - Requires: `restApiId`
- `aws_api_gateway_base_path_mapping` - Requires: `domainName`
- `aws_api_gateway_deployment` - Requires: `restApiId`
- `aws_api_gateway_documentation_part` - Requires: `restApiId`
- `aws_api_gateway_documentation_version` - Requires: `restApiId`
- `aws_api_gateway_gateway_response` - Requires: `restApiId`
- `aws_api_gateway_integration` - Requires: `restApiId`, `resourceId`, `httpMethod`
- `aws_api_gateway_integration_response` - Requires: `restApiId`, `resourceId`, `httpMethod`, `statusCode`
- `aws_api_gateway_method` - Requires: `restApiId`, `resourceId`, `httpMethod`
- `aws_api_gateway_method_response` - Requires: `restApiId`, `resourceId`, `httpMethod`, `statusCode`
- `aws_api_gateway_method_settings` - Requires: `restApiId`, `stageName`
- `aws_api_gateway_model` - Requires: `restApiId`
- `aws_api_gateway_request_validator` - Requires: `restApiId`
- `aws_api_gateway_resource` - Requires: `restApiId`
- `aws_api_gateway_rest_api_policy` - Requires: `restApiId`
- `aws_api_gateway_stage` - Requires: `restApiId`
- `aws_api_gateway_usage_plan_key` - Requires: `usagePlanId`
- `aws_apigatewayv2_api_mapping` - Requires: `DomainName`
- `aws_apigatewayv2_authorizer` - Requires: `ApiId`
- `aws_apigatewayv2_deployment` - Requires: `ApiId`
- `aws_apigatewayv2_integration` - Requires: `ApiId`
- `aws_apigatewayv2_integration_response` - Requires: `IntegrationId`, `ApiId`
- `aws_apigatewayv2_model` - Requires: `ApiId`
- `aws_apigatewayv2_route` - Requires: `ApiId`
- `aws_apigatewayv2_route_response` - Requires: `RouteId`, `ApiId`
- `aws_apigatewayv2_stage` - Requires: `ApiId`
- `aws_appautoscaling_policy` - Requires: `ServiceNamespace`
- `aws_appautoscaling_scheduled_action` - Requires: `ServiceNamespace`
- `aws_appautoscaling_target` - Requires: `ServiceNamespace`
- `aws_appconfig_configuration_profile` - Requires: `ApplicationId`
- `aws_appconfig_deployment` - Requires: `ApplicationId`, `EnvironmentId`
- `aws_appconfig_environment` - Requires: `ApplicationId`
- `aws_appconfig_hosted_configuration_version` - Requires: `ApplicationId`, `ConfigurationProfileId`
- `aws_appfabric_app_authorization` - Requires: `appBundleIdentifier`
- `aws_appfabric_app_authorization_connection` - Requires: `appBundleIdentifier`
- `aws_appfabric_ingestion` - Requires: `appBundleIdentifier`
- `aws_appfabric_ingestion_destination` - Requires: `appBundleIdentifier`, `ingestionIdentifier`
- `aws_appmesh_gateway_route` - Requires: `meshName`, `virtualGatewayName`
- `aws_appmesh_route` - Requires: `meshName`, `virtualRouterName`
- `aws_appmesh_virtual_gateway` - Requires: `meshName`
- `aws_appmesh_virtual_node` - Requires: `meshName`
- `aws_appmesh_virtual_router` - Requires: `meshName`
- `aws_appmesh_virtual_service` - Requires: `meshName`
- `aws_apprunner_auto_scaling_configuration_version` - Requires: `AutoScalingConfigurationArn`
- `aws_apprunner_custom_domain_association` - Requires: `ServiceArn`
- `aws_apprunner_default_auto_scaling_configuration_version` - Requires: `AutoScalingConfigurationArn`
- `aws_apprunner_deployment` - Requires: `ServiceArn`
- `aws_appstream_user` - Requires: `AuthenticationType`
- `aws_appstream_user_stack_association` - Requires: 
- `aws_appsync_api_key` - Requires: `apiId`
- `aws_appsync_channel_namespace` - Requires: `apiId`
- `aws_appsync_datasource` - Requires: `apiId`
- `aws_appsync_domain_name_api_association` - Requires: `domainName`
- `aws_appsync_function` - Requires: `apiId`
- `aws_appsync_resolver` - Requires: `apiId`, `typeName`
- `aws_appsync_source_api_association` - Requires: `apiId`
- `aws_appsync_type` - Requires: `apiId`, `format`
- `aws_athena_database` - Requires: `CatalogName`
- `aws_athena_prepared_statement` - Requires: `WorkGroup`
- `aws_athena_workgroup` - Requires: `WorkGroup`
- `aws_auditmanager_control` - Requires: `controlType`
- `aws_auditmanager_framework` - Requires: `frameworkType`
- `aws_auditmanager_framework_share` - Requires: `requestType`
- `aws_autoscaling_lifecycle_hook` - Requires: `AutoScalingGroupName`
- `aws_autoscaling_traffic_source_attachment` - Requires: `AutoScalingGroupName`
- `aws_backup_restore_testing_selection` - Requires: `RestoreTestingPlanName`
- `aws_backup_selection` - Requires: `BackupPlanId`
- `aws_backup_vault_lock_configuration` - Requires: `BackupVaultName`
- `aws_backup_vault_notifications` - Requires: `BackupVaultName`
- `aws_backup_vault_policy` - Requires: `BackupVaultName`
- `aws_bedrockagent_agent_action_group` - Requires: `agentId`, `agentVersion`
- `aws_bedrockagent_agent_alias` - Requires: `agentId`
- `aws_bedrockagent_agent_collaborator` - Requires: `agentId`, `agentVersion`
- `aws_bedrockagent_agent_knowledge_base_association` - Requires: `agentId`, `agentVersion`
- `aws_bedrockagent_data_source` - Requires: `knowledgeBaseId`
- `aws_bedrockagentcore_agent_runtime_endpoint` - Requires: `agentRuntimeId`
- `aws_bedrockagentcore_gateway_target` - Requires: `gatewayIdentifier`
- `aws_budgets_budget` - Requires: `AccountId`
- `aws_budgets_budget_action` - Requires: `AccountId`, `BudgetName`
- `aws_chatbot_slack_channel_configuration` - Requires: 
- `aws_chime_voice_connector_origination` - Requires: `VoiceConnectorId`
- `aws_chime_voice_connector_streaming` - Requires: `VoiceConnectorId`
- `aws_chime_voice_connector_termination` - Requires: `VoiceConnectorId`
- `aws_chime_voice_connector_termination_credentials` - Requires: `VoiceConnectorId`
- `aws_cloudcontrolapi_resource` - Requires: `TypeName`
- `aws_cloudformation_stack_instances` - Requires: `StackSetName`
- `aws_cloudformation_stack_set_instance` - Requires: `StackSetName`
- `aws_cloudfront_monitoring_subscription` - Requires: `DistributionId`
- `aws_cloudfrontkeyvaluestore_key` - Requires: 
- `aws_cloudwatch_event_target` - Requires: `Rule`
- `aws_cloudwatch_log_account_policy` - Requires: `policyType`
- `aws_cloudwatch_log_data_protection_policy` - Requires: `logGroupIdentifier`
- `aws_cloudwatch_log_delivery_destination_policy` - Requires: `deliveryDestinationName`
- `aws_cloudwatch_log_index_policy` - Requires: `logGroupIdentifiers`
- `aws_cloudwatch_log_stream` - Requires: 
- `aws_cloudwatch_log_transformer` - Requires: `logGroupIdentifier`
- `aws_codeartifact_domain_permissions_policy` - Requires: `domain`
- `aws_codeartifact_repository_permissions_policy` - Requires: `domain`, `repository`
- `aws_codebuild_resource_policy` - Requires: `resourceArn`
- `aws_codebuild_webhook` - Requires: `names`
- `aws_codecatalyst_dev_environment` - Requires: `spaceName`
- `aws_codecatalyst_project` - Requires: `spaceName`
- `aws_codecatalyst_source_repository` - Requires: `spaceName`, `projectName`
- `aws_codecommit_approval_rule_template_association` - Requires: `repositoryName`
- `aws_codecommit_trigger` - Requires: `repositoryName`
- `aws_codedeploy_deployment_group` - Requires: `applicationName`
- `aws_cognito_identity_pool` - Requires: `MaxResults`
- `aws_cognito_identity_pool_provider_principal_tag` - Requires: `IdentityPoolId`, `IdentityProviderName`
- `aws_cognito_identity_pool_roles_attachment` - Requires: `IdentityPoolId`
- `aws_cognito_identity_provider` - Requires: `UserPoolId`
- `aws_cognito_log_delivery_configuration` - Requires: `UserPoolId`
- `aws_cognito_managed_login_branding` - Requires: `UserPoolId`, `ManagedLoginBrandingId`
- `aws_cognito_managed_user_pool_client` - Requires: `UserPoolId`
- `aws_cognito_resource_server` - Requires: `UserPoolId`
- `aws_cognito_risk_configuration` - Requires: `UserPoolId`
- `aws_cognito_user` - Requires: `UserPoolId`
- `aws_cognito_user_group` - Requires: `UserPoolId`
- `aws_cognito_user_in_group` - Requires: `UserPoolId`, `GroupName`
- `aws_cognito_user_pool` - Requires: `MaxResults`
- `aws_cognito_user_pool_client` - Requires: `UserPoolId`
- `aws_cognito_user_pool_domain` - Requires: `Domain`
- `aws_cognito_user_pool_ui_customization` - Requires: `UserPoolId`
- `aws_computeoptimizer_recommendation_preferences` - Requires: `resourceType`
- `aws_config_remediation_configuration` - Requires: `ConfigRuleNames`
- `aws_connect_bot_association` - Requires: `InstanceId`, `LexVersion`
- `aws_connect_contact_flow` - Requires: `InstanceId`
- `aws_connect_contact_flow_module` - Requires: `InstanceId`
- `aws_connect_hours_of_operation` - Requires: `InstanceId`
- `aws_connect_instance_storage_config` - Requires: `InstanceId`, `ResourceType`
- `aws_connect_lambda_function_association` - Requires: `InstanceId`
- `aws_connect_phone_number` - Requires: `InstanceId`
- `aws_connect_queue` - Requires: `InstanceId`
- `aws_connect_quick_connect` - Requires: `InstanceId`
- `aws_connect_routing_profile` - Requires: `InstanceId`
- `aws_connect_security_profile` - Requires: `InstanceId`
- `aws_connect_user` - Requires: `InstanceId`
- `aws_connect_user_hierarchy_group` - Requires: `InstanceId`
- `aws_connect_user_hierarchy_structure` - Requires: `InstanceId`
- `aws_connect_vocabulary` - Requires: `InstanceId`
- `aws_controltower_baseline` - Requires: 
- `aws_dataexchange_revision` - Requires: `DataSetId`
- `aws_dataexchange_revision_assets` - Requires: `DataSetId`, `RevisionId`
- `aws_datapipeline_pipeline_definition` - Requires: `pipelineId`
- `aws_datazone_asset_type` - Requires: `domainIdentifier`, `managed`, `searchScope`
- `aws_datazone_environment` - Requires: `domainIdentifier`, `projectIdentifier`
- `aws_datazone_environment_blueprint_configuration` - Requires: `domainIdentifier`
- `aws_datazone_environment_profile` - Requires: `domainIdentifier`
- `aws_datazone_form_type` - Requires: `domainIdentifier`, `managed`, `searchScope`
- `aws_datazone_glossary` - Requires: `domainIdentifier`, `searchScope`
- `aws_datazone_glossary_term` - Requires: `domainIdentifier`, `searchScope`
- `aws_datazone_project` - Requires: `domainIdentifier`
- `aws_datazone_user_profile` - Requires: `domainIdentifier`, `userType`
- `aws_db_proxy_default_target_group` - Requires: `DBProxyName`
- `aws_db_proxy_target` - Requires: `DBProxyName`
- `aws_db_snapshot_copy` - Requires: `DBSnapshotIdentifier`
- `aws_detective_member` - Requires: `GraphArn`
- `aws_detective_organization_configuration` - Requires: `GraphArn`
- `aws_devicefarm_device_pool` - Requires: `arn`
- `aws_devicefarm_instance_profile` - Requires: 
- `aws_devicefarm_project` - Requires: 
- `aws_devopsguru_resource_collection` - Requires: `ResourceCollectionType`
- `aws_directory_service_conditional_forwarder` - Requires: `DirectoryId`
- `aws_directory_service_region` - Requires: `DirectoryId`
- `aws_directory_service_shared_directory` - Requires: `OwnerDirectoryId`
- `aws_directory_service_shared_directory_accepter` - Requires: `OwnerDirectoryId`
- `aws_drs_replication_configuration_template` - Requires: 
- `aws_dynamodb_kinesis_streaming_destination` - Requires: `TableName`
- `aws_dynamodb_resource_policy` - Requires: `ResourceArn`
- `aws_dynamodb_table` - Requires: `TableName`
- `aws_dynamodb_table_item` - Requires: `TableName`
- `aws_dynamodb_table_replica` - Requires: `TableName`
- `aws_dynamodb_tag` - Requires: `ResourceArn`
- `aws_ebs_encryption_by_default` - Requires: 
- `aws_ec2_client_vpn_route` - Requires: `ClientVpnEndpointId`
- `aws_ec2_image_block_public_access` - Requires: `Attribute`, `ImageId`
- `aws_ec2_serial_console_access` - Requires: 
- `aws_ec2_transit_gateway_policy_table_association` - Requires: `TransitGatewayPolicyTableId`
- `aws_ec2_transit_gateway_prefix_list_reference` - Requires: `TransitGatewayRouteTableId`
- `aws_ec2_transit_gateway_route` - Requires: `TransitGatewayRouteTableId`, `Filters`
- `aws_ec2_transit_gateway_route_table_association` - Requires: `TransitGatewayPolicyTableId`
- `aws_ec2_transit_gateway_route_table_propagation` - Requires: `TransitGatewayRouteTableId`
- `aws_ecr_account_setting` - Requires: `name`
- `aws_ecr_lifecycle_policy` - Requires: `repositoryName`
- `aws_ecr_registry_policy` - Requires: 
- `aws_ecrpublic_repository_policy` - Requires: `repositoryName`
- `aws_ecs_tag` - Requires: `resourceArn`
- `aws_ecs_task_definition` - Requires: `taskDefinition`
- `aws_ecs_task_set` - Requires: `cluster`, `service`
- `aws_efs_backup_policy` - Requires: `FileSystemId`
- `aws_efs_file_system_policy` - Requires: `FileSystemId`
- `aws_efs_mount_target` - Requires: 
- `aws_eks_access_policy_association` - Requires: `clusterName`, `principalArn`
- `aws_eks_addon` - Requires: `clusterName`
- `aws_eks_capability` - Requires: `name`
- `aws_eks_fargate_profile` - Requires: `clusterName`
- `aws_eks_identity_provider_config` - Requires: `clusterName`
- `aws_eks_node_group` - Requires: `clusterName`
- `aws_eks_pod_identity_association` - Requires: `clusterName`
- `aws_elastic_beanstalk_configuration_template` - Requires: `ApplicationName`
- `aws_elasticsearch_domain` - Requires: `DomainNames`
- `aws_elasticsearch_domain_policy` - Requires: `DomainName`
- `aws_elasticsearch_domain_saml_options` - Requires: `DomainName`
- `aws_elasticsearch_vpc_endpoint` - Requires: `VpcEndpointIds`
- `aws_elastictranscoder_pipeline` - Requires: 
- `aws_emr_instance_fleet` - Requires: `ClusterId`
- `aws_emr_instance_group` - Requires: `ClusterId`
- `aws_emr_managed_scaling_policy` - Requires: `ClusterId`
- `aws_evidently_feature` - Requires: `project`
- `aws_evidently_launch` - Requires: `project`
- `aws_evidently_project` - Requires: 
- `aws_finspace_kx_cluster` - Requires: 
- `aws_finspace_kx_user` - Requires: `maxResults`
- `aws_fis_target_account_configuration` - Requires: `experimentTemplateId`
- `aws_fms_admin_account` - Requires: 
- `aws_globalaccelerator_accelerator` - Requires: 
- `aws_globalaccelerator_custom_routing_listener` - Requires: `AcceleratorArn`
- `aws_globalaccelerator_endpoint_group` - Requires: `ListenerArn`
- `aws_globalaccelerator_listener` - Requires: `AcceleratorArn`
- `aws_glue_catalog_table` - Requires: `DatabaseName`
- `aws_glue_catalog_table_optimizer` - Requires: `CatalogId`, `DatabaseName`, `TableName`, `Type`
- `aws_glue_partition` - Requires: `DatabaseName`, `TableName`
- `aws_glue_partition_index` - Requires: `DatabaseName`, `TableName`
- `aws_glue_resource_policy` - Requires: 
- `aws_glue_user_defined_function` - Requires: `Pattern`
- `aws_grafana_license_association` - Requires: `workspaceId`
- `aws_grafana_role_association` - Requires: `workspaceId`
- `aws_grafana_workspace_saml_configuration` - Requires: `workspaceId`
- `aws_grafana_workspace_service_account` - Requires: `workspaceId`
- `aws_grafana_workspace_service_account_token` - Requires: `serviceAccountId`, `workspaceId`
- `aws_guardduty_detector_feature` - Requires: `DetectorId`
- `aws_guardduty_filter` - Requires: `DetectorId`
- `aws_guardduty_ipset` - Requires: `DetectorId`
- `aws_guardduty_member` - Requires: `DetectorId`
- `aws_guardduty_member_detector_feature` - Requires: `DetectorId`, `AccountIds`
- `aws_guardduty_organization_configuration` - Requires: `DetectorId`
- `aws_guardduty_organization_configuration_feature` - Requires: `DetectorId`
- `aws_guardduty_publishing_destination` - Requires: `DetectorId`
- `aws_guardduty_threatintelset` - Requires: `DetectorId`
- `aws_iam_account_password_policy` - Requires: 
- `aws_iam_group_policies_exclusive` - Requires: `GroupName`
- `aws_iam_group_policy` - Requires: `GroupName`
- `aws_iam_group_policy_attachment` - Requires: `GroupName`
- `aws_iam_group_policy_attachments_exclusive` - Requires: `GroupName`
- `aws_iam_instance_profile` - Requires: `InstanceProfileName`
- `aws_iam_organizations_features` - Requires: `JobId`
- `aws_iam_policy_attachment` - Requires: `PolicyArn`
- `aws_iam_role_policies_exclusive` - Requires: `RoleName`
- `aws_iam_role_policy` - Requires: `RoleName`
- `aws_iam_role_policy_attachment` - Requires: `RoleName`
- `aws_iam_role_policy_attachments_exclusive` - Requires: `RoleName`
- `aws_iam_user_group_membership` - Requires: `GroupName`
- `aws_iam_user_login_profile` - Requires: 
- `aws_iam_user_policy` - Requires: `UserName`
- `aws_iam_user_policy_attachment` - Requires: `UserName`
- `aws_iam_user_policy_attachments_exclusive` - Requires: `UserName`
- `aws_identitystore_group` - Requires: `IdentityStoreId`
- `aws_identitystore_group_membership` - Requires: `IdentityStoreId`, `GroupId`
- `aws_identitystore_user` - Requires: `IdentityStoreId`
- `aws_iot_logging_options` - Requires: 
- `aws_iot_thing_principal_attachment` - Requires: `thingName`
- `aws_kendra_data_source` - Requires: `IndexId`
- `aws_kendra_experience` - Requires: `IndexId`
- `aws_kendra_faq` - Requires: `IndexId`
- `aws_kendra_query_suggestions_block_list` - Requires: `IndexId`
- `aws_kendra_thesaurus` - Requires: `IndexId`
- `aws_keyspaces_table` - Requires: `keyspaceName`
- `aws_kinesis_resource_policy` - Requires: `ResourceARN`
- `aws_kinesis_stream_consumer` - Requires: `StreamARN`
- `aws_kinesisanalyticsv2_application_snapshot` - Requires: `ApplicationName`
- `aws_kms_ciphertext` - Requires: `KeyId`
- `aws_kms_grant` - Requires: `KeyId`
- `aws_kms_key_policy` - Requires: `KeyId`
- `aws_lakeformation_identity_center_configuration` - Requires: 
- `aws_lambda_alias` - Requires: `FunctionName`
- `aws_lambda_function_event_invoke_config` - Requires: `FunctionName`
- `aws_lambda_function_recursion_config` - Requires: `FunctionName`
- `aws_lambda_function_url` - Requires: `FunctionName`
- `aws_lambda_layer_version` - Requires: `LayerName`
- `aws_lambda_layer_version_permission` - Requires: `LayerName`
- `aws_lambda_permission` - Requires: `FunctionName`
- `aws_lambda_provisioned_concurrency_config` - Requires: `FunctionName`
- `aws_lambda_runtime_management_config` - Requires: `FunctionName`
- `aws_lb_listener` - Requires: 
- `aws_lb_listener_rule` - Requires: 
- `aws_lb_trust_store` - Requires: `LoadBalancerArn`
- `aws_lb_trust_store_revocation` - Requires: `LoadBalancerArn`
- `aws_lex_bot_alias` - Requires: `botName`
- `aws_lexv2models_bot_locale` - Requires: `botId`, `botVersion`
- `aws_lexv2models_bot_version` - Requires: `botId`
- `aws_lexv2models_intent` - Requires: `botId`, `botVersion`, `localeId`
- `aws_lexv2models_slot` - Requires: `botId`, `botVersion`, `localeId`, `intentId`
- `aws_lexv2models_slot_type` - Requires: `botId`, `botVersion`, `localeId`
- `aws_licensemanager_association` - Requires: `LicenseConfigurationArn`
- `aws_lightsail_bucket_access_key` - Requires: `bucketName`
- `aws_lightsail_container_service_deployment_version` - Requires: `serviceName`
- `aws_lightsail_instance_public_ports` - Requires: `instanceName`
- `aws_lightsail_lb_certificate_attachment` - Requires: `loadBalancerName`
- `aws_load_balancer_listener_policy` - Requires: 
- `aws_m2_deployment` - Requires: `applicationId`
- `aws_media_store_container_policy` - Requires: `ContainerName`
- `aws_medialive_multiplex_program` - Requires: `MultiplexId`
- `aws_msk_scram_secret_association` - Requires: `ClusterArn`
- `aws_msk_single_scram_secret_association` - Requires: `ClusterArn`
- `aws_networkfirewall_firewall_transit_gateway_attachment_accepter` - Requires: 
- `aws_networkmanager_site` - Requires: `GlobalNetworkId`
- `aws_networkmanager_transit_gateway_registration` - Requires: `GlobalNetworkId`
- `aws_notifications_event_rule` - Requires: `notificationConfigurationArn`
- `aws_observabilityadmin_centralization_rule_for_organization` - Requires: 
- `aws_opensearchserverless_access_policy` - Requires: `type`
- `aws_opensearchserverless_lifecycle_policy` - Requires: `type`
- `aws_opensearchserverless_security_config` - Requires: `type`
- `aws_opensearchserverless_security_policy` - Requires: `type`
- `aws_opsworks_application` - Requires: 
- `aws_organizations_policy` - Requires: `Filter`
- `aws_organizations_policy_attachment` - Requires: `PolicyId`
- `aws_organizations_resource_policy` - Requires: 
- `aws_prometheus_alert_manager_definition` - Requires: `workspaceId`
- `aws_prometheus_query_logging_configuration` - Requires: `workspaceId`
- `aws_prometheus_resource_policy` - Requires: `workspaceId`
- `aws_prometheus_rule_group_namespace` - Requires: `workspaceId`
- `aws_prometheus_workspace_configuration` - Requires: `workspaceId`
- `aws_qldb_ledger` - Requires: 
- `aws_quicksight_analysis` - Requires: `AwsAccountId`
- `aws_quicksight_custom_permissions` - Requires: `AwsAccountId`, `CustomPermissionsName`
- `aws_quicksight_dashboard` - Requires: `AwsAccountId`
- `aws_quicksight_data_set` - Requires: `AwsAccountId`
- `aws_quicksight_data_source` - Requires: `AwsAccountId`
- `aws_quicksight_folder` - Requires: `AwsAccountId`
- `aws_quicksight_group` - Requires: `AwsAccountId`, `Namespace`
- `aws_quicksight_group_membership` - Requires: `GroupName`, `AwsAccountId`, `Namespace`
- `aws_quicksight_iam_policy_assignment` - Requires: `AwsAccountId`, `Namespace`
- `aws_quicksight_ingestion` - Requires: `DataSetId`, `AwsAccountId`
- `aws_quicksight_ip_restriction` - Requires: `AwsAccountId`
- `aws_quicksight_namespace` - Requires: `AwsAccountId`
- `aws_quicksight_refresh_schedule` - Requires: `AwsAccountId`, `DataSetId`
- `aws_quicksight_role_custom_permission` - Requires: `Role`, `AwsAccountId`, `Namespace`
- `aws_quicksight_role_membership` - Requires: `Role`, `AwsAccountId`, `Namespace`
- `aws_quicksight_template` - Requires: `AwsAccountId`
- `aws_quicksight_template_alias` - Requires: `AwsAccountId`, `TemplateId`
- `aws_quicksight_theme` - Requires: `AwsAccountId`
- `aws_quicksight_user` - Requires: `AwsAccountId`, `Namespace`
- `aws_quicksight_user_custom_permission` - Requires: `UserName`, `AwsAccountId`, `Namespace`
- `aws_quicksight_vpc_connection` - Requires: `AwsAccountId`
- `aws_ram_principal_association` - Requires: `resourceOwner`
- `aws_ram_resource_association` - Requires: `resourceOwner`
- `aws_ram_resource_share` - Requires: `resourceOwner`
- `aws_redshift_logging` - Requires: `ClusterIdentifier`
- `aws_redshift_partner` - Requires: `AccountId`, `ClusterIdentifier`
- `aws_redshift_resource_policy` - Requires: `ResourceArn`
- `aws_redshiftdata_statement` - Requires: `Id`
- `aws_route53_cidr_location` - Requires: `CollectionId`
- `aws_route53_hosted_zone_dnssec` - Requires: `HostedZoneId`
- `aws_route53_key_signing_key` - Requires: `HostedZoneId`
- `aws_route53_record` - Requires: `HostedZoneId`
- `aws_route53_records_exclusive` - Requires: `HostedZoneId`
- `aws_route53_vpc_association_authorization` - Requires: `Id`
- `aws_route53_zone_association` - Requires: `VPCId`, `VPCRegion`
- `aws_route53domains_delegation_signer_record` - Requires: `DomainName`
- `aws_route53profiles_resource_association` - Requires: `ProfileId`
- `aws_route53recoverycontrolconfig_routing_control` - Requires: `ControlPanelArn`
- `aws_route53recoverycontrolconfig_safety_rule` - Requires: `ControlPanelArn`
- `aws_route53recoveryreadiness_cell` - Requires: 
- `aws_s3_bucket_abac` - Requires: `Bucket`
- `aws_s3_bucket_accelerate_configuration` - Requires: `Bucket`
- `aws_s3_bucket_acl` - Requires: `Bucket`
- `aws_s3_bucket_analytics_configuration` - Requires: `Bucket`, `Id`
- `aws_s3_bucket_cors_configuration` - Requires: `Bucket`
- `aws_s3_bucket_intelligent_tiering_configuration` - Requires: `Bucket`, `Id`
- `aws_s3_bucket_inventory` - Requires: `Bucket`, `Id`
- `aws_s3_bucket_inventory_configuration` - Requires: `Bucket`
- `aws_s3_bucket_lifecycle_configuration` - Requires: `Bucket`
- `aws_s3_bucket_logging` - Requires: `Bucket`
- `aws_s3_bucket_metadata_configuration` - Requires: `Bucket`
- `aws_s3_bucket_metric` - Requires: `Bucket`, `Id`
- `aws_s3_bucket_metrics_configuration` - Requires: `Bucket`
- `aws_s3_bucket_notification` - Requires: `Bucket`
- `aws_s3_bucket_object` - Requires: `Bucket`, `Key`
- `aws_s3_bucket_object_lock_configuration` - Requires: `Bucket`
- `aws_s3_bucket_ownership_controls` - Requires: `Bucket`
- `aws_s3_bucket_policy` - Requires: `Bucket`
- `aws_s3_bucket_public_access_block` - Requires: `Bucket`
- `aws_s3_bucket_replication_configuration` - Requires: `Bucket`
- `aws_s3_bucket_request_payment_configuration` - Requires: `Bucket`
- `aws_s3_bucket_server_side_encryption_configuration` - Requires: `Bucket`
- `aws_s3_bucket_versioning` - Requires: `Bucket`
- `aws_s3_bucket_website_configuration` - Requires: `Bucket`
- `aws_s3_object` - Requires: `Bucket`, `Key`
- `aws_s3_object_copy` - Requires: `Bucket`, `Key`
- `aws_s3control_access_grant` - Requires: 
- `aws_s3tables_table` - Requires: `tableBucketARN`
- `aws_s3tables_table_bucket_policy` - Requires: `tableBucketARN`
- `aws_s3tables_table_bucket_replication` - Requires: `tableBucketARN`
- `aws_s3tables_table_policy` - Requires: `tableBucketARN`, `namespace`, `name`
- `aws_s3vectors_index` - Requires: 
- `aws_sagemaker_model_package_group_policy` - Requires: `ModelPackageGroupName`
- `aws_schemas_schema` - Requires: `RegistryName`
- `aws_secretsmanager_secret_policy` - Requires: `SecretId`
- `aws_secretsmanager_secret_rotation` - Requires: `SecretId`
- `aws_secretsmanager_secret_version` - Requires: `SecretId`
- `aws_securityhub_organization_configuration` - Requires: 
- `aws_securityhub_standards_control_association` - Requires: `SecurityControlId`
- `aws_securitylake_subscriber_notification` - Requires: `subscriberId`
- `aws_serverlessapplicationrepository_cloudformation_stack` - Requires: `ApplicationId`
- `aws_service_discovery_instance` - Requires: `ServiceId`
- `aws_servicecatalog_constraint` - Requires: `PortfolioId`
- `aws_servicecatalog_provisioning_artifact` - Requires: `ProductId`
- `aws_servicequotas_service_quota` - Requires: `ServiceCode`
- `aws_ses_receipt_rule` - Requires: `RuleSetName`, `RuleName`
- `aws_ses_receipt_rule_set` - Requires: `RuleSetName`
- `aws_sesv2_configuration_set_event_destination` - Requires: `ConfigurationSetName`
- `aws_sesv2_email_identity_feedback_attributes` - Requires: `EmailIdentity`
- `aws_sesv2_email_identity_mail_from_attributes` - Requires: `EmailIdentity`
- `aws_sesv2_email_identity_policy` - Requires: `EmailIdentity`
- `aws_sfn_alias` - Requires: `stateMachineArn`
- `aws_shield_proactive_engagement` - Requires: 
- `aws_sns_topic_data_protection_policy` - Requires: `ResourceArn`
- `aws_sns_topic_policy` - Requires: `TopicArn`
- `aws_sns_topic_subscription` - Requires: `TopicArn`
- `aws_spot_datafeed_subscription` - Requires: 
- `aws_sqs_queue_redrive_allow_policy` - Requires: `QueueUrl`
- `aws_sqs_queue_redrive_policy` - Requires: `QueueUrl`
- `aws_ssm_maintenance_window_target` - Requires: `WindowId`
- `aws_ssm_maintenance_window_task` - Requires: `WindowId`
- `aws_ssm_service_setting` - Requires: `SettingId`
- `aws_ssmcontacts_contact_channel` - Requires: `ContactId`
- `aws_ssmcontacts_plan` - Requires: `ContactId`
- `aws_ssmcontacts_rotation` - Requires: 
- `aws_ssoadmin_application` - Requires: `InstanceArn`
- `aws_ssoadmin_application_access_scope` - Requires: `ApplicationArn`
- `aws_ssoadmin_application_assignment` - Requires: `ApplicationArn`
- `aws_ssoadmin_permission_set` - Requires: `InstanceArn`
- `aws_ssoadmin_trusted_token_issuer` - Requires: `InstanceArn`
- `aws_storagegateway_cache` - Requires: `GatewayARN`
- `aws_storagegateway_cached_iscsi_volume` - Requires: `VolumeARNs`
- `aws_storagegateway_file_system_association` - Requires: `FileSystemAssociationARNList`
- `aws_storagegateway_nfs_file_share` - Requires: `FileShareARNList`
- `aws_storagegateway_smb_file_share` - Requires: `FileShareARNList`
- `aws_storagegateway_stored_iscsi_volume` - Requires: `VolumeARNs`
- `aws_storagegateway_upload_buffer` - Requires: `GatewayARN`
- `aws_storagegateway_working_storage` - Requires: `GatewayARN`
- `aws_swf_domain` - Requires: `registrationStatus`
- `aws_transfer_access` - Requires: `ServerId`
- `aws_transfer_agreement` - Requires: `ServerId`
- `aws_transfer_host_key` - Requires: `ServerId`
- `aws_transfer_user` - Requires: `ServerId`
- `aws_transfer_web_app_customization` - Requires: `WebAppId`
- `aws_verifiedpermissions_identity_source` - Requires: `policyStoreId`
- `aws_verifiedpermissions_policy` - Requires: `policyStoreId`
- `aws_verifiedpermissions_policy_template` - Requires: `policyStoreId`
- `aws_verifiedpermissions_schema` - Requires: `policyStoreId`
- `aws_vpc_block_public_access_exclusion` - Requires: 
- `aws_vpc_ipam_pool_cidr_allocation` - Requires: `IpamPoolId`
- `aws_vpc_ipv6_cidr_block_association` - Requires: `PoolId`
- `aws_vpclattice_access_log_subscription` - Requires: `resourceIdentifier`
- `aws_vpclattice_auth_policy` - Requires: `resourceIdentifier`
- `aws_vpclattice_domain_verification` - Requires: `serviceNetworkServiceAssociationIdentifier`
- `aws_vpclattice_listener` - Requires: `serviceIdentifier`
- `aws_vpclattice_listener_rule` - Requires: `listenerIdentifier`, `serviceIdentifier`
- `aws_vpclattice_resource_policy` - Requires: `resourceArn`
- `aws_vpclattice_service_network_service_association` - Requires: 
- `aws_wafv2_ip_set` - Requires: `Scope`
- `aws_wafv2_regex_pattern_set` - Requires: `Scope`
- `aws_wafv2_rule_group` - Requires: `Scope`
- `aws_wafv2_web_acl` - Requires: `Scope`
- `aws_wafv2_web_acl_association` - Requires: `WebACLArn`
- `aws_wafv2_web_acl_logging_configuration` - Requires: `ResourceArn`
- `aws_wafv2_web_acl_rule_group_association` - Requires: `WebACLArn`
- `aws_worklink_fleet` - Requires: 

