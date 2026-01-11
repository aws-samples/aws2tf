# CloudFormation Stack Resources - To Test

This file lists all CloudFormation resource types in `code/stacks.py` that currently have placeholder entries using `common.call_resource("aws_null", ...)`. These resources are recognized but not yet fully implemented.

**Total Resources:** 1022
**Services:** 252

## Purpose

These placeholder entries allow aws2tf to:
1. Recognize the resource type when importing CloudFormation stacks
2. Log the resource to `stack-fetched-explicit.log`
3. Avoid "UNPROCESSED" errors

To fully implement any of these resources, follow the stack resource testing procedure in `.kiro/steering/stack-resource-testing.md`.


**Total Resources:** 786
**Services:** 193

## Resources by Service

### ACMPCA (1 resources)

- [ ] `AWS::ACMPCA::CertificateAuthorityActivation` <!-- READY: aws_acmpca_certificate_authority_activation can be implemented in aws2tf -->

### APS (2 resources)

- [ ] `AWS::APS::RuleGroupsNamespace` <!-- READY: aws_aps_rule_groups_namespace can be implemented in aws2tf -->
- [ ] `AWS::APS::Workspace` <!-- READY: aws_aps_workspace can be implemented in aws2tf -->

### ARCZonalShift (1 resources)

- [ ] `AWS::ARCZonalShift::ZonalAutoshiftConfiguration` <!-- READY: aws_arczonalshift_zonal_autoshift_configuration can be implemented in aws2tf -->

### AmazonMQ (1 resources)

- [ ] `AWS::AmazonMQ::ConfigurationAssociation` <!-- READY: aws_amazonmq_configuration_association can be implemented in aws2tf -->

### Amplify (1 resources)

- [ ] `AWS::Amplify::Domain` <!-- READY: aws_amplify_domain can be implemented in aws2tf -->

### AmplifyUIBuilder (3 resources)

- [ ] `AWS::AmplifyUIBuilder::Component` <!-- READY: aws_amplifyuibuilder_component can be implemented in aws2tf -->
- [ ] `AWS::AmplifyUIBuilder::Form` <!-- READY: aws_amplifyuibuilder_form can be implemented in aws2tf -->
- [ ] `AWS::AmplifyUIBuilder::Theme` <!-- READY: aws_amplifyuibuilder_theme can be implemented in aws2tf -->

### ApiGateway (2 resources)

- [ ] `AWS::ApiGateway::DocumentationPart` <!-- READY: aws_apigateway_documentation_part can be implemented in aws2tf -->
- [ ] `AWS::ApiGateway::DocumentationVersion` <!-- READY: aws_apigateway_documentation_version can be implemented in aws2tf -->

### ApiGatewayV2 (1 resources)

- [ ] `AWS::ApiGatewayV2::ApiGatewayManagedOverrides` <!-- READY: aws_apigatewayv2_api_gateway_managed_overrides can be implemented in aws2tf -->

### AppConfig (8 resources)

- [ ] `AWS::AppConfig::Application` <!-- READY: aws_appconfig_application can be implemented in aws2tf -->
- [ ] `AWS::AppConfig::ConfigurationProfile` <!-- READY: aws_appconfig_configuration_profile can be implemented in aws2tf -->
- [ ] `AWS::AppConfig::Deployment` <!-- READY: aws_appconfig_deployment can be implemented in aws2tf -->
- [ ] `AWS::AppConfig::DeploymentStrategy` <!-- READY: aws_appconfig_deployment_strategy can be implemented in aws2tf -->
- [ ] `AWS::AppConfig::Environment` <!-- READY: aws_appconfig_environment can be implemented in aws2tf -->
- [ ] `AWS::AppConfig::Extension` <!-- READY: aws_appconfig_extension can be implemented in aws2tf -->
- [ ] `AWS::AppConfig::ExtensionAssociation` <!-- READY: aws_appconfig_extension_association can be implemented in aws2tf -->
- [ ] `AWS::AppConfig::HostedConfigurationVersion` <!-- READY: aws_appconfig_hosted_configuration_version can be implemented in aws2tf -->

### AppFlow (3 resources)

- [ ] `AWS::AppFlow::Connector` <!-- READY: aws_appflow_connector can be implemented in aws2tf -->
- [ ] `AWS::AppFlow::ConnectorProfile` <!-- READY: aws_appflow_connector_profile can be implemented in aws2tf -->
- [ ] `AWS::AppFlow::Flow` <!-- READY: aws_appflow_flow can be implemented in aws2tf -->

### AppRunner (5 resources)

- [ ] `AWS::AppRunner::AutoScalingConfiguration` <!-- READY: aws_apprunner_auto_scaling_configuration can be implemented in aws2tf -->
- [ ] `AWS::AppRunner::Service` <!-- READY: aws_apprunner_service can be implemented in aws2tf -->
- [ ] `AWS::AppRunner::VpcConnector` <!-- READY: aws_apprunner_vpc_connector can be implemented in aws2tf -->
- [ ] `AWS::AppRunner::VpcIngressConnection` <!-- READY: aws_apprunner_vpc_ingress_connection can be implemented in aws2tf -->

### AppStream (13 resources)

- [ ] `AWS::AppStream::AppBlock` <!-- READY: aws_appstream_app_block can be implemented in aws2tf -->
- [ ] `AWS::AppStream::AppBlockBuilder` <!-- READY: aws_appstream_app_block_builder can be implemented in aws2tf -->
- [ ] `AWS::AppStream::Application` <!-- READY: aws_appstream_application can be implemented in aws2tf -->
- [ ] `AWS::AppStream::ApplicationEntitlementAssociation` <!-- READY: aws_appstream_application_entitlement_association can be implemented in aws2tf -->
- [ ] `AWS::AppStream::ApplicationFleetAssociation` <!-- READY: aws_appstream_application_fleet_association can be implemented in aws2tf -->
- [ ] `AWS::AppStream::Entitlement` <!-- READY: aws_appstream_entitlement can be implemented in aws2tf -->
- [ ] `AWS::AppStream::Fleet` <!-- READY: aws_appstream_fleet can be implemented in aws2tf -->
- [ ] `AWS::AppStream::ImageBuilder` <!-- READY: aws_appstream_image_builder can be implemented in aws2tf -->
- [ ] `AWS::AppStream::Stack` <!-- READY: aws_appstream_stack can be implemented in aws2tf -->
- [ ] `AWS::AppStream::StackFleetAssociation` <!-- READY: aws_appstream_stack_fleet_association can be implemented in aws2tf -->
- [ ] `AWS::AppStream::StackUserAssociation` <!-- READY: aws_appstream_stack_user_association can be implemented in aws2tf -->
- [ ] `AWS::AppStream::User` <!-- READY: aws_appstream_user can be implemented in aws2tf -->

### AppSync (10 resources)

- [ ] `AWS::AppSync::ApiKey` <!-- READY: aws_appsync_api_key can be implemented in aws2tf -->
- [ ] `AWS::AppSync::DataSource` <!-- READY: aws_appsync_data_source can be implemented in aws2tf -->
- [ ] `AWS::AppSync::DomainName` <!-- READY: aws_appsync_domain_name can be implemented in aws2tf -->
- [ ] `AWS::AppSync::FunctionConfiguration` <!-- READY: aws_appsync_function_configuration can be implemented in aws2tf -->
- [ ] `AWS::AppSync::GraphQLApi` <!-- READY: aws_appsync_graph_qlapi can be implemented in aws2tf -->
- [ ] `AWS::AppSync::GraphQLSchema` <!-- READY: aws_appsync_graph_qlschema can be implemented in aws2tf -->
- [ ] `AWS::AppSync::Resolver` <!-- READY: aws_appsync_resolver can be implemented in aws2tf -->
- [ ] `AWS::AppSync::SourceApiAssociation` <!-- READY: aws_appsync_source_api_association can be implemented in aws2tf -->

### ApplicationInsights (1 resources)

- [ ] `AWS::ApplicationInsights::Application` <!-- READY: aws_applicationinsights_application can be implemented in aws2tf -->

### Athena (1 resources)

- [ ] `AWS::Athena::CapacityReservation` <!-- READY: aws_athena_capacity_reservation can be implemented in aws2tf -->

### AutoScaling (3 resources)

- [ ] `AWS::AutoScaling::ScalingPolicy` <!-- READY: aws_autoscaling_scaling_policy can be implemented in aws2tf -->
- [ ] `AWS::AutoScaling::ScheduledAction` <!-- READY: aws_autoscaling_scheduled_action can be implemented in aws2tf -->
- [ ] `AWS::AutoScaling::WarmPool` <!-- READY: aws_autoscaling_warm_pool can be implemented in aws2tf -->

### AutoScalingPlans (1 resources)

- [ ] `AWS::AutoScalingPlans::ScalingPlan` <!-- READY: aws_autoscalingplans_scaling_plan can be implemented in aws2tf -->

### B2BI (4 resources)

- [ ] `AWS::B2BI::Capability` <!-- READY: aws_b2bi_capability can be implemented in aws2tf -->
- [ ] `AWS::B2BI::Partnership` <!-- READY: aws_b2bi_partnership can be implemented in aws2tf -->
- [ ] `AWS::B2BI::Profile` <!-- READY: aws_b2bi_profile can be implemented in aws2tf -->
- [ ] `AWS::B2BI::Transformer` <!-- READY: aws_b2bi_transformer can be implemented in aws2tf -->

### Backup (7 resources)

- [ ] `AWS::Backup::BackupPlan` <!-- READY: aws_backup_backup_plan can be implemented in aws2tf -->
- [ ] `AWS::Backup::BackupSelection` <!-- READY: aws_backup_backup_selection can be implemented in aws2tf -->
- [ ] `AWS::Backup::BackupVault` <!-- READY: aws_backup_backup_vault can be implemented in aws2tf -->
- [ ] `AWS::Backup::ReportPlan` <!-- READY: aws_backup_report_plan can be implemented in aws2tf -->
- [ ] `AWS::Backup::RestoreTestingPlan` <!-- READY: aws_backup_restore_testing_plan can be implemented in aws2tf -->
- [ ] `AWS::Backup::RestoreTestingSelection` <!-- READY: aws_backup_restore_testing_selection can be implemented in aws2tf -->

### BackupGateway (1 resources)

- [ ] `AWS::BackupGateway::Hypervisor` <!-- READY: aws_backupgateway_hypervisor can be implemented in aws2tf -->

### Batch (4 resources)

- [ ] `AWS::Batch::ComputeEnvironment` <!-- READY: aws_batch_compute_environment can be implemented in aws2tf -->
- [ ] `AWS::Batch::JobDefinition` <!-- READY: aws_batch_job_definition can be implemented in aws2tf -->
- [ ] `AWS::Batch::JobQueue` <!-- READY: aws_batch_job_queue can be implemented in aws2tf -->
- [ ] `AWS::Batch::SchedulingPolicy` <!-- READY: aws_batch_scheduling_policy can be implemented in aws2tf -->

### Bedrock (10 resources)

- [ ] `AWS::Bedrock::Agent` <!-- READY: aws_bedrock_agent can be implemented in aws2tf -->
- [ ] `AWS::Bedrock::AgentAlias` <!-- READY: aws_bedrock_agent_alias can be implemented in aws2tf -->
- [ ] `AWS::Bedrock::DataSource` <!-- READY: aws_bedrock_data_source can be implemented in aws2tf -->
- [ ] `AWS::Bedrock::FlowAlias` <!-- READY: aws_bedrock_flow_alias can be implemented in aws2tf -->
- [ ] `AWS::Bedrock::FlowVersion` <!-- READY: aws_bedrock_flow_version can be implemented in aws2tf -->
- [ ] `AWS::Bedrock::Guardrail` <!-- READY: aws_bedrock_guardrail can be implemented in aws2tf -->
- [ ] `AWS::Bedrock::GuardrailVersion` <!-- READY: aws_bedrock_guardrail_version can be implemented in aws2tf -->
- [ ] `AWS::Bedrock::KnowledgeBase` <!-- READY: aws_bedrock_knowledge_base can be implemented in aws2tf -->
- [ ] `AWS::Bedrock::Prompt` <!-- READY: aws_bedrock_prompt can be implemented in aws2tf -->
- [ ] `AWS::Bedrock::PromptVersion` <!-- READY: aws_bedrock_prompt_version can be implemented in aws2tf -->

### BillingConductor (4 resources)

- [ ] `AWS::BillingConductor::BillingGroup` <!-- READY: aws_billingconductor_billing_group can be implemented in aws2tf -->
- [ ] `AWS::BillingConductor::CustomLineItem` <!-- READY: aws_billingconductor_custom_line_item can be implemented in aws2tf -->
- [ ] `AWS::BillingConductor::PricingPlan` <!-- READY: aws_billingconductor_pricing_plan can be implemented in aws2tf -->
- [ ] `AWS::BillingConductor::PricingRule` <!-- READY: aws_billingconductor_pricing_rule can be implemented in aws2tf -->

### Budgets (2 resources)

- [ ] `AWS::Budgets::BudgetsAction` <!-- READY: aws_budgets_budgets_action can be implemented in aws2tf -->

### Cassandra (2 resources)

- [ ] `AWS::Cassandra::Keyspace` <!-- READY: aws_cassandra_keyspace can be implemented in aws2tf -->
- [ ] `AWS::Cassandra::Table` <!-- READY: aws_cassandra_table can be implemented in aws2tf -->

### CertificateManager (1 resources)

- [ ] `AWS::CertificateManager::Account` <!-- READY: aws_certificatemanager_account can be implemented in aws2tf -->

### Chatbot (2 resources)

- [ ] `AWS::Chatbot::MicrosoftTeamsChannelConfiguration` <!-- READY: aws_chatbot_microsoft_teams_channel_configuration can be implemented in aws2tf -->
- [ ] `AWS::Chatbot::SlackChannelConfiguration` <!-- READY: aws_chatbot_slack_channel_configuration can be implemented in aws2tf -->

### CleanRooms (5 resources)

- [ ] `AWS::CleanRooms::AnalysisTemplate` <!-- READY: aws_cleanrooms_analysis_template can be implemented in aws2tf -->
- [ ] `AWS::CleanRooms::ConfiguredTable` <!-- READY: aws_cleanrooms_configured_table can be implemented in aws2tf -->
- [ ] `AWS::CleanRooms::ConfiguredTableAssociation` <!-- READY: aws_cleanrooms_configured_table_association can be implemented in aws2tf -->
- [ ] `AWS::CleanRooms::Membership` <!-- READY: aws_cleanrooms_membership can be implemented in aws2tf -->

### CloudFormation (13 resources)

- [ ] `AWS::CloudFormation::HookDefaultVersion` <!-- READY: aws_cloudformation_hook_default_version can be implemented in aws2tf -->
- [ ] `AWS::CloudFormation::HookTypeConfig` <!-- READY: aws_cloudformation_hook_type_config can be implemented in aws2tf -->
- [ ] `AWS::CloudFormation::HookVersion` <!-- READY: aws_cloudformation_hook_version can be implemented in aws2tf -->
- [ ] `AWS::CloudFormation::Macro` <!-- READY: aws_cloudformation_macro can be implemented in aws2tf -->
- [ ] `AWS::CloudFormation::ModuleDefaultVersion` <!-- READY: aws_cloudformation_module_default_version can be implemented in aws2tf -->
- [ ] `AWS::CloudFormation::ModuleVersion` <!-- READY: aws_cloudformation_module_version can be implemented in aws2tf -->
- [ ] `AWS::CloudFormation::PublicTypeVersion` <!-- READY: aws_cloudformation_public_type_version can be implemented in aws2tf -->
- [ ] `AWS::CloudFormation::Publisher` <!-- READY: aws_cloudformation_publisher can be implemented in aws2tf -->
- [ ] `AWS::CloudFormation::ResourceDefaultVersion` <!-- READY: aws_cloudformation_resource_default_version can be implemented in aws2tf -->
- [ ] `AWS::CloudFormation::ResourceVersion` <!-- READY: aws_cloudformation_resource_version can be implemented in aws2tf -->
- [ ] `AWS::CloudFormation::StackSet` <!-- READY: aws_cloudformation_stack_set can be implemented in aws2tf -->
- [ ] `AWS::CloudFormation::TypeActivation` <!-- READY: aws_cloudformation_type_activation can be implemented in aws2tf -->
- [ ] `AWS::CloudFormation::WaitConditionHandle` <!-- READY: aws_cloudformation_wait_condition_handle can be implemented in aws2tf -->

### CloudFront (9 resources)

- [ ] `AWS::CloudFront::ContinuousDeploymentPolicy` <!-- READY: aws_cloudfront_continuous_deployment_policy can be implemented in aws2tf -->
- [ ] `AWS::CloudFront::KeyGroup` <!-- READY: aws_cloudfront_key_group can be implemented in aws2tf -->
- [ ] `AWS::CloudFront::KeyValueStore` <!-- READY: aws_cloudfront_key_value_store can be implemented in aws2tf -->
- [ ] `AWS::CloudFront::OriginAccessControl` <!-- READY: aws_cloudfront_origin_access_control can be implemented in aws2tf -->
- [ ] `AWS::CloudFront::PublicKey` <!-- READY: aws_cloudfront_public_key can be implemented in aws2tf -->
- [ ] `AWS::CloudFront::RealtimeLogConfig` <!-- READY: aws_cloudfront_realtime_log_config can be implemented in aws2tf -->
- [ ] `AWS::CloudFront::StreamingDistribution` <!-- READY: aws_cloudfront_streaming_distribution can be implemented in aws2tf -->

### CloudTrail (4 resources)

- [ ] `AWS::CloudTrail::Channel` <!-- READY: aws_cloudtrail_channel can be implemented in aws2tf -->
- [ ] `AWS::CloudTrail::EventDataStore` <!-- READY: aws_cloudtrail_event_data_store can be implemented in aws2tf -->
- [ ] `AWS::CloudTrail::ResourcePolicy` <!-- READY: aws_cloudtrail_resource_policy can be implemented in aws2tf -->
- [ ] `AWS::CloudTrail::Trail` <!-- READY: aws_cloudtrail_trail can be implemented in aws2tf -->

### CloudWatch (5 resources)

- [ ] `AWS::CloudWatch::AnomalyDetector` <!-- READY: aws_cloudwatch_anomaly_detector can be implemented in aws2tf -->
- [ ] `AWS::CloudWatch::CompositeAlarm` <!-- READY: aws_cloudwatch_composite_alarm can be implemented in aws2tf -->
- [x] `AWS::CloudWatch::Dashboard` <!-- COMPLETED: Test Successful -->
- [ ] `AWS::CloudWatch::InsightRule` <!-- READY: aws_cloudwatch_insight_rule can be implemented in aws2tf -->
- [ ] `AWS::CloudWatch::MetricStream` <!-- READY: aws_cloudwatch_metric_stream can be implemented in aws2tf -->

### CodeArtifact (2 resources)

- [ ] `AWS::CodeArtifact::Domain` <!-- READY: aws_codeartifact_domain can be implemented in aws2tf -->
- [ ] `AWS::CodeArtifact::Repository` <!-- READY: aws_codeartifact_repository can be implemented in aws2tf -->

### CodeBuild (2 resources)

- [ ] `AWS::CodeBuild::ReportGroup` <!-- READY: aws_codebuild_report_group can be implemented in aws2tf -->

### CodeDeploy (3 resources)

- [ ] `AWS::CodeDeploy::Application` <!-- READY: aws_codedeploy_application can be implemented in aws2tf -->
- [ ] `AWS::CodeDeploy::DeploymentConfig` <!-- READY: aws_codedeploy_deployment_config can be implemented in aws2tf -->
- [ ] `AWS::CodeDeploy::DeploymentGroup` <!-- READY: aws_codedeploy_deployment_group can be implemented in aws2tf -->

### CodeGuruProfiler (1 resources)

- [ ] `AWS::CodeGuruProfiler::ProfilingGroup` <!-- READY: aws_codeguruprofiler_profiling_group can be implemented in aws2tf -->

### CodePipeline (3 resources)

- [ ] `AWS::CodePipeline::CustomActionType` <!-- READY: aws_codepipeline_custom_action_type can be implemented in aws2tf -->
- [ ] `AWS::CodePipeline::Pipeline` <!-- READY: aws_codepipeline_pipeline can be implemented in aws2tf -->
- [ ] `AWS::CodePipeline::Webhook` <!-- READY: aws_codepipeline_webhook can be implemented in aws2tf -->

### CodeStar (1 resources)

- [ ] `AWS::CodeStar::GitHubRepository` <!-- READY: aws_codestar_git_hub_repository can be implemented in aws2tf -->

### CodeStarConnections (3 resources)

- [ ] `AWS::CodeStarConnections::Connection` <!-- READY: aws_codestarconnections_connection can be implemented in aws2tf -->
- [ ] `AWS::CodeStarConnections::RepositoryLink` <!-- READY: aws_codestarconnections_repository_link can be implemented in aws2tf -->
- [ ] `AWS::CodeStarConnections::SyncConfiguration` <!-- READY: aws_codestarconnections_sync_configuration can be implemented in aws2tf -->

### CodeStarNotifications (1 resources)

- [ ] `AWS::CodeStarNotifications::NotificationRule` <!-- READY: aws_codestarnotifications_notification_rule can be implemented in aws2tf -->

### Cognito (11 resources)

- [ ] `AWS::Cognito::IdentityPool` <!-- READY: aws_cognito_identity_pool can be implemented in aws2tf -->
- [ ] `AWS::Cognito::IdentityPoolPrincipalTag` <!-- READY: aws_cognito_identity_pool_principal_tag can be implemented in aws2tf -->
- [ ] `AWS::Cognito::IdentityPoolRoleAttachment` <!-- READY: aws_cognito_identity_pool_role_attachment can be implemented in aws2tf -->
- [ ] `AWS::Cognito::LogDeliveryConfiguration` <!-- READY: aws_cognito_log_delivery_configuration can be implemented in aws2tf -->
- [ ] `AWS::Cognito::UserPoolIdentityProvider` <!-- READY: aws_cognito_user_pool_identity_provider can be implemented in aws2tf -->
- [ ] `AWS::Cognito::UserPoolResourceServer` <!-- READY: aws_cognito_user_pool_resource_server can be implemented in aws2tf -->
- [ ] `AWS::Cognito::UserPoolRiskConfigurationAttachment` <!-- READY: aws_cognito_user_pool_risk_configuration_attachment can be implemented in aws2tf -->
- [ ] `AWS::Cognito::UserPoolUICustomizationAttachment` <!-- READY: aws_cognito_user_pool_uicustomization_attachment can be implemented in aws2tf -->
- [ ] `AWS::Cognito::UserPoolUser` <!-- READY: aws_cognito_user_pool_user can be implemented in aws2tf -->
- [ ] `AWS::Cognito::UserPoolUserToGroupAttachment` <!-- READY: aws_cognito_user_pool_user_to_group_attachment can be implemented in aws2tf -->

### Comprehend (2 resources)

- [ ] `AWS::Comprehend::Flywheel` <!-- READY: aws_comprehend_flywheel can be implemented in aws2tf -->

### Config (7 resources)

- [ ] `AWS::Config::AggregationAuthorization` <!-- READY: aws_config_aggregation_authorization can be implemented in aws2tf -->
- [ ] `AWS::Config::ConfigurationAggregator` <!-- READY: aws_config_configuration_aggregator can be implemented in aws2tf -->
- [ ] `AWS::Config::OrganizationConfigRule` <!-- READY: aws_config_organization_config_rule can be implemented in aws2tf -->
- [ ] `AWS::Config::OrganizationConformancePack` <!-- READY: aws_config_organization_conformance_pack can be implemented in aws2tf -->
- [ ] `AWS::Config::RemediationConfiguration` <!-- READY: aws_config_remediation_configuration can be implemented in aws2tf -->
- [ ] `AWS::Config::StoredQuery` <!-- READY: aws_config_stored_query can be implemented in aws2tf -->

### Connect (13 resources)

- [ ] `AWS::Connect::ApprovedOrigin` <!-- READY: aws_connect_approved_origin can be implemented in aws2tf -->
- [ ] `AWS::Connect::EvaluationForm` <!-- READY: aws_connect_evaluation_form can be implemented in aws2tf -->
- [ ] `AWS::Connect::PredefinedAttribute` <!-- READY: aws_connect_predefined_attribute can be implemented in aws2tf -->
- [ ] `AWS::Connect::Prompt` <!-- READY: aws_connect_prompt can be implemented in aws2tf -->
- [ ] `AWS::Connect::QuickConnect` <!-- READY: aws_connect_quick_connect can be implemented in aws2tf -->
- [ ] `AWS::Connect::Rule` <!-- READY: aws_connect_rule can be implemented in aws2tf -->
- [ ] `AWS::Connect::SecurityKey` <!-- READY: aws_connect_security_key can be implemented in aws2tf -->
- [ ] `AWS::Connect::TaskTemplate` <!-- READY: aws_connect_task_template can be implemented in aws2tf -->
- [ ] `AWS::Connect::TrafficDistributionGroup` <!-- READY: aws_connect_traffic_distribution_group can be implemented in aws2tf -->
- [ ] `AWS::Connect::View` <!-- READY: aws_connect_view can be implemented in aws2tf -->
- [ ] `AWS::Connect::ViewVersion` <!-- READY: aws_connect_view_version can be implemented in aws2tf -->

### ConnectCampaigns (1 resources)

- [ ] `AWS::ConnectCampaigns::Campaign` <!-- READY: aws_connectcampaigns_campaign can be implemented in aws2tf -->

### ControlTower (2 resources)

- [ ] `AWS::ControlTower::EnabledControl` <!-- READY: aws_controltower_enabled_control can be implemented in aws2tf -->
- [ ] `AWS::ControlTower::LandingZone` <!-- READY: aws_controltower_landing_zone can be implemented in aws2tf -->

### CustomerProfiles (5 resources)

- [ ] `AWS::CustomerProfiles::CalculatedAttributeDefinition` <!-- READY: aws_customerprofiles_calculated_attribute_definition can be implemented in aws2tf -->
- [ ] `AWS::CustomerProfiles::Domain` <!-- READY: aws_customerprofiles_domain can be implemented in aws2tf -->
- [ ] `AWS::CustomerProfiles::EventStream` <!-- READY: aws_customerprofiles_event_stream can be implemented in aws2tf -->
- [ ] `AWS::CustomerProfiles::Integration` <!-- READY: aws_customerprofiles_integration can be implemented in aws2tf -->
- [ ] `AWS::CustomerProfiles::ObjectType` <!-- READY: aws_customerprofiles_object_type can be implemented in aws2tf -->

### DMS (8 resources)

- [ ] `AWS::DMS::Certificate` <!-- READY: aws_dms_certificate can be implemented in aws2tf -->
- [ ] `AWS::DMS::DataProvider` <!-- READY: aws_dms_data_provider can be implemented in aws2tf -->
- [ ] `AWS::DMS::Endpoint` <!-- READY: aws_dms_endpoint can be implemented in aws2tf -->
- [ ] `AWS::DMS::EventSubscription` <!-- READY: aws_dms_event_subscription can be implemented in aws2tf -->
- [ ] `AWS::DMS::InstanceProfile` <!-- READY: aws_dms_instance_profile can be implemented in aws2tf -->
- [ ] `AWS::DMS::MigrationProject` <!-- READY: aws_dms_migration_project can be implemented in aws2tf -->
- [ ] `AWS::DMS::ReplicationConfig` <!-- READY: aws_dms_replication_config can be implemented in aws2tf -->
- [ ] `AWS::DMS::ReplicationTask` <!-- READY: aws_dms_replication_task can be implemented in aws2tf -->

### DataBrew (6 resources)

- [ ] `AWS::DataBrew::Dataset` <!-- READY: aws_databrew_dataset can be implemented in aws2tf -->
- [ ] `AWS::DataBrew::Job` <!-- READY: aws_databrew_job can be implemented in aws2tf -->
- [ ] `AWS::DataBrew::Project` <!-- READY: aws_databrew_project can be implemented in aws2tf -->
- [ ] `AWS::DataBrew::Recipe` <!-- READY: aws_databrew_recipe can be implemented in aws2tf -->
- [ ] `AWS::DataBrew::Ruleset` <!-- READY: aws_databrew_ruleset can be implemented in aws2tf -->
- [ ] `AWS::DataBrew::Schedule` <!-- READY: aws_databrew_schedule can be implemented in aws2tf -->

### DataSync (14 resources)

- [ ] `AWS::DataSync::Agent` <!-- READY: aws_datasync_agent can be implemented in aws2tf -->
- [ ] `AWS::DataSync::LocationFSxLustre` <!-- READY: aws_datasync_location_fsx_lustre can be implemented in aws2tf -->
- [ ] `AWS::DataSync::LocationFSxONTAP` <!-- READY: aws_datasync_location_fsx_ontap can be implemented in aws2tf -->
- [ ] `AWS::DataSync::LocationFSxOpenZFS` <!-- READY: aws_datasync_location_fsx_open_zfs can be implemented in aws2tf -->
- [ ] `AWS::DataSync::LocationFSxWindows` <!-- READY: aws_datasync_location_fsx_windows can be implemented in aws2tf -->
- [ ] `AWS::DataSync::StorageSystem` <!-- READY: aws_datasync_storage_system can be implemented in aws2tf -->
- [ ] `AWS::DataSync::Task` <!-- READY: aws_datasync_task can be implemented in aws2tf -->

### Detective (3 resources)

- [ ] `AWS::Detective::Graph` <!-- READY: aws_detective_graph can be implemented in aws2tf -->
- [ ] `AWS::Detective::MemberInvitation` <!-- READY: aws_detective_member_invitation can be implemented in aws2tf -->
- [ ] `AWS::Detective::OrganizationAdmin` <!-- READY: aws_detective_organization_admin can be implemented in aws2tf -->

### DevOpsGuru (3 resources)

- [ ] `AWS::DevOpsGuru::LogAnomalyDetectionIntegration` <!-- READY: aws_devopsguru_log_anomaly_detection_integration can be implemented in aws2tf -->
- [ ] `AWS::DevOpsGuru::NotificationChannel` <!-- READY: aws_devopsguru_notification_channel can be implemented in aws2tf -->
- [ ] `AWS::DevOpsGuru::ResourceCollection` <!-- READY: aws_devopsguru_resource_collection can be implemented in aws2tf -->

### DeviceFarm (6 resources)

- [ ] `AWS::DeviceFarm::VPCEConfiguration` <!-- READY: aws_devicefarm_vpceconfiguration can be implemented in aws2tf -->

### DirectoryService (1 resources)

- [ ] `AWS::DirectoryService::SimpleAD` <!-- READY: aws_directoryservice_simple_ad can be implemented in aws2tf -->

### DocDB (2 resources)

- [ ] `AWS::DocDB::DBClusterParameterGroup` <!-- READY: aws_docdb_dbcluster_parameter_group can be implemented in aws2tf -->
- [ ] `AWS::DocDB::EventSubscription` <!-- READY: aws_docdb_event_subscription can be implemented in aws2tf -->

### EC2 (67 resources)

- [ ] `AWS::EC2::CapacityReservation` <!-- READY: aws_ec2_capacity_reservation can be implemented in aws2tf -->
- [ ] `AWS::EC2::CapacityReservationFleet` <!-- READY: aws_ec2_capacity_reservation_fleet can be implemented in aws2tf -->
- [ ] `AWS::EC2::CarrierGateway` <!-- READY: aws_ec2_carrier_gateway can be implemented in aws2tf -->
- [ ] `AWS::EC2::ClientVpnAuthorizationRule` <!-- READY: aws_ec2_client_vpn_authorization_rule can be implemented in aws2tf -->
- [ ] `AWS::EC2::ClientVpnEndpoint` <!-- READY: aws_ec2_client_vpn_endpoint can be implemented in aws2tf -->
- [ ] `AWS::EC2::ClientVpnRoute` <!-- READY: aws_ec2_client_vpn_route can be implemented in aws2tf -->
- [ ] `AWS::EC2::ClientVpnTargetNetworkAssociation` <!-- READY: aws_ec2_client_vpn_target_network_association can be implemented in aws2tf -->
- [ ] `AWS::EC2::CustomerGateway` <!-- READY: aws_ec2_customer_gateway can be implemented in aws2tf -->
- [ ] `AWS::EC2::EC2Fleet` <!-- READY: aws_ec2_ec2_fleet can be implemented in aws2tf -->
- [ ] `AWS::EC2::EgressOnlyInternetGateway` <!-- READY: aws_ec2_egress_only_internet_gateway can be implemented in aws2tf -->
- [ ] `AWS::EC2::EnclaveCertificateIamRoleAssociation` <!-- READY: aws_ec2_enclave_certificate_iam_role_association can be implemented in aws2tf -->
- [ ] `AWS::EC2::Host` <!-- READY: aws_ec2_host can be implemented in aws2tf -->
- [ ] `AWS::EC2::IPAM` <!-- READY: aws_ec2_ipam can be implemented in aws2tf -->
- [ ] `AWS::EC2::IPAMAllocation` <!-- READY: aws_ec2_ipamallocation can be implemented in aws2tf -->
- [ ] `AWS::EC2::IPAMPool` <!-- READY: aws_ec2_ipampool can be implemented in aws2tf -->
- [ ] `AWS::EC2::IPAMPoolCidr` <!-- READY: aws_ec2_ipampool_cidr can be implemented in aws2tf -->
- [ ] `AWS::EC2::IPAMResourceDiscovery` <!-- READY: aws_ec2_ipamresource_discovery can be implemented in aws2tf -->
- [ ] `AWS::EC2::IPAMResourceDiscoveryAssociation` <!-- READY: aws_ec2_ipamresource_discovery_association can be implemented in aws2tf -->
- [ ] `AWS::EC2::IPAMScope` <!-- READY: aws_ec2_ipamscope can be implemented in aws2tf -->
- [ ] `AWS::EC2::InstanceConnectEndpoint` <!-- READY: aws_ec2_instance_connect_endpoint can be implemented in aws2tf -->
- [ ] `AWS::EC2::LocalGatewayRouteTable` <!-- READY: aws_ec2_local_gateway_route_table can be implemented in aws2tf -->
- [ ] `AWS::EC2::LocalGatewayRouteTableVPCAssociation` <!-- READY: aws_ec2_local_gateway_route_table_vpcassociation can be implemented in aws2tf -->
- [ ] `AWS::EC2::LocalGatewayRouteTableVirtualInterfaceGroupAssociation` <!-- READY: aws_ec2_local_gateway_route_table_virtual_interface_group_association can be implemented in aws2tf -->
- [ ] `AWS::EC2::NetworkInsightsAccessScope` <!-- READY: aws_ec2_network_insights_access_scope can be implemented in aws2tf -->
- [ ] `AWS::EC2::NetworkInsightsAccessScopeAnalysis` <!-- READY: aws_ec2_network_insights_access_scope_analysis can be implemented in aws2tf -->
- [ ] `AWS::EC2::NetworkInsightsAnalysis` <!-- READY: aws_ec2_network_insights_analysis can be implemented in aws2tf -->
- [ ] `AWS::EC2::NetworkInsightsPath` <!-- READY: aws_ec2_network_insights_path can be implemented in aws2tf -->
- [ ] `AWS::EC2::NetworkInterface` <!-- READY: aws_ec2_network_interface can be implemented in aws2tf -->
- [ ] `AWS::EC2::NetworkInterfaceAttachment` <!-- READY: aws_ec2_network_interface_attachment can be implemented in aws2tf -->
- [ ] `AWS::EC2::NetworkInterfacePermission` <!-- READY: aws_ec2_network_interface_permission can be implemented in aws2tf -->
- [ ] `AWS::EC2::NetworkPerformanceMetricSubscription` <!-- READY: aws_ec2_network_performance_metric_subscription can be implemented in aws2tf -->
- [ ] `AWS::EC2::PlacementGroup` <!-- READY: aws_ec2_placement_group can be implemented in aws2tf -->
- [ ] `AWS::EC2::PrefixList` <!-- READY: aws_ec2_prefix_list can be implemented in aws2tf -->
- [ ] `AWS::EC2::SnapshotBlockPublicAccess` <!-- READY: aws_ec2_snapshot_block_public_access can be implemented in aws2tf -->
- [ ] `AWS::EC2::SpotFleet` <!-- READY: aws_ec2_spot_fleet can be implemented in aws2tf -->
- [ ] `AWS::EC2::SubnetCidrBlock` <!-- READY: aws_ec2_subnet_cidr_block can be implemented in aws2tf -->
- [ ] `AWS::EC2::TrafficMirrorFilter` <!-- READY: aws_ec2_traffic_mirror_filter can be implemented in aws2tf -->
- [ ] `AWS::EC2::TrafficMirrorFilterRule` <!-- READY: aws_ec2_traffic_mirror_filter_rule can be implemented in aws2tf -->
- [ ] `AWS::EC2::TrafficMirrorSession` <!-- READY: aws_ec2_traffic_mirror_session can be implemented in aws2tf -->
- [ ] `AWS::EC2::TrafficMirrorTarget` <!-- READY: aws_ec2_traffic_mirror_target can be implemented in aws2tf -->
- [ ] `AWS::EC2::TransitGateway` <!-- READY: aws_ec2_transit_gateway can be implemented in aws2tf -->
- [ ] `AWS::EC2::TransitGatewayAttachment` <!-- READY: aws_ec2_transit_gateway_attachment can be implemented in aws2tf -->
- [ ] `AWS::EC2::TransitGatewayConnect` <!-- READY: aws_ec2_transit_gateway_connect can be implemented in aws2tf -->
- [ ] `AWS::EC2::TransitGatewayMulticastDomain` <!-- READY: aws_ec2_transit_gateway_multicast_domain can be implemented in aws2tf -->
- [ ] `AWS::EC2::TransitGatewayPeeringAttachment` <!-- READY: aws_ec2_transit_gateway_peering_attachment can be implemented in aws2tf -->
- [ ] `AWS::EC2::TransitGatewayRoute` <!-- READY: aws_ec2_transit_gateway_route can be implemented in aws2tf -->
- [ ] `AWS::EC2::TransitGatewayRouteTable` <!-- READY: aws_ec2_transit_gateway_route_table can be implemented in aws2tf -->
- [ ] `AWS::EC2::TransitGatewayRouteTableAssociation` <!-- READY: aws_ec2_transit_gateway_route_table_association can be implemented in aws2tf -->
- [ ] `AWS::EC2::TransitGatewayRouteTablePropagation` <!-- READY: aws_ec2_transit_gateway_route_table_propagation can be implemented in aws2tf -->
- [ ] `AWS::EC2::TransitGatewayVpcAttachment` <!-- READY: aws_ec2_transit_gateway_vpc_attachment can be implemented in aws2tf -->
- [ ] `AWS::EC2::VPCCidrBlock` <!-- READY: aws_ec2_vpccidr_block can be implemented in aws2tf -->
- [ ] `AWS::EC2::VPCEndpointConnectionNotification` <!-- READY: aws_ec2_vpcendpoint_connection_notification can be implemented in aws2tf -->
- [ ] `AWS::EC2::VPCEndpointServicePermissions` <!-- READY: aws_ec2_vpcendpoint_service_permissions can be implemented in aws2tf -->
- [ ] `AWS::EC2::VPCPeeringConnection` <!-- READY: aws_ec2_vpcpeering_connection can be implemented in aws2tf -->
- [ ] `AWS::EC2::VPNConnection` <!-- READY: aws_ec2_vpnconnection can be implemented in aws2tf -->
- [ ] `AWS::EC2::VPNConnectionRoute` <!-- READY: aws_ec2_vpnconnection_route can be implemented in aws2tf -->
- [ ] `AWS::EC2::VPNGateway` <!-- READY: aws_ec2_vpngateway can be implemented in aws2tf -->
- [ ] `AWS::EC2::VPNGatewayRoutePropagation` <!-- READY: aws_ec2_vpngateway_route_propagation can be implemented in aws2tf -->
- [ ] `AWS::EC2::VerifiedAccessEndpoint` <!-- READY: aws_ec2_verified_access_endpoint can be implemented in aws2tf -->
- [ ] `AWS::EC2::VerifiedAccessGroup` <!-- READY: aws_ec2_verified_access_group can be implemented in aws2tf -->
- [ ] `AWS::EC2::VerifiedAccessInstance` <!-- READY: aws_ec2_verified_access_instance can be implemented in aws2tf -->
- [ ] `AWS::EC2::VerifiedAccessTrustProvider` <!-- READY: aws_ec2_verified_access_trust_provider can be implemented in aws2tf -->
- [ ] `AWS::EC2::VolumeAttachment` <!-- READY: aws_ec2_volume_attachment can be implemented in aws2tf -->

### ECR (3 resources)

- [ ] `AWS::ECR::PullThroughCacheRule` <!-- READY: aws_ecr_pull_through_cache_rule can be implemented in aws2tf -->
- [ ] `AWS::ECR::RegistryPolicy` <!-- READY: aws_ecr_registry_policy can be implemented in aws2tf -->

### ECS (5 resources)

- [ ] `AWS::ECS::CapacityProvider` <!-- READY: aws_ecs_capacity_provider can be implemented in aws2tf -->
- [ ] `AWS::ECS::ClusterCapacityProviderAssociations` <!-- READY: aws_ecs_cluster_capacity_provider_associations can be implemented in aws2tf -->
- [ ] `AWS::ECS::ExpressGatewayService` <!-- READY: aws_ecs_express_gateway_service can be implemented in aws2tf -->
- [ ] `AWS::ECS::PrimaryTaskSet` <!-- READY: aws_ecs_primary_task_set can be implemented in aws2tf -->
- [ ] `AWS::ECS::TaskSet` <!-- READY: aws_ecs_task_set can be implemented in aws2tf -->

### EKS (5 resources)

- [ ] `AWS::EKS::AccessEntry` <!-- READY: aws_eks_access_entry can be implemented in aws2tf -->
- [ ] `AWS::EKS::Addon` <!-- READY: aws_eks_addon can be implemented in aws2tf -->
- [ ] `AWS::EKS::FargateProfile` <!-- READY: aws_eks_fargate_profile can be implemented in aws2tf -->
- [ ] `AWS::EKS::IdentityProviderConfig` <!-- READY: aws_eks_identity_provider_config can be implemented in aws2tf -->

### EMR (5 resources)

- [ ] `AWS::EMR::InstanceFleetConfig` <!-- READY: aws_emr_instance_fleet_config can be implemented in aws2tf -->
- [ ] `AWS::EMR::Step` <!-- READY: aws_emr_step can be implemented in aws2tf -->
- [ ] `AWS::EMR::WALWorkspace` <!-- READY: aws_emr_walworkspace can be implemented in aws2tf -->

### ElastiCache (10 resources)

- [ ] `AWS::ElastiCache::CacheCluster` <!-- READY: aws_elasticache_cache_cluster can be implemented in aws2tf -->
- [ ] `AWS::ElastiCache::GlobalReplicationGroup` <!-- READY: aws_elasticache_global_replication_group can be implemented in aws2tf -->
- [ ] `AWS::ElastiCache::ParameterGroup` <!-- READY: aws_elasticache_parameter_group can be implemented in aws2tf -->
- [ ] `AWS::ElastiCache::ReplicationGroup` <!-- READY: aws_elasticache_replication_group can be implemented in aws2tf -->
- [ ] `AWS::ElastiCache::SecurityGroup` <!-- READY: aws_elasticache_security_group can be implemented in aws2tf -->
- [ ] `AWS::ElastiCache::SecurityGroupIngress` <!-- READY: aws_elasticache_security_group_ingress can be implemented in aws2tf -->
- [ ] `AWS::ElastiCache::ServerlessCache` <!-- READY: aws_elasticache_serverless_cache can be implemented in aws2tf -->
- [ ] `AWS::ElastiCache::SubnetGroup` <!-- READY: aws_elasticache_subnet_group can be implemented in aws2tf -->
- [ ] `AWS::ElastiCache::User` <!-- READY: aws_elasticache_user can be implemented in aws2tf -->
- [ ] `AWS::ElastiCache::UserGroup` <!-- READY: aws_elasticache_user_group can be implemented in aws2tf -->

### ElasticBeanstalk (4 resources)

- [ ] `AWS::ElasticBeanstalk::Application` <!-- READY: aws_elasticbeanstalk_application can be implemented in aws2tf -->
- [ ] `AWS::ElasticBeanstalk::ApplicationVersion` <!-- READY: aws_elasticbeanstalk_application_version can be implemented in aws2tf -->
- [ ] `AWS::ElasticBeanstalk::ConfigurationTemplate` <!-- READY: aws_elasticbeanstalk_configuration_template can be implemented in aws2tf -->
- [ ] `AWS::ElasticBeanstalk::Environment` <!-- READY: aws_elasticbeanstalk_environment can be implemented in aws2tf -->

### ElasticLoadBalancing (1 resources)

- [ ] `AWS::ElasticLoadBalancing::LoadBalancer` <!-- READY: aws_elasticloadbalancing_load_balancer can be implemented in aws2tf -->

### ElasticLoadBalancingV2 (3 resources)

- [ ] `AWS::ElasticLoadBalancingV2::ListenerCertificate` <!-- READY: aws_elasticloadbalancingv2_listener_certificate can be implemented in aws2tf -->
- [ ] `AWS::ElasticLoadBalancingV2::TrustStore` <!-- READY: aws_elasticloadbalancingv2_trust_store can be implemented in aws2tf -->
- [ ] `AWS::ElasticLoadBalancingV2::TrustStoreRevocation` <!-- READY: aws_elasticloadbalancingv2_trust_store_revocation can be implemented in aws2tf -->

### Elasticsearch (1 resources)

- [ ] `AWS::Elasticsearch::Domain` <!-- READY: aws_elasticsearch_domain can be implemented in aws2tf -->

### EntityResolution (3 resources)

- [ ] `AWS::EntityResolution::IdMappingWorkflow` <!-- READY: aws_entityresolution_id_mapping_workflow can be implemented in aws2tf -->
- [ ] `AWS::EntityResolution::MatchingWorkflow` <!-- READY: aws_entityresolution_matching_workflow can be implemented in aws2tf -->
- [ ] `AWS::EntityResolution::SchemaMapping` <!-- READY: aws_entityresolution_schema_mapping can be implemented in aws2tf -->

### EventSchemas (4 resources)

- [ ] `AWS::EventSchemas::Discoverer` <!-- READY: aws_eventschemas_discoverer can be implemented in aws2tf -->
- [ ] `AWS::EventSchemas::Registry` <!-- READY: aws_eventschemas_registry can be implemented in aws2tf -->
- [ ] `AWS::EventSchemas::RegistryPolicy` <!-- READY: aws_eventschemas_registry_policy can be implemented in aws2tf -->
- [ ] `AWS::EventSchemas::Schema` <!-- READY: aws_eventschemas_schema can be implemented in aws2tf -->

### Events (5 resources)

- [ ] `AWS::Events::ApiDestination` <!-- READY: aws_events_api_destination can be implemented in aws2tf -->
- [ ] `AWS::Events::Archive` <!-- READY: aws_events_archive can be implemented in aws2tf -->
- [ ] `AWS::Events::Connection` <!-- READY: aws_events_connection can be implemented in aws2tf -->
- [ ] `AWS::Events::Endpoint` <!-- READY: aws_events_endpoint can be implemented in aws2tf -->
- [ ] `AWS::Events::EventBusPolicy` <!-- READY: aws_events_event_bus_policy can be implemented in aws2tf -->

### Evidently (5 resources)

- [ ] `AWS::Evidently::Experiment` <!-- READY: aws_evidently_experiment can be implemented in aws2tf -->
- [ ] `AWS::Evidently::Feature` <!-- READY: aws_evidently_feature can be implemented in aws2tf -->
- [ ] `AWS::Evidently::Launch` <!-- READY: aws_evidently_launch can be implemented in aws2tf -->

### FIS (2 resources)

- [ ] `AWS::FIS::ExperimentTemplate` <!-- READY: aws_fis_experiment_template can be implemented in aws2tf -->

### FMS (3 resources)

- [ ] `AWS::FMS::NotificationChannel` <!-- READY: aws_fms_notification_channel can be implemented in aws2tf -->
- [ ] `AWS::FMS::ResourceSet` <!-- READY: aws_fms_resource_set can be implemented in aws2tf -->

### FSx (5 resources)

- [ ] `AWS::FSx::FileSystem` <!-- READY: aws_fsx_file_system can be implemented in aws2tf -->
- [ ] `AWS::FSx::Snapshot` <!-- READY: aws_fsx_snapshot can be implemented in aws2tf -->
- [ ] `AWS::FSx::StorageVirtualMachine` <!-- READY: aws_fsx_storage_virtual_machine can be implemented in aws2tf -->
- [ ] `AWS::FSx::Volume` <!-- READY: aws_fsx_volume can be implemented in aws2tf -->

### FinSpace (1 resources)

- [ ] `AWS::FinSpace::Environment` <!-- READY: aws_finspace_environment can be implemented in aws2tf -->

### Forecast (2 resources)

- [ ] `AWS::Forecast::Dataset` <!-- READY: aws_forecast_dataset can be implemented in aws2tf -->
- [ ] `AWS::Forecast::DatasetGroup` <!-- READY: aws_forecast_dataset_group can be implemented in aws2tf -->

### FraudDetector (7 resources)

- [ ] `AWS::FraudDetector::Detector` <!-- READY: aws_frauddetector_detector can be implemented in aws2tf -->
- [ ] `AWS::FraudDetector::EntityType` <!-- READY: aws_frauddetector_entity_type can be implemented in aws2tf -->
- [ ] `AWS::FraudDetector::EventType` <!-- READY: aws_frauddetector_event_type can be implemented in aws2tf -->
- [ ] `AWS::FraudDetector::Label` <!-- READY: aws_frauddetector_label can be implemented in aws2tf -->
- [ ] `AWS::FraudDetector::List` <!-- READY: aws_frauddetector_list can be implemented in aws2tf -->
- [ ] `AWS::FraudDetector::Outcome` <!-- READY: aws_frauddetector_outcome can be implemented in aws2tf -->
- [ ] `AWS::FraudDetector::Variable` <!-- READY: aws_frauddetector_variable can be implemented in aws2tf -->

### GameLift (9 resources)

- [ ] `AWS::GameLift::Alias` <!-- READY: aws_gamelift_alias can be implemented in aws2tf -->
- [ ] `AWS::GameLift::Build` <!-- READY: aws_gamelift_build can be implemented in aws2tf -->
- [ ] `AWS::GameLift::GameServerGroup` <!-- READY: aws_gamelift_game_server_group can be implemented in aws2tf -->
- [ ] `AWS::GameLift::Location` <!-- READY: aws_gamelift_location can be implemented in aws2tf -->
- [ ] `AWS::GameLift::MatchmakingConfiguration` <!-- READY: aws_gamelift_matchmaking_configuration can be implemented in aws2tf -->
- [ ] `AWS::GameLift::MatchmakingRuleSet` <!-- READY: aws_gamelift_matchmaking_rule_set can be implemented in aws2tf -->
- [ ] `AWS::GameLift::Script` <!-- READY: aws_gamelift_script can be implemented in aws2tf -->

### GlobalAccelerator (3 resources)

- [ ] `AWS::GlobalAccelerator::EndpointGroup` <!-- READY: aws_globalaccelerator_endpoint_group can be implemented in aws2tf -->
- [ ] `AWS::GlobalAccelerator::Listener` <!-- READY: aws_globalaccelerator_listener can be implemented in aws2tf -->

### Glue (11 resources)

- [ ] `AWS::Glue::CustomEntityType` <!-- READY: aws_glue_custom_entity_type can be implemented in aws2tf -->
- [ ] `AWS::Glue::DataCatalogEncryptionSettings` <!-- READY: aws_glue_data_catalog_encryption_settings can be implemented in aws2tf -->
- [ ] `AWS::Glue::DataQualityRuleset` <!-- READY: aws_glue_data_quality_ruleset can be implemented in aws2tf -->
- [ ] `AWS::Glue::DevEndpoint` <!-- READY: aws_glue_dev_endpoint can be implemented in aws2tf -->
- [ ] `AWS::Glue::MLTransform` <!-- READY: aws_glue_mltransform can be implemented in aws2tf -->
- [ ] `AWS::Glue::Registry` <!-- READY: aws_glue_registry can be implemented in aws2tf -->
- [ ] `AWS::Glue::Schema` <!-- READY: aws_glue_schema can be implemented in aws2tf -->
- [ ] `AWS::Glue::SchemaVersion` <!-- READY: aws_glue_schema_version can be implemented in aws2tf -->
- [ ] `AWS::Glue::SchemaVersionMetadata` <!-- READY: aws_glue_schema_version_metadata can be implemented in aws2tf -->
- [ ] `AWS::Glue::Trigger` <!-- READY: aws_glue_trigger can be implemented in aws2tf -->
- [ ] `AWS::Glue::Workflow` <!-- READY: aws_glue_workflow can be implemented in aws2tf -->

### Grafana (1 resources)

- [ ] `AWS::Grafana::Workspace` <!-- READY: aws_grafana_workspace can be implemented in aws2tf -->

### Greengrass (16 resources)

- [ ] `AWS::Greengrass::ConnectorDefinition` <!-- READY: aws_greengrass_connector_definition can be implemented in aws2tf -->
- [ ] `AWS::Greengrass::ConnectorDefinitionVersion` <!-- READY: aws_greengrass_connector_definition_version can be implemented in aws2tf -->
- [ ] `AWS::Greengrass::CoreDefinition` <!-- READY: aws_greengrass_core_definition can be implemented in aws2tf -->
- [ ] `AWS::Greengrass::CoreDefinitionVersion` <!-- READY: aws_greengrass_core_definition_version can be implemented in aws2tf -->
- [ ] `AWS::Greengrass::DeviceDefinition` <!-- READY: aws_greengrass_device_definition can be implemented in aws2tf -->
- [ ] `AWS::Greengrass::DeviceDefinitionVersion` <!-- READY: aws_greengrass_device_definition_version can be implemented in aws2tf -->
- [ ] `AWS::Greengrass::FunctionDefinition` <!-- READY: aws_greengrass_function_definition can be implemented in aws2tf -->
- [ ] `AWS::Greengrass::FunctionDefinitionVersion` <!-- READY: aws_greengrass_function_definition_version can be implemented in aws2tf -->
- [ ] `AWS::Greengrass::Group` <!-- READY: aws_greengrass_group can be implemented in aws2tf -->
- [ ] `AWS::Greengrass::GroupVersion` <!-- READY: aws_greengrass_group_version can be implemented in aws2tf -->
- [ ] `AWS::Greengrass::LoggerDefinition` <!-- READY: aws_greengrass_logger_definition can be implemented in aws2tf -->
- [ ] `AWS::Greengrass::LoggerDefinitionVersion` <!-- READY: aws_greengrass_logger_definition_version can be implemented in aws2tf -->
- [ ] `AWS::Greengrass::ResourceDefinition` <!-- READY: aws_greengrass_resource_definition can be implemented in aws2tf -->
- [ ] `AWS::Greengrass::ResourceDefinitionVersion` <!-- READY: aws_greengrass_resource_definition_version can be implemented in aws2tf -->
- [ ] `AWS::Greengrass::SubscriptionDefinition` <!-- READY: aws_greengrass_subscription_definition can be implemented in aws2tf -->
- [ ] `AWS::Greengrass::SubscriptionDefinitionVersion` <!-- READY: aws_greengrass_subscription_definition_version can be implemented in aws2tf -->

### GreengrassV2 (2 resources)

- [ ] `AWS::GreengrassV2::ComponentVersion` <!-- READY: aws_greengrassv2_component_version can be implemented in aws2tf -->
- [ ] `AWS::GreengrassV2::Deployment` <!-- READY: aws_greengrassv2_deployment can be implemented in aws2tf -->

### GroundStation (3 resources)

- [ ] `AWS::GroundStation::Config` <!-- READY: aws_groundstation_config can be implemented in aws2tf -->
- [ ] `AWS::GroundStation::DataflowEndpointGroup` <!-- READY: aws_groundstation_dataflow_endpoint_group can be implemented in aws2tf -->
- [ ] `AWS::GroundStation::MissionProfile` <!-- READY: aws_groundstation_mission_profile can be implemented in aws2tf -->

### GuardDuty (6 resources)

- [ ] `AWS::GuardDuty::Detector` <!-- READY: aws_guardduty_detector can be implemented in aws2tf -->
- [ ] `AWS::GuardDuty::Filter` <!-- READY: aws_guardduty_filter can be implemented in aws2tf -->
- [ ] `AWS::GuardDuty::IPSet` <!-- READY: aws_guardduty_ipset can be implemented in aws2tf -->
- [ ] `AWS::GuardDuty::Master` <!-- READY: aws_guardduty_master can be implemented in aws2tf -->
- [ ] `AWS::GuardDuty::Member` <!-- READY: aws_guardduty_member can be implemented in aws2tf -->
- [ ] `AWS::GuardDuty::ThreatIntelSet` <!-- READY: aws_guardduty_threat_intel_set can be implemented in aws2tf -->

### HealthImaging (1 resources)

- [ ] `AWS::HealthImaging::Datastore` <!-- READY: aws_healthimaging_datastore can be implemented in aws2tf -->

### HealthLake (1 resources)

- [ ] `AWS::HealthLake::FHIRDatastore` <!-- READY: aws_healthlake_fhirdatastore can be implemented in aws2tf -->

### IAM (7 resources)

- [ ] `AWS::IAM::GroupPolicy` <!-- READY: aws_iam_group_policy can be implemented in aws2tf -->
- [ ] `AWS::IAM::OIDCProvider` <!-- READY: aws_iam_oidcprovider can be implemented in aws2tf -->
- [ ] `AWS::IAM::RolePolicy` <!-- READY: aws_iam_role_policy can be implemented in aws2tf -->
- [ ] `AWS::IAM::SAMLProvider` <!-- READY: aws_iam_samlprovider can be implemented in aws2tf -->
- [ ] `AWS::IAM::ServerCertificate` <!-- READY: aws_iam_server_certificate can be implemented in aws2tf -->
- [ ] `AWS::IAM::UserPolicy` <!-- READY: aws_iam_user_policy can be implemented in aws2tf -->
- [ ] `AWS::IAM::VirtualMFADevice` <!-- READY: aws_iam_virtual_mfadevice can be implemented in aws2tf -->

### IVS (4 resources)

- [ ] `AWS::IVS::StreamKey` <!-- READY: aws_ivs_stream_key can be implemented in aws2tf -->

### IdentityStore (2 resources)

- [ ] `AWS::IdentityStore::Group` <!-- READY: aws_identitystore_group can be implemented in aws2tf -->
- [ ] `AWS::IdentityStore::GroupMembership` <!-- READY: aws_identitystore_group_membership can be implemented in aws2tf -->

### ImageBuilder (9 resources)

- [ ] `AWS::ImageBuilder::Component` <!-- READY: aws_imagebuilder_component can be implemented in aws2tf -->
- [ ] `AWS::ImageBuilder::ContainerRecipe` <!-- READY: aws_imagebuilder_container_recipe can be implemented in aws2tf -->
- [ ] `AWS::ImageBuilder::DistributionConfiguration` <!-- READY: aws_imagebuilder_distribution_configuration can be implemented in aws2tf -->
- [ ] `AWS::ImageBuilder::ImagePipeline` <!-- READY: aws_imagebuilder_image_pipeline can be implemented in aws2tf -->
- [ ] `AWS::ImageBuilder::ImageRecipe` <!-- READY: aws_imagebuilder_image_recipe can be implemented in aws2tf -->
- [ ] `AWS::ImageBuilder::InfrastructureConfiguration` <!-- READY: aws_imagebuilder_infrastructure_configuration can be implemented in aws2tf -->

### InspectorV2 (1 resources)

- [ ] `AWS::InspectorV2::Filter` <!-- READY: aws_inspectorv2_filter can be implemented in aws2tf -->

### InternetMonitor (1 resources)

- [ ] `AWS::InternetMonitor::Monitor` <!-- READY: aws_internetmonitor_monitor can be implemented in aws2tf -->

### IoT (28 resources)

- [ ] `AWS::IoT::AccountAuditConfiguration` <!-- READY: aws_iot_account_audit_configuration can be implemented in aws2tf -->
- [ ] `AWS::IoT::CACertificate` <!-- READY: aws_iot_cacertificate can be implemented in aws2tf -->
- [ ] `AWS::IoT::CertificateProvider` <!-- READY: aws_iot_certificate_provider can be implemented in aws2tf -->
- [ ] `AWS::IoT::CustomMetric` <!-- READY: aws_iot_custom_metric can be implemented in aws2tf -->
- [ ] `AWS::IoT::Dimension` <!-- READY: aws_iot_dimension can be implemented in aws2tf -->
- [ ] `AWS::IoT::FleetMetric` <!-- READY: aws_iot_fleet_metric can be implemented in aws2tf -->
- [ ] `AWS::IoT::JobTemplate` <!-- READY: aws_iot_job_template can be implemented in aws2tf -->
- [ ] `AWS::IoT::Logging` <!-- READY: aws_iot_logging can be implemented in aws2tf -->
- [ ] `AWS::IoT::MitigationAction` <!-- READY: aws_iot_mitigation_action can be implemented in aws2tf -->
- [ ] `AWS::IoT::Policy` <!-- READY: aws_iot_policy can be implemented in aws2tf -->
- [ ] `AWS::IoT::PolicyPrincipalAttachment` <!-- READY: aws_iot_policy_principal_attachment can be implemented in aws2tf -->
- [ ] `AWS::IoT::ResourceSpecificLogging` <!-- READY: aws_iot_resource_specific_logging can be implemented in aws2tf -->
- [ ] `AWS::IoT::ScheduledAudit` <!-- READY: aws_iot_scheduled_audit can be implemented in aws2tf -->
- [ ] `AWS::IoT::SecurityProfile` <!-- READY: aws_iot_security_profile can be implemented in aws2tf -->
- [ ] `AWS::IoT::SoftwarePackage` <!-- READY: aws_iot_software_package can be implemented in aws2tf -->
- [ ] `AWS::IoT::SoftwarePackageVersion` <!-- READY: aws_iot_software_package_version can be implemented in aws2tf -->
- [ ] `AWS::IoT::Thing` <!-- READY: aws_iot_thing can be implemented in aws2tf -->
- [ ] `AWS::IoT::TopicRule` <!-- READY: aws_iot_topic_rule can be implemented in aws2tf -->

### IoT1Click (3 resources)

- [ ] `AWS::IoT1Click::Device` <!-- READY: aws_iot1click_device can be implemented in aws2tf -->
- [ ] `AWS::IoT1Click::Placement` <!-- READY: aws_iot1click_placement can be implemented in aws2tf -->
- [ ] `AWS::IoT1Click::Project` <!-- READY: aws_iot1click_project can be implemented in aws2tf -->

### IoTAnalytics (4 resources)

- [ ] `AWS::IoTAnalytics::Channel` <!-- READY: aws_iotanalytics_channel can be implemented in aws2tf -->
- [ ] `AWS::IoTAnalytics::Dataset` <!-- READY: aws_iotanalytics_dataset can be implemented in aws2tf -->
- [ ] `AWS::IoTAnalytics::Datastore` <!-- READY: aws_iotanalytics_datastore can be implemented in aws2tf -->
- [ ] `AWS::IoTAnalytics::Pipeline` <!-- READY: aws_iotanalytics_pipeline can be implemented in aws2tf -->

### IoTCoreDeviceAdvisor (1 resources)

- [ ] `AWS::IoTCoreDeviceAdvisor::SuiteDefinition` <!-- READY: aws_iotcoredeviceadvisor_suite_definition can be implemented in aws2tf -->

### IoTEvents (3 resources)

- [ ] `AWS::IoTEvents::AlarmModel` <!-- READY: aws_iotevents_alarm_model can be implemented in aws2tf -->
- [ ] `AWS::IoTEvents::DetectorModel` <!-- READY: aws_iotevents_detector_model can be implemented in aws2tf -->
- [ ] `AWS::IoTEvents::Input` <!-- READY: aws_iotevents_input can be implemented in aws2tf -->

### IoTFleetHub (1 resources)

- [ ] `AWS::IoTFleetHub::Application` <!-- READY: aws_iotfleethub_application can be implemented in aws2tf -->

### IoTSiteWise (7 resources)

- [ ] `AWS::IoTSiteWise::AccessPolicy` <!-- READY: aws_iotsitewise_access_policy can be implemented in aws2tf -->
- [ ] `AWS::IoTSiteWise::Asset` <!-- READY: aws_iotsitewise_asset can be implemented in aws2tf -->
- [ ] `AWS::IoTSiteWise::AssetModel` <!-- READY: aws_iotsitewise_asset_model can be implemented in aws2tf -->
- [ ] `AWS::IoTSiteWise::Dashboard` <!-- READY: aws_iotsitewise_dashboard can be implemented in aws2tf -->
- [ ] `AWS::IoTSiteWise::Gateway` <!-- READY: aws_iotsitewise_gateway can be implemented in aws2tf -->
- [ ] `AWS::IoTSiteWise::Portal` <!-- READY: aws_iotsitewise_portal can be implemented in aws2tf -->
- [ ] `AWS::IoTSiteWise::Project` <!-- READY: aws_iotsitewise_project can be implemented in aws2tf -->

### IoTThingsGraph (1 resources)

- [ ] `AWS::IoTThingsGraph::FlowTemplate` <!-- READY: aws_iotthingsgraph_flow_template can be implemented in aws2tf -->

### IoTTwinMaker (5 resources)

- [ ] `AWS::IoTTwinMaker::ComponentType` <!-- READY: aws_iottwinmaker_component_type can be implemented in aws2tf -->
- [ ] `AWS::IoTTwinMaker::Entity` <!-- READY: aws_iottwinmaker_entity can be implemented in aws2tf -->
- [ ] `AWS::IoTTwinMaker::Scene` <!-- READY: aws_iottwinmaker_scene can be implemented in aws2tf -->
- [ ] `AWS::IoTTwinMaker::SyncJob` <!-- READY: aws_iottwinmaker_sync_job can be implemented in aws2tf -->
- [ ] `AWS::IoTTwinMaker::Workspace` <!-- READY: aws_iottwinmaker_workspace can be implemented in aws2tf -->

### IoTWireless (9 resources)

- [ ] `AWS::IoTWireless::Destination` <!-- READY: aws_iotwireless_destination can be implemented in aws2tf -->
- [ ] `AWS::IoTWireless::DeviceProfile` <!-- READY: aws_iotwireless_device_profile can be implemented in aws2tf -->
- [ ] `AWS::IoTWireless::FuotaTask` <!-- READY: aws_iotwireless_fuota_task can be implemented in aws2tf -->
- [ ] `AWS::IoTWireless::MulticastGroup` <!-- READY: aws_iotwireless_multicast_group can be implemented in aws2tf -->
- [ ] `AWS::IoTWireless::NetworkAnalyzerConfiguration` <!-- READY: aws_iotwireless_network_analyzer_configuration can be implemented in aws2tf -->
- [ ] `AWS::IoTWireless::ServiceProfile` <!-- READY: aws_iotwireless_service_profile can be implemented in aws2tf -->
- [ ] `AWS::IoTWireless::TaskDefinition` <!-- READY: aws_iotwireless_task_definition can be implemented in aws2tf -->
- [ ] `AWS::IoTWireless::WirelessDevice` <!-- READY: aws_iotwireless_wireless_device can be implemented in aws2tf -->
- [ ] `AWS::IoTWireless::WirelessGateway` <!-- READY: aws_iotwireless_wireless_gateway can be implemented in aws2tf -->

### KafkaConnect (1 resources)

- [ ] `AWS::KafkaConnect::Connector` <!-- READY: aws_kafkaconnect_connector can be implemented in aws2tf -->

### KendraRanking (1 resources)

- [ ] `AWS::KendraRanking::ExecutionPlan` <!-- READY: aws_kendraranking_execution_plan can be implemented in aws2tf -->

### Kinesis (1 resources)

- [ ] `AWS::Kinesis::StreamConsumer` <!-- READY: aws_kinesis_stream_consumer can be implemented in aws2tf -->

### KinesisAnalytics (3 resources)

- [ ] `AWS::KinesisAnalytics::Application` <!-- READY: aws_kinesisanalytics_application can be implemented in aws2tf -->
- [ ] `AWS::KinesisAnalytics::ApplicationOutput` <!-- READY: aws_kinesisanalytics_application_output can be implemented in aws2tf -->
- [ ] `AWS::KinesisAnalytics::ApplicationReferenceDataSource` <!-- READY: aws_kinesisanalytics_application_reference_data_source can be implemented in aws2tf -->

### KinesisAnalyticsV2 (4 resources)

- [ ] `AWS::KinesisAnalyticsV2::Application` <!-- READY: aws_kinesisanalyticsv2_application can be implemented in aws2tf -->
- [ ] `AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption` <!-- READY: aws_kinesisanalyticsv2_application_cloud_watch_logging_option can be implemented in aws2tf -->
- [ ] `AWS::KinesisAnalyticsV2::ApplicationOutput` <!-- READY: aws_kinesisanalyticsv2_application_output can be implemented in aws2tf -->
- [ ] `AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource` <!-- READY: aws_kinesisanalyticsv2_application_reference_data_source can be implemented in aws2tf -->

### KinesisVideo (2 resources)

- [ ] `AWS::KinesisVideo::SignalingChannel` <!-- READY: aws_kinesisvideo_signaling_channel can be implemented in aws2tf -->
- [ ] `AWS::KinesisVideo::Stream` <!-- READY: aws_kinesisvideo_stream can be implemented in aws2tf -->

### LakeFormation (3 resources)

- [ ] `AWS::LakeFormation::Tag` <!-- READY: aws_lakeformation_tag can be implemented in aws2tf -->
- [ ] `AWS::LakeFormation::TagAssociation` <!-- READY: aws_lakeformation_tag_association can be implemented in aws2tf -->

### Lambda (5 resources)

- [ ] `AWS::Lambda::Alias` <!-- READY: aws_lambda_alias can be implemented in aws2tf -->
- [ ] `AWS::Lambda::CodeSigningConfig` <!-- READY: aws_lambda_code_signing_config can be implemented in aws2tf -->
- [ ] `AWS::Lambda::Url` <!-- READY: aws_lambda_url can be implemented in aws2tf -->
- [ ] `AWS::Lambda::Version` <!-- READY: aws_lambda_version can be implemented in aws2tf -->

### Lex (4 resources)

- [ ] `AWS::Lex::Bot` <!-- READY: aws_lex_bot can be implemented in aws2tf -->
- [ ] `AWS::Lex::BotAlias` <!-- READY: aws_lex_bot_alias can be implemented in aws2tf -->
- [ ] `AWS::Lex::BotVersion` <!-- READY: aws_lex_bot_version can be implemented in aws2tf -->
- [ ] `AWS::Lex::ResourcePolicy` <!-- READY: aws_lex_resource_policy can be implemented in aws2tf -->

### LicenseManager (2 resources)

- [ ] `AWS::LicenseManager::License` <!-- READY: aws_licensemanager_license can be implemented in aws2tf -->

### Lightsail (10 resources)

- [ ] `AWS::Lightsail::Alarm` <!-- READY: aws_lightsail_alarm can be implemented in aws2tf -->
- [ ] `AWS::Lightsail::Bucket` <!-- READY: aws_lightsail_bucket can be implemented in aws2tf -->
- [ ] `AWS::Lightsail::Certificate` <!-- READY: aws_lightsail_certificate can be implemented in aws2tf -->
- [ ] `AWS::Lightsail::Container` <!-- READY: aws_lightsail_container can be implemented in aws2tf -->
- [ ] `AWS::Lightsail::Database` <!-- READY: aws_lightsail_database can be implemented in aws2tf -->
- [ ] `AWS::Lightsail::Disk` <!-- READY: aws_lightsail_disk can be implemented in aws2tf -->
- [ ] `AWS::Lightsail::Instance` <!-- READY: aws_lightsail_instance can be implemented in aws2tf -->
- [ ] `AWS::Lightsail::LoadBalancer` <!-- READY: aws_lightsail_load_balancer can be implemented in aws2tf -->
- [ ] `AWS::Lightsail::LoadBalancerTlsCertificate` <!-- READY: aws_lightsail_load_balancer_tls_certificate can be implemented in aws2tf -->

### Location (7 resources)

- [ ] `AWS::Location::APIKey` <!-- READY: aws_location_apikey can be implemented in aws2tf -->
- [ ] `AWS::Location::TrackerConsumer` <!-- READY: aws_location_tracker_consumer can be implemented in aws2tf -->

### Logs (12 resources)

- [ ] `AWS::Logs::AccountPolicy` <!-- READY: aws_logs_account_policy can be implemented in aws2tf -->
- [ ] `AWS::Logs::Delivery` <!-- READY: aws_logs_delivery can be implemented in aws2tf -->
- [ ] `AWS::Logs::DeliveryDestination` <!-- READY: aws_logs_delivery_destination can be implemented in aws2tf -->
- [ ] `AWS::Logs::DeliverySource` <!-- READY: aws_logs_delivery_source can be implemented in aws2tf -->
- [ ] `AWS::Logs::Destination` <!-- READY: aws_logs_destination can be implemented in aws2tf -->
- [ ] `AWS::Logs::LogAnomalyDetector` <!-- READY: aws_logs_log_anomaly_detector can be implemented in aws2tf -->
- [ ] `AWS::Logs::LogStream` <!-- READY: aws_logs_log_stream can be implemented in aws2tf -->
- [ ] `AWS::Logs::LogStream` <!-- READY: aws_logs_log_stream can be implemented in aws2tf -->
- [ ] `AWS::Logs::MetricFilter` <!-- READY: aws_logs_metric_filter can be implemented in aws2tf -->
- [ ] `AWS::Logs::ResourcePolicy` <!-- READY: aws_logs_resource_policy can be implemented in aws2tf -->
- [ ] `AWS::Logs::SubscriptionFilter` <!-- READY: aws_logs_subscription_filter can be implemented in aws2tf -->

### LookoutMetrics (2 resources)

- [ ] `AWS::LookoutMetrics::Alert` <!-- READY: aws_lookoutmetrics_alert can be implemented in aws2tf -->
- [ ] `AWS::LookoutMetrics::AnomalyDetector` <!-- READY: aws_lookoutmetrics_anomaly_detector can be implemented in aws2tf -->

### LookoutVision (1 resources)

- [ ] `AWS::LookoutVision::Project` <!-- READY: aws_lookoutvision_project can be implemented in aws2tf -->

### MSK (4 resources)

- [ ] `AWS::MSK::BatchScramSecret` <!-- READY: aws_msk_batch_scram_secret can be implemented in aws2tf -->
- [ ] `AWS::MSK::Configuration` <!-- READY: aws_msk_configuration can be implemented in aws2tf -->
- [ ] `AWS::MSK::Replicator` <!-- READY: aws_msk_replicator can be implemented in aws2tf -->
- [ ] `AWS::MSK::VpcConnection` <!-- READY: aws_msk_vpc_connection can be implemented in aws2tf -->

### Macie (4 resources)

- [ ] `AWS::Macie::AllowList` <!-- READY: aws_macie_allow_list can be implemented in aws2tf -->
- [ ] `AWS::Macie::CustomDataIdentifier` <!-- READY: aws_macie_custom_data_identifier can be implemented in aws2tf -->
- [ ] `AWS::Macie::FindingsFilter` <!-- READY: aws_macie_findings_filter can be implemented in aws2tf -->
- [ ] `AWS::Macie::Session` <!-- READY: aws_macie_session can be implemented in aws2tf -->

### ManagedBlockchain (1 resources)

- [ ] `AWS::ManagedBlockchain::Member` <!-- READY: aws_managedblockchain_member can be implemented in aws2tf -->

### MediaConnect (9 resources)

- [ ] `AWS::MediaConnect::Bridge` <!-- READY: aws_mediaconnect_bridge can be implemented in aws2tf -->
- [ ] `AWS::MediaConnect::BridgeOutput` <!-- READY: aws_mediaconnect_bridge_output can be implemented in aws2tf -->
- [ ] `AWS::MediaConnect::BridgeSource` <!-- READY: aws_mediaconnect_bridge_source can be implemented in aws2tf -->
- [ ] `AWS::MediaConnect::Flow` <!-- READY: aws_mediaconnect_flow can be implemented in aws2tf -->
- [ ] `AWS::MediaConnect::FlowEntitlement` <!-- READY: aws_mediaconnect_flow_entitlement can be implemented in aws2tf -->
- [ ] `AWS::MediaConnect::FlowOutput` <!-- READY: aws_mediaconnect_flow_output can be implemented in aws2tf -->
- [ ] `AWS::MediaConnect::FlowSource` <!-- READY: aws_mediaconnect_flow_source can be implemented in aws2tf -->
- [ ] `AWS::MediaConnect::FlowVpcInterface` <!-- READY: aws_mediaconnect_flow_vpc_interface can be implemented in aws2tf -->
- [ ] `AWS::MediaConnect::Gateway` <!-- READY: aws_mediaconnect_gateway can be implemented in aws2tf -->

### MediaConvert (3 resources)

- [ ] `AWS::MediaConvert::JobTemplate` <!-- READY: aws_mediaconvert_job_template can be implemented in aws2tf -->
- [ ] `AWS::MediaConvert::Preset` <!-- READY: aws_mediaconvert_preset can be implemented in aws2tf -->
- [ ] `AWS::MediaConvert::Queue` <!-- READY: aws_mediaconvert_queue can be implemented in aws2tf -->

### MediaLive (5 resources)

- [ ] `AWS::MediaLive::Channel` <!-- READY: aws_medialive_channel can be implemented in aws2tf -->
- [ ] `AWS::MediaLive::Input` <!-- READY: aws_medialive_input can be implemented in aws2tf -->
- [ ] `AWS::MediaLive::InputSecurityGroup` <!-- READY: aws_medialive_input_security_group can be implemented in aws2tf -->
- [ ] `AWS::MediaLive::Multiplex` <!-- READY: aws_medialive_multiplex can be implemented in aws2tf -->
- [ ] `AWS::MediaLive::Multiplexprogram` <!-- READY: aws_medialive_multiplexprogram can be implemented in aws2tf -->

### MediaPackage (5 resources)

- [ ] `AWS::MediaPackage::Asset` <!-- READY: aws_mediapackage_asset can be implemented in aws2tf -->
- [ ] `AWS::MediaPackage::Channel` <!-- READY: aws_mediapackage_channel can be implemented in aws2tf -->
- [ ] `AWS::MediaPackage::OriginEndpoint` <!-- READY: aws_mediapackage_origin_endpoint can be implemented in aws2tf -->
- [ ] `AWS::MediaPackage::PackagingConfiguration` <!-- READY: aws_mediapackage_packaging_configuration can be implemented in aws2tf -->
- [ ] `AWS::MediaPackage::PackagingGroup` <!-- READY: aws_mediapackage_packaging_group can be implemented in aws2tf -->

### MediaPackageV2 (5 resources)

- [ ] `AWS::MediaPackageV2::Channel` <!-- READY: aws_mediapackagev2_channel can be implemented in aws2tf -->
- [ ] `AWS::MediaPackageV2::ChannelGroup` <!-- READY: aws_mediapackagev2_channel_group can be implemented in aws2tf -->
- [ ] `AWS::MediaPackageV2::ChannelPolicy` <!-- READY: aws_mediapackagev2_channel_policy can be implemented in aws2tf -->
- [ ] `AWS::MediaPackageV2::OriginEndpoint` <!-- READY: aws_mediapackagev2_origin_endpoint can be implemented in aws2tf -->
- [ ] `AWS::MediaPackageV2::OriginEndpointPolicy` <!-- READY: aws_mediapackagev2_origin_endpoint_policy can be implemented in aws2tf -->

### MediaStore (1 resources)

- [ ] `AWS::MediaStore::Container` <!-- READY: aws_mediastore_container can be implemented in aws2tf -->

### MediaTailor (6 resources)

- [ ] `AWS::MediaTailor::Channel` <!-- READY: aws_mediatailor_channel can be implemented in aws2tf -->
- [ ] `AWS::MediaTailor::ChannelPolicy` <!-- READY: aws_mediatailor_channel_policy can be implemented in aws2tf -->
- [ ] `AWS::MediaTailor::LiveSource` <!-- READY: aws_mediatailor_live_source can be implemented in aws2tf -->
- [ ] `AWS::MediaTailor::PlaybackConfiguration` <!-- READY: aws_mediatailor_playback_configuration can be implemented in aws2tf -->
- [ ] `AWS::MediaTailor::SourceLocation` <!-- READY: aws_mediatailor_source_location can be implemented in aws2tf -->
- [ ] `AWS::MediaTailor::VodSource` <!-- READY: aws_mediatailor_vod_source can be implemented in aws2tf -->

### MemoryDB (5 resources)

- [ ] `AWS::MemoryDB::ACL` <!-- READY: aws_memorydb_acl can be implemented in aws2tf -->
- [ ] `AWS::MemoryDB::Cluster` <!-- READY: aws_memorydb_cluster can be implemented in aws2tf -->
- [ ] `AWS::MemoryDB::ParameterGroup` <!-- READY: aws_memorydb_parameter_group can be implemented in aws2tf -->
- [ ] `AWS::MemoryDB::SubnetGroup` <!-- READY: aws_memorydb_subnet_group can be implemented in aws2tf -->
- [ ] `AWS::MemoryDB::User` <!-- READY: aws_memorydb_user can be implemented in aws2tf -->

### Neptune (5 resources)

- [ ] `AWS::Neptune::DBCluster` <!-- READY: aws_neptune_dbcluster can be implemented in aws2tf -->
- [ ] `AWS::Neptune::DBClusterParameterGroup` <!-- READY: aws_neptune_dbcluster_parameter_group can be implemented in aws2tf -->
- [ ] `AWS::Neptune::DBInstance` <!-- READY: aws_neptune_dbinstance can be implemented in aws2tf -->
- [ ] `AWS::Neptune::DBParameterGroup` <!-- READY: aws_neptune_dbparameter_group can be implemented in aws2tf -->
- [ ] `AWS::Neptune::DBSubnetGroup` <!-- READY: aws_neptune_dbsubnet_group can be implemented in aws2tf -->

### NeptuneGraph (2 resources)

- [ ] `AWS::NeptuneGraph::PrivateGraphEndpoint` <!-- READY: aws_neptunegraph_private_graph_endpoint can be implemented in aws2tf -->

### NetworkFirewall (1 resources)

- [ ] `AWS::NetworkFirewall::TLSInspectionConfiguration` <!-- READY: aws_networkfirewall_tlsinspection_configuration can be implemented in aws2tf -->

### NetworkManager (14 resources)

- [ ] `AWS::NetworkManager::ConnectPeer` <!-- READY: aws_networkmanager_connect_peer can be implemented in aws2tf -->
- [ ] `AWS::NetworkManager::CoreNetwork` <!-- READY: aws_networkmanager_core_network can be implemented in aws2tf -->
- [ ] `AWS::NetworkManager::Device` <!-- READY: aws_networkmanager_device can be implemented in aws2tf -->
- [ ] `AWS::NetworkManager::GlobalNetwork` <!-- READY: aws_networkmanager_global_network can be implemented in aws2tf -->
- [ ] `AWS::NetworkManager::Site` <!-- READY: aws_networkmanager_site can be implemented in aws2tf -->
- [ ] `AWS::NetworkManager::TransitGatewayRegistration` <!-- READY: aws_networkmanager_transit_gateway_registration can be implemented in aws2tf -->

### NimbleStudio (4 resources)

- [ ] `AWS::NimbleStudio::LaunchProfile` <!-- READY: aws_nimblestudio_launch_profile can be implemented in aws2tf -->
- [ ] `AWS::NimbleStudio::StreamingImage` <!-- READY: aws_nimblestudio_streaming_image can be implemented in aws2tf -->
- [ ] `AWS::NimbleStudio::Studio` <!-- READY: aws_nimblestudio_studio can be implemented in aws2tf -->
- [ ] `AWS::NimbleStudio::StudioComponent` <!-- READY: aws_nimblestudio_studio_component can be implemented in aws2tf -->

### Omics (6 resources)

- [ ] `AWS::Omics::AnnotationStore` <!-- READY: aws_omics_annotation_store can be implemented in aws2tf -->
- [ ] `AWS::Omics::ReferenceStore` <!-- READY: aws_omics_reference_store can be implemented in aws2tf -->
- [ ] `AWS::Omics::RunGroup` <!-- READY: aws_omics_run_group can be implemented in aws2tf -->
- [ ] `AWS::Omics::SequenceStore` <!-- READY: aws_omics_sequence_store can be implemented in aws2tf -->
- [ ] `AWS::Omics::VariantStore` <!-- READY: aws_omics_variant_store can be implemented in aws2tf -->
- [ ] `AWS::Omics::Workflow` <!-- READY: aws_omics_workflow can be implemented in aws2tf -->

### OpenSearchServerless (6 resources)

- [ ] `AWS::OpenSearchServerless::AccessPolicy` <!-- READY: aws_opensearchserverless_access_policy can be implemented in aws2tf -->
- [ ] `AWS::OpenSearchServerless::Collection` <!-- READY: aws_opensearchserverless_collection can be implemented in aws2tf -->
- [ ] `AWS::OpenSearchServerless::LifecyclePolicy` <!-- READY: aws_opensearchserverless_lifecycle_policy can be implemented in aws2tf -->
- [ ] `AWS::OpenSearchServerless::SecurityPolicy` <!-- READY: aws_opensearchserverless_security_policy can be implemented in aws2tf -->
- [ ] `AWS::OpenSearchServerless::VpcEndpoint` <!-- READY: aws_opensearchserverless_vpc_endpoint can be implemented in aws2tf -->

### OpsWorks (7 resources)

- [ ] `AWS::OpsWorks::App` <!-- READY: aws_opsworks_app can be implemented in aws2tf -->
- [ ] `AWS::OpsWorks::ElasticLoadBalancerAttachment` <!-- READY: aws_opsworks_elastic_load_balancer_attachment can be implemented in aws2tf -->
- [ ] `AWS::OpsWorks::Layer` <!-- READY: aws_opsworks_layer can be implemented in aws2tf -->
- [ ] `AWS::OpsWorks::Volume` <!-- READY: aws_opsworks_volume can be implemented in aws2tf -->

### OpsWorksCM (1 resources)

- [ ] `AWS::OpsWorksCM::Server` <!-- READY: aws_opsworkscm_server can be implemented in aws2tf -->

### Organizations (5 resources)

- [ ] `AWS::Organizations::Account` <!-- READY: aws_organizations_account can be implemented in aws2tf -->
- [ ] `AWS::Organizations::Organization` <!-- READY: aws_organizations_organization can be implemented in aws2tf -->
- [ ] `AWS::Organizations::OrganizationalUnit` <!-- READY: aws_organizations_organizational_unit can be implemented in aws2tf -->
- [ ] `AWS::Organizations::Policy` <!-- READY: aws_organizations_policy can be implemented in aws2tf -->
- [ ] `AWS::Organizations::ResourcePolicy` <!-- READY: aws_organizations_resource_policy can be implemented in aws2tf -->

### PCAConnectorAD (5 resources)

- [ ] `AWS::PCAConnectorAD::Connector` <!-- READY: aws_pcaconnectorad_connector can be implemented in aws2tf -->
- [ ] `AWS::PCAConnectorAD::DirectoryRegistration` <!-- READY: aws_pcaconnectorad_directory_registration can be implemented in aws2tf -->
- [ ] `AWS::PCAConnectorAD::ServicePrincipalName` <!-- READY: aws_pcaconnectorad_service_principal_name can be implemented in aws2tf -->
- [ ] `AWS::PCAConnectorAD::Template` <!-- READY: aws_pcaconnectorad_template can be implemented in aws2tf -->
- [ ] `AWS::PCAConnectorAD::TemplateGroupAccessControlEntry` <!-- READY: aws_pcaconnectorad_template_group_access_control_entry can be implemented in aws2tf -->

### Panorama (3 resources)

- [ ] `AWS::Panorama::ApplicationInstance` <!-- READY: aws_panorama_application_instance can be implemented in aws2tf -->
- [ ] `AWS::Panorama::Package` <!-- READY: aws_panorama_package can be implemented in aws2tf -->
- [ ] `AWS::Panorama::PackageVersion` <!-- READY: aws_panorama_package_version can be implemented in aws2tf -->

### PaymentCryptography (2 resources)

- [ ] `AWS::PaymentCryptography::Alias` <!-- READY: aws_paymentcryptography_alias can be implemented in aws2tf -->

### Personalize (4 resources)

- [ ] `AWS::Personalize::Dataset` <!-- READY: aws_personalize_dataset can be implemented in aws2tf -->
- [ ] `AWS::Personalize::DatasetGroup` <!-- READY: aws_personalize_dataset_group can be implemented in aws2tf -->
- [ ] `AWS::Personalize::Schema` <!-- READY: aws_personalize_schema can be implemented in aws2tf -->
- [ ] `AWS::Personalize::Solution` <!-- READY: aws_personalize_solution can be implemented in aws2tf -->

### Pinpoint (19 resources)

- [ ] `AWS::Pinpoint::ADMChannel` <!-- READY: aws_pinpoint_admchannel can be implemented in aws2tf -->
- [ ] `AWS::Pinpoint::APNSChannel` <!-- READY: aws_pinpoint_apnschannel can be implemented in aws2tf -->
- [ ] `AWS::Pinpoint::APNSSandboxChannel` <!-- READY: aws_pinpoint_apnssandbox_channel can be implemented in aws2tf -->
- [ ] `AWS::Pinpoint::APNSVoipChannel` <!-- READY: aws_pinpoint_apnsvoip_channel can be implemented in aws2tf -->
- [ ] `AWS::Pinpoint::APNSVoipSandboxChannel` <!-- READY: aws_pinpoint_apnsvoip_sandbox_channel can be implemented in aws2tf -->
- [ ] `AWS::Pinpoint::ApplicationSettings` <!-- READY: aws_pinpoint_application_settings can be implemented in aws2tf -->
- [ ] `AWS::Pinpoint::Campaign` <!-- READY: aws_pinpoint_campaign can be implemented in aws2tf -->
- [ ] `AWS::Pinpoint::GCMChannel` <!-- READY: aws_pinpoint_gcmchannel can be implemented in aws2tf -->
- [ ] `AWS::Pinpoint::InAppTemplate` <!-- READY: aws_pinpoint_in_app_template can be implemented in aws2tf -->
- [ ] `AWS::Pinpoint::PushTemplate` <!-- READY: aws_pinpoint_push_template can be implemented in aws2tf -->
- [ ] `AWS::Pinpoint::SMSChannel` <!-- READY: aws_pinpoint_smschannel can be implemented in aws2tf -->
- [ ] `AWS::Pinpoint::Segment` <!-- READY: aws_pinpoint_segment can be implemented in aws2tf -->
- [ ] `AWS::Pinpoint::SmsTemplate` <!-- READY: aws_pinpoint_sms_template can be implemented in aws2tf -->
- [ ] `AWS::Pinpoint::VoiceChannel` <!-- READY: aws_pinpoint_voice_channel can be implemented in aws2tf -->

### PinpointEmail (4 resources)

- [ ] `AWS::PinpointEmail::ConfigurationSet` <!-- READY: aws_pinpointemail_configuration_set can be implemented in aws2tf -->
- [ ] `AWS::PinpointEmail::ConfigurationSetEventDestination` <!-- READY: aws_pinpointemail_configuration_set_event_destination can be implemented in aws2tf -->
- [ ] `AWS::PinpointEmail::DedicatedIpPool` <!-- READY: aws_pinpointemail_dedicated_ip_pool can be implemented in aws2tf -->
- [ ] `AWS::PinpointEmail::Identity` <!-- READY: aws_pinpointemail_identity can be implemented in aws2tf -->

### Proton (3 resources)

- [ ] `AWS::Proton::EnvironmentAccountConnection` <!-- READY: aws_proton_environment_account_connection can be implemented in aws2tf -->
- [ ] `AWS::Proton::EnvironmentTemplate` <!-- READY: aws_proton_environment_template can be implemented in aws2tf -->
- [ ] `AWS::Proton::ServiceTemplate` <!-- READY: aws_proton_service_template can be implemented in aws2tf -->

### QuickSight (9 resources)

- [ ] `AWS::QuickSight::Analysis` <!-- READY: aws_quicksight_analysis can be implemented in aws2tf -->
- [ ] `AWS::QuickSight::Dashboard` <!-- READY: aws_quicksight_dashboard can be implemented in aws2tf -->
- [ ] `AWS::QuickSight::DataSet` <!-- READY: aws_quicksight_data_set can be implemented in aws2tf -->
- [ ] `AWS::QuickSight::DataSource` <!-- READY: aws_quicksight_data_source can be implemented in aws2tf -->
- [ ] `AWS::QuickSight::RefreshSchedule` <!-- READY: aws_quicksight_refresh_schedule can be implemented in aws2tf -->
- [ ] `AWS::QuickSight::Template` <!-- READY: aws_quicksight_template can be implemented in aws2tf -->
- [ ] `AWS::QuickSight::Theme` <!-- READY: aws_quicksight_theme can be implemented in aws2tf -->
- [ ] `AWS::QuickSight::Topic` <!-- READY: aws_quicksight_topic can be implemented in aws2tf -->
- [ ] `AWS::QuickSight::VPCConnection` <!-- READY: aws_quicksight_vpcconnection can be implemented in aws2tf -->

### RAM (2 resources)

- [ ] `AWS::RAM::Permission` <!-- READY: aws_ram_permission can be implemented in aws2tf -->
- [ ] `AWS::RAM::ResourceShare` <!-- READY: aws_ram_resource_share can be implemented in aws2tf -->

### RDS (7 resources)

- [ ] `AWS::RDS::CustomDBEngineVersion` <!-- READY: aws_rds_custom_dbengine_version can be implemented in aws2tf -->
- [ ] `AWS::RDS::DBProxy` <!-- READY: aws_rds_dbproxy can be implemented in aws2tf -->
- [ ] `AWS::RDS::DBProxyEndpoint` <!-- READY: aws_rds_dbproxy_endpoint can be implemented in aws2tf -->
- [ ] `AWS::RDS::DBProxyTargetGroup` <!-- READY: aws_rds_dbproxy_target_group can be implemented in aws2tf -->
- [ ] `AWS::RDS::DBSecurityGroupIngress` <!-- READY: aws_rds_dbsecurity_group_ingress can be implemented in aws2tf -->
- [ ] `AWS::RDS::GlobalCluster` <!-- READY: aws_rds_global_cluster can be implemented in aws2tf -->
- [ ] `AWS::RDS::OptionGroup` <!-- READY: aws_rds_option_group can be implemented in aws2tf -->

### Redshift (6 resources)

- [ ] `AWS::Redshift::ClusterSecurityGroup` <!-- READY: aws_redshift_cluster_security_group can be implemented in aws2tf -->
- [ ] `AWS::Redshift::ClusterSecurityGroupIngress` <!-- READY: aws_redshift_cluster_security_group_ingress can be implemented in aws2tf -->
- [ ] `AWS::Redshift::EndpointAccess` <!-- READY: aws_redshift_endpoint_access can be implemented in aws2tf -->
- [ ] `AWS::Redshift::EndpointAuthorization` <!-- READY: aws_redshift_endpoint_authorization can be implemented in aws2tf -->
- [ ] `AWS::Redshift::EventSubscription` <!-- READY: aws_redshift_event_subscription can be implemented in aws2tf -->
- [ ] `AWS::Redshift::ScheduledAction` <!-- READY: aws_redshift_scheduled_action can be implemented in aws2tf -->

### RefactorSpaces (4 resources)

- [ ] `AWS::RefactorSpaces::Application` <!-- READY: aws_refactorspaces_application can be implemented in aws2tf -->
- [ ] `AWS::RefactorSpaces::Environment` <!-- READY: aws_refactorspaces_environment can be implemented in aws2tf -->
- [ ] `AWS::RefactorSpaces::Route` <!-- READY: aws_refactorspaces_route can be implemented in aws2tf -->
- [ ] `AWS::RefactorSpaces::Service` <!-- READY: aws_refactorspaces_service can be implemented in aws2tf -->

### Rekognition (3 resources)

- [ ] `AWS::Rekognition::Collection` <!-- READY: aws_rekognition_collection can be implemented in aws2tf -->
- [ ] `AWS::Rekognition::Project` <!-- READY: aws_rekognition_project can be implemented in aws2tf -->
- [ ] `AWS::Rekognition::StreamProcessor` <!-- READY: aws_rekognition_stream_processor can be implemented in aws2tf -->

### ResilienceHub (2 resources)

- [ ] `AWS::ResilienceHub::App` <!-- READY: aws_resiliencehub_app can be implemented in aws2tf -->

### ResourceExplorer2 (3 resources)

- [ ] `AWS::ResourceExplorer2::DefaultViewAssociation` <!-- READY: aws_resourceexplorer2_default_view_association can be implemented in aws2tf -->
- [ ] `AWS::ResourceExplorer2::View` <!-- READY: aws_resourceexplorer2_view can be implemented in aws2tf -->

### ResourceGroups (1 resources)

- [ ] `AWS::ResourceGroups::Group` <!-- READY: aws_resourcegroups_group can be implemented in aws2tf -->

### RoboMaker (6 resources)

- [ ] `AWS::RoboMaker::Fleet` <!-- READY: aws_robomaker_fleet can be implemented in aws2tf -->
- [ ] `AWS::RoboMaker::Robot` <!-- READY: aws_robomaker_robot can be implemented in aws2tf -->
- [ ] `AWS::RoboMaker::RobotApplication` <!-- READY: aws_robomaker_robot_application can be implemented in aws2tf -->
- [ ] `AWS::RoboMaker::RobotApplicationVersion` <!-- READY: aws_robomaker_robot_application_version can be implemented in aws2tf -->
- [ ] `AWS::RoboMaker::SimulationApplication` <!-- READY: aws_robomaker_simulation_application can be implemented in aws2tf -->
- [ ] `AWS::RoboMaker::SimulationApplicationVersion` <!-- READY: aws_robomaker_simulation_application_version can be implemented in aws2tf -->

### RolesAnywhere (3 resources)

- [ ] `AWS::RolesAnywhere::CRL` <!-- READY: aws_rolesanywhere_crl can be implemented in aws2tf -->

### Route53 (5 resources)

- [ ] `AWS::Route53::CidrCollection` <!-- READY: aws_route53_cidr_collection can be implemented in aws2tf -->
- [ ] `AWS::Route53::DNSSEC` <!-- READY: aws_route53_dnssec can be implemented in aws2tf -->
- [ ] `AWS::Route53::HealthCheck` <!-- READY: aws_route53_health_check can be implemented in aws2tf -->
- [ ] `AWS::Route53::KeySigningKey` <!-- READY: aws_route53_key_signing_key can be implemented in aws2tf -->
- [ ] `AWS::Route53::RecordSetGroup` <!-- READY: aws_route53_record_set_group can be implemented in aws2tf -->

### Route53RecoveryControl (4 resources)

- [ ] `AWS::Route53RecoveryControl::Cluster` <!-- READY: aws_route53recoverycontrol_cluster can be implemented in aws2tf -->
- [ ] `AWS::Route53RecoveryControl::ControlPanel` <!-- READY: aws_route53recoverycontrol_control_panel can be implemented in aws2tf -->
- [ ] `AWS::Route53RecoveryControl::RoutingControl` <!-- READY: aws_route53recoverycontrol_routing_control can be implemented in aws2tf -->
- [ ] `AWS::Route53RecoveryControl::SafetyRule` <!-- READY: aws_route53recoverycontrol_safety_rule can be implemented in aws2tf -->

### Route53Resolver (11 resources)

- [ ] `AWS::Route53Resolver::FirewallDomainList` <!-- READY: aws_route53resolver_firewall_domain_list can be implemented in aws2tf -->
- [ ] `AWS::Route53Resolver::FirewallRuleGroup` <!-- READY: aws_route53resolver_firewall_rule_group can be implemented in aws2tf -->
- [ ] `AWS::Route53Resolver::FirewallRuleGroupAssociation` <!-- READY: aws_route53resolver_firewall_rule_group_association can be implemented in aws2tf -->
- [ ] `AWS::Route53Resolver::OutpostResolver` <!-- READY: aws_route53resolver_outpost_resolver can be implemented in aws2tf -->
- [ ] `AWS::Route53Resolver::ResolverConfig` <!-- READY: aws_route53resolver_resolver_config can be implemented in aws2tf -->
- [ ] `AWS::Route53Resolver::ResolverDNSSECConfig` <!-- READY: aws_route53resolver_resolver_dnssecconfig can be implemented in aws2tf -->
- [ ] `AWS::Route53Resolver::ResolverEndpoint` <!-- READY: aws_route53resolver_resolver_endpoint can be implemented in aws2tf -->
- [ ] `AWS::Route53Resolver::ResolverQueryLoggingConfig` <!-- READY: aws_route53resolver_resolver_query_logging_config can be implemented in aws2tf -->
- [ ] `AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation` <!-- READY: aws_route53resolver_resolver_query_logging_config_association can be implemented in aws2tf -->
- [ ] `AWS::Route53Resolver::ResolverRule` <!-- READY: aws_route53resolver_resolver_rule can be implemented in aws2tf -->
- [ ] `AWS::Route53Resolver::ResolverRuleAssociation` <!-- READY: aws_route53resolver_resolver_rule_association can be implemented in aws2tf -->

### S3 (1 resources)

- [ ] `AWS::S3::StorageLensGroup` <!-- READY: aws_s3_storage_lens_group can be implemented in aws2tf -->

### S3Express (2 resources)

- [ ] `AWS::S3Express::BucketPolicy` <!-- READY: aws_s3express_bucket_policy can be implemented in aws2tf -->
- [ ] `AWS::S3Express::DirectoryBucket` <!-- READY: aws_s3express_directory_bucket can be implemented in aws2tf -->

### S3ObjectLambda (2 resources)

- [ ] `AWS::S3ObjectLambda::AccessPoint` <!-- READY: aws_s3objectlambda_access_point can be implemented in aws2tf -->
- [ ] `AWS::S3ObjectLambda::AccessPointPolicy` <!-- READY: aws_s3objectlambda_access_point_policy can be implemented in aws2tf -->

### S3Outposts (4 resources)

- [ ] `AWS::S3Outposts::AccessPoint` <!-- READY: aws_s3outposts_access_point can be implemented in aws2tf -->
- [ ] `AWS::S3Outposts::Bucket` <!-- READY: aws_s3outposts_bucket can be implemented in aws2tf -->
- [ ] `AWS::S3Outposts::BucketPolicy` <!-- READY: aws_s3outposts_bucket_policy can be implemented in aws2tf -->
- [ ] `AWS::S3Outposts::Endpoint` <!-- READY: aws_s3outposts_endpoint can be implemented in aws2tf -->

### SDB (1 resources)

- [ ] `AWS::SDB::Domain` <!-- READY: aws_sdb_domain can be implemented in aws2tf -->

### SES (10 resources)

- [ ] `AWS::SES::ConfigurationSetEventDestination` <!-- READY: aws_ses_configuration_set_event_destination can be implemented in aws2tf -->
- [ ] `AWS::SES::ContactList` <!-- READY: aws_ses_contact_list can be implemented in aws2tf -->
- [ ] `AWS::SES::DedicatedIpPool` <!-- READY: aws_ses_dedicated_ip_pool can be implemented in aws2tf -->
- [ ] `AWS::SES::ReceiptRule` <!-- READY: aws_ses_receipt_rule can be implemented in aws2tf -->
- [ ] `AWS::SES::ReceiptRuleSet` <!-- READY: aws_ses_receipt_rule_set can be implemented in aws2tf -->
- [ ] `AWS::SES::VdmAttributes` <!-- READY: aws_ses_vdm_attributes can be implemented in aws2tf -->

### SNS (1 resources)

- [ ] `AWS::SNS::TopicInlinePolicy` <!-- READY: aws_sns_topic_inline_policy can be implemented in aws2tf -->

### SQS (1 resources)

- [ ] `AWS::SQS::QueueInlinePolicy` <!-- READY: aws_sqs_queue_inline_policy can be implemented in aws2tf -->

### SSM (6 resources)

- [ ] `AWS::SSM::MaintenanceWindow` <!-- READY: aws_ssm_maintenance_window can be implemented in aws2tf -->
- [ ] `AWS::SSM::MaintenanceWindowTarget` <!-- READY: aws_ssm_maintenance_window_target can be implemented in aws2tf -->
- [ ] `AWS::SSM::MaintenanceWindowTask` <!-- READY: aws_ssm_maintenance_window_task can be implemented in aws2tf -->
- [ ] `AWS::SSM::PatchBaseline` <!-- READY: aws_ssm_patch_baseline can be implemented in aws2tf -->
- [ ] `AWS::SSM::ResourcePolicy` <!-- READY: aws_ssm_resource_policy can be implemented in aws2tf -->

### SSMContacts (4 resources)

- [ ] `AWS::SSMContacts::Contact` <!-- READY: aws_ssmcontacts_contact can be implemented in aws2tf -->
- [ ] `AWS::SSMContacts::ContactChannel` <!-- READY: aws_ssmcontacts_contact_channel can be implemented in aws2tf -->
- [ ] `AWS::SSMContacts::Plan` <!-- READY: aws_ssmcontacts_plan can be implemented in aws2tf -->

### SSMIncidents (2 resources)

- [ ] `AWS::SSMIncidents::ReplicationSet` <!-- READY: aws_ssmincidents_replication_set can be implemented in aws2tf -->
- [ ] `AWS::SSMIncidents::ResponsePlan` <!-- READY: aws_ssmincidents_response_plan can be implemented in aws2tf -->

### SSO (3 resources)

- [ ] `AWS::SSO::Assignment` <!-- READY: aws_sso_assignment can be implemented in aws2tf -->
- [ ] `AWS::SSO::InstanceAccessControlAttributeConfiguration` <!-- READY: aws_sso_instance_access_control_attribute_configuration can be implemented in aws2tf -->
- [ ] `AWS::SSO::PermissionSet` <!-- READY: aws_sso_permission_set can be implemented in aws2tf -->

### SageMaker (14 resources)

- [ ] `AWS::SageMaker::EndpointConfig` <!-- READY: aws_sagemaker_endpoint_config can be implemented in aws2tf -->
- [ ] `AWS::SageMaker::InferenceComponent` <!-- READY: aws_sagemaker_inference_component can be implemented in aws2tf -->
- [ ] `AWS::SageMaker::InferenceExperiment` <!-- READY: aws_sagemaker_inference_experiment can be implemented in aws2tf -->
- [ ] `AWS::SageMaker::ModelBiasJobDefinition` <!-- READY: aws_sagemaker_model_bias_job_definition can be implemented in aws2tf -->
- [ ] `AWS::SageMaker::ModelCard` <!-- READY: aws_sagemaker_model_card can be implemented in aws2tf -->
- [ ] `AWS::SageMaker::ModelExplainabilityJobDefinition` <!-- READY: aws_sagemaker_model_explainability_job_definition can be implemented in aws2tf -->
- [ ] `AWS::SageMaker::ModelPackage` <!-- READY: aws_sagemaker_model_package can be implemented in aws2tf -->
- [ ] `AWS::SageMaker::ModelPackageGroup` <!-- READY: aws_sagemaker_model_package_group can be implemented in aws2tf -->
- [ ] `AWS::SageMaker::ModelQualityJobDefinition` <!-- READY: aws_sagemaker_model_quality_job_definition can be implemented in aws2tf -->
- [ ] `AWS::SageMaker::MonitoringSchedule` <!-- READY: aws_sagemaker_monitoring_schedule can be implemented in aws2tf -->

### Scheduler (2 resources)

- [ ] `AWS::Scheduler::Schedule` <!-- READY: aws_scheduler_schedule can be implemented in aws2tf -->
- [x] `AWS::Scheduler::ScheduleGroup` <!-- COMPLETED: Test Successful -->

### SecurityHub (3 resources)

- [ ] `AWS::SecurityHub::AutomationRule` <!-- READY: aws_securityhub_automation_rule can be implemented in aws2tf -->
- [ ] `AWS::SecurityHub::Hub` <!-- READY: aws_securityhub_hub can be implemented in aws2tf -->
- [ ] `AWS::SecurityHub::Standard` <!-- READY: aws_securityhub_standard can be implemented in aws2tf -->

### ServiceCatalog (15 resources)

- [ ] `AWS::ServiceCatalog::AcceptedPortfolioShare` <!-- READY: aws_servicecatalog_accepted_portfolio_share can be implemented in aws2tf -->
- [ ] `AWS::ServiceCatalog::CloudFormationProduct` <!-- READY: aws_servicecatalog_cloud_formation_product can be implemented in aws2tf -->
- [ ] `AWS::ServiceCatalog::CloudFormationProvisionedProduct` <!-- READY: aws_servicecatalog_cloud_formation_provisioned_product can be implemented in aws2tf -->
- [ ] `AWS::ServiceCatalog::LaunchNotificationConstraint` <!-- READY: aws_servicecatalog_launch_notification_constraint can be implemented in aws2tf -->
- [ ] `AWS::ServiceCatalog::LaunchRoleConstraint` <!-- READY: aws_servicecatalog_launch_role_constraint can be implemented in aws2tf -->
- [ ] `AWS::ServiceCatalog::LaunchTemplateConstraint` <!-- READY: aws_servicecatalog_launch_template_constraint can be implemented in aws2tf -->
- [ ] `AWS::ServiceCatalog::Portfolio` <!-- READY: aws_servicecatalog_portfolio can be implemented in aws2tf -->
- [ ] `AWS::ServiceCatalog::PortfolioProductAssociation` <!-- READY: aws_servicecatalog_portfolio_product_association can be implemented in aws2tf -->
- [ ] `AWS::ServiceCatalog::ResourceUpdateConstraint` <!-- READY: aws_servicecatalog_resource_update_constraint can be implemented in aws2tf -->
- [ ] `AWS::ServiceCatalog::ServiceAction` <!-- READY: aws_servicecatalog_service_action can be implemented in aws2tf -->
- [ ] `AWS::ServiceCatalog::ServiceActionAssociation` <!-- READY: aws_servicecatalog_service_action_association can be implemented in aws2tf -->
- [ ] `AWS::ServiceCatalog::StackSetConstraint` <!-- READY: aws_servicecatalog_stack_set_constraint can be implemented in aws2tf -->
- [ ] `AWS::ServiceCatalog::TagOptionAssociation` <!-- READY: aws_servicecatalog_tag_option_association can be implemented in aws2tf -->

### ServiceCatalogAppRegistry (4 resources)

- [ ] `AWS::ServiceCatalogAppRegistry::ResourceAssociation` <!-- READY: aws_servicecatalogappregistry_resource_association can be implemented in aws2tf -->

### ServiceDiscovery (2 resources)

- [ ] `AWS::ServiceDiscovery::Instance` <!-- READY: aws_servicediscovery_instance can be implemented in aws2tf -->
- [ ] `AWS::ServiceDiscovery::PublicDnsNamespace` <!-- READY: aws_servicediscovery_public_dns_namespace can be implemented in aws2tf -->

### Shield (4 resources)

- [ ] `AWS::Shield::DRTAccess` <!-- READY: aws_shield_drtaccess can be implemented in aws2tf -->
- [ ] `AWS::Shield::ProtectionGroup` <!-- READY: aws_shield_protection_group can be implemented in aws2tf -->

### Signer (2 resources)

- [ ] `AWS::Signer::ProfilePermission` <!-- READY: aws_signer_profile_permission can be implemented in aws2tf -->
- [ ] `AWS::Signer::SigningProfile` <!-- READY: aws_signer_signing_profile can be implemented in aws2tf -->

### SimSpaceWeaver (1 resources)

- [ ] `AWS::SimSpaceWeaver::Simulation` <!-- READY: aws_simspaceweaver_simulation can be implemented in aws2tf -->

### StepFunctions (1 resources)

- [ ] `AWS::StepFunctions::StateMachineVersion` <!-- READY: aws_stepfunctions_state_machine_version can be implemented in aws2tf -->

### SupportApp (3 resources)

- [ ] `AWS::SupportApp::AccountAlias` <!-- READY: aws_supportapp_account_alias can be implemented in aws2tf -->
- [ ] `AWS::SupportApp::SlackChannelConfiguration` <!-- READY: aws_supportapp_slack_channel_configuration can be implemented in aws2tf -->
- [ ] `AWS::SupportApp::SlackWorkspaceConfiguration` <!-- READY: aws_supportapp_slack_workspace_configuration can be implemented in aws2tf -->

### SystemsManagerSAP (1 resources)

- [ ] `AWS::SystemsManagerSAP::Application` <!-- READY: aws_systemsmanagersap_application can be implemented in aws2tf -->

### Timestream (3 resources)

- [ ] `AWS::Timestream::Database` <!-- READY: aws_timestream_database can be implemented in aws2tf -->
- [ ] `AWS::Timestream::ScheduledQuery` <!-- READY: aws_timestream_scheduled_query can be implemented in aws2tf -->
- [ ] `AWS::Timestream::Table` <!-- READY: aws_timestream_table can be implemented in aws2tf -->

### Transfer (7 resources)

- [ ] `AWS::Transfer::Agreement` <!-- READY: aws_transfer_agreement can be implemented in aws2tf -->
- [ ] `AWS::Transfer::Certificate` <!-- READY: aws_transfer_certificate can be implemented in aws2tf -->
- [ ] `AWS::Transfer::Connector` <!-- READY: aws_transfer_connector can be implemented in aws2tf -->
- [ ] `AWS::Transfer::Profile` <!-- READY: aws_transfer_profile can be implemented in aws2tf -->
- [ ] `AWS::Transfer::Server` <!-- READY: aws_transfer_server can be implemented in aws2tf -->
- [ ] `AWS::Transfer::User` <!-- READY: aws_transfer_user can be implemented in aws2tf -->
- [ ] `AWS::Transfer::Workflow` <!-- READY: aws_transfer_workflow can be implemented in aws2tf -->

### VoiceID (1 resources)

- [ ] `AWS::VoiceID::Domain` <!-- READY: aws_voiceid_domain can be implemented in aws2tf -->

### WAF (7 resources)

- [ ] `AWS::WAF::WebACL` <!-- READY: aws_waf_web_acl can be implemented in aws2tf -->

### WAFRegional (11 resources)

- [ ] `AWS::WAFRegional::WebACLAssociation` <!-- READY: aws_wafregional_web_aclassociation can be implemented in aws2tf -->

### WAFv2 (3 resources)

- [ ] `AWS::WAFv2::RegexPatternSet` <!-- READY: aws_wafv2_regex_pattern_set can be implemented in aws2tf -->
- [ ] `AWS::WAFv2::RuleGroup` <!-- READY: aws_wafv2_rule_group can be implemented in aws2tf -->
- [ ] `AWS::WAFv2::WebACLAssociation` <!-- READY: aws_wafv2_web_aclassociation can be implemented in aws2tf -->

### Wisdom (3 resources)

- [ ] `AWS::Wisdom::Assistant` <!-- READY: aws_wisdom_assistant can be implemented in aws2tf -->
- [ ] `AWS::Wisdom::AssistantAssociation` <!-- READY: aws_wisdom_assistant_association can be implemented in aws2tf -->
- [ ] `AWS::Wisdom::KnowledgeBase` <!-- READY: aws_wisdom_knowledge_base can be implemented in aws2tf -->

### WorkSpaces (1 resources)

- [ ] `AWS::WorkSpaces::ConnectionAlias` <!-- READY: aws_workspaces_connection_alias can be implemented in aws2tf -->

### WorkSpacesThinClient (1 resources)

- [ ] `AWS::WorkSpacesThinClient::Environment` <!-- READY: aws_workspacesthinclient_environment can be implemented in aws2tf -->

### WorkSpacesWeb (8 resources)

- [ ] `AWS::WorkSpacesWeb::BrowserSettings` <!-- READY: aws_workspacesweb_browser_settings can be implemented in aws2tf -->
- [ ] `AWS::WorkSpacesWeb::IdentityProvider` <!-- READY: aws_workspacesweb_identity_provider can be implemented in aws2tf -->
- [ ] `AWS::WorkSpacesWeb::IpAccessSettings` <!-- READY: aws_workspacesweb_ip_access_settings can be implemented in aws2tf -->
- [ ] `AWS::WorkSpacesWeb::NetworkSettings` <!-- READY: aws_workspacesweb_network_settings can be implemented in aws2tf -->
- [ ] `AWS::WorkSpacesWeb::Portal` <!-- READY: aws_workspacesweb_portal can be implemented in aws2tf -->
- [ ] `AWS::WorkSpacesWeb::TrustStore` <!-- READY: aws_workspacesweb_trust_store can be implemented in aws2tf -->
- [ ] `AWS::WorkSpacesWeb::UserAccessLoggingSettings` <!-- READY: aws_workspacesweb_user_access_logging_settings can be implemented in aws2tf -->
- [ ] `AWS::WorkSpacesWeb::UserSettings` <!-- READY: aws_workspacesweb_user_settings can be implemented in aws2tf -->

### XRay (3 resources)

- [ ] `AWS::XRay::Group` <!-- READY: aws_xray_group can be implemented in aws2tf -->
- [ ] `AWS::XRay::ResourcePolicy` <!-- READY: aws_xray_resource_policy can be implemented in aws2tf -->
- [ ] `AWS::XRay::SamplingRule` <!-- READY: aws_xray_sampling_rule can be implemented in aws2tf -->

## Implementation Checklist

For each resource type, the implementation process involves:

1. **Check Terraform Support**
   - Verify the resource exists in [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
   - Note the Terraform resource name (e.g., `aws_bedrock_agent`)

2. **Add to aws_dict.py**
   - Define boto3 client name (e.g., `bedrock-agent`)
   - Define API method for listing (e.g., `list_agents`)
   - Define response key and ID field

3. **Create Get Function**
   - Implement in `code/get_aws_resources/aws_<service>.py`
   - Handle both list all and get specific cases
   - Register in `code/common.py`

4. **Create Handler (if needed)**
   - Implement in `code/fixtf_aws_resources/fixtf_<service>.py`
   - Handle computed fields, defaults, and lifecycle blocks
   - Register in `code/fixtf.py`

5. **Test with CloudFormation Stack**
   - Create test CloudFormation stack with the resource
   - Run: `./aws2tf.py -r <region> -t stack -i <stack-name>`
   - Verify Terraform generation and import
   - Document results in test directory

6. **Update stacks.py**
   - Replace `common.call_resource("aws_null", type+" "+pid)`
   - With: `common.call_resource("aws_<resource_type>", pid)` or `parn`

## Priority Recommendations

### High Priority (Common Services)
- AWS::Bedrock::* - AI/ML services gaining adoption
- AWS::QBusiness::* - Amazon Q Business
- AWS::Notifications::* - Cross-service notifications
- AWS::Route53Profiles::* - DNS management

### Medium Priority (Specialized Services)
- AWS::Deadline::* - Media rendering workloads
- AWS::IoTFleetWise::* - Automotive IoT
- AWS::BillingConductor::* - Cost management

### Low Priority (Niche Services)
- AWS::EVS::* - VMware migration
- AWS::ODB::* - Oracle database
- AWS::PCS::* - Parallel computing