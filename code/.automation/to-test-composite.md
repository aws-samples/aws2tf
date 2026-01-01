# Composite ID Resources - Require Special Handling

**Total Resources:** 65

These resources use composite import IDs (multiple identifiers separated by commas) and are not currently supported by aws2tf's standard import mechanism. They require special handling to parse and manage the composite identifiers.

---

## aws_auditmanager

### `aws_auditmanager_assessment_delegation`

**Import ID Format:**
```
abcdef-123456,arn:aws:iam::123456789012:role/example,example
```

**Components:** 3
1. `abcdef-123456`
2. `arn:aws:iam::123456789012:role/example`
3. `example`

## aws_bedrockagentcore

### `aws_bedrockagentcore_agent_runtime_endpoint`

**Import ID Format:**
```
AGENTRUNTIME1234567890,example-endpoint
```

**Components:** 2
1. `AGENTRUNTIME1234567890`
2. `example-endpoint`

### `aws_bedrockagentcore_gateway_target`

**Import ID Format:**
```
GATEWAY1234567890,TARGET0987654321
```

**Components:** 2
1. `GATEWAY1234567890`
2. `TARGET0987654321`

### `aws_bedrockagentcore_memory_strategy`

**Import ID Format:**
```
MEMORY1234567890,STRATEGY0987654321
```

**Components:** 2
1. `MEMORY1234567890`
2. `STRATEGY0987654321`

## aws_cloudformation

### `aws_cloudformation_stack_set_instance`

**Import ID Format:**
```
example,123456789012,us-east-1
```

**Components:** 3
1. `example`
2. `123456789012`
3. `us-east-1`

## aws_codecommit

### `aws_codecommit_approval_rule_template_association`

**Import ID Format:**
```
approver-rule-for-example,MyExampleRepo
```

**Components:** 2
1. `approver-rule-for-example`
2. `MyExampleRepo`

## aws_cognito

### `aws_cognito_user_pool_ui_customization`

**Import ID Format:**
```
us-west-2_ZCTarbt5C,12bu4fuk3mlgqa2rtrujgp6egq
```

**Components:** 2
1. `us-west-2_ZCTarbt5C`
2. `12bu4fuk3mlgqa2rtrujgp6egq`

## aws_controltower

### `aws_controltower_control`

**Import ID Format:**
```
arn:aws:organizations::123456789101:ou/o-qqaejywet/ou-qg5o-ufbhdtv3,arn:aws:controltower:us-east-1::control/WTDSMKDKDNLE
```

**Components:** 2
1. `arn:aws:organizations::123456789101:ou/o-qqaejywet/ou-qg5o-ufbhdtv3`
2. `arn:aws:controltower:us-east-1::control/WTDSMKDKDNLE`

## aws_directory

### `aws_directory_service_region`

**Import ID Format:**
```
d-9267651497,us-east-2
```

**Components:** 2
1. `d-9267651497`
2. `us-east-2`

## aws_eks

### `aws_eks_capability`

**Import ID Format:**
```
my-cluster,my-capability
```

**Components:** 2
1. `my-cluster`
2. `my-capability`

## aws_elasticache

### `aws_elasticache_user_group_association`

**Import ID Format:**
```
userGoupId1,userId
```

**Components:** 2
1. `userGoupId1`
2. `userId`

## aws_finspace

### `aws_finspace_kx_cluster`

**Import ID Format:**
```
n3ceo7wqxoxcti5tujqwzs,my-tf-kx-cluster
```

**Components:** 2
1. `n3ceo7wqxoxcti5tujqwzs`
2. `my-tf-kx-cluster`

### `aws_finspace_kx_database`

**Import ID Format:**
```
n3ceo7wqxoxcti5tujqwzs,my-tf-kx-database
```

**Components:** 2
1. `n3ceo7wqxoxcti5tujqwzs`
2. `my-tf-kx-database`

### `aws_finspace_kx_dataview`

**Import ID Format:**
```
n3ceo7wqxoxcti5tujqwzs,my-tf-kx-database,my-tf-kx-dataview
```

**Components:** 3
1. `n3ceo7wqxoxcti5tujqwzs`
2. `my-tf-kx-database`
3. `my-tf-kx-dataview`

### `aws_finspace_kx_scaling_group`

**Import ID Format:**
```
n3ceo7wqxoxcti5tujqwzs,my-tf-kx-scalinggroup
```

**Components:** 2
1. `n3ceo7wqxoxcti5tujqwzs`
2. `my-tf-kx-scalinggroup`

### `aws_finspace_kx_user`

**Import ID Format:**
```
n3ceo7wqxoxcti5tujqwzs,my-tf-kx-user
```

**Components:** 2
1. `n3ceo7wqxoxcti5tujqwzs`
2. `my-tf-kx-user`

### `aws_finspace_kx_volume`

**Import ID Format:**
```
n3ceo7wqxoxcti5tujqwzs,my-tf-kx-volume
```

**Components:** 2
1. `n3ceo7wqxoxcti5tujqwzs`
2. `my-tf-kx-volume`

## aws_fis

### `aws_fis_target_account_configuration`

**Import ID Format:**
```
123456789012,abcd123456789
```

**Components:** 2
1. `123456789012`
2. `abcd123456789`

## aws_lakeformation

### `aws_lakeformation_data_cells_filter`

**Import ID Format:**
```
database_name,name,table_catalog_id,table_name
```

**Components:** 4
1. `database_name`
2. `name`
3. `table_catalog_id`
4. `table_name`

### `aws_lakeformation_lf_tag_expression`

**Import ID Format:**
```
example-tag-expression,123456789012
```

**Components:** 2
1. `example-tag-expression`
2. `123456789012`

## aws_lambda

### `aws_lambda_runtime_management_config`

**Import ID Format:**
```
example,$LATEST
```

**Components:** 2
1. `example`
2. `$LATEST`

## aws_licensemanager

### `aws_licensemanager_association`

**Import ID Format:**
```
arn:aws:ec2:eu-west-1:123456789012:image/ami-123456789abcdef01,arn:aws:license-manager:eu-west-1:123456789012:license-configuration:lic-0123456789abcdef0123456789abcdef
```

**Components:** 2
1. `arn:aws:ec2:eu-west-1:123456789012:image/ami-123456789abcdef01`
2. `arn:aws:license-manager:eu-west-1:123456789012:license-configuration:lic-0123456789abcdef0123456789abcdef`

## aws_lightsail

### `aws_lightsail_bucket_resource_access`

**Import ID Format:**
```
example-bucket,example-instance
```

**Components:** 2
1. `example-bucket`
2. `example-instance`

### `aws_lightsail_disk_attachment`

**Import ID Format:**
```
example-disk,example-instance
```

**Components:** 2
1. `example-disk`
2. `example-instance`

### `aws_lightsail_domain_entry`

**Import ID Format:**
```
www,example.com,A,127.0.0.1
```

**Components:** 4
1. `www`
2. `example.com`
3. `A`
4. `127.0.0.1`

### `aws_lightsail_lb_attachment`

**Import ID Format:**
```
example-load-balancer,example-instance
```

**Components:** 2
1. `example-load-balancer`
2. `example-instance`

### `aws_lightsail_lb_certificate`

**Import ID Format:**
```
example-load-balancer,example-load-balancer-certificate
```

**Components:** 2
1. `example-load-balancer`
2. `example-load-balancer-certificate`

### `aws_lightsail_lb_certificate_attachment`

**Import ID Format:**
```
example-load-balancer,example-certificate
```

**Components:** 2
1. `example-load-balancer`
2. `example-certificate`

## aws_m2

### `aws_m2_deployment`

**Import ID Format:**
```
APPLICATION-ID,DEPLOYMENT-ID
```

**Components:** 2
1. `APPLICATION-ID`
2. `DEPLOYMENT-ID`

## aws_msk

### `aws_msk_single_scram_secret_association`

**Import ID Format:**
```
arn:aws:kafka:us-west-2:123456789012:cluster/example/279c0212-d057-4dba-9aa9-1c4e5a25bfc7-3,arn:aws:secretsmanager:us-east-1:123456789012:secret:example-123456
```

**Components:** 2
1. `arn:aws:kafka:us-west-2:123456789012:cluster/example/279c0212-d057-4dba-9aa9-1c4e5a25bfc7-3`
2. `arn:aws:secretsmanager:us-east-1:123456789012:secret:example-123456`

## aws_nat

### `aws_nat_gateway_eip_association`

**Import ID Format:**
```
nat-1234567890abcdef1,eipalloc-1234567890abcdef1
```

**Components:** 2
1. `nat-1234567890abcdef1`
2. `eipalloc-1234567890abcdef1`

## aws_networkmanager

### `aws_networkmanager_customer_gateway_association`

**Import ID Format:**
```
global-network-0d47f6t230mz46dy4,arn:aws:ec2:us-west-2:123456789012:customer-gateway/cgw-123abc05e04123abc
```

**Components:** 2
1. `global-network-0d47f6t230mz46dy4`
2. `arn:aws:ec2:us-west-2:123456789012:customer-gateway/cgw-123abc05e04123abc`

### `aws_networkmanager_link_association`

**Import ID Format:**
```
global-network-0d47f6t230mz46dy4,link-444555aaabbb11223,device-07f6fd08867abc123
```

**Components:** 3
1. `global-network-0d47f6t230mz46dy4`
2. `link-444555aaabbb11223`
3. `device-07f6fd08867abc123`

### `aws_networkmanager_transit_gateway_connect_peer_association`

**Import ID Format:**
```
global-network-0d47f6t230mz46dy4,arn:aws:ec2:us-west-2:123456789012:transit-gateway-connect-peer/tgw-connect-peer-12345678
```

**Components:** 2
1. `global-network-0d47f6t230mz46dy4`
2. `arn:aws:ec2:us-west-2:123456789012:transit-gateway-connect-peer/tgw-connect-peer-12345678`

## aws_networkmonitor

### `aws_networkmonitor_probe`

**Import ID Format:**
```
monitor-7786087912324693644,probe-3qm8p693i4fi1h8lqylzkbp42e
```

**Components:** 2
1. `monitor-7786087912324693644`
2. `probe-3qm8p693i4fi1h8lqylzkbp42e`

## aws_notifications

### `aws_notifications_channel_association`

**Import ID Format:**
```
arn:aws:notifications:us-west-2:123456789012:configuration:example-notification-config,arn:aws:notificationscontacts:us-west-2:123456789012:emailcontact:example-contact
```

**Components:** 2
1. `arn:aws:notifications:us-west-2:123456789012:configuration:example-notification-config`
2. `arn:aws:notificationscontacts:us-west-2:123456789012:emailcontact:example-contact`

## aws_opensearch

### `aws_opensearch_authorize_vpc_endpoint_access`

**Import ID Format:**
```
authorize_vpc_endpoint_access-id-12345678,123456789012
```

**Components:** 2
1. `authorize_vpc_endpoint_access-id-12345678`
2. `123456789012`

## aws_organizations

### `aws_organizations_tag`

**Import ID Format:**
```
ou-1234567,ExampleKey
```

**Components:** 2
1. `ou-1234567`
2. `ExampleKey`

## aws_quicksight

### `aws_quicksight_custom_permissions`

**Import ID Format:**
```
123456789012,example-permissions
```

**Components:** 2
1. `123456789012`
2. `example-permissions`

### `aws_quicksight_folder_membership`

**Import ID Format:**
```
123456789012,example-folder,DATASET,example-dataset
```

**Components:** 4
1. `123456789012`
2. `example-folder`
3. `DATASET`
4. `example-dataset`

### `aws_quicksight_role_custom_permission`

**Import ID Format:**
```
012345678901,default,READER
```

**Components:** 3
1. `012345678901`
2. `default`
3. `READER`

### `aws_quicksight_role_membership`

**Import ID Format:**
```
012345678901,default,READER,example-group
```

**Components:** 4
1. `012345678901`
2. `default`
3. `READER`
4. `example-group`

## aws_s3control

### `aws_s3control_directory_bucket_access_point_scope`

**Import ID Format:**
```
example--zoneid--xa-s3,123456789012
```

**Components:** 2
1. `example--zoneid--xa-s3`
2. `123456789012`

## aws_securityhub

### `aws_securityhub_product_subscription`

**Import ID Format:**
```
arn:aws:securityhub:eu-west-1:733251395267:product/alertlogic/althreatmanagement,arn:aws:securityhub:eu-west-1:123456789012:product-subscription/alertlogic/althreatmanagement
```

**Components:** 2
1. `arn:aws:securityhub:eu-west-1:733251395267:product/alertlogic/althreatmanagement`
2. `arn:aws:securityhub:eu-west-1:123456789012:product-subscription/alertlogic/althreatmanagement`

## aws_servicecatalogappregistry

### `aws_servicecatalogappregistry_attribute_group_association`

**Import ID Format:**
```
12456778723424sdffsdfsdq34,12234t3564dsfsdf34asff4ww3
```

**Components:** 2
1. `12456778723424sdffsdfsdq34`
2. `12234t3564dsfsdf34asff4ww3`

## aws_servicequotas

### `aws_servicequotas_template`

**Import ID Format:**
```
us-east-1,L-2ACBD22F,lambda
```

**Components:** 3
1. `us-east-1`
2. `L-2ACBD22F`
3. `lambda`

## aws_sesv2

### `aws_sesv2_dedicated_ip_assignment`

**Import ID Format:**
```
0.0.0.0,my-pool
```

**Components:** 2
1. `0.0.0.0`
2. `my-pool`

## aws_ssoadmin

### `aws_ssoadmin_application_access_scope`

**Import ID Format:**
```
arn:aws:sso::123456789012:application/ssoins-123456789012/apl-123456789012,sso:account:access
```

**Components:** 2
1. `arn:aws:sso::123456789012:application/ssoins-123456789012/apl-123456789012`
2. `sso:account:access`

### `aws_ssoadmin_customer_managed_policy_attachment`

**Import ID Format:**
```
TestPolicy,/,arn:aws:sso:::permissionSet/ssoins-2938j0x8920sbj72/ps-80383020jr9302rk,arn:aws:sso:::instance/ssoins-2938j0x8920sbj72
```

**Components:** 4
1. `TestPolicy`
2. `/`
3. `arn:aws:sso:::permissionSet/ssoins-2938j0x8920sbj72/ps-80383020jr9302rk`
4. `arn:aws:sso:::instance/ssoins-2938j0x8920sbj72`

### `aws_ssoadmin_permissions_boundary_attachment`

**Import ID Format:**
```
arn:aws:sso:::permissionSet/ssoins-2938j0x8920sbj72/ps-80383020jr9302rk,arn:aws:sso:::instance/ssoins-2938j0x8920sbj72
```

**Components:** 2
1. `arn:aws:sso:::permissionSet/ssoins-2938j0x8920sbj72/ps-80383020jr9302rk`
2. `arn:aws:sso:::instance/ssoins-2938j0x8920sbj72`

## aws_synthetics

### `aws_synthetics_group_association`

**Import ID Format:**
```
arn:aws:synthetics:us-west-2:123456789012:canary:tf-acc-test-abcd1234,examplename
```

**Components:** 2
1. `arn:aws:synthetics:us-west-2:123456789012:canary:tf-acc-test-abcd1234`
2. `examplename`

## aws_transfer

### `aws_transfer_host_key`

**Import ID Format:**
```
s-12345678,key-12345
```

**Components:** 2
1. `s-12345678`
2. `key-12345`

### `aws_transfer_tag`

**Import ID Format:**
```
arn:aws:transfer:us-east-1:123456789012:server/s-1234567890abcdef0,Name
```

**Components:** 2
1. `arn:aws:transfer:us-east-1:123456789012:server/s-1234567890abcdef0`
2. `Name`

## aws_verifiedpermissions

### `aws_verifiedpermissions_policy`

**Import ID Format:**
```
policy-id-12345678,policy-store-id-12345678
```

**Components:** 2
1. `policy-id-12345678`
2. `policy-store-id-12345678`

## aws_vpc

### `aws_vpc_route_server_propagation`

**Import ID Format:**
```
rs-12345678,rtb-656c65616e6f72
```

**Components:** 2
1. `rs-12345678`
2. `rtb-656c65616e6f72`

### `aws_vpc_route_server_vpc_association`

**Import ID Format:**
```
rs-12345678,vpc-0f001273ec18911b1
```

**Components:** 2
1. `rs-12345678`
2. `vpc-0f001273ec18911b1`

## aws_wafv2

### `aws_wafv2_api_key`

**Import ID Format:**
```
a1b2c3d4-5678-90ab-cdef-EXAMPLE11111,REGIONAL
```

**Components:** 2
1. `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`
2. `REGIONAL`

### `aws_wafv2_web_acl_rule_group_association`

**Import ID Format:**
```
arn:aws:wafv2:us-east-1:123456789012:regional/webacl/example-web-acl/12345678-1234-1234-1234-123456789012,arn:aws:wafv2:us-east-1:123456789012:regional/rulegroup/example-rule-group/87654321-4321-4321-4321-210987654321,example-rule-group-rule
```

**Components:** 3
1. `arn:aws:wafv2:us-east-1:123456789012:regional/webacl/example-web-acl/12345678-1234-1234-1234-123456789012`
2. `arn:aws:wafv2:us-east-1:123456789012:regional/rulegroup/example-rule-group/87654321-4321-4321-4321-210987654321`
3. `example-rule-group-rule`

## aws_workspacesweb

### `aws_workspacesweb_browser_settings_association`

**Import ID Format:**
```
arn:aws:workspaces-web:us-west-2:123456789012:browserSettings/browser_settings-id-12345678,arn:aws:workspaces-web:us-west-2:123456789012:portal/portal-id-12345678
```

**Components:** 2
1. `arn:aws:workspaces-web:us-west-2:123456789012:browserSettings/browser_settings-id-12345678`
2. `arn:aws:workspaces-web:us-west-2:123456789012:portal/portal-id-12345678`

### `aws_workspacesweb_data_protection_settings_association`

**Import ID Format:**
```
arn:aws:workspaces-web:us-west-2:123456789012:dataProtectionSettings/data_protection_settings-id-12345678,arn:aws:workspaces-web:us-west-2:123456789012:portal/portal-id-12345678
```

**Components:** 2
1. `arn:aws:workspaces-web:us-west-2:123456789012:dataProtectionSettings/data_protection_settings-id-12345678`
2. `arn:aws:workspaces-web:us-west-2:123456789012:portal/portal-id-12345678`

### `aws_workspacesweb_ip_access_settings_association`

**Import ID Format:**
```
arn:aws:workspaces-web:us-west-2:123456789012:ipAccessSettings/ip_access_settings-id-12345678,arn:aws:workspaces-web:us-west-2:123456789012:portal/portal-id-12345678
```

**Components:** 2
1. `arn:aws:workspaces-web:us-west-2:123456789012:ipAccessSettings/ip_access_settings-id-12345678`
2. `arn:aws:workspaces-web:us-west-2:123456789012:portal/portal-id-12345678`

### `aws_workspacesweb_network_settings_association`

**Import ID Format:**
```
arn:aws:workspaces-web:us-west-2:123456789012:networkSettings/network_settings-id-12345678,arn:aws:workspaces-web:us-west-2:123456789012:portal/portal-id-12345678
```

**Components:** 2
1. `arn:aws:workspaces-web:us-west-2:123456789012:networkSettings/network_settings-id-12345678`
2. `arn:aws:workspaces-web:us-west-2:123456789012:portal/portal-id-12345678`

### `aws_workspacesweb_session_logger_association`

**Import ID Format:**
```
arn:aws:workspaces-web:us-west-2:123456789012:sessionLogger/session_logger-id-12345678,arn:aws:workspaces-web:us-west-2:123456789012:portal/portal-id-12345678
```

**Components:** 2
1. `arn:aws:workspaces-web:us-west-2:123456789012:sessionLogger/session_logger-id-12345678`
2. `arn:aws:workspaces-web:us-west-2:123456789012:portal/portal-id-12345678`

### `aws_workspacesweb_trust_store_association`

**Import ID Format:**
```
arn:aws:workspaces-web:us-west-2:123456789012:trustStore/trust_store-id-12345678,arn:aws:workspaces-web:us-west-2:123456789012:portal/portal-id-12345678
```

**Components:** 2
1. `arn:aws:workspaces-web:us-west-2:123456789012:trustStore/trust_store-id-12345678`
2. `arn:aws:workspaces-web:us-west-2:123456789012:portal/portal-id-12345678`

### `aws_workspacesweb_user_access_logging_settings_association`

**Import ID Format:**
```
arn:aws:workspaces-web:us-west-2:123456789012:userAccessLoggingSettings/user_access_logging_settings-id-12345678,arn:aws:workspaces-web:us-west-2:123456789012:portal/portal-id-12345678
```

**Components:** 2
1. `arn:aws:workspaces-web:us-west-2:123456789012:userAccessLoggingSettings/user_access_logging_settings-id-12345678`
2. `arn:aws:workspaces-web:us-west-2:123456789012:portal/portal-id-12345678`

---

## Implementation Notes

To support these resources, aws2tf would need to:

1. **Parse composite IDs** - Split the import ID by comma to extract individual components
2. **Validate components** - Ensure each component exists and is accessible
3. **Handle dependencies** - Many composite IDs reference parent resources (e.g., portal + settings)
4. **Generate correct imports** - Create Terraform import blocks with the full composite ID
5. **Track relationships** - Maintain awareness of resource associations

Association resources (like `*_association`) typically link two parent resources together and use both resource identifiers in the import ID.
