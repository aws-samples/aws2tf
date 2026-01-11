# CloudFormation Stack Resources - Unsupported

This file lists all CloudFormation resource types that cannot currently be implemented in aws2tf due to:
- No Terraform AWS provider support
- Marked as not implemented in aws2tf (aws_not_implemented.py)
- No import support in Terraform (aws_no_import.py)

**Total Unsupported Resources:** 236
**Services:** 109

## Status Categories

- **NO TERRAFORM SUPPORT**: Terraform AWS provider does not have an equivalent resource
- **NOT SUPPORTED**: Resource exists in Terraform but is in aws_not_implemented.py
- **NO IMPORT SUPPORT**: Terraform can create but cannot import this resource type

## Unsupported Resources by Service

### AIOps (1 resources)

- [ ] `AWS::AIOps::Investigation` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### ARCRegionSwitch (1 resources)

- [ ] `AWS::ARCRegionSwitch::RegionSwitch` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### ASK (1 resources)

- [ ] `AWS::ASK::Skill` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### AppIntegrations (2 resources)

- [ ] `AWS::AppIntegrations::DataIntegration` <!-- NO IMPORT SUPPORT: aws_appintegrations_data_integration - Terraform does not support importing this resource type -->
- [ ] `AWS::AppIntegrations::EventIntegration` <!-- NO IMPORT SUPPORT: aws_appintegrations_event_integration - Terraform does not support importing this resource type -->

### AppRunner (5 resources)

- [ ] `AWS::AppRunner::ObservabilityConfiguration` <!-- NOT SUPPORTED: aws_apprunner_observability_configuration is in aws_not_implemented.py -->

### AppStream (13 resources)

- [ ] `AWS::AppStream::DirectoryConfig` <!-- NOT SUPPORTED: aws_appstream_directory_config is in aws_not_implemented.py -->

### AppSync (10 resources)

- [ ] `AWS::AppSync::ApiCache` <!-- NOT SUPPORTED: aws_appsync_api_cache is in aws_not_implemented.py -->
- [ ] `AWS::AppSync::DomainNameApiAssociation` <!-- NOT SUPPORTED: aws_appsync_domain_name_api_association is in aws_not_implemented.py -->

### AppTest (1 resources)

- [ ] `AWS::AppTest::TestCase` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### ApplicationSignals (1 resources)

- [ ] `AWS::ApplicationSignals::ServiceLevelObjective` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### AuditManager (1 resources)

- [ ] `AWS::AuditManager::Assessment` <!-- NOT SUPPORTED: aws_auditmanager_assessment is in aws_not_implemented.py -->

### BCMDataExports (1 resources)

- [ ] `AWS::BCMDataExports::Export` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### Backup (7 resources)

- [ ] `AWS::Backup::Framework` <!-- NO IMPORT SUPPORT: aws_backup_framework - Terraform does not support importing this resource type -->

### BedrockAgentCore (1 resources)

- [ ] `AWS::BedrockAgentCore::AgentVersion` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### Billing (1 resources)

- [ ] `AWS::Billing::BillingView` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### Budgets (2 resources)

- [ ] `AWS::Budgets::Budget` <!-- NOT SUPPORTED: aws_budgets_budget is in aws_not_implemented.py -->

### CE (3 resources)

- [ ] `AWS::CE::AnomalyMonitor` <!-- NOT SUPPORTED: aws_ce_anomaly_monitor is in aws_not_implemented.py -->
- [ ] `AWS::CE::AnomalySubscription` <!-- NOT SUPPORTED: aws_ce_anomaly_subscription is in aws_not_implemented.py -->
- [ ] `AWS::CE::CostCategory` <!-- NOT SUPPORTED: aws_ce_cost_category is in aws_not_implemented.py -->

### CUR (1 resources)

- [ ] `AWS::CUR::ReportDefinition` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### Cases (2 resources)

- [ ] `AWS::Cases::Domain` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::Cases::IntegrationAssociation` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### CleanRooms (5 resources)

- [ ] `AWS::CleanRooms::Collaboration` <!-- NO IMPORT SUPPORT: aws_cleanrooms_collaboration - Terraform does not support importing this resource type -->

### CleanRoomsML (1 resources)

- [ ] `AWS::CleanRoomsML::TrainingDataset` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### CloudFront (9 resources)

- [ ] `AWS::CloudFront::MonitoringSubscription` <!-- NOT SUPPORTED: aws_cloudfront_monitoring_subscription is in aws_not_implemented.py -->
- [ ] `AWS::CloudFront::ResponseHeadersPolicy` <!-- NO IMPORT SUPPORT: aws_cloudfront_response_headers_policy - Terraform does not support importing this resource type -->

### CodeBuild (2 resources)

- [ ] `AWS::CodeBuild::SourceCredential` <!-- NO IMPORT SUPPORT: aws_codebuild_source_credential - Terraform does not support importing this resource type -->

### CodeConnections (3 resources)

- [ ] `AWS::CodeConnections::Connection` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::CodeConnections::RepositoryLink` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::CodeConnections::SyncConfiguration` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### CodeGuruReviewer (1 resources)

- [ ] `AWS::CodeGuruReviewer::RepositoryAssociation` <!-- NO IMPORT SUPPORT: aws_codegurureviewer_repository_association - Terraform does not support importing this resource type -->

### Cognito (11 resources)

- [ ] `AWS::Cognito::UserPoolDomain` <!-- NOT SUPPORTED: aws_cognito_user_pool_domain is in aws_not_implemented.py -->

### Comprehend (2 resources)

- [ ] `AWS::Comprehend::DocumentClassifier` <!-- NOT SUPPORTED: aws_comprehend_document_classifier is in aws_not_implemented.py -->

### Config (7 resources)

- [ ] `AWS::Config::ConformancePack` <!-- NO IMPORT SUPPORT: aws_config_conformance_pack - Terraform does not support importing this resource type -->

### Connect (13 resources)

- [ ] `AWS::Connect::ContactFlowModule` <!-- NOT SUPPORTED: aws_connect_contact_flow_module is in aws_not_implemented.py -->
- [ ] `AWS::Connect::UserHierarchyGroup` <!-- NOT SUPPORTED: aws_connect_user_hierarchy_group is in aws_not_implemented.py -->

### ConnectCampaignsV2 (1 resources)

- [ ] `AWS::ConnectCampaignsV2::Campaign` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### DAX (3 resources)

- [ ] `AWS::DAX::Cluster` <!-- NOT SUPPORTED: aws_dax_cluster is in aws_not_implemented.py -->
- [ ] `AWS::DAX::ParameterGroup` <!-- NOT SUPPORTED: aws_dax_parameter_group is in aws_not_implemented.py -->
- [ ] `AWS::DAX::SubnetGroup` <!-- NOT SUPPORTED: aws_dax_subnet_group is in aws_not_implemented.py -->

### DLM (1 resources)

- [ ] `AWS::DLM::LifecyclePolicy` <!-- NOT SUPPORTED: aws_dlm_lifecycle_policy is in aws_not_implemented.py -->

### DSQL (1 resources)

- [ ] `AWS::DSQL::Cluster` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### DataPipeline (1 resources)

- [ ] `AWS::DataPipeline::Pipeline` <!-- NOT SUPPORTED: aws_datapipeline_pipeline is in aws_not_implemented.py -->

### DataSync (14 resources)

- [ ] `AWS::DataSync::LocationAzureBlob` <!-- NOT SUPPORTED: aws_datasync_location_azure_blob is in aws_not_implemented.py -->
- [ ] `AWS::DataSync::LocationEFS` <!-- NOT SUPPORTED: aws_datasync_location_efs is in aws_not_implemented.py -->
- [ ] `AWS::DataSync::LocationHDFS` <!-- NOT SUPPORTED: aws_datasync_location_hdfs is in aws_not_implemented.py -->
- [ ] `AWS::DataSync::LocationNFS` <!-- NOT SUPPORTED: aws_datasync_location_nfs is in aws_not_implemented.py -->
- [ ] `AWS::DataSync::LocationObjectStorage` <!-- NOT SUPPORTED: aws_datasync_location_object_storage is in aws_not_implemented.py -->
- [ ] `AWS::DataSync::LocationS3` <!-- NOT SUPPORTED: aws_datasync_location_s3 is in aws_not_implemented.py -->
- [ ] `AWS::DataSync::LocationSMB` <!-- NOT SUPPORTED: aws_datasync_location_smb is in aws_not_implemented.py -->

### Deadline (9 resources)

- [ ] `AWS::Deadline::Farm` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::Deadline::Fleet` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::Deadline::LicenseEndpoint` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::Deadline::MeteredProduct` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::Deadline::Monitor` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::Deadline::Queue` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::Deadline::QueueEnvironment` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::Deadline::QueueFleetAssociation` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::Deadline::StorageProfile` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### DevOpsAgent (1 resources)

- [ ] `AWS::DevOpsAgent::AgentConfiguration` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### DeviceFarm (6 resources)

- [ ] `AWS::DeviceFarm::DevicePool` <!-- NOT SUPPORTED: aws_devicefarm_device_pool is in aws_not_implemented.py -->
- [ ] `AWS::DeviceFarm::InstanceProfile` <!-- NOT SUPPORTED: aws_devicefarm_instance_profile is in aws_not_implemented.py -->
- [ ] `AWS::DeviceFarm::NetworkProfile` <!-- NOT SUPPORTED: aws_devicefarm_network_profile is in aws_not_implemented.py -->
- [ ] `AWS::DeviceFarm::Project` <!-- NOT SUPPORTED: aws_devicefarm_project is in aws_not_implemented.py -->
- [ ] `AWS::DeviceFarm::TestGridProject` <!-- NOT SUPPORTED: aws_devicefarm_test_grid_project is in aws_not_implemented.py -->

### DocDBElastic (1 resources)

- [ ] `AWS::DocDBElastic::Cluster` <!-- NOT SUPPORTED: aws_docdbelastic_cluster is in aws_not_implemented.py -->

### DynamoDB (1 resources)

- [ ] `AWS::DynamoDB::GlobalTable` <!-- NOT SUPPORTED: aws_dynamodb_global_table is in aws_not_implemented.py -->

### EC2 (67 resources)

- [ ] `AWS::EC2::LocalGatewayRoute` <!-- NOT SUPPORTED: aws_ec2_local_gateway_route is in aws_not_implemented.py -->
- [ ] `AWS::EC2::TransitGatewayMulticastDomainAssociation` <!-- NO IMPORT SUPPORT: aws_ec2_transit_gateway_multicast_domain_association - Terraform does not support importing this resource type -->
- [ ] `AWS::EC2::TransitGatewayMulticastGroupMember` <!-- NO IMPORT SUPPORT: aws_ec2_transit_gateway_multicast_group_member - Terraform does not support importing this resource type -->
- [ ] `AWS::EC2::TransitGatewayMulticastGroupSource` <!-- NO IMPORT SUPPORT: aws_ec2_transit_gateway_multicast_group_source - Terraform does not support importing this resource type -->

### ECR (3 resources)

- [ ] `AWS::ECR::ReplicationConfiguration` <!-- NO IMPORT SUPPORT: aws_ecr_replication_configuration - Terraform does not support importing this resource type -->

### EKS (5 resources)

- [ ] `AWS::EKS::PodIdentityAssociation` <!-- NO IMPORT SUPPORT: aws_eks_pod_identity_association - Terraform does not support importing this resource type -->

### EMR (5 resources)

- [ ] `AWS::EMR::Studio` <!-- NOT SUPPORTED: aws_emr_studio is in aws_not_implemented.py -->
- [ ] `AWS::EMR::StudioSessionMapping` <!-- NOT SUPPORTED: aws_emr_studio_session_mapping is in aws_not_implemented.py -->

### EMRContainers (1 resources)

- [ ] `AWS::EMRContainers::VirtualCluster` <!-- NOT SUPPORTED: aws_emrcontainers_virtual_cluster is in aws_not_implemented.py -->

### EMRServerless (1 resources)

- [ ] `AWS::EMRServerless::Application` <!-- NOT SUPPORTED: aws_emrserverless_application is in aws_not_implemented.py -->

### EVS (1 resources)

- [ ] `AWS::EVS::Cluster` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### Evidently (5 resources)

- [ ] `AWS::Evidently::Project` <!-- NOT SUPPORTED: aws_evidently_project is in aws_not_implemented.py -->
- [ ] `AWS::Evidently::Segment` <!-- NOT SUPPORTED: aws_evidently_segment is in aws_not_implemented.py -->

### FIS (2 resources)

- [ ] `AWS::FIS::TargetAccountConfiguration` <!-- NOT SUPPORTED: aws_fis_target_account_configuration is in aws_not_implemented.py -->

### FMS (3 resources)

- [ ] `AWS::FMS::Policy` <!-- NOT SUPPORTED: aws_fms_policy is in aws_not_implemented.py -->

### FSx (5 resources)

- [ ] `AWS::FSx::DataRepositoryAssociation` <!-- NO IMPORT SUPPORT: aws_fsx_data_repository_association - Terraform does not support importing this resource type -->

### GameLift (9 resources)

- [ ] `AWS::GameLift::Fleet` <!-- NOT SUPPORTED: aws_gamelift_fleet is in aws_not_implemented.py -->
- [ ] `AWS::GameLift::GameSessionQueue` <!-- NOT SUPPORTED: aws_gamelift_game_session_queue is in aws_not_implemented.py -->

### GameLiftStreams (1 resources)

- [ ] `AWS::GameLiftStreams::Stream` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### GlobalAccelerator (3 resources)

- [ ] `AWS::GlobalAccelerator::Accelerator` <!-- NO IMPORT SUPPORT: aws_globalaccelerator_accelerator - Terraform does not support importing this resource type -->

### IVS (4 resources)

- [ ] `AWS::IVS::Channel` <!-- NOT SUPPORTED: aws_ivs_channel is in aws_not_implemented.py -->
- [ ] `AWS::IVS::PlaybackKeyPair` <!-- NOT SUPPORTED: aws_ivs_playback_key_pair is in aws_not_implemented.py -->
- [ ] `AWS::IVS::RecordingConfiguration` <!-- NOT SUPPORTED: aws_ivs_recording_configuration is in aws_not_implemented.py -->

### IVSChat (2 resources)

- [ ] `AWS::IVSChat::LoggingConfiguration` <!-- NOT SUPPORTED: aws_ivschat_logging_configuration is in aws_not_implemented.py -->
- [ ] `AWS::IVSChat::Room` <!-- NOT SUPPORTED: aws_ivschat_room is in aws_not_implemented.py -->

### ImageBuilder (9 resources)

- [ ] `AWS::ImageBuilder::Image` <!-- NO IMPORT SUPPORT: aws_imagebuilder_image - Terraform does not support importing this resource type -->
- [ ] `AWS::ImageBuilder::LifecyclePolicy` <!-- NOT SUPPORTED: aws_imagebuilder_lifecycle_policy is in aws_not_implemented.py -->
- [ ] `AWS::ImageBuilder::Workflow` <!-- NOT SUPPORTED: aws_imagebuilder_workflow is in aws_not_implemented.py -->

### Inspector (3 resources)

- [ ] `AWS::Inspector::AssessmentTarget` <!-- NOT SUPPORTED: aws_inspector_assessment_target is in aws_not_implemented.py -->
- [ ] `AWS::Inspector::AssessmentTemplate` <!-- NOT SUPPORTED: aws_inspector_assessment_template is in aws_not_implemented.py -->
- [ ] `AWS::Inspector::ResourceGroup` <!-- NO IMPORT SUPPORT: aws_inspector_resource_group - Terraform does not support importing this resource type -->

### Invoicing (1 resources)

- [ ] `AWS::Invoicing::InvoiceUnit` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### IoT (28 resources)

- [ ] `AWS::IoT::Authorizer` <!-- NOT SUPPORTED: aws_iot_authorizer is in aws_not_implemented.py -->
- [ ] `AWS::IoT::BillingGroup` <!-- NOT SUPPORTED: aws_iot_billing_group is in aws_not_implemented.py -->
- [ ] `AWS::IoT::Certificate` <!-- NO IMPORT SUPPORT: aws_iot_certificate - Terraform does not support importing this resource type -->
- [ ] `AWS::IoT::DomainConfiguration` <!-- NOT SUPPORTED: aws_iot_domain_configuration is in aws_not_implemented.py -->
- [ ] `AWS::IoT::ProvisioningTemplate` <!-- NOT SUPPORTED: aws_iot_provisioning_template is in aws_not_implemented.py -->
- [ ] `AWS::IoT::RoleAlias` <!-- NOT SUPPORTED: aws_iot_role_alias is in aws_not_implemented.py -->
- [ ] `AWS::IoT::ThingGroup` <!-- NOT SUPPORTED: aws_iot_thing_group is in aws_not_implemented.py -->
- [ ] `AWS::IoT::ThingPrincipalAttachment` <!-- NO IMPORT SUPPORT: aws_iot_thing_principal_attachment - Terraform does not support importing this resource type -->
- [ ] `AWS::IoT::ThingType` <!-- NOT SUPPORTED: aws_iot_thing_type is in aws_not_implemented.py -->
- [ ] `AWS::IoT::TopicRuleDestination` <!-- NOT SUPPORTED: aws_iot_topic_rule_destination is in aws_not_implemented.py -->

### IoTFleetWise (6 resources)

- [ ] `AWS::IoTFleetWise::Campaign` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::IoTFleetWise::DecoderManifest` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::IoTFleetWise::Fleet` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::IoTFleetWise::ModelManifest` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::IoTFleetWise::SignalCatalog` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::IoTFleetWise::Vehicle` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### IoTManagedIntegrations (1 resources)

- [ ] `AWS::IoTManagedIntegrations::Integration` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### KMS (1 resources)

- [ ] `AWS::KMS::ReplicaKey` <!-- NOT SUPPORTED: aws_kms_replica_key is in aws_not_implemented.py -->

### LakeFormation (3 resources)

- [ ] `AWS::LakeFormation::DataCellsFilter` <!-- NOT SUPPORTED: aws_lakeformation_data_cells_filter is in aws_not_implemented.py -->

### Lambda (5 resources)

- [ ] `AWS::Lambda::LayerVersionPermission` <!-- NO IMPORT SUPPORT: aws_lambda_layer_version_permission - Terraform does not support importing this resource type -->

### LaunchWizard (1 resources)

- [ ] `AWS::LaunchWizard::Deployment` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### LicenseManager (2 resources)

- [ ] `AWS::LicenseManager::Grant` <!-- NOT SUPPORTED: aws_licensemanager_grant is in aws_not_implemented.py -->

### Lightsail (10 resources)

- [ ] `AWS::Lightsail::StaticIp` <!-- NO IMPORT SUPPORT: aws_lightsail_static_ip - Terraform does not support importing this resource type -->

### Logs (1 resources)

- [ ] `AWS::Logs::QueryDefinition` <!-- NO IMPORT SUPPORT: aws_cloudwatch_query_definition - Terraform does not support importing this resource type -->

### Location (7 resources)

- [ ] `AWS::Location::GeofenceCollection` <!-- NOT SUPPORTED: aws_location_geofence_collection is in aws_not_implemented.py -->
- [ ] `AWS::Location::Map` <!-- NOT SUPPORTED: aws_location_map is in aws_not_implemented.py -->
- [ ] `AWS::Location::PlaceIndex` <!-- NOT SUPPORTED: aws_location_place_index is in aws_not_implemented.py -->
- [ ] `AWS::Location::RouteCalculator` <!-- NOT SUPPORTED: aws_location_route_calculator is in aws_not_implemented.py -->
- [ ] `AWS::Location::Tracker` <!-- NOT SUPPORTED: aws_location_tracker is in aws_not_implemented.py -->

### LookoutEquipment (1 resources)

- [ ] `AWS::LookoutEquipment::InferenceScheduler` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### M2 (2 resources)

- [ ] `AWS::M2::Application` <!-- NOT SUPPORTED: aws_m2_application is in aws_not_implemented.py -->
- [ ] `AWS::M2::Environment` <!-- NOT SUPPORTED: aws_m2_environment is in aws_not_implemented.py -->

### MPA (1 resources)

- [ ] `AWS::MPA::ApprovalRuleTemplate` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### NeptuneGraph (2 resources)

- [ ] `AWS::NeptuneGraph::Graph` <!-- NOT SUPPORTED: aws_neptunegraph_graph is in aws_not_implemented.py -->

### NetworkManager (14 resources)

- [ ] `AWS::NetworkManager::ConnectAttachment` <!-- NOT SUPPORTED: aws_networkmanager_connect_attachment is in aws_not_implemented.py -->
- [ ] `AWS::NetworkManager::CustomerGatewayAssociation` <!-- NOT SUPPORTED: aws_networkmanager_customer_gateway_association is in aws_not_implemented.py -->
- [ ] `AWS::NetworkManager::Link` <!-- NOT SUPPORTED: aws_networkmanager_link is in aws_not_implemented.py -->
- [ ] `AWS::NetworkManager::LinkAssociation` <!-- NOT SUPPORTED: aws_networkmanager_link_association is in aws_not_implemented.py -->
- [ ] `AWS::NetworkManager::SiteToSiteVpnAttachment` <!-- NOT SUPPORTED: aws_networkmanager_site_to_site_vpn_attachment is in aws_not_implemented.py -->
- [ ] `AWS::NetworkManager::TransitGatewayPeering` <!-- NOT SUPPORTED: aws_networkmanager_transit_gateway_peering is in aws_not_implemented.py -->
- [ ] `AWS::NetworkManager::TransitGatewayRouteTableAttachment` <!-- NOT SUPPORTED: aws_networkmanager_transit_gateway_route_table_attachment is in aws_not_implemented.py -->
- [ ] `AWS::NetworkManager::VpcAttachment` <!-- NOT SUPPORTED: aws_networkmanager_vpc_attachment is in aws_not_implemented.py -->

### Notifications (7 resources)

- [ ] `AWS::Notifications::ChannelAssociation` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::Notifications::EventRule` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::Notifications::ManagedNotificationAccountContactAssociation` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::Notifications::ManagedNotificationAdditionalChannelAssociation` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::Notifications::NotificationConfiguration` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::Notifications::NotificationHub` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::Notifications::OrganizationalUnitAssociation` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### NotificationsContacts (1 resources)

- [ ] `AWS::NotificationsContacts::EmailContact` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### ODB (1 resources)

- [ ] `AWS::ODB::DatabaseInstance` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### OSIS (1 resources)

- [ ] `AWS::OSIS::Pipeline` <!-- NOT SUPPORTED: aws_osis_pipeline is in aws_not_implemented.py -->

### Oam (2 resources)

- [ ] `AWS::Oam::Link` <!-- NOT SUPPORTED: aws_oam_link is in aws_not_implemented.py -->
- [ ] `AWS::Oam::Sink` <!-- NOT SUPPORTED: aws_oam_sink is in aws_not_implemented.py -->

### ObservabilityAdmin (1 resources)

- [ ] `AWS::ObservabilityAdmin::ObservabilityConfiguration` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### OpenSearchServerless (6 resources)

- [ ] `AWS::OpenSearchServerless::SecurityConfig` <!-- NOT SUPPORTED: aws_opensearchserverless_security_config is in aws_not_implemented.py -->

### OpsWorks (7 resources)

- [ ] `AWS::OpsWorks::Instance` <!-- NOT SUPPORTED: aws_opsworks_instance is in aws_not_implemented.py -->
- [ ] `AWS::OpsWorks::Stack` <!-- NOT SUPPORTED: aws_opsworks_stack is in aws_not_implemented.py -->
- [ ] `AWS::OpsWorks::UserProfile` <!-- NO IMPORT SUPPORT: aws_opsworks_user_profile - Terraform does not support importing this resource type -->

### PCAConnectorSCEP (2 resources)

- [ ] `AWS::PCAConnectorSCEP::Challenge` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::PCAConnectorSCEP::Connector` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### PCS (3 resources)

- [ ] `AWS::PCS::Cluster` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::PCS::ComputeNodeGroup` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::PCS::Queue` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### PaymentCryptography (2 resources)

- [ ] `AWS::PaymentCryptography::Key` <!-- NOT SUPPORTED: aws_paymentcryptography_key is in aws_not_implemented.py -->

### Pinpoint (19 resources)

- [ ] `AWS::Pinpoint::App` <!-- NOT SUPPORTED: aws_pinpoint_app is in aws_not_implemented.py -->
- [ ] `AWS::Pinpoint::BaiduChannel` <!-- NOT SUPPORTED: aws_pinpoint_baidu_channel is in aws_not_implemented.py -->
- [ ] `AWS::Pinpoint::EmailChannel` <!-- NOT SUPPORTED: aws_pinpoint_email_channel is in aws_not_implemented.py -->
- [ ] `AWS::Pinpoint::EmailTemplate` <!-- NOT SUPPORTED: aws_pinpoint_email_template is in aws_not_implemented.py -->
- [ ] `AWS::Pinpoint::EventStream` <!-- NOT SUPPORTED: aws_pinpoint_event_stream is in aws_not_implemented.py -->

### QBusiness (6 resources)

- [ ] `AWS::QBusiness::Application` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::QBusiness::DataSource` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::QBusiness::Index` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::QBusiness::Plugin` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::QBusiness::Retriever` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::QBusiness::WebExperience` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### QLDB (2 resources)

- [ ] `AWS::QLDB::Ledger` <!-- NO IMPORT SUPPORT: aws_qldb_ledger - Terraform does not support importing this resource type -->
- [ ] `AWS::QLDB::Stream` <!-- NO IMPORT SUPPORT: aws_qldb_stream - Terraform does not support importing this resource type -->

### RTBFabric (1 resources)

- [ ] `AWS::RTBFabric::Endpoint` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### RUM (1 resources)

- [ ] `AWS::RUM::AppMonitor` <!-- NOT SUPPORTED: aws_rum_app_monitor is in aws_not_implemented.py -->

### Rbin (1 resources)

- [ ] `AWS::Rbin::Rule` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### ResilienceHub (2 resources)

- [ ] `AWS::ResilienceHub::ResiliencyPolicy` <!-- NOT SUPPORTED: aws_resiliencehub_resiliency_policy is in aws_not_implemented.py -->

### ResourceExplorer2 (3 resources)

- [ ] `AWS::ResourceExplorer2::Index` <!-- NOT SUPPORTED: aws_resourceexplorer2_index is in aws_not_implemented.py -->

### RolesAnywhere (3 resources)

- [ ] `AWS::RolesAnywhere::Profile` <!-- NOT SUPPORTED: aws_rolesanywhere_profile is in aws_not_implemented.py -->
- [ ] `AWS::RolesAnywhere::TrustAnchor` <!-- NOT SUPPORTED: aws_rolesanywhere_trust_anchor is in aws_not_implemented.py -->

### Route53Profiles (3 resources)

- [ ] `AWS::Route53Profiles::Profile` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::Route53Profiles::ProfileAssociation` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::Route53Profiles::ProfileResourceAssociation` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### Route53RecoveryReadiness (4 resources)

- [ ] `AWS::Route53RecoveryReadiness::Cell` <!-- NO IMPORT SUPPORT: aws_route53recoveryreadiness_cell - Terraform does not support importing this resource type -->
- [ ] `AWS::Route53RecoveryReadiness::ReadinessCheck` <!-- NO IMPORT SUPPORT: aws_route53recoveryreadiness_readiness_check - Terraform does not support importing this resource type -->
- [ ] `AWS::Route53RecoveryReadiness::RecoveryGroup` <!-- NO IMPORT SUPPORT: aws_route53recoveryreadiness_recovery_group - Terraform does not support importing this resource type -->
- [ ] `AWS::Route53RecoveryReadiness::ResourceSet` <!-- NO IMPORT SUPPORT: aws_route53recoveryreadiness_resource_set - Terraform does not support importing this resource type -->

### SES (10 resources)

- [ ] `AWS::SES::ConfigurationSet` <!-- NOT SUPPORTED: aws_ses_configuration_set is in aws_not_implemented.py -->
- [ ] `AWS::SES::EmailIdentity` <!-- NOT SUPPORTED: aws_ses_email_identity is in aws_not_implemented.py -->
- [ ] `AWS::SES::ReceiptFilter` <!-- NOT SUPPORTED: aws_ses_receipt_filter is in aws_not_implemented.py -->
- [ ] `AWS::SES::Template` <!-- NOT SUPPORTED: aws_ses_template is in aws_not_implemented.py -->

### SMSVOICE (4 resources)

- [ ] `AWS::SMSVOICE::ConfigurationSet` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::SMSVOICE::OptOutList` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::SMSVOICE::PhoneNumber` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
- [ ] `AWS::SMSVOICE::Pool` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### SSM (6 resources)

- [ ] `AWS::SSM::ResourceDataSync` <!-- NOT SUPPORTED: aws_ssm_resource_data_sync is in aws_not_implemented.py -->

### SSMContacts (4 resources)

- [ ] `AWS::SSMContacts::Rotation` <!-- NOT SUPPORTED: aws_ssmcontacts_rotation is in aws_not_implemented.py -->

### SSMGuiConnect (1 resources)

- [ ] `AWS::SSMGuiConnect::Preferences` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### SSMQuickSetup (1 resources)

- [ ] `AWS::SSMQuickSetup::ConfigurationManager` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->

### SageMaker (14 resources)

- [ ] `AWS::SageMaker::DataQualityJobDefinition` <!-- NOT SUPPORTED: aws_sagemaker_data_quality_job_definition is in aws_not_implemented.py -->
- [ ] `AWS::SageMaker::Device` <!-- NOT SUPPORTED: aws_sagemaker_device is in aws_not_implemented.py -->
- [ ] `AWS::SageMaker::DeviceFleet` <!-- NOT SUPPORTED: aws_sagemaker_device_fleet is in aws_not_implemented.py -->
- [ ] `AWS::SageMaker::FeatureGroup` <!-- NOT SUPPORTED: aws_sagemaker_feature_group is in aws_not_implemented.py -->

### ServiceCatalog (15 resources)

- [ ] `AWS::ServiceCatalog::PortfolioShare` <!-- NOT SUPPORTED: aws_servicecatalog_portfolio_share is in aws_not_implemented.py -->
- [ ] `AWS::ServiceCatalog::TagOption` <!-- NOT SUPPORTED: aws_servicecatalog_tag_option is in aws_not_implemented.py -->

### ServiceCatalogAppRegistry (4 resources)

- [ ] `AWS::ServiceCatalogAppRegistry::Application` <!-- NOT SUPPORTED: aws_servicecatalogappregistry_application is in aws_not_implemented.py -->
- [ ] `AWS::ServiceCatalogAppRegistry::AttributeGroup` <!-- NOT SUPPORTED: aws_servicecatalogappregistry_attribute_group is in aws_not_implemented.py -->
- [ ] `AWS::ServiceCatalogAppRegistry::AttributeGroupAssociation` <!-- NOT SUPPORTED: aws_servicecatalogappregistry_attribute_group_association is in aws_not_implemented.py -->

### Shield (4 resources)

- [ ] `AWS::Shield::ProactiveEngagement` <!-- NOT SUPPORTED: aws_shield_proactive_engagement is in aws_not_implemented.py -->
- [ ] `AWS::Shield::Protection` <!-- NOT SUPPORTED: aws_shield_protection is in aws_not_implemented.py -->

### Synthetics (2 resources)

- [ ] `AWS::Synthetics::Canary` <!-- NOT SUPPORTED: aws_synthetics_canary is in aws_not_implemented.py -->
- [ ] `AWS::Synthetics::Group` <!-- NOT SUPPORTED: aws_synthetics_group is in aws_not_implemented.py -->

### VerifiedPermissions (4 resources)

- [ ] `AWS::VerifiedPermissions::IdentitySource` <!-- NOT SUPPORTED: aws_verifiedpermissions_identity_source is in aws_not_implemented.py -->
- [ ] `AWS::VerifiedPermissions::Policy` <!-- NOT SUPPORTED: aws_verifiedpermissions_policy is in aws_not_implemented.py -->
- [ ] `AWS::VerifiedPermissions::PolicyStore` <!-- NOT SUPPORTED: aws_verifiedpermissions_policy_store is in aws_not_implemented.py -->
- [ ] `AWS::VerifiedPermissions::PolicyTemplate` <!-- NOT SUPPORTED: aws_verifiedpermissions_policy_template is in aws_not_implemented.py -->

### WAF (7 resources)

- [ ] `AWS::WAF::ByteMatchSet` <!-- NOT SUPPORTED: aws_waf_byte_match_set is in aws_not_implemented.py -->
- [ ] `AWS::WAF::IPSet` <!-- NOT SUPPORTED: aws_waf_ipset is in aws_not_implemented.py -->
- [ ] `AWS::WAF::Rule` <!-- NOT SUPPORTED: aws_waf_rule is in aws_not_implemented.py -->
- [ ] `AWS::WAF::SizeConstraintSet` <!-- NOT SUPPORTED: aws_waf_size_constraint_set is in aws_not_implemented.py -->
- [ ] `AWS::WAF::SqlInjectionMatchSet` <!-- NOT SUPPORTED: aws_waf_sql_injection_match_set is in aws_not_implemented.py -->
- [ ] `AWS::WAF::XssMatchSet` <!-- NOT SUPPORTED: aws_waf_xss_match_set is in aws_not_implemented.py -->

### WAFRegional (11 resources)

- [ ] `AWS::WAFRegional::ByteMatchSet` <!-- NOT SUPPORTED: aws_wafregional_byte_match_set is in aws_not_implemented.py -->
- [ ] `AWS::WAFRegional::GeoMatchSet` <!-- NOT SUPPORTED: aws_wafregional_geo_match_set is in aws_not_implemented.py -->
- [ ] `AWS::WAFRegional::IPSet` <!-- NOT SUPPORTED: aws_wafregional_ipset is in aws_not_implemented.py -->
- [ ] `AWS::WAFRegional::RateBasedRule` <!-- NOT SUPPORTED: aws_wafregional_rate_based_rule is in aws_not_implemented.py -->
- [ ] `AWS::WAFRegional::RegexPatternSet` <!-- NOT SUPPORTED: aws_wafregional_regex_pattern_set is in aws_not_implemented.py -->
- [ ] `AWS::WAFRegional::Rule` <!-- NOT SUPPORTED: aws_wafregional_rule is in aws_not_implemented.py -->
- [ ] `AWS::WAFRegional::SizeConstraintSet` <!-- NOT SUPPORTED: aws_wafregional_size_constraint_set is in aws_not_implemented.py -->
- [ ] `AWS::WAFRegional::SqlInjectionMatchSet` <!-- NOT SUPPORTED: aws_wafregional_sql_injection_match_set is in aws_not_implemented.py -->
- [ ] `AWS::WAFRegional::WebACL` <!-- NOT SUPPORTED: aws_wafregional_web_acl is in aws_not_implemented.py -->
- [ ] `AWS::WAFRegional::XssMatchSet` <!-- NOT SUPPORTED: aws_wafregional_xss_match_set is in aws_not_implemented.py -->

## Notes

### NO TERRAFORM SUPPORT Resources

These resources are from AWS services that are not yet supported by the Terraform AWS provider.
They cannot be implemented in aws2tf until Terraform adds support.

**Action Required:** Monitor Terraform AWS provider releases for new resource support.

### NOT SUPPORTED Resources

These resources have Terraform support but are marked as not implemented in aws2tf.
They are listed in `code/fixtf_aws_resources/aws_not_implemented.py`.

**Action Required:** Follow the standard resource testing procedure to implement these resources.

### NO IMPORT SUPPORT Resources

These resources can be created by Terraform but cannot be imported from existing infrastructure.
They are listed in `code/fixtf_aws_resources/aws_no_import.py`.

**Action Required:** These resources cannot be imported via aws2tf. They can only be managed if created by Terraform.