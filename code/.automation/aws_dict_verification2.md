# AWS Dictionary Deep Verification Report

**Generated:** Sat 17 Jan 2026 14:32:17 GMT
**Region:** us-east-1

## Summary

- **Total Resources:** 1611
- **Tested:** 1608
- **Skipped:** 3

### Results

- ✅ **Valid:** 731 (API call successful, structure correct)
- ⚠️  **Warnings:** 158 (API call successful, but structure issues)
- ❌ **Errors:** 127 (Method not found or requires parameters)
- 🔒 **Permission Errors:** 20 (Access denied)
- 🔴 **API Errors:** 572 (Other API failures)

### API Call Statistics

- **API Calls Made:** 891
- **API Calls Failed:** 562
- **Success Rate:** 61.3%

### Structure Validation

- **topkey Correct:** 763
- **topkey Incorrect:** 125
- **key Field Found:** 722
- **key Field Missing:** 32

## ❌ Errors (Method Issues)

These resources have method-related issues:

### `aws_finspace_kx_cluster`

- **Client:** `finspace-data`
- **Method:** `list_clusters`
- **Current topkey:** `Clusters`
- **Current key:** `ClusterId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_clusters' not found on client 'finspace-data'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_finspace_kx_database`

- **Client:** `finspace-data`
- **Method:** `list_databases`
- **Current topkey:** `Databases`
- **Current key:** `DatabaseId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_databases' not found on client 'finspace-data'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_finspace_kx_scaling_group`

- **Client:** `finspace-data`
- **Method:** `list_scaling_groups`
- **Current topkey:** `ScalingGroups`
- **Current key:** `ScalingGroupId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_scaling_groups' not found on client 'finspace-data'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_finspace_kx_volume`

- **Client:** `finspace-data`
- **Method:** `list_volumes`
- **Current topkey:** `Volumes`
- **Current key:** `VolumeId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_volumes' not found on client 'finspace-data'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_load_balancer_policy`

- **Client:** `elbv2`
- **Method:** `describe_load_balancer_policy_types`
- **Current topkey:** `Policies`
- **Current key:** `PolicyName`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_load_balancer_policy_types' not found on client 'elbv2'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_macie2_classification_export_configuration`

- **Client:** `macie2`
- **Method:** `list_classification_export_configurations`
- **Current topkey:** `ClassificationExportConfigurations`
- **Current key:** `Id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_classification_export_configurations' not found on client 'macie2'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_macie2_classification_job`

- **Client:** `macie2`
- **Method:** `list_jobs`
- **Current topkey:** `ClassificationJobs`
- **Current key:** `Id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_jobs' not found on client 'macie2'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_macie2_member`

- **Client:** `macie2`
- **Method:** `list_invitation_accepters`
- **Current topkey:** `InvitationAccepters`
- **Current key:** `AccountId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_invitation_accepters' not found on client 'macie2'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_msk_cluster_policy`

- **Client:** `kafka`
- **Method:** `list_cluster_policies`
- **Current topkey:** `ClusterPolicies`
- **Current key:** `PolicyName`
- **Error Type:** `method_not_found`

**Error:** Method 'list_cluster_policies' not found on client 'kafka'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_neptune_cluster_instance`

- **Client:** `neptune`
- **Method:** `describe_db_cluster_instances`
- **Current topkey:** `DBClusterInstances`
- **Current key:** `DBInstanceIdentifier`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_db_cluster_instances' not found on client 'neptune'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_networkfirewall_logging_configuration`

- **Client:** `network-firewall`
- **Method:** `list_logging_configurations`
- **Current topkey:** `LoggingConfigurations`
- **Current key:** `FirewallArn`
- **Error Type:** `method_not_found`

**Error:** Method 'list_logging_configurations' not found on client 'network-firewall'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_networkfirewall_resource_policy`

- **Client:** `network-firewall`
- **Method:** `list_resource_policies`
- **Current topkey:** `ResourcePolicies`
- **Current key:** `ResourceArn`
- **Error Type:** `method_not_found`

**Error:** Method 'list_resource_policies' not found on client 'network-firewall'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_networkmanager_attachment_accepter`

- **Client:** `networkmanager`
- **Method:** `list_attachment_accepters`
- **Current topkey:** `AttachmentAccepters`
- **Current key:** `AttachmentId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_attachment_accepters' not found on client 'networkmanager'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_networkmanager_connect_attachment`

- **Client:** `networkmanager`
- **Method:** `list_connect_attachments`
- **Current topkey:** `ConnectAttachments`
- **Current key:** `AttachmentId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_connect_attachments' not found on client 'networkmanager'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_networkmanager_connection`

- **Client:** `networkmanager`
- **Method:** `list_connections`
- **Current topkey:** `Connections`
- **Current key:** `ConnectionId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_connections' not found on client 'networkmanager'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_networkmanager_core_network_policy_attachment`

- **Client:** `networkmanager`
- **Method:** `list_core_network_policy_attachments`
- **Current topkey:** `CoreNetworkPolicyAttachments`
- **Current key:** `CoreNetworkPolicyAttachmentId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_core_network_policy_attachments' not found on client 'networkmanager'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_networkmanager_customer_gateway_association`

- **Client:** `networkmanager`
- **Method:** `list_customer_gateway_associations`
- **Current topkey:** `CustomerGatewayAssociations`
- **Current key:** `CustomerGatewayAssociationId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_customer_gateway_associations' not found on client 'networkmanager'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_networkmanager_link`

- **Client:** `networkmanager`
- **Method:** `list_links`
- **Current topkey:** `Links`
- **Current key:** `LinkId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_links' not found on client 'networkmanager'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_networkmanager_link_association`

- **Client:** `networkmanager`
- **Method:** `list_link_associations`
- **Current topkey:** `LinkAssociations`
- **Current key:** `LinkAssociationId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_link_associations' not found on client 'networkmanager'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_networkmanager_site_to_site_vpn_attachment`

- **Client:** `networkmanager`
- **Method:** `list_site_to_site_vpn_attachments`
- **Current topkey:** `SiteToSiteVpnAttachments`
- **Current key:** `SiteToSiteVpnAttachmentId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_site_to_site_vpn_attachments' not found on client 'networkmanager'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_networkmanager_transit_gateway_connect_peer_association`

- **Client:** `networkmanager`
- **Method:** `list_transit_gateway_connect_peers`
- **Current topkey:** `TransitGatewayConnectPeers`
- **Current key:** `TransitGatewayConnectPeerId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_transit_gateway_connect_peers' not found on client 'networkmanager'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_networkmanager_transit_gateway_peering`

- **Client:** `networkmanager`
- **Method:** `list_transit_gateway_peerings`
- **Current topkey:** `TransitGatewayPeerings`
- **Current key:** `TransitGatewayPeeringId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_transit_gateway_peerings' not found on client 'networkmanager'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_networkmanager_transit_gateway_route_table_attachment`

- **Client:** `networkmanager`
- **Method:** `list_transit_gateway_route_tables`
- **Current topkey:** `TransitGatewayRouteTables`
- **Current key:** `TransitGatewayRouteTableId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_transit_gateway_route_tables' not found on client 'networkmanager'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_networkmanager_vpc_attachment`

- **Client:** `networkmanager`
- **Method:** `list_vpc_attachments`
- **Current topkey:** `VpcAttachments`
- **Current key:** `VpcAttachmentId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_vpc_attachments' not found on client 'networkmanager'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_networkmonitor_probe`

- **Client:** `networkmonitor`
- **Method:** `list_monitor_probes`
- **Current topkey:** `probes`
- **Current key:** `probeArn`
- **Error Type:** `method_not_found`

**Error:** Method 'list_monitor_probes' not found on client 'networkmonitor'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_oam_link`

- **Client:** `networkmanager`
- **Method:** `list_links`
- **Current topkey:** `Links`
- **Current key:** `LinkId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_links' not found on client 'networkmanager'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_oam_sink`

- **Client:** `networkmanager`
- **Method:** `list_links`
- **Current topkey:** `Links`
- **Current key:** `LinkId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_links' not found on client 'networkmanager'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_oam_sink_policy`

- **Client:** `networkmanager`
- **Method:** `list_links`
- **Current topkey:** `Links`
- **Current key:** `LinkId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_links' not found on client 'networkmanager'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_opensearch_inbound_connection_accepter`

- **Client:** `opensearch`
- **Method:** `list_inbound_connection_accepters`
- **Current topkey:** `InboundConnectionAccepters`
- **Current key:** `ConnectionId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_inbound_connection_accepters' not found on client 'opensearch'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_opensearch_outbound_connection`

- **Client:** `opensearch`
- **Method:** `list_inbound_connection_accepters`
- **Current topkey:** `InboundConnectionAccepters`
- **Current key:** `InboundConnectionId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_inbound_connection_accepters' not found on client 'opensearch'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_opensearch_package`

- **Client:** `opensearch`
- **Method:** `list_packages`
- **Current topkey:** `Packages`
- **Current key:** `PackageID`
- **Error Type:** `method_not_found`

**Error:** Method 'list_packages' not found on client 'opensearch'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_opensearch_package_association`

- **Client:** `opensearch`
- **Method:** `list_packages`
- **Current topkey:** `Packages`
- **Current key:** `PackageID`
- **Error Type:** `method_not_found`

**Error:** Method 'list_packages' not found on client 'opensearch'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_pinpoint_adm_channel`

- **Client:** `pinpoint`
- **Method:** `list_adm_channels`
- **Current topkey:** `AdmChannels`
- **Current key:** `Id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_adm_channels' not found on client 'pinpoint'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_pinpoint_apns_channel`

- **Client:** `pinpoint`
- **Method:** `list_apns_channels`
- **Current topkey:** `ApnsChannels`
- **Current key:** `Id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_apns_channels' not found on client 'pinpoint'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_pinpoint_apns_sandbox_channel`

- **Client:** `pinpoint`
- **Method:** `list_apns_sandbox_channels`
- **Current topkey:** `ApnsSandboxChannels`
- **Current key:** `Id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_apns_sandbox_channels' not found on client 'pinpoint'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_pinpoint_apns_voip_channel`

- **Client:** `pinpoint`
- **Method:** `list_apns_voip_channels`
- **Current topkey:** `ApnsVoipChannels`
- **Current key:** `Id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_apns_voip_channels' not found on client 'pinpoint'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_pinpoint_apns_voip_sandbox_channel`

- **Client:** `pinpoint`
- **Method:** `list_apns_voip_sandbox_channels`
- **Current topkey:** `ApnsVoipSandboxChannels`
- **Current key:** `Id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_apns_voip_sandbox_channels' not found on client 'pinpoint'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_pinpoint_app`

- **Client:** `pinpoint`
- **Method:** `list_apps`
- **Current topkey:** `Apps`
- **Current key:** `Id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_apps' not found on client 'pinpoint'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_pinpoint_baidu_channel`

- **Client:** `pinpoint`
- **Method:** `list_baidu_channels`
- **Current topkey:** `BaiduChannels`
- **Current key:** `Id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_baidu_channels' not found on client 'pinpoint'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_pinpoint_email_channel`

- **Client:** `pinpoint`
- **Method:** `list_email_channels`
- **Current topkey:** `EmailChannels`
- **Current key:** `Id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_email_channels' not found on client 'pinpoint'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_pinpoint_email_template`

- **Client:** `pinpoint-email`
- **Method:** `list_email_templates`
- **Current topkey:** `TemplatesMetadata`
- **Current key:** `TemplateName`
- **Error Type:** `method_not_found`

**Error:** Method 'list_email_templates' not found on client 'pinpoint-email'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_pinpoint_event_stream`

- **Client:** `pinpoint`
- **Method:** `list_event_streams`
- **Current topkey:** `EventStreams`
- **Current key:** `Id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_event_streams' not found on client 'pinpoint'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_pinpoint_gcm_channel`

- **Client:** `pinpoint`
- **Method:** `list_gcm_channels`
- **Current topkey:** `GcmChannels`
- **Current key:** `Id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_gcm_channels' not found on client 'pinpoint'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_pinpoint_sms_channel`

- **Client:** `pinpoint`
- **Method:** `list_sms_channels`
- **Current topkey:** `SmsChannels`
- **Current key:** `Id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_sms_channels' not found on client 'pinpoint'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_proxy_protocol_policy`

- **Client:** `wafv2`
- **Method:** `list_proxy_protocol_policies`
- **Current topkey:** `ProxyProtocolPolicies`
- **Current key:** `Name`
- **Error Type:** `method_not_found`

**Error:** Method 'list_proxy_protocol_policies' not found on client 'wafv2'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_quicksight_account_subscription`

- **Client:** `quicksight`
- **Method:** `list_account_subscriptions`
- **Current topkey:** `AccountSubscriptions`
- **Current key:** `SubscriptionId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_account_subscriptions' not found on client 'quicksight'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_quicksight_folder_membership`

- **Client:** `quicksight`
- **Method:** `list_folder_memberships`
- **Current topkey:** `FolderMemberships`
- **Current key:** `FolderMembershipId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_folder_memberships' not found on client 'quicksight'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_quicksight_key_registration`

- **Client:** `quicksight`
- **Method:** `list_key_registrations`
- **Current topkey:** `KeyRegistrations`
- **Current key:** `KeyArn`
- **Error Type:** `method_not_found`

**Error:** Method 'list_key_registrations' not found on client 'quicksight'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_ram_resource_share_accepter`

- **Client:** `ram`
- **Method:** `list_resource_share_accepters`
- **Current topkey:** `ResourceShareAccepters`
- **Current key:** `ResourceShareAccepterArn`
- **Error Type:** `method_not_found`

**Error:** Method 'list_resource_share_accepters' not found on client 'ram'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_ram_sharing_with_organization`

- **Client:** `ram`
- **Method:** `list_sharing_accounts`
- **Current topkey:** `AccountIds`
- **Current key:** `AccountId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_sharing_accounts' not found on client 'ram'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_rbin_rule`

- **Client:** `rbin`
- **Method:** `list_resolver_rules`
- **Current topkey:** `ResolverRules`
- **Current key:** `Id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_resolver_rules' not found on client 'rbin'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_redshiftserverless_resource_policy`

- **Client:** `redshift-serverless`
- **Method:** `describe_resource_policies`
- **Current topkey:** `ResourcePolicies`
- **Current key:** `ResourcePolicyId`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_resource_policies' not found on client 'redshift-serverless'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_resourceexplorer2_index`

- **Client:** `resource-explorer-2`
- **Method:** `list_indices`
- **Current topkey:** `Indices`
- **Current key:** `Name`
- **Error Type:** `method_not_found`

**Error:** Method 'list_indices' not found on client 'resource-explorer-2'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_resourcegroups_resource`

- **Client:** `resource-groups`
- **Method:** `list_resources`
- **Current topkey:** `ResourceIdentifiers`
- **Current key:** `ResourceArn`
- **Error Type:** `method_not_found`

**Error:** Method 'list_resources' not found on client 'resource-groups'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_route53_resolver_firewall_rule`

- **Client:** `route53resolver`
- **Method:** `list_resolver_firewall_rules`
- **Current topkey:** `ResolverFirewallRules`
- **Current key:** `Id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_resolver_firewall_rules' not found on client 'route53resolver'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_rum_metrics_destination`

- **Client:** `rum`
- **Method:** `list_metrics_destinations`
- **Current topkey:** `MetricsDestinations`
- **Current key:** `Name`
- **Error Type:** `method_not_found`

**Error:** Method 'list_metrics_destinations' not found on client 'rum'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_s3control_bucket`

- **Client:** `s3control`
- **Method:** `list_buckets`
- **Current topkey:** `Buckets`
- **Current key:** `Name`
- **Error Type:** `method_not_found`

**Error:** Method 'list_buckets' not found on client 's3control'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_sagemaker_endpoint_configuration`

- **Client:** `sagemaker`
- **Method:** `list_endpoint_configurations`
- **Current topkey:** `EndpointConfigurations`
- **Current key:** `EndpointConfigurationArn`
- **Error Type:** `method_not_found`

**Error:** Method 'list_endpoint_configurations' not found on client 'sagemaker'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_sagemaker_servicecatalog_portfolio_status`

- **Client:** `sagemaker`
- **Method:** `get_service_catalog_portfolio_status`
- **Current topkey:** `Status`
- **Current key:** `Status`
- **Error Type:** `method_not_found`

**Error:** Method 'get_service_catalog_portfolio_status' not found on client 'sagemaker'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_schemas_registry_policy`

- **Client:** `schemas`
- **Method:** `get_registry_policy`
- **Current topkey:** `Policy`
- **Current key:** `Policy`
- **Error Type:** `method_not_found`

**Error:** Method 'get_registry_policy' not found on client 'schemas'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_securityhub_finding_aggregator`

- **Client:** `securityhub`
- **Method:** `describe_finding_aggregators`
- **Current topkey:** `FindingAggregators`
- **Current key:** `FindingAggregatorArn`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_finding_aggregators' not found on client 'securityhub'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_securityhub_insight`

- **Client:** `securityhub`
- **Method:** `describe_insights`
- **Current topkey:** `Insights`
- **Current key:** `InsightArn`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_insights' not found on client 'securityhub'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_securityhub_invite_accepter`

- **Client:** `securityhub`
- **Method:** `describe_invite_accepters`
- **Current topkey:** `InviteAccepters`
- **Current key:** `InviteAccepterArn`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_invite_accepters' not found on client 'securityhub'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_securityhub_member`

- **Client:** `securityhub`
- **Method:** `describe_members`
- **Current topkey:** `Members`
- **Current key:** `MemberArn`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_members' not found on client 'securityhub'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_securityhub_organization_admin_account`

- **Client:** `securityhub`
- **Method:** `describe_organization_admin_account`
- **Current topkey:** `AdminAccount`
- **Current key:** `AdminAccount`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_organization_admin_account' not found on client 'securityhub'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_securityhub_product_subscription`

- **Client:** `securityhub`
- **Method:** `describe_product_subscriptions`
- **Current topkey:** `ProductSubscriptions`
- **Current key:** `ProductSubscriptionArn`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_product_subscriptions' not found on client 'securityhub'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_securityhub_standards_subscription`

- **Client:** `securityhub`
- **Method:** `describe_standards_subscriptions`
- **Current topkey:** `StandardsSubscriptions`
- **Current key:** `StandardsSubscriptionArn`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_standards_subscriptions' not found on client 'securityhub'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_securitylake_data_lake`

- **Client:** `securitylake`
- **Method:** `describe_data_lakes`
- **Current topkey:** `DataLakes`
- **Current key:** `DataLakeArn`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_data_lakes' not found on client 'securitylake'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_servicecatalog_budget_resource_association`

- **Client:** `servicecatalog`
- **Method:** `list_budget_resource_associations`
- **Current topkey:** `BudgetResourceAssociations`
- **Current key:** `BudgetResourceAssociationId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_budget_resource_associations' not found on client 'servicecatalog'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_servicecatalog_organizations_access`

- **Client:** `servicecatalog`
- **Method:** `list_organization_access`
- **Current topkey:** `OrganizationAccess`
- **Current key:** `Id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_organization_access' not found on client 'servicecatalog'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_servicecatalog_portfolio_share`

- **Client:** `servicecatalog`
- **Method:** `list_portfolio_shares`
- **Current topkey:** `PortfolioShares`
- **Current key:** `Id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_portfolio_shares' not found on client 'servicecatalog'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_servicecatalog_principal_portfolio_association`

- **Client:** `servicecatalog`
- **Method:** `list_principal_portfolio_associations`
- **Current topkey:** `Principals`
- **Current key:** `PrincipalARN`
- **Error Type:** `method_not_found`

**Error:** Method 'list_principal_portfolio_associations' not found on client 'servicecatalog'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_servicecatalog_product_portfolio_association`

- **Client:** `servicecatalog`
- **Method:** `list_product_portfolio_associations`
- **Current topkey:** `PortfolioDetails`
- **Current key:** `Id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_product_portfolio_associations' not found on client 'servicecatalog'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_servicecatalog_provisioned_product`

- **Client:** `servicecatalog`
- **Method:** `list_provisioned_products`
- **Current topkey:** `ProvisionedProducts`
- **Current key:** `Id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_provisioned_products' not found on client 'servicecatalog'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_servicecatalog_tag_option_resource_association`

- **Client:** `servicecatalog`
- **Method:** `list_tag_option_resource_associations`
- **Current topkey:** `TagOptionResourceAssociations`
- **Current key:** `Id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_tag_option_resource_associations' not found on client 'servicecatalog'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_servicecatalogappregistry_attribute_group_association`

- **Client:** `servicecatalog-appregistry`
- **Method:** `list_attribute_group_associations`
- **Current topkey:** `attributeGroupAssociations`
- **Current key:** `id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_attribute_group_associations' not found on client 'servicecatalog-appregistry'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_servicequotas_template`

- **Client:** `service-quotas`
- **Method:** `list_templates`
- **Current topkey:** `Templates`
- **Current key:** `TemplateId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_templates' not found on client 'service-quotas'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_servicequotas_template_association`

- **Client:** `service-quotas`
- **Method:** `list_template_associations`
- **Current topkey:** `TemplateAssociations`
- **Current key:** `TemplateAssociationId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_template_associations' not found on client 'service-quotas'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_ses_configuration_set`

- **Client:** `ses`
- **Method:** `describe_configuration_sets`
- **Current topkey:** `ConfigurationSets`
- **Current key:** `Name`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_configuration_sets' not found on client 'ses'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_ses_domain_dkim`

- **Client:** `ses`
- **Method:** `describe_domain_dkim`
- **Current topkey:** `DkimAttributes`
- **Current key:** `DkimTokens`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_domain_dkim' not found on client 'ses'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_ses_domain_identity`

- **Client:** `ses`
- **Method:** `describe_domain_identity`
- **Current topkey:** `DomainIdentities`
- **Current key:** `DomainIdentity`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_domain_identity' not found on client 'ses'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_ses_domain_identity_verification`

- **Client:** `ses`
- **Method:** `describe_domain_identity_verification`
- **Current topkey:** `VerificationToken`
- **Current key:** `VerificationToken`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_domain_identity_verification' not found on client 'ses'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_ses_domain_mail_from`

- **Client:** `ses`
- **Method:** `describe_domain_mail_from`
- **Current topkey:** `MailFromAttributes`
- **Current key:** `MailFromDomain`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_domain_mail_from' not found on client 'ses'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_ses_email_identity`

- **Client:** `ses`
- **Method:** `describe_email_identity`
- **Current topkey:** `IdentityType`
- **Current key:** `IdentityType`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_email_identity' not found on client 'ses'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_ses_event_destination`

- **Client:** `ses`
- **Method:** `describe_event_destination`
- **Current topkey:** `EventDestination`
- **Current key:** `EventDestination`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_event_destination' not found on client 'ses'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_ses_identity_notification_topic`

- **Client:** `ses`
- **Method:** `describe_identity_notification_topic`
- **Current topkey:** `Identity`
- **Current key:** `Identity`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_identity_notification_topic' not found on client 'ses'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_ses_identity_policy`

- **Client:** `ses`
- **Method:** `describe_identity_policy`
- **Current topkey:** `Policy`
- **Current key:** `Policy`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_identity_policy' not found on client 'ses'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_ses_receipt_filter`

- **Client:** `ses`
- **Method:** `describe_receipt_filter`
- **Current topkey:** `Filter`
- **Current key:** `Filter`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_receipt_filter' not found on client 'ses'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_ses_template`

- **Client:** `ses`
- **Method:** `describe_template`
- **Current topkey:** `Template`
- **Current key:** `Template`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_template' not found on client 'ses'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_shield_application_layer_automatic_response`

- **Client:** `shield`
- **Method:** `list_application_layer_automatic_response_associations`
- **Current topkey:** `ApplicationLayerAutomaticResponseAssociations`
- **Current key:** `Id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_application_layer_automatic_response_associations' not found on client 'shield'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_shield_drt_access_log_bucket_association`

- **Client:** `shield`
- **Method:** `list_drt_access_log_bucket_associations`
- **Current topkey:** `DrtAccessLogBucketAssociations`
- **Current key:** `Id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_drt_access_log_bucket_associations' not found on client 'shield'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_shield_drt_access_role_arn_association`

- **Client:** `shield`
- **Method:** `list_drt_access_role_arn_associations`
- **Current topkey:** `DrtAccessRoleArnAssociations`
- **Current key:** `Id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_drt_access_role_arn_associations' not found on client 'shield'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_shield_protection_health_check_association`

- **Client:** `shield`
- **Method:** `list_protection_health_check_associations`
- **Current topkey:** `ProtectionHealthCheckAssociations`
- **Current key:** `Id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_protection_health_check_associations' not found on client 'shield'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_snapshot_create_volume_permission`

- **Client:** `ec2`
- **Method:** `describe_create_volume_permissions`
- **Current topkey:** `CreateVolumePermissions`
- **Current key:** `UserId`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_create_volume_permissions' not found on client 'ec2'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_sns_sms_preferences`

- **Client:** `sns`
- **Method:** `get_sms_preferences`
- **Current topkey:** `SMSPreferences`
- **Current key:** `SMSPreferences`
- **Error Type:** `method_not_found`

**Error:** Method 'get_sms_preferences' not found on client 'sns'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_ssm_patch_group`

- **Client:** `ssm`
- **Method:** `list_patch_groups`
- **Current topkey:** `PatchGroups`
- **Current key:** `PatchGroup`
- **Error Type:** `method_not_found`

**Error:** Method 'list_patch_groups' not found on client 'ssm'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_ssoadmin_application_assignment_configuration`

- **Client:** `sso-admin`
- **Method:** `list_application_assignment_configurations`
- **Current topkey:** `ApplicationAssignmentConfigurations`
- **Current key:** `AccountAssignmentCreationTime`
- **Error Type:** `method_not_found`

**Error:** Method 'list_application_assignment_configurations' not found on client 'sso-admin'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_ssoadmin_customer_managed_policy_attachment`

- **Client:** `sso-admin`
- **Method:** `list_customer_managed_policy_attachments`
- **Current topkey:** `CustomerManagedPolicyAttachments`
- **Current key:** `AccountAssignmentCreationTime`
- **Error Type:** `method_not_found`

**Error:** Method 'list_customer_managed_policy_attachments' not found on client 'sso-admin'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_ssoadmin_instance_access_control_attributes`

- **Client:** `sso-admin`
- **Method:** `list_instance_access_control_attribute_configuration`
- **Current topkey:** `InstanceAccessControlAttributeConfiguration`
- **Current key:** `AccountAssignmentCreationTime`
- **Error Type:** `method_not_found`

**Error:** Method 'list_instance_access_control_attribute_configuration' not found on client 'sso-admin'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_ssoadmin_managed_policy_attachment`

- **Client:** `sso-admin`
- **Method:** `list_managed_policy_attachments`
- **Current topkey:** `ManagedPolicyAttachments`
- **Current key:** `AccountAssignmentCreationTime`
- **Error Type:** `method_not_found`

**Error:** Method 'list_managed_policy_attachments' not found on client 'sso-admin'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_ssoadmin_permission_set_inline_policy`

- **Client:** `sso-admin`
- **Method:** `list_permission_set_inline_policies`
- **Current topkey:** `PermissionSetInlinePolicies`
- **Current key:** `PermissionSetArn`
- **Error Type:** `method_not_found`

**Error:** Method 'list_permission_set_inline_policies' not found on client 'sso-admin'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_ssoadmin_permissions_boundary_attachment`

- **Client:** `sso-admin`
- **Method:** `list_permissions_boundary_attachments`
- **Current topkey:** `PermissionsBoundaryAttachments`
- **Current key:** `AccountAssignmentCreationTime`
- **Error Type:** `method_not_found`

**Error:** Method 'list_permissions_boundary_attachments' not found on client 'sso-admin'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_storagegateway_gateway`

- **Client:** `storagegateway`
- **Method:** `describe_gateways`
- **Current topkey:** `Gateways`
- **Current key:** `GatewayARN`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_gateways' not found on client 'storagegateway'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_storagegateway_tape_pool`

- **Client:** `storagegateway`
- **Method:** `describe_tape_pools`
- **Current topkey:** `TapePools`
- **Current key:** `PoolARN`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_tape_pools' not found on client 'storagegateway'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_synthetics_canary`

- **Client:** `synthetics`
- **Method:** `list_canaries`
- **Current topkey:** `Canaries`
- **Current key:** `Name`
- **Error Type:** `method_not_found`

**Error:** Method 'list_canaries' not found on client 'synthetics'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_synthetics_group`

- **Client:** `synthetics`
- **Method:** `list_canary_groups`
- **Current topkey:** `Groups`
- **Current key:** `Name`
- **Error Type:** `method_not_found`

**Error:** Method 'list_canary_groups' not found on client 'synthetics'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_synthetics_group_association`

- **Client:** `synthetics`
- **Method:** `list_group_associations`
- **Current topkey:** `GroupAssociations`
- **Current key:** `Name`
- **Error Type:** `method_not_found`

**Error:** Method 'list_group_associations' not found on client 'synthetics'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_transfer_ssh_key`

- **Client:** `transfer`
- **Method:** `list_ssh_public_keys`
- **Current topkey:** `SshPublicKeys`
- **Current key:** `Arn`
- **Error Type:** `method_not_found`

**Error:** Method 'list_ssh_public_keys' not found on client 'transfer'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_transfer_tag`

- **Client:** `transfer`
- **Method:** `list_tags`
- **Current topkey:** `Tags`
- **Current key:** `Key`
- **Error Type:** `method_not_found`

**Error:** Method 'list_tags' not found on client 'transfer'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_vpc_dhcp_options_association`

- **Client:** `ec2`
- **Method:** `describe_dhcp_options_associations`
- **Current topkey:** `DhcpOptionsAssociations`
- **Current key:** `DhcpOptionsId`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_dhcp_options_associations' not found on client 'ec2'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_vpc_endpoint_service_allowed_principal`

- **Client:** `ec2`
- **Method:** `describe_vpc_endpoint_service_allowed_principals`
- **Current topkey:** `AllowedPrincipals`
- **Current key:** `Principal`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_vpc_endpoint_service_allowed_principals' not found on client 'ec2'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_vpc_endpoint_subnet_association`

- **Client:** `ec2`
- **Method:** `describe_vpc_endpoint_subnet_associations`
- **Current topkey:** `SubnetAssociations`
- **Current key:** `SubnetId`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_vpc_endpoint_subnet_associations' not found on client 'ec2'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_vpc_ipam_organization_admin_account`

- **Client:** `ec2`
- **Method:** `describe_ipam_organization_admin_accounts`
- **Current topkey:** `OrganizationAdminAccounts`
- **Current key:** `AccountId`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_ipam_organization_admin_accounts' not found on client 'ec2'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_vpc_ipam_preview_next_cidr`

- **Client:** `ec2`
- **Method:** `describe_ipam_preview_next_cidrs`
- **Current topkey:** `Cidrs`
- **Current key:** `Cidr`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_ipam_preview_next_cidrs' not found on client 'ec2'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_vpc_network_performance_metric_subscription`

- **Client:** `ec2`
- **Method:** `describe_network_insights_path_subscriptions`
- **Current topkey:** `NetworkInsightsPathSubscriptions`
- **Current key:** `NetworkInsightsPathSubscriptionId`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_network_insights_path_subscriptions' not found on client 'ec2'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_vpc_route_server_association`

- **Client:** `ec2`
- **Method:** `describe_route_server_associations`
- **Current topkey:** `RouteServerAssociations`
- **Current key:** `RouteServerAssociationId`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_route_server_associations' not found on client 'ec2'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_vpc_route_server_propagation`

- **Client:** `ec2`
- **Method:** `describe_route_server_propagations`
- **Current topkey:** `RouteServerPropagations`
- **Current key:** `RouteServerPropagationId`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_route_server_propagations' not found on client 'ec2'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_vpc_route_server_vpc_association`

- **Client:** `ec2`
- **Method:** `describe_route_server_vpc_associations`
- **Current topkey:** `RouteServerVpcAssociations`
- **Current key:** `RouteServerVpcAssociationId`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_route_server_vpc_associations' not found on client 'ec2'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_vpclattice_resource_configuration`

- **Client:** `vpc-lattice`
- **Method:** `list_resource_configurations`
- **Current topkey:** `items`
- **Current key:** `id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_resource_configurations' not found on client 'vpc-lattice'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_vpclattice_resource_gateway`

- **Client:** `vpc-lattice`
- **Method:** `list_resource_gateways`
- **Current topkey:** `items`
- **Current key:** `id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_resource_gateways' not found on client 'vpc-lattice'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_vpclattice_service_network_resource_association`

- **Client:** `vpc-lattice`
- **Method:** `list_service_network_resource_associations`
- **Current topkey:** `items`
- **Current key:** `id`
- **Error Type:** `method_not_found`

**Error:** Method 'list_service_network_resource_associations' not found on client 'vpc-lattice'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_vpclattice_target_group_attachment`

- **Client:** `vpc-lattice`
- **Method:** `list_target_group_attachments`
- **Current topkey:** `TargetGroupAttachments`
- **Current key:** `TargetGroupAttachmentId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_target_group_attachments' not found on client 'vpc-lattice'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_vpn_connection_route`

- **Client:** `ec2`
- **Method:** `describe_vpn_connection_routes`
- **Current topkey:** `VpnConnectionRoutes`
- **Current key:** `DestinationCidrBlock`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_vpn_connection_routes' not found on client 'ec2'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_vpn_gateway_attachment`

- **Client:** `ec2`
- **Method:** `describe_vpn_gateway_attachments`
- **Current topkey:** `VpnGatewayAttachments`
- **Current key:** `VpnGatewayId`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_vpn_gateway_attachments' not found on client 'ec2'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_vpn_gateway_route_propagation`

- **Client:** `ec2`
- **Method:** `describe_vpn_gateway_route_propagations`
- **Current topkey:** `VpnGatewayRoutePropagations`
- **Current key:** `VpnGatewayId`
- **Error Type:** `method_not_found`

**Error:** Method 'describe_vpn_gateway_route_propagations' not found on client 'ec2'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_wafregional_web_acl_association`

- **Client:** `waf-regional`
- **Method:** `list_web_acl_associations`
- **Current topkey:** `WebACLAssociations`
- **Current key:** `AssociationId`
- **Error Type:** `method_not_found`

**Error:** Method 'list_web_acl_associations' not found on client 'waf-regional'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

### `aws_xray_resource_policy`

- **Client:** `xray`
- **Method:** `get_resource_policy`
- **Current topkey:** `ResourcePolicy`
- **Current key:** `PolicyName`
- **Error Type:** `method_not_found`

**Error:** Method 'get_resource_policy' not found on client 'xray'

**Action Needed:**
1. Find the correct boto3 method name for this resource
2. Update the `descfn` field in aws_dict.py
3. Re-run verification to confirm fix

## ⚠️  Warnings (Structure Issues)

These resources have API calls that succeed but have structure validation issues:

### `aws_appstream_fleet_stack_association`

- **Client:** `appstream`
- **Method:** `describe_fleets`
- **Current topkey:** `FleetStackAssociations`
- **Current key:** `FleetName`
- **Actual Response Keys:** `Fleets`, `ResponseMetadata`

**Issues:**
- topkey 'FleetStackAssociations' not found in response. Available keys: ['Fleets', 'ResponseMetadata']
- Possible correct topkey values: ['Fleets']

**Recommended Fix:**
```python
aws_appstream_fleet_stack_association = {
    "clfn": "appstream",
    "descfn": "describe_fleets",
    "topkey": "Fleets",  # CHANGED from "FleetStackAssociations"
    "key": "FleetName",
    "filterid": "FleetName"
}
```

### `aws_appsync_graphql_api`

- **Client:** `appsync`
- **Method:** `list_graphql_apis`
- **Current topkey:** `GraphqlApis`
- **Current key:** `ApiId`
- **Actual Response Keys:** `ResponseMetadata`, `graphqlApis`

**Issues:**
- topkey 'GraphqlApis' not found in response. Available keys: ['ResponseMetadata', 'graphqlApis']
- Possible correct topkey values: ['graphqlApis']

**Recommended Fix:**
```python
aws_appsync_graphql_api = {
    "clfn": "appsync",
    "descfn": "list_graphql_apis",
    "topkey": "graphqlApis",  # CHANGED from "GraphqlApis"
    "key": "ApiId",
    "filterid": "ApiId"
}
```

### `aws_auditmanager_account_registration`

- **Client:** `auditmanager`
- **Method:** `get_account_status`
- **Current topkey:** `AccountRegistrations`
- **Current key:** `Id`
- **Actual Response Keys:** `ResponseMetadata`, `status`

**Issues:**
- topkey 'AccountRegistrations' not found in response. Available keys: ['ResponseMetadata', 'status']

**Recommended Fix:**
```python
aws_auditmanager_account_registration = {
    "clfn": "auditmanager",
    "descfn": "get_account_status",
    "topkey": "",  # CHANGED from "AccountRegistrations" - no wrapper key
    "key": "Id",
    "filterid": "Id"
}
```

### `aws_autoscaling_attachment`

- **Client:** `autoscaling`
- **Method:** `describe_auto_scaling_groups`
- **Current topkey:** `Attachments`
- **Current key:** `AttachmentName`
- **Actual Response Keys:** `AutoScalingGroups`, `ResponseMetadata`

**Issues:**
- topkey 'Attachments' not found in response. Available keys: ['AutoScalingGroups', 'ResponseMetadata']
- Possible correct topkey values: ['AutoScalingGroups']

**Recommended Fix:**
```python
aws_autoscaling_attachment = {
    "clfn": "autoscaling",
    "descfn": "describe_auto_scaling_groups",
    "topkey": "AutoScalingGroups",  # CHANGED from "Attachments"
    "key": "AttachmentName",
    "filterid": "AttachmentName"
}
```

### `aws_autoscaling_notification`

- **Client:** `autoscaling`
- **Method:** `describe_notification_configurations`
- **Current topkey:** `Notifications`
- **Current key:** `TopicARN`
- **Actual Response Keys:** `NotificationConfigurations`, `ResponseMetadata`

**Issues:**
- topkey 'Notifications' not found in response. Available keys: ['NotificationConfigurations', 'ResponseMetadata']
- Possible correct topkey values: ['NotificationConfigurations']

**Recommended Fix:**
```python
aws_autoscaling_notification = {
    "clfn": "autoscaling",
    "descfn": "describe_notification_configurations",
    "topkey": "NotificationConfigurations",  # CHANGED from "Notifications"
    "key": "TopicARN",
    "filterid": "TopicARN"
}
```

### `aws_backup_global_settings`

- **Client:** `backup`
- **Method:** `describe_global_settings`
- **Current topkey:** `GlobalSettings`
- **Current key:** `GlobalSettingsName`
- **Actual Response Keys:** `ResponseMetadata`, `GlobalSettings`, `LastUpdateTime`

**Issues:**
- key field 'GlobalSettingsName' not found in response object. Available fields: ['isCrossAccountBackupEnabled', 'isDelegatedAdministratorEnabled', 'isMpaEnabled']

**Recommended Fix:**
```python
aws_backup_global_settings = {
    "clfn": "backup",
    "descfn": "describe_global_settings",
    "topkey": "GlobalSettings",
    "key": "GlobalSettingsName",
    "filterid": "GlobalSettingsName"
}
```

### `aws_backup_region_settings`

- **Client:** `backup`
- **Method:** `describe_region_settings`
- **Current topkey:** `ResourceTypeOptInPreference`
- **Current key:** `null`
- **Actual Response Keys:** `ResponseMetadata`, `ResourceTypeOptInPreference`, `ResourceTypeManagementPreference`

**Issues:**
- key field 'null' not found in response object. Available fields: ['Aurora', 'CloudFormation', 'DSQL', 'DocumentDB', 'DynamoDB', 'EBS', 'EC2', 'EFS', 'EKS', 'FSx', 'Neptune', 'RDS', 'Redshift', 'Redshift Serverless', 'S3', 'SAP HANA on Amazon EC2', 'Storage Gateway', 'Timestream', 'VirtualMachine']

**Recommended Fix:**
```python
aws_backup_region_settings = {
    "clfn": "backup",
    "descfn": "describe_region_settings",
    "topkey": "ResourceTypeOptInPreference",
    "key": "null",
    "filterid": "null"
}
```

### `aws_bedrock_model_invocation_logging_configuration`

- **Client:** `bedrock`
- **Method:** `get_model_invocation_logging_configuration`
- **Current topkey:** `loggingConfig`
- **Current key:** `null`
- **Actual Response Keys:** `ResponseMetadata`

**Issues:**
- topkey 'loggingConfig' not found in response. Available keys: ['ResponseMetadata']

**Recommended Fix:**
```python
aws_bedrock_model_invocation_logging_configuration = {
    "clfn": "bedrock",
    "descfn": "get_model_invocation_logging_configuration",
    "topkey": "",  # CHANGED from "loggingConfig" - no wrapper key
    "key": "null",
    "filterid": "null"
}
```

### `aws_bedrockagentcore_memory_strategy`

- **Client:** `bedrock-agentcore-control`
- **Method:** `list_memories`
- **Current topkey:** `memoryStrategies`
- **Current key:** `strategyId`
- **Actual Response Keys:** `ResponseMetadata`, `memories`

**Issues:**
- topkey 'memoryStrategies' not found in response. Available keys: ['ResponseMetadata', 'memories']
- Possible correct topkey values: ['memories']

**Recommended Fix:**
```python
aws_bedrockagentcore_memory_strategy = {
    "clfn": "bedrock-agentcore-control",
    "descfn": "list_memories",
    "topkey": "memories",  # CHANGED from "memoryStrategies"
    "key": "strategyId",
    "filterid": "strategyId"
}
```

### `aws_bedrockagentcore_token_vault_cmk`

- **Client:** `bedrock-agentcore-control`
- **Method:** `get_token_vault`
- **Current topkey:** `tokenVault`
- **Current key:** `vaultId`
- **Actual Response Keys:** `ResponseMetadata`, `tokenVaultId`, `kmsConfiguration`, `lastModifiedDate`

**Issues:**
- topkey 'tokenVault' not found in response. Available keys: ['ResponseMetadata', 'tokenVaultId', 'kmsConfiguration', 'lastModifiedDate']
- Possible correct topkey values: ['kmsConfiguration']

**Recommended Fix:**
```python
aws_bedrockagentcore_token_vault_cmk = {
    "clfn": "bedrock-agentcore-control",
    "descfn": "get_token_vault",
    "topkey": "kmsConfiguration",  # CHANGED from "tokenVault"
    "key": "vaultId",
    "filterid": "vaultId"
}
```

### `aws_ce_cost_category`

- **Client:** `ce`
- **Method:** `list_cost_category_definitions`
- **Current topkey:** `CostCategories`
- **Current key:** `CostCategoryArn`
- **Actual Response Keys:** `CostCategoryReferences`, `ResponseMetadata`

**Issues:**
- topkey 'CostCategories' not found in response. Available keys: ['CostCategoryReferences', 'ResponseMetadata']
- Possible correct topkey values: ['CostCategoryReferences']

**Recommended Fix:**
```python
aws_ce_cost_category = {
    "clfn": "ce",
    "descfn": "list_cost_category_definitions",
    "topkey": "CostCategoryReferences",  # CHANGED from "CostCategories"
    "key": "CostCategoryArn",
    "filterid": "CostCategoryArn"
}
```

### `aws_chimesdkmediapipelines_media_insights_pipeline_configuration`

- **Client:** `chime-sdk-media-pipelines`
- **Method:** `list_media_insights_pipeline_configurations`
- **Current topkey:** `MediaInsightsPipelines`
- **Current key:** `Name`
- **Actual Response Keys:** `ResponseMetadata`, `MediaInsightsPipelineConfigurations`

**Issues:**
- topkey 'MediaInsightsPipelines' not found in response. Available keys: ['ResponseMetadata', 'MediaInsightsPipelineConfigurations']
- Possible correct topkey values: ['MediaInsightsPipelineConfigurations']

**Recommended Fix:**
```python
aws_chimesdkmediapipelines_media_insights_pipeline_configuration = {
    "clfn": "chime-sdk-media-pipelines",
    "descfn": "list_media_insights_pipeline_configurations",
    "topkey": "MediaInsightsPipelineConfigurations",  # CHANGED from "MediaInsightsPipelines"
    "key": "Name",
    "filterid": "Name"
}
```

### `aws_chimesdkvoice_global_settings`

- **Client:** `chime-sdk-voice`
- **Method:** `get_global_settings`
- **Current topkey:** `GlobalSettings`
- **Current key:** `GlobalSettingsName`
- **Actual Response Keys:** `ResponseMetadata`, `VoiceConnector`

**Issues:**
- topkey 'GlobalSettings' not found in response. Available keys: ['ResponseMetadata', 'VoiceConnector']
- Possible correct topkey values: ['VoiceConnector']

**Recommended Fix:**
```python
aws_chimesdkvoice_global_settings = {
    "clfn": "chime-sdk-voice",
    "descfn": "get_global_settings",
    "topkey": "VoiceConnector",  # CHANGED from "GlobalSettings"
    "key": "GlobalSettingsName",
    "filterid": "GlobalSettingsName"
}
```

### `aws_cloudfront_cache_policy`

- **Client:** `cloudfront`
- **Method:** `list_cache_policies`
- **Current topkey:** `CachePolicyList`
- **Current key:** `CachePolicyId`
- **Actual Response Keys:** `ResponseMetadata`, `CachePolicyList`

**Issues:**
- key field 'CachePolicyId' not found in response object. Available fields: ['MaxItems', 'Quantity', 'Items']

**Recommended Fix:**
```python
aws_cloudfront_cache_policy = {
    "clfn": "cloudfront",
    "descfn": "list_cache_policies",
    "topkey": "CachePolicyList",
    "key": "CachePolicyId",
    "filterid": "CachePolicyId"
}
```

### `aws_cloudfront_continuous_deployment_policy`

- **Client:** `cloudfront`
- **Method:** `list_continuous_deployment_policies`
- **Current topkey:** `ContinuousDeploymentPolicyList`
- **Current key:** `ContinuousDeploymentPolicyId`
- **Actual Response Keys:** `ResponseMetadata`, `ContinuousDeploymentPolicyList`

**Issues:**
- key field 'ContinuousDeploymentPolicyId' not found in response object. Available fields: ['MaxItems', 'Quantity', 'Items']

**Recommended Fix:**
```python
aws_cloudfront_continuous_deployment_policy = {
    "clfn": "cloudfront",
    "descfn": "list_continuous_deployment_policies",
    "topkey": "ContinuousDeploymentPolicyList",
    "key": "ContinuousDeploymentPolicyId",
    "filterid": "ContinuousDeploymentPolicyId"
}
```

### `aws_cloudfront_distribution`

- **Client:** `cloudfront`
- **Method:** `list_distributions`
- **Current topkey:** `DistributionList.Items`
- **Current key:** `Id`
- **Actual Response Keys:** `ResponseMetadata`, `DistributionList`

**Issues:**
- topkey 'DistributionList.Items' not found in response. Available keys: ['ResponseMetadata', 'DistributionList']
- Possible correct topkey values: ['DistributionList']

**Recommended Fix:**
```python
aws_cloudfront_distribution = {
    "clfn": "cloudfront",
    "descfn": "list_distributions",
    "topkey": "DistributionList",  # CHANGED from "DistributionList.Items"
    "key": "Id",
    "filterid": "Id"
}
```

### `aws_cloudfront_field_level_encryption_config`

- **Client:** `cloudfront`
- **Method:** `list_field_level_encryption_configs`
- **Current topkey:** `FieldLevelEncryptionList`
- **Current key:** `Id`
- **Actual Response Keys:** `ResponseMetadata`, `FieldLevelEncryptionList`

**Issues:**
- key field 'Id' not found in response object. Available fields: ['MaxItems', 'Quantity']

**Recommended Fix:**
```python
aws_cloudfront_field_level_encryption_config = {
    "clfn": "cloudfront",
    "descfn": "list_field_level_encryption_configs",
    "topkey": "FieldLevelEncryptionList",
    "key": "Id",
    "filterid": "Id"
}
```

### `aws_cloudfront_field_level_encryption_profile`

- **Client:** `cloudfront`
- **Method:** `list_field_level_encryption_profiles`
- **Current topkey:** `FieldLevelEncryptionProfileList`
- **Current key:** `Id`
- **Actual Response Keys:** `ResponseMetadata`, `FieldLevelEncryptionProfileList`

**Issues:**
- key field 'Id' not found in response object. Available fields: ['MaxItems', 'Quantity']

**Recommended Fix:**
```python
aws_cloudfront_field_level_encryption_profile = {
    "clfn": "cloudfront",
    "descfn": "list_field_level_encryption_profiles",
    "topkey": "FieldLevelEncryptionProfileList",
    "key": "Id",
    "filterid": "Id"
}
```

### `aws_cloudfront_function`

- **Client:** `cloudfront`
- **Method:** `list_functions`
- **Current topkey:** `FunctionList`
- **Current key:** `Name`
- **Actual Response Keys:** `ResponseMetadata`, `FunctionList`

**Issues:**
- key field 'Name' not found in response object. Available fields: ['MaxItems', 'Quantity', 'Items']

**Recommended Fix:**
```python
aws_cloudfront_function = {
    "clfn": "cloudfront",
    "descfn": "list_functions",
    "topkey": "FunctionList",
    "key": "Name",
    "filterid": "Name"
}
```

### `aws_cloudfront_key_group`

- **Client:** `cloudfront`
- **Method:** `list_key_groups`
- **Current topkey:** `KeyGroupList`
- **Current key:** `Id`
- **Actual Response Keys:** `ResponseMetadata`, `KeyGroupList`

**Issues:**
- key field 'Id' not found in response object. Available fields: ['MaxItems', 'Quantity']

**Recommended Fix:**
```python
aws_cloudfront_key_group = {
    "clfn": "cloudfront",
    "descfn": "list_key_groups",
    "topkey": "KeyGroupList",
    "key": "Id",
    "filterid": "Id"
}
```

### `aws_cloudfront_key_value_store`

- **Client:** `cloudfront`
- **Method:** `list_key_value_stores`
- **Current topkey:** `KeyValueStoreList`
- **Current key:** `Id`
- **Actual Response Keys:** `ResponseMetadata`, `KeyValueStoreList`

**Issues:**
- key field 'Id' not found in response object. Available fields: ['MaxItems', 'Quantity', 'Items']

**Recommended Fix:**
```python
aws_cloudfront_key_value_store = {
    "clfn": "cloudfront",
    "descfn": "list_key_value_stores",
    "topkey": "KeyValueStoreList",
    "key": "Id",
    "filterid": "Id"
}
```

### `aws_cloudfront_multitenant_distribution`

- **Client:** `cloudfront`
- **Method:** `list_distributions`
- **Current topkey:** `DistributionList`
- **Current key:** `Id`
- **Actual Response Keys:** `ResponseMetadata`, `DistributionList`

**Issues:**
- key field 'Id' not found in response object. Available fields: ['Marker', 'MaxItems', 'IsTruncated', 'Quantity']

**Recommended Fix:**
```python
aws_cloudfront_multitenant_distribution = {
    "clfn": "cloudfront",
    "descfn": "list_distributions",
    "topkey": "DistributionList",
    "key": "Id",
    "filterid": "Id"
}
```

### `aws_cloudfront_origin_access_control`

- **Client:** `cloudfront`
- **Method:** `list_origin_access_controls`
- **Current topkey:** `OriginAccessControlList`
- **Current key:** `Id`
- **Actual Response Keys:** `ResponseMetadata`, `OriginAccessControlList`

**Issues:**
- key field 'Id' not found in response object. Available fields: ['Marker', 'MaxItems', 'IsTruncated', 'Quantity', 'Items']

**Recommended Fix:**
```python
aws_cloudfront_origin_access_control = {
    "clfn": "cloudfront",
    "descfn": "list_origin_access_controls",
    "topkey": "OriginAccessControlList",
    "key": "Id",
    "filterid": "Id"
}
```

### `aws_cloudfront_origin_access_identity`

- **Client:** `cloudfront`
- **Method:** `list_cloud_front_origin_access_identities`
- **Current topkey:** `CloudFrontOriginAccessIdentityList`
- **Current key:** `Id`
- **Actual Response Keys:** `ResponseMetadata`, `CloudFrontOriginAccessIdentityList`

**Issues:**
- key field 'Id' not found in response object. Available fields: ['Marker', 'MaxItems', 'IsTruncated', 'Quantity', 'Items']

**Recommended Fix:**
```python
aws_cloudfront_origin_access_identity = {
    "clfn": "cloudfront",
    "descfn": "list_cloud_front_origin_access_identities",
    "topkey": "CloudFrontOriginAccessIdentityList",
    "key": "Id",
    "filterid": "Id"
}
```

### `aws_cloudfront_origin_request_policy`

- **Client:** `cloudfront`
- **Method:** `list_cloud_front_origin_access_identities`
- **Current topkey:** `OriginRequestPolicyList`
- **Current key:** `Id`
- **Actual Response Keys:** `ResponseMetadata`, `CloudFrontOriginAccessIdentityList`

**Issues:**
- topkey 'OriginRequestPolicyList' not found in response. Available keys: ['ResponseMetadata', 'CloudFrontOriginAccessIdentityList']
- Possible correct topkey values: ['CloudFrontOriginAccessIdentityList']

**Recommended Fix:**
```python
aws_cloudfront_origin_request_policy = {
    "clfn": "cloudfront",
    "descfn": "list_cloud_front_origin_access_identities",
    "topkey": "CloudFrontOriginAccessIdentityList",  # CHANGED from "OriginRequestPolicyList"
    "key": "Id",
    "filterid": "Id"
}
```

### `aws_cloudfront_public_key`

- **Client:** `cloudfront`
- **Method:** `list_public_keys`
- **Current topkey:** `PublicKeyList`
- **Current key:** `Id`
- **Actual Response Keys:** `ResponseMetadata`, `PublicKeyList`

**Issues:**
- key field 'Id' not found in response object. Available fields: ['MaxItems', 'Quantity']

**Recommended Fix:**
```python
aws_cloudfront_public_key = {
    "clfn": "cloudfront",
    "descfn": "list_public_keys",
    "topkey": "PublicKeyList",
    "key": "Id",
    "filterid": "Id"
}
```

### `aws_cloudfront_realtime_log_config`

- **Client:** `cloudfront`
- **Method:** `list_realtime_log_configs`
- **Current topkey:** `RealtimeLogConfigs`
- **Current key:** `ARN`
- **Actual Response Keys:** `ResponseMetadata`, `RealtimeLogConfigs`

**Issues:**
- key field 'ARN' not found in response object. Available fields: ['MaxItems', 'Items', 'IsTruncated', 'Marker']

**Recommended Fix:**
```python
aws_cloudfront_realtime_log_config = {
    "clfn": "cloudfront",
    "descfn": "list_realtime_log_configs",
    "topkey": "RealtimeLogConfigs",
    "key": "ARN",
    "filterid": "ARN"
}
```

### `aws_cloudfront_response_headers_policy`

- **Client:** `cloudfront`
- **Method:** `list_response_headers_policies`
- **Current topkey:** `ResponseHeadersPolicyList`
- **Current key:** `Id`
- **Actual Response Keys:** `ResponseMetadata`, `ResponseHeadersPolicyList`

**Issues:**
- key field 'Id' not found in response object. Available fields: ['MaxItems', 'Quantity', 'Items']

**Recommended Fix:**
```python
aws_cloudfront_response_headers_policy = {
    "clfn": "cloudfront",
    "descfn": "list_response_headers_policies",
    "topkey": "ResponseHeadersPolicyList",
    "key": "Id",
    "filterid": "Id"
}
```

### `aws_cloudfront_vpc_origin`

- **Client:** `cloudfront`
- **Method:** `list_vpc_origins`
- **Current topkey:** `VpcOriginList`
- **Current key:** `Id`
- **Actual Response Keys:** `ResponseMetadata`, `VpcOriginList`

**Issues:**
- key field 'Id' not found in response object. Available fields: ['MaxItems', 'Quantity', 'Items']

**Recommended Fix:**
```python
aws_cloudfront_vpc_origin = {
    "clfn": "cloudfront",
    "descfn": "list_vpc_origins",
    "topkey": "VpcOriginList",
    "key": "Id",
    "filterid": "Id"
}
```

### `aws_cloudwatch_event_bus_policy`

- **Client:** `events`
- **Method:** `describe_event_bus`
- **Current topkey:** `Policy`
- **Current key:** `Name`
- **Actual Response Keys:** `Name`, `Arn`, `ResponseMetadata`

**Issues:**
- topkey 'Policy' not found in response. Available keys: ['Name', 'Arn', 'ResponseMetadata']

**Recommended Fix:**
```python
aws_cloudwatch_event_bus_policy = {
    "clfn": "events",
    "descfn": "describe_event_bus",
    "topkey": "",  # CHANGED from "Policy" - no wrapper key
    "key": "Name",
    "filterid": "Name"
}
```

### `aws_cloudwatch_event_permission`

- **Client:** `events`
- **Method:** `describe_event_bus`
- **Current topkey:** `Policy`
- **Current key:** `Sid`
- **Actual Response Keys:** `Name`, `Arn`, `ResponseMetadata`

**Issues:**
- topkey 'Policy' not found in response. Available keys: ['Name', 'Arn', 'ResponseMetadata']

**Recommended Fix:**
```python
aws_cloudwatch_event_permission = {
    "clfn": "events",
    "descfn": "describe_event_bus",
    "topkey": "",  # CHANGED from "Policy" - no wrapper key
    "key": "Sid",
    "filterid": "Sid"
}
```

### `aws_codegurureviewer_repository_association`

- **Client:** `codeguru-reviewer`
- **Method:** `list_repository_associations`
- **Current topkey:** `RepositoryAssociations`
- **Current key:** `Name`
- **Actual Response Keys:** `ResponseMetadata`, `RepositoryAssociationSummaries`

**Issues:**
- topkey 'RepositoryAssociations' not found in response. Available keys: ['ResponseMetadata', 'RepositoryAssociationSummaries']
- Possible correct topkey values: ['RepositoryAssociationSummaries']

**Recommended Fix:**
```python
aws_codegurureviewer_repository_association = {
    "clfn": "codeguru-reviewer",
    "descfn": "list_repository_associations",
    "topkey": "RepositoryAssociationSummaries",  # CHANGED from "RepositoryAssociations"
    "key": "Name",
    "filterid": "Name"
}
```

### `aws_comprehend_document_classifier`

- **Client:** `comprehend`
- **Method:** `list_document_classifiers`
- **Current topkey:** `DocumentClassifiers`
- **Current key:** `DocumentClassifierArn`
- **Actual Response Keys:** `DocumentClassifierPropertiesList`, `ResponseMetadata`

**Issues:**
- topkey 'DocumentClassifiers' not found in response. Available keys: ['DocumentClassifierPropertiesList', 'ResponseMetadata']
- Possible correct topkey values: ['DocumentClassifierPropertiesList']

**Recommended Fix:**
```python
aws_comprehend_document_classifier = {
    "clfn": "comprehend",
    "descfn": "list_document_classifiers",
    "topkey": "DocumentClassifierPropertiesList",  # CHANGED from "DocumentClassifiers"
    "key": "DocumentClassifierArn",
    "filterid": "DocumentClassifierArn"
}
```

### `aws_comprehend_entity_recognizer`

- **Client:** `comprehend`
- **Method:** `list_entity_recognizers`
- **Current topkey:** `EntityRecognizers`
- **Current key:** `EntityRecognizerArn`
- **Actual Response Keys:** `EntityRecognizerPropertiesList`, `ResponseMetadata`

**Issues:**
- topkey 'EntityRecognizers' not found in response. Available keys: ['EntityRecognizerPropertiesList', 'ResponseMetadata']
- Possible correct topkey values: ['EntityRecognizerPropertiesList']

**Recommended Fix:**
```python
aws_comprehend_entity_recognizer = {
    "clfn": "comprehend",
    "descfn": "list_entity_recognizers",
    "topkey": "EntityRecognizerPropertiesList",  # CHANGED from "EntityRecognizers"
    "key": "EntityRecognizerArn",
    "filterid": "EntityRecognizerArn"
}
```

### `aws_costoptimizationhub_enrollment_status`

- **Client:** `cost-optimization-hub`
- **Method:** `get_preferences`
- **Current topkey:** `status`
- **Current key:** `status`
- **Actual Response Keys:** `savingsEstimationMode`, `memberAccountDiscountVisibility`, `preferredCommitment`, `ResponseMetadata`

**Issues:**
- topkey 'status' not found in response. Available keys: ['savingsEstimationMode', 'memberAccountDiscountVisibility', 'preferredCommitment', 'ResponseMetadata']
- Possible correct topkey values: ['preferredCommitment']

**Recommended Fix:**
```python
aws_costoptimizationhub_enrollment_status = {
    "clfn": "cost-optimization-hub",
    "descfn": "get_preferences",
    "topkey": "preferredCommitment",  # CHANGED from "status"
    "key": "status",
    "filterid": "status"
}
```

### `aws_costoptimizationhub_preferences`

- **Client:** `cost-optimization-hub`
- **Method:** `get_preferences`
- **Current topkey:** `preferences`
- **Current key:** `memberAccountDiscountVisibility`
- **Actual Response Keys:** `savingsEstimationMode`, `memberAccountDiscountVisibility`, `preferredCommitment`, `ResponseMetadata`

**Issues:**
- topkey 'preferences' not found in response. Available keys: ['savingsEstimationMode', 'memberAccountDiscountVisibility', 'preferredCommitment', 'ResponseMetadata']
- Possible correct topkey values: ['preferredCommitment']

**Recommended Fix:**
```python
aws_costoptimizationhub_preferences = {
    "clfn": "cost-optimization-hub",
    "descfn": "get_preferences",
    "topkey": "preferredCommitment",  # CHANGED from "preferences"
    "key": "memberAccountDiscountVisibility",
    "filterid": "memberAccountDiscountVisibility"
}
```

### `aws_datapipeline_pipeline`

- **Client:** `datapipeline`
- **Method:** `list_pipelines`
- **Current topkey:** `Pipelines`
- **Current key:** `Name`
- **Actual Response Keys:** `pipelineIdList`, `hasMoreResults`, `ResponseMetadata`

**Issues:**
- topkey 'Pipelines' not found in response. Available keys: ['pipelineIdList', 'hasMoreResults', 'ResponseMetadata']
- Possible correct topkey values: ['pipelineIdList']

**Recommended Fix:**
```python
aws_datapipeline_pipeline = {
    "clfn": "datapipeline",
    "descfn": "list_pipelines",
    "topkey": "pipelineIdList",  # CHANGED from "Pipelines"
    "key": "Name",
    "filterid": "Name"
}
```

### `aws_db_instance_role_association`

- **Client:** `rds`
- **Method:** `describe_db_instances`
- **Current topkey:** `DBInstanceRoleAssociations`
- **Current key:** `DBInstanceArn`
- **Actual Response Keys:** `DBInstances`, `ResponseMetadata`

**Issues:**
- topkey 'DBInstanceRoleAssociations' not found in response. Available keys: ['DBInstances', 'ResponseMetadata']
- Possible correct topkey values: ['DBInstances']

**Recommended Fix:**
```python
aws_db_instance_role_association = {
    "clfn": "rds",
    "descfn": "describe_db_instances",
    "topkey": "DBInstances",  # CHANGED from "DBInstanceRoleAssociations"
    "key": "DBInstanceArn",
    "filterid": "DBInstanceArn"
}
```

### `aws_default_vpc_dhcp_options`

- **Client:** `ec2`
- **Method:** `describe_dhcp_options`
- **Current topkey:** `VpcDhcpOptions`
- **Current key:** `VpcDhcpOptionsId`
- **Actual Response Keys:** `DhcpOptions`, `ResponseMetadata`

**Issues:**
- topkey 'VpcDhcpOptions' not found in response. Available keys: ['DhcpOptions', 'ResponseMetadata']
- Possible correct topkey values: ['DhcpOptions']

**Recommended Fix:**
```python
aws_default_vpc_dhcp_options = {
    "clfn": "ec2",
    "descfn": "describe_dhcp_options",
    "topkey": "DhcpOptions",  # CHANGED from "VpcDhcpOptions"
    "key": "VpcDhcpOptionsId",
    "filterid": "VpcDhcpOptionsId"
}
```

### `aws_detective_invitation_accepter`

- **Client:** `detective`
- **Method:** `list_invitations`
- **Current topkey:** `InvitationAccepters`
- **Current key:** `GraphArn`
- **Actual Response Keys:** `ResponseMetadata`, `Invitations`

**Issues:**
- topkey 'InvitationAccepters' not found in response. Available keys: ['ResponseMetadata', 'Invitations']
- Possible correct topkey values: ['Invitations']

**Recommended Fix:**
```python
aws_detective_invitation_accepter = {
    "clfn": "detective",
    "descfn": "list_invitations",
    "topkey": "Invitations",  # CHANGED from "InvitationAccepters"
    "key": "GraphArn",
    "filterid": "GraphArn"
}
```

### `aws_detective_organization_admin_account`

- **Client:** `detective`
- **Method:** `list_organization_admin_accounts`
- **Current topkey:** `OrganizationAdminAccounts`
- **Current key:** `GraphArn`
- **Actual Response Keys:** `ResponseMetadata`, `Administrators`

**Issues:**
- topkey 'OrganizationAdminAccounts' not found in response. Available keys: ['ResponseMetadata', 'Administrators']
- Possible correct topkey values: ['Administrators']

**Recommended Fix:**
```python
aws_detective_organization_admin_account = {
    "clfn": "detective",
    "descfn": "list_organization_admin_accounts",
    "topkey": "Administrators",  # CHANGED from "OrganizationAdminAccounts"
    "key": "GraphArn",
    "filterid": "GraphArn"
}
```

### `aws_devopsguru_event_sources_config`

- **Client:** `devops-guru`
- **Method:** `describe_event_sources_config`
- **Current topkey:** `EventSources`
- **Current key:** `EventSources`
- **Actual Response Keys:** `ResponseMetadata`, `EventSources`

**Issues:**
- key field 'EventSources' not found in response object. Available fields: ['AmazonCodeGuruProfiler']

**Recommended Fix:**
```python
aws_devopsguru_event_sources_config = {
    "clfn": "devops-guru",
    "descfn": "describe_event_sources_config",
    "topkey": "EventSources",
    "key": "EventSources",
    "filterid": "EventSources"
}
```

### `aws_devopsguru_service_integration`

- **Client:** `devops-guru`
- **Method:** `describe_service_integration`
- **Current topkey:** `ServiceIntegration`
- **Current key:** `ServiceIntegration`
- **Actual Response Keys:** `ResponseMetadata`, `ServiceIntegration`

**Issues:**
- key field 'ServiceIntegration' not found in response object. Available fields: ['OpsCenter', 'LogsAnomalyDetection', 'KMSServerSideEncryption']

**Recommended Fix:**
```python
aws_devopsguru_service_integration = {
    "clfn": "devops-guru",
    "descfn": "describe_service_integration",
    "topkey": "ServiceIntegration",
    "key": "ServiceIntegration",
    "filterid": "ServiceIntegration"
}
```

### `aws_directory_service_radius_settings`

- **Client:** `ds`
- **Method:** `describe_directories`
- **Current topkey:** `RadiusSettings`
- **Current key:** `DirectoryId`
- **Actual Response Keys:** `DirectoryDescriptions`, `ResponseMetadata`

**Issues:**
- topkey 'RadiusSettings' not found in response. Available keys: ['DirectoryDescriptions', 'ResponseMetadata']
- Possible correct topkey values: ['DirectoryDescriptions']

**Recommended Fix:**
```python
aws_directory_service_radius_settings = {
    "clfn": "ds",
    "descfn": "describe_directories",
    "topkey": "DirectoryDescriptions",  # CHANGED from "RadiusSettings"
    "key": "DirectoryId",
    "filterid": "DirectoryId"
}
```

### `aws_dms_s3_endpoint`

- **Client:** `dms`
- **Method:** `describe_endpoints`
- **Current topkey:** `S3Endpoints`
- **Current key:** `EndpointIdentifier`
- **Actual Response Keys:** `Endpoints`, `ResponseMetadata`

**Issues:**
- topkey 'S3Endpoints' not found in response. Available keys: ['Endpoints', 'ResponseMetadata']
- Possible correct topkey values: ['Endpoints']

**Recommended Fix:**
```python
aws_dms_s3_endpoint = {
    "clfn": "dms",
    "descfn": "describe_endpoints",
    "topkey": "Endpoints",  # CHANGED from "S3Endpoints"
    "key": "EndpointIdentifier",
    "filterid": "EndpointIdentifier"
}
```

### `aws_docdbelastic_cluster`

- **Client:** `docdb-elastic`
- **Method:** `list_clusters`
- **Current topkey:** `Clusters`
- **Current key:** `ClusterName`
- **Actual Response Keys:** `ResponseMetadata`, `clusters`

**Issues:**
- topkey 'Clusters' not found in response. Available keys: ['ResponseMetadata', 'clusters']
- Possible correct topkey values: ['clusters']

**Recommended Fix:**
```python
aws_docdbelastic_cluster = {
    "clfn": "docdb-elastic",
    "descfn": "list_clusters",
    "topkey": "clusters",  # CHANGED from "Clusters"
    "key": "ClusterName",
    "filterid": "ClusterName"
}
```

### `aws_dsql_cluster_peering`

- **Client:** `dsql`
- **Method:** `list_clusters`
- **Current topkey:** `clusterPeerings`
- **Current key:** `id`
- **Actual Response Keys:** `ResponseMetadata`, `clusters`

**Issues:**
- topkey 'clusterPeerings' not found in response. Available keys: ['ResponseMetadata', 'clusters']
- Possible correct topkey values: ['clusters']

**Recommended Fix:**
```python
aws_dsql_cluster_peering = {
    "clfn": "dsql",
    "descfn": "list_clusters",
    "topkey": "clusters",  # CHANGED from "clusterPeerings"
    "key": "id",
    "filterid": "id"
}
```

### `aws_dx_bgp_peer`

- **Client:** `directconnect`
- **Method:** `describe_virtual_interfaces`
- **Current topkey:** `BgpPeers`
- **Current key:** `BgpPeerId`
- **Actual Response Keys:** `virtualInterfaces`, `ResponseMetadata`

**Issues:**
- topkey 'BgpPeers' not found in response. Available keys: ['virtualInterfaces', 'ResponseMetadata']
- Possible correct topkey values: ['virtualInterfaces']

**Recommended Fix:**
```python
aws_dx_bgp_peer = {
    "clfn": "directconnect",
    "descfn": "describe_virtual_interfaces",
    "topkey": "virtualInterfaces",  # CHANGED from "BgpPeers"
    "key": "BgpPeerId",
    "filterid": "BgpPeerId"
}
```

### `aws_dx_connection_association`

- **Client:** `directconnect`
- **Method:** `describe_connections`
- **Current topkey:** `ConnectionAssociations`
- **Current key:** `ConnectionId`
- **Actual Response Keys:** `connections`, `ResponseMetadata`

**Issues:**
- topkey 'ConnectionAssociations' not found in response. Available keys: ['connections', 'ResponseMetadata']
- Possible correct topkey values: ['connections']

**Recommended Fix:**
```python
aws_dx_connection_association = {
    "clfn": "directconnect",
    "descfn": "describe_connections",
    "topkey": "connections",  # CHANGED from "ConnectionAssociations"
    "key": "ConnectionId",
    "filterid": "ConnectionId"
}
```

### `aws_dx_connection_confirmation`

- **Client:** `directconnect`
- **Method:** `describe_connections`
- **Current topkey:** `Confirmations`
- **Current key:** `ConfirmationToken`
- **Actual Response Keys:** `connections`, `ResponseMetadata`

**Issues:**
- topkey 'Confirmations' not found in response. Available keys: ['connections', 'ResponseMetadata']
- Possible correct topkey values: ['connections']

**Recommended Fix:**
```python
aws_dx_connection_confirmation = {
    "clfn": "directconnect",
    "descfn": "describe_connections",
    "topkey": "connections",  # CHANGED from "Confirmations"
    "key": "ConfirmationToken",
    "filterid": "ConfirmationToken"
}
```

### `aws_dx_hosted_connection`

- **Client:** `directconnect`
- **Method:** `describe_connections`
- **Current topkey:** `GatewayAssociationProposals`
- **Current key:** `ProposalId`
- **Actual Response Keys:** `connections`, `ResponseMetadata`

**Issues:**
- topkey 'GatewayAssociationProposals' not found in response. Available keys: ['connections', 'ResponseMetadata']
- Possible correct topkey values: ['connections']

**Recommended Fix:**
```python
aws_dx_hosted_connection = {
    "clfn": "directconnect",
    "descfn": "describe_connections",
    "topkey": "connections",  # CHANGED from "GatewayAssociationProposals"
    "key": "ProposalId",
    "filterid": "ProposalId"
}
```

### `aws_dx_hosted_private_virtual_interface`

- **Client:** `directconnect`
- **Method:** `describe_virtual_interfaces`
- **Current topkey:** `VirtualInterfaces`
- **Current key:** `VirtualInterfaceId`
- **Actual Response Keys:** `virtualInterfaces`, `ResponseMetadata`

**Issues:**
- topkey 'VirtualInterfaces' not found in response. Available keys: ['virtualInterfaces', 'ResponseMetadata']
- Possible correct topkey values: ['virtualInterfaces']

**Recommended Fix:**
```python
aws_dx_hosted_private_virtual_interface = {
    "clfn": "directconnect",
    "descfn": "describe_virtual_interfaces",
    "topkey": "virtualInterfaces",  # CHANGED from "VirtualInterfaces"
    "key": "VirtualInterfaceId",
    "filterid": "VirtualInterfaceId"
}
```

### `aws_dx_hosted_private_virtual_interface_accepter`

- **Client:** `directconnect`
- **Method:** `describe_virtual_interfaces`
- **Current topkey:** `VirtualInterfaces`
- **Current key:** `VirtualInterfaceId`
- **Actual Response Keys:** `virtualInterfaces`, `ResponseMetadata`

**Issues:**
- topkey 'VirtualInterfaces' not found in response. Available keys: ['virtualInterfaces', 'ResponseMetadata']
- Possible correct topkey values: ['virtualInterfaces']

**Recommended Fix:**
```python
aws_dx_hosted_private_virtual_interface_accepter = {
    "clfn": "directconnect",
    "descfn": "describe_virtual_interfaces",
    "topkey": "virtualInterfaces",  # CHANGED from "VirtualInterfaces"
    "key": "VirtualInterfaceId",
    "filterid": "VirtualInterfaceId"
}
```

### `aws_dx_hosted_public_virtual_interface`

- **Client:** `directconnect`
- **Method:** `describe_virtual_interfaces`
- **Current topkey:** `VirtualInterfaces`
- **Current key:** `VirtualInterfaceId`
- **Actual Response Keys:** `virtualInterfaces`, `ResponseMetadata`

**Issues:**
- topkey 'VirtualInterfaces' not found in response. Available keys: ['virtualInterfaces', 'ResponseMetadata']
- Possible correct topkey values: ['virtualInterfaces']

**Recommended Fix:**
```python
aws_dx_hosted_public_virtual_interface = {
    "clfn": "directconnect",
    "descfn": "describe_virtual_interfaces",
    "topkey": "virtualInterfaces",  # CHANGED from "VirtualInterfaces"
    "key": "VirtualInterfaceId",
    "filterid": "VirtualInterfaceId"
}
```

### `aws_dx_hosted_public_virtual_interface_accepter`

- **Client:** `directconnect`
- **Method:** `describe_virtual_interfaces`
- **Current topkey:** `VirtualInterfaces`
- **Current key:** `VirtualInterfaceId`
- **Actual Response Keys:** `virtualInterfaces`, `ResponseMetadata`

**Issues:**
- topkey 'VirtualInterfaces' not found in response. Available keys: ['virtualInterfaces', 'ResponseMetadata']
- Possible correct topkey values: ['virtualInterfaces']

**Recommended Fix:**
```python
aws_dx_hosted_public_virtual_interface_accepter = {
    "clfn": "directconnect",
    "descfn": "describe_virtual_interfaces",
    "topkey": "virtualInterfaces",  # CHANGED from "VirtualInterfaces"
    "key": "VirtualInterfaceId",
    "filterid": "VirtualInterfaceId"
}
```

### `aws_dx_hosted_transit_virtual_interface`

- **Client:** `directconnect`
- **Method:** `describe_virtual_interfaces`
- **Current topkey:** `VirtualInterfaces`
- **Current key:** `VirtualInterfaceId`
- **Actual Response Keys:** `virtualInterfaces`, `ResponseMetadata`

**Issues:**
- topkey 'VirtualInterfaces' not found in response. Available keys: ['virtualInterfaces', 'ResponseMetadata']
- Possible correct topkey values: ['virtualInterfaces']

**Recommended Fix:**
```python
aws_dx_hosted_transit_virtual_interface = {
    "clfn": "directconnect",
    "descfn": "describe_virtual_interfaces",
    "topkey": "virtualInterfaces",  # CHANGED from "VirtualInterfaces"
    "key": "VirtualInterfaceId",
    "filterid": "VirtualInterfaceId"
}
```

### `aws_dx_hosted_transit_virtual_interface_accepter`

- **Client:** `directconnect`
- **Method:** `describe_virtual_interfaces`
- **Current topkey:** `VirtualInterfaces`
- **Current key:** `VirtualInterfaceId`
- **Actual Response Keys:** `virtualInterfaces`, `ResponseMetadata`

**Issues:**
- topkey 'VirtualInterfaces' not found in response. Available keys: ['virtualInterfaces', 'ResponseMetadata']
- Possible correct topkey values: ['virtualInterfaces']

**Recommended Fix:**
```python
aws_dx_hosted_transit_virtual_interface_accepter = {
    "clfn": "directconnect",
    "descfn": "describe_virtual_interfaces",
    "topkey": "virtualInterfaces",  # CHANGED from "VirtualInterfaces"
    "key": "VirtualInterfaceId",
    "filterid": "VirtualInterfaceId"
}
```

### `aws_dx_macsec_key_association`

- **Client:** `directconnect`
- **Method:** `describe_connections`
- **Current topkey:** `MacsecKeyAssociations`
- **Current key:** `AssociationId`
- **Actual Response Keys:** `connections`, `ResponseMetadata`

**Issues:**
- topkey 'MacsecKeyAssociations' not found in response. Available keys: ['connections', 'ResponseMetadata']
- Possible correct topkey values: ['connections']

**Recommended Fix:**
```python
aws_dx_macsec_key_association = {
    "clfn": "directconnect",
    "descfn": "describe_connections",
    "topkey": "connections",  # CHANGED from "MacsecKeyAssociations"
    "key": "AssociationId",
    "filterid": "AssociationId"
}
```

### `aws_dx_private_virtual_interface`

- **Client:** `directconnect`
- **Method:** `describe_virtual_interfaces`
- **Current topkey:** `VirtualInterfaces`
- **Current key:** `VirtualInterfaceId`
- **Actual Response Keys:** `virtualInterfaces`, `ResponseMetadata`

**Issues:**
- topkey 'VirtualInterfaces' not found in response. Available keys: ['virtualInterfaces', 'ResponseMetadata']
- Possible correct topkey values: ['virtualInterfaces']

**Recommended Fix:**
```python
aws_dx_private_virtual_interface = {
    "clfn": "directconnect",
    "descfn": "describe_virtual_interfaces",
    "topkey": "virtualInterfaces",  # CHANGED from "VirtualInterfaces"
    "key": "VirtualInterfaceId",
    "filterid": "VirtualInterfaceId"
}
```

### `aws_dx_public_virtual_interface`

- **Client:** `directconnect`
- **Method:** `describe_virtual_interfaces`
- **Current topkey:** `VirtualInterfaces`
- **Current key:** `VirtualInterfaceId`
- **Actual Response Keys:** `virtualInterfaces`, `ResponseMetadata`

**Issues:**
- topkey 'VirtualInterfaces' not found in response. Available keys: ['virtualInterfaces', 'ResponseMetadata']
- Possible correct topkey values: ['virtualInterfaces']

**Recommended Fix:**
```python
aws_dx_public_virtual_interface = {
    "clfn": "directconnect",
    "descfn": "describe_virtual_interfaces",
    "topkey": "virtualInterfaces",  # CHANGED from "VirtualInterfaces"
    "key": "VirtualInterfaceId",
    "filterid": "VirtualInterfaceId"
}
```

### `aws_dx_transit_virtual_interface`

- **Client:** `directconnect`
- **Method:** `describe_virtual_interfaces`
- **Current topkey:** `VirtualInterfaces`
- **Current key:** `VirtualInterfaceId`
- **Actual Response Keys:** `virtualInterfaces`, `ResponseMetadata`

**Issues:**
- topkey 'VirtualInterfaces' not found in response. Available keys: ['virtualInterfaces', 'ResponseMetadata']
- Possible correct topkey values: ['virtualInterfaces']

**Recommended Fix:**
```python
aws_dx_transit_virtual_interface = {
    "clfn": "directconnect",
    "descfn": "describe_virtual_interfaces",
    "topkey": "virtualInterfaces",  # CHANGED from "VirtualInterfaces"
    "key": "VirtualInterfaceId",
    "filterid": "VirtualInterfaceId"
}
```

### `aws_ebs_snapshot_copy`

- **Client:** `ec2`
- **Method:** `describe_snapshots`
- **Current topkey:** `SnapshotCopyGrants`
- **Current key:** `SnapshotCopyGrantName`
- **Actual Response Keys:** `Snapshots`, `ResponseMetadata`

**Issues:**
- topkey 'SnapshotCopyGrants' not found in response. Available keys: ['Snapshots', 'ResponseMetadata']
- Possible correct topkey values: ['Snapshots']

**Recommended Fix:**
```python
aws_ebs_snapshot_copy = {
    "clfn": "ec2",
    "descfn": "describe_snapshots",
    "topkey": "Snapshots",  # CHANGED from "SnapshotCopyGrants"
    "key": "SnapshotCopyGrantName",
    "filterid": "SnapshotCopyGrantName"
}
```

### `aws_ebs_snapshot_import`

- **Client:** `ec2`
- **Method:** `describe_import_snapshot_tasks`
- **Current topkey:** `SnapshotTasks`
- **Current key:** `SnapshotTaskIdentifier`
- **Actual Response Keys:** `ImportSnapshotTasks`, `ResponseMetadata`

**Issues:**
- topkey 'SnapshotTasks' not found in response. Available keys: ['ImportSnapshotTasks', 'ResponseMetadata']
- Possible correct topkey values: ['ImportSnapshotTasks']

**Recommended Fix:**
```python
aws_ebs_snapshot_import = {
    "clfn": "ec2",
    "descfn": "describe_import_snapshot_tasks",
    "topkey": "ImportSnapshotTasks",  # CHANGED from "SnapshotTasks"
    "key": "SnapshotTaskIdentifier",
    "filterid": "SnapshotTaskIdentifier"
}
```

### `aws_ec2_local_gateway_route`

- **Client:** `ec2`
- **Method:** `describe_local_gateway_route_tables`
- **Current topkey:** `LocalGatewayRoutes`
- **Current key:** `LocalGatewayRouteTableId`
- **Actual Response Keys:** `LocalGatewayRouteTables`, `ResponseMetadata`

**Issues:**
- topkey 'LocalGatewayRoutes' not found in response. Available keys: ['LocalGatewayRouteTables', 'ResponseMetadata']
- Possible correct topkey values: ['LocalGatewayRouteTables']

**Recommended Fix:**
```python
aws_ec2_local_gateway_route = {
    "clfn": "ec2",
    "descfn": "describe_local_gateway_route_tables",
    "topkey": "LocalGatewayRouteTables",  # CHANGED from "LocalGatewayRoutes"
    "key": "LocalGatewayRouteTableId",
    "filterid": "LocalGatewayRouteTableId"
}
```

### `aws_elasticache_user_group_association`

- **Client:** `elasticache`
- **Method:** `describe_user_groups`
- **Current topkey:** `UserGroupMemberships`
- **Current key:** `UserGroupId`
- **Actual Response Keys:** `UserGroups`, `ResponseMetadata`

**Issues:**
- topkey 'UserGroupMemberships' not found in response. Available keys: ['UserGroups', 'ResponseMetadata']
- Possible correct topkey values: ['UserGroups']

**Recommended Fix:**
```python
aws_elasticache_user_group_association = {
    "clfn": "elasticache",
    "descfn": "describe_user_groups",
    "topkey": "UserGroups",  # CHANGED from "UserGroupMemberships"
    "key": "UserGroupId",
    "filterid": "UserGroupId"
}
```

### `aws_emr_block_public_access_configuration`

- **Client:** `emr`
- **Method:** `get_block_public_access_configuration`
- **Current topkey:** `BlockPublicAccessConfigurations`
- **Current key:** `Id`
- **Actual Response Keys:** `BlockPublicAccessConfiguration`, `BlockPublicAccessConfigurationMetadata`, `ResponseMetadata`

**Issues:**
- topkey 'BlockPublicAccessConfigurations' not found in response. Available keys: ['BlockPublicAccessConfiguration', 'BlockPublicAccessConfigurationMetadata', 'ResponseMetadata']
- Possible correct topkey values: ['BlockPublicAccessConfiguration', 'BlockPublicAccessConfigurationMetadata']

**Recommended Fix:**
```python
aws_emr_block_public_access_configuration = {
    "clfn": "emr",
    "descfn": "get_block_public_access_configuration",
    "topkey": "BlockPublicAccessConfiguration",  # CHANGED from "BlockPublicAccessConfigurations"
    "key": "Id",
    "filterid": "Id"
}
```

### `aws_emrcontainers_job_template`

- **Client:** `emr-containers`
- **Method:** `list_job_templates`
- **Current topkey:** `JobTemplates`
- **Current key:** `Id`
- **Actual Response Keys:** `ResponseMetadata`, `templates`

**Issues:**
- topkey 'JobTemplates' not found in response. Available keys: ['ResponseMetadata', 'templates']
- Possible correct topkey values: ['templates']

**Recommended Fix:**
```python
aws_emrcontainers_job_template = {
    "clfn": "emr-containers",
    "descfn": "list_job_templates",
    "topkey": "templates",  # CHANGED from "JobTemplates"
    "key": "Id",
    "filterid": "Id"
}
```

### `aws_emrcontainers_virtual_cluster`

- **Client:** `emr-containers`
- **Method:** `list_virtual_clusters`
- **Current topkey:** `VirtualClusters`
- **Current key:** `Id`
- **Actual Response Keys:** `ResponseMetadata`, `virtualClusters`

**Issues:**
- topkey 'VirtualClusters' not found in response. Available keys: ['ResponseMetadata', 'virtualClusters']
- Possible correct topkey values: ['virtualClusters']

**Recommended Fix:**
```python
aws_emrcontainers_virtual_cluster = {
    "clfn": "emr-containers",
    "descfn": "list_virtual_clusters",
    "topkey": "virtualClusters",  # CHANGED from "VirtualClusters"
    "key": "Id",
    "filterid": "Id"
}
```

### `aws_emrserverless_application`

- **Client:** `emr-serverless`
- **Method:** `list_applications`
- **Current topkey:** `Applications`
- **Current key:** `Id`
- **Actual Response Keys:** `ResponseMetadata`, `applications`

**Issues:**
- topkey 'Applications' not found in response. Available keys: ['ResponseMetadata', 'applications']
- Possible correct topkey values: ['applications']

**Recommended Fix:**
```python
aws_emrserverless_application = {
    "clfn": "emr-serverless",
    "descfn": "list_applications",
    "topkey": "applications",  # CHANGED from "Applications"
    "key": "Id",
    "filterid": "Id"
}
```

### `aws_finspace_kx_environment`

- **Client:** `finspace`
- **Method:** `list_environments`
- **Current topkey:** `Environments`
- **Current key:** `EnvironmentId`
- **Actual Response Keys:** `ResponseMetadata`, `environments`

**Issues:**
- topkey 'Environments' not found in response. Available keys: ['ResponseMetadata', 'environments']
- Possible correct topkey values: ['environments']

**Recommended Fix:**
```python
aws_finspace_kx_environment = {
    "clfn": "finspace",
    "descfn": "list_environments",
    "topkey": "environments",  # CHANGED from "Environments"
    "key": "EnvironmentId",
    "filterid": "EnvironmentId"
}
```

### `aws_fsx_data_repository_association`

- **Client:** `fsx`
- **Method:** `describe_data_repository_associations`
- **Current topkey:** `DataRepositoryAssociations`
- **Current key:** `AssociationId`
- **Actual Response Keys:** `Associations`, `ResponseMetadata`

**Issues:**
- topkey 'DataRepositoryAssociations' not found in response. Available keys: ['Associations', 'ResponseMetadata']
- Possible correct topkey values: ['Associations']

**Recommended Fix:**
```python
aws_fsx_data_repository_association = {
    "clfn": "fsx",
    "descfn": "describe_data_repository_associations",
    "topkey": "Associations",  # CHANGED from "DataRepositoryAssociations"
    "key": "AssociationId",
    "filterid": "AssociationId"
}
```

### `aws_gamelift_fleet`

- **Client:** `gamelift`
- **Method:** `list_fleets`
- **Current topkey:** `Fleets`
- **Current key:** `FleetId`
- **Actual Response Keys:** `FleetIds`, `ResponseMetadata`

**Issues:**
- topkey 'Fleets' not found in response. Available keys: ['FleetIds', 'ResponseMetadata']
- Possible correct topkey values: ['FleetIds']

**Recommended Fix:**
```python
aws_gamelift_fleet = {
    "clfn": "gamelift",
    "descfn": "list_fleets",
    "topkey": "FleetIds",  # CHANGED from "Fleets"
    "key": "FleetId",
    "filterid": "FleetId"
}
```

### `aws_glue_data_catalog_encryption_settings`

- **Client:** `glue`
- **Method:** `get_data_catalog_encryption_settings`
- **Current topkey:** `DataCatalogEncryptionSettings`
- **Current key:** `CatalogId`
- **Actual Response Keys:** `DataCatalogEncryptionSettings`, `ResponseMetadata`

**Issues:**
- key field 'CatalogId' not found in response object. Available fields: ['EncryptionAtRest', 'ConnectionPasswordEncryption']

**Recommended Fix:**
```python
aws_glue_data_catalog_encryption_settings = {
    "clfn": "glue",
    "descfn": "get_data_catalog_encryption_settings",
    "topkey": "DataCatalogEncryptionSettings",
    "key": "CatalogId",
    "filterid": "CatalogId"
}
```

### `aws_glue_dev_endpoint`

- **Client:** `glue`
- **Method:** `list_dev_endpoints`
- **Current topkey:** `DevEndpoints`
- **Current key:** `EndpointName`
- **Actual Response Keys:** `DevEndpointNames`, `NextToken`, `ResponseMetadata`

**Issues:**
- topkey 'DevEndpoints' not found in response. Available keys: ['DevEndpointNames', 'NextToken', 'ResponseMetadata']
- Possible correct topkey values: ['DevEndpointNames']

**Recommended Fix:**
```python
aws_glue_dev_endpoint = {
    "clfn": "glue",
    "descfn": "list_dev_endpoints",
    "topkey": "DevEndpointNames",  # CHANGED from "DevEndpoints"
    "key": "EndpointName",
    "filterid": "EndpointName"
}
```

### `aws_grafana_workspace_api_key`

- **Client:** `grafana`
- **Method:** `list_workspaces`
- **Current topkey:** `ApiKeys`
- **Current key:** `KeyId`
- **Actual Response Keys:** `ResponseMetadata`, `workspaces`

**Issues:**
- topkey 'ApiKeys' not found in response. Available keys: ['ResponseMetadata', 'workspaces']
- Possible correct topkey values: ['workspaces']

**Recommended Fix:**
```python
aws_grafana_workspace_api_key = {
    "clfn": "grafana",
    "descfn": "list_workspaces",
    "topkey": "workspaces",  # CHANGED from "ApiKeys"
    "key": "KeyId",
    "filterid": "KeyId"
}
```

### `aws_guardduty_invite_accepter`

- **Client:** `guardduty`
- **Method:** `list_invitations`
- **Current topkey:** `InvitationAccepters`
- **Current key:** `InvitationAccepterId`
- **Actual Response Keys:** `ResponseMetadata`, `Invitations`

**Issues:**
- topkey 'InvitationAccepters' not found in response. Available keys: ['ResponseMetadata', 'Invitations']
- Possible correct topkey values: ['Invitations']

**Recommended Fix:**
```python
aws_guardduty_invite_accepter = {
    "clfn": "guardduty",
    "descfn": "list_invitations",
    "topkey": "Invitations",  # CHANGED from "InvitationAccepters"
    "key": "InvitationAccepterId",
    "filterid": "InvitationAccepterId"
}
```

### `aws_iam_security_token_service_preferences`

- **Client:** `iam`
- **Method:** `get_account_summary`
- **Current topkey:** `AccountTokenVersion`
- **Current key:** `AccountTokenVersion`
- **Actual Response Keys:** `SummaryMap`, `ResponseMetadata`

**Issues:**
- topkey 'AccountTokenVersion' not found in response. Available keys: ['SummaryMap', 'ResponseMetadata']
- Possible correct topkey values: ['SummaryMap']

**Recommended Fix:**
```python
aws_iam_security_token_service_preferences = {
    "clfn": "iam",
    "descfn": "get_account_summary",
    "topkey": "SummaryMap",  # CHANGED from "AccountTokenVersion"
    "key": "AccountTokenVersion",
    "filterid": "AccountTokenVersion"
}
```

### `aws_inspector2_delegated_admin_account`

- **Client:** `inspector2`
- **Method:** `list_delegated_admin_accounts`
- **Current topkey:** `DelegatedAdminAccounts`
- **Current key:** `AccountId`
- **Actual Response Keys:** `ResponseMetadata`, `delegatedAdminAccounts`

**Issues:**
- topkey 'DelegatedAdminAccounts' not found in response. Available keys: ['ResponseMetadata', 'delegatedAdminAccounts']
- Possible correct topkey values: ['delegatedAdminAccounts']

**Recommended Fix:**
```python
aws_inspector2_delegated_admin_account = {
    "clfn": "inspector2",
    "descfn": "list_delegated_admin_accounts",
    "topkey": "delegatedAdminAccounts",  # CHANGED from "DelegatedAdminAccounts"
    "key": "AccountId",
    "filterid": "AccountId"
}
```

### `aws_inspector2_enabler`

- **Client:** `inspector2`
- **Method:** `batch_get_account_status`
- **Current topkey:** `Enablers`
- **Current key:** `Name`
- **Actual Response Keys:** `ResponseMetadata`, `accounts`, `failedAccounts`

**Issues:**
- topkey 'Enablers' not found in response. Available keys: ['ResponseMetadata', 'accounts', 'failedAccounts']
- Possible correct topkey values: ['accounts', 'failedAccounts']

**Recommended Fix:**
```python
aws_inspector2_enabler = {
    "clfn": "inspector2",
    "descfn": "batch_get_account_status",
    "topkey": "accounts",  # CHANGED from "Enablers"
    "key": "Name",
    "filterid": "Name"
}
```

### `aws_inspector2_member_association`

- **Client:** `inspector2`
- **Method:** `list_members`
- **Current topkey:** `MemberAssociations`
- **Current key:** `AccountId`
- **Actual Response Keys:** `ResponseMetadata`, `members`

**Issues:**
- topkey 'MemberAssociations' not found in response. Available keys: ['ResponseMetadata', 'members']
- Possible correct topkey values: ['members']

**Recommended Fix:**
```python
aws_inspector2_member_association = {
    "clfn": "inspector2",
    "descfn": "list_members",
    "topkey": "members",  # CHANGED from "MemberAssociations"
    "key": "AccountId",
    "filterid": "AccountId"
}
```

### `aws_inspector_assessment_target`

- **Client:** `inspector`
- **Method:** `list_assessment_targets`
- **Current topkey:** `AssessmentTargets`
- **Current key:** `Name`
- **Actual Response Keys:** `assessmentTargetArns`, `ResponseMetadata`

**Issues:**
- topkey 'AssessmentTargets' not found in response. Available keys: ['assessmentTargetArns', 'ResponseMetadata']
- Possible correct topkey values: ['assessmentTargetArns']

**Recommended Fix:**
```python
aws_inspector_assessment_target = {
    "clfn": "inspector",
    "descfn": "list_assessment_targets",
    "topkey": "assessmentTargetArns",  # CHANGED from "AssessmentTargets"
    "key": "Name",
    "filterid": "Name"
}
```

### `aws_inspector_assessment_template`

- **Client:** `inspector`
- **Method:** `list_assessment_templates`
- **Current topkey:** `AssessmentTemplates`
- **Current key:** `Name`
- **Actual Response Keys:** `assessmentTemplateArns`, `ResponseMetadata`

**Issues:**
- topkey 'AssessmentTemplates' not found in response. Available keys: ['assessmentTemplateArns', 'ResponseMetadata']
- Possible correct topkey values: ['assessmentTemplateArns']

**Recommended Fix:**
```python
aws_inspector_assessment_template = {
    "clfn": "inspector",
    "descfn": "list_assessment_templates",
    "topkey": "assessmentTemplateArns",  # CHANGED from "AssessmentTemplates"
    "key": "Name",
    "filterid": "Name"
}
```

### `aws_inspector_resource_group`

- **Client:** `inspector`
- **Method:** `list_assessment_targets`
- **Current topkey:** `ResourceGroups`
- **Current key:** `Name`
- **Actual Response Keys:** `assessmentTargetArns`, `ResponseMetadata`

**Issues:**
- topkey 'ResourceGroups' not found in response. Available keys: ['assessmentTargetArns', 'ResponseMetadata']
- Possible correct topkey values: ['assessmentTargetArns']

**Recommended Fix:**
```python
aws_inspector_resource_group = {
    "clfn": "inspector",
    "descfn": "list_assessment_targets",
    "topkey": "assessmentTargetArns",  # CHANGED from "ResourceGroups"
    "key": "Name",
    "filterid": "Name"
}
```

### `aws_internet_gateway_attachment`

- **Client:** `ec2`
- **Method:** `describe_internet_gateways`
- **Current topkey:** `InternetGatewayAttachments`
- **Current key:** `InternetGatewayId`
- **Actual Response Keys:** `InternetGateways`, `ResponseMetadata`

**Issues:**
- topkey 'InternetGatewayAttachments' not found in response. Available keys: ['InternetGateways', 'ResponseMetadata']
- Possible correct topkey values: ['InternetGateways']

**Recommended Fix:**
```python
aws_internet_gateway_attachment = {
    "clfn": "ec2",
    "descfn": "describe_internet_gateways",
    "topkey": "InternetGateways",  # CHANGED from "InternetGatewayAttachments"
    "key": "InternetGatewayId",
    "filterid": "InternetGatewayId"
}
```

### `aws_invoicing_invoice_unit`

- **Client:** `invoicing`
- **Method:** `list_invoice_units`
- **Current topkey:** `invoiceUnits`
- **Current key:** `invoiceUnitArn`
- **Actual Response Keys:** `InvoiceUnits`, `ResponseMetadata`

**Issues:**
- topkey 'invoiceUnits' not found in response. Available keys: ['InvoiceUnits', 'ResponseMetadata']
- Possible correct topkey values: ['InvoiceUnits']

**Recommended Fix:**
```python
aws_invoicing_invoice_unit = {
    "clfn": "invoicing",
    "descfn": "list_invoice_units",
    "topkey": "InvoiceUnits",  # CHANGED from "invoiceUnits"
    "key": "invoiceUnitArn",
    "filterid": "invoiceUnitArn"
}
```

### `aws_iot_authorizer`

- **Client:** `iot`
- **Method:** `list_authorizers`
- **Current topkey:** `Authorizers`
- **Current key:** `AuthorizerName`
- **Actual Response Keys:** `ResponseMetadata`, `authorizers`

**Issues:**
- topkey 'Authorizers' not found in response. Available keys: ['ResponseMetadata', 'authorizers']
- Possible correct topkey values: ['authorizers']

**Recommended Fix:**
```python
aws_iot_authorizer = {
    "clfn": "iot",
    "descfn": "list_authorizers",
    "topkey": "authorizers",  # CHANGED from "Authorizers"
    "key": "AuthorizerName",
    "filterid": "AuthorizerName"
}
```

### `aws_iot_billing_group`

- **Client:** `iot`
- **Method:** `list_billing_groups`
- **Current topkey:** `BillingGroups`
- **Current key:** `BillingGroupName`
- **Actual Response Keys:** `ResponseMetadata`, `billingGroups`

**Issues:**
- topkey 'BillingGroups' not found in response. Available keys: ['ResponseMetadata', 'billingGroups']
- Possible correct topkey values: ['billingGroups']

**Recommended Fix:**
```python
aws_iot_billing_group = {
    "clfn": "iot",
    "descfn": "list_billing_groups",
    "topkey": "billingGroups",  # CHANGED from "BillingGroups"
    "key": "BillingGroupName",
    "filterid": "BillingGroupName"
}
```

### `aws_iot_ca_certificate`

- **Client:** `iot`
- **Method:** `list_ca_certificates`
- **Current topkey:** `CACertificates`
- **Current key:** `Id`
- **Actual Response Keys:** `ResponseMetadata`, `certificates`

**Issues:**
- topkey 'CACertificates' not found in response. Available keys: ['ResponseMetadata', 'certificates']
- Possible correct topkey values: ['certificates']

**Recommended Fix:**
```python
aws_iot_ca_certificate = {
    "clfn": "iot",
    "descfn": "list_ca_certificates",
    "topkey": "certificates",  # CHANGED from "CACertificates"
    "key": "Id",
    "filterid": "Id"
}
```

### `aws_iot_certificate`

- **Client:** `iot`
- **Method:** `list_certificates`
- **Current topkey:** `Certificates`
- **Current key:** `CertificateId`
- **Actual Response Keys:** `ResponseMetadata`, `certificates`

**Issues:**
- topkey 'Certificates' not found in response. Available keys: ['ResponseMetadata', 'certificates']
- Possible correct topkey values: ['certificates']

**Recommended Fix:**
```python
aws_iot_certificate = {
    "clfn": "iot",
    "descfn": "list_certificates",
    "topkey": "certificates",  # CHANGED from "Certificates"
    "key": "CertificateId",
    "filterid": "CertificateId"
}
```

### `aws_iot_domain_configuration`

- **Client:** `iot`
- **Method:** `list_domain_configurations`
- **Current topkey:** `DomainConfigurations`
- **Current key:** `DomainConfigurationName`
- **Actual Response Keys:** `ResponseMetadata`, `domainConfigurations`

**Issues:**
- topkey 'DomainConfigurations' not found in response. Available keys: ['ResponseMetadata', 'domainConfigurations']
- Possible correct topkey values: ['domainConfigurations']

**Recommended Fix:**
```python
aws_iot_domain_configuration = {
    "clfn": "iot",
    "descfn": "list_domain_configurations",
    "topkey": "domainConfigurations",  # CHANGED from "DomainConfigurations"
    "key": "DomainConfigurationName",
    "filterid": "DomainConfigurationName"
}
```

### `aws_iot_event_configurations`

- **Client:** `iot`
- **Method:** `describe_event_configurations`
- **Current topkey:** `EventConfigurations`
- **Current key:** `EventConfigurationName`
- **Actual Response Keys:** `ResponseMetadata`, `eventConfigurations`

**Issues:**
- topkey 'EventConfigurations' not found in response. Available keys: ['ResponseMetadata', 'eventConfigurations']
- Possible correct topkey values: ['eventConfigurations']

**Recommended Fix:**
```python
aws_iot_event_configurations = {
    "clfn": "iot",
    "descfn": "describe_event_configurations",
    "topkey": "eventConfigurations",  # CHANGED from "EventConfigurations"
    "key": "EventConfigurationName",
    "filterid": "EventConfigurationName"
}
```

### `aws_iot_indexing_configuration`

- **Client:** `iot`
- **Method:** `get_indexing_configuration`
- **Current topkey:** `IndexingConfigurations`
- **Current key:** `IndexingConfigurationName`
- **Actual Response Keys:** `ResponseMetadata`, `thingIndexingConfiguration`, `thingGroupIndexingConfiguration`

**Issues:**
- topkey 'IndexingConfigurations' not found in response. Available keys: ['ResponseMetadata', 'thingIndexingConfiguration', 'thingGroupIndexingConfiguration']
- Possible correct topkey values: ['thingIndexingConfiguration', 'thingGroupIndexingConfiguration']

**Recommended Fix:**
```python
aws_iot_indexing_configuration = {
    "clfn": "iot",
    "descfn": "get_indexing_configuration",
    "topkey": "thingIndexingConfiguration",  # CHANGED from "IndexingConfigurations"
    "key": "IndexingConfigurationName",
    "filterid": "IndexingConfigurationName"
}
```

### `aws_iot_policy_attachment`

- **Client:** `iot`
- **Method:** `list_policies`
- **Current topkey:** `Policies`
- **Current key:** `PolicyName`
- **Actual Response Keys:** `ResponseMetadata`, `policies`

**Issues:**
- topkey 'Policies' not found in response. Available keys: ['ResponseMetadata', 'policies']
- Possible correct topkey values: ['policies']

**Recommended Fix:**
```python
aws_iot_policy_attachment = {
    "clfn": "iot",
    "descfn": "list_policies",
    "topkey": "policies",  # CHANGED from "Policies"
    "key": "PolicyName",
    "filterid": "PolicyName"
}
```

### `aws_iot_provisioning_template`

- **Client:** `iot`
- **Method:** `list_provisioning_templates`
- **Current topkey:** `ProvisioningTemplates`
- **Current key:** `TemplateName`
- **Actual Response Keys:** `ResponseMetadata`, `templates`

**Issues:**
- topkey 'ProvisioningTemplates' not found in response. Available keys: ['ResponseMetadata', 'templates']
- Possible correct topkey values: ['templates']

**Recommended Fix:**
```python
aws_iot_provisioning_template = {
    "clfn": "iot",
    "descfn": "list_provisioning_templates",
    "topkey": "templates",  # CHANGED from "ProvisioningTemplates"
    "key": "TemplateName",
    "filterid": "TemplateName"
}
```

### `aws_iot_role_alias`

- **Client:** `iot`
- **Method:** `list_role_aliases`
- **Current topkey:** `RoleAliases`
- **Current key:** `RoleAliasName`
- **Actual Response Keys:** `ResponseMetadata`, `roleAliases`

**Issues:**
- topkey 'RoleAliases' not found in response. Available keys: ['ResponseMetadata', 'roleAliases']
- Possible correct topkey values: ['roleAliases']

**Recommended Fix:**
```python
aws_iot_role_alias = {
    "clfn": "iot",
    "descfn": "list_role_aliases",
    "topkey": "roleAliases",  # CHANGED from "RoleAliases"
    "key": "RoleAliasName",
    "filterid": "RoleAliasName"
}
```

### `aws_iot_thing_group`

- **Client:** `iot`
- **Method:** `list_thing_groups`
- **Current topkey:** `ThingGroups`
- **Current key:** `ThingGroupName`
- **Actual Response Keys:** `ResponseMetadata`, `thingGroups`

**Issues:**
- topkey 'ThingGroups' not found in response. Available keys: ['ResponseMetadata', 'thingGroups']
- Possible correct topkey values: ['thingGroups']

**Recommended Fix:**
```python
aws_iot_thing_group = {
    "clfn": "iot",
    "descfn": "list_thing_groups",
    "topkey": "thingGroups",  # CHANGED from "ThingGroups"
    "key": "ThingGroupName",
    "filterid": "ThingGroupName"
}
```

### `aws_iot_thing_type`

- **Client:** `iot`
- **Method:** `list_thing_types`
- **Current topkey:** `ThingTypes`
- **Current key:** `ThingTypeName`
- **Actual Response Keys:** `ResponseMetadata`, `thingTypes`

**Issues:**
- topkey 'ThingTypes' not found in response. Available keys: ['ResponseMetadata', 'thingTypes']
- Possible correct topkey values: ['thingTypes']

**Recommended Fix:**
```python
aws_iot_thing_type = {
    "clfn": "iot",
    "descfn": "list_thing_types",
    "topkey": "thingTypes",  # CHANGED from "ThingTypes"
    "key": "ThingTypeName",
    "filterid": "ThingTypeName"
}
```

### `aws_iot_topic_rule_destination`

- **Client:** `iot`
- **Method:** `list_topic_rule_destinations`
- **Current topkey:** `destinations`
- **Current key:** `destinationName`
- **Actual Response Keys:** `ResponseMetadata`, `destinationSummaries`

**Issues:**
- topkey 'destinations' not found in response. Available keys: ['ResponseMetadata', 'destinationSummaries']
- Possible correct topkey values: ['destinationSummaries']

**Recommended Fix:**
```python
aws_iot_topic_rule_destination = {
    "clfn": "iot",
    "descfn": "list_topic_rule_destinations",
    "topkey": "destinationSummaries",  # CHANGED from "destinations"
    "key": "destinationName",
    "filterid": "destinationName"
}
```

### `aws_ivs_channel`

- **Client:** `ivs`
- **Method:** `list_channels`
- **Current topkey:** `Channels`
- **Current key:** `arn`
- **Actual Response Keys:** `ResponseMetadata`, `channels`

**Issues:**
- topkey 'Channels' not found in response. Available keys: ['ResponseMetadata', 'channels']
- Possible correct topkey values: ['channels']

**Recommended Fix:**
```python
aws_ivs_channel = {
    "clfn": "ivs",
    "descfn": "list_channels",
    "topkey": "channels",  # CHANGED from "Channels"
    "key": "arn",
    "filterid": "arn"
}
```

### `aws_ivs_playback_key_pair`

- **Client:** `ivs`
- **Method:** `list_playback_key_pairs`
- **Current topkey:** `PlaybackKeyPairs`
- **Current key:** `arn`
- **Actual Response Keys:** `ResponseMetadata`, `keyPairs`

**Issues:**
- topkey 'PlaybackKeyPairs' not found in response. Available keys: ['ResponseMetadata', 'keyPairs']
- Possible correct topkey values: ['keyPairs']

**Recommended Fix:**
```python
aws_ivs_playback_key_pair = {
    "clfn": "ivs",
    "descfn": "list_playback_key_pairs",
    "topkey": "keyPairs",  # CHANGED from "PlaybackKeyPairs"
    "key": "arn",
    "filterid": "arn"
}
```

### `aws_ivs_recording_configuration`

- **Client:** `ivs`
- **Method:** `list_recording_configurations`
- **Current topkey:** `RecordingConfigurations`
- **Current key:** `arn`
- **Actual Response Keys:** `ResponseMetadata`, `recordingConfigurations`

**Issues:**
- topkey 'RecordingConfigurations' not found in response. Available keys: ['ResponseMetadata', 'recordingConfigurations']
- Possible correct topkey values: ['recordingConfigurations']

**Recommended Fix:**
```python
aws_ivs_recording_configuration = {
    "clfn": "ivs",
    "descfn": "list_recording_configurations",
    "topkey": "recordingConfigurations",  # CHANGED from "RecordingConfigurations"
    "key": "arn",
    "filterid": "arn"
}
```

### `aws_ivschat_logging_configuration`

- **Client:** `ivschat`
- **Method:** `list_logging_configurations`
- **Current topkey:** `LoggingConfigurations`
- **Current key:** `arn`
- **Actual Response Keys:** `ResponseMetadata`, `loggingConfigurations`

**Issues:**
- topkey 'LoggingConfigurations' not found in response. Available keys: ['ResponseMetadata', 'loggingConfigurations']
- Possible correct topkey values: ['loggingConfigurations']

**Recommended Fix:**
```python
aws_ivschat_logging_configuration = {
    "clfn": "ivschat",
    "descfn": "list_logging_configurations",
    "topkey": "loggingConfigurations",  # CHANGED from "LoggingConfigurations"
    "key": "arn",
    "filterid": "arn"
}
```

### `aws_ivschat_room`

- **Client:** `ivschat`
- **Method:** `list_rooms`
- **Current topkey:** `Rooms`
- **Current key:** `arn`
- **Actual Response Keys:** `ResponseMetadata`, `rooms`

**Issues:**
- topkey 'Rooms' not found in response. Available keys: ['ResponseMetadata', 'rooms']
- Possible correct topkey values: ['rooms']

**Recommended Fix:**
```python
aws_ivschat_room = {
    "clfn": "ivschat",
    "descfn": "list_rooms",
    "topkey": "rooms",  # CHANGED from "Rooms"
    "key": "arn",
    "filterid": "arn"
}
```

### `aws_keyspaces_keyspace`

- **Client:** `keyspaces`
- **Method:** `list_keyspaces`
- **Current topkey:** `Keyspaces`
- **Current key:** `Name`
- **Actual Response Keys:** `keyspaces`, `ResponseMetadata`

**Issues:**
- topkey 'Keyspaces' not found in response. Available keys: ['keyspaces', 'ResponseMetadata']
- Possible correct topkey values: ['keyspaces']

**Recommended Fix:**
```python
aws_keyspaces_keyspace = {
    "clfn": "keyspaces",
    "descfn": "list_keyspaces",
    "topkey": "keyspaces",  # CHANGED from "Keyspaces"
    "key": "Name",
    "filterid": "Name"
}
```

### `aws_kinesis_video_stream`

- **Client:** `kinesisvideo`
- **Method:** `list_streams`
- **Current topkey:** `StreamNames`
- **Current key:** `StreamName`
- **Actual Response Keys:** `ResponseMetadata`, `StreamInfoList`

**Issues:**
- topkey 'StreamNames' not found in response. Available keys: ['ResponseMetadata', 'StreamInfoList']
- Possible correct topkey values: ['StreamInfoList']

**Recommended Fix:**
```python
aws_kinesis_video_stream = {
    "clfn": "kinesisvideo",
    "descfn": "list_streams",
    "topkey": "StreamInfoList",  # CHANGED from "StreamNames"
    "key": "StreamName",
    "filterid": "StreamName"
}
```

### `aws_lakeformation_data_lake_settings`

- **Client:** `lakeformation`
- **Method:** `get_data_lake_settings`
- **Current topkey:** `DataLakeSettings`
- **Current key:** `DataLakeSettingsId`
- **Actual Response Keys:** `ResponseMetadata`, `DataLakeSettings`

**Issues:**
- key field 'DataLakeSettingsId' not found in response object. Available fields: ['DataLakeAdmins', 'ReadOnlyAdmins', 'CreateDatabaseDefaultPermissions', 'CreateTableDefaultPermissions', 'Parameters', 'TrustedResourceOwners', 'AllowExternalDataFiltering', 'ExternalDataFilteringAllowList']

**Recommended Fix:**
```python
aws_lakeformation_data_lake_settings = {
    "clfn": "lakeformation",
    "descfn": "get_data_lake_settings",
    "topkey": "DataLakeSettings",
    "key": "DataLakeSettingsId",
    "filterid": "DataLakeSettingsId"
}
```

### `aws_lakeformation_opt_in`

- **Client:** `lakeformation`
- **Method:** `get_data_lake_settings`
- **Current topkey:** `DataLakeSettings`
- **Current key:** `DataLakeSettings`
- **Actual Response Keys:** `ResponseMetadata`, `DataLakeSettings`

**Issues:**
- key field 'DataLakeSettings' not found in response object. Available fields: ['DataLakeAdmins', 'ReadOnlyAdmins', 'CreateDatabaseDefaultPermissions', 'CreateTableDefaultPermissions', 'Parameters', 'TrustedResourceOwners', 'AllowExternalDataFiltering', 'ExternalDataFilteringAllowList']

**Recommended Fix:**
```python
aws_lakeformation_opt_in = {
    "clfn": "lakeformation",
    "descfn": "get_data_lake_settings",
    "topkey": "DataLakeSettings",
    "key": "DataLakeSettings",
    "filterid": "DataLakeSettings"
}
```

### `aws_lakeformation_permissions`

- **Client:** `lakeformation`
- **Method:** `list_permissions`
- **Current topkey:** `Permissions`
- **Current key:** `Principal`
- **Actual Response Keys:** `ResponseMetadata`, `PrincipalResourcePermissions`, `NextToken`

**Issues:**
- topkey 'Permissions' not found in response. Available keys: ['ResponseMetadata', 'PrincipalResourcePermissions', 'NextToken']
- Possible correct topkey values: ['PrincipalResourcePermissions']

**Recommended Fix:**
```python
aws_lakeformation_permissions = {
    "clfn": "lakeformation",
    "descfn": "list_permissions",
    "topkey": "PrincipalResourcePermissions",  # CHANGED from "Permissions"
    "key": "Principal",
    "filterid": "Principal"
}
```

### `aws_launch_template`

- **Client:** `ec2`
- **Method:** `describe_launch_templates`
- **Current topkey:** `LaunchTemplates`
- **Current key:** `LaunchTemplateIds`
- **Actual Response Keys:** `LaunchTemplates`, `ResponseMetadata`

**Issues:**
- key field 'LaunchTemplateIds' not found in response items. Available fields: ['LaunchTemplateId', 'LaunchTemplateName', 'CreateTime', 'CreatedBy', 'DefaultVersionNumber', 'LatestVersionNumber', 'Operator']
- Possible correct key values: ['LaunchTemplateId', 'LaunchTemplateName']

**Recommended Fix:**
```python
aws_launch_template = {
    "clfn": "ec2",
    "descfn": "describe_launch_templates",
    "topkey": "LaunchTemplates",
    "key": "LaunchTemplateIds",
    "filterid": "LaunchTemplateIds"
}
```

### `aws_lb_ssl_negotiation_policy`

- **Client:** `elbv2`
- **Method:** `describe_ssl_policies`
- **Current topkey:** `SslPolicies`
- **Current key:** `SslPolicyName`
- **Actual Response Keys:** `SslPolicies`, `ResponseMetadata`

**Issues:**
- key field 'SslPolicyName' not found in response items. Available fields: ['SslProtocols', 'Ciphers', 'Name', 'SupportedLoadBalancerTypes']
- Possible correct key values: ['Name']

**Recommended Fix:**
```python
aws_lb_ssl_negotiation_policy = {
    "clfn": "elbv2",
    "descfn": "describe_ssl_policies",
    "topkey": "SslPolicies",
    "key": "SslPolicyName",
    "filterid": "SslPolicyName"
}
```

### `aws_licensemanager_grant_accepter`

- **Client:** `license-manager`
- **Method:** `list_received_grants`
- **Current topkey:** `GrantAccepters`
- **Current key:** `GrantId`
- **Actual Response Keys:** `Grants`, `ResponseMetadata`

**Issues:**
- topkey 'GrantAccepters' not found in response. Available keys: ['Grants', 'ResponseMetadata']
- Possible correct topkey values: ['Grants']

**Recommended Fix:**
```python
aws_licensemanager_grant_accepter = {
    "clfn": "license-manager",
    "descfn": "list_received_grants",
    "topkey": "Grants",  # CHANGED from "GrantAccepters"
    "key": "GrantId",
    "filterid": "GrantId"
}
```

### `aws_lightsail_bucket_resource_access`

- **Client:** `lightsail`
- **Method:** `get_buckets`
- **Current topkey:** `Buckets`
- **Current key:** `name`
- **Actual Response Keys:** `buckets`, `ResponseMetadata`

**Issues:**
- topkey 'Buckets' not found in response. Available keys: ['buckets', 'ResponseMetadata']
- Possible correct topkey values: ['buckets']

**Recommended Fix:**
```python
aws_lightsail_bucket_resource_access = {
    "clfn": "lightsail",
    "descfn": "get_buckets",
    "topkey": "buckets",  # CHANGED from "Buckets"
    "key": "name",
    "filterid": "name"
}
```

### `aws_lightsail_disk_attachment`

- **Client:** `lightsail`
- **Method:** `get_disks`
- **Current topkey:** `DiskAttachments`
- **Current key:** `name`
- **Actual Response Keys:** `disks`, `ResponseMetadata`

**Issues:**
- topkey 'DiskAttachments' not found in response. Available keys: ['disks', 'ResponseMetadata']
- Possible correct topkey values: ['disks']

**Recommended Fix:**
```python
aws_lightsail_disk_attachment = {
    "clfn": "lightsail",
    "descfn": "get_disks",
    "topkey": "disks",  # CHANGED from "DiskAttachments"
    "key": "name",
    "filterid": "name"
}
```

### `aws_lightsail_distribution`

- **Client:** `lightsail`
- **Method:** `get_distributions`
- **Current topkey:** `Distributions`
- **Current key:** `name`
- **Actual Response Keys:** `distributions`, `ResponseMetadata`

**Issues:**
- topkey 'Distributions' not found in response. Available keys: ['distributions', 'ResponseMetadata']
- Possible correct topkey values: ['distributions']

**Recommended Fix:**
```python
aws_lightsail_distribution = {
    "clfn": "lightsail",
    "descfn": "get_distributions",
    "topkey": "distributions",  # CHANGED from "Distributions"
    "key": "name",
    "filterid": "name"
}
```

### `aws_lightsail_domain`

- **Client:** `lightsail`
- **Method:** `get_domains`
- **Current topkey:** `Domains`
- **Current key:** `name`
- **Actual Response Keys:** `domains`, `ResponseMetadata`

**Issues:**
- topkey 'Domains' not found in response. Available keys: ['domains', 'ResponseMetadata']
- Possible correct topkey values: ['domains']

**Recommended Fix:**
```python
aws_lightsail_domain = {
    "clfn": "lightsail",
    "descfn": "get_domains",
    "topkey": "domains",  # CHANGED from "Domains"
    "key": "name",
    "filterid": "name"
}
```

### `aws_lightsail_domain_entry`

- **Client:** `lightsail`
- **Method:** `get_domains`
- **Current topkey:** `DomainEntries`
- **Current key:** `name`
- **Actual Response Keys:** `domains`, `ResponseMetadata`

**Issues:**
- topkey 'DomainEntries' not found in response. Available keys: ['domains', 'ResponseMetadata']
- Possible correct topkey values: ['domains']

**Recommended Fix:**
```python
aws_lightsail_domain_entry = {
    "clfn": "lightsail",
    "descfn": "get_domains",
    "topkey": "domains",  # CHANGED from "DomainEntries"
    "key": "name",
    "filterid": "name"
}
```

### `aws_lightsail_key_pair`

- **Client:** `lightsail`
- **Method:** `get_key_pairs`
- **Current topkey:** `PortInfo`
- **Current key:** `name`
- **Actual Response Keys:** `keyPairs`, `ResponseMetadata`

**Issues:**
- topkey 'PortInfo' not found in response. Available keys: ['keyPairs', 'ResponseMetadata']
- Possible correct topkey values: ['keyPairs']

**Recommended Fix:**
```python
aws_lightsail_key_pair = {
    "clfn": "lightsail",
    "descfn": "get_key_pairs",
    "topkey": "keyPairs",  # CHANGED from "PortInfo"
    "key": "name",
    "filterid": "name"
}
```

### `aws_lightsail_lb_attachment`

- **Client:** `lightsail`
- **Method:** `get_load_balancers`
- **Current topkey:** `LoadBalancers`
- **Current key:** `name`
- **Actual Response Keys:** `loadBalancers`, `ResponseMetadata`

**Issues:**
- topkey 'LoadBalancers' not found in response. Available keys: ['loadBalancers', 'ResponseMetadata']
- Possible correct topkey values: ['loadBalancers']

**Recommended Fix:**
```python
aws_lightsail_lb_attachment = {
    "clfn": "lightsail",
    "descfn": "get_load_balancers",
    "topkey": "loadBalancers",  # CHANGED from "LoadBalancers"
    "key": "name",
    "filterid": "name"
}
```

### `aws_lightsail_lb_certificate`

- **Client:** `lightsail`
- **Method:** `get_key_pairs`
- **Current topkey:** `KeyPairs`
- **Current key:** `name`
- **Actual Response Keys:** `keyPairs`, `ResponseMetadata`

**Issues:**
- topkey 'KeyPairs' not found in response. Available keys: ['keyPairs', 'ResponseMetadata']
- Possible correct topkey values: ['keyPairs']

**Recommended Fix:**
```python
aws_lightsail_lb_certificate = {
    "clfn": "lightsail",
    "descfn": "get_key_pairs",
    "topkey": "keyPairs",  # CHANGED from "KeyPairs"
    "key": "name",
    "filterid": "name"
}
```

### `aws_lightsail_lb_https_redirection_policy`

- **Client:** `lightsail`
- **Method:** `get_key_pairs`
- **Current topkey:** `KeyPairs`
- **Current key:** `name`
- **Actual Response Keys:** `keyPairs`, `ResponseMetadata`

**Issues:**
- topkey 'KeyPairs' not found in response. Available keys: ['keyPairs', 'ResponseMetadata']
- Possible correct topkey values: ['keyPairs']

**Recommended Fix:**
```python
aws_lightsail_lb_https_redirection_policy = {
    "clfn": "lightsail",
    "descfn": "get_key_pairs",
    "topkey": "keyPairs",  # CHANGED from "KeyPairs"
    "key": "name",
    "filterid": "name"
}
```

### `aws_lightsail_lb_stickiness_policy`

- **Client:** `lightsail`
- **Method:** `get_load_balancers`
- **Current topkey:** `HttpsRedirectPolicies`
- **Current key:** `name`
- **Actual Response Keys:** `loadBalancers`, `ResponseMetadata`

**Issues:**
- topkey 'HttpsRedirectPolicies' not found in response. Available keys: ['loadBalancers', 'ResponseMetadata']
- Possible correct topkey values: ['loadBalancers']

**Recommended Fix:**
```python
aws_lightsail_lb_stickiness_policy = {
    "clfn": "lightsail",
    "descfn": "get_load_balancers",
    "topkey": "loadBalancers",  # CHANGED from "HttpsRedirectPolicies"
    "key": "name",
    "filterid": "name"
}
```

### `aws_lightsail_static_ip`

- **Client:** `lightsail`
- **Method:** `get_key_pairs`
- **Current topkey:** `KeyPairs`
- **Current key:** `name`
- **Actual Response Keys:** `keyPairs`, `ResponseMetadata`

**Issues:**
- topkey 'KeyPairs' not found in response. Available keys: ['keyPairs', 'ResponseMetadata']
- Possible correct topkey values: ['keyPairs']

**Recommended Fix:**
```python
aws_lightsail_static_ip = {
    "clfn": "lightsail",
    "descfn": "get_key_pairs",
    "topkey": "keyPairs",  # CHANGED from "KeyPairs"
    "key": "name",
    "filterid": "name"
}
```

### `aws_lightsail_static_ip_attachment`

- **Client:** `lightsail`
- **Method:** `get_static_ips`
- **Current topkey:** `StaticIps`
- **Current key:** `name`
- **Actual Response Keys:** `staticIps`, `ResponseMetadata`

**Issues:**
- topkey 'StaticIps' not found in response. Available keys: ['staticIps', 'ResponseMetadata']
- Possible correct topkey values: ['staticIps']

**Recommended Fix:**
```python
aws_lightsail_static_ip_attachment = {
    "clfn": "lightsail",
    "descfn": "get_static_ips",
    "topkey": "staticIps",  # CHANGED from "StaticIps"
    "key": "name",
    "filterid": "name"
}
```

### `aws_load_balancer_backend_server_policy`

- **Client:** `elbv2`
- **Method:** `describe_load_balancers`
- **Current topkey:** `BackendServerDescriptions`
- **Current key:** `PolicyName`
- **Actual Response Keys:** `LoadBalancers`, `ResponseMetadata`

**Issues:**
- topkey 'BackendServerDescriptions' not found in response. Available keys: ['LoadBalancers', 'ResponseMetadata']
- Possible correct topkey values: ['LoadBalancers']

**Recommended Fix:**
```python
aws_load_balancer_backend_server_policy = {
    "clfn": "elbv2",
    "descfn": "describe_load_balancers",
    "topkey": "LoadBalancers",  # CHANGED from "BackendServerDescriptions"
    "key": "PolicyName",
    "filterid": "PolicyName"
}
```

### `aws_location_geofence_collection`

- **Client:** `location`
- **Method:** `list_geofence_collections`
- **Current topkey:** `GeofenceCollections`
- **Current key:** `CollectionName`
- **Actual Response Keys:** `ResponseMetadata`, `Entries`

**Issues:**
- topkey 'GeofenceCollections' not found in response. Available keys: ['ResponseMetadata', 'Entries']
- Possible correct topkey values: ['Entries']

**Recommended Fix:**
```python
aws_location_geofence_collection = {
    "clfn": "location",
    "descfn": "list_geofence_collections",
    "topkey": "Entries",  # CHANGED from "GeofenceCollections"
    "key": "CollectionName",
    "filterid": "CollectionName"
}
```

### `aws_location_map`

- **Client:** `location`
- **Method:** `list_maps`
- **Current topkey:** `Maps`
- **Current key:** `MapName`
- **Actual Response Keys:** `ResponseMetadata`, `Entries`

**Issues:**
- topkey 'Maps' not found in response. Available keys: ['ResponseMetadata', 'Entries']
- Possible correct topkey values: ['Entries']

**Recommended Fix:**
```python
aws_location_map = {
    "clfn": "location",
    "descfn": "list_maps",
    "topkey": "Entries",  # CHANGED from "Maps"
    "key": "MapName",
    "filterid": "MapName"
}
```

### `aws_location_place_index`

- **Client:** `location`
- **Method:** `list_place_indexes`
- **Current topkey:** `PlaceIndexes`
- **Current key:** `IndexName`
- **Actual Response Keys:** `ResponseMetadata`, `Entries`

**Issues:**
- topkey 'PlaceIndexes' not found in response. Available keys: ['ResponseMetadata', 'Entries']
- Possible correct topkey values: ['Entries']

**Recommended Fix:**
```python
aws_location_place_index = {
    "clfn": "location",
    "descfn": "list_place_indexes",
    "topkey": "Entries",  # CHANGED from "PlaceIndexes"
    "key": "IndexName",
    "filterid": "IndexName"
}
```

### `aws_location_route_calculator`

- **Client:** `location`
- **Method:** `list_route_calculators`
- **Current topkey:** `RouteCalculators`
- **Current key:** `CalculatorName`
- **Actual Response Keys:** `ResponseMetadata`, `Entries`

**Issues:**
- topkey 'RouteCalculators' not found in response. Available keys: ['ResponseMetadata', 'Entries']
- Possible correct topkey values: ['Entries']

**Recommended Fix:**
```python
aws_location_route_calculator = {
    "clfn": "location",
    "descfn": "list_route_calculators",
    "topkey": "Entries",  # CHANGED from "RouteCalculators"
    "key": "CalculatorName",
    "filterid": "CalculatorName"
}
```

### `aws_location_tracker`

- **Client:** `location`
- **Method:** `list_trackers`
- **Current topkey:** `Trackers`
- **Current key:** `TrackerName`
- **Actual Response Keys:** `ResponseMetadata`, `Entries`

**Issues:**
- topkey 'Trackers' not found in response. Available keys: ['ResponseMetadata', 'Entries']
- Possible correct topkey values: ['Entries']

**Recommended Fix:**
```python
aws_location_tracker = {
    "clfn": "location",
    "descfn": "list_trackers",
    "topkey": "Entries",  # CHANGED from "Trackers"
    "key": "TrackerName",
    "filterid": "TrackerName"
}
```

### `aws_macie2_invitation_accepter`

- **Client:** `macie2`
- **Method:** `list_invitations`
- **Current topkey:** `Invitations`
- **Current key:** `AccountId`
- **Actual Response Keys:** `ResponseMetadata`, `invitations`

**Issues:**
- topkey 'Invitations' not found in response. Available keys: ['ResponseMetadata', 'invitations']
- Possible correct topkey values: ['invitations']

**Recommended Fix:**
```python
aws_macie2_invitation_accepter = {
    "clfn": "macie2",
    "descfn": "list_invitations",
    "topkey": "invitations",  # CHANGED from "Invitations"
    "key": "AccountId",
    "filterid": "AccountId"
}
```

### `aws_main_route_table_association`

- **Client:** `ec2`
- **Method:** `describe_route_tables`
- **Current topkey:** `RouteTables`
- **Current key:** `Associations[].Main`
- **Actual Response Keys:** `RouteTables`, `ResponseMetadata`

**Issues:**
- key field 'Associations[].Main' not found in response items. Available fields: ['Associations', 'PropagatingVgws', 'RouteTableId', 'Routes', 'Tags', 'VpcId', 'OwnerId']
- Possible correct key values: ['RouteTableId', 'VpcId', 'OwnerId']

**Recommended Fix:**
```python
aws_main_route_table_association = {
    "clfn": "ec2",
    "descfn": "describe_route_tables",
    "topkey": "RouteTables",
    "key": "Associations[].Main",
    "filterid": "Associations[].Main"
}
```

### `aws_media_packagev2_channel_group`

- **Client:** `mediapackagev2`
- **Method:** `list_channel_groups`
- **Current topkey:** `items`
- **Current key:** `Arn`
- **Actual Response Keys:** `ResponseMetadata`, `Items`

**Issues:**
- topkey 'items' not found in response. Available keys: ['ResponseMetadata', 'Items']
- Possible correct topkey values: ['Items']

**Recommended Fix:**
```python
aws_media_packagev2_channel_group = {
    "clfn": "mediapackagev2",
    "descfn": "list_channel_groups",
    "topkey": "Items",  # CHANGED from "items"
    "key": "Arn",
    "filterid": "Arn"
}
```

### `aws_mskconnect_connector`

- **Client:** `kafkaconnect`
- **Method:** `list_connectors`
- **Current topkey:** `Connectors`
- **Current key:** `Name`
- **Actual Response Keys:** `ResponseMetadata`, `connectors`

**Issues:**
- topkey 'Connectors' not found in response. Available keys: ['ResponseMetadata', 'connectors']
- Possible correct topkey values: ['connectors']

**Recommended Fix:**
```python
aws_mskconnect_connector = {
    "clfn": "kafkaconnect",
    "descfn": "list_connectors",
    "topkey": "connectors",  # CHANGED from "Connectors"
    "key": "Name",
    "filterid": "Name"
}
```

### `aws_mskconnect_custom_plugin`

- **Client:** `kafkaconnect`
- **Method:** `list_custom_plugins`
- **Current topkey:** `CustomPlugins`
- **Current key:** `Name`
- **Actual Response Keys:** `ResponseMetadata`, `customPlugins`

**Issues:**
- topkey 'CustomPlugins' not found in response. Available keys: ['ResponseMetadata', 'customPlugins']
- Possible correct topkey values: ['customPlugins']

**Recommended Fix:**
```python
aws_mskconnect_custom_plugin = {
    "clfn": "kafkaconnect",
    "descfn": "list_custom_plugins",
    "topkey": "customPlugins",  # CHANGED from "CustomPlugins"
    "key": "Name",
    "filterid": "Name"
}
```

### `aws_mskconnect_worker_configuration`

- **Client:** `kafkaconnect`
- **Method:** `list_worker_configurations`
- **Current topkey:** `WorkerConfigurations`
- **Current key:** `Name`
- **Actual Response Keys:** `ResponseMetadata`, `workerConfigurations`

**Issues:**
- topkey 'WorkerConfigurations' not found in response. Available keys: ['ResponseMetadata', 'workerConfigurations']
- Possible correct topkey values: ['workerConfigurations']

**Recommended Fix:**
```python
aws_mskconnect_worker_configuration = {
    "clfn": "kafkaconnect",
    "descfn": "list_worker_configurations",
    "topkey": "workerConfigurations",  # CHANGED from "WorkerConfigurations"
    "key": "Name",
    "filterid": "Name"
}
```

### `aws_neptune_event_subscription`

- **Client:** `neptune`
- **Method:** `describe_event_subscriptions`
- **Current topkey:** `EventSubscriptions`
- **Current key:** `SubscriptionName`
- **Actual Response Keys:** `EventSubscriptionsList`, `ResponseMetadata`

**Issues:**
- topkey 'EventSubscriptions' not found in response. Available keys: ['EventSubscriptionsList', 'ResponseMetadata']
- Possible correct topkey values: ['EventSubscriptionsList']

**Recommended Fix:**
```python
aws_neptune_event_subscription = {
    "clfn": "neptune",
    "descfn": "describe_event_subscriptions",
    "topkey": "EventSubscriptionsList",  # CHANGED from "EventSubscriptions"
    "key": "SubscriptionName",
    "filterid": "SubscriptionName"
}
```

### `aws_rekognition_stream_processor`

- **Client:** `rekognition`
- **Method:** `list_stream_processors`
- **Current topkey:** `StreamProcessors`
- **Current key:** `Name`
- **Actual Response Keys:** `ResponseMetadata`

**Issues:**
- topkey 'StreamProcessors' not found in response. Available keys: ['ResponseMetadata']

**Recommended Fix:**
```python
aws_rekognition_stream_processor = {
    "clfn": "rekognition",
    "descfn": "list_stream_processors",
    "topkey": "",  # CHANGED from "StreamProcessors" - no wrapper key
    "key": "Name",
    "filterid": "Name"
}
```

### `aws_rolesanywhere_profile`

- **Client:** `rolesanywhere`
- **Method:** `list_profiles`
- **Current topkey:** `Profiles`
- **Current key:** `ProfileName`
- **Actual Response Keys:** `ResponseMetadata`, `profiles`

**Issues:**
- topkey 'Profiles' not found in response. Available keys: ['ResponseMetadata', 'profiles']
- Possible correct topkey values: ['profiles']

**Recommended Fix:**
```python
aws_rolesanywhere_profile = {
    "clfn": "rolesanywhere",
    "descfn": "list_profiles",
    "topkey": "profiles",  # CHANGED from "Profiles"
    "key": "ProfileName",
    "filterid": "ProfileName"
}
```

### `aws_rolesanywhere_trust_anchor`

- **Client:** `rolesanywhere`
- **Method:** `list_trust_anchors`
- **Current topkey:** `TrustAnchors`
- **Current key:** `TrustAnchorId`
- **Actual Response Keys:** `ResponseMetadata`, `trustAnchors`

**Issues:**
- topkey 'TrustAnchors' not found in response. Available keys: ['ResponseMetadata', 'trustAnchors']
- Possible correct topkey values: ['trustAnchors']

**Recommended Fix:**
```python
aws_rolesanywhere_trust_anchor = {
    "clfn": "rolesanywhere",
    "descfn": "list_trust_anchors",
    "topkey": "trustAnchors",  # CHANGED from "TrustAnchors"
    "key": "TrustAnchorId",
    "filterid": "TrustAnchorId"
}
```

### `aws_route_table_association`

- **Client:** `ec2`
- **Method:** `describe_route_tables`
- **Current topkey:** `RouteTables`
- **Current key:** `.Associations.0.SubnetId`
- **Actual Response Keys:** `RouteTables`, `ResponseMetadata`

**Issues:**
- Complex nested key '.Associations.0.SubnetId' - manual verification needed

**Recommended Fix:**
```python
aws_route_table_association = {
    "clfn": "ec2",
    "descfn": "describe_route_tables",
    "topkey": "RouteTables",
    "key": ".Associations.0.SubnetId",
    "filterid": ".Associations.0.SubnetId"
}
```

### `aws_rum_app_monitor`

- **Client:** `rum`
- **Method:** `list_app_monitors`
- **Current topkey:** `AppMonitors`
- **Current key:** `Name`
- **Actual Response Keys:** `ResponseMetadata`, `AppMonitorSummaries`

**Issues:**
- topkey 'AppMonitors' not found in response. Available keys: ['ResponseMetadata', 'AppMonitorSummaries']
- Possible correct topkey values: ['AppMonitorSummaries']

**Recommended Fix:**
```python
aws_rum_app_monitor = {
    "clfn": "rum",
    "descfn": "list_app_monitors",
    "topkey": "AppMonitorSummaries",  # CHANGED from "AppMonitors"
    "key": "Name",
    "filterid": "Name"
}
```

### `aws_sagemaker_data_quality_job_definition`

- **Client:** `sagemaker`
- **Method:** `list_data_quality_job_definitions`
- **Current topkey:** `DataQualityJobDefinitions`
- **Current key:** `DataQualityJobDefinitionArn`
- **Actual Response Keys:** `JobDefinitionSummaries`, `ResponseMetadata`

**Issues:**
- topkey 'DataQualityJobDefinitions' not found in response. Available keys: ['JobDefinitionSummaries', 'ResponseMetadata']
- Possible correct topkey values: ['JobDefinitionSummaries']

**Recommended Fix:**
```python
aws_sagemaker_data_quality_job_definition = {
    "clfn": "sagemaker",
    "descfn": "list_data_quality_job_definitions",
    "topkey": "JobDefinitionSummaries",  # CHANGED from "DataQualityJobDefinitions"
    "key": "DataQualityJobDefinitionArn",
    "filterid": "DataQualityJobDefinitionArn"
}
```

### `aws_sagemaker_feature_group`

- **Client:** `sagemaker`
- **Method:** `list_feature_groups`
- **Current topkey:** `FeatureGroups`
- **Current key:** `FeatureGroupArn`
- **Actual Response Keys:** `FeatureGroupSummaries`, `ResponseMetadata`

**Issues:**
- topkey 'FeatureGroups' not found in response. Available keys: ['FeatureGroupSummaries', 'ResponseMetadata']
- Possible correct topkey values: ['FeatureGroupSummaries']

**Recommended Fix:**
```python
aws_sagemaker_feature_group = {
    "clfn": "sagemaker",
    "descfn": "list_feature_groups",
    "topkey": "FeatureGroupSummaries",  # CHANGED from "FeatureGroups"
    "key": "FeatureGroupArn",
    "filterid": "FeatureGroupArn"
}
```

### `aws_sagemaker_space`

- **Client:** `sagemaker`
- **Method:** `list_spaces`
- **Current topkey:** `Spaces`
- **Current key:** `Arn`
- **Actual Response Keys:** `Spaces`, `ResponseMetadata`

**Issues:**
- key field 'Arn' not found in response items. Available fields: ['DomainId', 'SpaceName', 'Status', 'CreationTime', 'LastModifiedTime', 'SpaceSettingsSummary', 'SpaceSharingSettingsSummary', 'OwnershipSettingsSummary']
- Possible correct key values: ['DomainId', 'SpaceName']

**Recommended Fix:**
```python
aws_sagemaker_space = {
    "clfn": "sagemaker",
    "descfn": "list_spaces",
    "topkey": "Spaces",
    "key": "Arn",
    "filterid": "Arn"
}
```

### `aws_sagemaker_user_profile`

- **Client:** `sagemaker`
- **Method:** `list_user_profiles`
- **Current topkey:** `UserProfiles`
- **Current key:** `UserProfileArn`
- **Actual Response Keys:** `UserProfiles`, `ResponseMetadata`

**Issues:**
- key field 'UserProfileArn' not found in response items. Available fields: ['DomainId', 'UserProfileName', 'Status', 'CreationTime', 'LastModifiedTime']
- Possible correct key values: ['DomainId', 'UserProfileName']

**Recommended Fix:**
```python
aws_sagemaker_user_profile = {
    "clfn": "sagemaker",
    "descfn": "list_user_profiles",
    "topkey": "UserProfiles",
    "key": "UserProfileArn",
    "filterid": "UserProfileArn"
}
```

### `aws_securityhub_account`

- **Client:** `securityhub`
- **Method:** `describe_hub`
- **Current topkey:** `Hub`
- **Current key:** `HubArn`
- **Actual Response Keys:** `ResponseMetadata`, `HubArn`, `SubscribedAt`, `AutoEnableControls`, `ControlFindingGenerator`

**Issues:**
- topkey 'Hub' not found in response. Available keys: ['ResponseMetadata', 'HubArn', 'SubscribedAt', 'AutoEnableControls', 'ControlFindingGenerator']

**Recommended Fix:**
```python
aws_securityhub_account = {
    "clfn": "securityhub",
    "descfn": "describe_hub",
    "topkey": "",  # CHANGED from "Hub" - no wrapper key
    "key": "HubArn",
    "filterid": "HubArn"
}
```

### `aws_servicecatalog_tag_option`

- **Client:** `servicecatalog`
- **Method:** `list_tag_options`
- **Current topkey:** `TagOptions`
- **Current key:** `Id`
- **Actual Response Keys:** `TagOptionDetails`, `ResponseMetadata`

**Issues:**
- topkey 'TagOptions' not found in response. Available keys: ['TagOptionDetails', 'ResponseMetadata']
- Possible correct topkey values: ['TagOptionDetails']

**Recommended Fix:**
```python
aws_servicecatalog_tag_option = {
    "clfn": "servicecatalog",
    "descfn": "list_tag_options",
    "topkey": "TagOptionDetails",  # CHANGED from "TagOptions"
    "key": "Id",
    "filterid": "Id"
}
```

### `aws_ses_active_receipt_rule_set`

- **Client:** `ses`
- **Method:** `describe_active_receipt_rule_set`
- **Current topkey:** `Rules`
- **Current key:** `Name`
- **Actual Response Keys:** `ResponseMetadata`

**Issues:**
- topkey 'Rules' not found in response. Available keys: ['ResponseMetadata']

**Recommended Fix:**
```python
aws_ses_active_receipt_rule_set = {
    "clfn": "ses",
    "descfn": "describe_active_receipt_rule_set",
    "topkey": "",  # CHANGED from "Rules" - no wrapper key
    "key": "Name",
    "filterid": "Name"
}
```

### `aws_sesv2_account_suppression_attributes`

- **Client:** `sesv2`
- **Method:** `get_account`
- **Current topkey:** `SuppressionAttributes`
- **Current key:** `SuppressionAttributes`
- **Actual Response Keys:** `ResponseMetadata`, `DedicatedIpAutoWarmupEnabled`, `EnforcementStatus`, `ProductionAccessEnabled`, `SendQuota`, `SendingEnabled`, `SuppressionAttributes`, `VdmAttributes`

**Issues:**
- key field 'SuppressionAttributes' not found in response object. Available fields: ['SuppressedReasons']

**Recommended Fix:**
```python
aws_sesv2_account_suppression_attributes = {
    "clfn": "sesv2",
    "descfn": "get_account",
    "topkey": "SuppressionAttributes",
    "key": "SuppressionAttributes",
    "filterid": "SuppressionAttributes"
}
```

### `aws_sesv2_account_vdm_attributes`

- **Client:** `sesv2`
- **Method:** `get_account`
- **Current topkey:** `VdmAttributes`
- **Current key:** `VdmAttributes`
- **Actual Response Keys:** `ResponseMetadata`, `DedicatedIpAutoWarmupEnabled`, `EnforcementStatus`, `ProductionAccessEnabled`, `SendQuota`, `SendingEnabled`, `SuppressionAttributes`, `VdmAttributes`

**Issues:**
- key field 'VdmAttributes' not found in response object. Available fields: ['VdmEnabled']

**Recommended Fix:**
```python
aws_sesv2_account_vdm_attributes = {
    "clfn": "sesv2",
    "descfn": "get_account",
    "topkey": "VdmAttributes",
    "key": "VdmAttributes",
    "filterid": "VdmAttributes"
}
```

### `aws_simpledb_domain`

- **Client:** `sdb`
- **Method:** `list_domains`
- **Current topkey:** `DomainNames`
- **Current key:** `DomainName`
- **Actual Response Keys:** `ResponseMetadata`

**Issues:**
- topkey 'DomainNames' not found in response. Available keys: ['ResponseMetadata']

**Recommended Fix:**
```python
aws_simpledb_domain = {
    "clfn": "sdb",
    "descfn": "list_domains",
    "topkey": "",  # CHANGED from "DomainNames" - no wrapper key
    "key": "DomainName",
    "filterid": "DomainName"
}
```

### `aws_sqs_queue`

- **Client:** `sqs`
- **Method:** `list_queues`
- **Current topkey:** `QueueUrls`
- **Current key:** ``
- **Actual Response Keys:** `ResponseMetadata`

**Issues:**
- topkey 'QueueUrls' not found in response. Available keys: ['ResponseMetadata']

**Recommended Fix:**
```python
aws_sqs_queue = {
    "clfn": "sqs",
    "descfn": "list_queues",
    "topkey": "",  # CHANGED from "QueueUrls" - no wrapper key
    "key": "",
    "filterid": ""
}
```

### `aws_ssm_default_patch_baseline`

- **Client:** `ssm`
- **Method:** `get_default_patch_baseline`
- **Current topkey:** `Baseline`
- **Current key:** `BaselineId`
- **Actual Response Keys:** `BaselineId`, `OperatingSystem`, `ResponseMetadata`

**Issues:**
- topkey 'Baseline' not found in response. Available keys: ['BaselineId', 'OperatingSystem', 'ResponseMetadata']

**Recommended Fix:**
```python
aws_ssm_default_patch_baseline = {
    "clfn": "ssm",
    "descfn": "get_default_patch_baseline",
    "topkey": "",  # CHANGED from "Baseline" - no wrapper key
    "key": "BaselineId",
    "filterid": "BaselineId"
}
```

### `aws_ssoadmin_instances`

- **Client:** `sso-admin`
- **Method:** `list_instances`
- **Current topkey:** `Instances`
- **Current key:** `Arn`
- **Actual Response Keys:** `Instances`, `ResponseMetadata`

**Issues:**
- key field 'Arn' not found in response items. Available fields: ['InstanceArn', 'IdentityStoreId', 'OwnerAccountId', 'CreatedDate', 'Status']
- Possible correct key values: ['InstanceArn', 'IdentityStoreId', 'OwnerAccountId']

**Recommended Fix:**
```python
aws_ssoadmin_instances = {
    "clfn": "sso-admin",
    "descfn": "list_instances",
    "topkey": "Instances",
    "key": "Arn",
    "filterid": "Arn"
}
```

### `aws_vpc_ipv4_cidr_block_association`

- **Client:** `ec2`
- **Method:** `describe_vpcs`
- **Current topkey:** `Vpcs`
- **Current key:** `AssociationId`
- **Actual Response Keys:** `Vpcs`, `ResponseMetadata`

**Issues:**
- key field 'AssociationId' not found in response items. Available fields: ['OwnerId', 'InstanceTenancy', 'CidrBlockAssociationSet', 'IsDefault', 'Tags', 'BlockPublicAccessStates', 'VpcId', 'State', 'CidrBlock', 'DhcpOptionsId']
- Possible correct key values: ['OwnerId', 'CidrBlockAssociationSet', 'VpcId', 'CidrBlock', 'DhcpOptionsId']

**Recommended Fix:**
```python
aws_vpc_ipv4_cidr_block_association = {
    "clfn": "ec2",
    "descfn": "describe_vpcs",
    "topkey": "Vpcs",
    "key": "AssociationId",
    "filterid": "AssociationId"
}
```

### `aws_wafregional_rate_based_rule`

- **Client:** `waf-regional`
- **Method:** `list_rate_based_rules`
- **Current topkey:** `RateBasedRules`
- **Current key:** `RuleId`
- **Actual Response Keys:** `Rules`, `ResponseMetadata`

**Issues:**
- topkey 'RateBasedRules' not found in response. Available keys: ['Rules', 'ResponseMetadata']
- Possible correct topkey values: ['Rules']

**Recommended Fix:**
```python
aws_wafregional_rate_based_rule = {
    "clfn": "waf-regional",
    "descfn": "list_rate_based_rules",
    "topkey": "Rules",  # CHANGED from "RateBasedRules"
    "key": "RuleId",
    "filterid": "RuleId"
}
```

### `aws_xray_encryption_config`

- **Client:** `xray`
- **Method:** `get_encryption_config`
- **Current topkey:** `EncryptionConfig`
- **Current key:** `EncryptionConfigId`
- **Actual Response Keys:** `ResponseMetadata`, `EncryptionConfig`

**Issues:**
- key field 'EncryptionConfigId' not found in response object. Available fields: ['Status', 'Type']

**Recommended Fix:**
```python
aws_xray_encryption_config = {
    "clfn": "xray",
    "descfn": "get_encryption_config",
    "topkey": "EncryptionConfig",
    "key": "EncryptionConfigId",
    "filterid": "EncryptionConfigId"
}
```

### `aws_xray_sampling_rule`

- **Client:** `xray`
- **Method:** `get_sampling_rules`
- **Current topkey:** `SamplingRuleRecords`
- **Current key:** `RuleName`
- **Actual Response Keys:** `ResponseMetadata`, `SamplingRuleRecords`

**Issues:**
- key field 'RuleName' not found in response items. Available fields: ['SamplingRule', 'CreatedAt', 'ModifiedAt']

**Recommended Fix:**
```python
aws_xray_sampling_rule = {
    "clfn": "xray",
    "descfn": "get_sampling_rules",
    "topkey": "SamplingRuleRecords",
    "key": "RuleName",
    "filterid": "RuleName"
}
```

## 🔒 Permission Errors

These resources require additional IAM permissions:

### `aws_auditmanager_assessment`

- **Client:** `auditmanager`
- **Method:** `list_assessments`
- **Error Code:** `AccessDeniedException`

**Error:** Permission denied: Please complete AWS Audit Manager setup from home page to enable this action in this account.

**Action Needed:**
1. Grant IAM permissions for this service
2. Required permission: `auditmanager:list_assessments`
3. Re-run verification after granting permissions
4. This is NOT an error in aws_dict.py - configuration is likely correct

### `aws_auditmanager_assessment_delegation`

- **Client:** `auditmanager`
- **Method:** `get_delegations`
- **Error Code:** `AccessDeniedException`

**Error:** Permission denied: Please complete AWS Audit Manager setup from home page to enable this action in this account.

**Action Needed:**
1. Grant IAM permissions for this service
2. Required permission: `auditmanager:get_delegations`
3. Re-run verification after granting permissions
4. This is NOT an error in aws_dict.py - configuration is likely correct

### `aws_auditmanager_assessment_report`

- **Client:** `auditmanager`
- **Method:** `list_assessment_reports`
- **Error Code:** `AccessDeniedException`

**Error:** Permission denied: Please complete AWS Audit Manager setup from home page to enable this action in this account.

**Action Needed:**
1. Grant IAM permissions for this service
2. Required permission: `auditmanager:list_assessment_reports`
3. Re-run verification after granting permissions
4. This is NOT an error in aws_dict.py - configuration is likely correct

### `aws_auditmanager_organization_admin_account_registration`

- **Client:** `auditmanager`
- **Method:** `get_organization_admin_account`
- **Error Code:** `AccessDeniedException`

**Error:** Permission denied: Please complete AWS Audit Manager setup from home page to enable this action in this account.

**Action Needed:**
1. Grant IAM permissions for this service
2. Required permission: `auditmanager:get_organization_admin_account`
3. Re-run verification after granting permissions
4. This is NOT an error in aws_dict.py - configuration is likely correct

### `aws_fms_policy`

- **Client:** `fms`
- **Method:** `list_policies`
- **Error Code:** `AccessDeniedException`

**Error:** Permission denied: No default admin could be found for account 566972129213 in Region us-east-1

**Action Needed:**
1. Grant IAM permissions for this service
2. Required permission: `fms:list_policies`
3. Re-run verification after granting permissions
4. This is NOT an error in aws_dict.py - configuration is likely correct

### `aws_fms_resource_set`

- **Client:** `fms`
- **Method:** `list_resource_sets`
- **Error Code:** `AccessDeniedException`

**Error:** Permission denied: No default admin could be found for account 566972129213 in Region us-east-1

**Action Needed:**
1. Grant IAM permissions for this service
2. Required permission: `fms:list_resource_sets`
3. Re-run verification after granting permissions
4. This is NOT an error in aws_dict.py - configuration is likely correct

### `aws_inspector2_organization_configuration`

- **Client:** `inspector2`
- **Method:** `describe_organization_configuration`
- **Error Code:** `AccessDeniedException`

**Error:** Permission denied: Invoking account does not have access to describe the organization configuration.

**Action Needed:**
1. Grant IAM permissions for this service
2. Required permission: `inspector2:describe_organization_configuration`
3. Re-run verification after granting permissions
4. This is NOT an error in aws_dict.py - configuration is likely correct

### `aws_macie2_account`

- **Client:** `macie2`
- **Method:** `get_macie_session`
- **Error Code:** `AccessDeniedException`

**Error:** Permission denied: Macie is not enabled

**Action Needed:**
1. Grant IAM permissions for this service
2. Required permission: `macie2:get_macie_session`
3. Re-run verification after granting permissions
4. This is NOT an error in aws_dict.py - configuration is likely correct

### `aws_macie2_custom_data_identifier`

- **Client:** `macie2`
- **Method:** `list_custom_data_identifiers`
- **Error Code:** `AccessDeniedException`

**Error:** Permission denied: Macie is not enabled

**Action Needed:**
1. Grant IAM permissions for this service
2. Required permission: `macie2:list_custom_data_identifiers`
3. Re-run verification after granting permissions
4. This is NOT an error in aws_dict.py - configuration is likely correct

### `aws_macie2_findings_filter`

- **Client:** `macie2`
- **Method:** `list_findings_filters`
- **Error Code:** `AccessDeniedException`

**Error:** Permission denied: Macie is not enabled.

**Action Needed:**
1. Grant IAM permissions for this service
2. Required permission: `macie2:list_findings_filters`
3. Re-run verification after granting permissions
4. This is NOT an error in aws_dict.py - configuration is likely correct

### `aws_macie2_organization_admin_account`

- **Client:** `macie2`
- **Method:** `list_members`
- **Error Code:** `AccessDeniedException`

**Error:** Permission denied: Macie is not enabled

**Action Needed:**
1. Grant IAM permissions for this service
2. Required permission: `macie2:list_members`
3. Re-run verification after granting permissions
4. This is NOT an error in aws_dict.py - configuration is likely correct

### `aws_macie2_organization_configuration`

- **Client:** `macie2`
- **Method:** `describe_organization_configuration`
- **Error Code:** `AccessDeniedException`

**Error:** Permission denied: The request failed because you must be the Macie administrator for an organization to perform this operation

**Action Needed:**
1. Grant IAM permissions for this service
2. Required permission: `macie2:describe_organization_configuration`
3. Re-run verification after granting permissions
4. This is NOT an error in aws_dict.py - configuration is likely correct

### `aws_securityhub_configuration_policy`

- **Client:** `securityhub`
- **Method:** `list_configuration_policies`
- **Error Code:** `AccessDeniedException`

**Error:** Permission denied: Must be a Security Hub delegated administrator with Central Configuration enabled

**Action Needed:**
1. Grant IAM permissions for this service
2. Required permission: `securityhub:list_configuration_policies`
3. Re-run verification after granting permissions
4. This is NOT an error in aws_dict.py - configuration is likely correct

### `aws_securityhub_configuration_policy_association`

- **Client:** `securityhub`
- **Method:** `list_configuration_policy_associations`
- **Error Code:** `AccessDeniedException`

**Error:** Permission denied: Must be a Security Hub delegated administrator with Central Configuration enabled

**Action Needed:**
1. Grant IAM permissions for this service
2. Required permission: `securityhub:list_configuration_policy_associations`
3. Re-run verification after granting permissions
4. This is NOT an error in aws_dict.py - configuration is likely correct

### `aws_securitylake_aws_log_source`

- **Client:** `securitylake`
- **Method:** `list_log_sources`
- **Error Code:** `AccessDeniedException`

**Error:** Permission denied: The request failed because your account is not authorized to perform this operation.

**Action Needed:**
1. Grant IAM permissions for this service
2. Required permission: `securitylake:list_log_sources`
3. Re-run verification after granting permissions
4. This is NOT an error in aws_dict.py - configuration is likely correct

### `aws_securitylake_custom_log_source`

- **Client:** `securitylake`
- **Method:** `list_log_sources`
- **Error Code:** `AccessDeniedException`

**Error:** Permission denied: The request failed because your account is not authorized to perform this operation.

**Action Needed:**
1. Grant IAM permissions for this service
2. Required permission: `securitylake:list_log_sources`
3. Re-run verification after granting permissions
4. This is NOT an error in aws_dict.py - configuration is likely correct

### `aws_securitylake_subscriber`

- **Client:** `securitylake`
- **Method:** `list_subscribers`
- **Error Code:** `AccessDeniedException`

**Error:** Permission denied: The request failed because your account is not authorized to perform this operation.

**Action Needed:**
1. Grant IAM permissions for this service
2. Required permission: `securitylake:list_subscribers`
3. Re-run verification after granting permissions
4. This is NOT an error in aws_dict.py - configuration is likely correct

### `aws_timestreamquery_scheduled_query`

- **Client:** `timestream-query`
- **Method:** `list_scheduled_queries`
- **Error Code:** `AccessDeniedException`

**Error:** Permission denied: Only existing Timestream for LiveAnalytics customers can access the service. Reach out to AWS support, for more information.

**Action Needed:**
1. Grant IAM permissions for this service
2. Required permission: `timestream-query:list_scheduled_queries`
3. Re-run verification after granting permissions
4. This is NOT an error in aws_dict.py - configuration is likely correct

### `aws_timestreamwrite_database`

- **Client:** `timestream-write`
- **Method:** `list_databases`
- **Error Code:** `AccessDeniedException`

**Error:** Permission denied: Only existing Timestream for LiveAnalytics customers can access the service. Reach out to AWS support, for more information.

**Action Needed:**
1. Grant IAM permissions for this service
2. Required permission: `timestream-write:list_databases`
3. Re-run verification after granting permissions
4. This is NOT an error in aws_dict.py - configuration is likely correct

### `aws_timestreamwrite_table`

- **Client:** `timestream-write`
- **Method:** `list_tables`
- **Error Code:** `AccessDeniedException`

**Error:** Permission denied: Only existing Timestream for LiveAnalytics customers can access the service. Reach out to AWS support, for more information.

**Action Needed:**
1. Grant IAM permissions for this service
2. Required permission: `timestream-write:list_tables`
3. Re-run verification after granting permissions
4. This is NOT an error in aws_dict.py - configuration is likely correct

## 🔴 API Errors

These resources encountered API errors:

### `aws_accessanalyzer_archive_rule`

- **Client:** `accessanalyzer`
- **Method:** `list_archive_rules`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "analyzerName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_account_alternate_contact`

- **Client:** `organizations`
- **Method:** `describe_account`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AccountId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_account_primary_contact`

- **Client:** `organizations`
- **Method:** `describe_account`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AccountId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_acmpca_certificate`

- **Client:** `acm-pca`
- **Method:** `get_certificate`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "CertificateAuthorityArn"
Missing required parameter in input: "CertificateArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_acmpca_permission`

- **Client:** `acm-pca`
- **Method:** `list_permissions`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "CertificateAuthorityArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_acmpca_policy`

- **Client:** `acm-pca`
- **Method:** `get_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ResourceArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ami_launch_permission`

- **Client:** `ec2`
- **Method:** `describe_image_attribute`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Attribute"
Missing required parameter in input: "ImageId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_amplify_backend_environment`

- **Client:** `amplify`
- **Method:** `list_backend_environments`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "appId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_amplify_branch`

- **Client:** `amplify`
- **Method:** `list_branches`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "appId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_amplify_domain_association`

- **Client:** `amplify`
- **Method:** `list_domain_associations`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "appId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_amplify_webhook`

- **Client:** `amplify`
- **Method:** `list_webhooks`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "appId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_api_gateway_authorizer`

- **Client:** `apigateway`
- **Method:** `get_authorizers`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "restApiId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_api_gateway_base_path_mapping`

- **Client:** `apigateway`
- **Method:** `get_base_path_mappings`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "domainName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_api_gateway_deployment`

- **Client:** `apigateway`
- **Method:** `get_deployments`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "restApiId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_api_gateway_documentation_part`

- **Client:** `apigateway`
- **Method:** `get_documentation_parts`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "restApiId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_api_gateway_documentation_version`

- **Client:** `apigateway`
- **Method:** `get_documentation_versions`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "restApiId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_api_gateway_gateway_response`

- **Client:** `apigateway`
- **Method:** `get_gateway_responses`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "restApiId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_api_gateway_integration`

- **Client:** `apigateway`
- **Method:** `get_integration`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "restApiId"
Missing required parameter in input: "resourceId"
Missing required parameter in input: "httpMethod"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_api_gateway_integration_response`

- **Client:** `apigateway`
- **Method:** `get_integration_response`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "restApiId"
Missing required parameter in input: "resourceId"
Missing required parameter in input: "httpMethod"
Missing required parameter in input: "statusCode"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_api_gateway_method`

- **Client:** `apigateway`
- **Method:** `get_method`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "restApiId"
Missing required parameter in input: "resourceId"
Missing required parameter in input: "httpMethod"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_api_gateway_method_response`

- **Client:** `apigateway`
- **Method:** `get_method_response`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "restApiId"
Missing required parameter in input: "resourceId"
Missing required parameter in input: "httpMethod"
Missing required parameter in input: "statusCode"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_api_gateway_method_settings`

- **Client:** `apigateway`
- **Method:** `get_stage`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "restApiId"
Missing required parameter in input: "stageName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_api_gateway_model`

- **Client:** `apigateway`
- **Method:** `get_models`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "restApiId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_api_gateway_request_validator`

- **Client:** `apigateway`
- **Method:** `get_request_validators`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "restApiId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_api_gateway_resource`

- **Client:** `apigateway`
- **Method:** `get_resources`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "restApiId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_api_gateway_rest_api_policy`

- **Client:** `apigateway`
- **Method:** `get_rest_api`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "restApiId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_api_gateway_stage`

- **Client:** `apigateway`
- **Method:** `get_stages`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "restApiId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_api_gateway_usage_plan_key`

- **Client:** `apigateway`
- **Method:** `get_usage_plan_keys`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "usagePlanId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_apigatewayv2_api_mapping`

- **Client:** `apigatewayv2`
- **Method:** `get_api_mappings`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DomainName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_apigatewayv2_authorizer`

- **Client:** `apigatewayv2`
- **Method:** `get_authorizers`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ApiId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_apigatewayv2_deployment`

- **Client:** `apigatewayv2`
- **Method:** `get_deployments`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ApiId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_apigatewayv2_integration`

- **Client:** `apigatewayv2`
- **Method:** `get_integrations`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ApiId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_apigatewayv2_integration_response`

- **Client:** `apigatewayv2`
- **Method:** `get_integration_responses`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "IntegrationId"
Missing required parameter in input: "ApiId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_apigatewayv2_model`

- **Client:** `apigatewayv2`
- **Method:** `get_models`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ApiId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_apigatewayv2_route`

- **Client:** `apigatewayv2`
- **Method:** `get_routes`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ApiId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_apigatewayv2_route_response`

- **Client:** `apigatewayv2`
- **Method:** `get_route_responses`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "RouteId"
Missing required parameter in input: "ApiId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_apigatewayv2_stage`

- **Client:** `apigatewayv2`
- **Method:** `get_stages`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ApiId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_appautoscaling_policy`

- **Client:** `application-autoscaling`
- **Method:** `describe_scaling_policies`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ServiceNamespace"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_appautoscaling_scheduled_action`

- **Client:** `application-autoscaling`
- **Method:** `describe_scheduled_actions`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ServiceNamespace"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_appautoscaling_target`

- **Client:** `application-autoscaling`
- **Method:** `describe_scalable_targets`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ServiceNamespace"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_appconfig_configuration_profile`

- **Client:** `appconfig`
- **Method:** `list_configuration_profiles`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ApplicationId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_appconfig_deployment`

- **Client:** `appconfig`
- **Method:** `list_deployments`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ApplicationId"
Missing required parameter in input: "EnvironmentId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_appconfig_environment`

- **Client:** `appconfig`
- **Method:** `list_environments`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ApplicationId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_appconfig_hosted_configuration_version`

- **Client:** `appconfig`
- **Method:** `list_hosted_configuration_versions`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ApplicationId"
Missing required parameter in input: "ConfigurationProfileId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_appfabric_app_authorization`

- **Client:** `appfabric`
- **Method:** `list_app_authorizations`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "appBundleIdentifier"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_appfabric_app_authorization_connection`

- **Client:** `appfabric`
- **Method:** `list_app_authorizations`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "appBundleIdentifier"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_appfabric_ingestion`

- **Client:** `appfabric`
- **Method:** `list_ingestions`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "appBundleIdentifier"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_appfabric_ingestion_destination`

- **Client:** `appfabric`
- **Method:** `list_ingestion_destinations`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "appBundleIdentifier"
Missing required parameter in input: "ingestionIdentifier"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_appmesh_gateway_route`

- **Client:** `appmesh`
- **Method:** `list_gateway_routes`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "meshName"
Missing required parameter in input: "virtualGatewayName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_appmesh_route`

- **Client:** `appmesh`
- **Method:** `list_routes`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "meshName"
Missing required parameter in input: "virtualRouterName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_appmesh_virtual_gateway`

- **Client:** `appmesh`
- **Method:** `list_virtual_gateways`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "meshName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_appmesh_virtual_node`

- **Client:** `appmesh`
- **Method:** `list_virtual_nodes`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "meshName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_appmesh_virtual_router`

- **Client:** `appmesh`
- **Method:** `list_virtual_routers`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "meshName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_appmesh_virtual_service`

- **Client:** `appmesh`
- **Method:** `list_virtual_services`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "meshName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_apprunner_auto_scaling_configuration_version`

- **Client:** `apprunner`
- **Method:** `describe_auto_scaling_configuration`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AutoScalingConfigurationArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_apprunner_custom_domain_association`

- **Client:** `apprunner`
- **Method:** `describe_custom_domains`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ServiceArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_apprunner_default_auto_scaling_configuration_version`

- **Client:** `apprunner`
- **Method:** `describe_auto_scaling_configuration`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AutoScalingConfigurationArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_apprunner_deployment`

- **Client:** `apprunner`
- **Method:** `list_operations`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ServiceArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_appstream_user`

- **Client:** `appstream`
- **Method:** `describe_users`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AuthenticationType"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_appstream_user_stack_association`

- **Client:** `appstream`
- **Method:** `describe_user_stack_associations`
- **Error Code:** `InvalidParameterCombinationException`
- **Error Type:** `api_error`

**Error:** API error (InvalidParameterCombinationException): At least one of user name or stack name must be provided

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_appsync_api_cache`

- **Client:** `appsync`
- **Method:** `get_api_cache`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "apiId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_appsync_api_key`

- **Client:** `appsync`
- **Method:** `list_api_keys`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "apiId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_appsync_channel_namespace`

- **Client:** `appsync`
- **Method:** `list_channel_namespaces`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "apiId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_appsync_datasource`

- **Client:** `appsync`
- **Method:** `list_data_sources`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "apiId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_appsync_domain_name_api_association`

- **Client:** `appsync`
- **Method:** `get_domain_name`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "domainName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_appsync_function`

- **Client:** `appsync`
- **Method:** `list_functions`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "apiId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_appsync_resolver`

- **Client:** `appsync`
- **Method:** `list_resolvers`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "apiId"
Missing required parameter in input: "typeName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_appsync_source_api_association`

- **Client:** `appsync`
- **Method:** `list_source_api_associations`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "apiId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_appsync_type`

- **Client:** `appsync`
- **Method:** `list_types`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "apiId"
Missing required parameter in input: "format"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_athena_database`

- **Client:** `athena`
- **Method:** `list_databases`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "CatalogName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_athena_prepared_statement`

- **Client:** `athena`
- **Method:** `list_prepared_statements`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "WorkGroup"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_athena_workgroup`

- **Client:** `athena`
- **Method:** `get_work_group`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "WorkGroup"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_auditmanager_control`

- **Client:** `auditmanager`
- **Method:** `list_controls`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "controlType"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_auditmanager_framework`

- **Client:** `auditmanager`
- **Method:** `list_assessment_frameworks`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "frameworkType"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_auditmanager_framework_share`

- **Client:** `auditmanager`
- **Method:** `list_assessment_framework_share_requests`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "requestType"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_autoscaling_lifecycle_hook`

- **Client:** `autoscaling`
- **Method:** `describe_lifecycle_hooks`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AutoScalingGroupName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_autoscaling_traffic_source_attachment`

- **Client:** `autoscaling`
- **Method:** `describe_traffic_sources`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AutoScalingGroupName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_backup_restore_testing_selection`

- **Client:** `backup`
- **Method:** `list_restore_testing_selections`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "RestoreTestingPlanName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_backup_selection`

- **Client:** `backup`
- **Method:** `list_backup_selections`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "BackupPlanId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_backup_vault_lock_configuration`

- **Client:** `backup`
- **Method:** `describe_backup_vault`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "BackupVaultName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_backup_vault_notifications`

- **Client:** `backup`
- **Method:** `get_backup_vault_notifications`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "BackupVaultName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_backup_vault_policy`

- **Client:** `backup`
- **Method:** `get_backup_vault_access_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "BackupVaultName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_bedrockagent_agent_action_group`

- **Client:** `bedrock-agent`
- **Method:** `list_agent_action_groups`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "agentId"
Missing required parameter in input: "agentVersion"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_bedrockagent_agent_alias`

- **Client:** `bedrock-agent`
- **Method:** `list_agent_aliases`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "agentId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_bedrockagent_agent_collaborator`

- **Client:** `bedrock-agent`
- **Method:** `list_agent_collaborators`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "agentId"
Missing required parameter in input: "agentVersion"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_bedrockagent_agent_knowledge_base_association`

- **Client:** `bedrock-agent`
- **Method:** `list_agent_knowledge_bases`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "agentId"
Missing required parameter in input: "agentVersion"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_bedrockagent_data_source`

- **Client:** `bedrock-agent`
- **Method:** `list_data_sources`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "knowledgeBaseId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_bedrockagentcore_agent_runtime_endpoint`

- **Client:** `bedrock-agentcore-control`
- **Method:** `list_agent_runtime_endpoints`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "agentRuntimeId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_bedrockagentcore_gateway_target`

- **Client:** `bedrock-agentcore-control`
- **Method:** `list_gateway_targets`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "gatewayIdentifier"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_budgets_budget`

- **Client:** `budgets`
- **Method:** `describe_budgets`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AccountId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_budgets_budget_action`

- **Client:** `budgets`
- **Method:** `describe_budget_actions_for_budget`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AccountId"
Missing required parameter in input: "BudgetName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_chatbot_slack_channel_configuration`

- **Client:** `chatbot`
- **Method:** `describe_slack_channel_configurations`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Could not connect to the endpoint URL: "https://chatbot.us-east-1.amazonaws.com/describe-slack-channel-configurations"

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_chatbot_teams_channel_configuration`

- **Client:** `chatbot`
- **Method:** `list_microsoft_teams_channel_configurations`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Could not connect to the endpoint URL: "https://chatbot.us-east-1.amazonaws.com/list-ms-teams-channel-configurations"

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_chime_voice_connector_logging`

- **Client:** `chime-sdk-voice`
- **Method:** `get_voice_connector_logging_configuration`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "VoiceConnectorId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_chime_voice_connector_origination`

- **Client:** `chime-sdk-voice`
- **Method:** `get_voice_connector_origination`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "VoiceConnectorId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_chime_voice_connector_streaming`

- **Client:** `chime-sdk-voice`
- **Method:** `get_voice_connector_streaming_configuration`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "VoiceConnectorId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_chime_voice_connector_termination`

- **Client:** `chime-sdk-voice`
- **Method:** `get_voice_connector_termination`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "VoiceConnectorId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_chime_voice_connector_termination_credentials`

- **Client:** `chime-sdk-voice`
- **Method:** `list_voice_connector_termination_credentials`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "VoiceConnectorId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cloudcontrolapi_resource`

- **Client:** `cloudcontrol`
- **Method:** `list_resources`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "TypeName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cloudformation_stack_instances`

- **Client:** `cloudformation`
- **Method:** `list_stack_instances`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "StackSetName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cloudformation_stack_set_instance`

- **Client:** `cloudformation`
- **Method:** `list_stack_instances`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "StackSetName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cloudfront_monitoring_subscription`

- **Client:** `cloudfront`
- **Method:** `get_monitoring_subscription`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DistributionId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cloudfrontkeyvaluestore_key`

- **Client:** `cloudfront-keyvaluestore`
- **Method:** `list_keys`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: KVS ARN must be provided to use this service

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_cloudfrontkeyvaluestore_keys_exclusive`

- **Client:** `cloudfront-keyvaluestore`
- **Method:** `list_keys`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: KVS ARN must be provided to use this service

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_cloudsearch_domain`

- **Client:** `cloudsearch`
- **Method:** `describe_domains`
- **Error Code:** `NotAuthorized`
- **Error Type:** `api_error`

**Error:** API error (NotAuthorized): New domain creation not supported on this account. Please reach out to AWS Support for assistance.

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_cloudsearch_domain_service_access_policy`

- **Client:** `cloudsearch`
- **Method:** `describe_service_access_policies`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DomainName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cloudwatch_event_target`

- **Client:** `events`
- **Method:** `list_targets_by_rule`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Rule"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cloudwatch_log_account_policy`

- **Client:** `logs`
- **Method:** `describe_account_policies`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "policyType"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cloudwatch_log_data_protection_policy`

- **Client:** `logs`
- **Method:** `get_data_protection_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "logGroupIdentifier"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cloudwatch_log_delivery_destination_policy`

- **Client:** `logs`
- **Method:** `get_delivery_destination_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "deliveryDestinationName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cloudwatch_log_index_policy`

- **Client:** `logs`
- **Method:** `describe_index_policies`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "logGroupIdentifiers"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cloudwatch_log_stream`

- **Client:** `logs`
- **Method:** `describe_log_streams`
- **Error Code:** `ValidationException`
- **Error Type:** `invalid_parameters`

**Error:** Invalid parameters: Either LogGroupName or LogGroupArn must be provided.

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_cloudwatch_log_subscription_filter`

- **Client:** `logs`
- **Method:** `describe_subscription_filters`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "logGroupName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cloudwatch_log_transformer`

- **Client:** `logs`
- **Method:** `get_transformer`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "logGroupIdentifier"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_codeartifact_domain_permissions_policy`

- **Client:** `codeartifact`
- **Method:** `get_domain_permissions_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "domain"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_codeartifact_repository_permissions_policy`

- **Client:** `codeartifact`
- **Method:** `get_repository_permissions_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "domain"
Missing required parameter in input: "repository"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_codebuild_resource_policy`

- **Client:** `codebuild`
- **Method:** `get_resource_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "resourceArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_codebuild_webhook`

- **Client:** `codebuild`
- **Method:** `batch_get_projects`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "names"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_codecatalyst_dev_environment`

- **Client:** `codecatalyst`
- **Method:** `list_dev_environments`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "spaceName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_codecatalyst_project`

- **Client:** `codecatalyst`
- **Method:** `list_projects`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "spaceName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_codecatalyst_source_repository`

- **Client:** `codecatalyst`
- **Method:** `list_source_repositories`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "spaceName"
Missing required parameter in input: "projectName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_codecommit_approval_rule_template_association`

- **Client:** `codecommit`
- **Method:** `list_associated_approval_rule_templates_for_repository`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "repositoryName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_codecommit_trigger`

- **Client:** `codecommit`
- **Method:** `get_repository_triggers`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "repositoryName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_codedeploy_deployment_group`

- **Client:** `codedeploy`
- **Method:** `list_deployment_groups`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "applicationName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cognito_identity_pool`

- **Client:** `cognito-identity`
- **Method:** `list_identity_pools`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "MaxResults"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cognito_identity_pool_provider_principal_tag`

- **Client:** `cognito-identity`
- **Method:** `get_principal_tag_attribute_map`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "IdentityPoolId"
Missing required parameter in input: "IdentityProviderName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cognito_identity_pool_roles_attachment`

- **Client:** `cognito-identity`
- **Method:** `get_identity_pool_roles`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "IdentityPoolId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cognito_identity_provider`

- **Client:** `cognito-idp`
- **Method:** `list_identity_providers`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "UserPoolId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cognito_log_delivery_configuration`

- **Client:** `cognito-idp`
- **Method:** `get_log_delivery_configuration`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "UserPoolId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cognito_managed_login_branding`

- **Client:** `cognito-idp`
- **Method:** `describe_managed_login_branding`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "UserPoolId"
Missing required parameter in input: "ManagedLoginBrandingId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cognito_managed_user_pool_client`

- **Client:** `cognito-idp`
- **Method:** `list_user_pool_clients`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "UserPoolId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cognito_resource_server`

- **Client:** `cognito-idp`
- **Method:** `list_resource_servers`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "UserPoolId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cognito_risk_configuration`

- **Client:** `cognito-idp`
- **Method:** `describe_risk_configuration`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "UserPoolId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cognito_user`

- **Client:** `cognito-idp`
- **Method:** `list_users`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "UserPoolId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cognito_user_group`

- **Client:** `cognito-idp`
- **Method:** `list_groups`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "UserPoolId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cognito_user_in_group`

- **Client:** `cognito-idp`
- **Method:** `list_users_in_group`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "UserPoolId"
Missing required parameter in input: "GroupName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cognito_user_pool`

- **Client:** `cognito-idp`
- **Method:** `list_user_pools`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "MaxResults"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cognito_user_pool_client`

- **Client:** `cognito-idp`
- **Method:** `list_user_pool_clients`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "UserPoolId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cognito_user_pool_domain`

- **Client:** `cognito-idp`
- **Method:** `describe_user_pool_domain`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Domain"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_cognito_user_pool_ui_customization`

- **Client:** `cognito-idp`
- **Method:** `get_ui_customization`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "UserPoolId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_computeoptimizer_recommendation_preferences`

- **Client:** `compute-optimizer`
- **Method:** `get_recommendation_preferences`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "resourceType"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_config_remediation_configuration`

- **Client:** `config`
- **Method:** `describe_remediation_configurations`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ConfigRuleNames"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_connect_bot_association`

- **Client:** `connect`
- **Method:** `list_bots`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "InstanceId"
Missing required parameter in input: "LexVersion"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_connect_contact_flow`

- **Client:** `connect`
- **Method:** `list_contact_flows`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "InstanceId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_connect_contact_flow_module`

- **Client:** `connect`
- **Method:** `list_contact_flow_modules`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "InstanceId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_connect_hours_of_operation`

- **Client:** `connect`
- **Method:** `list_hours_of_operations`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "InstanceId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_connect_instance_storage_config`

- **Client:** `connect`
- **Method:** `list_instance_storage_configs`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "InstanceId"
Missing required parameter in input: "ResourceType"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_connect_lambda_function_association`

- **Client:** `connect`
- **Method:** `list_lambda_functions`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "InstanceId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_connect_phone_number`

- **Client:** `connect`
- **Method:** `list_phone_numbers`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "InstanceId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_connect_queue`

- **Client:** `connect`
- **Method:** `list_queues`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "InstanceId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_connect_quick_connect`

- **Client:** `connect`
- **Method:** `list_quick_connects`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "InstanceId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_connect_routing_profile`

- **Client:** `connect`
- **Method:** `list_routing_profiles`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "InstanceId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_connect_security_profile`

- **Client:** `connect`
- **Method:** `list_security_profiles`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "InstanceId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_connect_user`

- **Client:** `connect`
- **Method:** `list_users`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "InstanceId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_connect_user_hierarchy_group`

- **Client:** `connect`
- **Method:** `list_user_hierarchy_groups`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "InstanceId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_connect_user_hierarchy_structure`

- **Client:** `connect`
- **Method:** `describe_user_hierarchy_structure`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "InstanceId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_connect_vocabulary`

- **Client:** `connect`
- **Method:** `search_vocabularies`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "InstanceId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_controltower_baseline`

- **Client:** `controltower`
- **Method:** `list_enabled_baselines`
- **Error Code:** `ValidationException`
- **Error Type:** `invalid_parameters`

**Error:** Invalid parameters: AWS Control Tower could not complete the operation because it could not assume the 'AWSControlTowerAdmin' role. Check the configuration for this role and try again.

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_controltower_control`

- **Client:** `controltower`
- **Method:** `list_enabled_controls`
- **Error Code:** `ResourceNotFoundException`
- **Error Type:** `api_error`

**Error:** API error (ResourceNotFoundException): AWS Control Tower cannot complete the operation, because you must create a landing zone first. To continue, create your landing zone from the console, or call the CreateLandingZone API.

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_customerprofiles_profile`

- **Client:** `customer-profiles`
- **Method:** `search_profiles`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DomainName"
Missing required parameter in input: "KeyName"
Missing required parameter in input: "Values"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_dataexchange_revision`

- **Client:** `dataexchange`
- **Method:** `list_data_set_revisions`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DataSetId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_dataexchange_revision_assets`

- **Client:** `dataexchange`
- **Method:** `list_revision_assets`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DataSetId"
Missing required parameter in input: "RevisionId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_datapipeline_pipeline_definition`

- **Client:** `datapipeline`
- **Method:** `get_pipeline_definition`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "pipelineId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_datazone_asset_type`

- **Client:** `datazone`
- **Method:** `search_types`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "domainIdentifier"
Missing required parameter in input: "managed"
Missing required parameter in input: "searchScope"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_datazone_environment`

- **Client:** `datazone`
- **Method:** `list_environments`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "domainIdentifier"
Missing required parameter in input: "projectIdentifier"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_datazone_environment_blueprint_configuration`

- **Client:** `datazone`
- **Method:** `list_environment_blueprint_configurations`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "domainIdentifier"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_datazone_environment_profile`

- **Client:** `datazone`
- **Method:** `list_environment_profiles`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "domainIdentifier"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_datazone_form_type`

- **Client:** `datazone`
- **Method:** `search_types`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "domainIdentifier"
Missing required parameter in input: "managed"
Missing required parameter in input: "searchScope"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_datazone_glossary`

- **Client:** `datazone`
- **Method:** `search`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "domainIdentifier"
Missing required parameter in input: "searchScope"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_datazone_glossary_term`

- **Client:** `datazone`
- **Method:** `search`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "domainIdentifier"
Missing required parameter in input: "searchScope"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_datazone_project`

- **Client:** `datazone`
- **Method:** `list_projects`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "domainIdentifier"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_datazone_user_profile`

- **Client:** `datazone`
- **Method:** `search_user_profiles`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "domainIdentifier"
Missing required parameter in input: "userType"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_db_proxy_default_target_group`

- **Client:** `rds`
- **Method:** `describe_db_proxy_target_groups`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DBProxyName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_db_proxy_target`

- **Client:** `rds`
- **Method:** `describe_db_proxy_targets`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DBProxyName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_db_snapshot_copy`

- **Client:** `rds`
- **Method:** `describe_db_snapshot_attributes`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DBSnapshotIdentifier"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_detective_member`

- **Client:** `detective`
- **Method:** `list_members`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "GraphArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_detective_organization_configuration`

- **Client:** `detective`
- **Method:** `describe_organization_configuration`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "GraphArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_devicefarm_device_pool`

- **Client:** `devicefarm`
- **Method:** `list_device_pools`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "arn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_devicefarm_instance_profile`

- **Client:** `devicefarm`
- **Method:** `list_instance_profiles`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Could not connect to the endpoint URL: "https://devicefarm.us-east-1.amazonaws.com/"

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_devicefarm_network_profile`

- **Client:** `devicefarm`
- **Method:** `list_network_profiles`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "arn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_devicefarm_project`

- **Client:** `devicefarm`
- **Method:** `list_projects`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Could not connect to the endpoint URL: "https://devicefarm.us-east-1.amazonaws.com/"

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_devicefarm_test_grid_project`

- **Client:** `devicefarm`
- **Method:** `list_test_grid_projects`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Could not connect to the endpoint URL: "https://devicefarm.us-east-1.amazonaws.com/"

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_devicefarm_upload`

- **Client:** `devicefarm`
- **Method:** `list_uploads`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "arn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_devopsguru_resource_collection`

- **Client:** `devops-guru`
- **Method:** `get_resource_collection`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ResourceCollectionType"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_directory_service_conditional_forwarder`

- **Client:** `ds`
- **Method:** `describe_conditional_forwarders`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DirectoryId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_directory_service_region`

- **Client:** `ds`
- **Method:** `describe_regions`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DirectoryId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_directory_service_shared_directory`

- **Client:** `ds`
- **Method:** `describe_shared_directories`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "OwnerDirectoryId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_directory_service_shared_directory_accepter`

- **Client:** `ds`
- **Method:** `describe_shared_directories`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "OwnerDirectoryId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_drs_replication_configuration_template`

- **Client:** `drs`
- **Method:** `describe_replication_configuration_templates`
- **Error Code:** `UninitializedAccountException`
- **Error Type:** `api_error`

**Error:** API error (UninitializedAccountException): Account not initialized

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_dx_gateway_association`

- **Client:** `directconnect`
- **Method:** `describe_direct_connect_gateway_associations`
- **Error Code:** `DirectConnectClientException`
- **Error Type:** `api_error`

**Error:** API error (DirectConnectClientException): Either Direct Connect Gateway ID or Associated Gateway ID or Association ID must be set

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_dynamodb_contributor_insights`

- **Client:** `dynamodb`
- **Method:** `describe_contributor_insights`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "TableName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_dynamodb_kinesis_streaming_destination`

- **Client:** `dynamodb`
- **Method:** `describe_kinesis_streaming_destination`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "TableName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_dynamodb_resource_policy`

- **Client:** `dynamodb`
- **Method:** `get_resource_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ResourceArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_dynamodb_table`

- **Client:** `dynamodb`
- **Method:** `describe_table`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "TableName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_dynamodb_table_item`

- **Client:** `dynamodb`
- **Method:** `describe_table`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "TableName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_dynamodb_table_replica`

- **Client:** `dynamodb`
- **Method:** `describe_table_replica_auto_scaling`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "TableName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_dynamodb_tag`

- **Client:** `dynamodb`
- **Method:** `list_tags_of_resource`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ResourceArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ebs_encryption_by_default`

- **Client:** `ec2`
- **Method:** `get_ebs_encryption_by_default`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: object of type 'bool' has no len()

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_ec2_client_vpn_authorization_rule`

- **Client:** `ec2`
- **Method:** `describe_client_vpn_authorization_rules`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ClientVpnEndpointId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ec2_client_vpn_route`

- **Client:** `ec2`
- **Method:** `describe_client_vpn_routes`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ClientVpnEndpointId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ec2_image_block_public_access`

- **Client:** `ec2`
- **Method:** `describe_image_attribute`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Attribute"
Missing required parameter in input: "ImageId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ec2_serial_console_access`

- **Client:** `ec2`
- **Method:** `get_serial_console_access_status`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: object of type 'bool' has no len()

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_ec2_transit_gateway_policy_table`

- **Client:** `ec2`
- **Method:** `get_transit_gateway_policy_table_entries`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "TransitGatewayPolicyTableId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ec2_transit_gateway_policy_table_association`

- **Client:** `ec2`
- **Method:** `get_transit_gateway_policy_table_associations`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "TransitGatewayPolicyTableId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ec2_transit_gateway_prefix_list_reference`

- **Client:** `ec2`
- **Method:** `get_transit_gateway_prefix_list_references`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "TransitGatewayRouteTableId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ec2_transit_gateway_route`

- **Client:** `ec2`
- **Method:** `search_transit_gateway_routes`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "TransitGatewayRouteTableId"
Missing required parameter in input: "Filters"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ec2_transit_gateway_route_table_association`

- **Client:** `ec2`
- **Method:** `get_transit_gateway_policy_table_associations`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "TransitGatewayPolicyTableId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ec2_transit_gateway_route_table_propagation`

- **Client:** `ec2`
- **Method:** `get_transit_gateway_route_table_propagations`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "TransitGatewayRouteTableId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ecr_account_setting`

- **Client:** `ecr`
- **Method:** `get_account_setting`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "name"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ecr_lifecycle_policy`

- **Client:** `ecr`
- **Method:** `get_lifecycle_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "repositoryName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ecr_registry_policy`

- **Client:** `ecr`
- **Method:** `get_registry_policy`
- **Error Code:** `RegistryPolicyNotFoundException`
- **Error Type:** `api_error`

**Error:** API error (RegistryPolicyNotFoundException): Registry policy does not exist in the registry with id '566972129213'

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_ecr_replication_configuration`

- **Client:** `ecr`
- **Method:** `get_registry_policy`
- **Error Code:** `RegistryPolicyNotFoundException`
- **Error Type:** `api_error`

**Error:** API error (RegistryPolicyNotFoundException): Registry policy does not exist in the registry with id '566972129213'

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_ecr_repository_policy`

- **Client:** `ecr`
- **Method:** `get_repository_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "repositoryName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ecrpublic_repository_policy`

- **Client:** `ecr-public`
- **Method:** `get_repository_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "repositoryName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ecs_tag`

- **Client:** `ecs`
- **Method:** `list_tags_for_resource`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "resourceArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ecs_task_definition`

- **Client:** `ecs`
- **Method:** `describe_task_definition`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "taskDefinition"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ecs_task_set`

- **Client:** `ecs`
- **Method:** `describe_task_sets`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "cluster"
Missing required parameter in input: "service"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_efs_backup_policy`

- **Client:** `efs`
- **Method:** `describe_backup_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "FileSystemId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_efs_file_system_policy`

- **Client:** `efs`
- **Method:** `describe_file_system_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "FileSystemId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_efs_mount_target`

- **Client:** `efs`
- **Method:** `describe_mount_targets`
- **Error Code:** `BadRequest`
- **Error Type:** `api_error`

**Error:** API error (BadRequest): Must specify exactly one mutually exclusive parameter.

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_efs_replication_configuration`

- **Client:** `efs`
- **Method:** `describe_replication_configurations`
- **Error Code:** `ReplicationNotFound`
- **Error Type:** `api_error`

**Error:** API error (ReplicationNotFound): No replications found.

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_eks_access_entry`

- **Client:** `eks`
- **Method:** `list_access_entries`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "clusterName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_eks_access_policy_association`

- **Client:** `eks`
- **Method:** `list_associated_access_policies`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "clusterName"
Missing required parameter in input: "principalArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_eks_addon`

- **Client:** `eks`
- **Method:** `list_addons`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "clusterName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_eks_capability`

- **Client:** `eks`
- **Method:** `describe_cluster`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "name"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_eks_fargate_profile`

- **Client:** `eks`
- **Method:** `list_fargate_profiles`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "clusterName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_eks_identity_provider_config`

- **Client:** `eks`
- **Method:** `list_identity_provider_configs`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "clusterName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_eks_node_group`

- **Client:** `eks`
- **Method:** `list_nodegroups`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "clusterName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_eks_pod_identity_association`

- **Client:** `eks`
- **Method:** `list_pod_identity_associations`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "clusterName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_elastic_beanstalk_configuration_template`

- **Client:** `elasticbeanstalk`
- **Method:** `describe_configuration_settings`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ApplicationName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_elasticsearch_domain`

- **Client:** `es`
- **Method:** `describe_elasticsearch_domains`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DomainNames"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_elasticsearch_domain_policy`

- **Client:** `es`
- **Method:** `describe_elasticsearch_domain_config`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DomainName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_elasticsearch_domain_saml_options`

- **Client:** `es`
- **Method:** `describe_elasticsearch_domain`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DomainName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_elasticsearch_vpc_endpoint`

- **Client:** `es`
- **Method:** `describe_vpc_endpoints`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "VpcEndpointIds"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_elastictranscoder_pipeline`

- **Client:** `elastictranscoder`
- **Method:** `list_pipelines`
- **Error Code:** `ValidationException`
- **Error Type:** `invalid_parameters`

**Error:** Invalid parameters: AWS is discontinuing support for Amazon Elastic Transcoder and is no longer open to new customers. For more information about transitioning to AWS Elemental MediaConvert, see https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_elastictranscoder_preset`

- **Client:** `elastictranscoder`
- **Method:** `list_presets`
- **Error Code:** `ValidationException`
- **Error Type:** `invalid_parameters`

**Error:** Invalid parameters: AWS is discontinuing support for Amazon Elastic Transcoder and is no longer open to new customers. For more information about transitioning to AWS Elemental MediaConvert, see https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_elb_attachment`

- **Client:** `elb`
- **Method:** `describe_load_balancer_attributes`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "LoadBalancerName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_emr_instance_fleet`

- **Client:** `emr`
- **Method:** `list_instance_fleets`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ClusterId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_emr_instance_group`

- **Client:** `emr`
- **Method:** `list_instance_groups`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ClusterId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_emr_managed_scaling_policy`

- **Client:** `emr`
- **Method:** `get_managed_scaling_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ClusterId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_evidently_feature`

- **Client:** `evidently`
- **Method:** `list_features`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "project"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_evidently_launch`

- **Client:** `evidently`
- **Method:** `list_launches`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "project"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_evidently_project`

- **Client:** `evidently`
- **Method:** `list_projects`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Could not connect to the endpoint URL: "https://evidently.us-east-1.amazonaws.com/projects"

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_evidently_segment`

- **Client:** `evidently`
- **Method:** `list_segments`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Could not connect to the endpoint URL: "https://evidently.us-east-1.amazonaws.com/segments"

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_finspace_kx_dataview`

- **Client:** `finspace-data`
- **Method:** `list_data_views`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "datasetId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_finspace_kx_user`

- **Client:** `finspace-data`
- **Method:** `list_users`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "maxResults"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_fis_target_account_configuration`

- **Client:** `fis`
- **Method:** `list_target_account_configurations`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "experimentTemplateId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_fms_admin_account`

- **Client:** `fms`
- **Method:** `list_admin_accounts_for_organization`
- **Error Code:** `InvalidOperationException`
- **Error Type:** `api_error`

**Error:** API error (InvalidOperationException): No default admin could be found for organization o-kwejogzrjh

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_glacier_vault_lock`

- **Client:** `glacier`
- **Method:** `get_vault_lock`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "vaultName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_globalaccelerator_accelerator`

- **Client:** `globalaccelerator`
- **Method:** `list_accelerators`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Could not connect to the endpoint URL: "https://globalaccelerator.us-east-1.amazonaws.com/"

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_globalaccelerator_cross_account_attachment`

- **Client:** `globalaccelerator`
- **Method:** `list_cross_account_attachments`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Could not connect to the endpoint URL: "https://globalaccelerator.us-east-1.amazonaws.com/"

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_globalaccelerator_custom_routing_accelerator`

- **Client:** `globalaccelerator`
- **Method:** `list_accelerators`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Could not connect to the endpoint URL: "https://globalaccelerator.us-east-1.amazonaws.com/"

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_globalaccelerator_custom_routing_endpoint_group`

- **Client:** `globalaccelerator`
- **Method:** `list_endpoint_groups`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ListenerArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_globalaccelerator_custom_routing_listener`

- **Client:** `globalaccelerator`
- **Method:** `list_listeners`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AcceleratorArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_globalaccelerator_endpoint_group`

- **Client:** `globalaccelerator`
- **Method:** `list_endpoint_groups`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ListenerArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_globalaccelerator_listener`

- **Client:** `globalaccelerator`
- **Method:** `list_listeners`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AcceleratorArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_glue_catalog_table`

- **Client:** `glue`
- **Method:** `get_tables`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DatabaseName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_glue_catalog_table_optimizer`

- **Client:** `glue`
- **Method:** `list_table_optimizer_runs`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "CatalogId"
Missing required parameter in input: "DatabaseName"
Missing required parameter in input: "TableName"
Missing required parameter in input: "Type"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_glue_partition`

- **Client:** `glue`
- **Method:** `get_partitions`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DatabaseName"
Missing required parameter in input: "TableName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_glue_partition_index`

- **Client:** `glue`
- **Method:** `get_partition_indexes`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DatabaseName"
Missing required parameter in input: "TableName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_glue_resource_policy`

- **Client:** `glue`
- **Method:** `get_resource_policy`
- **Error Code:** `EntityNotFoundException`
- **Error Type:** `api_error`

**Error:** API error (EntityNotFoundException): Policy not found

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_glue_trigger`

- **Client:** `glue`
- **Method:** `get_trigger`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Name"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_glue_user_defined_function`

- **Client:** `glue`
- **Method:** `get_user_defined_functions`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Pattern"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_grafana_license_association`

- **Client:** `grafana`
- **Method:** `describe_workspace`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "workspaceId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_grafana_role_association`

- **Client:** `grafana`
- **Method:** `list_permissions`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "workspaceId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_grafana_workspace_saml_configuration`

- **Client:** `grafana`
- **Method:** `describe_workspace_authentication`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "workspaceId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_grafana_workspace_service_account`

- **Client:** `grafana`
- **Method:** `list_workspace_service_accounts`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "workspaceId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_grafana_workspace_service_account_token`

- **Client:** `grafana`
- **Method:** `list_workspace_service_account_tokens`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "serviceAccountId"
Missing required parameter in input: "workspaceId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_guardduty_detector_feature`

- **Client:** `guardduty`
- **Method:** `get_detector`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DetectorId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_guardduty_filter`

- **Client:** `guardduty`
- **Method:** `list_filters`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DetectorId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_guardduty_ipset`

- **Client:** `guardduty`
- **Method:** `list_ip_sets`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DetectorId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_guardduty_member`

- **Client:** `guardduty`
- **Method:** `list_members`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DetectorId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_guardduty_member_detector_feature`

- **Client:** `guardduty`
- **Method:** `get_member_detectors`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DetectorId"
Missing required parameter in input: "AccountIds"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_guardduty_organization_configuration`

- **Client:** `guardduty`
- **Method:** `describe_organization_configuration`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DetectorId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_guardduty_organization_configuration_feature`

- **Client:** `guardduty`
- **Method:** `describe_organization_configuration`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DetectorId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_guardduty_publishing_destination`

- **Client:** `guardduty`
- **Method:** `list_publishing_destinations`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DetectorId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_guardduty_threatintelset`

- **Client:** `guardduty`
- **Method:** `list_threat_intel_sets`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DetectorId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_iam_account_password_policy`

- **Client:** `iam`
- **Method:** `get_account_password_policy`
- **Error Code:** `NoSuchEntity`
- **Error Type:** `api_error`

**Error:** API error (NoSuchEntity): The Password Policy with domain name 566972129213 cannot be found.

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_iam_group_membership`

- **Client:** `iam`
- **Method:** `get_group`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "GroupName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_iam_group_policies_exclusive`

- **Client:** `iam`
- **Method:** `list_group_policies`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "GroupName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_iam_group_policy`

- **Client:** `iam`
- **Method:** `list_group_policies`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "GroupName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_iam_group_policy_attachment`

- **Client:** `iam`
- **Method:** `list_attached_group_policies`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "GroupName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_iam_group_policy_attachments_exclusive`

- **Client:** `iam`
- **Method:** `list_attached_group_policies`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "GroupName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_iam_instance_profile`

- **Client:** `iam`
- **Method:** `get_instance_profile`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "InstanceProfileName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_iam_organizations_features`

- **Client:** `iam`
- **Method:** `get_organizations_access_report`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "JobId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_iam_policy_attachment`

- **Client:** `iam`
- **Method:** `get_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "PolicyArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_iam_role_policies_exclusive`

- **Client:** `iam`
- **Method:** `list_role_policies`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "RoleName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_iam_role_policy`

- **Client:** `iam`
- **Method:** `list_role_policies`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "RoleName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_iam_role_policy_attachment`

- **Client:** `iam`
- **Method:** `list_attached_role_policies`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "RoleName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_iam_role_policy_attachments_exclusive`

- **Client:** `iam`
- **Method:** `list_attached_role_policies`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "RoleName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_iam_user_group_membership`

- **Client:** `iam`
- **Method:** `get_group`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "GroupName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_iam_user_login_profile`

- **Client:** `iam`
- **Method:** `get_login_profile`
- **Error Code:** `NoSuchEntity`
- **Error Type:** `api_error`

**Error:** API error (NoSuchEntity): Login Profile for User andyt530 cannot be found.

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_iam_user_policies_exclusive`

- **Client:** `iam`
- **Method:** `list_user_policies`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "UserName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_iam_user_policy`

- **Client:** `iam`
- **Method:** `list_user_policies`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "UserName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_iam_user_policy_attachment`

- **Client:** `iam`
- **Method:** `list_attached_user_policies`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "UserName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_iam_user_policy_attachments_exclusive`

- **Client:** `iam`
- **Method:** `list_attached_user_policies`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "UserName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_identitystore_group`

- **Client:** `identitystore`
- **Method:** `list_groups`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "IdentityStoreId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_identitystore_group_membership`

- **Client:** `identitystore`
- **Method:** `list_group_memberships`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "IdentityStoreId"
Missing required parameter in input: "GroupId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_identitystore_user`

- **Client:** `identitystore`
- **Method:** `list_users`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "IdentityStoreId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_iot_logging_options`

- **Client:** `iot`
- **Method:** `get_v2_logging_options`
- **Error Code:** `NotConfiguredException`
- **Error Type:** `api_error`

**Error:** API error (NotConfiguredException): SetV2LoggingOptions was not previously called. No logging options have been set.

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_iot_thing_group_membership`

- **Client:** `iot`
- **Method:** `list_things_in_thing_group`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "thingGroupName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_iot_thing_principal_attachment`

- **Client:** `iot`
- **Method:** `list_thing_principals`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "thingName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_kendra_data_source`

- **Client:** `kendra`
- **Method:** `list_data_sources`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "IndexId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_kendra_experience`

- **Client:** `kendra`
- **Method:** `list_experiences`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "IndexId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_kendra_faq`

- **Client:** `kendra`
- **Method:** `list_faqs`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "IndexId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_kendra_query_suggestions_block_list`

- **Client:** `kendra`
- **Method:** `list_query_suggestions_block_lists`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "IndexId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_kendra_thesaurus`

- **Client:** `kendra`
- **Method:** `list_thesauri`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "IndexId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_keyspaces_table`

- **Client:** `keyspaces`
- **Method:** `list_tables`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "keyspaceName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_kinesis_resource_policy`

- **Client:** `kinesis`
- **Method:** `get_resource_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ResourceARN"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_kinesis_stream_consumer`

- **Client:** `kinesis`
- **Method:** `list_stream_consumers`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "StreamARN"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_kinesisanalyticsv2_application_snapshot`

- **Client:** `kinesisanalyticsv2`
- **Method:** `list_application_snapshots`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ApplicationName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_kms_ciphertext`

- **Client:** `kms`
- **Method:** `list_grants`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "KeyId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_kms_grant`

- **Client:** `kms`
- **Method:** `list_grants`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "KeyId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_kms_key_policy`

- **Client:** `kms`
- **Method:** `list_key_policies`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "KeyId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_lakeformation_identity_center_configuration`

- **Client:** `lakeformation`
- **Method:** `describe_lake_formation_identity_center_configuration`
- **Error Code:** `EntityNotFoundException`
- **Error Type:** `api_error`

**Error:** API error (EntityNotFoundException): The requested application is not found

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_lakeformation_resource_lf_tags`

- **Client:** `lakeformation`
- **Method:** `get_resource_lf_tags`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Resource"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_lambda_alias`

- **Client:** `lambda`
- **Method:** `list_aliases`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "FunctionName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_lambda_function_event_invoke_config`

- **Client:** `lambda`
- **Method:** `list_function_event_invoke_configs`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "FunctionName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_lambda_function_recursion_config`

- **Client:** `lambda`
- **Method:** `get_function_recursion_config`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "FunctionName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_lambda_function_url`

- **Client:** `lambda`
- **Method:** `list_function_url_configs`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "FunctionName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_lambda_layer_version`

- **Client:** `lambda`
- **Method:** `list_layer_versions`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "LayerName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_lambda_layer_version_permission`

- **Client:** `lambda`
- **Method:** `list_layer_versions`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "LayerName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_lambda_permission`

- **Client:** `lambda`
- **Method:** `get_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "FunctionName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_lambda_provisioned_concurrency_config`

- **Client:** `lambda`
- **Method:** `list_provisioned_concurrency_configs`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "FunctionName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_lambda_runtime_management_config`

- **Client:** `lambda`
- **Method:** `get_runtime_management_config`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "FunctionName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_lb_listener`

- **Client:** `elbv2`
- **Method:** `describe_listeners`
- **Error Code:** `ValidationError`
- **Error Type:** `api_error`

**Error:** API error (ValidationError): You must specify either listener ARNs or a load balancer ARN

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_lb_listener_certificate`

- **Client:** `elbv2`
- **Method:** `describe_listener_certificates`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ListenerArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_lb_listener_rule`

- **Client:** `elbv2`
- **Method:** `describe_rules`
- **Error Code:** `ValidationError`
- **Error Type:** `api_error`

**Error:** API error (ValidationError): You must specify either listener rule ARNs or a listener ARN

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_lb_target_group_attachment`

- **Client:** `elbv2`
- **Method:** `describe_target_group_attributes`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "TargetGroupArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_lb_trust_store`

- **Client:** `elbv2`
- **Method:** `describe_load_balancer_attributes`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "LoadBalancerArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_lb_trust_store_revocation`

- **Client:** `elbv2`
- **Method:** `describe_load_balancer_attributes`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "LoadBalancerArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_lex_bot_alias`

- **Client:** `lex-models`
- **Method:** `get_bot_aliases`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "botName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_lexv2models_bot_locale`

- **Client:** `lexv2-models`
- **Method:** `list_bot_locales`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "botId"
Missing required parameter in input: "botVersion"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_lexv2models_bot_version`

- **Client:** `lexv2-models`
- **Method:** `list_bot_versions`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "botId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_lexv2models_intent`

- **Client:** `lexv2-models`
- **Method:** `list_intents`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "botId"
Missing required parameter in input: "botVersion"
Missing required parameter in input: "localeId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_lexv2models_slot`

- **Client:** `lexv2-models`
- **Method:** `list_slots`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "botId"
Missing required parameter in input: "botVersion"
Missing required parameter in input: "localeId"
Missing required parameter in input: "intentId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_lexv2models_slot_type`

- **Client:** `lexv2-models`
- **Method:** `list_slot_types`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "botId"
Missing required parameter in input: "botVersion"
Missing required parameter in input: "localeId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_licensemanager_association`

- **Client:** `license-manager`
- **Method:** `list_associations_for_license_configuration`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "LicenseConfigurationArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_lightsail_bucket_access_key`

- **Client:** `lightsail`
- **Method:** `get_bucket_access_keys`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "bucketName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_lightsail_container_service_deployment_version`

- **Client:** `lightsail`
- **Method:** `get_container_service_deployments`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "serviceName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_lightsail_instance_public_ports`

- **Client:** `lightsail`
- **Method:** `get_instance_port_states`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "instanceName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_lightsail_lb_certificate_attachment`

- **Client:** `lightsail`
- **Method:** `get_load_balancer_tls_certificates`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "loadBalancerName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_load_balancer_listener_policy`

- **Client:** `elbv2`
- **Method:** `describe_listeners`
- **Error Code:** `ValidationError`
- **Error Type:** `api_error`

**Error:** API error (ValidationError): You must specify either listener ARNs or a load balancer ARN

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_location_tracker_association`

- **Client:** `location`
- **Method:** `list_tracker_consumers`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "TrackerName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_m2_deployment`

- **Client:** `m2`
- **Method:** `list_deployments`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "applicationId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_media_store_container_policy`

- **Client:** `mediastore`
- **Method:** `get_container_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ContainerName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_medialive_multiplex_program`

- **Client:** `medialive`
- **Method:** `list_multiplex_programs`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "MultiplexId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_msk_scram_secret_association`

- **Client:** `kafka`
- **Method:** `list_scram_secrets`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ClusterArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_msk_single_scram_secret_association`

- **Client:** `kafka`
- **Method:** `list_scram_secrets`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ClusterArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_networkfirewall_firewall_transit_gateway_attachment_accepter`

- **Client:** `network-firewall`
- **Method:** `describe_firewall`
- **Error Code:** `InvalidRequestException`
- **Error Type:** `api_error`

**Error:** API error (InvalidRequestException): At least one of FirewallName or FirewallArn must be set

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_networkfirewall_vpc_endpoint_association`

- **Client:** `network-firewall`
- **Method:** `describe_firewall`
- **Error Code:** `InvalidRequestException`
- **Error Type:** `api_error`

**Error:** API error (InvalidRequestException): At least one of FirewallName or FirewallArn must be set

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_networkmanager_device`

- **Client:** `networkmanager`
- **Method:** `get_devices`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "GlobalNetworkId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_networkmanager_site`

- **Client:** `networkmanager`
- **Method:** `get_sites`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "GlobalNetworkId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_networkmanager_transit_gateway_registration`

- **Client:** `networkmanager`
- **Method:** `get_transit_gateway_registrations`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "GlobalNetworkId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_notifications_event_rule`

- **Client:** `notifications`
- **Method:** `list_event_rules`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "notificationConfigurationArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_observabilityadmin_centralization_rule_for_organization`

- **Client:** `observabilityadmin`
- **Method:** `list_resource_telemetry`
- **Error Code:** `ValidationException`
- **Error Type:** `invalid_parameters`

**Error:** Invalid parameters: Account not onboarded to Telemetry Evaluation.

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_opensearch_authorize_vpc_endpoint_access`

- **Client:** `opensearch`
- **Method:** `list_vpc_endpoint_access`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DomainName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_opensearchserverless_access_policy`

- **Client:** `opensearchserverless`
- **Method:** `list_access_policies`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "type"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_opensearchserverless_lifecycle_policy`

- **Client:** `opensearchserverless`
- **Method:** `list_lifecycle_policies`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "type"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_opensearchserverless_security_config`

- **Client:** `opensearchserverless`
- **Method:** `list_security_configs`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "type"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_opensearchserverless_security_policy`

- **Client:** `opensearchserverless`
- **Method:** `list_security_policies`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "type"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_opsworks_application`

- **Client:** `opsworks`
- **Method:** `list_applications`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Unknown service: 'opsworks'. Valid service names are: accessanalyzer, account, acm, acm-pca, aiops, amp, amplify, amplifybackend, amplifyuibuilder, apigateway, apigatewaymanagementapi, apigatewayv2, appconfig, appconfigdata, appfabric, appflow, appintegrations, application-autoscaling, application-insights, application-signals, applicationcostprofiler, appmesh, apprunner, appstream, appsync, arc-region-switch, arc-zonal-shift, artifact, athena, auditmanager, autoscaling, autoscaling-plans, b2bi, backup, backup-gateway, backupsearch, batch, bcm-dashboards, bcm-data-exports, bcm-pricing-calculator, bcm-recommended-actions, bedrock, bedrock-agent, bedrock-agent-runtime, bedrock-agentcore, bedrock-agentcore-control, bedrock-data-automation, bedrock-data-automation-runtime, bedrock-runtime, billing, billingconductor, braket, budgets, ce, chatbot, chime, chime-sdk-identity, chime-sdk-media-pipelines, chime-sdk-meetings, chime-sdk-messaging, chime-sdk-voice, cleanrooms, cleanroomsml, cloud9, cloudcontrol, clouddirectory, cloudformation, cloudfront, cloudfront-keyvaluestore, cloudhsm, cloudhsmv2, cloudsearch, cloudsearchdomain, cloudtrail, cloudtrail-data, cloudwatch, codeartifact, codebuild, codecatalyst, codecommit, codeconnections, codedeploy, codeguru-reviewer, codeguru-security, codeguruprofiler, codepipeline, codestar-connections, codestar-notifications, cognito-identity, cognito-idp, cognito-sync, comprehend, comprehendmedical, compute-optimizer, compute-optimizer-automation, config, connect, connect-contact-lens, connectcampaigns, connectcampaignsv2, connectcases, connectparticipant, controlcatalog, controltower, cost-optimization-hub, cur, customer-profiles, databrew, dataexchange, datapipeline, datasync, datazone, dax, deadline, detective, devicefarm, devops-guru, directconnect, discovery, dlm, dms, docdb, docdb-elastic, drs, ds, ds-data, dsql, dynamodb, dynamodbstreams, ebs, ec2, ec2-instance-connect, ec2-mercury, ecr, ecr-public, ecs, efs, eks, eks-auth, elasticache, elasticbeanstalk, elastictranscoder, elb, elbv2, emr, emr-containers, emr-serverless, entityresolution, es, events, evidently, evs, finspace, finspace-data, firehose, fis, fms, forecast, forecastquery, frauddetector, freetier, fsx, gamelift, gameliftstreams, geo-maps, geo-places, geo-routes, glacier, globalaccelerator, glue, grafana, greengrass, greengrassv2, groundstation, guardduty, health, healthlake, iam, identitystore, imagebuilder, importexport, inspector, inspector-scan, inspector2, internetmonitor, invoicing, iot, iot-data, iot-jobs-data, iot-managed-integrations, iotanalytics, iotdeviceadvisor, iotevents, iotevents-data, iotfleetwise, iotsecuretunneling, iotsitewise, iotthingsgraph, iottwinmaker, iotwireless, ivs, ivs-realtime, ivschat, kafka, kafkaconnect, kendra, kendra-ranking, keyspaces, keyspacesstreams, kinesis, kinesis-video-archived-media, kinesis-video-media, kinesis-video-signaling, kinesis-video-webrtc-storage, kinesisanalytics, kinesisanalyticsv2, kinesisvideo, kms, lakeformation, lambda, launch-wizard, lex-models, lex-runtime, lexv2-models, lexv2-runtime, license-manager, license-manager-linux-subscriptions, license-manager-user-subscriptions, lightsail, location, logs, lookoutequipment, m2, machinelearning, macie2, mailmanager, managedblockchain, managedblockchain-query, marketplace-agreement, marketplace-catalog, marketplace-deployment, marketplace-entitlement, marketplace-reporting, marketplacecommerceanalytics, mediaconnect, mediaconvert, medialive, mediapackage, mediapackage-vod, mediapackagev2, mediastore, mediastore-data, mediatailor, medical-imaging, memorydb, meteringmarketplace, mgh, mgn, migration-hub-refactor-spaces, migrationhub-config, migrationhuborchestrator, migrationhubstrategy, mpa, mq, mturk, mwaa, mwaa-serverless, neptune, neptune-graph, neptunedata, network-firewall, networkflowmonitor, networkmanager, networkmonitor, notifications, notificationscontacts, nova-act, oam, observabilityadmin, odb, omics, opensearch, opensearchserverless, organizations, osis, outposts, panorama, partnercentral-account, partnercentral-benefits, partnercentral-channel, partnercentral-selling, payment-cryptography, payment-cryptography-data, pca-connector-ad, pca-connector-scep, pcs, personalize, personalize-events, personalize-runtime, pi, pinpoint, pinpoint-email, pinpoint-sms-voice, pinpoint-sms-voice-v2, pipes, polly, pricing, proton, qapps, qbusiness, qconnect, quicksight, ram, rbin, rds, rds-data, redshift, redshift-data, redshift-serverless, rekognition, repostspace, resiliencehub, resource-explorer-2, resource-groups, resourcegroupstaggingapi, rolesanywhere, route53, route53-recovery-cluster, route53-recovery-control-config, route53-recovery-readiness, route53domains, route53globalresolver, route53profiles, route53resolver, rtbfabric, rum, s3, s3control, s3outposts, s3tables, s3vectors, sagemaker, sagemaker-a2i-runtime, sagemaker-edge, sagemaker-featurestore-runtime, sagemaker-geospatial, sagemaker-metrics, sagemaker-runtime, savingsplans, scheduler, schemas, sdb, secretsmanager, security-ir, securityhub, securitylake, serverlessrepo, service-quotas, servicecatalog, servicecatalog-appregistry, servicediscovery, ses, sesv2, shield, signer, signin, simspaceweaver, sms-voice, snow-device-management, snowball, sns, socialmessaging, sqs, ssm, ssm-contacts, ssm-guiconnect, ssm-incidents, ssm-quicksetup, ssm-sap, sso, sso-admin, sso-oidc, stepfunctions, storagegateway, sts, supplychain, support, support-app, swf, synthetics, taxsettings, textract, timestream-influxdb, timestream-query, timestream-write, tnb, transcribe, transfer, translate, trustedadvisor, verifiedpermissions, voice-id, vpc-lattice, vpc-lattice-preview, vpc-service-network, waf, waf-regional, wafv2, wellarchitected, wickr, wisdom, workdocs, workmail, workmailmessageflow, workspaces, workspaces-instances, workspaces-thin-client, workspaces-web, xray

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_opsworks_custom_layer`

- **Client:** `opsworks`
- **Method:** `list_custom_layers`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Unknown service: 'opsworks'. Valid service names are: accessanalyzer, account, acm, acm-pca, aiops, amp, amplify, amplifybackend, amplifyuibuilder, apigateway, apigatewaymanagementapi, apigatewayv2, appconfig, appconfigdata, appfabric, appflow, appintegrations, application-autoscaling, application-insights, application-signals, applicationcostprofiler, appmesh, apprunner, appstream, appsync, arc-region-switch, arc-zonal-shift, artifact, athena, auditmanager, autoscaling, autoscaling-plans, b2bi, backup, backup-gateway, backupsearch, batch, bcm-dashboards, bcm-data-exports, bcm-pricing-calculator, bcm-recommended-actions, bedrock, bedrock-agent, bedrock-agent-runtime, bedrock-agentcore, bedrock-agentcore-control, bedrock-data-automation, bedrock-data-automation-runtime, bedrock-runtime, billing, billingconductor, braket, budgets, ce, chatbot, chime, chime-sdk-identity, chime-sdk-media-pipelines, chime-sdk-meetings, chime-sdk-messaging, chime-sdk-voice, cleanrooms, cleanroomsml, cloud9, cloudcontrol, clouddirectory, cloudformation, cloudfront, cloudfront-keyvaluestore, cloudhsm, cloudhsmv2, cloudsearch, cloudsearchdomain, cloudtrail, cloudtrail-data, cloudwatch, codeartifact, codebuild, codecatalyst, codecommit, codeconnections, codedeploy, codeguru-reviewer, codeguru-security, codeguruprofiler, codepipeline, codestar-connections, codestar-notifications, cognito-identity, cognito-idp, cognito-sync, comprehend, comprehendmedical, compute-optimizer, compute-optimizer-automation, config, connect, connect-contact-lens, connectcampaigns, connectcampaignsv2, connectcases, connectparticipant, controlcatalog, controltower, cost-optimization-hub, cur, customer-profiles, databrew, dataexchange, datapipeline, datasync, datazone, dax, deadline, detective, devicefarm, devops-guru, directconnect, discovery, dlm, dms, docdb, docdb-elastic, drs, ds, ds-data, dsql, dynamodb, dynamodbstreams, ebs, ec2, ec2-instance-connect, ec2-mercury, ecr, ecr-public, ecs, efs, eks, eks-auth, elasticache, elasticbeanstalk, elastictranscoder, elb, elbv2, emr, emr-containers, emr-serverless, entityresolution, es, events, evidently, evs, finspace, finspace-data, firehose, fis, fms, forecast, forecastquery, frauddetector, freetier, fsx, gamelift, gameliftstreams, geo-maps, geo-places, geo-routes, glacier, globalaccelerator, glue, grafana, greengrass, greengrassv2, groundstation, guardduty, health, healthlake, iam, identitystore, imagebuilder, importexport, inspector, inspector-scan, inspector2, internetmonitor, invoicing, iot, iot-data, iot-jobs-data, iot-managed-integrations, iotanalytics, iotdeviceadvisor, iotevents, iotevents-data, iotfleetwise, iotsecuretunneling, iotsitewise, iotthingsgraph, iottwinmaker, iotwireless, ivs, ivs-realtime, ivschat, kafka, kafkaconnect, kendra, kendra-ranking, keyspaces, keyspacesstreams, kinesis, kinesis-video-archived-media, kinesis-video-media, kinesis-video-signaling, kinesis-video-webrtc-storage, kinesisanalytics, kinesisanalyticsv2, kinesisvideo, kms, lakeformation, lambda, launch-wizard, lex-models, lex-runtime, lexv2-models, lexv2-runtime, license-manager, license-manager-linux-subscriptions, license-manager-user-subscriptions, lightsail, location, logs, lookoutequipment, m2, machinelearning, macie2, mailmanager, managedblockchain, managedblockchain-query, marketplace-agreement, marketplace-catalog, marketplace-deployment, marketplace-entitlement, marketplace-reporting, marketplacecommerceanalytics, mediaconnect, mediaconvert, medialive, mediapackage, mediapackage-vod, mediapackagev2, mediastore, mediastore-data, mediatailor, medical-imaging, memorydb, meteringmarketplace, mgh, mgn, migration-hub-refactor-spaces, migrationhub-config, migrationhuborchestrator, migrationhubstrategy, mpa, mq, mturk, mwaa, mwaa-serverless, neptune, neptune-graph, neptunedata, network-firewall, networkflowmonitor, networkmanager, networkmonitor, notifications, notificationscontacts, nova-act, oam, observabilityadmin, odb, omics, opensearch, opensearchserverless, organizations, osis, outposts, panorama, partnercentral-account, partnercentral-benefits, partnercentral-channel, partnercentral-selling, payment-cryptography, payment-cryptography-data, pca-connector-ad, pca-connector-scep, pcs, personalize, personalize-events, personalize-runtime, pi, pinpoint, pinpoint-email, pinpoint-sms-voice, pinpoint-sms-voice-v2, pipes, polly, pricing, proton, qapps, qbusiness, qconnect, quicksight, ram, rbin, rds, rds-data, redshift, redshift-data, redshift-serverless, rekognition, repostspace, resiliencehub, resource-explorer-2, resource-groups, resourcegroupstaggingapi, rolesanywhere, route53, route53-recovery-cluster, route53-recovery-control-config, route53-recovery-readiness, route53domains, route53globalresolver, route53profiles, route53resolver, rtbfabric, rum, s3, s3control, s3outposts, s3tables, s3vectors, sagemaker, sagemaker-a2i-runtime, sagemaker-edge, sagemaker-featurestore-runtime, sagemaker-geospatial, sagemaker-metrics, sagemaker-runtime, savingsplans, scheduler, schemas, sdb, secretsmanager, security-ir, securityhub, securitylake, serverlessrepo, service-quotas, servicecatalog, servicecatalog-appregistry, servicediscovery, ses, sesv2, shield, signer, signin, simspaceweaver, sms-voice, snow-device-management, snowball, sns, socialmessaging, sqs, ssm, ssm-contacts, ssm-guiconnect, ssm-incidents, ssm-quicksetup, ssm-sap, sso, sso-admin, sso-oidc, stepfunctions, storagegateway, sts, supplychain, support, support-app, swf, synthetics, taxsettings, textract, timestream-influxdb, timestream-query, timestream-write, tnb, transcribe, transfer, translate, trustedadvisor, verifiedpermissions, voice-id, vpc-lattice, vpc-lattice-preview, vpc-service-network, waf, waf-regional, wafv2, wellarchitected, wickr, wisdom, workdocs, workmail, workmailmessageflow, workspaces, workspaces-instances, workspaces-thin-client, workspaces-web, xray

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_opsworks_ecs_cluster_layer`

- **Client:** `opsworks`
- **Method:** `describe_ecs_clusters`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Unknown service: 'opsworks'. Valid service names are: accessanalyzer, account, acm, acm-pca, aiops, amp, amplify, amplifybackend, amplifyuibuilder, apigateway, apigatewaymanagementapi, apigatewayv2, appconfig, appconfigdata, appfabric, appflow, appintegrations, application-autoscaling, application-insights, application-signals, applicationcostprofiler, appmesh, apprunner, appstream, appsync, arc-region-switch, arc-zonal-shift, artifact, athena, auditmanager, autoscaling, autoscaling-plans, b2bi, backup, backup-gateway, backupsearch, batch, bcm-dashboards, bcm-data-exports, bcm-pricing-calculator, bcm-recommended-actions, bedrock, bedrock-agent, bedrock-agent-runtime, bedrock-agentcore, bedrock-agentcore-control, bedrock-data-automation, bedrock-data-automation-runtime, bedrock-runtime, billing, billingconductor, braket, budgets, ce, chatbot, chime, chime-sdk-identity, chime-sdk-media-pipelines, chime-sdk-meetings, chime-sdk-messaging, chime-sdk-voice, cleanrooms, cleanroomsml, cloud9, cloudcontrol, clouddirectory, cloudformation, cloudfront, cloudfront-keyvaluestore, cloudhsm, cloudhsmv2, cloudsearch, cloudsearchdomain, cloudtrail, cloudtrail-data, cloudwatch, codeartifact, codebuild, codecatalyst, codecommit, codeconnections, codedeploy, codeguru-reviewer, codeguru-security, codeguruprofiler, codepipeline, codestar-connections, codestar-notifications, cognito-identity, cognito-idp, cognito-sync, comprehend, comprehendmedical, compute-optimizer, compute-optimizer-automation, config, connect, connect-contact-lens, connectcampaigns, connectcampaignsv2, connectcases, connectparticipant, controlcatalog, controltower, cost-optimization-hub, cur, customer-profiles, databrew, dataexchange, datapipeline, datasync, datazone, dax, deadline, detective, devicefarm, devops-guru, directconnect, discovery, dlm, dms, docdb, docdb-elastic, drs, ds, ds-data, dsql, dynamodb, dynamodbstreams, ebs, ec2, ec2-instance-connect, ec2-mercury, ecr, ecr-public, ecs, efs, eks, eks-auth, elasticache, elasticbeanstalk, elastictranscoder, elb, elbv2, emr, emr-containers, emr-serverless, entityresolution, es, events, evidently, evs, finspace, finspace-data, firehose, fis, fms, forecast, forecastquery, frauddetector, freetier, fsx, gamelift, gameliftstreams, geo-maps, geo-places, geo-routes, glacier, globalaccelerator, glue, grafana, greengrass, greengrassv2, groundstation, guardduty, health, healthlake, iam, identitystore, imagebuilder, importexport, inspector, inspector-scan, inspector2, internetmonitor, invoicing, iot, iot-data, iot-jobs-data, iot-managed-integrations, iotanalytics, iotdeviceadvisor, iotevents, iotevents-data, iotfleetwise, iotsecuretunneling, iotsitewise, iotthingsgraph, iottwinmaker, iotwireless, ivs, ivs-realtime, ivschat, kafka, kafkaconnect, kendra, kendra-ranking, keyspaces, keyspacesstreams, kinesis, kinesis-video-archived-media, kinesis-video-media, kinesis-video-signaling, kinesis-video-webrtc-storage, kinesisanalytics, kinesisanalyticsv2, kinesisvideo, kms, lakeformation, lambda, launch-wizard, lex-models, lex-runtime, lexv2-models, lexv2-runtime, license-manager, license-manager-linux-subscriptions, license-manager-user-subscriptions, lightsail, location, logs, lookoutequipment, m2, machinelearning, macie2, mailmanager, managedblockchain, managedblockchain-query, marketplace-agreement, marketplace-catalog, marketplace-deployment, marketplace-entitlement, marketplace-reporting, marketplacecommerceanalytics, mediaconnect, mediaconvert, medialive, mediapackage, mediapackage-vod, mediapackagev2, mediastore, mediastore-data, mediatailor, medical-imaging, memorydb, meteringmarketplace, mgh, mgn, migration-hub-refactor-spaces, migrationhub-config, migrationhuborchestrator, migrationhubstrategy, mpa, mq, mturk, mwaa, mwaa-serverless, neptune, neptune-graph, neptunedata, network-firewall, networkflowmonitor, networkmanager, networkmonitor, notifications, notificationscontacts, nova-act, oam, observabilityadmin, odb, omics, opensearch, opensearchserverless, organizations, osis, outposts, panorama, partnercentral-account, partnercentral-benefits, partnercentral-channel, partnercentral-selling, payment-cryptography, payment-cryptography-data, pca-connector-ad, pca-connector-scep, pcs, personalize, personalize-events, personalize-runtime, pi, pinpoint, pinpoint-email, pinpoint-sms-voice, pinpoint-sms-voice-v2, pipes, polly, pricing, proton, qapps, qbusiness, qconnect, quicksight, ram, rbin, rds, rds-data, redshift, redshift-data, redshift-serverless, rekognition, repostspace, resiliencehub, resource-explorer-2, resource-groups, resourcegroupstaggingapi, rolesanywhere, route53, route53-recovery-cluster, route53-recovery-control-config, route53-recovery-readiness, route53domains, route53globalresolver, route53profiles, route53resolver, rtbfabric, rum, s3, s3control, s3outposts, s3tables, s3vectors, sagemaker, sagemaker-a2i-runtime, sagemaker-edge, sagemaker-featurestore-runtime, sagemaker-geospatial, sagemaker-metrics, sagemaker-runtime, savingsplans, scheduler, schemas, sdb, secretsmanager, security-ir, securityhub, securitylake, serverlessrepo, service-quotas, servicecatalog, servicecatalog-appregistry, servicediscovery, ses, sesv2, shield, signer, signin, simspaceweaver, sms-voice, snow-device-management, snowball, sns, socialmessaging, sqs, ssm, ssm-contacts, ssm-guiconnect, ssm-incidents, ssm-quicksetup, ssm-sap, sso, sso-admin, sso-oidc, stepfunctions, storagegateway, sts, supplychain, support, support-app, swf, synthetics, taxsettings, textract, timestream-influxdb, timestream-query, timestream-write, tnb, transcribe, transfer, translate, trustedadvisor, verifiedpermissions, voice-id, vpc-lattice, vpc-lattice-preview, vpc-service-network, waf, waf-regional, wafv2, wellarchitected, wickr, wisdom, workdocs, workmail, workmailmessageflow, workspaces, workspaces-instances, workspaces-thin-client, workspaces-web, xray

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_opsworks_ganglia_layer`

- **Client:** `opsworks`
- **Method:** `list_ganglia_layers`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Unknown service: 'opsworks'. Valid service names are: accessanalyzer, account, acm, acm-pca, aiops, amp, amplify, amplifybackend, amplifyuibuilder, apigateway, apigatewaymanagementapi, apigatewayv2, appconfig, appconfigdata, appfabric, appflow, appintegrations, application-autoscaling, application-insights, application-signals, applicationcostprofiler, appmesh, apprunner, appstream, appsync, arc-region-switch, arc-zonal-shift, artifact, athena, auditmanager, autoscaling, autoscaling-plans, b2bi, backup, backup-gateway, backupsearch, batch, bcm-dashboards, bcm-data-exports, bcm-pricing-calculator, bcm-recommended-actions, bedrock, bedrock-agent, bedrock-agent-runtime, bedrock-agentcore, bedrock-agentcore-control, bedrock-data-automation, bedrock-data-automation-runtime, bedrock-runtime, billing, billingconductor, braket, budgets, ce, chatbot, chime, chime-sdk-identity, chime-sdk-media-pipelines, chime-sdk-meetings, chime-sdk-messaging, chime-sdk-voice, cleanrooms, cleanroomsml, cloud9, cloudcontrol, clouddirectory, cloudformation, cloudfront, cloudfront-keyvaluestore, cloudhsm, cloudhsmv2, cloudsearch, cloudsearchdomain, cloudtrail, cloudtrail-data, cloudwatch, codeartifact, codebuild, codecatalyst, codecommit, codeconnections, codedeploy, codeguru-reviewer, codeguru-security, codeguruprofiler, codepipeline, codestar-connections, codestar-notifications, cognito-identity, cognito-idp, cognito-sync, comprehend, comprehendmedical, compute-optimizer, compute-optimizer-automation, config, connect, connect-contact-lens, connectcampaigns, connectcampaignsv2, connectcases, connectparticipant, controlcatalog, controltower, cost-optimization-hub, cur, customer-profiles, databrew, dataexchange, datapipeline, datasync, datazone, dax, deadline, detective, devicefarm, devops-guru, directconnect, discovery, dlm, dms, docdb, docdb-elastic, drs, ds, ds-data, dsql, dynamodb, dynamodbstreams, ebs, ec2, ec2-instance-connect, ec2-mercury, ecr, ecr-public, ecs, efs, eks, eks-auth, elasticache, elasticbeanstalk, elastictranscoder, elb, elbv2, emr, emr-containers, emr-serverless, entityresolution, es, events, evidently, evs, finspace, finspace-data, firehose, fis, fms, forecast, forecastquery, frauddetector, freetier, fsx, gamelift, gameliftstreams, geo-maps, geo-places, geo-routes, glacier, globalaccelerator, glue, grafana, greengrass, greengrassv2, groundstation, guardduty, health, healthlake, iam, identitystore, imagebuilder, importexport, inspector, inspector-scan, inspector2, internetmonitor, invoicing, iot, iot-data, iot-jobs-data, iot-managed-integrations, iotanalytics, iotdeviceadvisor, iotevents, iotevents-data, iotfleetwise, iotsecuretunneling, iotsitewise, iotthingsgraph, iottwinmaker, iotwireless, ivs, ivs-realtime, ivschat, kafka, kafkaconnect, kendra, kendra-ranking, keyspaces, keyspacesstreams, kinesis, kinesis-video-archived-media, kinesis-video-media, kinesis-video-signaling, kinesis-video-webrtc-storage, kinesisanalytics, kinesisanalyticsv2, kinesisvideo, kms, lakeformation, lambda, launch-wizard, lex-models, lex-runtime, lexv2-models, lexv2-runtime, license-manager, license-manager-linux-subscriptions, license-manager-user-subscriptions, lightsail, location, logs, lookoutequipment, m2, machinelearning, macie2, mailmanager, managedblockchain, managedblockchain-query, marketplace-agreement, marketplace-catalog, marketplace-deployment, marketplace-entitlement, marketplace-reporting, marketplacecommerceanalytics, mediaconnect, mediaconvert, medialive, mediapackage, mediapackage-vod, mediapackagev2, mediastore, mediastore-data, mediatailor, medical-imaging, memorydb, meteringmarketplace, mgh, mgn, migration-hub-refactor-spaces, migrationhub-config, migrationhuborchestrator, migrationhubstrategy, mpa, mq, mturk, mwaa, mwaa-serverless, neptune, neptune-graph, neptunedata, network-firewall, networkflowmonitor, networkmanager, networkmonitor, notifications, notificationscontacts, nova-act, oam, observabilityadmin, odb, omics, opensearch, opensearchserverless, organizations, osis, outposts, panorama, partnercentral-account, partnercentral-benefits, partnercentral-channel, partnercentral-selling, payment-cryptography, payment-cryptography-data, pca-connector-ad, pca-connector-scep, pcs, personalize, personalize-events, personalize-runtime, pi, pinpoint, pinpoint-email, pinpoint-sms-voice, pinpoint-sms-voice-v2, pipes, polly, pricing, proton, qapps, qbusiness, qconnect, quicksight, ram, rbin, rds, rds-data, redshift, redshift-data, redshift-serverless, rekognition, repostspace, resiliencehub, resource-explorer-2, resource-groups, resourcegroupstaggingapi, rolesanywhere, route53, route53-recovery-cluster, route53-recovery-control-config, route53-recovery-readiness, route53domains, route53globalresolver, route53profiles, route53resolver, rtbfabric, rum, s3, s3control, s3outposts, s3tables, s3vectors, sagemaker, sagemaker-a2i-runtime, sagemaker-edge, sagemaker-featurestore-runtime, sagemaker-geospatial, sagemaker-metrics, sagemaker-runtime, savingsplans, scheduler, schemas, sdb, secretsmanager, security-ir, securityhub, securitylake, serverlessrepo, service-quotas, servicecatalog, servicecatalog-appregistry, servicediscovery, ses, sesv2, shield, signer, signin, simspaceweaver, sms-voice, snow-device-management, snowball, sns, socialmessaging, sqs, ssm, ssm-contacts, ssm-guiconnect, ssm-incidents, ssm-quicksetup, ssm-sap, sso, sso-admin, sso-oidc, stepfunctions, storagegateway, sts, supplychain, support, support-app, swf, synthetics, taxsettings, textract, timestream-influxdb, timestream-query, timestream-write, tnb, transcribe, transfer, translate, trustedadvisor, verifiedpermissions, voice-id, vpc-lattice, vpc-lattice-preview, vpc-service-network, waf, waf-regional, wafv2, wellarchitected, wickr, wisdom, workdocs, workmail, workmailmessageflow, workspaces, workspaces-instances, workspaces-thin-client, workspaces-web, xray

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_opsworks_haproxy_layer`

- **Client:** `opsworks`
- **Method:** `list_haproxy_layers`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Unknown service: 'opsworks'. Valid service names are: accessanalyzer, account, acm, acm-pca, aiops, amp, amplify, amplifybackend, amplifyuibuilder, apigateway, apigatewaymanagementapi, apigatewayv2, appconfig, appconfigdata, appfabric, appflow, appintegrations, application-autoscaling, application-insights, application-signals, applicationcostprofiler, appmesh, apprunner, appstream, appsync, arc-region-switch, arc-zonal-shift, artifact, athena, auditmanager, autoscaling, autoscaling-plans, b2bi, backup, backup-gateway, backupsearch, batch, bcm-dashboards, bcm-data-exports, bcm-pricing-calculator, bcm-recommended-actions, bedrock, bedrock-agent, bedrock-agent-runtime, bedrock-agentcore, bedrock-agentcore-control, bedrock-data-automation, bedrock-data-automation-runtime, bedrock-runtime, billing, billingconductor, braket, budgets, ce, chatbot, chime, chime-sdk-identity, chime-sdk-media-pipelines, chime-sdk-meetings, chime-sdk-messaging, chime-sdk-voice, cleanrooms, cleanroomsml, cloud9, cloudcontrol, clouddirectory, cloudformation, cloudfront, cloudfront-keyvaluestore, cloudhsm, cloudhsmv2, cloudsearch, cloudsearchdomain, cloudtrail, cloudtrail-data, cloudwatch, codeartifact, codebuild, codecatalyst, codecommit, codeconnections, codedeploy, codeguru-reviewer, codeguru-security, codeguruprofiler, codepipeline, codestar-connections, codestar-notifications, cognito-identity, cognito-idp, cognito-sync, comprehend, comprehendmedical, compute-optimizer, compute-optimizer-automation, config, connect, connect-contact-lens, connectcampaigns, connectcampaignsv2, connectcases, connectparticipant, controlcatalog, controltower, cost-optimization-hub, cur, customer-profiles, databrew, dataexchange, datapipeline, datasync, datazone, dax, deadline, detective, devicefarm, devops-guru, directconnect, discovery, dlm, dms, docdb, docdb-elastic, drs, ds, ds-data, dsql, dynamodb, dynamodbstreams, ebs, ec2, ec2-instance-connect, ec2-mercury, ecr, ecr-public, ecs, efs, eks, eks-auth, elasticache, elasticbeanstalk, elastictranscoder, elb, elbv2, emr, emr-containers, emr-serverless, entityresolution, es, events, evidently, evs, finspace, finspace-data, firehose, fis, fms, forecast, forecastquery, frauddetector, freetier, fsx, gamelift, gameliftstreams, geo-maps, geo-places, geo-routes, glacier, globalaccelerator, glue, grafana, greengrass, greengrassv2, groundstation, guardduty, health, healthlake, iam, identitystore, imagebuilder, importexport, inspector, inspector-scan, inspector2, internetmonitor, invoicing, iot, iot-data, iot-jobs-data, iot-managed-integrations, iotanalytics, iotdeviceadvisor, iotevents, iotevents-data, iotfleetwise, iotsecuretunneling, iotsitewise, iotthingsgraph, iottwinmaker, iotwireless, ivs, ivs-realtime, ivschat, kafka, kafkaconnect, kendra, kendra-ranking, keyspaces, keyspacesstreams, kinesis, kinesis-video-archived-media, kinesis-video-media, kinesis-video-signaling, kinesis-video-webrtc-storage, kinesisanalytics, kinesisanalyticsv2, kinesisvideo, kms, lakeformation, lambda, launch-wizard, lex-models, lex-runtime, lexv2-models, lexv2-runtime, license-manager, license-manager-linux-subscriptions, license-manager-user-subscriptions, lightsail, location, logs, lookoutequipment, m2, machinelearning, macie2, mailmanager, managedblockchain, managedblockchain-query, marketplace-agreement, marketplace-catalog, marketplace-deployment, marketplace-entitlement, marketplace-reporting, marketplacecommerceanalytics, mediaconnect, mediaconvert, medialive, mediapackage, mediapackage-vod, mediapackagev2, mediastore, mediastore-data, mediatailor, medical-imaging, memorydb, meteringmarketplace, mgh, mgn, migration-hub-refactor-spaces, migrationhub-config, migrationhuborchestrator, migrationhubstrategy, mpa, mq, mturk, mwaa, mwaa-serverless, neptune, neptune-graph, neptunedata, network-firewall, networkflowmonitor, networkmanager, networkmonitor, notifications, notificationscontacts, nova-act, oam, observabilityadmin, odb, omics, opensearch, opensearchserverless, organizations, osis, outposts, panorama, partnercentral-account, partnercentral-benefits, partnercentral-channel, partnercentral-selling, payment-cryptography, payment-cryptography-data, pca-connector-ad, pca-connector-scep, pcs, personalize, personalize-events, personalize-runtime, pi, pinpoint, pinpoint-email, pinpoint-sms-voice, pinpoint-sms-voice-v2, pipes, polly, pricing, proton, qapps, qbusiness, qconnect, quicksight, ram, rbin, rds, rds-data, redshift, redshift-data, redshift-serverless, rekognition, repostspace, resiliencehub, resource-explorer-2, resource-groups, resourcegroupstaggingapi, rolesanywhere, route53, route53-recovery-cluster, route53-recovery-control-config, route53-recovery-readiness, route53domains, route53globalresolver, route53profiles, route53resolver, rtbfabric, rum, s3, s3control, s3outposts, s3tables, s3vectors, sagemaker, sagemaker-a2i-runtime, sagemaker-edge, sagemaker-featurestore-runtime, sagemaker-geospatial, sagemaker-metrics, sagemaker-runtime, savingsplans, scheduler, schemas, sdb, secretsmanager, security-ir, securityhub, securitylake, serverlessrepo, service-quotas, servicecatalog, servicecatalog-appregistry, servicediscovery, ses, sesv2, shield, signer, signin, simspaceweaver, sms-voice, snow-device-management, snowball, sns, socialmessaging, sqs, ssm, ssm-contacts, ssm-guiconnect, ssm-incidents, ssm-quicksetup, ssm-sap, sso, sso-admin, sso-oidc, stepfunctions, storagegateway, sts, supplychain, support, support-app, swf, synthetics, taxsettings, textract, timestream-influxdb, timestream-query, timestream-write, tnb, transcribe, transfer, translate, trustedadvisor, verifiedpermissions, voice-id, vpc-lattice, vpc-lattice-preview, vpc-service-network, waf, waf-regional, wafv2, wellarchitected, wickr, wisdom, workdocs, workmail, workmailmessageflow, workspaces, workspaces-instances, workspaces-thin-client, workspaces-web, xray

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_opsworks_instance`

- **Client:** `opsworks`
- **Method:** `list_instances`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Unknown service: 'opsworks'. Valid service names are: accessanalyzer, account, acm, acm-pca, aiops, amp, amplify, amplifybackend, amplifyuibuilder, apigateway, apigatewaymanagementapi, apigatewayv2, appconfig, appconfigdata, appfabric, appflow, appintegrations, application-autoscaling, application-insights, application-signals, applicationcostprofiler, appmesh, apprunner, appstream, appsync, arc-region-switch, arc-zonal-shift, artifact, athena, auditmanager, autoscaling, autoscaling-plans, b2bi, backup, backup-gateway, backupsearch, batch, bcm-dashboards, bcm-data-exports, bcm-pricing-calculator, bcm-recommended-actions, bedrock, bedrock-agent, bedrock-agent-runtime, bedrock-agentcore, bedrock-agentcore-control, bedrock-data-automation, bedrock-data-automation-runtime, bedrock-runtime, billing, billingconductor, braket, budgets, ce, chatbot, chime, chime-sdk-identity, chime-sdk-media-pipelines, chime-sdk-meetings, chime-sdk-messaging, chime-sdk-voice, cleanrooms, cleanroomsml, cloud9, cloudcontrol, clouddirectory, cloudformation, cloudfront, cloudfront-keyvaluestore, cloudhsm, cloudhsmv2, cloudsearch, cloudsearchdomain, cloudtrail, cloudtrail-data, cloudwatch, codeartifact, codebuild, codecatalyst, codecommit, codeconnections, codedeploy, codeguru-reviewer, codeguru-security, codeguruprofiler, codepipeline, codestar-connections, codestar-notifications, cognito-identity, cognito-idp, cognito-sync, comprehend, comprehendmedical, compute-optimizer, compute-optimizer-automation, config, connect, connect-contact-lens, connectcampaigns, connectcampaignsv2, connectcases, connectparticipant, controlcatalog, controltower, cost-optimization-hub, cur, customer-profiles, databrew, dataexchange, datapipeline, datasync, datazone, dax, deadline, detective, devicefarm, devops-guru, directconnect, discovery, dlm, dms, docdb, docdb-elastic, drs, ds, ds-data, dsql, dynamodb, dynamodbstreams, ebs, ec2, ec2-instance-connect, ec2-mercury, ecr, ecr-public, ecs, efs, eks, eks-auth, elasticache, elasticbeanstalk, elastictranscoder, elb, elbv2, emr, emr-containers, emr-serverless, entityresolution, es, events, evidently, evs, finspace, finspace-data, firehose, fis, fms, forecast, forecastquery, frauddetector, freetier, fsx, gamelift, gameliftstreams, geo-maps, geo-places, geo-routes, glacier, globalaccelerator, glue, grafana, greengrass, greengrassv2, groundstation, guardduty, health, healthlake, iam, identitystore, imagebuilder, importexport, inspector, inspector-scan, inspector2, internetmonitor, invoicing, iot, iot-data, iot-jobs-data, iot-managed-integrations, iotanalytics, iotdeviceadvisor, iotevents, iotevents-data, iotfleetwise, iotsecuretunneling, iotsitewise, iotthingsgraph, iottwinmaker, iotwireless, ivs, ivs-realtime, ivschat, kafka, kafkaconnect, kendra, kendra-ranking, keyspaces, keyspacesstreams, kinesis, kinesis-video-archived-media, kinesis-video-media, kinesis-video-signaling, kinesis-video-webrtc-storage, kinesisanalytics, kinesisanalyticsv2, kinesisvideo, kms, lakeformation, lambda, launch-wizard, lex-models, lex-runtime, lexv2-models, lexv2-runtime, license-manager, license-manager-linux-subscriptions, license-manager-user-subscriptions, lightsail, location, logs, lookoutequipment, m2, machinelearning, macie2, mailmanager, managedblockchain, managedblockchain-query, marketplace-agreement, marketplace-catalog, marketplace-deployment, marketplace-entitlement, marketplace-reporting, marketplacecommerceanalytics, mediaconnect, mediaconvert, medialive, mediapackage, mediapackage-vod, mediapackagev2, mediastore, mediastore-data, mediatailor, medical-imaging, memorydb, meteringmarketplace, mgh, mgn, migration-hub-refactor-spaces, migrationhub-config, migrationhuborchestrator, migrationhubstrategy, mpa, mq, mturk, mwaa, mwaa-serverless, neptune, neptune-graph, neptunedata, network-firewall, networkflowmonitor, networkmanager, networkmonitor, notifications, notificationscontacts, nova-act, oam, observabilityadmin, odb, omics, opensearch, opensearchserverless, organizations, osis, outposts, panorama, partnercentral-account, partnercentral-benefits, partnercentral-channel, partnercentral-selling, payment-cryptography, payment-cryptography-data, pca-connector-ad, pca-connector-scep, pcs, personalize, personalize-events, personalize-runtime, pi, pinpoint, pinpoint-email, pinpoint-sms-voice, pinpoint-sms-voice-v2, pipes, polly, pricing, proton, qapps, qbusiness, qconnect, quicksight, ram, rbin, rds, rds-data, redshift, redshift-data, redshift-serverless, rekognition, repostspace, resiliencehub, resource-explorer-2, resource-groups, resourcegroupstaggingapi, rolesanywhere, route53, route53-recovery-cluster, route53-recovery-control-config, route53-recovery-readiness, route53domains, route53globalresolver, route53profiles, route53resolver, rtbfabric, rum, s3, s3control, s3outposts, s3tables, s3vectors, sagemaker, sagemaker-a2i-runtime, sagemaker-edge, sagemaker-featurestore-runtime, sagemaker-geospatial, sagemaker-metrics, sagemaker-runtime, savingsplans, scheduler, schemas, sdb, secretsmanager, security-ir, securityhub, securitylake, serverlessrepo, service-quotas, servicecatalog, servicecatalog-appregistry, servicediscovery, ses, sesv2, shield, signer, signin, simspaceweaver, sms-voice, snow-device-management, snowball, sns, socialmessaging, sqs, ssm, ssm-contacts, ssm-guiconnect, ssm-incidents, ssm-quicksetup, ssm-sap, sso, sso-admin, sso-oidc, stepfunctions, storagegateway, sts, supplychain, support, support-app, swf, synthetics, taxsettings, textract, timestream-influxdb, timestream-query, timestream-write, tnb, transcribe, transfer, translate, trustedadvisor, verifiedpermissions, voice-id, vpc-lattice, vpc-lattice-preview, vpc-service-network, waf, waf-regional, wafv2, wellarchitected, wickr, wisdom, workdocs, workmail, workmailmessageflow, workspaces, workspaces-instances, workspaces-thin-client, workspaces-web, xray

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_opsworks_java_app_layer`

- **Client:** `opsworks`
- **Method:** `list_java_app_layers`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Unknown service: 'opsworks'. Valid service names are: accessanalyzer, account, acm, acm-pca, aiops, amp, amplify, amplifybackend, amplifyuibuilder, apigateway, apigatewaymanagementapi, apigatewayv2, appconfig, appconfigdata, appfabric, appflow, appintegrations, application-autoscaling, application-insights, application-signals, applicationcostprofiler, appmesh, apprunner, appstream, appsync, arc-region-switch, arc-zonal-shift, artifact, athena, auditmanager, autoscaling, autoscaling-plans, b2bi, backup, backup-gateway, backupsearch, batch, bcm-dashboards, bcm-data-exports, bcm-pricing-calculator, bcm-recommended-actions, bedrock, bedrock-agent, bedrock-agent-runtime, bedrock-agentcore, bedrock-agentcore-control, bedrock-data-automation, bedrock-data-automation-runtime, bedrock-runtime, billing, billingconductor, braket, budgets, ce, chatbot, chime, chime-sdk-identity, chime-sdk-media-pipelines, chime-sdk-meetings, chime-sdk-messaging, chime-sdk-voice, cleanrooms, cleanroomsml, cloud9, cloudcontrol, clouddirectory, cloudformation, cloudfront, cloudfront-keyvaluestore, cloudhsm, cloudhsmv2, cloudsearch, cloudsearchdomain, cloudtrail, cloudtrail-data, cloudwatch, codeartifact, codebuild, codecatalyst, codecommit, codeconnections, codedeploy, codeguru-reviewer, codeguru-security, codeguruprofiler, codepipeline, codestar-connections, codestar-notifications, cognito-identity, cognito-idp, cognito-sync, comprehend, comprehendmedical, compute-optimizer, compute-optimizer-automation, config, connect, connect-contact-lens, connectcampaigns, connectcampaignsv2, connectcases, connectparticipant, controlcatalog, controltower, cost-optimization-hub, cur, customer-profiles, databrew, dataexchange, datapipeline, datasync, datazone, dax, deadline, detective, devicefarm, devops-guru, directconnect, discovery, dlm, dms, docdb, docdb-elastic, drs, ds, ds-data, dsql, dynamodb, dynamodbstreams, ebs, ec2, ec2-instance-connect, ec2-mercury, ecr, ecr-public, ecs, efs, eks, eks-auth, elasticache, elasticbeanstalk, elastictranscoder, elb, elbv2, emr, emr-containers, emr-serverless, entityresolution, es, events, evidently, evs, finspace, finspace-data, firehose, fis, fms, forecast, forecastquery, frauddetector, freetier, fsx, gamelift, gameliftstreams, geo-maps, geo-places, geo-routes, glacier, globalaccelerator, glue, grafana, greengrass, greengrassv2, groundstation, guardduty, health, healthlake, iam, identitystore, imagebuilder, importexport, inspector, inspector-scan, inspector2, internetmonitor, invoicing, iot, iot-data, iot-jobs-data, iot-managed-integrations, iotanalytics, iotdeviceadvisor, iotevents, iotevents-data, iotfleetwise, iotsecuretunneling, iotsitewise, iotthingsgraph, iottwinmaker, iotwireless, ivs, ivs-realtime, ivschat, kafka, kafkaconnect, kendra, kendra-ranking, keyspaces, keyspacesstreams, kinesis, kinesis-video-archived-media, kinesis-video-media, kinesis-video-signaling, kinesis-video-webrtc-storage, kinesisanalytics, kinesisanalyticsv2, kinesisvideo, kms, lakeformation, lambda, launch-wizard, lex-models, lex-runtime, lexv2-models, lexv2-runtime, license-manager, license-manager-linux-subscriptions, license-manager-user-subscriptions, lightsail, location, logs, lookoutequipment, m2, machinelearning, macie2, mailmanager, managedblockchain, managedblockchain-query, marketplace-agreement, marketplace-catalog, marketplace-deployment, marketplace-entitlement, marketplace-reporting, marketplacecommerceanalytics, mediaconnect, mediaconvert, medialive, mediapackage, mediapackage-vod, mediapackagev2, mediastore, mediastore-data, mediatailor, medical-imaging, memorydb, meteringmarketplace, mgh, mgn, migration-hub-refactor-spaces, migrationhub-config, migrationhuborchestrator, migrationhubstrategy, mpa, mq, mturk, mwaa, mwaa-serverless, neptune, neptune-graph, neptunedata, network-firewall, networkflowmonitor, networkmanager, networkmonitor, notifications, notificationscontacts, nova-act, oam, observabilityadmin, odb, omics, opensearch, opensearchserverless, organizations, osis, outposts, panorama, partnercentral-account, partnercentral-benefits, partnercentral-channel, partnercentral-selling, payment-cryptography, payment-cryptography-data, pca-connector-ad, pca-connector-scep, pcs, personalize, personalize-events, personalize-runtime, pi, pinpoint, pinpoint-email, pinpoint-sms-voice, pinpoint-sms-voice-v2, pipes, polly, pricing, proton, qapps, qbusiness, qconnect, quicksight, ram, rbin, rds, rds-data, redshift, redshift-data, redshift-serverless, rekognition, repostspace, resiliencehub, resource-explorer-2, resource-groups, resourcegroupstaggingapi, rolesanywhere, route53, route53-recovery-cluster, route53-recovery-control-config, route53-recovery-readiness, route53domains, route53globalresolver, route53profiles, route53resolver, rtbfabric, rum, s3, s3control, s3outposts, s3tables, s3vectors, sagemaker, sagemaker-a2i-runtime, sagemaker-edge, sagemaker-featurestore-runtime, sagemaker-geospatial, sagemaker-metrics, sagemaker-runtime, savingsplans, scheduler, schemas, sdb, secretsmanager, security-ir, securityhub, securitylake, serverlessrepo, service-quotas, servicecatalog, servicecatalog-appregistry, servicediscovery, ses, sesv2, shield, signer, signin, simspaceweaver, sms-voice, snow-device-management, snowball, sns, socialmessaging, sqs, ssm, ssm-contacts, ssm-guiconnect, ssm-incidents, ssm-quicksetup, ssm-sap, sso, sso-admin, sso-oidc, stepfunctions, storagegateway, sts, supplychain, support, support-app, swf, synthetics, taxsettings, textract, timestream-influxdb, timestream-query, timestream-write, tnb, transcribe, transfer, translate, trustedadvisor, verifiedpermissions, voice-id, vpc-lattice, vpc-lattice-preview, vpc-service-network, waf, waf-regional, wafv2, wellarchitected, wickr, wisdom, workdocs, workmail, workmailmessageflow, workspaces, workspaces-instances, workspaces-thin-client, workspaces-web, xray

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_opsworks_memcached_layer`

- **Client:** `opsworks`
- **Method:** `list_memcached_layers`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Unknown service: 'opsworks'. Valid service names are: accessanalyzer, account, acm, acm-pca, aiops, amp, amplify, amplifybackend, amplifyuibuilder, apigateway, apigatewaymanagementapi, apigatewayv2, appconfig, appconfigdata, appfabric, appflow, appintegrations, application-autoscaling, application-insights, application-signals, applicationcostprofiler, appmesh, apprunner, appstream, appsync, arc-region-switch, arc-zonal-shift, artifact, athena, auditmanager, autoscaling, autoscaling-plans, b2bi, backup, backup-gateway, backupsearch, batch, bcm-dashboards, bcm-data-exports, bcm-pricing-calculator, bcm-recommended-actions, bedrock, bedrock-agent, bedrock-agent-runtime, bedrock-agentcore, bedrock-agentcore-control, bedrock-data-automation, bedrock-data-automation-runtime, bedrock-runtime, billing, billingconductor, braket, budgets, ce, chatbot, chime, chime-sdk-identity, chime-sdk-media-pipelines, chime-sdk-meetings, chime-sdk-messaging, chime-sdk-voice, cleanrooms, cleanroomsml, cloud9, cloudcontrol, clouddirectory, cloudformation, cloudfront, cloudfront-keyvaluestore, cloudhsm, cloudhsmv2, cloudsearch, cloudsearchdomain, cloudtrail, cloudtrail-data, cloudwatch, codeartifact, codebuild, codecatalyst, codecommit, codeconnections, codedeploy, codeguru-reviewer, codeguru-security, codeguruprofiler, codepipeline, codestar-connections, codestar-notifications, cognito-identity, cognito-idp, cognito-sync, comprehend, comprehendmedical, compute-optimizer, compute-optimizer-automation, config, connect, connect-contact-lens, connectcampaigns, connectcampaignsv2, connectcases, connectparticipant, controlcatalog, controltower, cost-optimization-hub, cur, customer-profiles, databrew, dataexchange, datapipeline, datasync, datazone, dax, deadline, detective, devicefarm, devops-guru, directconnect, discovery, dlm, dms, docdb, docdb-elastic, drs, ds, ds-data, dsql, dynamodb, dynamodbstreams, ebs, ec2, ec2-instance-connect, ec2-mercury, ecr, ecr-public, ecs, efs, eks, eks-auth, elasticache, elasticbeanstalk, elastictranscoder, elb, elbv2, emr, emr-containers, emr-serverless, entityresolution, es, events, evidently, evs, finspace, finspace-data, firehose, fis, fms, forecast, forecastquery, frauddetector, freetier, fsx, gamelift, gameliftstreams, geo-maps, geo-places, geo-routes, glacier, globalaccelerator, glue, grafana, greengrass, greengrassv2, groundstation, guardduty, health, healthlake, iam, identitystore, imagebuilder, importexport, inspector, inspector-scan, inspector2, internetmonitor, invoicing, iot, iot-data, iot-jobs-data, iot-managed-integrations, iotanalytics, iotdeviceadvisor, iotevents, iotevents-data, iotfleetwise, iotsecuretunneling, iotsitewise, iotthingsgraph, iottwinmaker, iotwireless, ivs, ivs-realtime, ivschat, kafka, kafkaconnect, kendra, kendra-ranking, keyspaces, keyspacesstreams, kinesis, kinesis-video-archived-media, kinesis-video-media, kinesis-video-signaling, kinesis-video-webrtc-storage, kinesisanalytics, kinesisanalyticsv2, kinesisvideo, kms, lakeformation, lambda, launch-wizard, lex-models, lex-runtime, lexv2-models, lexv2-runtime, license-manager, license-manager-linux-subscriptions, license-manager-user-subscriptions, lightsail, location, logs, lookoutequipment, m2, machinelearning, macie2, mailmanager, managedblockchain, managedblockchain-query, marketplace-agreement, marketplace-catalog, marketplace-deployment, marketplace-entitlement, marketplace-reporting, marketplacecommerceanalytics, mediaconnect, mediaconvert, medialive, mediapackage, mediapackage-vod, mediapackagev2, mediastore, mediastore-data, mediatailor, medical-imaging, memorydb, meteringmarketplace, mgh, mgn, migration-hub-refactor-spaces, migrationhub-config, migrationhuborchestrator, migrationhubstrategy, mpa, mq, mturk, mwaa, mwaa-serverless, neptune, neptune-graph, neptunedata, network-firewall, networkflowmonitor, networkmanager, networkmonitor, notifications, notificationscontacts, nova-act, oam, observabilityadmin, odb, omics, opensearch, opensearchserverless, organizations, osis, outposts, panorama, partnercentral-account, partnercentral-benefits, partnercentral-channel, partnercentral-selling, payment-cryptography, payment-cryptography-data, pca-connector-ad, pca-connector-scep, pcs, personalize, personalize-events, personalize-runtime, pi, pinpoint, pinpoint-email, pinpoint-sms-voice, pinpoint-sms-voice-v2, pipes, polly, pricing, proton, qapps, qbusiness, qconnect, quicksight, ram, rbin, rds, rds-data, redshift, redshift-data, redshift-serverless, rekognition, repostspace, resiliencehub, resource-explorer-2, resource-groups, resourcegroupstaggingapi, rolesanywhere, route53, route53-recovery-cluster, route53-recovery-control-config, route53-recovery-readiness, route53domains, route53globalresolver, route53profiles, route53resolver, rtbfabric, rum, s3, s3control, s3outposts, s3tables, s3vectors, sagemaker, sagemaker-a2i-runtime, sagemaker-edge, sagemaker-featurestore-runtime, sagemaker-geospatial, sagemaker-metrics, sagemaker-runtime, savingsplans, scheduler, schemas, sdb, secretsmanager, security-ir, securityhub, securitylake, serverlessrepo, service-quotas, servicecatalog, servicecatalog-appregistry, servicediscovery, ses, sesv2, shield, signer, signin, simspaceweaver, sms-voice, snow-device-management, snowball, sns, socialmessaging, sqs, ssm, ssm-contacts, ssm-guiconnect, ssm-incidents, ssm-quicksetup, ssm-sap, sso, sso-admin, sso-oidc, stepfunctions, storagegateway, sts, supplychain, support, support-app, swf, synthetics, taxsettings, textract, timestream-influxdb, timestream-query, timestream-write, tnb, transcribe, transfer, translate, trustedadvisor, verifiedpermissions, voice-id, vpc-lattice, vpc-lattice-preview, vpc-service-network, waf, waf-regional, wafv2, wellarchitected, wickr, wisdom, workdocs, workmail, workmailmessageflow, workspaces, workspaces-instances, workspaces-thin-client, workspaces-web, xray

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_opsworks_mysql_layer`

- **Client:** `opsworks`
- **Method:** `list_mysql_layers`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Unknown service: 'opsworks'. Valid service names are: accessanalyzer, account, acm, acm-pca, aiops, amp, amplify, amplifybackend, amplifyuibuilder, apigateway, apigatewaymanagementapi, apigatewayv2, appconfig, appconfigdata, appfabric, appflow, appintegrations, application-autoscaling, application-insights, application-signals, applicationcostprofiler, appmesh, apprunner, appstream, appsync, arc-region-switch, arc-zonal-shift, artifact, athena, auditmanager, autoscaling, autoscaling-plans, b2bi, backup, backup-gateway, backupsearch, batch, bcm-dashboards, bcm-data-exports, bcm-pricing-calculator, bcm-recommended-actions, bedrock, bedrock-agent, bedrock-agent-runtime, bedrock-agentcore, bedrock-agentcore-control, bedrock-data-automation, bedrock-data-automation-runtime, bedrock-runtime, billing, billingconductor, braket, budgets, ce, chatbot, chime, chime-sdk-identity, chime-sdk-media-pipelines, chime-sdk-meetings, chime-sdk-messaging, chime-sdk-voice, cleanrooms, cleanroomsml, cloud9, cloudcontrol, clouddirectory, cloudformation, cloudfront, cloudfront-keyvaluestore, cloudhsm, cloudhsmv2, cloudsearch, cloudsearchdomain, cloudtrail, cloudtrail-data, cloudwatch, codeartifact, codebuild, codecatalyst, codecommit, codeconnections, codedeploy, codeguru-reviewer, codeguru-security, codeguruprofiler, codepipeline, codestar-connections, codestar-notifications, cognito-identity, cognito-idp, cognito-sync, comprehend, comprehendmedical, compute-optimizer, compute-optimizer-automation, config, connect, connect-contact-lens, connectcampaigns, connectcampaignsv2, connectcases, connectparticipant, controlcatalog, controltower, cost-optimization-hub, cur, customer-profiles, databrew, dataexchange, datapipeline, datasync, datazone, dax, deadline, detective, devicefarm, devops-guru, directconnect, discovery, dlm, dms, docdb, docdb-elastic, drs, ds, ds-data, dsql, dynamodb, dynamodbstreams, ebs, ec2, ec2-instance-connect, ec2-mercury, ecr, ecr-public, ecs, efs, eks, eks-auth, elasticache, elasticbeanstalk, elastictranscoder, elb, elbv2, emr, emr-containers, emr-serverless, entityresolution, es, events, evidently, evs, finspace, finspace-data, firehose, fis, fms, forecast, forecastquery, frauddetector, freetier, fsx, gamelift, gameliftstreams, geo-maps, geo-places, geo-routes, glacier, globalaccelerator, glue, grafana, greengrass, greengrassv2, groundstation, guardduty, health, healthlake, iam, identitystore, imagebuilder, importexport, inspector, inspector-scan, inspector2, internetmonitor, invoicing, iot, iot-data, iot-jobs-data, iot-managed-integrations, iotanalytics, iotdeviceadvisor, iotevents, iotevents-data, iotfleetwise, iotsecuretunneling, iotsitewise, iotthingsgraph, iottwinmaker, iotwireless, ivs, ivs-realtime, ivschat, kafka, kafkaconnect, kendra, kendra-ranking, keyspaces, keyspacesstreams, kinesis, kinesis-video-archived-media, kinesis-video-media, kinesis-video-signaling, kinesis-video-webrtc-storage, kinesisanalytics, kinesisanalyticsv2, kinesisvideo, kms, lakeformation, lambda, launch-wizard, lex-models, lex-runtime, lexv2-models, lexv2-runtime, license-manager, license-manager-linux-subscriptions, license-manager-user-subscriptions, lightsail, location, logs, lookoutequipment, m2, machinelearning, macie2, mailmanager, managedblockchain, managedblockchain-query, marketplace-agreement, marketplace-catalog, marketplace-deployment, marketplace-entitlement, marketplace-reporting, marketplacecommerceanalytics, mediaconnect, mediaconvert, medialive, mediapackage, mediapackage-vod, mediapackagev2, mediastore, mediastore-data, mediatailor, medical-imaging, memorydb, meteringmarketplace, mgh, mgn, migration-hub-refactor-spaces, migrationhub-config, migrationhuborchestrator, migrationhubstrategy, mpa, mq, mturk, mwaa, mwaa-serverless, neptune, neptune-graph, neptunedata, network-firewall, networkflowmonitor, networkmanager, networkmonitor, notifications, notificationscontacts, nova-act, oam, observabilityadmin, odb, omics, opensearch, opensearchserverless, organizations, osis, outposts, panorama, partnercentral-account, partnercentral-benefits, partnercentral-channel, partnercentral-selling, payment-cryptography, payment-cryptography-data, pca-connector-ad, pca-connector-scep, pcs, personalize, personalize-events, personalize-runtime, pi, pinpoint, pinpoint-email, pinpoint-sms-voice, pinpoint-sms-voice-v2, pipes, polly, pricing, proton, qapps, qbusiness, qconnect, quicksight, ram, rbin, rds, rds-data, redshift, redshift-data, redshift-serverless, rekognition, repostspace, resiliencehub, resource-explorer-2, resource-groups, resourcegroupstaggingapi, rolesanywhere, route53, route53-recovery-cluster, route53-recovery-control-config, route53-recovery-readiness, route53domains, route53globalresolver, route53profiles, route53resolver, rtbfabric, rum, s3, s3control, s3outposts, s3tables, s3vectors, sagemaker, sagemaker-a2i-runtime, sagemaker-edge, sagemaker-featurestore-runtime, sagemaker-geospatial, sagemaker-metrics, sagemaker-runtime, savingsplans, scheduler, schemas, sdb, secretsmanager, security-ir, securityhub, securitylake, serverlessrepo, service-quotas, servicecatalog, servicecatalog-appregistry, servicediscovery, ses, sesv2, shield, signer, signin, simspaceweaver, sms-voice, snow-device-management, snowball, sns, socialmessaging, sqs, ssm, ssm-contacts, ssm-guiconnect, ssm-incidents, ssm-quicksetup, ssm-sap, sso, sso-admin, sso-oidc, stepfunctions, storagegateway, sts, supplychain, support, support-app, swf, synthetics, taxsettings, textract, timestream-influxdb, timestream-query, timestream-write, tnb, transcribe, transfer, translate, trustedadvisor, verifiedpermissions, voice-id, vpc-lattice, vpc-lattice-preview, vpc-service-network, waf, waf-regional, wafv2, wellarchitected, wickr, wisdom, workdocs, workmail, workmailmessageflow, workspaces, workspaces-instances, workspaces-thin-client, workspaces-web, xray

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_opsworks_nodejs_app_layer`

- **Client:** `opsworks`
- **Method:** `list_nodejs_app_layers`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Unknown service: 'opsworks'. Valid service names are: accessanalyzer, account, acm, acm-pca, aiops, amp, amplify, amplifybackend, amplifyuibuilder, apigateway, apigatewaymanagementapi, apigatewayv2, appconfig, appconfigdata, appfabric, appflow, appintegrations, application-autoscaling, application-insights, application-signals, applicationcostprofiler, appmesh, apprunner, appstream, appsync, arc-region-switch, arc-zonal-shift, artifact, athena, auditmanager, autoscaling, autoscaling-plans, b2bi, backup, backup-gateway, backupsearch, batch, bcm-dashboards, bcm-data-exports, bcm-pricing-calculator, bcm-recommended-actions, bedrock, bedrock-agent, bedrock-agent-runtime, bedrock-agentcore, bedrock-agentcore-control, bedrock-data-automation, bedrock-data-automation-runtime, bedrock-runtime, billing, billingconductor, braket, budgets, ce, chatbot, chime, chime-sdk-identity, chime-sdk-media-pipelines, chime-sdk-meetings, chime-sdk-messaging, chime-sdk-voice, cleanrooms, cleanroomsml, cloud9, cloudcontrol, clouddirectory, cloudformation, cloudfront, cloudfront-keyvaluestore, cloudhsm, cloudhsmv2, cloudsearch, cloudsearchdomain, cloudtrail, cloudtrail-data, cloudwatch, codeartifact, codebuild, codecatalyst, codecommit, codeconnections, codedeploy, codeguru-reviewer, codeguru-security, codeguruprofiler, codepipeline, codestar-connections, codestar-notifications, cognito-identity, cognito-idp, cognito-sync, comprehend, comprehendmedical, compute-optimizer, compute-optimizer-automation, config, connect, connect-contact-lens, connectcampaigns, connectcampaignsv2, connectcases, connectparticipant, controlcatalog, controltower, cost-optimization-hub, cur, customer-profiles, databrew, dataexchange, datapipeline, datasync, datazone, dax, deadline, detective, devicefarm, devops-guru, directconnect, discovery, dlm, dms, docdb, docdb-elastic, drs, ds, ds-data, dsql, dynamodb, dynamodbstreams, ebs, ec2, ec2-instance-connect, ec2-mercury, ecr, ecr-public, ecs, efs, eks, eks-auth, elasticache, elasticbeanstalk, elastictranscoder, elb, elbv2, emr, emr-containers, emr-serverless, entityresolution, es, events, evidently, evs, finspace, finspace-data, firehose, fis, fms, forecast, forecastquery, frauddetector, freetier, fsx, gamelift, gameliftstreams, geo-maps, geo-places, geo-routes, glacier, globalaccelerator, glue, grafana, greengrass, greengrassv2, groundstation, guardduty, health, healthlake, iam, identitystore, imagebuilder, importexport, inspector, inspector-scan, inspector2, internetmonitor, invoicing, iot, iot-data, iot-jobs-data, iot-managed-integrations, iotanalytics, iotdeviceadvisor, iotevents, iotevents-data, iotfleetwise, iotsecuretunneling, iotsitewise, iotthingsgraph, iottwinmaker, iotwireless, ivs, ivs-realtime, ivschat, kafka, kafkaconnect, kendra, kendra-ranking, keyspaces, keyspacesstreams, kinesis, kinesis-video-archived-media, kinesis-video-media, kinesis-video-signaling, kinesis-video-webrtc-storage, kinesisanalytics, kinesisanalyticsv2, kinesisvideo, kms, lakeformation, lambda, launch-wizard, lex-models, lex-runtime, lexv2-models, lexv2-runtime, license-manager, license-manager-linux-subscriptions, license-manager-user-subscriptions, lightsail, location, logs, lookoutequipment, m2, machinelearning, macie2, mailmanager, managedblockchain, managedblockchain-query, marketplace-agreement, marketplace-catalog, marketplace-deployment, marketplace-entitlement, marketplace-reporting, marketplacecommerceanalytics, mediaconnect, mediaconvert, medialive, mediapackage, mediapackage-vod, mediapackagev2, mediastore, mediastore-data, mediatailor, medical-imaging, memorydb, meteringmarketplace, mgh, mgn, migration-hub-refactor-spaces, migrationhub-config, migrationhuborchestrator, migrationhubstrategy, mpa, mq, mturk, mwaa, mwaa-serverless, neptune, neptune-graph, neptunedata, network-firewall, networkflowmonitor, networkmanager, networkmonitor, notifications, notificationscontacts, nova-act, oam, observabilityadmin, odb, omics, opensearch, opensearchserverless, organizations, osis, outposts, panorama, partnercentral-account, partnercentral-benefits, partnercentral-channel, partnercentral-selling, payment-cryptography, payment-cryptography-data, pca-connector-ad, pca-connector-scep, pcs, personalize, personalize-events, personalize-runtime, pi, pinpoint, pinpoint-email, pinpoint-sms-voice, pinpoint-sms-voice-v2, pipes, polly, pricing, proton, qapps, qbusiness, qconnect, quicksight, ram, rbin, rds, rds-data, redshift, redshift-data, redshift-serverless, rekognition, repostspace, resiliencehub, resource-explorer-2, resource-groups, resourcegroupstaggingapi, rolesanywhere, route53, route53-recovery-cluster, route53-recovery-control-config, route53-recovery-readiness, route53domains, route53globalresolver, route53profiles, route53resolver, rtbfabric, rum, s3, s3control, s3outposts, s3tables, s3vectors, sagemaker, sagemaker-a2i-runtime, sagemaker-edge, sagemaker-featurestore-runtime, sagemaker-geospatial, sagemaker-metrics, sagemaker-runtime, savingsplans, scheduler, schemas, sdb, secretsmanager, security-ir, securityhub, securitylake, serverlessrepo, service-quotas, servicecatalog, servicecatalog-appregistry, servicediscovery, ses, sesv2, shield, signer, signin, simspaceweaver, sms-voice, snow-device-management, snowball, sns, socialmessaging, sqs, ssm, ssm-contacts, ssm-guiconnect, ssm-incidents, ssm-quicksetup, ssm-sap, sso, sso-admin, sso-oidc, stepfunctions, storagegateway, sts, supplychain, support, support-app, swf, synthetics, taxsettings, textract, timestream-influxdb, timestream-query, timestream-write, tnb, transcribe, transfer, translate, trustedadvisor, verifiedpermissions, voice-id, vpc-lattice, vpc-lattice-preview, vpc-service-network, waf, waf-regional, wafv2, wellarchitected, wickr, wisdom, workdocs, workmail, workmailmessageflow, workspaces, workspaces-instances, workspaces-thin-client, workspaces-web, xray

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_opsworks_permission`

- **Client:** `opsworks`
- **Method:** `list_permissions`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Unknown service: 'opsworks'. Valid service names are: accessanalyzer, account, acm, acm-pca, aiops, amp, amplify, amplifybackend, amplifyuibuilder, apigateway, apigatewaymanagementapi, apigatewayv2, appconfig, appconfigdata, appfabric, appflow, appintegrations, application-autoscaling, application-insights, application-signals, applicationcostprofiler, appmesh, apprunner, appstream, appsync, arc-region-switch, arc-zonal-shift, artifact, athena, auditmanager, autoscaling, autoscaling-plans, b2bi, backup, backup-gateway, backupsearch, batch, bcm-dashboards, bcm-data-exports, bcm-pricing-calculator, bcm-recommended-actions, bedrock, bedrock-agent, bedrock-agent-runtime, bedrock-agentcore, bedrock-agentcore-control, bedrock-data-automation, bedrock-data-automation-runtime, bedrock-runtime, billing, billingconductor, braket, budgets, ce, chatbot, chime, chime-sdk-identity, chime-sdk-media-pipelines, chime-sdk-meetings, chime-sdk-messaging, chime-sdk-voice, cleanrooms, cleanroomsml, cloud9, cloudcontrol, clouddirectory, cloudformation, cloudfront, cloudfront-keyvaluestore, cloudhsm, cloudhsmv2, cloudsearch, cloudsearchdomain, cloudtrail, cloudtrail-data, cloudwatch, codeartifact, codebuild, codecatalyst, codecommit, codeconnections, codedeploy, codeguru-reviewer, codeguru-security, codeguruprofiler, codepipeline, codestar-connections, codestar-notifications, cognito-identity, cognito-idp, cognito-sync, comprehend, comprehendmedical, compute-optimizer, compute-optimizer-automation, config, connect, connect-contact-lens, connectcampaigns, connectcampaignsv2, connectcases, connectparticipant, controlcatalog, controltower, cost-optimization-hub, cur, customer-profiles, databrew, dataexchange, datapipeline, datasync, datazone, dax, deadline, detective, devicefarm, devops-guru, directconnect, discovery, dlm, dms, docdb, docdb-elastic, drs, ds, ds-data, dsql, dynamodb, dynamodbstreams, ebs, ec2, ec2-instance-connect, ec2-mercury, ecr, ecr-public, ecs, efs, eks, eks-auth, elasticache, elasticbeanstalk, elastictranscoder, elb, elbv2, emr, emr-containers, emr-serverless, entityresolution, es, events, evidently, evs, finspace, finspace-data, firehose, fis, fms, forecast, forecastquery, frauddetector, freetier, fsx, gamelift, gameliftstreams, geo-maps, geo-places, geo-routes, glacier, globalaccelerator, glue, grafana, greengrass, greengrassv2, groundstation, guardduty, health, healthlake, iam, identitystore, imagebuilder, importexport, inspector, inspector-scan, inspector2, internetmonitor, invoicing, iot, iot-data, iot-jobs-data, iot-managed-integrations, iotanalytics, iotdeviceadvisor, iotevents, iotevents-data, iotfleetwise, iotsecuretunneling, iotsitewise, iotthingsgraph, iottwinmaker, iotwireless, ivs, ivs-realtime, ivschat, kafka, kafkaconnect, kendra, kendra-ranking, keyspaces, keyspacesstreams, kinesis, kinesis-video-archived-media, kinesis-video-media, kinesis-video-signaling, kinesis-video-webrtc-storage, kinesisanalytics, kinesisanalyticsv2, kinesisvideo, kms, lakeformation, lambda, launch-wizard, lex-models, lex-runtime, lexv2-models, lexv2-runtime, license-manager, license-manager-linux-subscriptions, license-manager-user-subscriptions, lightsail, location, logs, lookoutequipment, m2, machinelearning, macie2, mailmanager, managedblockchain, managedblockchain-query, marketplace-agreement, marketplace-catalog, marketplace-deployment, marketplace-entitlement, marketplace-reporting, marketplacecommerceanalytics, mediaconnect, mediaconvert, medialive, mediapackage, mediapackage-vod, mediapackagev2, mediastore, mediastore-data, mediatailor, medical-imaging, memorydb, meteringmarketplace, mgh, mgn, migration-hub-refactor-spaces, migrationhub-config, migrationhuborchestrator, migrationhubstrategy, mpa, mq, mturk, mwaa, mwaa-serverless, neptune, neptune-graph, neptunedata, network-firewall, networkflowmonitor, networkmanager, networkmonitor, notifications, notificationscontacts, nova-act, oam, observabilityadmin, odb, omics, opensearch, opensearchserverless, organizations, osis, outposts, panorama, partnercentral-account, partnercentral-benefits, partnercentral-channel, partnercentral-selling, payment-cryptography, payment-cryptography-data, pca-connector-ad, pca-connector-scep, pcs, personalize, personalize-events, personalize-runtime, pi, pinpoint, pinpoint-email, pinpoint-sms-voice, pinpoint-sms-voice-v2, pipes, polly, pricing, proton, qapps, qbusiness, qconnect, quicksight, ram, rbin, rds, rds-data, redshift, redshift-data, redshift-serverless, rekognition, repostspace, resiliencehub, resource-explorer-2, resource-groups, resourcegroupstaggingapi, rolesanywhere, route53, route53-recovery-cluster, route53-recovery-control-config, route53-recovery-readiness, route53domains, route53globalresolver, route53profiles, route53resolver, rtbfabric, rum, s3, s3control, s3outposts, s3tables, s3vectors, sagemaker, sagemaker-a2i-runtime, sagemaker-edge, sagemaker-featurestore-runtime, sagemaker-geospatial, sagemaker-metrics, sagemaker-runtime, savingsplans, scheduler, schemas, sdb, secretsmanager, security-ir, securityhub, securitylake, serverlessrepo, service-quotas, servicecatalog, servicecatalog-appregistry, servicediscovery, ses, sesv2, shield, signer, signin, simspaceweaver, sms-voice, snow-device-management, snowball, sns, socialmessaging, sqs, ssm, ssm-contacts, ssm-guiconnect, ssm-incidents, ssm-quicksetup, ssm-sap, sso, sso-admin, sso-oidc, stepfunctions, storagegateway, sts, supplychain, support, support-app, swf, synthetics, taxsettings, textract, timestream-influxdb, timestream-query, timestream-write, tnb, transcribe, transfer, translate, trustedadvisor, verifiedpermissions, voice-id, vpc-lattice, vpc-lattice-preview, vpc-service-network, waf, waf-regional, wafv2, wellarchitected, wickr, wisdom, workdocs, workmail, workmailmessageflow, workspaces, workspaces-instances, workspaces-thin-client, workspaces-web, xray

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_opsworks_php_app_layer`

- **Client:** `opsworks`
- **Method:** `list_php_app_layers`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Unknown service: 'opsworks'. Valid service names are: accessanalyzer, account, acm, acm-pca, aiops, amp, amplify, amplifybackend, amplifyuibuilder, apigateway, apigatewaymanagementapi, apigatewayv2, appconfig, appconfigdata, appfabric, appflow, appintegrations, application-autoscaling, application-insights, application-signals, applicationcostprofiler, appmesh, apprunner, appstream, appsync, arc-region-switch, arc-zonal-shift, artifact, athena, auditmanager, autoscaling, autoscaling-plans, b2bi, backup, backup-gateway, backupsearch, batch, bcm-dashboards, bcm-data-exports, bcm-pricing-calculator, bcm-recommended-actions, bedrock, bedrock-agent, bedrock-agent-runtime, bedrock-agentcore, bedrock-agentcore-control, bedrock-data-automation, bedrock-data-automation-runtime, bedrock-runtime, billing, billingconductor, braket, budgets, ce, chatbot, chime, chime-sdk-identity, chime-sdk-media-pipelines, chime-sdk-meetings, chime-sdk-messaging, chime-sdk-voice, cleanrooms, cleanroomsml, cloud9, cloudcontrol, clouddirectory, cloudformation, cloudfront, cloudfront-keyvaluestore, cloudhsm, cloudhsmv2, cloudsearch, cloudsearchdomain, cloudtrail, cloudtrail-data, cloudwatch, codeartifact, codebuild, codecatalyst, codecommit, codeconnections, codedeploy, codeguru-reviewer, codeguru-security, codeguruprofiler, codepipeline, codestar-connections, codestar-notifications, cognito-identity, cognito-idp, cognito-sync, comprehend, comprehendmedical, compute-optimizer, compute-optimizer-automation, config, connect, connect-contact-lens, connectcampaigns, connectcampaignsv2, connectcases, connectparticipant, controlcatalog, controltower, cost-optimization-hub, cur, customer-profiles, databrew, dataexchange, datapipeline, datasync, datazone, dax, deadline, detective, devicefarm, devops-guru, directconnect, discovery, dlm, dms, docdb, docdb-elastic, drs, ds, ds-data, dsql, dynamodb, dynamodbstreams, ebs, ec2, ec2-instance-connect, ec2-mercury, ecr, ecr-public, ecs, efs, eks, eks-auth, elasticache, elasticbeanstalk, elastictranscoder, elb, elbv2, emr, emr-containers, emr-serverless, entityresolution, es, events, evidently, evs, finspace, finspace-data, firehose, fis, fms, forecast, forecastquery, frauddetector, freetier, fsx, gamelift, gameliftstreams, geo-maps, geo-places, geo-routes, glacier, globalaccelerator, glue, grafana, greengrass, greengrassv2, groundstation, guardduty, health, healthlake, iam, identitystore, imagebuilder, importexport, inspector, inspector-scan, inspector2, internetmonitor, invoicing, iot, iot-data, iot-jobs-data, iot-managed-integrations, iotanalytics, iotdeviceadvisor, iotevents, iotevents-data, iotfleetwise, iotsecuretunneling, iotsitewise, iotthingsgraph, iottwinmaker, iotwireless, ivs, ivs-realtime, ivschat, kafka, kafkaconnect, kendra, kendra-ranking, keyspaces, keyspacesstreams, kinesis, kinesis-video-archived-media, kinesis-video-media, kinesis-video-signaling, kinesis-video-webrtc-storage, kinesisanalytics, kinesisanalyticsv2, kinesisvideo, kms, lakeformation, lambda, launch-wizard, lex-models, lex-runtime, lexv2-models, lexv2-runtime, license-manager, license-manager-linux-subscriptions, license-manager-user-subscriptions, lightsail, location, logs, lookoutequipment, m2, machinelearning, macie2, mailmanager, managedblockchain, managedblockchain-query, marketplace-agreement, marketplace-catalog, marketplace-deployment, marketplace-entitlement, marketplace-reporting, marketplacecommerceanalytics, mediaconnect, mediaconvert, medialive, mediapackage, mediapackage-vod, mediapackagev2, mediastore, mediastore-data, mediatailor, medical-imaging, memorydb, meteringmarketplace, mgh, mgn, migration-hub-refactor-spaces, migrationhub-config, migrationhuborchestrator, migrationhubstrategy, mpa, mq, mturk, mwaa, mwaa-serverless, neptune, neptune-graph, neptunedata, network-firewall, networkflowmonitor, networkmanager, networkmonitor, notifications, notificationscontacts, nova-act, oam, observabilityadmin, odb, omics, opensearch, opensearchserverless, organizations, osis, outposts, panorama, partnercentral-account, partnercentral-benefits, partnercentral-channel, partnercentral-selling, payment-cryptography, payment-cryptography-data, pca-connector-ad, pca-connector-scep, pcs, personalize, personalize-events, personalize-runtime, pi, pinpoint, pinpoint-email, pinpoint-sms-voice, pinpoint-sms-voice-v2, pipes, polly, pricing, proton, qapps, qbusiness, qconnect, quicksight, ram, rbin, rds, rds-data, redshift, redshift-data, redshift-serverless, rekognition, repostspace, resiliencehub, resource-explorer-2, resource-groups, resourcegroupstaggingapi, rolesanywhere, route53, route53-recovery-cluster, route53-recovery-control-config, route53-recovery-readiness, route53domains, route53globalresolver, route53profiles, route53resolver, rtbfabric, rum, s3, s3control, s3outposts, s3tables, s3vectors, sagemaker, sagemaker-a2i-runtime, sagemaker-edge, sagemaker-featurestore-runtime, sagemaker-geospatial, sagemaker-metrics, sagemaker-runtime, savingsplans, scheduler, schemas, sdb, secretsmanager, security-ir, securityhub, securitylake, serverlessrepo, service-quotas, servicecatalog, servicecatalog-appregistry, servicediscovery, ses, sesv2, shield, signer, signin, simspaceweaver, sms-voice, snow-device-management, snowball, sns, socialmessaging, sqs, ssm, ssm-contacts, ssm-guiconnect, ssm-incidents, ssm-quicksetup, ssm-sap, sso, sso-admin, sso-oidc, stepfunctions, storagegateway, sts, supplychain, support, support-app, swf, synthetics, taxsettings, textract, timestream-influxdb, timestream-query, timestream-write, tnb, transcribe, transfer, translate, trustedadvisor, verifiedpermissions, voice-id, vpc-lattice, vpc-lattice-preview, vpc-service-network, waf, waf-regional, wafv2, wellarchitected, wickr, wisdom, workdocs, workmail, workmailmessageflow, workspaces, workspaces-instances, workspaces-thin-client, workspaces-web, xray

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_opsworks_rails_app_layer`

- **Client:** `opsworks`
- **Method:** `list_rails_app_layers`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Unknown service: 'opsworks'. Valid service names are: accessanalyzer, account, acm, acm-pca, aiops, amp, amplify, amplifybackend, amplifyuibuilder, apigateway, apigatewaymanagementapi, apigatewayv2, appconfig, appconfigdata, appfabric, appflow, appintegrations, application-autoscaling, application-insights, application-signals, applicationcostprofiler, appmesh, apprunner, appstream, appsync, arc-region-switch, arc-zonal-shift, artifact, athena, auditmanager, autoscaling, autoscaling-plans, b2bi, backup, backup-gateway, backupsearch, batch, bcm-dashboards, bcm-data-exports, bcm-pricing-calculator, bcm-recommended-actions, bedrock, bedrock-agent, bedrock-agent-runtime, bedrock-agentcore, bedrock-agentcore-control, bedrock-data-automation, bedrock-data-automation-runtime, bedrock-runtime, billing, billingconductor, braket, budgets, ce, chatbot, chime, chime-sdk-identity, chime-sdk-media-pipelines, chime-sdk-meetings, chime-sdk-messaging, chime-sdk-voice, cleanrooms, cleanroomsml, cloud9, cloudcontrol, clouddirectory, cloudformation, cloudfront, cloudfront-keyvaluestore, cloudhsm, cloudhsmv2, cloudsearch, cloudsearchdomain, cloudtrail, cloudtrail-data, cloudwatch, codeartifact, codebuild, codecatalyst, codecommit, codeconnections, codedeploy, codeguru-reviewer, codeguru-security, codeguruprofiler, codepipeline, codestar-connections, codestar-notifications, cognito-identity, cognito-idp, cognito-sync, comprehend, comprehendmedical, compute-optimizer, compute-optimizer-automation, config, connect, connect-contact-lens, connectcampaigns, connectcampaignsv2, connectcases, connectparticipant, controlcatalog, controltower, cost-optimization-hub, cur, customer-profiles, databrew, dataexchange, datapipeline, datasync, datazone, dax, deadline, detective, devicefarm, devops-guru, directconnect, discovery, dlm, dms, docdb, docdb-elastic, drs, ds, ds-data, dsql, dynamodb, dynamodbstreams, ebs, ec2, ec2-instance-connect, ec2-mercury, ecr, ecr-public, ecs, efs, eks, eks-auth, elasticache, elasticbeanstalk, elastictranscoder, elb, elbv2, emr, emr-containers, emr-serverless, entityresolution, es, events, evidently, evs, finspace, finspace-data, firehose, fis, fms, forecast, forecastquery, frauddetector, freetier, fsx, gamelift, gameliftstreams, geo-maps, geo-places, geo-routes, glacier, globalaccelerator, glue, grafana, greengrass, greengrassv2, groundstation, guardduty, health, healthlake, iam, identitystore, imagebuilder, importexport, inspector, inspector-scan, inspector2, internetmonitor, invoicing, iot, iot-data, iot-jobs-data, iot-managed-integrations, iotanalytics, iotdeviceadvisor, iotevents, iotevents-data, iotfleetwise, iotsecuretunneling, iotsitewise, iotthingsgraph, iottwinmaker, iotwireless, ivs, ivs-realtime, ivschat, kafka, kafkaconnect, kendra, kendra-ranking, keyspaces, keyspacesstreams, kinesis, kinesis-video-archived-media, kinesis-video-media, kinesis-video-signaling, kinesis-video-webrtc-storage, kinesisanalytics, kinesisanalyticsv2, kinesisvideo, kms, lakeformation, lambda, launch-wizard, lex-models, lex-runtime, lexv2-models, lexv2-runtime, license-manager, license-manager-linux-subscriptions, license-manager-user-subscriptions, lightsail, location, logs, lookoutequipment, m2, machinelearning, macie2, mailmanager, managedblockchain, managedblockchain-query, marketplace-agreement, marketplace-catalog, marketplace-deployment, marketplace-entitlement, marketplace-reporting, marketplacecommerceanalytics, mediaconnect, mediaconvert, medialive, mediapackage, mediapackage-vod, mediapackagev2, mediastore, mediastore-data, mediatailor, medical-imaging, memorydb, meteringmarketplace, mgh, mgn, migration-hub-refactor-spaces, migrationhub-config, migrationhuborchestrator, migrationhubstrategy, mpa, mq, mturk, mwaa, mwaa-serverless, neptune, neptune-graph, neptunedata, network-firewall, networkflowmonitor, networkmanager, networkmonitor, notifications, notificationscontacts, nova-act, oam, observabilityadmin, odb, omics, opensearch, opensearchserverless, organizations, osis, outposts, panorama, partnercentral-account, partnercentral-benefits, partnercentral-channel, partnercentral-selling, payment-cryptography, payment-cryptography-data, pca-connector-ad, pca-connector-scep, pcs, personalize, personalize-events, personalize-runtime, pi, pinpoint, pinpoint-email, pinpoint-sms-voice, pinpoint-sms-voice-v2, pipes, polly, pricing, proton, qapps, qbusiness, qconnect, quicksight, ram, rbin, rds, rds-data, redshift, redshift-data, redshift-serverless, rekognition, repostspace, resiliencehub, resource-explorer-2, resource-groups, resourcegroupstaggingapi, rolesanywhere, route53, route53-recovery-cluster, route53-recovery-control-config, route53-recovery-readiness, route53domains, route53globalresolver, route53profiles, route53resolver, rtbfabric, rum, s3, s3control, s3outposts, s3tables, s3vectors, sagemaker, sagemaker-a2i-runtime, sagemaker-edge, sagemaker-featurestore-runtime, sagemaker-geospatial, sagemaker-metrics, sagemaker-runtime, savingsplans, scheduler, schemas, sdb, secretsmanager, security-ir, securityhub, securitylake, serverlessrepo, service-quotas, servicecatalog, servicecatalog-appregistry, servicediscovery, ses, sesv2, shield, signer, signin, simspaceweaver, sms-voice, snow-device-management, snowball, sns, socialmessaging, sqs, ssm, ssm-contacts, ssm-guiconnect, ssm-incidents, ssm-quicksetup, ssm-sap, sso, sso-admin, sso-oidc, stepfunctions, storagegateway, sts, supplychain, support, support-app, swf, synthetics, taxsettings, textract, timestream-influxdb, timestream-query, timestream-write, tnb, transcribe, transfer, translate, trustedadvisor, verifiedpermissions, voice-id, vpc-lattice, vpc-lattice-preview, vpc-service-network, waf, waf-regional, wafv2, wellarchitected, wickr, wisdom, workdocs, workmail, workmailmessageflow, workspaces, workspaces-instances, workspaces-thin-client, workspaces-web, xray

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_opsworks_rds_db_instance`

- **Client:** `opsworks`
- **Method:** `list_rds_db_instances`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Unknown service: 'opsworks'. Valid service names are: accessanalyzer, account, acm, acm-pca, aiops, amp, amplify, amplifybackend, amplifyuibuilder, apigateway, apigatewaymanagementapi, apigatewayv2, appconfig, appconfigdata, appfabric, appflow, appintegrations, application-autoscaling, application-insights, application-signals, applicationcostprofiler, appmesh, apprunner, appstream, appsync, arc-region-switch, arc-zonal-shift, artifact, athena, auditmanager, autoscaling, autoscaling-plans, b2bi, backup, backup-gateway, backupsearch, batch, bcm-dashboards, bcm-data-exports, bcm-pricing-calculator, bcm-recommended-actions, bedrock, bedrock-agent, bedrock-agent-runtime, bedrock-agentcore, bedrock-agentcore-control, bedrock-data-automation, bedrock-data-automation-runtime, bedrock-runtime, billing, billingconductor, braket, budgets, ce, chatbot, chime, chime-sdk-identity, chime-sdk-media-pipelines, chime-sdk-meetings, chime-sdk-messaging, chime-sdk-voice, cleanrooms, cleanroomsml, cloud9, cloudcontrol, clouddirectory, cloudformation, cloudfront, cloudfront-keyvaluestore, cloudhsm, cloudhsmv2, cloudsearch, cloudsearchdomain, cloudtrail, cloudtrail-data, cloudwatch, codeartifact, codebuild, codecatalyst, codecommit, codeconnections, codedeploy, codeguru-reviewer, codeguru-security, codeguruprofiler, codepipeline, codestar-connections, codestar-notifications, cognito-identity, cognito-idp, cognito-sync, comprehend, comprehendmedical, compute-optimizer, compute-optimizer-automation, config, connect, connect-contact-lens, connectcampaigns, connectcampaignsv2, connectcases, connectparticipant, controlcatalog, controltower, cost-optimization-hub, cur, customer-profiles, databrew, dataexchange, datapipeline, datasync, datazone, dax, deadline, detective, devicefarm, devops-guru, directconnect, discovery, dlm, dms, docdb, docdb-elastic, drs, ds, ds-data, dsql, dynamodb, dynamodbstreams, ebs, ec2, ec2-instance-connect, ec2-mercury, ecr, ecr-public, ecs, efs, eks, eks-auth, elasticache, elasticbeanstalk, elastictranscoder, elb, elbv2, emr, emr-containers, emr-serverless, entityresolution, es, events, evidently, evs, finspace, finspace-data, firehose, fis, fms, forecast, forecastquery, frauddetector, freetier, fsx, gamelift, gameliftstreams, geo-maps, geo-places, geo-routes, glacier, globalaccelerator, glue, grafana, greengrass, greengrassv2, groundstation, guardduty, health, healthlake, iam, identitystore, imagebuilder, importexport, inspector, inspector-scan, inspector2, internetmonitor, invoicing, iot, iot-data, iot-jobs-data, iot-managed-integrations, iotanalytics, iotdeviceadvisor, iotevents, iotevents-data, iotfleetwise, iotsecuretunneling, iotsitewise, iotthingsgraph, iottwinmaker, iotwireless, ivs, ivs-realtime, ivschat, kafka, kafkaconnect, kendra, kendra-ranking, keyspaces, keyspacesstreams, kinesis, kinesis-video-archived-media, kinesis-video-media, kinesis-video-signaling, kinesis-video-webrtc-storage, kinesisanalytics, kinesisanalyticsv2, kinesisvideo, kms, lakeformation, lambda, launch-wizard, lex-models, lex-runtime, lexv2-models, lexv2-runtime, license-manager, license-manager-linux-subscriptions, license-manager-user-subscriptions, lightsail, location, logs, lookoutequipment, m2, machinelearning, macie2, mailmanager, managedblockchain, managedblockchain-query, marketplace-agreement, marketplace-catalog, marketplace-deployment, marketplace-entitlement, marketplace-reporting, marketplacecommerceanalytics, mediaconnect, mediaconvert, medialive, mediapackage, mediapackage-vod, mediapackagev2, mediastore, mediastore-data, mediatailor, medical-imaging, memorydb, meteringmarketplace, mgh, mgn, migration-hub-refactor-spaces, migrationhub-config, migrationhuborchestrator, migrationhubstrategy, mpa, mq, mturk, mwaa, mwaa-serverless, neptune, neptune-graph, neptunedata, network-firewall, networkflowmonitor, networkmanager, networkmonitor, notifications, notificationscontacts, nova-act, oam, observabilityadmin, odb, omics, opensearch, opensearchserverless, organizations, osis, outposts, panorama, partnercentral-account, partnercentral-benefits, partnercentral-channel, partnercentral-selling, payment-cryptography, payment-cryptography-data, pca-connector-ad, pca-connector-scep, pcs, personalize, personalize-events, personalize-runtime, pi, pinpoint, pinpoint-email, pinpoint-sms-voice, pinpoint-sms-voice-v2, pipes, polly, pricing, proton, qapps, qbusiness, qconnect, quicksight, ram, rbin, rds, rds-data, redshift, redshift-data, redshift-serverless, rekognition, repostspace, resiliencehub, resource-explorer-2, resource-groups, resourcegroupstaggingapi, rolesanywhere, route53, route53-recovery-cluster, route53-recovery-control-config, route53-recovery-readiness, route53domains, route53globalresolver, route53profiles, route53resolver, rtbfabric, rum, s3, s3control, s3outposts, s3tables, s3vectors, sagemaker, sagemaker-a2i-runtime, sagemaker-edge, sagemaker-featurestore-runtime, sagemaker-geospatial, sagemaker-metrics, sagemaker-runtime, savingsplans, scheduler, schemas, sdb, secretsmanager, security-ir, securityhub, securitylake, serverlessrepo, service-quotas, servicecatalog, servicecatalog-appregistry, servicediscovery, ses, sesv2, shield, signer, signin, simspaceweaver, sms-voice, snow-device-management, snowball, sns, socialmessaging, sqs, ssm, ssm-contacts, ssm-guiconnect, ssm-incidents, ssm-quicksetup, ssm-sap, sso, sso-admin, sso-oidc, stepfunctions, storagegateway, sts, supplychain, support, support-app, swf, synthetics, taxsettings, textract, timestream-influxdb, timestream-query, timestream-write, tnb, transcribe, transfer, translate, trustedadvisor, verifiedpermissions, voice-id, vpc-lattice, vpc-lattice-preview, vpc-service-network, waf, waf-regional, wafv2, wellarchitected, wickr, wisdom, workdocs, workmail, workmailmessageflow, workspaces, workspaces-instances, workspaces-thin-client, workspaces-web, xray

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_opsworks_stack`

- **Client:** `opsworks`
- **Method:** `list_stacks`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Unknown service: 'opsworks'. Valid service names are: accessanalyzer, account, acm, acm-pca, aiops, amp, amplify, amplifybackend, amplifyuibuilder, apigateway, apigatewaymanagementapi, apigatewayv2, appconfig, appconfigdata, appfabric, appflow, appintegrations, application-autoscaling, application-insights, application-signals, applicationcostprofiler, appmesh, apprunner, appstream, appsync, arc-region-switch, arc-zonal-shift, artifact, athena, auditmanager, autoscaling, autoscaling-plans, b2bi, backup, backup-gateway, backupsearch, batch, bcm-dashboards, bcm-data-exports, bcm-pricing-calculator, bcm-recommended-actions, bedrock, bedrock-agent, bedrock-agent-runtime, bedrock-agentcore, bedrock-agentcore-control, bedrock-data-automation, bedrock-data-automation-runtime, bedrock-runtime, billing, billingconductor, braket, budgets, ce, chatbot, chime, chime-sdk-identity, chime-sdk-media-pipelines, chime-sdk-meetings, chime-sdk-messaging, chime-sdk-voice, cleanrooms, cleanroomsml, cloud9, cloudcontrol, clouddirectory, cloudformation, cloudfront, cloudfront-keyvaluestore, cloudhsm, cloudhsmv2, cloudsearch, cloudsearchdomain, cloudtrail, cloudtrail-data, cloudwatch, codeartifact, codebuild, codecatalyst, codecommit, codeconnections, codedeploy, codeguru-reviewer, codeguru-security, codeguruprofiler, codepipeline, codestar-connections, codestar-notifications, cognito-identity, cognito-idp, cognito-sync, comprehend, comprehendmedical, compute-optimizer, compute-optimizer-automation, config, connect, connect-contact-lens, connectcampaigns, connectcampaignsv2, connectcases, connectparticipant, controlcatalog, controltower, cost-optimization-hub, cur, customer-profiles, databrew, dataexchange, datapipeline, datasync, datazone, dax, deadline, detective, devicefarm, devops-guru, directconnect, discovery, dlm, dms, docdb, docdb-elastic, drs, ds, ds-data, dsql, dynamodb, dynamodbstreams, ebs, ec2, ec2-instance-connect, ec2-mercury, ecr, ecr-public, ecs, efs, eks, eks-auth, elasticache, elasticbeanstalk, elastictranscoder, elb, elbv2, emr, emr-containers, emr-serverless, entityresolution, es, events, evidently, evs, finspace, finspace-data, firehose, fis, fms, forecast, forecastquery, frauddetector, freetier, fsx, gamelift, gameliftstreams, geo-maps, geo-places, geo-routes, glacier, globalaccelerator, glue, grafana, greengrass, greengrassv2, groundstation, guardduty, health, healthlake, iam, identitystore, imagebuilder, importexport, inspector, inspector-scan, inspector2, internetmonitor, invoicing, iot, iot-data, iot-jobs-data, iot-managed-integrations, iotanalytics, iotdeviceadvisor, iotevents, iotevents-data, iotfleetwise, iotsecuretunneling, iotsitewise, iotthingsgraph, iottwinmaker, iotwireless, ivs, ivs-realtime, ivschat, kafka, kafkaconnect, kendra, kendra-ranking, keyspaces, keyspacesstreams, kinesis, kinesis-video-archived-media, kinesis-video-media, kinesis-video-signaling, kinesis-video-webrtc-storage, kinesisanalytics, kinesisanalyticsv2, kinesisvideo, kms, lakeformation, lambda, launch-wizard, lex-models, lex-runtime, lexv2-models, lexv2-runtime, license-manager, license-manager-linux-subscriptions, license-manager-user-subscriptions, lightsail, location, logs, lookoutequipment, m2, machinelearning, macie2, mailmanager, managedblockchain, managedblockchain-query, marketplace-agreement, marketplace-catalog, marketplace-deployment, marketplace-entitlement, marketplace-reporting, marketplacecommerceanalytics, mediaconnect, mediaconvert, medialive, mediapackage, mediapackage-vod, mediapackagev2, mediastore, mediastore-data, mediatailor, medical-imaging, memorydb, meteringmarketplace, mgh, mgn, migration-hub-refactor-spaces, migrationhub-config, migrationhuborchestrator, migrationhubstrategy, mpa, mq, mturk, mwaa, mwaa-serverless, neptune, neptune-graph, neptunedata, network-firewall, networkflowmonitor, networkmanager, networkmonitor, notifications, notificationscontacts, nova-act, oam, observabilityadmin, odb, omics, opensearch, opensearchserverless, organizations, osis, outposts, panorama, partnercentral-account, partnercentral-benefits, partnercentral-channel, partnercentral-selling, payment-cryptography, payment-cryptography-data, pca-connector-ad, pca-connector-scep, pcs, personalize, personalize-events, personalize-runtime, pi, pinpoint, pinpoint-email, pinpoint-sms-voice, pinpoint-sms-voice-v2, pipes, polly, pricing, proton, qapps, qbusiness, qconnect, quicksight, ram, rbin, rds, rds-data, redshift, redshift-data, redshift-serverless, rekognition, repostspace, resiliencehub, resource-explorer-2, resource-groups, resourcegroupstaggingapi, rolesanywhere, route53, route53-recovery-cluster, route53-recovery-control-config, route53-recovery-readiness, route53domains, route53globalresolver, route53profiles, route53resolver, rtbfabric, rum, s3, s3control, s3outposts, s3tables, s3vectors, sagemaker, sagemaker-a2i-runtime, sagemaker-edge, sagemaker-featurestore-runtime, sagemaker-geospatial, sagemaker-metrics, sagemaker-runtime, savingsplans, scheduler, schemas, sdb, secretsmanager, security-ir, securityhub, securitylake, serverlessrepo, service-quotas, servicecatalog, servicecatalog-appregistry, servicediscovery, ses, sesv2, shield, signer, signin, simspaceweaver, sms-voice, snow-device-management, snowball, sns, socialmessaging, sqs, ssm, ssm-contacts, ssm-guiconnect, ssm-incidents, ssm-quicksetup, ssm-sap, sso, sso-admin, sso-oidc, stepfunctions, storagegateway, sts, supplychain, support, support-app, swf, synthetics, taxsettings, textract, timestream-influxdb, timestream-query, timestream-write, tnb, transcribe, transfer, translate, trustedadvisor, verifiedpermissions, voice-id, vpc-lattice, vpc-lattice-preview, vpc-service-network, waf, waf-regional, wafv2, wellarchitected, wickr, wisdom, workdocs, workmail, workmailmessageflow, workspaces, workspaces-instances, workspaces-thin-client, workspaces-web, xray

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_opsworks_static_web_layer`

- **Client:** `opsworks`
- **Method:** `list_static_web_layers`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Unknown service: 'opsworks'. Valid service names are: accessanalyzer, account, acm, acm-pca, aiops, amp, amplify, amplifybackend, amplifyuibuilder, apigateway, apigatewaymanagementapi, apigatewayv2, appconfig, appconfigdata, appfabric, appflow, appintegrations, application-autoscaling, application-insights, application-signals, applicationcostprofiler, appmesh, apprunner, appstream, appsync, arc-region-switch, arc-zonal-shift, artifact, athena, auditmanager, autoscaling, autoscaling-plans, b2bi, backup, backup-gateway, backupsearch, batch, bcm-dashboards, bcm-data-exports, bcm-pricing-calculator, bcm-recommended-actions, bedrock, bedrock-agent, bedrock-agent-runtime, bedrock-agentcore, bedrock-agentcore-control, bedrock-data-automation, bedrock-data-automation-runtime, bedrock-runtime, billing, billingconductor, braket, budgets, ce, chatbot, chime, chime-sdk-identity, chime-sdk-media-pipelines, chime-sdk-meetings, chime-sdk-messaging, chime-sdk-voice, cleanrooms, cleanroomsml, cloud9, cloudcontrol, clouddirectory, cloudformation, cloudfront, cloudfront-keyvaluestore, cloudhsm, cloudhsmv2, cloudsearch, cloudsearchdomain, cloudtrail, cloudtrail-data, cloudwatch, codeartifact, codebuild, codecatalyst, codecommit, codeconnections, codedeploy, codeguru-reviewer, codeguru-security, codeguruprofiler, codepipeline, codestar-connections, codestar-notifications, cognito-identity, cognito-idp, cognito-sync, comprehend, comprehendmedical, compute-optimizer, compute-optimizer-automation, config, connect, connect-contact-lens, connectcampaigns, connectcampaignsv2, connectcases, connectparticipant, controlcatalog, controltower, cost-optimization-hub, cur, customer-profiles, databrew, dataexchange, datapipeline, datasync, datazone, dax, deadline, detective, devicefarm, devops-guru, directconnect, discovery, dlm, dms, docdb, docdb-elastic, drs, ds, ds-data, dsql, dynamodb, dynamodbstreams, ebs, ec2, ec2-instance-connect, ec2-mercury, ecr, ecr-public, ecs, efs, eks, eks-auth, elasticache, elasticbeanstalk, elastictranscoder, elb, elbv2, emr, emr-containers, emr-serverless, entityresolution, es, events, evidently, evs, finspace, finspace-data, firehose, fis, fms, forecast, forecastquery, frauddetector, freetier, fsx, gamelift, gameliftstreams, geo-maps, geo-places, geo-routes, glacier, globalaccelerator, glue, grafana, greengrass, greengrassv2, groundstation, guardduty, health, healthlake, iam, identitystore, imagebuilder, importexport, inspector, inspector-scan, inspector2, internetmonitor, invoicing, iot, iot-data, iot-jobs-data, iot-managed-integrations, iotanalytics, iotdeviceadvisor, iotevents, iotevents-data, iotfleetwise, iotsecuretunneling, iotsitewise, iotthingsgraph, iottwinmaker, iotwireless, ivs, ivs-realtime, ivschat, kafka, kafkaconnect, kendra, kendra-ranking, keyspaces, keyspacesstreams, kinesis, kinesis-video-archived-media, kinesis-video-media, kinesis-video-signaling, kinesis-video-webrtc-storage, kinesisanalytics, kinesisanalyticsv2, kinesisvideo, kms, lakeformation, lambda, launch-wizard, lex-models, lex-runtime, lexv2-models, lexv2-runtime, license-manager, license-manager-linux-subscriptions, license-manager-user-subscriptions, lightsail, location, logs, lookoutequipment, m2, machinelearning, macie2, mailmanager, managedblockchain, managedblockchain-query, marketplace-agreement, marketplace-catalog, marketplace-deployment, marketplace-entitlement, marketplace-reporting, marketplacecommerceanalytics, mediaconnect, mediaconvert, medialive, mediapackage, mediapackage-vod, mediapackagev2, mediastore, mediastore-data, mediatailor, medical-imaging, memorydb, meteringmarketplace, mgh, mgn, migration-hub-refactor-spaces, migrationhub-config, migrationhuborchestrator, migrationhubstrategy, mpa, mq, mturk, mwaa, mwaa-serverless, neptune, neptune-graph, neptunedata, network-firewall, networkflowmonitor, networkmanager, networkmonitor, notifications, notificationscontacts, nova-act, oam, observabilityadmin, odb, omics, opensearch, opensearchserverless, organizations, osis, outposts, panorama, partnercentral-account, partnercentral-benefits, partnercentral-channel, partnercentral-selling, payment-cryptography, payment-cryptography-data, pca-connector-ad, pca-connector-scep, pcs, personalize, personalize-events, personalize-runtime, pi, pinpoint, pinpoint-email, pinpoint-sms-voice, pinpoint-sms-voice-v2, pipes, polly, pricing, proton, qapps, qbusiness, qconnect, quicksight, ram, rbin, rds, rds-data, redshift, redshift-data, redshift-serverless, rekognition, repostspace, resiliencehub, resource-explorer-2, resource-groups, resourcegroupstaggingapi, rolesanywhere, route53, route53-recovery-cluster, route53-recovery-control-config, route53-recovery-readiness, route53domains, route53globalresolver, route53profiles, route53resolver, rtbfabric, rum, s3, s3control, s3outposts, s3tables, s3vectors, sagemaker, sagemaker-a2i-runtime, sagemaker-edge, sagemaker-featurestore-runtime, sagemaker-geospatial, sagemaker-metrics, sagemaker-runtime, savingsplans, scheduler, schemas, sdb, secretsmanager, security-ir, securityhub, securitylake, serverlessrepo, service-quotas, servicecatalog, servicecatalog-appregistry, servicediscovery, ses, sesv2, shield, signer, signin, simspaceweaver, sms-voice, snow-device-management, snowball, sns, socialmessaging, sqs, ssm, ssm-contacts, ssm-guiconnect, ssm-incidents, ssm-quicksetup, ssm-sap, sso, sso-admin, sso-oidc, stepfunctions, storagegateway, sts, supplychain, support, support-app, swf, synthetics, taxsettings, textract, timestream-influxdb, timestream-query, timestream-write, tnb, transcribe, transfer, translate, trustedadvisor, verifiedpermissions, voice-id, vpc-lattice, vpc-lattice-preview, vpc-service-network, waf, waf-regional, wafv2, wellarchitected, wickr, wisdom, workdocs, workmail, workmailmessageflow, workspaces, workspaces-instances, workspaces-thin-client, workspaces-web, xray

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_opsworks_user_profile`

- **Client:** `opsworks`
- **Method:** `list_user_profiles`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Unknown service: 'opsworks'. Valid service names are: accessanalyzer, account, acm, acm-pca, aiops, amp, amplify, amplifybackend, amplifyuibuilder, apigateway, apigatewaymanagementapi, apigatewayv2, appconfig, appconfigdata, appfabric, appflow, appintegrations, application-autoscaling, application-insights, application-signals, applicationcostprofiler, appmesh, apprunner, appstream, appsync, arc-region-switch, arc-zonal-shift, artifact, athena, auditmanager, autoscaling, autoscaling-plans, b2bi, backup, backup-gateway, backupsearch, batch, bcm-dashboards, bcm-data-exports, bcm-pricing-calculator, bcm-recommended-actions, bedrock, bedrock-agent, bedrock-agent-runtime, bedrock-agentcore, bedrock-agentcore-control, bedrock-data-automation, bedrock-data-automation-runtime, bedrock-runtime, billing, billingconductor, braket, budgets, ce, chatbot, chime, chime-sdk-identity, chime-sdk-media-pipelines, chime-sdk-meetings, chime-sdk-messaging, chime-sdk-voice, cleanrooms, cleanroomsml, cloud9, cloudcontrol, clouddirectory, cloudformation, cloudfront, cloudfront-keyvaluestore, cloudhsm, cloudhsmv2, cloudsearch, cloudsearchdomain, cloudtrail, cloudtrail-data, cloudwatch, codeartifact, codebuild, codecatalyst, codecommit, codeconnections, codedeploy, codeguru-reviewer, codeguru-security, codeguruprofiler, codepipeline, codestar-connections, codestar-notifications, cognito-identity, cognito-idp, cognito-sync, comprehend, comprehendmedical, compute-optimizer, compute-optimizer-automation, config, connect, connect-contact-lens, connectcampaigns, connectcampaignsv2, connectcases, connectparticipant, controlcatalog, controltower, cost-optimization-hub, cur, customer-profiles, databrew, dataexchange, datapipeline, datasync, datazone, dax, deadline, detective, devicefarm, devops-guru, directconnect, discovery, dlm, dms, docdb, docdb-elastic, drs, ds, ds-data, dsql, dynamodb, dynamodbstreams, ebs, ec2, ec2-instance-connect, ec2-mercury, ecr, ecr-public, ecs, efs, eks, eks-auth, elasticache, elasticbeanstalk, elastictranscoder, elb, elbv2, emr, emr-containers, emr-serverless, entityresolution, es, events, evidently, evs, finspace, finspace-data, firehose, fis, fms, forecast, forecastquery, frauddetector, freetier, fsx, gamelift, gameliftstreams, geo-maps, geo-places, geo-routes, glacier, globalaccelerator, glue, grafana, greengrass, greengrassv2, groundstation, guardduty, health, healthlake, iam, identitystore, imagebuilder, importexport, inspector, inspector-scan, inspector2, internetmonitor, invoicing, iot, iot-data, iot-jobs-data, iot-managed-integrations, iotanalytics, iotdeviceadvisor, iotevents, iotevents-data, iotfleetwise, iotsecuretunneling, iotsitewise, iotthingsgraph, iottwinmaker, iotwireless, ivs, ivs-realtime, ivschat, kafka, kafkaconnect, kendra, kendra-ranking, keyspaces, keyspacesstreams, kinesis, kinesis-video-archived-media, kinesis-video-media, kinesis-video-signaling, kinesis-video-webrtc-storage, kinesisanalytics, kinesisanalyticsv2, kinesisvideo, kms, lakeformation, lambda, launch-wizard, lex-models, lex-runtime, lexv2-models, lexv2-runtime, license-manager, license-manager-linux-subscriptions, license-manager-user-subscriptions, lightsail, location, logs, lookoutequipment, m2, machinelearning, macie2, mailmanager, managedblockchain, managedblockchain-query, marketplace-agreement, marketplace-catalog, marketplace-deployment, marketplace-entitlement, marketplace-reporting, marketplacecommerceanalytics, mediaconnect, mediaconvert, medialive, mediapackage, mediapackage-vod, mediapackagev2, mediastore, mediastore-data, mediatailor, medical-imaging, memorydb, meteringmarketplace, mgh, mgn, migration-hub-refactor-spaces, migrationhub-config, migrationhuborchestrator, migrationhubstrategy, mpa, mq, mturk, mwaa, mwaa-serverless, neptune, neptune-graph, neptunedata, network-firewall, networkflowmonitor, networkmanager, networkmonitor, notifications, notificationscontacts, nova-act, oam, observabilityadmin, odb, omics, opensearch, opensearchserverless, organizations, osis, outposts, panorama, partnercentral-account, partnercentral-benefits, partnercentral-channel, partnercentral-selling, payment-cryptography, payment-cryptography-data, pca-connector-ad, pca-connector-scep, pcs, personalize, personalize-events, personalize-runtime, pi, pinpoint, pinpoint-email, pinpoint-sms-voice, pinpoint-sms-voice-v2, pipes, polly, pricing, proton, qapps, qbusiness, qconnect, quicksight, ram, rbin, rds, rds-data, redshift, redshift-data, redshift-serverless, rekognition, repostspace, resiliencehub, resource-explorer-2, resource-groups, resourcegroupstaggingapi, rolesanywhere, route53, route53-recovery-cluster, route53-recovery-control-config, route53-recovery-readiness, route53domains, route53globalresolver, route53profiles, route53resolver, rtbfabric, rum, s3, s3control, s3outposts, s3tables, s3vectors, sagemaker, sagemaker-a2i-runtime, sagemaker-edge, sagemaker-featurestore-runtime, sagemaker-geospatial, sagemaker-metrics, sagemaker-runtime, savingsplans, scheduler, schemas, sdb, secretsmanager, security-ir, securityhub, securitylake, serverlessrepo, service-quotas, servicecatalog, servicecatalog-appregistry, servicediscovery, ses, sesv2, shield, signer, signin, simspaceweaver, sms-voice, snow-device-management, snowball, sns, socialmessaging, sqs, ssm, ssm-contacts, ssm-guiconnect, ssm-incidents, ssm-quicksetup, ssm-sap, sso, sso-admin, sso-oidc, stepfunctions, storagegateway, sts, supplychain, support, support-app, swf, synthetics, taxsettings, textract, timestream-influxdb, timestream-query, timestream-write, tnb, transcribe, transfer, translate, trustedadvisor, verifiedpermissions, voice-id, vpc-lattice, vpc-lattice-preview, vpc-service-network, waf, waf-regional, wafv2, wellarchitected, wickr, wisdom, workdocs, workmail, workmailmessageflow, workspaces, workspaces-instances, workspaces-thin-client, workspaces-web, xray

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_organizations_organizational_unit`

- **Client:** `organizations`
- **Method:** `describe_organizational_unit`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "OrganizationalUnitId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_organizations_policy`

- **Client:** `organizations`
- **Method:** `list_policies`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Filter"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_organizations_policy_attachment`

- **Client:** `organizations`
- **Method:** `list_targets_for_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "PolicyId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_organizations_resource_policy`

- **Client:** `organizations`
- **Method:** `describe_resource_policy`
- **Error Code:** `ResourcePolicyNotFoundException`
- **Error Type:** `api_error`

**Error:** API error (ResourcePolicyNotFoundException): No resource-based policy found.

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_organizations_tag`

- **Client:** `organizations`
- **Method:** `list_tags_for_resource`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ResourceId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_prometheus_alert_manager_definition`

- **Client:** `amp`
- **Method:** `describe_alert_manager_definition`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "workspaceId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_prometheus_query_logging_configuration`

- **Client:** `amp`
- **Method:** `describe_workspace`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "workspaceId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_prometheus_resource_policy`

- **Client:** `amp`
- **Method:** `describe_resource_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "workspaceId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_prometheus_rule_group_namespace`

- **Client:** `amp`
- **Method:** `list_rule_groups_namespaces`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "workspaceId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_prometheus_workspace_configuration`

- **Client:** `amp`
- **Method:** `describe_workspace_configuration`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "workspaceId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_qldb_ledger`

- **Client:** `qldb`
- **Method:** `list_ledgers`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Unknown service: 'qldb'. Valid service names are: accessanalyzer, account, acm, acm-pca, aiops, amp, amplify, amplifybackend, amplifyuibuilder, apigateway, apigatewaymanagementapi, apigatewayv2, appconfig, appconfigdata, appfabric, appflow, appintegrations, application-autoscaling, application-insights, application-signals, applicationcostprofiler, appmesh, apprunner, appstream, appsync, arc-region-switch, arc-zonal-shift, artifact, athena, auditmanager, autoscaling, autoscaling-plans, b2bi, backup, backup-gateway, backupsearch, batch, bcm-dashboards, bcm-data-exports, bcm-pricing-calculator, bcm-recommended-actions, bedrock, bedrock-agent, bedrock-agent-runtime, bedrock-agentcore, bedrock-agentcore-control, bedrock-data-automation, bedrock-data-automation-runtime, bedrock-runtime, billing, billingconductor, braket, budgets, ce, chatbot, chime, chime-sdk-identity, chime-sdk-media-pipelines, chime-sdk-meetings, chime-sdk-messaging, chime-sdk-voice, cleanrooms, cleanroomsml, cloud9, cloudcontrol, clouddirectory, cloudformation, cloudfront, cloudfront-keyvaluestore, cloudhsm, cloudhsmv2, cloudsearch, cloudsearchdomain, cloudtrail, cloudtrail-data, cloudwatch, codeartifact, codebuild, codecatalyst, codecommit, codeconnections, codedeploy, codeguru-reviewer, codeguru-security, codeguruprofiler, codepipeline, codestar-connections, codestar-notifications, cognito-identity, cognito-idp, cognito-sync, comprehend, comprehendmedical, compute-optimizer, compute-optimizer-automation, config, connect, connect-contact-lens, connectcampaigns, connectcampaignsv2, connectcases, connectparticipant, controlcatalog, controltower, cost-optimization-hub, cur, customer-profiles, databrew, dataexchange, datapipeline, datasync, datazone, dax, deadline, detective, devicefarm, devops-guru, directconnect, discovery, dlm, dms, docdb, docdb-elastic, drs, ds, ds-data, dsql, dynamodb, dynamodbstreams, ebs, ec2, ec2-instance-connect, ec2-mercury, ecr, ecr-public, ecs, efs, eks, eks-auth, elasticache, elasticbeanstalk, elastictranscoder, elb, elbv2, emr, emr-containers, emr-serverless, entityresolution, es, events, evidently, evs, finspace, finspace-data, firehose, fis, fms, forecast, forecastquery, frauddetector, freetier, fsx, gamelift, gameliftstreams, geo-maps, geo-places, geo-routes, glacier, globalaccelerator, glue, grafana, greengrass, greengrassv2, groundstation, guardduty, health, healthlake, iam, identitystore, imagebuilder, importexport, inspector, inspector-scan, inspector2, internetmonitor, invoicing, iot, iot-data, iot-jobs-data, iot-managed-integrations, iotanalytics, iotdeviceadvisor, iotevents, iotevents-data, iotfleetwise, iotsecuretunneling, iotsitewise, iotthingsgraph, iottwinmaker, iotwireless, ivs, ivs-realtime, ivschat, kafka, kafkaconnect, kendra, kendra-ranking, keyspaces, keyspacesstreams, kinesis, kinesis-video-archived-media, kinesis-video-media, kinesis-video-signaling, kinesis-video-webrtc-storage, kinesisanalytics, kinesisanalyticsv2, kinesisvideo, kms, lakeformation, lambda, launch-wizard, lex-models, lex-runtime, lexv2-models, lexv2-runtime, license-manager, license-manager-linux-subscriptions, license-manager-user-subscriptions, lightsail, location, logs, lookoutequipment, m2, machinelearning, macie2, mailmanager, managedblockchain, managedblockchain-query, marketplace-agreement, marketplace-catalog, marketplace-deployment, marketplace-entitlement, marketplace-reporting, marketplacecommerceanalytics, mediaconnect, mediaconvert, medialive, mediapackage, mediapackage-vod, mediapackagev2, mediastore, mediastore-data, mediatailor, medical-imaging, memorydb, meteringmarketplace, mgh, mgn, migration-hub-refactor-spaces, migrationhub-config, migrationhuborchestrator, migrationhubstrategy, mpa, mq, mturk, mwaa, mwaa-serverless, neptune, neptune-graph, neptunedata, network-firewall, networkflowmonitor, networkmanager, networkmonitor, notifications, notificationscontacts, nova-act, oam, observabilityadmin, odb, omics, opensearch, opensearchserverless, organizations, osis, outposts, panorama, partnercentral-account, partnercentral-benefits, partnercentral-channel, partnercentral-selling, payment-cryptography, payment-cryptography-data, pca-connector-ad, pca-connector-scep, pcs, personalize, personalize-events, personalize-runtime, pi, pinpoint, pinpoint-email, pinpoint-sms-voice, pinpoint-sms-voice-v2, pipes, polly, pricing, proton, qapps, qbusiness, qconnect, quicksight, ram, rbin, rds, rds-data, redshift, redshift-data, redshift-serverless, rekognition, repostspace, resiliencehub, resource-explorer-2, resource-groups, resourcegroupstaggingapi, rolesanywhere, route53, route53-recovery-cluster, route53-recovery-control-config, route53-recovery-readiness, route53domains, route53globalresolver, route53profiles, route53resolver, rtbfabric, rum, s3, s3control, s3outposts, s3tables, s3vectors, sagemaker, sagemaker-a2i-runtime, sagemaker-edge, sagemaker-featurestore-runtime, sagemaker-geospatial, sagemaker-metrics, sagemaker-runtime, savingsplans, scheduler, schemas, sdb, secretsmanager, security-ir, securityhub, securitylake, serverlessrepo, service-quotas, servicecatalog, servicecatalog-appregistry, servicediscovery, ses, sesv2, shield, signer, signin, simspaceweaver, sms-voice, snow-device-management, snowball, sns, socialmessaging, sqs, ssm, ssm-contacts, ssm-guiconnect, ssm-incidents, ssm-quicksetup, ssm-sap, sso, sso-admin, sso-oidc, stepfunctions, storagegateway, sts, supplychain, support, support-app, swf, synthetics, taxsettings, textract, timestream-influxdb, timestream-query, timestream-write, tnb, transcribe, transfer, translate, trustedadvisor, verifiedpermissions, voice-id, vpc-lattice, vpc-lattice-preview, vpc-service-network, waf, waf-regional, wafv2, wellarchitected, wickr, wisdom, workdocs, workmail, workmailmessageflow, workspaces, workspaces-instances, workspaces-thin-client, workspaces-web, xray

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_qldb_stream`

- **Client:** `qldb`
- **Method:** `list_streams`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Unknown service: 'qldb'. Valid service names are: accessanalyzer, account, acm, acm-pca, aiops, amp, amplify, amplifybackend, amplifyuibuilder, apigateway, apigatewaymanagementapi, apigatewayv2, appconfig, appconfigdata, appfabric, appflow, appintegrations, application-autoscaling, application-insights, application-signals, applicationcostprofiler, appmesh, apprunner, appstream, appsync, arc-region-switch, arc-zonal-shift, artifact, athena, auditmanager, autoscaling, autoscaling-plans, b2bi, backup, backup-gateway, backupsearch, batch, bcm-dashboards, bcm-data-exports, bcm-pricing-calculator, bcm-recommended-actions, bedrock, bedrock-agent, bedrock-agent-runtime, bedrock-agentcore, bedrock-agentcore-control, bedrock-data-automation, bedrock-data-automation-runtime, bedrock-runtime, billing, billingconductor, braket, budgets, ce, chatbot, chime, chime-sdk-identity, chime-sdk-media-pipelines, chime-sdk-meetings, chime-sdk-messaging, chime-sdk-voice, cleanrooms, cleanroomsml, cloud9, cloudcontrol, clouddirectory, cloudformation, cloudfront, cloudfront-keyvaluestore, cloudhsm, cloudhsmv2, cloudsearch, cloudsearchdomain, cloudtrail, cloudtrail-data, cloudwatch, codeartifact, codebuild, codecatalyst, codecommit, codeconnections, codedeploy, codeguru-reviewer, codeguru-security, codeguruprofiler, codepipeline, codestar-connections, codestar-notifications, cognito-identity, cognito-idp, cognito-sync, comprehend, comprehendmedical, compute-optimizer, compute-optimizer-automation, config, connect, connect-contact-lens, connectcampaigns, connectcampaignsv2, connectcases, connectparticipant, controlcatalog, controltower, cost-optimization-hub, cur, customer-profiles, databrew, dataexchange, datapipeline, datasync, datazone, dax, deadline, detective, devicefarm, devops-guru, directconnect, discovery, dlm, dms, docdb, docdb-elastic, drs, ds, ds-data, dsql, dynamodb, dynamodbstreams, ebs, ec2, ec2-instance-connect, ec2-mercury, ecr, ecr-public, ecs, efs, eks, eks-auth, elasticache, elasticbeanstalk, elastictranscoder, elb, elbv2, emr, emr-containers, emr-serverless, entityresolution, es, events, evidently, evs, finspace, finspace-data, firehose, fis, fms, forecast, forecastquery, frauddetector, freetier, fsx, gamelift, gameliftstreams, geo-maps, geo-places, geo-routes, glacier, globalaccelerator, glue, grafana, greengrass, greengrassv2, groundstation, guardduty, health, healthlake, iam, identitystore, imagebuilder, importexport, inspector, inspector-scan, inspector2, internetmonitor, invoicing, iot, iot-data, iot-jobs-data, iot-managed-integrations, iotanalytics, iotdeviceadvisor, iotevents, iotevents-data, iotfleetwise, iotsecuretunneling, iotsitewise, iotthingsgraph, iottwinmaker, iotwireless, ivs, ivs-realtime, ivschat, kafka, kafkaconnect, kendra, kendra-ranking, keyspaces, keyspacesstreams, kinesis, kinesis-video-archived-media, kinesis-video-media, kinesis-video-signaling, kinesis-video-webrtc-storage, kinesisanalytics, kinesisanalyticsv2, kinesisvideo, kms, lakeformation, lambda, launch-wizard, lex-models, lex-runtime, lexv2-models, lexv2-runtime, license-manager, license-manager-linux-subscriptions, license-manager-user-subscriptions, lightsail, location, logs, lookoutequipment, m2, machinelearning, macie2, mailmanager, managedblockchain, managedblockchain-query, marketplace-agreement, marketplace-catalog, marketplace-deployment, marketplace-entitlement, marketplace-reporting, marketplacecommerceanalytics, mediaconnect, mediaconvert, medialive, mediapackage, mediapackage-vod, mediapackagev2, mediastore, mediastore-data, mediatailor, medical-imaging, memorydb, meteringmarketplace, mgh, mgn, migration-hub-refactor-spaces, migrationhub-config, migrationhuborchestrator, migrationhubstrategy, mpa, mq, mturk, mwaa, mwaa-serverless, neptune, neptune-graph, neptunedata, network-firewall, networkflowmonitor, networkmanager, networkmonitor, notifications, notificationscontacts, nova-act, oam, observabilityadmin, odb, omics, opensearch, opensearchserverless, organizations, osis, outposts, panorama, partnercentral-account, partnercentral-benefits, partnercentral-channel, partnercentral-selling, payment-cryptography, payment-cryptography-data, pca-connector-ad, pca-connector-scep, pcs, personalize, personalize-events, personalize-runtime, pi, pinpoint, pinpoint-email, pinpoint-sms-voice, pinpoint-sms-voice-v2, pipes, polly, pricing, proton, qapps, qbusiness, qconnect, quicksight, ram, rbin, rds, rds-data, redshift, redshift-data, redshift-serverless, rekognition, repostspace, resiliencehub, resource-explorer-2, resource-groups, resourcegroupstaggingapi, rolesanywhere, route53, route53-recovery-cluster, route53-recovery-control-config, route53-recovery-readiness, route53domains, route53globalresolver, route53profiles, route53resolver, rtbfabric, rum, s3, s3control, s3outposts, s3tables, s3vectors, sagemaker, sagemaker-a2i-runtime, sagemaker-edge, sagemaker-featurestore-runtime, sagemaker-geospatial, sagemaker-metrics, sagemaker-runtime, savingsplans, scheduler, schemas, sdb, secretsmanager, security-ir, securityhub, securitylake, serverlessrepo, service-quotas, servicecatalog, servicecatalog-appregistry, servicediscovery, ses, sesv2, shield, signer, signin, simspaceweaver, sms-voice, snow-device-management, snowball, sns, socialmessaging, sqs, ssm, ssm-contacts, ssm-guiconnect, ssm-incidents, ssm-quicksetup, ssm-sap, sso, sso-admin, sso-oidc, stepfunctions, storagegateway, sts, supplychain, support, support-app, swf, synthetics, taxsettings, textract, timestream-influxdb, timestream-query, timestream-write, tnb, transcribe, transfer, translate, trustedadvisor, verifiedpermissions, voice-id, vpc-lattice, vpc-lattice-preview, vpc-service-network, waf, waf-regional, wafv2, wellarchitected, wickr, wisdom, workdocs, workmail, workmailmessageflow, workspaces, workspaces-instances, workspaces-thin-client, workspaces-web, xray

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_quicksight_account_settings`

- **Client:** `quicksight`
- **Method:** `describe_account_settings`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AwsAccountId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_quicksight_analysis`

- **Client:** `quicksight`
- **Method:** `list_analyses`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AwsAccountId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_quicksight_custom_permissions`

- **Client:** `quicksight`
- **Method:** `describe_custom_permissions`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AwsAccountId"
Missing required parameter in input: "CustomPermissionsName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_quicksight_dashboard`

- **Client:** `quicksight`
- **Method:** `list_dashboards`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AwsAccountId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_quicksight_data_set`

- **Client:** `quicksight`
- **Method:** `list_data_sets`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AwsAccountId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_quicksight_data_source`

- **Client:** `quicksight`
- **Method:** `list_data_sources`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AwsAccountId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_quicksight_folder`

- **Client:** `quicksight`
- **Method:** `list_folders`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AwsAccountId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_quicksight_group`

- **Client:** `quicksight`
- **Method:** `list_groups`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AwsAccountId"
Missing required parameter in input: "Namespace"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_quicksight_group_membership`

- **Client:** `quicksight`
- **Method:** `list_group_memberships`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "GroupName"
Missing required parameter in input: "AwsAccountId"
Missing required parameter in input: "Namespace"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_quicksight_iam_policy_assignment`

- **Client:** `quicksight`
- **Method:** `list_iam_policy_assignments`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AwsAccountId"
Missing required parameter in input: "Namespace"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_quicksight_ingestion`

- **Client:** `quicksight`
- **Method:** `list_ingestions`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DataSetId"
Missing required parameter in input: "AwsAccountId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_quicksight_ip_restriction`

- **Client:** `quicksight`
- **Method:** `describe_ip_restriction`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AwsAccountId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_quicksight_namespace`

- **Client:** `quicksight`
- **Method:** `list_namespaces`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AwsAccountId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_quicksight_refresh_schedule`

- **Client:** `quicksight`
- **Method:** `list_refresh_schedules`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AwsAccountId"
Missing required parameter in input: "DataSetId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_quicksight_role_custom_permission`

- **Client:** `quicksight`
- **Method:** `describe_role_custom_permission`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Role"
Missing required parameter in input: "AwsAccountId"
Missing required parameter in input: "Namespace"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_quicksight_role_membership`

- **Client:** `quicksight`
- **Method:** `list_role_memberships`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Role"
Missing required parameter in input: "AwsAccountId"
Missing required parameter in input: "Namespace"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_quicksight_template`

- **Client:** `quicksight`
- **Method:** `list_templates`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AwsAccountId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_quicksight_template_alias`

- **Client:** `quicksight`
- **Method:** `list_template_aliases`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AwsAccountId"
Missing required parameter in input: "TemplateId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_quicksight_theme`

- **Client:** `quicksight`
- **Method:** `list_themes`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AwsAccountId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_quicksight_user`

- **Client:** `quicksight`
- **Method:** `list_users`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AwsAccountId"
Missing required parameter in input: "Namespace"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_quicksight_user_custom_permission`

- **Client:** `quicksight`
- **Method:** `describe_user`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "UserName"
Missing required parameter in input: "AwsAccountId"
Missing required parameter in input: "Namespace"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_quicksight_vpc_connection`

- **Client:** `quicksight`
- **Method:** `list_vpc_connections`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AwsAccountId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ram_principal_association`

- **Client:** `ram`
- **Method:** `list_principals`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "resourceOwner"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ram_resource_association`

- **Client:** `ram`
- **Method:** `list_resources`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "resourceOwner"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ram_resource_share`

- **Client:** `ram`
- **Method:** `list_resources`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "resourceOwner"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_redshift_logging`

- **Client:** `redshift`
- **Method:** `describe_logging_status`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ClusterIdentifier"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_redshift_partner`

- **Client:** `redshift`
- **Method:** `describe_partners`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "AccountId"
Missing required parameter in input: "ClusterIdentifier"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_redshift_resource_policy`

- **Client:** `redshift`
- **Method:** `get_resource_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ResourceArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_redshiftdata_statement`

- **Client:** `redshift-data`
- **Method:** `describe_statement`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Id"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_route53_cidr_location`

- **Client:** `route53`
- **Method:** `list_cidr_locations`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "CollectionId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_route53_hosted_zone_dnssec`

- **Client:** `route53`
- **Method:** `get_dnssec`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "HostedZoneId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_route53_key_signing_key`

- **Client:** `route53`
- **Method:** `get_dnssec`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "HostedZoneId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_route53_record`

- **Client:** `route53`
- **Method:** `list_resource_record_sets`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "HostedZoneId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_route53_records_exclusive`

- **Client:** `route53`
- **Method:** `list_resource_record_sets`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "HostedZoneId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_route53_vpc_association_authorization`

- **Client:** `route53`
- **Method:** `get_hosted_zone`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Id"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_route53_zone_association`

- **Client:** `route53`
- **Method:** `list_hosted_zones_by_vpc`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "VPCId"
Missing required parameter in input: "VPCRegion"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_route53domains_delegation_signer_record`

- **Client:** `route53domains`
- **Method:** `get_domain_detail`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "DomainName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_route53profiles_resource_association`

- **Client:** `route53profiles`
- **Method:** `list_profile_resource_associations`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ProfileId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_route53recoverycontrolconfig_routing_control`

- **Client:** `route53-recovery-control-config`
- **Method:** `list_routing_controls`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ControlPanelArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_route53recoverycontrolconfig_safety_rule`

- **Client:** `route53-recovery-control-config`
- **Method:** `list_safety_rules`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ControlPanelArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_route53recoveryreadiness_cell`

- **Client:** `route53-recovery-readiness`
- **Method:** `list_cells`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Could not connect to the endpoint URL: "https://route53-recovery-readiness.us-east-1.amazonaws.com/cells"

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_route53recoveryreadiness_readiness_check`

- **Client:** `route53-recovery-readiness`
- **Method:** `list_readiness_checks`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Could not connect to the endpoint URL: "https://route53-recovery-readiness.us-east-1.amazonaws.com/readinesschecks"

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_route53recoveryreadiness_recovery_group`

- **Client:** `route53-recovery-readiness`
- **Method:** `list_recovery_groups`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Could not connect to the endpoint URL: "https://route53-recovery-readiness.us-east-1.amazonaws.com/recoverygroups"

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_route53recoveryreadiness_resource_set`

- **Client:** `route53-recovery-readiness`
- **Method:** `list_resource_sets`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Could not connect to the endpoint URL: "https://route53-recovery-readiness.us-east-1.amazonaws.com/resourcesets"

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_s3_access_point`

- **Client:** `s3control`
- **Method:** `list_access_points`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
AccountId is required but not set

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_s3_account_public_access_block`

- **Client:** `s3`
- **Method:** `get_public_access_block`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Bucket"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3_bucket_abac`

- **Client:** `s3`
- **Method:** `get_bucket_abac`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Bucket"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3_bucket_accelerate_configuration`

- **Client:** `s3`
- **Method:** `get_bucket_accelerate_configuration`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Bucket"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3_bucket_acl`

- **Client:** `s3`
- **Method:** `get_bucket_acl`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Bucket"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3_bucket_analytics_configuration`

- **Client:** `s3`
- **Method:** `get_bucket_analytics_configuration`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Bucket"
Missing required parameter in input: "Id"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3_bucket_cors_configuration`

- **Client:** `s3`
- **Method:** `get_bucket_cors`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Bucket"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3_bucket_intelligent_tiering_configuration`

- **Client:** `s3`
- **Method:** `get_bucket_intelligent_tiering_configuration`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Bucket"
Missing required parameter in input: "Id"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3_bucket_inventory`

- **Client:** `s3`
- **Method:** `get_bucket_inventory_configuration`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Bucket"
Missing required parameter in input: "Id"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3_bucket_inventory_configuration`

- **Client:** `s3`
- **Method:** `list_bucket_inventory_configurations`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Bucket"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3_bucket_lifecycle_configuration`

- **Client:** `s3`
- **Method:** `get_bucket_lifecycle_configuration`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Bucket"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3_bucket_logging`

- **Client:** `s3`
- **Method:** `get_bucket_logging`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Bucket"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3_bucket_metadata_configuration`

- **Client:** `s3`
- **Method:** `get_bucket_metadata_configuration`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Bucket"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3_bucket_metric`

- **Client:** `s3`
- **Method:** `get_bucket_metrics_configuration`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Bucket"
Missing required parameter in input: "Id"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3_bucket_metrics_configuration`

- **Client:** `s3`
- **Method:** `list_bucket_metrics_configurations`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Bucket"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3_bucket_notification`

- **Client:** `s3`
- **Method:** `get_bucket_notification_configuration`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Bucket"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3_bucket_object`

- **Client:** `s3`
- **Method:** `get_object`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Bucket"
Missing required parameter in input: "Key"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3_bucket_object_lock_configuration`

- **Client:** `s3`
- **Method:** `get_object_lock_configuration`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Bucket"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3_bucket_ownership_controls`

- **Client:** `s3`
- **Method:** `get_bucket_ownership_controls`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Bucket"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3_bucket_policy`

- **Client:** `s3`
- **Method:** `get_bucket_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Bucket"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3_bucket_public_access_block`

- **Client:** `s3`
- **Method:** `get_public_access_block`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Bucket"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3_bucket_replication_configuration`

- **Client:** `s3`
- **Method:** `get_bucket_replication`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Bucket"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3_bucket_request_payment_configuration`

- **Client:** `s3`
- **Method:** `get_bucket_request_payment`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Bucket"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3_bucket_server_side_encryption_configuration`

- **Client:** `s3`
- **Method:** `get_bucket_encryption`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Bucket"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3_bucket_versioning`

- **Client:** `s3`
- **Method:** `get_bucket_versioning`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Bucket"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3_bucket_website_configuration`

- **Client:** `s3`
- **Method:** `get_bucket_website`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Bucket"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3_object`

- **Client:** `s3`
- **Method:** `get_object`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Bucket"
Missing required parameter in input: "Key"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3_object_copy`

- **Client:** `s3`
- **Method:** `get_object`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Bucket"
Missing required parameter in input: "Key"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3control_access_grant`

- **Client:** `s3control`
- **Method:** `list_access_grants`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
AccountId is required but not set

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_s3control_access_grants_instance`

- **Client:** `s3control`
- **Method:** `list_access_grants`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
AccountId is required but not set

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_s3control_access_grants_instance_resource_policy`

- **Client:** `s3control`
- **Method:** `list_access_grants`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
AccountId is required but not set

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_s3control_access_grants_location`

- **Client:** `s3control`
- **Method:** `list_access_grants`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
AccountId is required but not set

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_s3control_access_point_policy`

- **Client:** `s3control`
- **Method:** `get_access_point_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
AccountId is required but not set

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_s3control_bucket_lifecycle_configuration`

- **Client:** `s3control`
- **Method:** `get_bucket_lifecycle_configuration`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
AccountId is required but not set

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_s3control_bucket_policy`

- **Client:** `s3control`
- **Method:** `get_bucket_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
AccountId is required but not set

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_s3control_directory_bucket_access_point_scope`

- **Client:** `s3control`
- **Method:** `get_access_point_policy_for_object_lambda`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
AccountId is required but not set

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_s3control_multi_region_access_point`

- **Client:** `s3control`
- **Method:** `list_access_points`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
AccountId is required but not set

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_s3control_multi_region_access_point_policy`

- **Client:** `s3control`
- **Method:** `list_access_points`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
AccountId is required but not set

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_s3control_object_lambda_access_point`

- **Client:** `s3control`
- **Method:** `list_access_points`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
AccountId is required but not set

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_s3control_object_lambda_access_point_policy`

- **Client:** `s3control`
- **Method:** `list_access_points`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
AccountId is required but not set

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_s3control_storage_lens_configuration`

- **Client:** `s3control`
- **Method:** `get_storage_lens_configuration`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
AccountId is required but not set

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_s3tables_namespace`

- **Client:** `s3tables`
- **Method:** `list_namespaces`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "tableBucketARN"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3tables_table`

- **Client:** `s3tables`
- **Method:** `list_tables`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "tableBucketARN"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3tables_table_bucket_policy`

- **Client:** `s3tables`
- **Method:** `get_table_bucket_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "tableBucketARN"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3tables_table_bucket_replication`

- **Client:** `s3tables`
- **Method:** `get_table_bucket_replication`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "tableBucketARN"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3tables_table_policy`

- **Client:** `s3tables`
- **Method:** `get_table_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "tableBucketARN"
Missing required parameter in input: "namespace"
Missing required parameter in input: "name"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_s3vectors_index`

- **Client:** `s3vectors`
- **Method:** `list_indexes`
- **Error Code:** `ValidationException`
- **Error Type:** `invalid_parameters`

**Error:** Invalid parameters: Must specify either vectorBucketName or vectorBucketArn but not both

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_s3vectors_vector_bucket_policy`

- **Client:** `s3vectors`
- **Method:** `get_vector_bucket_policy`
- **Error Code:** `ValidationException`
- **Error Type:** `invalid_parameters`

**Error:** Invalid parameters: Must specify either vectorBucketName or vectorBucketArn but not both

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_sagemaker_device`

- **Client:** `sagemaker`
- **Method:** `list_devices`
- **Error Code:** `ThrottlingException`
- **Error Type:** `rate_limited`

**Error:** Rate limited: Rate exceeded

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_sagemaker_device_fleet`

- **Client:** `sagemaker`
- **Method:** `list_device_fleets`
- **Error Code:** `ThrottlingException`
- **Error Type:** `rate_limited`

**Error:** Rate limited: Rate exceeded

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_sagemaker_image_version`

- **Client:** `sagemaker`
- **Method:** `list_image_versions`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ImageName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_sagemaker_model_package_group_policy`

- **Client:** `sagemaker`
- **Method:** `get_model_package_group_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ModelPackageGroupName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_schemas_schema`

- **Client:** `schemas`
- **Method:** `list_schemas`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "RegistryName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_secretsmanager_secret_policy`

- **Client:** `secretsmanager`
- **Method:** `get_resource_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "SecretId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_secretsmanager_secret_rotation`

- **Client:** `secretsmanager`
- **Method:** `describe_secret`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "SecretId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_secretsmanager_secret_version`

- **Client:** `secretsmanager`
- **Method:** `list_secret_version_ids`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "SecretId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_securityhub_organization_configuration`

- **Client:** `securityhub`
- **Method:** `describe_organization_configuration`
- **Error Code:** `InvalidAccessException`
- **Error Type:** `api_error`

**Error:** API error (InvalidAccessException): Account 566972129213 is not an administrator for this organization

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_securityhub_standards_control`

- **Client:** `securityhub`
- **Method:** `describe_standards_controls`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "StandardsSubscriptionArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_securityhub_standards_control_association`

- **Client:** `securityhub`
- **Method:** `list_standards_control_associations`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "SecurityControlId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_securitylake_subscriber_notification`

- **Client:** `securitylake`
- **Method:** `get_subscriber`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "subscriberId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_serverlessapplicationrepository_cloudformation_stack`

- **Client:** `serverlessrepo`
- **Method:** `list_application_versions`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ApplicationId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_service_discovery_instance`

- **Client:** `servicediscovery`
- **Method:** `list_instances`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ServiceId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_servicecatalog_constraint`

- **Client:** `servicecatalog`
- **Method:** `list_constraints_for_portfolio`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "PortfolioId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_servicecatalog_provisioning_artifact`

- **Client:** `servicecatalog`
- **Method:** `list_provisioning_artifacts`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ProductId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_servicequotas_service_quota`

- **Client:** `service-quotas`
- **Method:** `list_service_quotas`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ServiceCode"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ses_receipt_rule`

- **Client:** `ses`
- **Method:** `describe_receipt_rule`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "RuleSetName"
Missing required parameter in input: "RuleName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ses_receipt_rule_set`

- **Client:** `ses`
- **Method:** `describe_receipt_rule_set`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "RuleSetName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_sesv2_configuration_set_event_destination`

- **Client:** `sesv2`
- **Method:** `get_configuration_set_event_destinations`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ConfigurationSetName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_sesv2_email_identity_feedback_attributes`

- **Client:** `sesv2`
- **Method:** `get_email_identity`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "EmailIdentity"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_sesv2_email_identity_mail_from_attributes`

- **Client:** `sesv2`
- **Method:** `get_email_identity`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "EmailIdentity"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_sesv2_email_identity_policy`

- **Client:** `sesv2`
- **Method:** `get_email_identity_policies`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "EmailIdentity"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_sfn_alias`

- **Client:** `stepfunctions`
- **Method:** `list_state_machine_aliases`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "stateMachineArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_shield_proactive_engagement`

- **Client:** `shield`
- **Method:** `describe_emergency_contact_settings`
- **Error Code:** `ResourceNotFoundException`
- **Error Type:** `api_error`

**Error:** API error (ResourceNotFoundException): The subscription does not exist.

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_shield_protection`

- **Client:** `shield`
- **Method:** `list_protections`
- **Error Code:** `ResourceNotFoundException`
- **Error Type:** `api_error`

**Error:** API error (ResourceNotFoundException): The subscription does not exist.

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_shield_protection_group`

- **Client:** `shield`
- **Method:** `list_protection_groups`
- **Error Code:** `ResourceNotFoundException`
- **Error Type:** `api_error`

**Error:** API error (ResourceNotFoundException): The subscription does not exist.

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_shield_subscription`

- **Client:** `shield`
- **Method:** `describe_subscription`
- **Error Code:** `ResourceNotFoundException`
- **Error Type:** `api_error`

**Error:** API error (ResourceNotFoundException): The subscription does not exist.

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_signer_signing_profile_permission`

- **Client:** `signer`
- **Method:** `list_profile_permissions`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "profileName"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_sns_topic_data_protection_policy`

- **Client:** `sns`
- **Method:** `get_data_protection_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ResourceArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_sns_topic_policy`

- **Client:** `sns`
- **Method:** `get_topic_attributes`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "TopicArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_sns_topic_subscription`

- **Client:** `sns`
- **Method:** `list_subscriptions_by_topic`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "TopicArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_spot_datafeed_subscription`

- **Client:** `ec2`
- **Method:** `describe_spot_datafeed_subscription`
- **Error Code:** `InvalidSpotDatafeed.NotFound`
- **Error Type:** `api_error`

**Error:** API error (InvalidSpotDatafeed.NotFound): Spot datafeed subscription does not exist.

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_sqs_queue_policy`

- **Client:** `sqs`
- **Method:** `get_queue_attributes`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "QueueUrl"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_sqs_queue_redrive_allow_policy`

- **Client:** `sqs`
- **Method:** `get_queue_attributes`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "QueueUrl"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_sqs_queue_redrive_policy`

- **Client:** `sqs`
- **Method:** `get_queue_attributes`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "QueueUrl"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ssm_maintenance_window_target`

- **Client:** `ssm`
- **Method:** `describe_maintenance_window_targets`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "WindowId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ssm_maintenance_window_task`

- **Client:** `ssm`
- **Method:** `describe_maintenance_window_tasks`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "WindowId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ssm_service_setting`

- **Client:** `ssm`
- **Method:** `get_service_setting`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "SettingId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ssmcontacts_contact_channel`

- **Client:** `ssm-contacts`
- **Method:** `list_contact_channels`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ContactId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ssmcontacts_plan`

- **Client:** `ssm-contacts`
- **Method:** `get_contact`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ContactId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ssmcontacts_rotation`

- **Client:** `ssm-contacts`
- **Method:** `list_rotations`
- **Error Code:** `ValidationException`
- **Error Type:** `invalid_parameters`

**Error:** Invalid parameters: Invalid value provided - Account not found for the request

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_ssmquicksetup_configuration_manager`

- **Client:** `ssmquicksetup`
- **Method:** `list_configuration_managers`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Unknown service: 'ssmquicksetup'. Valid service names are: accessanalyzer, account, acm, acm-pca, aiops, amp, amplify, amplifybackend, amplifyuibuilder, apigateway, apigatewaymanagementapi, apigatewayv2, appconfig, appconfigdata, appfabric, appflow, appintegrations, application-autoscaling, application-insights, application-signals, applicationcostprofiler, appmesh, apprunner, appstream, appsync, arc-region-switch, arc-zonal-shift, artifact, athena, auditmanager, autoscaling, autoscaling-plans, b2bi, backup, backup-gateway, backupsearch, batch, bcm-dashboards, bcm-data-exports, bcm-pricing-calculator, bcm-recommended-actions, bedrock, bedrock-agent, bedrock-agent-runtime, bedrock-agentcore, bedrock-agentcore-control, bedrock-data-automation, bedrock-data-automation-runtime, bedrock-runtime, billing, billingconductor, braket, budgets, ce, chatbot, chime, chime-sdk-identity, chime-sdk-media-pipelines, chime-sdk-meetings, chime-sdk-messaging, chime-sdk-voice, cleanrooms, cleanroomsml, cloud9, cloudcontrol, clouddirectory, cloudformation, cloudfront, cloudfront-keyvaluestore, cloudhsm, cloudhsmv2, cloudsearch, cloudsearchdomain, cloudtrail, cloudtrail-data, cloudwatch, codeartifact, codebuild, codecatalyst, codecommit, codeconnections, codedeploy, codeguru-reviewer, codeguru-security, codeguruprofiler, codepipeline, codestar-connections, codestar-notifications, cognito-identity, cognito-idp, cognito-sync, comprehend, comprehendmedical, compute-optimizer, compute-optimizer-automation, config, connect, connect-contact-lens, connectcampaigns, connectcampaignsv2, connectcases, connectparticipant, controlcatalog, controltower, cost-optimization-hub, cur, customer-profiles, databrew, dataexchange, datapipeline, datasync, datazone, dax, deadline, detective, devicefarm, devops-guru, directconnect, discovery, dlm, dms, docdb, docdb-elastic, drs, ds, ds-data, dsql, dynamodb, dynamodbstreams, ebs, ec2, ec2-instance-connect, ec2-mercury, ecr, ecr-public, ecs, efs, eks, eks-auth, elasticache, elasticbeanstalk, elastictranscoder, elb, elbv2, emr, emr-containers, emr-serverless, entityresolution, es, events, evidently, evs, finspace, finspace-data, firehose, fis, fms, forecast, forecastquery, frauddetector, freetier, fsx, gamelift, gameliftstreams, geo-maps, geo-places, geo-routes, glacier, globalaccelerator, glue, grafana, greengrass, greengrassv2, groundstation, guardduty, health, healthlake, iam, identitystore, imagebuilder, importexport, inspector, inspector-scan, inspector2, internetmonitor, invoicing, iot, iot-data, iot-jobs-data, iot-managed-integrations, iotanalytics, iotdeviceadvisor, iotevents, iotevents-data, iotfleetwise, iotsecuretunneling, iotsitewise, iotthingsgraph, iottwinmaker, iotwireless, ivs, ivs-realtime, ivschat, kafka, kafkaconnect, kendra, kendra-ranking, keyspaces, keyspacesstreams, kinesis, kinesis-video-archived-media, kinesis-video-media, kinesis-video-signaling, kinesis-video-webrtc-storage, kinesisanalytics, kinesisanalyticsv2, kinesisvideo, kms, lakeformation, lambda, launch-wizard, lex-models, lex-runtime, lexv2-models, lexv2-runtime, license-manager, license-manager-linux-subscriptions, license-manager-user-subscriptions, lightsail, location, logs, lookoutequipment, m2, machinelearning, macie2, mailmanager, managedblockchain, managedblockchain-query, marketplace-agreement, marketplace-catalog, marketplace-deployment, marketplace-entitlement, marketplace-reporting, marketplacecommerceanalytics, mediaconnect, mediaconvert, medialive, mediapackage, mediapackage-vod, mediapackagev2, mediastore, mediastore-data, mediatailor, medical-imaging, memorydb, meteringmarketplace, mgh, mgn, migration-hub-refactor-spaces, migrationhub-config, migrationhuborchestrator, migrationhubstrategy, mpa, mq, mturk, mwaa, mwaa-serverless, neptune, neptune-graph, neptunedata, network-firewall, networkflowmonitor, networkmanager, networkmonitor, notifications, notificationscontacts, nova-act, oam, observabilityadmin, odb, omics, opensearch, opensearchserverless, organizations, osis, outposts, panorama, partnercentral-account, partnercentral-benefits, partnercentral-channel, partnercentral-selling, payment-cryptography, payment-cryptography-data, pca-connector-ad, pca-connector-scep, pcs, personalize, personalize-events, personalize-runtime, pi, pinpoint, pinpoint-email, pinpoint-sms-voice, pinpoint-sms-voice-v2, pipes, polly, pricing, proton, qapps, qbusiness, qconnect, quicksight, ram, rbin, rds, rds-data, redshift, redshift-data, redshift-serverless, rekognition, repostspace, resiliencehub, resource-explorer-2, resource-groups, resourcegroupstaggingapi, rolesanywhere, route53, route53-recovery-cluster, route53-recovery-control-config, route53-recovery-readiness, route53domains, route53globalresolver, route53profiles, route53resolver, rtbfabric, rum, s3, s3control, s3outposts, s3tables, s3vectors, sagemaker, sagemaker-a2i-runtime, sagemaker-edge, sagemaker-featurestore-runtime, sagemaker-geospatial, sagemaker-metrics, sagemaker-runtime, savingsplans, scheduler, schemas, sdb, secretsmanager, security-ir, securityhub, securitylake, serverlessrepo, service-quotas, servicecatalog, servicecatalog-appregistry, servicediscovery, ses, sesv2, shield, signer, signin, simspaceweaver, sms-voice, snow-device-management, snowball, sns, socialmessaging, sqs, ssm, ssm-contacts, ssm-guiconnect, ssm-incidents, ssm-quicksetup, ssm-sap, sso, sso-admin, sso-oidc, stepfunctions, storagegateway, sts, supplychain, support, support-app, swf, synthetics, taxsettings, textract, timestream-influxdb, timestream-query, timestream-write, tnb, transcribe, transfer, translate, trustedadvisor, verifiedpermissions, voice-id, vpc-lattice, vpc-lattice-preview, vpc-service-network, waf, waf-regional, wafv2, wellarchitected, wickr, wisdom, workdocs, workmail, workmailmessageflow, workspaces, workspaces-instances, workspaces-thin-client, workspaces-web, xray

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_ssoadmin_account_assignment`

- **Client:** `sso-admin`
- **Method:** `list_account_assignments`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "InstanceArn"
Missing required parameter in input: "AccountId"
Missing required parameter in input: "PermissionSetArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ssoadmin_application`

- **Client:** `sso-admin`
- **Method:** `list_applications`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "InstanceArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ssoadmin_application_access_scope`

- **Client:** `sso-admin`
- **Method:** `list_application_access_scopes`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ApplicationArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ssoadmin_application_assignment`

- **Client:** `sso-admin`
- **Method:** `list_application_assignments`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ApplicationArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ssoadmin_permission_set`

- **Client:** `sso-admin`
- **Method:** `list_permission_sets`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "InstanceArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_ssoadmin_trusted_token_issuer`

- **Client:** `sso-admin`
- **Method:** `list_trusted_token_issuers`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "InstanceArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_storagegateway_cache`

- **Client:** `storagegateway`
- **Method:** `describe_cache`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "GatewayARN"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_storagegateway_cached_iscsi_volume`

- **Client:** `storagegateway`
- **Method:** `describe_cached_iscsi_volumes`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "VolumeARNs"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_storagegateway_file_system_association`

- **Client:** `storagegateway`
- **Method:** `describe_file_system_associations`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "FileSystemAssociationARNList"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_storagegateway_nfs_file_share`

- **Client:** `storagegateway`
- **Method:** `describe_nfs_file_shares`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "FileShareARNList"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_storagegateway_smb_file_share`

- **Client:** `storagegateway`
- **Method:** `describe_smb_file_shares`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "FileShareARNList"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_storagegateway_stored_iscsi_volume`

- **Client:** `storagegateway`
- **Method:** `describe_stored_iscsi_volumes`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "VolumeARNs"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_storagegateway_upload_buffer`

- **Client:** `storagegateway`
- **Method:** `describe_upload_buffer`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "GatewayARN"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_storagegateway_working_storage`

- **Client:** `storagegateway`
- **Method:** `describe_working_storage`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "GatewayARN"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_swf_domain`

- **Client:** `swf`
- **Method:** `list_domains`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "registrationStatus"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_transfer_access`

- **Client:** `transfer`
- **Method:** `list_accesses`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ServerId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_transfer_agreement`

- **Client:** `transfer`
- **Method:** `list_agreements`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ServerId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_transfer_host_key`

- **Client:** `transfer`
- **Method:** `describe_server`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ServerId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_transfer_user`

- **Client:** `transfer`
- **Method:** `list_users`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ServerId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_transfer_web_app_customization`

- **Client:** `transfer`
- **Method:** `describe_web_app`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "WebAppId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_verifiedpermissions_identity_source`

- **Client:** `verifiedpermissions`
- **Method:** `list_identity_sources`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "policyStoreId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_verifiedpermissions_policy`

- **Client:** `verifiedpermissions`
- **Method:** `list_policies`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "policyStoreId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_verifiedpermissions_policy_template`

- **Client:** `verifiedpermissions`
- **Method:** `list_policy_templates`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "policyStoreId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_verifiedpermissions_schema`

- **Client:** `verifiedpermissions`
- **Method:** `get_schema`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "policyStoreId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_vpc_block_public_access_exclusion`

- **Client:** `ec2`
- **Method:** `describe_vpc_block_public_access_exclusions`
- **Error Code:** `MissingParameter`
- **Error Type:** `api_error`

**Error:** API error (MissingParameter): One of the following parameters must be provided: ExclusionIds, MaxResults

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_vpc_ipam_pool_cidr`

- **Client:** `ec2`
- **Method:** `get_ipam_pool_cidrs`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "IpamPoolId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_vpc_ipam_pool_cidr_allocation`

- **Client:** `ec2`
- **Method:** `get_ipam_pool_allocations`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "IpamPoolId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_vpc_ipv6_cidr_block_association`

- **Client:** `ec2`
- **Method:** `get_associated_ipv6_pool_cidrs`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "PoolId"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_vpclattice_access_log_subscription`

- **Client:** `vpc-lattice`
- **Method:** `list_access_log_subscriptions`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "resourceIdentifier"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_vpclattice_auth_policy`

- **Client:** `vpc-lattice`
- **Method:** `get_auth_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "resourceIdentifier"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_vpclattice_domain_verification`

- **Client:** `vpc-lattice`
- **Method:** `get_service_network_service_association`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "serviceNetworkServiceAssociationIdentifier"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_vpclattice_listener`

- **Client:** `vpc-lattice`
- **Method:** `list_listeners`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "serviceIdentifier"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_vpclattice_listener_rule`

- **Client:** `vpc-lattice`
- **Method:** `list_rules`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "listenerIdentifier"
Missing required parameter in input: "serviceIdentifier"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_vpclattice_resource_policy`

- **Client:** `vpc-lattice`
- **Method:** `get_resource_policy`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "resourceArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_vpclattice_service_network_service_association`

- **Client:** `vpc-lattice`
- **Method:** `list_service_network_service_associations`
- **Error Code:** `ValidationException`
- **Error Type:** `invalid_parameters`

**Error:** Invalid parameters: Must provide at least one of: serviceNetworkIdentifier, serviceIdentifier

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_vpclattice_service_network_vpc_association`

- **Client:** `vpc-lattice`
- **Method:** `list_service_network_vpc_associations`
- **Error Code:** `ValidationException`
- **Error Type:** `invalid_parameters`

**Error:** Invalid parameters: Must provide at least one of: serviceNetworkIdentifier, vpcIdentifier

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_wafv2_api_key`

- **Client:** `wafv2`
- **Method:** `list_api_keys`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Scope"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_wafv2_ip_set`

- **Client:** `wafv2`
- **Method:** `list_ip_sets`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Scope"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_wafv2_regex_pattern_set`

- **Client:** `wafv2`
- **Method:** `list_regex_pattern_sets`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Scope"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_wafv2_rule_group`

- **Client:** `wafv2`
- **Method:** `list_rule_groups`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Scope"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_wafv2_web_acl`

- **Client:** `wafv2`
- **Method:** `list_web_acls`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "Scope"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_wafv2_web_acl_association`

- **Client:** `wafv2`
- **Method:** `list_resources_for_web_acl`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "WebACLArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_wafv2_web_acl_logging_configuration`

- **Client:** `wafv2`
- **Method:** `get_logging_configuration`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "ResourceArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_wafv2_web_acl_rule_group_association`

- **Client:** `wafv2`
- **Method:** `list_resources_for_web_acl`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "WebACLArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

### `aws_worklink_fleet`

- **Client:** `worklink`
- **Method:** `list_fleets`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Unknown service: 'worklink'. Valid service names are: accessanalyzer, account, acm, acm-pca, aiops, amp, amplify, amplifybackend, amplifyuibuilder, apigateway, apigatewaymanagementapi, apigatewayv2, appconfig, appconfigdata, appfabric, appflow, appintegrations, application-autoscaling, application-insights, application-signals, applicationcostprofiler, appmesh, apprunner, appstream, appsync, arc-region-switch, arc-zonal-shift, artifact, athena, auditmanager, autoscaling, autoscaling-plans, b2bi, backup, backup-gateway, backupsearch, batch, bcm-dashboards, bcm-data-exports, bcm-pricing-calculator, bcm-recommended-actions, bedrock, bedrock-agent, bedrock-agent-runtime, bedrock-agentcore, bedrock-agentcore-control, bedrock-data-automation, bedrock-data-automation-runtime, bedrock-runtime, billing, billingconductor, braket, budgets, ce, chatbot, chime, chime-sdk-identity, chime-sdk-media-pipelines, chime-sdk-meetings, chime-sdk-messaging, chime-sdk-voice, cleanrooms, cleanroomsml, cloud9, cloudcontrol, clouddirectory, cloudformation, cloudfront, cloudfront-keyvaluestore, cloudhsm, cloudhsmv2, cloudsearch, cloudsearchdomain, cloudtrail, cloudtrail-data, cloudwatch, codeartifact, codebuild, codecatalyst, codecommit, codeconnections, codedeploy, codeguru-reviewer, codeguru-security, codeguruprofiler, codepipeline, codestar-connections, codestar-notifications, cognito-identity, cognito-idp, cognito-sync, comprehend, comprehendmedical, compute-optimizer, compute-optimizer-automation, config, connect, connect-contact-lens, connectcampaigns, connectcampaignsv2, connectcases, connectparticipant, controlcatalog, controltower, cost-optimization-hub, cur, customer-profiles, databrew, dataexchange, datapipeline, datasync, datazone, dax, deadline, detective, devicefarm, devops-guru, directconnect, discovery, dlm, dms, docdb, docdb-elastic, drs, ds, ds-data, dsql, dynamodb, dynamodbstreams, ebs, ec2, ec2-instance-connect, ec2-mercury, ecr, ecr-public, ecs, efs, eks, eks-auth, elasticache, elasticbeanstalk, elastictranscoder, elb, elbv2, emr, emr-containers, emr-serverless, entityresolution, es, events, evidently, evs, finspace, finspace-data, firehose, fis, fms, forecast, forecastquery, frauddetector, freetier, fsx, gamelift, gameliftstreams, geo-maps, geo-places, geo-routes, glacier, globalaccelerator, glue, grafana, greengrass, greengrassv2, groundstation, guardduty, health, healthlake, iam, identitystore, imagebuilder, importexport, inspector, inspector-scan, inspector2, internetmonitor, invoicing, iot, iot-data, iot-jobs-data, iot-managed-integrations, iotanalytics, iotdeviceadvisor, iotevents, iotevents-data, iotfleetwise, iotsecuretunneling, iotsitewise, iotthingsgraph, iottwinmaker, iotwireless, ivs, ivs-realtime, ivschat, kafka, kafkaconnect, kendra, kendra-ranking, keyspaces, keyspacesstreams, kinesis, kinesis-video-archived-media, kinesis-video-media, kinesis-video-signaling, kinesis-video-webrtc-storage, kinesisanalytics, kinesisanalyticsv2, kinesisvideo, kms, lakeformation, lambda, launch-wizard, lex-models, lex-runtime, lexv2-models, lexv2-runtime, license-manager, license-manager-linux-subscriptions, license-manager-user-subscriptions, lightsail, location, logs, lookoutequipment, m2, machinelearning, macie2, mailmanager, managedblockchain, managedblockchain-query, marketplace-agreement, marketplace-catalog, marketplace-deployment, marketplace-entitlement, marketplace-reporting, marketplacecommerceanalytics, mediaconnect, mediaconvert, medialive, mediapackage, mediapackage-vod, mediapackagev2, mediastore, mediastore-data, mediatailor, medical-imaging, memorydb, meteringmarketplace, mgh, mgn, migration-hub-refactor-spaces, migrationhub-config, migrationhuborchestrator, migrationhubstrategy, mpa, mq, mturk, mwaa, mwaa-serverless, neptune, neptune-graph, neptunedata, network-firewall, networkflowmonitor, networkmanager, networkmonitor, notifications, notificationscontacts, nova-act, oam, observabilityadmin, odb, omics, opensearch, opensearchserverless, organizations, osis, outposts, panorama, partnercentral-account, partnercentral-benefits, partnercentral-channel, partnercentral-selling, payment-cryptography, payment-cryptography-data, pca-connector-ad, pca-connector-scep, pcs, personalize, personalize-events, personalize-runtime, pi, pinpoint, pinpoint-email, pinpoint-sms-voice, pinpoint-sms-voice-v2, pipes, polly, pricing, proton, qapps, qbusiness, qconnect, quicksight, ram, rbin, rds, rds-data, redshift, redshift-data, redshift-serverless, rekognition, repostspace, resiliencehub, resource-explorer-2, resource-groups, resourcegroupstaggingapi, rolesanywhere, route53, route53-recovery-cluster, route53-recovery-control-config, route53-recovery-readiness, route53domains, route53globalresolver, route53profiles, route53resolver, rtbfabric, rum, s3, s3control, s3outposts, s3tables, s3vectors, sagemaker, sagemaker-a2i-runtime, sagemaker-edge, sagemaker-featurestore-runtime, sagemaker-geospatial, sagemaker-metrics, sagemaker-runtime, savingsplans, scheduler, schemas, sdb, secretsmanager, security-ir, securityhub, securitylake, serverlessrepo, service-quotas, servicecatalog, servicecatalog-appregistry, servicediscovery, ses, sesv2, shield, signer, signin, simspaceweaver, sms-voice, snow-device-management, snowball, sns, socialmessaging, sqs, ssm, ssm-contacts, ssm-guiconnect, ssm-incidents, ssm-quicksetup, ssm-sap, sso, sso-admin, sso-oidc, stepfunctions, storagegateway, sts, supplychain, support, support-app, swf, synthetics, taxsettings, textract, timestream-influxdb, timestream-query, timestream-write, tnb, transcribe, transfer, translate, trustedadvisor, verifiedpermissions, voice-id, vpc-lattice, vpc-lattice-preview, vpc-service-network, waf, waf-regional, wafv2, wellarchitected, wickr, wisdom, workdocs, workmail, workmailmessageflow, workspaces, workspaces-instances, workspaces-thin-client, workspaces-web, xray

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_worklink_website_certificate_authority_association`

- **Client:** `worklink`
- **Method:** `list_website_certificate_authorities`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Unknown service: 'worklink'. Valid service names are: accessanalyzer, account, acm, acm-pca, aiops, amp, amplify, amplifybackend, amplifyuibuilder, apigateway, apigatewaymanagementapi, apigatewayv2, appconfig, appconfigdata, appfabric, appflow, appintegrations, application-autoscaling, application-insights, application-signals, applicationcostprofiler, appmesh, apprunner, appstream, appsync, arc-region-switch, arc-zonal-shift, artifact, athena, auditmanager, autoscaling, autoscaling-plans, b2bi, backup, backup-gateway, backupsearch, batch, bcm-dashboards, bcm-data-exports, bcm-pricing-calculator, bcm-recommended-actions, bedrock, bedrock-agent, bedrock-agent-runtime, bedrock-agentcore, bedrock-agentcore-control, bedrock-data-automation, bedrock-data-automation-runtime, bedrock-runtime, billing, billingconductor, braket, budgets, ce, chatbot, chime, chime-sdk-identity, chime-sdk-media-pipelines, chime-sdk-meetings, chime-sdk-messaging, chime-sdk-voice, cleanrooms, cleanroomsml, cloud9, cloudcontrol, clouddirectory, cloudformation, cloudfront, cloudfront-keyvaluestore, cloudhsm, cloudhsmv2, cloudsearch, cloudsearchdomain, cloudtrail, cloudtrail-data, cloudwatch, codeartifact, codebuild, codecatalyst, codecommit, codeconnections, codedeploy, codeguru-reviewer, codeguru-security, codeguruprofiler, codepipeline, codestar-connections, codestar-notifications, cognito-identity, cognito-idp, cognito-sync, comprehend, comprehendmedical, compute-optimizer, compute-optimizer-automation, config, connect, connect-contact-lens, connectcampaigns, connectcampaignsv2, connectcases, connectparticipant, controlcatalog, controltower, cost-optimization-hub, cur, customer-profiles, databrew, dataexchange, datapipeline, datasync, datazone, dax, deadline, detective, devicefarm, devops-guru, directconnect, discovery, dlm, dms, docdb, docdb-elastic, drs, ds, ds-data, dsql, dynamodb, dynamodbstreams, ebs, ec2, ec2-instance-connect, ec2-mercury, ecr, ecr-public, ecs, efs, eks, eks-auth, elasticache, elasticbeanstalk, elastictranscoder, elb, elbv2, emr, emr-containers, emr-serverless, entityresolution, es, events, evidently, evs, finspace, finspace-data, firehose, fis, fms, forecast, forecastquery, frauddetector, freetier, fsx, gamelift, gameliftstreams, geo-maps, geo-places, geo-routes, glacier, globalaccelerator, glue, grafana, greengrass, greengrassv2, groundstation, guardduty, health, healthlake, iam, identitystore, imagebuilder, importexport, inspector, inspector-scan, inspector2, internetmonitor, invoicing, iot, iot-data, iot-jobs-data, iot-managed-integrations, iotanalytics, iotdeviceadvisor, iotevents, iotevents-data, iotfleetwise, iotsecuretunneling, iotsitewise, iotthingsgraph, iottwinmaker, iotwireless, ivs, ivs-realtime, ivschat, kafka, kafkaconnect, kendra, kendra-ranking, keyspaces, keyspacesstreams, kinesis, kinesis-video-archived-media, kinesis-video-media, kinesis-video-signaling, kinesis-video-webrtc-storage, kinesisanalytics, kinesisanalyticsv2, kinesisvideo, kms, lakeformation, lambda, launch-wizard, lex-models, lex-runtime, lexv2-models, lexv2-runtime, license-manager, license-manager-linux-subscriptions, license-manager-user-subscriptions, lightsail, location, logs, lookoutequipment, m2, machinelearning, macie2, mailmanager, managedblockchain, managedblockchain-query, marketplace-agreement, marketplace-catalog, marketplace-deployment, marketplace-entitlement, marketplace-reporting, marketplacecommerceanalytics, mediaconnect, mediaconvert, medialive, mediapackage, mediapackage-vod, mediapackagev2, mediastore, mediastore-data, mediatailor, medical-imaging, memorydb, meteringmarketplace, mgh, mgn, migration-hub-refactor-spaces, migrationhub-config, migrationhuborchestrator, migrationhubstrategy, mpa, mq, mturk, mwaa, mwaa-serverless, neptune, neptune-graph, neptunedata, network-firewall, networkflowmonitor, networkmanager, networkmonitor, notifications, notificationscontacts, nova-act, oam, observabilityadmin, odb, omics, opensearch, opensearchserverless, organizations, osis, outposts, panorama, partnercentral-account, partnercentral-benefits, partnercentral-channel, partnercentral-selling, payment-cryptography, payment-cryptography-data, pca-connector-ad, pca-connector-scep, pcs, personalize, personalize-events, personalize-runtime, pi, pinpoint, pinpoint-email, pinpoint-sms-voice, pinpoint-sms-voice-v2, pipes, polly, pricing, proton, qapps, qbusiness, qconnect, quicksight, ram, rbin, rds, rds-data, redshift, redshift-data, redshift-serverless, rekognition, repostspace, resiliencehub, resource-explorer-2, resource-groups, resourcegroupstaggingapi, rolesanywhere, route53, route53-recovery-cluster, route53-recovery-control-config, route53-recovery-readiness, route53domains, route53globalresolver, route53profiles, route53resolver, rtbfabric, rum, s3, s3control, s3outposts, s3tables, s3vectors, sagemaker, sagemaker-a2i-runtime, sagemaker-edge, sagemaker-featurestore-runtime, sagemaker-geospatial, sagemaker-metrics, sagemaker-runtime, savingsplans, scheduler, schemas, sdb, secretsmanager, security-ir, securityhub, securitylake, serverlessrepo, service-quotas, servicecatalog, servicecatalog-appregistry, servicediscovery, ses, sesv2, shield, signer, signin, simspaceweaver, sms-voice, snow-device-management, snowball, sns, socialmessaging, sqs, ssm, ssm-contacts, ssm-guiconnect, ssm-incidents, ssm-quicksetup, ssm-sap, sso, sso-admin, sso-oidc, stepfunctions, storagegateway, sts, supplychain, support, support-app, swf, synthetics, taxsettings, textract, timestream-influxdb, timestream-query, timestream-write, tnb, transcribe, transfer, translate, trustedadvisor, verifiedpermissions, voice-id, vpc-lattice, vpc-lattice-preview, vpc-service-network, waf, waf-regional, wafv2, wellarchitected, wickr, wisdom, workdocs, workmail, workmailmessageflow, workspaces, workspaces-instances, workspaces-thin-client, workspaces-web, xray

**Action Needed:**
1. Investigate the API error
2. May need different parameters or approach
3. Check AWS documentation for this API method

### `aws_workspacesweb_identity_provider`

- **Client:** `workspaces-web`
- **Method:** `list_identity_providers`
- **Error Type:** `unexpected_error`

**Error:** Unexpected error: Parameter validation failed:
Missing required parameter in input: "portalArn"

**Action Needed:**
1. This resource requires parent resource ID(s) to list
2. Verify it's documented in needid_dict.py
3. Ensure get function accepts parent ID parameter
4. This is expected behavior - not an error in aws_dict.py

## ✅ Valid Resources

The following 731 resources passed all validation checks:

### accessanalyzer_analyzer

- `aws_accessanalyzer_analyzer`

### account_region

- `aws_account_region`

### acm_certificate

- `aws_acm_certificate`
- `aws_acm_certificate_validation`

### acmpca_certificate

- `aws_acmpca_certificate_authority`
- `aws_acmpca_certificate_authority_certificate`

### alb

- `aws_alb`

### amplify_app

- `aws_amplify_app`

### api_gateway

- `aws_api_gateway_account`
- `aws_api_gateway_api_key`
- `aws_api_gateway_client_certificate`
- `aws_api_gateway_domain_name`
- `aws_api_gateway_domain_name_access_association`
- `aws_api_gateway_rest_api`
- `aws_api_gateway_rest_api_put`
- `aws_api_gateway_usage_plan`
- `aws_api_gateway_vpc_link`

### apigatewayv2_api

- `aws_apigatewayv2_api`

### apigatewayv2_domain

- `aws_apigatewayv2_domain_name`

### apigatewayv2_vpc

- `aws_apigatewayv2_vpc_link`

### app_cookie

- `aws_app_cookie_stickiness_policy`

### appconfig_application

- `aws_appconfig_application`

### appconfig_deployment

- `aws_appconfig_deployment_strategy`

### appconfig_extension

- `aws_appconfig_extension`
- `aws_appconfig_extension_association`

### appfabric_app

- `aws_appfabric_app_bundle`

### appflow_connector

- `aws_appflow_connector_profile`

### appflow_flow

- `aws_appflow_flow`

### appintegrations_data

- `aws_appintegrations_data_integration`

### appintegrations_event

- `aws_appintegrations_event_integration`

### applicationinsights_application

- `aws_applicationinsights_application`

### appmesh_mesh

- `aws_appmesh_mesh`

### apprunner_connection

- `aws_apprunner_connection`

### apprunner_observability

- `aws_apprunner_observability_configuration`

### apprunner_service

- `aws_apprunner_service`

### apprunner_vpc

- `aws_apprunner_vpc_connector`
- `aws_apprunner_vpc_ingress_connection`

### appstream_directory

- `aws_appstream_directory_config`

### appstream_fleet

- `aws_appstream_fleet`

### appstream_image

- `aws_appstream_image_builder`

### appstream_stack

- `aws_appstream_stack`

### appsync_api

- `aws_appsync_api`

### appsync_domain

- `aws_appsync_domain_name`

### athena_capacity

- `aws_athena_capacity_reservation`

### athena_data

- `aws_athena_data_catalog`

### athena_named

- `aws_athena_named_query`

### autoscaling_group

- `aws_autoscaling_group`
- `aws_autoscaling_group_tag`

### autoscaling_policy

- `aws_autoscaling_policy`

### autoscaling_schedule

- `aws_autoscaling_schedule`

### autoscalingplans_scaling

- `aws_autoscalingplans_scaling_plan`

### backup_framework

- `aws_backup_framework`

### backup_logically

- `aws_backup_logically_air_gapped_vault`

### backup_plan

- `aws_backup_plan`

### backup_report

- `aws_backup_report_plan`

### backup_restore

- `aws_backup_restore_testing_plan`

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

### bedrockagent_flow

- `aws_bedrockagent_flow`

### bedrockagent_knowledge

- `aws_bedrockagent_knowledge_base`

### bedrockagent_prompt

- `aws_bedrockagent_prompt`

### bedrockagentcore_agent

- `aws_bedrockagentcore_agent_runtime`

### bedrockagentcore_api

- `aws_bedrockagentcore_api_key_credential_provider`

### bedrockagentcore_browser

- `aws_bedrockagentcore_browser`

### bedrockagentcore_code

- `aws_bedrockagentcore_code_interpreter`

### bedrockagentcore_gateway

- `aws_bedrockagentcore_gateway`

### bedrockagentcore_memory

- `aws_bedrockagentcore_memory`

### bedrockagentcore_oauth2

- `aws_bedrockagentcore_oauth2_credential_provider`

### bedrockagentcore_workload

- `aws_bedrockagentcore_workload_identity`

### billing_view

- `aws_billing_view`

### ce_anomaly

- `aws_ce_anomaly_monitor`
- `aws_ce_anomaly_subscription`

### ce_cost

- `aws_ce_cost_allocation_tag`

### chime_voice

- `aws_chime_voice_connector`
- `aws_chime_voice_connector_group`

### chimesdkvoice_sip

- `aws_chimesdkvoice_sip_media_application`
- `aws_chimesdkvoice_sip_rule`

### chimesdkvoice_voice

- `aws_chimesdkvoice_voice_profile_domain`

### cleanrooms_collaboration

- `aws_cleanrooms_collaboration`

### cleanrooms_configured

- `aws_cleanrooms_configured_table`

### cleanrooms_membership

- `aws_cleanrooms_membership`

### cloud9_environment

- `aws_cloud9_environment_ec2`
- `aws_cloud9_environment_membership`

### cloudformation_stack

- `aws_cloudformation_stack`
- `aws_cloudformation_stack_set`

### cloudformation_type

- `aws_cloudformation_type`

### cloudfront_trust

- `aws_cloudfront_trust_store`

### cloudhsm_v2

- `aws_cloudhsm_v2_cluster`
- `aws_cloudhsm_v2_hsm`

### cloudtrail

- `aws_cloudtrail`

### cloudtrail_event

- `aws_cloudtrail_event_data_store`

### cloudtrail_organization

- `aws_cloudtrail_organization_delegated_admin_account`

### cloudwatch_composite

- `aws_cloudwatch_composite_alarm`

### cloudwatch_contributor

- `aws_cloudwatch_contributor_insight_rule`
- `aws_cloudwatch_contributor_managed_insight_rule`

### cloudwatch_dashboard

- `aws_cloudwatch_dashboard`

### cloudwatch_event

- `aws_cloudwatch_event_api_destination`
- `aws_cloudwatch_event_archive`
- `aws_cloudwatch_event_bus`
- `aws_cloudwatch_event_connection`
- `aws_cloudwatch_event_endpoint`
- `aws_cloudwatch_event_rule`

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

### cloudwatch_metric

- `aws_cloudwatch_metric_alarm`
- `aws_cloudwatch_metric_stream`

### cloudwatch_query

- `aws_cloudwatch_query_definition`

### codeartifact_domain

- `aws_codeartifact_domain`

### codeartifact_repository

- `aws_codeartifact_repository`

### codebuild_fleet

- `aws_codebuild_fleet`

### codebuild_project

- `aws_codebuild_project`

### codebuild_report

- `aws_codebuild_report_group`

### codebuild_source

- `aws_codebuild_source_credential`

### codecommit_approval

- `aws_codecommit_approval_rule_template`

### codecommit_repository

- `aws_codecommit_repository`

### codeconnections_connection

- `aws_codeconnections_connection`

### codeconnections_host

- `aws_codeconnections_host`

### codedeploy_app

- `aws_codedeploy_app`

### codedeploy_deployment

- `aws_codedeploy_deployment_config`

### codeguruprofiler_profiling

- `aws_codeguruprofiler_profiling_group`

### codepipeline

- `aws_codepipeline`

### codepipeline_custom

- `aws_codepipeline_custom_action_type`

### codepipeline_webhook

- `aws_codepipeline_webhook`

### codestarconnections_connection

- `aws_codestarconnections_connection`

### codestarconnections_host

- `aws_codestarconnections_host`

### codestarnotifications_notification

- `aws_codestarnotifications_notification_rule`

### computeoptimizer_enrollment

- `aws_computeoptimizer_enrollment_status`

### config_aggregate

- `aws_config_aggregate_authorization`

### config_config

- `aws_config_config_rule`

### config_configuration

- `aws_config_configuration_aggregator`
- `aws_config_configuration_recorder`
- `aws_config_configuration_recorder_status`

### config_conformance

- `aws_config_conformance_pack`

### config_delivery

- `aws_config_delivery_channel`

### config_organization

- `aws_config_organization_conformance_pack`
- `aws_config_organization_custom_policy_rule`
- `aws_config_organization_custom_rule`
- `aws_config_organization_managed_rule`

### config_retention

- `aws_config_retention_configuration`

### connect_instance

- `aws_connect_instance`

### connect_phone

- `aws_connect_phone_number_contact_flow_association`

### controltower_landing

- `aws_controltower_landing_zone`

### cur_report

- `aws_cur_report_definition`

### customer_gateway

- `aws_customer_gateway`

### customerprofiles_domain

- `aws_customerprofiles_domain`

### dataexchange_data

- `aws_dataexchange_data_set`

### dataexchange_event

- `aws_dataexchange_event_action`

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

### datazone_domain

- `aws_datazone_domain`

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

### db_option

- `aws_db_option_group`

### db_parameter

- `aws_db_parameter_group`

### db_proxy

- `aws_db_proxy`
- `aws_db_proxy_endpoint`

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

### detective_graph

- `aws_detective_graph`

### devopsguru_notification

- `aws_devopsguru_notification_channel`

### directory_service

- `aws_directory_service_directory`
- `aws_directory_service_log_subscription`
- `aws_directory_service_trust`

### dlm_lifecycle

- `aws_dlm_lifecycle_policy`

### dms_certificate

- `aws_dms_certificate`

### dms_endpoint

- `aws_dms_endpoint`

### dms_event

- `aws_dms_event_subscription`

### dms_replication

- `aws_dms_replication_config`
- `aws_dms_replication_instance`
- `aws_dms_replication_subnet_group`
- `aws_dms_replication_task`

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

### dsql_cluster

- `aws_dsql_cluster`

### dx_connection

- `aws_dx_connection`

### dx_gateway

- `aws_dx_gateway`
- `aws_dx_gateway_association_proposal`

### dx_lag

- `aws_dx_lag`

### dynamodb_global

- `aws_dynamodb_global_table`

### dynamodb_table

- `aws_dynamodb_table_export`

### ebs_default

- `aws_ebs_default_kms_key`

### ebs_fast

- `aws_ebs_fast_snapshot_restore`

### ebs_snapshot

- `aws_ebs_snapshot`
- `aws_ebs_snapshot_block_public_access`

### ebs_volume

- `aws_ebs_volume`

### ec2_allowed

- `aws_ec2_allowed_images_settings`

### ec2_availability

- `aws_ec2_availability_zone_group`

### ec2_capacity

- `aws_ec2_capacity_block_reservation`
- `aws_ec2_capacity_reservation`
- `aws_ec2_capacity_reservation_fleet`

### ec2_carrier

- `aws_ec2_carrier_gateway`

### ec2_client

- `aws_ec2_client_vpn_endpoint`
- `aws_ec2_client_vpn_network_association`

### ec2_default

- `aws_ec2_default_credit_specification`

### ec2_fleet

- `aws_ec2_fleet`

### ec2_host

- `aws_ec2_host`

### ec2_instance

- `aws_ec2_instance_connect_endpoint`
- `aws_ec2_instance_metadata_defaults`
- `aws_ec2_instance_state`

### ec2_local

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
- `aws_ec2_transit_gateway_route_table`
- `aws_ec2_transit_gateway_vpc_attachment`
- `aws_ec2_transit_gateway_vpc_attachment_accepter`
- `aws_ec2_transit_gateway_vpn_attachment`

### ecr_pull

- `aws_ecr_pull_through_cache_rule`

### ecr_registry

- `aws_ecr_registry_scanning_configuration`

### ecr_repository

- `aws_ecr_repository`
- `aws_ecr_repository_creation_template`

### ecrpublic_repository

- `aws_ecrpublic_repository`

### ecs_account

- `aws_ecs_account_setting_default`

### ecs_capacity

- `aws_ecs_capacity_provider`

### ecs_cluster

- `aws_ecs_cluster`
- `aws_ecs_cluster_capacity_providers`

### ecs_express

- `aws_ecs_express_gateway_service`

### ecs_service

- `aws_ecs_service`

### efs_access

- `aws_efs_access_point`

### efs_file

- `aws_efs_file_system`

### egress_only

- `aws_egress_only_internet_gateway`

### eip

- `aws_eip`

### eip_association

- `aws_eip_association`

### eip_domain

- `aws_eip_domain_name`

### eks_cluster

- `aws_eks_cluster`

### elastic_beanstalk

- `aws_elastic_beanstalk_application`
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

### elb

- `aws_elb`

### emr_cluster

- `aws_emr_cluster`

### emr_security

- `aws_emr_security_configuration`

### emr_studio

- `aws_emr_studio`
- `aws_emr_studio_session_mapping`

### fis_experiment

- `aws_fis_experiment_template`

### flow_log

- `aws_flow_log`

### fsx_backup

- `aws_fsx_backup`

### fsx_file

- `aws_fsx_file_cache`

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

### gamelift_game

- `aws_gamelift_game_server_group`
- `aws_gamelift_game_session_queue`

### gamelift_script

- `aws_gamelift_script`

### glacier_vault

- `aws_glacier_vault`

### glue_catalog

- `aws_glue_catalog_database`

### glue_classifier

- `aws_glue_classifier`

### glue_connection

- `aws_glue_connection`

### glue_crawler

- `aws_glue_crawler`

### glue_data

- `aws_glue_data_quality_ruleset`

### glue_job

- `aws_glue_job`

### glue_ml

- `aws_glue_ml_transform`

### glue_registry

- `aws_glue_registry`

### glue_schema

- `aws_glue_schema`

### glue_security

- `aws_glue_security_configuration`

### glue_workflow

- `aws_glue_workflow`

### grafana_workspace

- `aws_grafana_workspace`

### guardduty_detector

- `aws_guardduty_detector`

### guardduty_malware

- `aws_guardduty_malware_protection_plan`

### guardduty_organization

- `aws_guardduty_organization_admin_account`

### iam_access

- `aws_iam_access_key`

### iam_account

- `aws_iam_account_alias`

### iam_group

- `aws_iam_group`

### iam_openid

- `aws_iam_openid_connect_provider`

### iam_outbound

- `aws_iam_outbound_web_identity_federation`

### iam_policy

- `aws_iam_policy`

### iam_role

- `aws_iam_role`

### iam_saml

- `aws_iam_saml_provider`

### iam_server

- `aws_iam_server_certificate`

### iam_service

- `aws_iam_service_linked_role`
- `aws_iam_service_specific_credential`

### iam_signing

- `aws_iam_signing_certificate`

### iam_user

- `aws_iam_user`
- `aws_iam_user_ssh_key`

### iam_virtual

- `aws_iam_virtual_mfa_device`

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

### inspector2_filter

- `aws_inspector2_filter`

### instance

- `aws_instance`

### internet_gateway

- `aws_internet_gateway`

### internetmonitor_monitor

- `aws_internetmonitor_monitor`

### iot_policy

- `aws_iot_policy`

### iot_thing

- `aws_iot_thing`

### iot_topic

- `aws_iot_topic_rule`

### kendra_index

- `aws_kendra_index`

### key_pair

- `aws_key_pair`

### kinesis_analytics

- `aws_kinesis_analytics_application`

### kinesis_firehose

- `aws_kinesis_firehose_delivery_stream`

### kinesis_stream

- `aws_kinesis_stream`

### kinesisanalyticsv2_application

- `aws_kinesisanalyticsv2_application`

### kms_alias

- `aws_kms_alias`

### kms_custom

- `aws_kms_custom_key_store`

### kms_external

- `aws_kms_external_key`

### kms_key

- `aws_kms_key`

### kms_replica

- `aws_kms_replica_external_key`
- `aws_kms_replica_key`

### lakeformation_data

- `aws_lakeformation_data_cells_filter`

### lakeformation_lf

- `aws_lakeformation_lf_tag`
- `aws_lakeformation_lf_tag_expression`

### lakeformation_resource

- `aws_lakeformation_resource`
- `aws_lakeformation_resource_lf_tag`

### lambda_capacity

- `aws_lambda_capacity_provider`

### lambda_code

- `aws_lambda_code_signing_config`

### lambda_event

- `aws_lambda_event_source_mapping`

### lambda_function

- `aws_lambda_function`

### lambda_invocation

- `aws_lambda_invocation`

### launch_configuration

- `aws_launch_configuration`

### lb

- `aws_lb`

### lb_cookie

- `aws_lb_cookie_stickiness_policy`

### lb_target

- `aws_lb_target_group`

### lex_bot

- `aws_lex_bot`

### lex_intent

- `aws_lex_intent`

### lex_slot

- `aws_lex_slot_type`

### lexv2models_bot

- `aws_lexv2models_bot`

### licensemanager_grant

- `aws_licensemanager_grant`

### licensemanager_license

- `aws_licensemanager_license_configuration`

### lightsail_bucket

- `aws_lightsail_bucket`

### lightsail_certificate

- `aws_lightsail_certificate`

### lightsail_container

- `aws_lightsail_container_service`

### lightsail_database

- `aws_lightsail_database`

### lightsail_disk

- `aws_lightsail_disk`

### lightsail_instance

- `aws_lightsail_instance`

### lightsail_lb

- `aws_lightsail_lb`

### m2_application

- `aws_m2_application`

### m2_environment

- `aws_m2_environment`

### media_convert

- `aws_media_convert_queue`

### media_package

- `aws_media_package_channel`

### media_store

- `aws_media_store_container`

### medialive_channel

- `aws_medialive_channel`

### medialive_input

- `aws_medialive_input`
- `aws_medialive_input_security_group`

### medialive_multiplex

- `aws_medialive_multiplex`

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

### mq_configuration

- `aws_mq_configuration`

### msk_cluster

- `aws_msk_cluster`

### msk_configuration

- `aws_msk_configuration`

### msk_replicator

- `aws_msk_replicator`

### msk_serverless

- `aws_msk_serverless_cluster`

### msk_vpc

- `aws_msk_vpc_connection`

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

### networkmanager_dx

- `aws_networkmanager_dx_gateway_attachment`

### networkmanager_global

- `aws_networkmanager_global_network`

### networkmonitor_monitor

- `aws_networkmonitor_monitor`

### notifications_channel

- `aws_notifications_channel_association`

### notifications_notification

- `aws_notifications_notification_configuration`
- `aws_notifications_notification_hub`

### notificationscontacts_email

- `aws_notificationscontacts_email_contact`

### odb_cloud

- `aws_odb_cloud_autonomous_vm_cluster`
- `aws_odb_cloud_exadata_infrastructure`
- `aws_odb_cloud_vm_cluster`

### odb_network

- `aws_odb_network`
- `aws_odb_network_peering_connection`

### opensearch_domain

- `aws_opensearch_domain`
- `aws_opensearch_domain_policy`
- `aws_opensearch_domain_saml_options`

### opensearch_vpc

- `aws_opensearch_vpc_endpoint`

### opensearchserverless_collection

- `aws_opensearchserverless_collection`

### opensearchserverless_vpc

- `aws_opensearchserverless_vpc_endpoint`

### organizations_account

- `aws_organizations_account`

### organizations_delegated

- `aws_organizations_delegated_administrator`

### organizations_organization

- `aws_organizations_organization`

### osis_pipeline

- `aws_osis_pipeline`

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

### placement_group

- `aws_placement_group`

### prometheus_scraper

- `aws_prometheus_scraper`

### prometheus_workspace

- `aws_prometheus_workspace`

### qbusiness_application

- `aws_qbusiness_application`

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

### rds_shard

- `aws_rds_shard_group`

### redshift_authentication

- `aws_redshift_authentication_profile`

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

### resiliencehub_resiliency

- `aws_resiliencehub_resiliency_policy`

### resourceexplorer2_view

- `aws_resourceexplorer2_view`

### resourcegroups_group

- `aws_resourcegroups_group`

### route

- `aws_route`

### route53_cidr

- `aws_route53_cidr_collection`

### route53_delegation

- `aws_route53_delegation_set`

### route53_health

- `aws_route53_health_check`

### route53_query

- `aws_route53_query_log`

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

### route53_traffic

- `aws_route53_traffic_policy`
- `aws_route53_traffic_policy_instance`

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

### route53recoverycontrolconfig_cluster

- `aws_route53recoverycontrolconfig_cluster`

### route53recoverycontrolconfig_control

- `aws_route53recoverycontrolconfig_control_panel`

### route_table

- `aws_route_table`

### s3_bucket

- `aws_s3_bucket`

### s3_directory

- `aws_s3_directory_bucket`

### s3outposts_endpoint

- `aws_s3outposts_endpoint`

### s3tables_table

- `aws_s3tables_table_bucket`
- `aws_s3tables_table_replication`

### s3vectors_vector

- `aws_s3vectors_vector_bucket`

### sagemaker_app

- `aws_sagemaker_app`
- `aws_sagemaker_app_image_config`

### sagemaker_code

- `aws_sagemaker_code_repository`

### sagemaker_domain

- `aws_sagemaker_domain`

### sagemaker_endpoint

- `aws_sagemaker_endpoint`

### sagemaker_flow

- `aws_sagemaker_flow_definition`

### sagemaker_hub

- `aws_sagemaker_hub`

### sagemaker_human

- `aws_sagemaker_human_task_ui`

### sagemaker_image

- `aws_sagemaker_image`

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

### sagemaker_project

- `aws_sagemaker_project`

### sagemaker_studio

- `aws_sagemaker_studio_lifecycle_config`

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

### secretsmanager_secret

- `aws_secretsmanager_secret`

### security_group

- `aws_security_group`
- `aws_security_group_rule`

### securityhub_action

- `aws_securityhub_action_target`

### securityhub_automation

- `aws_securityhub_automation_rule`

### service_discovery

- `aws_service_discovery_http_namespace`
- `aws_service_discovery_private_dns_namespace`
- `aws_service_discovery_public_dns_namespace`
- `aws_service_discovery_service`

### servicecatalog_portfolio

- `aws_servicecatalog_portfolio`

### servicecatalog_product

- `aws_servicecatalog_product`

### servicecatalog_service

- `aws_servicecatalog_service_action`

### servicecatalogappregistry_application

- `aws_servicecatalogappregistry_application`

### servicecatalogappregistry_attribute

- `aws_servicecatalogappregistry_attribute_group`

### sesv2_configuration

- `aws_sesv2_configuration_set`

### sesv2_contact

- `aws_sesv2_contact_list`

### sesv2_dedicated

- `aws_sesv2_dedicated_ip_assignment`
- `aws_sesv2_dedicated_ip_pool`

### sesv2_email

- `aws_sesv2_email_identity`

### sesv2_tenant

- `aws_sesv2_tenant`

### sfn_activity

- `aws_sfn_activity`

### sfn_state

- `aws_sfn_state_machine`

### signer_signing

- `aws_signer_signing_job`
- `aws_signer_signing_profile`

### sns_platform

- `aws_sns_platform_application`

### sns_topic

- `aws_sns_topic`

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

### ssm_parameter

- `aws_ssm_parameter`

### ssm_patch

- `aws_ssm_patch_baseline`

### ssm_resource

- `aws_ssm_resource_data_sync`

### ssmcontacts_contact

- `aws_ssmcontacts_contact`

### ssmincidents_replication

- `aws_ssmincidents_replication_set`

### ssmincidents_response

- `aws_ssmincidents_response_plan`

### subnet

- `aws_subnet`

### timestreaminfluxdb_db

- `aws_timestreaminfluxdb_db_cluster`
- `aws_timestreaminfluxdb_db_instance`

### transcribe_language

- `aws_transcribe_language_model`

### transcribe_medical

- `aws_transcribe_medical_vocabulary`

### transcribe_vocabulary

- `aws_transcribe_vocabulary`
- `aws_transcribe_vocabulary_filter`

### transfer_certificate

- `aws_transfer_certificate`

### transfer_connector

- `aws_transfer_connector`

### transfer_profile

- `aws_transfer_profile`

### transfer_server

- `aws_transfer_server`

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

### verifiedpermissions_policy

- `aws_verifiedpermissions_policy_store`

### volume_attachment

- `aws_volume_attachment`

### vpc

- `aws_vpc`

### vpc_block

- `aws_vpc_block_public_access_options`

### vpc_dhcp

- `aws_vpc_dhcp_options`

### vpc_encryption

- `aws_vpc_encryption_control`

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
- `aws_vpc_ipam_resource_discovery`
- `aws_vpc_ipam_resource_discovery_association`
- `aws_vpc_ipam_scope`

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

### vpclattice_service

- `aws_vpclattice_service`
- `aws_vpclattice_service_network`

### vpclattice_target

- `aws_vpclattice_target_group`

### vpn_concentrator

- `aws_vpn_concentrator`

### vpn_connection

- `aws_vpn_connection`

### vpn_gateway

- `aws_vpn_gateway`

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

### wafregional_byte

- `aws_wafregional_byte_match_set`

### wafregional_geo

- `aws_wafregional_geo_match_set`

### wafregional_ipset

- `aws_wafregional_ipset`

### wafregional_regex

- `aws_wafregional_regex_match_set`
- `aws_wafregional_regex_pattern_set`

### wafregional_rule

- `aws_wafregional_rule`
- `aws_wafregional_rule_group`

### wafregional_size

- `aws_wafregional_size_constraint_set`

### wafregional_sql

- `aws_wafregional_sql_injection_match_set`

### wafregional_web

- `aws_wafregional_web_acl`

### wafregional_xss

- `aws_wafregional_xss_match_set`

### workspaces_connection

- `aws_workspaces_connection_alias`

### workspaces_directory

- `aws_workspaces_directory`

### workspaces_ip

- `aws_workspaces_ip_group`

### workspaces_workspace

- `aws_workspaces_workspace`

### workspacesweb_browser

- `aws_workspacesweb_browser_settings`
- `aws_workspacesweb_browser_settings_association`

### workspacesweb_data

- `aws_workspacesweb_data_protection_settings`
- `aws_workspacesweb_data_protection_settings_association`

### workspacesweb_ip

- `aws_workspacesweb_ip_access_settings`
- `aws_workspacesweb_ip_access_settings_association`

### workspacesweb_network

- `aws_workspacesweb_network_settings`
- `aws_workspacesweb_network_settings_association`

### workspacesweb_portal

- `aws_workspacesweb_portal`

### workspacesweb_session

- `aws_workspacesweb_session_logger`
- `aws_workspacesweb_session_logger_association`

### workspacesweb_trust

- `aws_workspacesweb_trust_store`
- `aws_workspacesweb_trust_store_association`

### workspacesweb_user

- `aws_workspacesweb_user_access_logging_settings`
- `aws_workspacesweb_user_access_logging_settings_association`
- `aws_workspacesweb_user_settings`
- `aws_workspacesweb_user_settings_association`

### xray_group

- `aws_xray_group`

## Verification Details

This deep verification performed:

1. **Actual API Calls:** Made real AWS API calls to validate methods work
2. **Response Structure Validation:** Checked that topkey exists in responses
3. **Key Field Validation:** Verified that key fields exist in response items
4. **Error Handling:** Categorized different types of failures

### Limitations

- Some methods require specific parameters (parent resource IDs) that couldn't be tested
- Permission errors may indicate missing IAM permissions rather than incorrect configuration
- Empty responses (no resources in account) prevent key field validation
- Rate limiting may cause some tests to fail

### Recommendations

1. **Fix Errors First:** Address resources with method not found errors
2. **Review Warnings:** Update topkey and key fields based on actual API responses
3. **Grant Permissions:** Add IAM permissions for resources with permission errors
4. **Retest:** Run verification again after fixes to confirm improvements

## Automated Fixes

This section provides machine-readable fix data for automated correction:

### Structure Fixes Needed

```python
# Copy these fixes into a fix script or apply manually
STRUCTURE_FIXES = {
    'aws_appstream_fleet_stack_association': {
        'current_topkey': 'FleetStackAssociations',
        'correct_topkey': 'Fleets',
        'clfn': 'appstream',
        'descfn': 'describe_fleets',
        'key': 'FleetName'
    },
    'aws_appsync_graphql_api': {
        'current_topkey': 'GraphqlApis',
        'correct_topkey': 'graphqlApis',
        'clfn': 'appsync',
        'descfn': 'list_graphql_apis',
        'key': 'ApiId'
    },
    'aws_auditmanager_account_registration': {
        'current_topkey': 'AccountRegistrations',
        'correct_topkey': '',  # No wrapper key
        'clfn': 'auditmanager',
        'descfn': 'get_account_status',
        'key': 'Id'
    },
    'aws_autoscaling_attachment': {
        'current_topkey': 'Attachments',
        'correct_topkey': 'AutoScalingGroups',
        'clfn': 'autoscaling',
        'descfn': 'describe_auto_scaling_groups',
        'key': 'AttachmentName'
    },
    'aws_autoscaling_notification': {
        'current_topkey': 'Notifications',
        'correct_topkey': 'NotificationConfigurations',
        'clfn': 'autoscaling',
        'descfn': 'describe_notification_configurations',
        'key': 'TopicARN'
    },
    'aws_bedrock_model_invocation_logging_configuration': {
        'current_topkey': 'loggingConfig',
        'correct_topkey': '',  # No wrapper key
        'clfn': 'bedrock',
        'descfn': 'get_model_invocation_logging_configuration',
        'key': 'null'
    },
    'aws_bedrockagentcore_memory_strategy': {
        'current_topkey': 'memoryStrategies',
        'correct_topkey': 'memories',
        'clfn': 'bedrock-agentcore-control',
        'descfn': 'list_memories',
        'key': 'strategyId'
    },
    'aws_bedrockagentcore_token_vault_cmk': {
        'current_topkey': 'tokenVault',
        'correct_topkey': 'kmsConfiguration',
        'clfn': 'bedrock-agentcore-control',
        'descfn': 'get_token_vault',
        'key': 'vaultId'
    },
    'aws_ce_cost_category': {
        'current_topkey': 'CostCategories',
        'correct_topkey': 'CostCategoryReferences',
        'clfn': 'ce',
        'descfn': 'list_cost_category_definitions',
        'key': 'CostCategoryArn'
    },
    'aws_chimesdkmediapipelines_media_insights_pipeline_configuration': {
        'current_topkey': 'MediaInsightsPipelines',
        'correct_topkey': 'MediaInsightsPipelineConfigurations',
        'clfn': 'chime-sdk-media-pipelines',
        'descfn': 'list_media_insights_pipeline_configurations',
        'key': 'Name'
    },
    'aws_chimesdkvoice_global_settings': {
        'current_topkey': 'GlobalSettings',
        'correct_topkey': 'VoiceConnector',
        'clfn': 'chime-sdk-voice',
        'descfn': 'get_global_settings',
        'key': 'GlobalSettingsName'
    },
    'aws_cloudfront_distribution': {
        'current_topkey': 'DistributionList.Items',
        'correct_topkey': 'DistributionList',
        'clfn': 'cloudfront',
        'descfn': 'list_distributions',
        'key': 'Id'
    },
    'aws_cloudfront_origin_request_policy': {
        'current_topkey': 'OriginRequestPolicyList',
        'correct_topkey': 'CloudFrontOriginAccessIdentityList',
        'clfn': 'cloudfront',
        'descfn': 'list_cloud_front_origin_access_identities',
        'key': 'Id'
    },
    'aws_cloudwatch_event_bus_policy': {
        'current_topkey': 'Policy',
        'correct_topkey': '',  # No wrapper key
        'clfn': 'events',
        'descfn': 'describe_event_bus',
        'key': 'Name'
    },
    'aws_cloudwatch_event_permission': {
        'current_topkey': 'Policy',
        'correct_topkey': '',  # No wrapper key
        'clfn': 'events',
        'descfn': 'describe_event_bus',
        'key': 'Sid'
    },
    'aws_codegurureviewer_repository_association': {
        'current_topkey': 'RepositoryAssociations',
        'correct_topkey': 'RepositoryAssociationSummaries',
        'clfn': 'codeguru-reviewer',
        'descfn': 'list_repository_associations',
        'key': 'Name'
    },
    'aws_comprehend_document_classifier': {
        'current_topkey': 'DocumentClassifiers',
        'correct_topkey': 'DocumentClassifierPropertiesList',
        'clfn': 'comprehend',
        'descfn': 'list_document_classifiers',
        'key': 'DocumentClassifierArn'
    },
    'aws_comprehend_entity_recognizer': {
        'current_topkey': 'EntityRecognizers',
        'correct_topkey': 'EntityRecognizerPropertiesList',
        'clfn': 'comprehend',
        'descfn': 'list_entity_recognizers',
        'key': 'EntityRecognizerArn'
    },
    'aws_costoptimizationhub_enrollment_status': {
        'current_topkey': 'status',
        'correct_topkey': 'preferredCommitment',
        'clfn': 'cost-optimization-hub',
        'descfn': 'get_preferences',
        'key': 'status'
    },
    'aws_costoptimizationhub_preferences': {
        'current_topkey': 'preferences',
        'correct_topkey': 'preferredCommitment',
        'clfn': 'cost-optimization-hub',
        'descfn': 'get_preferences',
        'key': 'memberAccountDiscountVisibility'
    },
    'aws_datapipeline_pipeline': {
        'current_topkey': 'Pipelines',
        'correct_topkey': 'pipelineIdList',
        'clfn': 'datapipeline',
        'descfn': 'list_pipelines',
        'key': 'Name'
    },
    'aws_db_instance_role_association': {
        'current_topkey': 'DBInstanceRoleAssociations',
        'correct_topkey': 'DBInstances',
        'clfn': 'rds',
        'descfn': 'describe_db_instances',
        'key': 'DBInstanceArn'
    },
    'aws_default_vpc_dhcp_options': {
        'current_topkey': 'VpcDhcpOptions',
        'correct_topkey': 'DhcpOptions',
        'clfn': 'ec2',
        'descfn': 'describe_dhcp_options',
        'key': 'VpcDhcpOptionsId'
    },
    'aws_detective_invitation_accepter': {
        'current_topkey': 'InvitationAccepters',
        'correct_topkey': 'Invitations',
        'clfn': 'detective',
        'descfn': 'list_invitations',
        'key': 'GraphArn'
    },
    'aws_detective_organization_admin_account': {
        'current_topkey': 'OrganizationAdminAccounts',
        'correct_topkey': 'Administrators',
        'clfn': 'detective',
        'descfn': 'list_organization_admin_accounts',
        'key': 'GraphArn'
    },
    'aws_directory_service_radius_settings': {
        'current_topkey': 'RadiusSettings',
        'correct_topkey': 'DirectoryDescriptions',
        'clfn': 'ds',
        'descfn': 'describe_directories',
        'key': 'DirectoryId'
    },
    'aws_dms_s3_endpoint': {
        'current_topkey': 'S3Endpoints',
        'correct_topkey': 'Endpoints',
        'clfn': 'dms',
        'descfn': 'describe_endpoints',
        'key': 'EndpointIdentifier'
    },
    'aws_docdbelastic_cluster': {
        'current_topkey': 'Clusters',
        'correct_topkey': 'clusters',
        'clfn': 'docdb-elastic',
        'descfn': 'list_clusters',
        'key': 'ClusterName'
    },
    'aws_dsql_cluster_peering': {
        'current_topkey': 'clusterPeerings',
        'correct_topkey': 'clusters',
        'clfn': 'dsql',
        'descfn': 'list_clusters',
        'key': 'id'
    },
    'aws_dx_bgp_peer': {
        'current_topkey': 'BgpPeers',
        'correct_topkey': 'virtualInterfaces',
        'clfn': 'directconnect',
        'descfn': 'describe_virtual_interfaces',
        'key': 'BgpPeerId'
    },
    'aws_dx_connection_association': {
        'current_topkey': 'ConnectionAssociations',
        'correct_topkey': 'connections',
        'clfn': 'directconnect',
        'descfn': 'describe_connections',
        'key': 'ConnectionId'
    },
    'aws_dx_connection_confirmation': {
        'current_topkey': 'Confirmations',
        'correct_topkey': 'connections',
        'clfn': 'directconnect',
        'descfn': 'describe_connections',
        'key': 'ConfirmationToken'
    },
    'aws_dx_hosted_connection': {
        'current_topkey': 'GatewayAssociationProposals',
        'correct_topkey': 'connections',
        'clfn': 'directconnect',
        'descfn': 'describe_connections',
        'key': 'ProposalId'
    },
    'aws_dx_hosted_private_virtual_interface': {
        'current_topkey': 'VirtualInterfaces',
        'correct_topkey': 'virtualInterfaces',
        'clfn': 'directconnect',
        'descfn': 'describe_virtual_interfaces',
        'key': 'VirtualInterfaceId'
    },
    'aws_dx_hosted_private_virtual_interface_accepter': {
        'current_topkey': 'VirtualInterfaces',
        'correct_topkey': 'virtualInterfaces',
        'clfn': 'directconnect',
        'descfn': 'describe_virtual_interfaces',
        'key': 'VirtualInterfaceId'
    },
    'aws_dx_hosted_public_virtual_interface': {
        'current_topkey': 'VirtualInterfaces',
        'correct_topkey': 'virtualInterfaces',
        'clfn': 'directconnect',
        'descfn': 'describe_virtual_interfaces',
        'key': 'VirtualInterfaceId'
    },
    'aws_dx_hosted_public_virtual_interface_accepter': {
        'current_topkey': 'VirtualInterfaces',
        'correct_topkey': 'virtualInterfaces',
        'clfn': 'directconnect',
        'descfn': 'describe_virtual_interfaces',
        'key': 'VirtualInterfaceId'
    },
    'aws_dx_hosted_transit_virtual_interface': {
        'current_topkey': 'VirtualInterfaces',
        'correct_topkey': 'virtualInterfaces',
        'clfn': 'directconnect',
        'descfn': 'describe_virtual_interfaces',
        'key': 'VirtualInterfaceId'
    },
    'aws_dx_hosted_transit_virtual_interface_accepter': {
        'current_topkey': 'VirtualInterfaces',
        'correct_topkey': 'virtualInterfaces',
        'clfn': 'directconnect',
        'descfn': 'describe_virtual_interfaces',
        'key': 'VirtualInterfaceId'
    },
    'aws_dx_macsec_key_association': {
        'current_topkey': 'MacsecKeyAssociations',
        'correct_topkey': 'connections',
        'clfn': 'directconnect',
        'descfn': 'describe_connections',
        'key': 'AssociationId'
    },
    'aws_dx_private_virtual_interface': {
        'current_topkey': 'VirtualInterfaces',
        'correct_topkey': 'virtualInterfaces',
        'clfn': 'directconnect',
        'descfn': 'describe_virtual_interfaces',
        'key': 'VirtualInterfaceId'
    },
    'aws_dx_public_virtual_interface': {
        'current_topkey': 'VirtualInterfaces',
        'correct_topkey': 'virtualInterfaces',
        'clfn': 'directconnect',
        'descfn': 'describe_virtual_interfaces',
        'key': 'VirtualInterfaceId'
    },
    'aws_dx_transit_virtual_interface': {
        'current_topkey': 'VirtualInterfaces',
        'correct_topkey': 'virtualInterfaces',
        'clfn': 'directconnect',
        'descfn': 'describe_virtual_interfaces',
        'key': 'VirtualInterfaceId'
    },
    'aws_ebs_snapshot_copy': {
        'current_topkey': 'SnapshotCopyGrants',
        'correct_topkey': 'Snapshots',
        'clfn': 'ec2',
        'descfn': 'describe_snapshots',
        'key': 'SnapshotCopyGrantName'
    },
    'aws_ebs_snapshot_import': {
        'current_topkey': 'SnapshotTasks',
        'correct_topkey': 'ImportSnapshotTasks',
        'clfn': 'ec2',
        'descfn': 'describe_import_snapshot_tasks',
        'key': 'SnapshotTaskIdentifier'
    },
    'aws_ec2_local_gateway_route': {
        'current_topkey': 'LocalGatewayRoutes',
        'correct_topkey': 'LocalGatewayRouteTables',
        'clfn': 'ec2',
        'descfn': 'describe_local_gateway_route_tables',
        'key': 'LocalGatewayRouteTableId'
    },
    'aws_elasticache_user_group_association': {
        'current_topkey': 'UserGroupMemberships',
        'correct_topkey': 'UserGroups',
        'clfn': 'elasticache',
        'descfn': 'describe_user_groups',
        'key': 'UserGroupId'
    },
    'aws_emr_block_public_access_configuration': {
        'current_topkey': 'BlockPublicAccessConfigurations',
        'correct_topkey': 'BlockPublicAccessConfiguration',
        'clfn': 'emr',
        'descfn': 'get_block_public_access_configuration',
        'key': 'Id'
    },
    'aws_emrcontainers_job_template': {
        'current_topkey': 'JobTemplates',
        'correct_topkey': 'templates',
        'clfn': 'emr-containers',
        'descfn': 'list_job_templates',
        'key': 'Id'
    },
    'aws_emrcontainers_virtual_cluster': {
        'current_topkey': 'VirtualClusters',
        'correct_topkey': 'virtualClusters',
        'clfn': 'emr-containers',
        'descfn': 'list_virtual_clusters',
        'key': 'Id'
    },
    'aws_emrserverless_application': {
        'current_topkey': 'Applications',
        'correct_topkey': 'applications',
        'clfn': 'emr-serverless',
        'descfn': 'list_applications',
        'key': 'Id'
    },
    'aws_finspace_kx_environment': {
        'current_topkey': 'Environments',
        'correct_topkey': 'environments',
        'clfn': 'finspace',
        'descfn': 'list_environments',
        'key': 'EnvironmentId'
    },
    'aws_fsx_data_repository_association': {
        'current_topkey': 'DataRepositoryAssociations',
        'correct_topkey': 'Associations',
        'clfn': 'fsx',
        'descfn': 'describe_data_repository_associations',
        'key': 'AssociationId'
    },
    'aws_gamelift_fleet': {
        'current_topkey': 'Fleets',
        'correct_topkey': 'FleetIds',
        'clfn': 'gamelift',
        'descfn': 'list_fleets',
        'key': 'FleetId'
    },
    'aws_glue_dev_endpoint': {
        'current_topkey': 'DevEndpoints',
        'correct_topkey': 'DevEndpointNames',
        'clfn': 'glue',
        'descfn': 'list_dev_endpoints',
        'key': 'EndpointName'
    },
    'aws_grafana_workspace_api_key': {
        'current_topkey': 'ApiKeys',
        'correct_topkey': 'workspaces',
        'clfn': 'grafana',
        'descfn': 'list_workspaces',
        'key': 'KeyId'
    },
    'aws_guardduty_invite_accepter': {
        'current_topkey': 'InvitationAccepters',
        'correct_topkey': 'Invitations',
        'clfn': 'guardduty',
        'descfn': 'list_invitations',
        'key': 'InvitationAccepterId'
    },
    'aws_iam_security_token_service_preferences': {
        'current_topkey': 'AccountTokenVersion',
        'correct_topkey': 'SummaryMap',
        'clfn': 'iam',
        'descfn': 'get_account_summary',
        'key': 'AccountTokenVersion'
    },
    'aws_inspector2_delegated_admin_account': {
        'current_topkey': 'DelegatedAdminAccounts',
        'correct_topkey': 'delegatedAdminAccounts',
        'clfn': 'inspector2',
        'descfn': 'list_delegated_admin_accounts',
        'key': 'AccountId'
    },
    'aws_inspector2_enabler': {
        'current_topkey': 'Enablers',
        'correct_topkey': 'accounts',
        'clfn': 'inspector2',
        'descfn': 'batch_get_account_status',
        'key': 'Name'
    },
    'aws_inspector2_member_association': {
        'current_topkey': 'MemberAssociations',
        'correct_topkey': 'members',
        'clfn': 'inspector2',
        'descfn': 'list_members',
        'key': 'AccountId'
    },
    'aws_inspector_assessment_target': {
        'current_topkey': 'AssessmentTargets',
        'correct_topkey': 'assessmentTargetArns',
        'clfn': 'inspector',
        'descfn': 'list_assessment_targets',
        'key': 'Name'
    },
    'aws_inspector_assessment_template': {
        'current_topkey': 'AssessmentTemplates',
        'correct_topkey': 'assessmentTemplateArns',
        'clfn': 'inspector',
        'descfn': 'list_assessment_templates',
        'key': 'Name'
    },
    'aws_inspector_resource_group': {
        'current_topkey': 'ResourceGroups',
        'correct_topkey': 'assessmentTargetArns',
        'clfn': 'inspector',
        'descfn': 'list_assessment_targets',
        'key': 'Name'
    },
    'aws_internet_gateway_attachment': {
        'current_topkey': 'InternetGatewayAttachments',
        'correct_topkey': 'InternetGateways',
        'clfn': 'ec2',
        'descfn': 'describe_internet_gateways',
        'key': 'InternetGatewayId'
    },
    'aws_invoicing_invoice_unit': {
        'current_topkey': 'invoiceUnits',
        'correct_topkey': 'InvoiceUnits',
        'clfn': 'invoicing',
        'descfn': 'list_invoice_units',
        'key': 'invoiceUnitArn'
    },
    'aws_iot_authorizer': {
        'current_topkey': 'Authorizers',
        'correct_topkey': 'authorizers',
        'clfn': 'iot',
        'descfn': 'list_authorizers',
        'key': 'AuthorizerName'
    },
    'aws_iot_billing_group': {
        'current_topkey': 'BillingGroups',
        'correct_topkey': 'billingGroups',
        'clfn': 'iot',
        'descfn': 'list_billing_groups',
        'key': 'BillingGroupName'
    },
    'aws_iot_ca_certificate': {
        'current_topkey': 'CACertificates',
        'correct_topkey': 'certificates',
        'clfn': 'iot',
        'descfn': 'list_ca_certificates',
        'key': 'Id'
    },
    'aws_iot_certificate': {
        'current_topkey': 'Certificates',
        'correct_topkey': 'certificates',
        'clfn': 'iot',
        'descfn': 'list_certificates',
        'key': 'CertificateId'
    },
    'aws_iot_domain_configuration': {
        'current_topkey': 'DomainConfigurations',
        'correct_topkey': 'domainConfigurations',
        'clfn': 'iot',
        'descfn': 'list_domain_configurations',
        'key': 'DomainConfigurationName'
    },
    'aws_iot_event_configurations': {
        'current_topkey': 'EventConfigurations',
        'correct_topkey': 'eventConfigurations',
        'clfn': 'iot',
        'descfn': 'describe_event_configurations',
        'key': 'EventConfigurationName'
    },
    'aws_iot_indexing_configuration': {
        'current_topkey': 'IndexingConfigurations',
        'correct_topkey': 'thingIndexingConfiguration',
        'clfn': 'iot',
        'descfn': 'get_indexing_configuration',
        'key': 'IndexingConfigurationName'
    },
    'aws_iot_policy_attachment': {
        'current_topkey': 'Policies',
        'correct_topkey': 'policies',
        'clfn': 'iot',
        'descfn': 'list_policies',
        'key': 'PolicyName'
    },
    'aws_iot_provisioning_template': {
        'current_topkey': 'ProvisioningTemplates',
        'correct_topkey': 'templates',
        'clfn': 'iot',
        'descfn': 'list_provisioning_templates',
        'key': 'TemplateName'
    },
    'aws_iot_role_alias': {
        'current_topkey': 'RoleAliases',
        'correct_topkey': 'roleAliases',
        'clfn': 'iot',
        'descfn': 'list_role_aliases',
        'key': 'RoleAliasName'
    },
    'aws_iot_thing_group': {
        'current_topkey': 'ThingGroups',
        'correct_topkey': 'thingGroups',
        'clfn': 'iot',
        'descfn': 'list_thing_groups',
        'key': 'ThingGroupName'
    },
    'aws_iot_thing_type': {
        'current_topkey': 'ThingTypes',
        'correct_topkey': 'thingTypes',
        'clfn': 'iot',
        'descfn': 'list_thing_types',
        'key': 'ThingTypeName'
    },
    'aws_iot_topic_rule_destination': {
        'current_topkey': 'destinations',
        'correct_topkey': 'destinationSummaries',
        'clfn': 'iot',
        'descfn': 'list_topic_rule_destinations',
        'key': 'destinationName'
    },
    'aws_ivs_channel': {
        'current_topkey': 'Channels',
        'correct_topkey': 'channels',
        'clfn': 'ivs',
        'descfn': 'list_channels',
        'key': 'arn'
    },
    'aws_ivs_playback_key_pair': {
        'current_topkey': 'PlaybackKeyPairs',
        'correct_topkey': 'keyPairs',
        'clfn': 'ivs',
        'descfn': 'list_playback_key_pairs',
        'key': 'arn'
    },
    'aws_ivs_recording_configuration': {
        'current_topkey': 'RecordingConfigurations',
        'correct_topkey': 'recordingConfigurations',
        'clfn': 'ivs',
        'descfn': 'list_recording_configurations',
        'key': 'arn'
    },
    'aws_ivschat_logging_configuration': {
        'current_topkey': 'LoggingConfigurations',
        'correct_topkey': 'loggingConfigurations',
        'clfn': 'ivschat',
        'descfn': 'list_logging_configurations',
        'key': 'arn'
    },
    'aws_ivschat_room': {
        'current_topkey': 'Rooms',
        'correct_topkey': 'rooms',
        'clfn': 'ivschat',
        'descfn': 'list_rooms',
        'key': 'arn'
    },
    'aws_keyspaces_keyspace': {
        'current_topkey': 'Keyspaces',
        'correct_topkey': 'keyspaces',
        'clfn': 'keyspaces',
        'descfn': 'list_keyspaces',
        'key': 'Name'
    },
    'aws_kinesis_video_stream': {
        'current_topkey': 'StreamNames',
        'correct_topkey': 'StreamInfoList',
        'clfn': 'kinesisvideo',
        'descfn': 'list_streams',
        'key': 'StreamName'
    },
    'aws_lakeformation_permissions': {
        'current_topkey': 'Permissions',
        'correct_topkey': 'PrincipalResourcePermissions',
        'clfn': 'lakeformation',
        'descfn': 'list_permissions',
        'key': 'Principal'
    },
    'aws_licensemanager_grant_accepter': {
        'current_topkey': 'GrantAccepters',
        'correct_topkey': 'Grants',
        'clfn': 'license-manager',
        'descfn': 'list_received_grants',
        'key': 'GrantId'
    },
    'aws_lightsail_bucket_resource_access': {
        'current_topkey': 'Buckets',
        'correct_topkey': 'buckets',
        'clfn': 'lightsail',
        'descfn': 'get_buckets',
        'key': 'name'
    },
    'aws_lightsail_disk_attachment': {
        'current_topkey': 'DiskAttachments',
        'correct_topkey': 'disks',
        'clfn': 'lightsail',
        'descfn': 'get_disks',
        'key': 'name'
    },
    'aws_lightsail_distribution': {
        'current_topkey': 'Distributions',
        'correct_topkey': 'distributions',
        'clfn': 'lightsail',
        'descfn': 'get_distributions',
        'key': 'name'
    },
    'aws_lightsail_domain': {
        'current_topkey': 'Domains',
        'correct_topkey': 'domains',
        'clfn': 'lightsail',
        'descfn': 'get_domains',
        'key': 'name'
    },
    'aws_lightsail_domain_entry': {
        'current_topkey': 'DomainEntries',
        'correct_topkey': 'domains',
        'clfn': 'lightsail',
        'descfn': 'get_domains',
        'key': 'name'
    },
    'aws_lightsail_key_pair': {
        'current_topkey': 'PortInfo',
        'correct_topkey': 'keyPairs',
        'clfn': 'lightsail',
        'descfn': 'get_key_pairs',
        'key': 'name'
    },
    'aws_lightsail_lb_attachment': {
        'current_topkey': 'LoadBalancers',
        'correct_topkey': 'loadBalancers',
        'clfn': 'lightsail',
        'descfn': 'get_load_balancers',
        'key': 'name'
    },
    'aws_lightsail_lb_certificate': {
        'current_topkey': 'KeyPairs',
        'correct_topkey': 'keyPairs',
        'clfn': 'lightsail',
        'descfn': 'get_key_pairs',
        'key': 'name'
    },
    'aws_lightsail_lb_https_redirection_policy': {
        'current_topkey': 'KeyPairs',
        'correct_topkey': 'keyPairs',
        'clfn': 'lightsail',
        'descfn': 'get_key_pairs',
        'key': 'name'
    },
    'aws_lightsail_lb_stickiness_policy': {
        'current_topkey': 'HttpsRedirectPolicies',
        'correct_topkey': 'loadBalancers',
        'clfn': 'lightsail',
        'descfn': 'get_load_balancers',
        'key': 'name'
    },
    'aws_lightsail_static_ip': {
        'current_topkey': 'KeyPairs',
        'correct_topkey': 'keyPairs',
        'clfn': 'lightsail',
        'descfn': 'get_key_pairs',
        'key': 'name'
    },
    'aws_lightsail_static_ip_attachment': {
        'current_topkey': 'StaticIps',
        'correct_topkey': 'staticIps',
        'clfn': 'lightsail',
        'descfn': 'get_static_ips',
        'key': 'name'
    },
    'aws_load_balancer_backend_server_policy': {
        'current_topkey': 'BackendServerDescriptions',
        'correct_topkey': 'LoadBalancers',
        'clfn': 'elbv2',
        'descfn': 'describe_load_balancers',
        'key': 'PolicyName'
    },
    'aws_location_geofence_collection': {
        'current_topkey': 'GeofenceCollections',
        'correct_topkey': 'Entries',
        'clfn': 'location',
        'descfn': 'list_geofence_collections',
        'key': 'CollectionName'
    },
    'aws_location_map': {
        'current_topkey': 'Maps',
        'correct_topkey': 'Entries',
        'clfn': 'location',
        'descfn': 'list_maps',
        'key': 'MapName'
    },
    'aws_location_place_index': {
        'current_topkey': 'PlaceIndexes',
        'correct_topkey': 'Entries',
        'clfn': 'location',
        'descfn': 'list_place_indexes',
        'key': 'IndexName'
    },
    'aws_location_route_calculator': {
        'current_topkey': 'RouteCalculators',
        'correct_topkey': 'Entries',
        'clfn': 'location',
        'descfn': 'list_route_calculators',
        'key': 'CalculatorName'
    },
    'aws_location_tracker': {
        'current_topkey': 'Trackers',
        'correct_topkey': 'Entries',
        'clfn': 'location',
        'descfn': 'list_trackers',
        'key': 'TrackerName'
    },
    'aws_macie2_invitation_accepter': {
        'current_topkey': 'Invitations',
        'correct_topkey': 'invitations',
        'clfn': 'macie2',
        'descfn': 'list_invitations',
        'key': 'AccountId'
    },
    'aws_media_packagev2_channel_group': {
        'current_topkey': 'items',
        'correct_topkey': 'Items',
        'clfn': 'mediapackagev2',
        'descfn': 'list_channel_groups',
        'key': 'Arn'
    },
    'aws_mskconnect_connector': {
        'current_topkey': 'Connectors',
        'correct_topkey': 'connectors',
        'clfn': 'kafkaconnect',
        'descfn': 'list_connectors',
        'key': 'Name'
    },
    'aws_mskconnect_custom_plugin': {
        'current_topkey': 'CustomPlugins',
        'correct_topkey': 'customPlugins',
        'clfn': 'kafkaconnect',
        'descfn': 'list_custom_plugins',
        'key': 'Name'
    },
    'aws_mskconnect_worker_configuration': {
        'current_topkey': 'WorkerConfigurations',
        'correct_topkey': 'workerConfigurations',
        'clfn': 'kafkaconnect',
        'descfn': 'list_worker_configurations',
        'key': 'Name'
    },
    'aws_neptune_event_subscription': {
        'current_topkey': 'EventSubscriptions',
        'correct_topkey': 'EventSubscriptionsList',
        'clfn': 'neptune',
        'descfn': 'describe_event_subscriptions',
        'key': 'SubscriptionName'
    },
    'aws_rekognition_stream_processor': {
        'current_topkey': 'StreamProcessors',
        'correct_topkey': '',  # No wrapper key
        'clfn': 'rekognition',
        'descfn': 'list_stream_processors',
        'key': 'Name'
    },
    'aws_rolesanywhere_profile': {
        'current_topkey': 'Profiles',
        'correct_topkey': 'profiles',
        'clfn': 'rolesanywhere',
        'descfn': 'list_profiles',
        'key': 'ProfileName'
    },
    'aws_rolesanywhere_trust_anchor': {
        'current_topkey': 'TrustAnchors',
        'correct_topkey': 'trustAnchors',
        'clfn': 'rolesanywhere',
        'descfn': 'list_trust_anchors',
        'key': 'TrustAnchorId'
    },
    'aws_rum_app_monitor': {
        'current_topkey': 'AppMonitors',
        'correct_topkey': 'AppMonitorSummaries',
        'clfn': 'rum',
        'descfn': 'list_app_monitors',
        'key': 'Name'
    },
    'aws_sagemaker_data_quality_job_definition': {
        'current_topkey': 'DataQualityJobDefinitions',
        'correct_topkey': 'JobDefinitionSummaries',
        'clfn': 'sagemaker',
        'descfn': 'list_data_quality_job_definitions',
        'key': 'DataQualityJobDefinitionArn'
    },
    'aws_sagemaker_feature_group': {
        'current_topkey': 'FeatureGroups',
        'correct_topkey': 'FeatureGroupSummaries',
        'clfn': 'sagemaker',
        'descfn': 'list_feature_groups',
        'key': 'FeatureGroupArn'
    },
    'aws_securityhub_account': {
        'current_topkey': 'Hub',
        'correct_topkey': '',  # No wrapper key
        'clfn': 'securityhub',
        'descfn': 'describe_hub',
        'key': 'HubArn'
    },
    'aws_servicecatalog_tag_option': {
        'current_topkey': 'TagOptions',
        'correct_topkey': 'TagOptionDetails',
        'clfn': 'servicecatalog',
        'descfn': 'list_tag_options',
        'key': 'Id'
    },
    'aws_ses_active_receipt_rule_set': {
        'current_topkey': 'Rules',
        'correct_topkey': '',  # No wrapper key
        'clfn': 'ses',
        'descfn': 'describe_active_receipt_rule_set',
        'key': 'Name'
    },
    'aws_simpledb_domain': {
        'current_topkey': 'DomainNames',
        'correct_topkey': '',  # No wrapper key
        'clfn': 'sdb',
        'descfn': 'list_domains',
        'key': 'DomainName'
    },
    'aws_sqs_queue': {
        'current_topkey': 'QueueUrls',
        'correct_topkey': '',  # No wrapper key
        'clfn': 'sqs',
        'descfn': 'list_queues',
        'key': ''
    },
    'aws_ssm_default_patch_baseline': {
        'current_topkey': 'Baseline',
        'correct_topkey': '',  # No wrapper key
        'clfn': 'ssm',
        'descfn': 'get_default_patch_baseline',
        'key': 'BaselineId'
    },
    'aws_wafregional_rate_based_rule': {
        'current_topkey': 'RateBasedRules',
        'correct_topkey': 'Rules',
        'clfn': 'waf-regional',
        'descfn': 'list_rate_based_rules',
        'key': 'RuleId'
    },
}
```

### Method Fixes Needed

```python
# These resources need method name corrections
METHOD_FIXES = {
    'aws_finspace_kx_cluster': {
        'current_method': 'list_clusters',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'finspace-data',
        'topkey': 'Clusters',
        'key': 'ClusterId'
    },
    'aws_finspace_kx_database': {
        'current_method': 'list_databases',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'finspace-data',
        'topkey': 'Databases',
        'key': 'DatabaseId'
    },
    'aws_finspace_kx_scaling_group': {
        'current_method': 'list_scaling_groups',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'finspace-data',
        'topkey': 'ScalingGroups',
        'key': 'ScalingGroupId'
    },
    'aws_finspace_kx_volume': {
        'current_method': 'list_volumes',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'finspace-data',
        'topkey': 'Volumes',
        'key': 'VolumeId'
    },
    'aws_load_balancer_policy': {
        'current_method': 'describe_load_balancer_policy_types',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'elbv2',
        'topkey': 'Policies',
        'key': 'PolicyName'
    },
    'aws_macie2_classification_export_configuration': {
        'current_method': 'list_classification_export_configurations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'macie2',
        'topkey': 'ClassificationExportConfigurations',
        'key': 'Id'
    },
    'aws_macie2_classification_job': {
        'current_method': 'list_jobs',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'macie2',
        'topkey': 'ClassificationJobs',
        'key': 'Id'
    },
    'aws_macie2_member': {
        'current_method': 'list_invitation_accepters',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'macie2',
        'topkey': 'InvitationAccepters',
        'key': 'AccountId'
    },
    'aws_msk_cluster_policy': {
        'current_method': 'list_cluster_policies',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'kafka',
        'topkey': 'ClusterPolicies',
        'key': 'PolicyName'
    },
    'aws_neptune_cluster_instance': {
        'current_method': 'describe_db_cluster_instances',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'neptune',
        'topkey': 'DBClusterInstances',
        'key': 'DBInstanceIdentifier'
    },
    'aws_networkfirewall_logging_configuration': {
        'current_method': 'list_logging_configurations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'network-firewall',
        'topkey': 'LoggingConfigurations',
        'key': 'FirewallArn'
    },
    'aws_networkfirewall_resource_policy': {
        'current_method': 'list_resource_policies',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'network-firewall',
        'topkey': 'ResourcePolicies',
        'key': 'ResourceArn'
    },
    'aws_networkmanager_attachment_accepter': {
        'current_method': 'list_attachment_accepters',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'networkmanager',
        'topkey': 'AttachmentAccepters',
        'key': 'AttachmentId'
    },
    'aws_networkmanager_connect_attachment': {
        'current_method': 'list_connect_attachments',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'networkmanager',
        'topkey': 'ConnectAttachments',
        'key': 'AttachmentId'
    },
    'aws_networkmanager_connection': {
        'current_method': 'list_connections',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'networkmanager',
        'topkey': 'Connections',
        'key': 'ConnectionId'
    },
    'aws_networkmanager_core_network_policy_attachment': {
        'current_method': 'list_core_network_policy_attachments',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'networkmanager',
        'topkey': 'CoreNetworkPolicyAttachments',
        'key': 'CoreNetworkPolicyAttachmentId'
    },
    'aws_networkmanager_customer_gateway_association': {
        'current_method': 'list_customer_gateway_associations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'networkmanager',
        'topkey': 'CustomerGatewayAssociations',
        'key': 'CustomerGatewayAssociationId'
    },
    'aws_networkmanager_link': {
        'current_method': 'list_links',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'networkmanager',
        'topkey': 'Links',
        'key': 'LinkId'
    },
    'aws_networkmanager_link_association': {
        'current_method': 'list_link_associations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'networkmanager',
        'topkey': 'LinkAssociations',
        'key': 'LinkAssociationId'
    },
    'aws_networkmanager_site_to_site_vpn_attachment': {
        'current_method': 'list_site_to_site_vpn_attachments',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'networkmanager',
        'topkey': 'SiteToSiteVpnAttachments',
        'key': 'SiteToSiteVpnAttachmentId'
    },
    'aws_networkmanager_transit_gateway_connect_peer_association': {
        'current_method': 'list_transit_gateway_connect_peers',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'networkmanager',
        'topkey': 'TransitGatewayConnectPeers',
        'key': 'TransitGatewayConnectPeerId'
    },
    'aws_networkmanager_transit_gateway_peering': {
        'current_method': 'list_transit_gateway_peerings',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'networkmanager',
        'topkey': 'TransitGatewayPeerings',
        'key': 'TransitGatewayPeeringId'
    },
    'aws_networkmanager_transit_gateway_route_table_attachment': {
        'current_method': 'list_transit_gateway_route_tables',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'networkmanager',
        'topkey': 'TransitGatewayRouteTables',
        'key': 'TransitGatewayRouteTableId'
    },
    'aws_networkmanager_vpc_attachment': {
        'current_method': 'list_vpc_attachments',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'networkmanager',
        'topkey': 'VpcAttachments',
        'key': 'VpcAttachmentId'
    },
    'aws_networkmonitor_probe': {
        'current_method': 'list_monitor_probes',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'networkmonitor',
        'topkey': 'probes',
        'key': 'probeArn'
    },
    'aws_oam_link': {
        'current_method': 'list_links',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'networkmanager',
        'topkey': 'Links',
        'key': 'LinkId'
    },
    'aws_oam_sink': {
        'current_method': 'list_links',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'networkmanager',
        'topkey': 'Links',
        'key': 'LinkId'
    },
    'aws_oam_sink_policy': {
        'current_method': 'list_links',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'networkmanager',
        'topkey': 'Links',
        'key': 'LinkId'
    },
    'aws_opensearch_inbound_connection_accepter': {
        'current_method': 'list_inbound_connection_accepters',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'opensearch',
        'topkey': 'InboundConnectionAccepters',
        'key': 'ConnectionId'
    },
    'aws_opensearch_outbound_connection': {
        'current_method': 'list_inbound_connection_accepters',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'opensearch',
        'topkey': 'InboundConnectionAccepters',
        'key': 'InboundConnectionId'
    },
    'aws_opensearch_package': {
        'current_method': 'list_packages',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'opensearch',
        'topkey': 'Packages',
        'key': 'PackageID'
    },
    'aws_opensearch_package_association': {
        'current_method': 'list_packages',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'opensearch',
        'topkey': 'Packages',
        'key': 'PackageID'
    },
    'aws_pinpoint_adm_channel': {
        'current_method': 'list_adm_channels',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'pinpoint',
        'topkey': 'AdmChannels',
        'key': 'Id'
    },
    'aws_pinpoint_apns_channel': {
        'current_method': 'list_apns_channels',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'pinpoint',
        'topkey': 'ApnsChannels',
        'key': 'Id'
    },
    'aws_pinpoint_apns_sandbox_channel': {
        'current_method': 'list_apns_sandbox_channels',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'pinpoint',
        'topkey': 'ApnsSandboxChannels',
        'key': 'Id'
    },
    'aws_pinpoint_apns_voip_channel': {
        'current_method': 'list_apns_voip_channels',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'pinpoint',
        'topkey': 'ApnsVoipChannels',
        'key': 'Id'
    },
    'aws_pinpoint_apns_voip_sandbox_channel': {
        'current_method': 'list_apns_voip_sandbox_channels',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'pinpoint',
        'topkey': 'ApnsVoipSandboxChannels',
        'key': 'Id'
    },
    'aws_pinpoint_app': {
        'current_method': 'list_apps',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'pinpoint',
        'topkey': 'Apps',
        'key': 'Id'
    },
    'aws_pinpoint_baidu_channel': {
        'current_method': 'list_baidu_channels',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'pinpoint',
        'topkey': 'BaiduChannels',
        'key': 'Id'
    },
    'aws_pinpoint_email_channel': {
        'current_method': 'list_email_channels',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'pinpoint',
        'topkey': 'EmailChannels',
        'key': 'Id'
    },
    'aws_pinpoint_email_template': {
        'current_method': 'list_email_templates',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'pinpoint-email',
        'topkey': 'TemplatesMetadata',
        'key': 'TemplateName'
    },
    'aws_pinpoint_event_stream': {
        'current_method': 'list_event_streams',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'pinpoint',
        'topkey': 'EventStreams',
        'key': 'Id'
    },
    'aws_pinpoint_gcm_channel': {
        'current_method': 'list_gcm_channels',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'pinpoint',
        'topkey': 'GcmChannels',
        'key': 'Id'
    },
    'aws_pinpoint_sms_channel': {
        'current_method': 'list_sms_channels',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'pinpoint',
        'topkey': 'SmsChannels',
        'key': 'Id'
    },
    'aws_proxy_protocol_policy': {
        'current_method': 'list_proxy_protocol_policies',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'wafv2',
        'topkey': 'ProxyProtocolPolicies',
        'key': 'Name'
    },
    'aws_quicksight_account_subscription': {
        'current_method': 'list_account_subscriptions',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'quicksight',
        'topkey': 'AccountSubscriptions',
        'key': 'SubscriptionId'
    },
    'aws_quicksight_folder_membership': {
        'current_method': 'list_folder_memberships',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'quicksight',
        'topkey': 'FolderMemberships',
        'key': 'FolderMembershipId'
    },
    'aws_quicksight_key_registration': {
        'current_method': 'list_key_registrations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'quicksight',
        'topkey': 'KeyRegistrations',
        'key': 'KeyArn'
    },
    'aws_ram_resource_share_accepter': {
        'current_method': 'list_resource_share_accepters',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'ram',
        'topkey': 'ResourceShareAccepters',
        'key': 'ResourceShareAccepterArn'
    },
    'aws_ram_sharing_with_organization': {
        'current_method': 'list_sharing_accounts',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'ram',
        'topkey': 'AccountIds',
        'key': 'AccountId'
    },
    'aws_rbin_rule': {
        'current_method': 'list_resolver_rules',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'rbin',
        'topkey': 'ResolverRules',
        'key': 'Id'
    },
    'aws_redshiftserverless_resource_policy': {
        'current_method': 'describe_resource_policies',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'redshift-serverless',
        'topkey': 'ResourcePolicies',
        'key': 'ResourcePolicyId'
    },
    'aws_resourceexplorer2_index': {
        'current_method': 'list_indices',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'resource-explorer-2',
        'topkey': 'Indices',
        'key': 'Name'
    },
    'aws_resourcegroups_resource': {
        'current_method': 'list_resources',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'resource-groups',
        'topkey': 'ResourceIdentifiers',
        'key': 'ResourceArn'
    },
    'aws_route53_resolver_firewall_rule': {
        'current_method': 'list_resolver_firewall_rules',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'route53resolver',
        'topkey': 'ResolverFirewallRules',
        'key': 'Id'
    },
    'aws_rum_metrics_destination': {
        'current_method': 'list_metrics_destinations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'rum',
        'topkey': 'MetricsDestinations',
        'key': 'Name'
    },
    'aws_s3control_bucket': {
        'current_method': 'list_buckets',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 's3control',
        'topkey': 'Buckets',
        'key': 'Name'
    },
    'aws_sagemaker_endpoint_configuration': {
        'current_method': 'list_endpoint_configurations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'sagemaker',
        'topkey': 'EndpointConfigurations',
        'key': 'EndpointConfigurationArn'
    },
    'aws_sagemaker_servicecatalog_portfolio_status': {
        'current_method': 'get_service_catalog_portfolio_status',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'sagemaker',
        'topkey': 'Status',
        'key': 'Status'
    },
    'aws_schemas_registry_policy': {
        'current_method': 'get_registry_policy',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'schemas',
        'topkey': 'Policy',
        'key': 'Policy'
    },
    'aws_securityhub_finding_aggregator': {
        'current_method': 'describe_finding_aggregators',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'securityhub',
        'topkey': 'FindingAggregators',
        'key': 'FindingAggregatorArn'
    },
    'aws_securityhub_insight': {
        'current_method': 'describe_insights',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'securityhub',
        'topkey': 'Insights',
        'key': 'InsightArn'
    },
    'aws_securityhub_invite_accepter': {
        'current_method': 'describe_invite_accepters',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'securityhub',
        'topkey': 'InviteAccepters',
        'key': 'InviteAccepterArn'
    },
    'aws_securityhub_member': {
        'current_method': 'describe_members',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'securityhub',
        'topkey': 'Members',
        'key': 'MemberArn'
    },
    'aws_securityhub_organization_admin_account': {
        'current_method': 'describe_organization_admin_account',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'securityhub',
        'topkey': 'AdminAccount',
        'key': 'AdminAccount'
    },
    'aws_securityhub_product_subscription': {
        'current_method': 'describe_product_subscriptions',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'securityhub',
        'topkey': 'ProductSubscriptions',
        'key': 'ProductSubscriptionArn'
    },
    'aws_securityhub_standards_subscription': {
        'current_method': 'describe_standards_subscriptions',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'securityhub',
        'topkey': 'StandardsSubscriptions',
        'key': 'StandardsSubscriptionArn'
    },
    'aws_securitylake_data_lake': {
        'current_method': 'describe_data_lakes',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'securitylake',
        'topkey': 'DataLakes',
        'key': 'DataLakeArn'
    },
    'aws_servicecatalog_budget_resource_association': {
        'current_method': 'list_budget_resource_associations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'servicecatalog',
        'topkey': 'BudgetResourceAssociations',
        'key': 'BudgetResourceAssociationId'
    },
    'aws_servicecatalog_organizations_access': {
        'current_method': 'list_organization_access',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'servicecatalog',
        'topkey': 'OrganizationAccess',
        'key': 'Id'
    },
    'aws_servicecatalog_portfolio_share': {
        'current_method': 'list_portfolio_shares',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'servicecatalog',
        'topkey': 'PortfolioShares',
        'key': 'Id'
    },
    'aws_servicecatalog_principal_portfolio_association': {
        'current_method': 'list_principal_portfolio_associations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'servicecatalog',
        'topkey': 'Principals',
        'key': 'PrincipalARN'
    },
    'aws_servicecatalog_product_portfolio_association': {
        'current_method': 'list_product_portfolio_associations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'servicecatalog',
        'topkey': 'PortfolioDetails',
        'key': 'Id'
    },
    'aws_servicecatalog_provisioned_product': {
        'current_method': 'list_provisioned_products',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'servicecatalog',
        'topkey': 'ProvisionedProducts',
        'key': 'Id'
    },
    'aws_servicecatalog_tag_option_resource_association': {
        'current_method': 'list_tag_option_resource_associations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'servicecatalog',
        'topkey': 'TagOptionResourceAssociations',
        'key': 'Id'
    },
    'aws_servicecatalogappregistry_attribute_group_association': {
        'current_method': 'list_attribute_group_associations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'servicecatalog-appregistry',
        'topkey': 'attributeGroupAssociations',
        'key': 'id'
    },
    'aws_servicequotas_template': {
        'current_method': 'list_templates',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'service-quotas',
        'topkey': 'Templates',
        'key': 'TemplateId'
    },
    'aws_servicequotas_template_association': {
        'current_method': 'list_template_associations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'service-quotas',
        'topkey': 'TemplateAssociations',
        'key': 'TemplateAssociationId'
    },
    'aws_ses_configuration_set': {
        'current_method': 'describe_configuration_sets',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'ses',
        'topkey': 'ConfigurationSets',
        'key': 'Name'
    },
    'aws_ses_domain_dkim': {
        'current_method': 'describe_domain_dkim',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'ses',
        'topkey': 'DkimAttributes',
        'key': 'DkimTokens'
    },
    'aws_ses_domain_identity': {
        'current_method': 'describe_domain_identity',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'ses',
        'topkey': 'DomainIdentities',
        'key': 'DomainIdentity'
    },
    'aws_ses_domain_identity_verification': {
        'current_method': 'describe_domain_identity_verification',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'ses',
        'topkey': 'VerificationToken',
        'key': 'VerificationToken'
    },
    'aws_ses_domain_mail_from': {
        'current_method': 'describe_domain_mail_from',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'ses',
        'topkey': 'MailFromAttributes',
        'key': 'MailFromDomain'
    },
    'aws_ses_email_identity': {
        'current_method': 'describe_email_identity',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'ses',
        'topkey': 'IdentityType',
        'key': 'IdentityType'
    },
    'aws_ses_event_destination': {
        'current_method': 'describe_event_destination',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'ses',
        'topkey': 'EventDestination',
        'key': 'EventDestination'
    },
    'aws_ses_identity_notification_topic': {
        'current_method': 'describe_identity_notification_topic',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'ses',
        'topkey': 'Identity',
        'key': 'Identity'
    },
    'aws_ses_identity_policy': {
        'current_method': 'describe_identity_policy',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'ses',
        'topkey': 'Policy',
        'key': 'Policy'
    },
    'aws_ses_receipt_filter': {
        'current_method': 'describe_receipt_filter',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'ses',
        'topkey': 'Filter',
        'key': 'Filter'
    },
    'aws_ses_template': {
        'current_method': 'describe_template',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'ses',
        'topkey': 'Template',
        'key': 'Template'
    },
    'aws_shield_application_layer_automatic_response': {
        'current_method': 'list_application_layer_automatic_response_associations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'shield',
        'topkey': 'ApplicationLayerAutomaticResponseAssociations',
        'key': 'Id'
    },
    'aws_shield_drt_access_log_bucket_association': {
        'current_method': 'list_drt_access_log_bucket_associations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'shield',
        'topkey': 'DrtAccessLogBucketAssociations',
        'key': 'Id'
    },
    'aws_shield_drt_access_role_arn_association': {
        'current_method': 'list_drt_access_role_arn_associations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'shield',
        'topkey': 'DrtAccessRoleArnAssociations',
        'key': 'Id'
    },
    'aws_shield_protection_health_check_association': {
        'current_method': 'list_protection_health_check_associations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'shield',
        'topkey': 'ProtectionHealthCheckAssociations',
        'key': 'Id'
    },
    'aws_snapshot_create_volume_permission': {
        'current_method': 'describe_create_volume_permissions',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'ec2',
        'topkey': 'CreateVolumePermissions',
        'key': 'UserId'
    },
    'aws_sns_sms_preferences': {
        'current_method': 'get_sms_preferences',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'sns',
        'topkey': 'SMSPreferences',
        'key': 'SMSPreferences'
    },
    'aws_ssm_patch_group': {
        'current_method': 'list_patch_groups',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'ssm',
        'topkey': 'PatchGroups',
        'key': 'PatchGroup'
    },
    'aws_ssoadmin_application_assignment_configuration': {
        'current_method': 'list_application_assignment_configurations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'sso-admin',
        'topkey': 'ApplicationAssignmentConfigurations',
        'key': 'AccountAssignmentCreationTime'
    },
    'aws_ssoadmin_customer_managed_policy_attachment': {
        'current_method': 'list_customer_managed_policy_attachments',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'sso-admin',
        'topkey': 'CustomerManagedPolicyAttachments',
        'key': 'AccountAssignmentCreationTime'
    },
    'aws_ssoadmin_instance_access_control_attributes': {
        'current_method': 'list_instance_access_control_attribute_configuration',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'sso-admin',
        'topkey': 'InstanceAccessControlAttributeConfiguration',
        'key': 'AccountAssignmentCreationTime'
    },
    'aws_ssoadmin_managed_policy_attachment': {
        'current_method': 'list_managed_policy_attachments',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'sso-admin',
        'topkey': 'ManagedPolicyAttachments',
        'key': 'AccountAssignmentCreationTime'
    },
    'aws_ssoadmin_permission_set_inline_policy': {
        'current_method': 'list_permission_set_inline_policies',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'sso-admin',
        'topkey': 'PermissionSetInlinePolicies',
        'key': 'PermissionSetArn'
    },
    'aws_ssoadmin_permissions_boundary_attachment': {
        'current_method': 'list_permissions_boundary_attachments',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'sso-admin',
        'topkey': 'PermissionsBoundaryAttachments',
        'key': 'AccountAssignmentCreationTime'
    },
    'aws_storagegateway_gateway': {
        'current_method': 'describe_gateways',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'storagegateway',
        'topkey': 'Gateways',
        'key': 'GatewayARN'
    },
    'aws_storagegateway_tape_pool': {
        'current_method': 'describe_tape_pools',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'storagegateway',
        'topkey': 'TapePools',
        'key': 'PoolARN'
    },
    'aws_synthetics_canary': {
        'current_method': 'list_canaries',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'synthetics',
        'topkey': 'Canaries',
        'key': 'Name'
    },
    'aws_synthetics_group': {
        'current_method': 'list_canary_groups',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'synthetics',
        'topkey': 'Groups',
        'key': 'Name'
    },
    'aws_synthetics_group_association': {
        'current_method': 'list_group_associations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'synthetics',
        'topkey': 'GroupAssociations',
        'key': 'Name'
    },
    'aws_transfer_ssh_key': {
        'current_method': 'list_ssh_public_keys',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'transfer',
        'topkey': 'SshPublicKeys',
        'key': 'Arn'
    },
    'aws_transfer_tag': {
        'current_method': 'list_tags',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'transfer',
        'topkey': 'Tags',
        'key': 'Key'
    },
    'aws_vpc_dhcp_options_association': {
        'current_method': 'describe_dhcp_options_associations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'ec2',
        'topkey': 'DhcpOptionsAssociations',
        'key': 'DhcpOptionsId'
    },
    'aws_vpc_endpoint_service_allowed_principal': {
        'current_method': 'describe_vpc_endpoint_service_allowed_principals',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'ec2',
        'topkey': 'AllowedPrincipals',
        'key': 'Principal'
    },
    'aws_vpc_endpoint_subnet_association': {
        'current_method': 'describe_vpc_endpoint_subnet_associations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'ec2',
        'topkey': 'SubnetAssociations',
        'key': 'SubnetId'
    },
    'aws_vpc_ipam_organization_admin_account': {
        'current_method': 'describe_ipam_organization_admin_accounts',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'ec2',
        'topkey': 'OrganizationAdminAccounts',
        'key': 'AccountId'
    },
    'aws_vpc_ipam_preview_next_cidr': {
        'current_method': 'describe_ipam_preview_next_cidrs',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'ec2',
        'topkey': 'Cidrs',
        'key': 'Cidr'
    },
    'aws_vpc_network_performance_metric_subscription': {
        'current_method': 'describe_network_insights_path_subscriptions',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'ec2',
        'topkey': 'NetworkInsightsPathSubscriptions',
        'key': 'NetworkInsightsPathSubscriptionId'
    },
    'aws_vpc_route_server_association': {
        'current_method': 'describe_route_server_associations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'ec2',
        'topkey': 'RouteServerAssociations',
        'key': 'RouteServerAssociationId'
    },
    'aws_vpc_route_server_propagation': {
        'current_method': 'describe_route_server_propagations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'ec2',
        'topkey': 'RouteServerPropagations',
        'key': 'RouteServerPropagationId'
    },
    'aws_vpc_route_server_vpc_association': {
        'current_method': 'describe_route_server_vpc_associations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'ec2',
        'topkey': 'RouteServerVpcAssociations',
        'key': 'RouteServerVpcAssociationId'
    },
    'aws_vpclattice_resource_configuration': {
        'current_method': 'list_resource_configurations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'vpc-lattice',
        'topkey': 'items',
        'key': 'id'
    },
    'aws_vpclattice_resource_gateway': {
        'current_method': 'list_resource_gateways',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'vpc-lattice',
        'topkey': 'items',
        'key': 'id'
    },
    'aws_vpclattice_service_network_resource_association': {
        'current_method': 'list_service_network_resource_associations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'vpc-lattice',
        'topkey': 'items',
        'key': 'id'
    },
    'aws_vpclattice_target_group_attachment': {
        'current_method': 'list_target_group_attachments',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'vpc-lattice',
        'topkey': 'TargetGroupAttachments',
        'key': 'TargetGroupAttachmentId'
    },
    'aws_vpn_connection_route': {
        'current_method': 'describe_vpn_connection_routes',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'ec2',
        'topkey': 'VpnConnectionRoutes',
        'key': 'DestinationCidrBlock'
    },
    'aws_vpn_gateway_attachment': {
        'current_method': 'describe_vpn_gateway_attachments',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'ec2',
        'topkey': 'VpnGatewayAttachments',
        'key': 'VpnGatewayId'
    },
    'aws_vpn_gateway_route_propagation': {
        'current_method': 'describe_vpn_gateway_route_propagations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'ec2',
        'topkey': 'VpnGatewayRoutePropagations',
        'key': 'VpnGatewayId'
    },
    'aws_wafregional_web_acl_association': {
        'current_method': 'list_web_acl_associations',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'waf-regional',
        'topkey': 'WebACLAssociations',
        'key': 'AssociationId'
    },
    'aws_xray_resource_policy': {
        'current_method': 'get_resource_policy',
        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs
        'clfn': 'xray',
        'topkey': 'ResourcePolicy',
        'key': 'PolicyName'
    },
}
```

