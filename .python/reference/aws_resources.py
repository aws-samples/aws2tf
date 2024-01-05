import boto3

if type == "all":
    print("all")

elif type == "aws_accessanalyzer_analyzer":
    clfn="accessanalyzer";descfn="list_analyzers";topkey='AnalyzerList';key="Name";filterid=key
elif type == "aws_accessanalyzer_archive_rule":
    clfn="accessanalyzer";descfn="list_archive_rules";topkey='ArchiveRules';key="RuleName";filterid=key
elif type == "aws_account_alternate_contact":
    clfn="organizations";descfn="describe_account";topkey='Account';key="Id";filterid=key
elif type == "aws_account_primary_contact":
    clfn="organizations";descfn="describe_account";topkey='Account';key="Id";filterid=key
elif type == "aws_acm_certificate":
    clfn="acm";descfn="list_certificates";topkey='CertificateSummaryList';key="CertificateArn";filterid=key
elif type == "aws_acm_certificate_validation":
    clfn="acm";descfn="list_certificates";topkey='CertificateSummaryList';key="CertificateArn";filterid=key
elif type == "aws_acmpca_certificate":
    clfn="acm-pca";descfn="list_certificates";topkey='CertificateAuthorityList';key="Arn";filterid=key
elif type == "aws_acmpca_certificate_authority":
    clfn="acm-pca";descfn="list_certificate_authorities";topkey='CertificateAuthorities';key="Arn";filterid=key
elif type == "aws_acmpca_certificate_authority_certificate":
    clfn="acm-pca";descfn="list_certificate_authorities";topkey='CertificateAuthorities';key="Arn";filterid=key
elif type == "aws_acmpca_permission":
    clfn="acm-pca";descfn="list_permissions";topkey='Permissions';key="Permission";filterid=key
elif type == "aws_acmpca_policy":
    clfn="acm-pca";descfn="list_policies";topkey='Policies';key="PolicyId";filterid=key
elif type == "aws_ami":
    clfn="ec2";descfn="describe_images";topkey='Images';key="ImageId";filterid=key
elif type == "aws_ami_copy":
    clfn="ec2";descfn="describe_images";topkey='Images';key="ImageId";filterid=key
elif type == "aws_ami_from_instance":
    clfn="ec2";descfn="describe_images";topkey='Images';key="ImageId";filterid=key
elif type == "aws_ami_launch_permission":
    clfn="ec2";descfn="describe_images";topkey='Images';key="ImageId";filterid=key
elif type == "aws_amplify_app":
    clfn="amplify";descfn="list_apps";topkey='apps';key="appId";filterid=key
elif type == "aws_amplify_backend_environment":
    clfn="amplify";descfn="list_backend_environments";topkey='backendEnvironments';key="environmentName";filterid=key
elif type == "aws_amplify_branch":
    clfn="amplify";descfn="list_branches";topkey='branches';key="branchName";filterid=key
elif type == "aws_amplify_domain_association":
    clfn="amplify";descfn="list_domain_associations";topkey='domainAssociations';key="domainName";filterid=key
elif type == "aws_amplify_webhook":
    clfn="amplify";descfn="list_webhooks";topkey='webhooks';key="webhookName";filterid=key
elif type == "aws_api_gateway_account":
    clfn="apigateway";descfn="get_account";topkey='account';key="cloudwatchRoleArn";filterid=key
elif type == "aws_api_gateway_api_key":
    clfn="apigateway";descfn="get_api_keys";topkey='items';key="id";filterid=key
elif type == "aws_api_gateway_authorizer":
    clfn="apigateway";descfn="get_authorizers";topkey='items';key="id";filterid=key
elif type == "aws_api_gateway_base_path_mapping":
    clfn="apigateway";descfn="get_base_path_mappings";topkey='items';key="id";filterid=key
elif type == "aws_api_gateway_client_certificate":
    clfn="apigateway";descfn="get_client_certificates";topkey='items';key="clientCertificateId";filterid=key
elif type == "aws_api_gateway_deployment":
    clfn="apigateway";descfn="get_deployments";topkey='items';key="id";filterid=key
elif type == "aws_api_gateway_documentation_part":
    clfn="apigateway";descfn="get_documentation_parts";topkey='items';key="id";filterid=key
elif type == "aws_api_gateway_documentation_version":
    clfn="apigateway";descfn="get_documentation_versions";topkey='items';key="version";filterid=key
elif type == "aws_api_gateway_domain_name":
    clfn="apigateway";descfn="get_domain_names";topkey='items';key="domainName";filterid=key
elif type == "aws_api_gateway_gateway_response":
    clfn="apigateway";descfn="get_gateway_responses";topkey='items';key="responseType";filterid=key
elif type == "aws_api_gateway_integration":
    clfn="apigateway";descfn="get_integrations";topkey='items';key="id";filterid=key
elif type == "aws_api_gateway_integration_response":
    clfn="apigateway";descfn="get_integration_responses";topkey='items';key="id";filterid=key
elif type == "aws_api_gateway_method":
    clfn="apigateway";descfn="get_methods";topkey='items';key="httpMethod";filterid=key
elif type == "aws_api_gateway_method_response":
    clfn="apigateway";descfn="get_method_responses";topkey='items';key="httpMethod";filterid=key
elif type == "aws_api_gateway_method_settings":
    clfn="apigateway";descfn="get_method_settings";topkey='items';key="httpMethod";filterid=key
elif type == "aws_api_gateway_model":
    clfn="apigateway";descfn="get_models";topkey='items';key="id";filterid=key
elif type == "aws_api_gateway_request_validator":
    clfn="apigateway";descfn="get_request_validators";topkey='items';key="id";filterid=key
elif type == "aws_api_gateway_resource":
    clfn="apigateway";descfn="get_resources";topkey='items';key="id";filterid=key
elif type == "aws_api_gateway_rest_api":
    clfn="apigateway";descfn="get_rest_apis";topkey='items';key="id";filterid=key
elif type == "aws_api_gateway_rest_api_policy":
    clfn="apigateway";descfn="get_rest_api_policy";topkey='policy';key="id";filterid=key
elif type == "aws_api_gateway_stage":
    clfn="apigateway";descfn="get_stages";topkey='items';key="stageName";filterid=key
elif type == "aws_api_gateway_usage_plan":
    clfn="apigateway";descfn="get_usage_plans";topkey='items';key="id";filterid=key
elif type == "aws_api_gateway_usage_plan_key":
    clfn="apigateway";descfn="get_usage_plan_keys";topkey='items';key="id";filterid=key
elif type == "aws_api_gateway_vpc_link":
    clfn="apigateway";descfn="get_vpc_links";topkey='items';key="id";filterid=key
elif type == "aws_apigatewayv2_api":
    clfn="apigatewayv2";descfn="get_apis";topkey='Items';key="ApiId";filterid=key
elif type == "aws_apigatewayv2_api_mapping":
    clfn="apigatewayv2";descfn="get_api_mappings";topkey='Items';key="ApiMappingId";filterid=key
elif type == "aws_apigatewayv2_authorizer":
    clfn="apigatewayv2";descfn="get_authorizers";topkey='Items';key="AuthorizerId";filterid=key
elif type == "aws_apigatewayv2_deployment":
    clfn="apigatewayv2";descfn="get_deployments";topkey='Items';key="DeploymentId";filterid=key
elif type == "aws_apigatewayv2_domain_name":
    clfn="apigatewayv2";descfn="get_domain_names";topkey='Items';key="DomainNameId";filterid=key
elif type == "aws_apigatewayv2_integration":
    clfn="apigatewayv2";descfn="get_integrations";topkey='Items';key="IntegrationId";filterid=key
elif type == "aws_apigatewayv2_integration_response":
    clfn="apigatewayv2";descfn="get_integration_responses";topkey='Items';key="IntegrationResponseId";filterid=key
elif type == "aws_apigatewayv2_model":
    clfn="apigatewayv2";descfn="get_models";topkey='Items';key="ModelId";filterid=key
elif type == "aws_apigatewayv2_route":
    clfn="apigatewayv2";descfn="get_routes";topkey='Items';key="RouteId";filterid=key
elif type == "aws_apigatewayv2_route_response":
    clfn="apigatewayv2";descfn="get_route_responses";topkey='Items';key="RouteResponseId";filterid=key
elif type == "aws_apigatewayv2_stage":
    clfn="apigatewayv2";descfn="get_stages";topkey='Items';key="StageName";filterid=key
elif type == "aws_apigatewayv2_vpc_link":
    clfn="apigatewayv2";descfn="get_vpc_links";topkey='Items';key="VpcLinkId";filterid=key
elif type == "aws_app_cookie_stickiness_policy":
    clfn="elb";descfn="describe_load_balancers";topkey='LoadBalancerDescriptions';key="AppCookieStickinessPolicyNames";filterid=key
elif type == "aws_appautoscaling_policy":
    clfn="appautoscaling";descfn="describe_scaling_policies";topkey='ScalingPolicies';key="PolicyName";filterid=key
elif type == "aws_appautoscaling_scheduled_action":
    clfn="appautoscaling";descfn="describe_scheduled_actions";topkey='ScheduledActions';key="ScheduledActionName";filterid=key
elif type == "aws_appautoscaling_target":
    clfn="appautoscaling";descfn="describe_scaling_targets";topkey='ScalingTargets';key="ResourceId";filterid=key
elif type == "aws_appconfig_application":
    clfn="appconfig";descfn="list_applications";topkey='Items';key="Id";filterid=key
elif type == "aws_appconfig_configuration_profile":
    clfn="appconfig";descfn="list_configuration_profiles";topkey='Items';key="Id";filterid=key
elif type == "aws_appconfig_deployment":
    clfn="appconfig";descfn="list_deployments";topkey='Items';key="Id";filterid=key
elif type == "aws_appconfig_deployment_strategy":
    clfn="appconfig";descfn="list_deployment_strategies";topkey='Items';key="Id";filterid=key
elif type == "aws_appconfig_environment":
    clfn="appconfig";descfn="list_environments";topkey='Items';key="Id";filterid=key
elif type == "aws_appconfig_extension":
    clfn="appconfig";descfn="list_extensions";topkey='Items';key="Id";filterid=key
elif type == "aws_appconfig_extension_association":
    clfn="appconfig";descfn="list_extension_associations";topkey='Items';key="Id";filterid=key
elif type == "aws_appconfig_hosted_configuration_version":
    clfn="appconfig";descfn="list_hosted_configuration_versions";topkey='Items';key="Id";filterid=key
elif type == "aws_appflow_connector_profile":
    clfn="appflow";descfn="list_connector_profiles";topkey='ConnectorProfileDetailsList';key="ConnectorProfileName";filterid=key
elif type == "aws_appflow_flow":
    clfn="appflow";descfn="list_flows";topkey='Flows';key="FlowName";filterid=key
elif type == "aws_appintegrations_data_integration":
    clfn="appintegrations";descfn="list_data_integrations";topkey='DataIntegrations';key="Name";filterid=key
elif type == "aws_appintegrations_event_integration":
    clfn="appintegrations";descfn="list_event_integrations";topkey='EventIntegrations';key="Name";filterid=key
elif type == "aws_applicationinsights_application":
    clfn="applicationinsights";descfn="list_applications";topkey='ApplicationInfoList';key="Name";filterid=key
elif type == "aws_appmesh_gateway_route":
    clfn="appmesh";descfn="list_gateway_routes";topkey='GatewayRoutes';key="GatewayRouteName";filterid=key
elif type == "aws_appmesh_mesh":
    clfn="appmesh";descfn="list_meshes";topkey='Meshes';key="MeshName";filterid=key
elif type == "aws_appmesh_route":
    clfn="appmesh";descfn="list_routes";topkey='Routes';key="RouteName";filterid=key
elif type == "aws_appmesh_virtual_gateway":
    clfn="appmesh";descfn="list_virtual_gateways";topkey='VirtualGateways';key="VirtualGatewayName";filterid=key
elif type == "aws_appmesh_virtual_node":
    clfn="appmesh";descfn="list_virtual_nodes";topkey='VirtualNodes';key="VirtualNodeName";filterid=key
elif type == "aws_appmesh_virtual_router":
    clfn="appmesh";descfn="list_virtual_routers";topkey='VirtualRouters';key="VirtualRouterName";filterid=key
elif type == "aws_appmesh_virtual_service":
    clfn="appmesh";descfn="list_virtual_services";topkey='VirtualServices';key="VirtualServiceName";filterid=key
elif type == "aws_apprunner_auto_scaling_configuration_ver=":
    clfn="apprunner";descfn="list_auto_scaling_configuration_versions";topkey='AutoScalingConfigurationVersions';key="AutoScalingConfigurationVersionArn";filterid=key
elif type == "aws_apprunner_connection":
    clfn="apprunner";descfn="list_connections";topkey='Connections';key="ConnectionArn";filterid=key
elif type == "aws_apprunner_custom_domain_association":
    clfn="apprunner";descfn="list_custom_domain_associations";topkey='CustomDomainAssociations';key="CustomDomainAssociationArn";filterid=key
elif type == "aws_apprunner_default_auto_scaling_configura=":
    clfn="apprunner";descfn="list_default_auto_scaling_configurations";topkey='DefaultAutoScalingConfigurations';key="DefaultAutoScalingConfigurationArn";filterid=key
elif type == "aws_apprunner_observability_configuration":
    clfn="apprunner";descfn="list_observability_configurations";topkey='ObservabilityConfigurations';key="ObservabilityConfigurationArn";filterid=key
elif type == "aws_apprunner_service":
    clfn="apprunner";descfn="list_services";topkey='Services';key="ServiceArn";filterid=key
elif type == "aws_apprunner_vpc_connector":
    clfn="apprunner";descfn="list_vpc_connectors";topkey='VpcConnectors';key="VpcConnectorArn";filterid=key
elif type == "aws_apprunner_vpc_ingress_connection":
    clfn="apprunner";descfn="list_vpc_ingress_connections";topkey='VpcIngressConnections';key="VpcIngressConnectionArn";filterid=key
elif type == "aws_appstream_directory_config":
    clfn="appstream";descfn="list_directory_configs";topkey='DirectoryConfigs';key="DirectoryName";filterid=key
elif type == "aws_appstream_fleet":
    clfn="appstream";descfn="list_fleets";topkey='Fleets';key="Name";filterid=key
elif type == "aws_appstream_fleet_stack_association":
    clfn="appstream";descfn="list_fleet_stack_associations";topkey='FleetStackAssociations';key="FleetName";filterid=key
elif type == "aws_appstream_image_builder":
    clfn="appstream";descfn="list_image_builders";topkey='ImageBuilders';key="Name";filterid=key
elif type == "aws_appstream_stack":
    clfn="appstream";descfn="list_stacks";topkey='Stacks';key="Name";filterid=key
elif type == "aws_appstream_user":
    clfn="appstream";descfn="list_users";topkey='Users';key="UserName";filterid=key
elif type == "aws_appstream_user_stack_association":
    clfn="appstream";descfn="list_user_stack_associations";topkey='UserStackAssociations';key="UserName";filterid=key
elif type == "aws_appsync_api_cache":
    clfn="appsync";descfn="list_api_caches";topkey='ApiCaches';key="ApiCacheName";filterid=key
elif type == "aws_appsync_api_key":
    clfn="appsync";descfn="list_api_keys";topkey='ApiKeys';key="ApiKeyId";filterid=key
elif type == "aws_appsync_datasource":
    clfn="appsync";descfn="list_data_sources";topkey='DataSources';key="DataSourceName";filterid=key
elif type == "aws_appsync_domain_name":
    clfn="appsync";descfn="list_domain_names";topkey='DomainNames';key="DomainName";filterid=key
elif type == "aws_appsync_domain_name_api_association":
    clfn="appsync";descfn="list_domain_name_api_associations";topkey='DomainNameApiAssociations';key="DomainName";filterid=key
elif type == "aws_appsync_function":
    clfn="appsync";descfn="list_functions";topkey='Functions';key="FunctionId";filterid=key
elif type == "aws_appsync_graphql_api":
    clfn="appsync";descfn="list_graphql_apis";topkey='GraphqlApis';key="ApiId";filterid=key
elif type == "aws_appsync_resolver":
    clfn="appsync";descfn="list_resolvers";topkey='Resolvers';key="ResolverArn";filterid=key
elif type == "aws_appsync_type":
    clfn="appsync";descfn="list_types";topkey='Types';key="TypeName";filterid=key

elif type == "aws_athena_data_catalog":
    clfn="athena";descfn="list_data_catalogs";topkey='DataCatalogs';key="Name";filterid=key
elif type == "aws_athena_database":
    clfn="athena";descfn="list_databases";topkey='Databases';key="Name";filterid=key
elif type == "aws_athena_named_query":
    clfn="athena";descfn="list_named_queries";topkey='NamedQueries';key="NamedQueryId";filterid=key
elif type == "aws_athena_prepared_statement":
    clfn="athena";descfn="list_prepared_statements";topkey='PreparedStatements';key="PreparedStatementName";filterid=key
elif type == "aws_athena_workgroup":
    clfn="athena";descfn="list_work_groups";topkey='WorkGroups';key="Name";filterid=key
elif type == "aws_auditmanager_account_registration":
    clfn="auditmanager";descfn="list_account_registrations";topkey='AccountRegistrations';key="Id";filterid=key
elif type == "aws_auditmanager_assessment":
    clfn="auditmanager";descfn="list_assessments";topkey='Assessments';key="Id";filterid=key
elif type == "aws_auditmanager_assessment_delegation":
    clfn="auditmanager";descfn="list_assessment_delegations";topkey='AssessmentDelegations';key="Id";filterid=key
elif type == "aws_auditmanager_assessment_report":
    clfn="auditmanager";descfn="list_assessment_reports";topkey='AssessmentReports';key="Id";filterid=key
elif type == "aws_auditmanager_control":
    clfn="auditmanager";descfn="list_controls";topkey='Controls';key="Id";filterid=key
elif type == "aws_auditmanager_framework":
    clfn="auditmanager";descfn="list_frameworks";topkey='Frameworks';key="Id";filterid=key
elif type == "aws_auditmanager_framework_share":
    clfn="auditmanager";descfn="list_framework_shares";topkey='FrameworkShares';key="Id";filterid=key
elif type == "aws_auditmanager_organization_admin_account_=":
    clfn="auditmanager";descfn="list_organization_admin_accounts";topkey='OrganizationAdminAccounts';key="Id";filterid=key
elif type == "aws_autoscaling_attachment":
    clfn="autoscaling";descfn="list_attachments";topkey='Attachments';key="AttachmentName";filterid=key
elif type == "aws_autoscaling_group":
    clfn="autoscaling";descfn="list_groups";topkey='Groups';key="AutoScalingGroupName";filterid=key
elif type == "aws_autoscaling_group_tag":
    clfn="autoscaling";descfn="list_tags";topkey='Tags';key="ResourceId";filterid=key
elif type == "aws_autoscaling_lifecycle_hook":
    clfn="autoscaling";descfn="list_lifecycle_hooks";topkey='LifecycleHooks';key="LifecycleHookName";filterid=key
elif type == "aws_autoscaling_notification":
    clfn="autoscaling";descfn="list_notifications";topkey='Notifications';key="TopicARN";filterid=key
elif type == "aws_autoscaling_policy":
    clfn="autoscaling";descfn="list_policies";topkey='Policies';key="PolicyName";filterid=key
elif type == "aws_autoscaling_schedule":
    clfn="autoscaling";descfn="list_schedules";topkey='Schedules';key="ScheduleName";filterid=key
elif type == "aws_autoscaling_traffic_source_attachment":
    clfn="autoscaling";descfn="list_traffic_source_attachments";topkey='TrafficSourceAttachments';key="TrafficSourceAttachmentName";filterid=key
elif type == "aws_autoscalingplans_scaling_plan":
    clfn="autoscalingplans";descfn="list_scaling_plans";topkey='ScalingPlans';key="ScalingPlanName";filterid=key
elif type == "aws_backup_framework":
    clfn="backup";descfn="list_frameworks";topkey='Frameworks';key="FrameworkName";filterid=key
elif type == "aws_backup_global_settings":
    clfn="backup";descfn="list_global_settings";topkey='GlobalSettings';key="GlobalSettingsName";filterid=key
elif type == "aws_backup_plan":
    clfn="backup";descfn="list_plans";topkey='Plans';key="PlanName";filterid=key
elif type == "aws_backup_region_settings":
    clfn="backup";descfn="list_region_settings";topkey='RegionSettings';key="RegionSettingsName";filterid=key
elif type == "aws_backup_report_plan":
    clfn="backup";descfn="list_report_plans";topkey='ReportPlans';key="ReportPlanName";filterid=key
elif type == "aws_backup_selection":
    clfn="backup";descfn="list_selections";topkey='Selections';key="SelectionName";filterid=key
elif type == "aws_backup_vault":
    clfn="backup";descfn="list_vaults";topkey='Vaults';key="VaultName";filterid=key
elif type == "aws_backup_vault_lock_configuration":
    clfn="backup";descfn="list_vault_lock_configuration";topkey='VaultLockConfiguration';key="VaultLockConfigurationName";filterid=key
elif type == "aws_backup_vault_notifications":
    clfn="backup";descfn="list_vault_notifications";topkey='VaultNotifications';key="VaultNotificationsName";filterid=key
elif type == "aws_backup_vault_policy":
    clfn="backup";descfn="list_vault_policies";topkey='VaultPolicies';key="VaultName";filterid=key
elif type == "aws_batch_compute_environment":
    clfn="batch";descfn="list_compute_environments";topkey='ComputeEnvironments';key="ComputeEnvironmentName";filterid=key
elif type == "aws_batch_job_definition":
    clfn="batch";descfn="list_job_definitions";topkey='JobDefinitions';key="JobDefinitionName";filterid=key
elif type == "aws_batch_job_queue":
    clfn="batch";descfn="list_job_queues";topkey='JobQueues';key="JobQueueName";filterid=key
elif type == "aws_batch_scheduling_policy":
    clfn="batch";descfn="list_scheduling_policies";topkey='SchedulingPolicies';key="SchedulingPolicyName";filterid=key
elif type == "aws_bedrock_model_invocation_logging_configuration":
    clfn="bedrock";descfn="list_model_invocation_logging_configurations";topkey='ModelInvocationLoggingConfigurations';key="ModelInvocationLoggingConfigurationName";filterid=key
elif type == "aws_billing_service_account":
    clfn="billing";descfn="list_service_accounts";topkey='ServiceAccounts';key="ServiceAccountId";filterid=key
elif type == "aws_budgets_budget":
    clfn="budgets";descfn="list_budgets";topkey='Budgets';key="BudgetName";filterid=key
elif type == "aws_budgets_budget_action":
    clfn="budgets";descfn="list_budget_actions";topkey='BudgetActions';key="ActionId";filterid=key
elif type == "aws_caller_identity":
    clfn="sts";descfn="get_caller_identity";topkey='UserId';key="UserId";filterid=key
elif type == "aws_canonical_user_id":
    clfn="sts";descfn="get_caller_identity";topkey='UserId';key="UserId";filterid=key
elif type == "aws_ce_anomaly_monitor":
    clfn="ce";descfn="list_anomaly_monitors";topkey='AnomalyMonitors';key="MonitorName";filterid=key
elif type == "aws_ce_anomaly_subscription":
    clfn="ce";descfn="list_anomaly_subscriptions";topkey='AnomalySubscriptions';key="SubscriptionName";filterid=key
elif type == "aws_ce_cost_allocation_tag":
    clfn="ce";descfn="list_cost_allocation_tags";topkey='CostAllocationTags';key="CostAllocationTagKey";filterid=key
elif type == "aws_ce_cost_category":
    clfn="ce";descfn="list_cost_categories";topkey='CostCategories';key="CostCategoryArn";filterid=key
elif type == "aws_chime_voice_connector":
elif type == "aws_chime_voice_connector_group":
elif type == "aws_chime_voice_connector_logging":
elif type == "aws_chime_voice_connector_origination":
elif type == "aws_chime_voice_connector_streaming":
elif type == "aws_chime_voice_connector_termination":
elif type == "aws_chime_voice_connector_termination_creden=":
elif type == "aws_chimesdkmediapipelines_media_insights_pipelin=":
elif type == "aws_chimesdkvoice_global_settings":
elif type == "aws_chimesdkvoice_sip_media_application":
elif type == "aws_chimesdkvoice_sip_rule":
elif type == "aws_chimesdkvoice_voice_profile_domain":
elif type == "aws_cleanrooms_collaboration":
elif type == "aws_cleanrooms_configured_table":
elif type == "aws_cloud9_environment_ec2":
elif type == "aws_cloud9_environment_membership":
elif type == "aws_cloudcontrolapi_resource":
elif type == "aws_cloudformation_stack":
elif type == "aws_cloudformation_stack_set":
elif type == "aws_cloudformation_stack_set_instance":
elif type == "aws_cloudformation_type":
elif type == "aws_cloudfront_cache_policy":
elif type == "aws_cloudfront_continuous_deployment_policy":
elif type == "aws_cloudfront_distribution":
elif type == "aws_cloudfront_field_level_encryption_config":
elif type == "aws_cloudfront_field_level_encryption_profil=":
elif type == "aws_cloudfront_function":
elif type == "aws_cloudfront_key_group":
elif type == "aws_cloudfront_monitoring_subscription":
elif type == "aws_cloudfront_origin_access_control":
elif type == "aws_cloudfront_origin_access_identities":
elif type == "aws_cloudfront_origin_access_identity":
elif type == "aws_cloudfront_origin_request_policy":
elif type == "aws_cloudfront_public_key":
elif type == "aws_cloudfront_realtime_log_config":
elif type == "aws_cloudfront_response_headers_policy":
elif type == "aws_cloudhsm_v2_cluster":
elif type == "aws_cloudhsm_v2_hsm":
elif type == "aws_cloudsearch_domain":
elif type == "aws_cloudsearch_domain_service_access_policy":
elif type == "aws_cloudtrail":
elif type == "aws_cloudtrail_event_data_store":
elif type == "aws_cloudwatch_composite_alarm":
elif type == "aws_cloudwatch_dashboard":
elif type == "aws_cloudwatch_event_api_destination":
elif type == "aws_cloudwatch_event_archive":
elif type == "aws_cloudwatch_event_bus":
elif type == "aws_cloudwatch_event_bus_policy":
elif type == "aws_cloudwatch_event_connection":
elif type == "aws_cloudwatch_event_endpoint":
elif type == "aws_cloudwatch_event_permission":
elif type == "aws_cloudwatch_event_rule":
elif type == "aws_cloudwatch_event_source":
elif type == "aws_cloudwatch_event_target":
elif type == "aws_cloudwatch_log_data_protection_policy":
elif type == "aws_cloudwatch_log_destination":
elif type == "aws_cloudwatch_log_destination_policy":
elif type == "aws_cloudwatch_log_group":
elif type == "aws_cloudwatch_log_metric_filter":
elif type == "aws_cloudwatch_log_resource_policy":
elif type == "aws_cloudwatch_log_stream":
elif type == "aws_cloudwatch_log_subscription_filter":
elif type == "aws_cloudwatch_metric_alarm":
elif type == "aws_cloudwatch_metric_stream":
elif type == "aws_cloudwatch_query_definition":
elif type == "aws_codeartifact_domain":
elif type == "aws_codeartifact_domain_permissions_policy":
elif type == "aws_codeartifact_repository":
elif type == "aws_codeartifact_repository_permissions_policy":
elif type == "aws_codebuild_project":
elif type == "aws_codebuild_report_group":
elif type == "aws_codebuild_resource_policy":
elif type == "aws_codebuild_source_credential":
elif type == "aws_codebuild_webhook":
elif type == "aws_codecatalyst_dev_environment":
elif type == "aws_codecatalyst_project":
elif type == "aws_codecatalyst_source_repository":
elif type == "aws_codecommit_approval_rule_template":
elif type == "aws_codecommit_approval_rule_template_associ=":
elif type == "aws_codecommit_repository":
elif type == "aws_codecommit_trigger":
elif type == "aws_codedeploy_app":
elif type == "aws_codedeploy_deployment_config":
elif type == "aws_codedeploy_deployment_group":
elif type == "aws_codeguruprofiler_profiling_group":
elif type == "aws_codegurureviewer_repository_association":
elif type == "aws_codepipeline":
elif type == "aws_codepipeline_custom_action_type":
elif type == "aws_codepipeline_webhook":
elif type == "aws_codestarconnections_connection":
elif type == "aws_codestarconnections_host":
elif type == "aws_codestarnotifications_notification_rule":
elif type == "aws_cognito_identity_pool":
elif type == "aws_cognito_identity_pool_provider_principal=":
elif type == "aws_cognito_identity_pool_roles_attachment":
elif type == "aws_cognito_identity_provider":
elif type == "aws_cognito_managed_user_pool_client":
elif type == "aws_cognito_resource_server":
elif type == "aws_cognito_risk_configuration":
elif type == "aws_cognito_user":
elif type == "aws_cognito_user_group":
elif type == "aws_cognito_user_in_group":
elif type == "aws_cognito_user_pool":
elif type == "aws_cognito_user_pool_client":
elif type == "aws_cognito_user_pool_domain":
elif type == "aws_cognito_user_pool_ui_customization":
elif type == "aws_comprehend_document_classifier":
elif type == "aws_comprehend_entity_recognizer":
elif type == "aws_config_aggregate_authorization":
elif type == "aws_config_config_rule":
elif type == "aws_config_configuration_aggregator":
elif type == "aws_config_configuration_recorder":
elif type == "aws_config_configuration_recorder_status":
elif type == "aws_config_conformance_pack":
elif type == "aws_config_delivery_channel":
elif type == "aws_config_organization_conformance_pack":
elif type == "aws_config_organization_custom_policy_rule":
elif type == "aws_config_organization_custom_rule":
elif type == "aws_config_organization_managed_rule":
elif type == "aws_config_remediation_configuration":
elif type == "aws_connect_bot_association":
elif type == "aws_connect_contact_flow":
elif type == "aws_connect_contact_flow_module":
elif type == "aws_connect_hours_of_operation":
elif type == "aws_connect_instance":
elif type == "aws_connect_instance_storage_config":
elif type == "aws_connect_lambda_function_association":
elif type == "aws_connect_phone_number":
elif type == "aws_connect_queue":
elif type == "aws_connect_quick_connect":
elif type == "aws_connect_routing_profile":
elif type == "aws_connect_security_profile":
elif type == "aws_connect_user":
elif type == "aws_connect_user_hierarchy_group":
elif type == "aws_connect_user_hierarchy_structure":
elif type == "aws_connect_vocabulary":
elif type == "aws_controltower_control":
elif type == "aws_cur_report_definition":
elif type == "aws_customer_gateway":
elif type == "aws_customerprofiles_domain":
elif type == "aws_customerprofiles_profile":
elif type == "aws_dataexchange_data_set":
elif type == "aws_dataexchange_revision":
elif type == "aws_datapipeline_pipeline":
elif type == "aws_datapipeline_pipeline_definition":
elif type == "aws_datasync_agent":
elif type == "aws_datasync_location_azure_blob":
elif type == "aws_datasync_location_efs":
elif type == "aws_datasync_location_fsx_lustre_file_s=":
elif type == "aws_datasync_location_fsx_ontap_file_sy=":
elif type == "aws_datasync_location_fsx_openzfs_file_=":
elif type == "aws_datasync_location_fsx_windows_file_=":
elif type == "aws_datasync_location_hdfs":
elif type == "aws_datasync_location_nfs":
elif type == "aws_datasync_location_object_storage":
elif type == "aws_datasync_location_s3":
elif type == "aws_datasync_location_smb":
elif type == "aws_datasync_task":
elif type == "aws_dax_cluster":
elif type == "aws_dax_parameter_group":
elif type == "aws_dax_subnet_group":
elif type == "aws_db_cluster_snapshot":
elif type == "aws_db_event_categories":
elif type == "aws_db_event_subscription":
elif type == "aws_db_instance":

elif type == "aws_db_instance_automated_backups_replicatio=":
elif type == "aws_db_instance_role_association":
elif type == "aws_db_instances":
elif type == "aws_db_option_group":
elif type == "aws_db_parameter_group":
elif type == "aws_db_proxy":
elif type == "aws_db_proxy_default_target_group":
elif type == "aws_db_proxy_endpoint":
elif type == "aws_db_proxy_target":
elif type == "aws_db_snapshot":
elif type == "aws_db_snapshot_copy":
elif type == "aws_db_subnet_group":
elif type == "aws_default_network_acl":
elif type == "aws_default_route_table":
elif type == "aws_default_security_group":
elif type == "aws_default_subnet":
elif type == "aws_default_tags":
elif type == "aws_default_vpc":
elif type == "aws_default_vpc_dhcp_options":
elif type == "aws_detective_graph":
elif type == "aws_detective_invitation_accepter":
elif type == "aws_detective_member":
elif type == "aws_detective_organization_admin_account":
elif type == "aws_detective_organization_configuration":
elif type == "aws_devicefarm_device_pool":
elif type == "aws_devicefarm_instance_profile":
elif type == "aws_devicefarm_network_profile":
elif type == "aws_devicefarm_project":
elif type == "aws_devicefarm_test_grid_project":
elif type == "aws_devicefarm_upload":
elif type == "aws_directory_service_conditional_forwarder":
elif type == "aws_directory_service_directory":
elif type == "aws_directory_service_log_subscription":
elif type == "aws_directory_service_radius_settings":
elif type == "aws_directory_service_region":
elif type == "aws_directory_service_shared_directory":
elif type == "aws_directory_service_shared_directory_accep=":
elif type == "aws_directory_service_trust":
elif type == "aws_dlm_lifecycle_policy":
elif type == "aws_dms_certificate":
elif type == "aws_dms_endpoint":
elif type == "aws_dms_event_subscription":
elif type == "aws_dms_replication_config":
elif type == "aws_dms_replication_instance":
elif type == "aws_dms_replication_subnet_group":
elif type == "aws_dms_replication_task":
elif type == "aws_dms_s3_endpoint":
elif type == "aws_docdb_cluster":
elif type == "aws_docdb_cluster_instance":
elif type == "aws_docdb_cluster_parameter_group":
elif type == "aws_docdb_cluster_snapshot":
elif type == "aws_docdb_event_subscription":
elif type == "aws_docdb_global_cluster":
elif type == "aws_docdb_subnet_group":
elif type == "aws_docdbelastic_cluster":
elif type == "aws_dx_bgp_peer":
elif type == "aws_dx_connection":
elif type == "aws_dx_connection_association":
elif type == "aws_dx_connection_confirmation":
elif type == "aws_dx_gateway":
elif type == "aws_dx_gateway_association":
elif type == "aws_dx_gateway_association_proposal":
elif type == "aws_dx_hosted_connection":
elif type == "aws_dx_hosted_private_virtual_interface":
elif type == "aws_dx_hosted_private_virtual_interface_<wbr=":
elif type == "aws_dx_hosted_public_virtual_interface":
elif type == "aws_dx_hosted_public_virtual_interface_=":
elif type == "aws_dx_hosted_transit_virtual_interface":
elif type == "aws_dx_hosted_transit_virtual_interface_<wbr=":
elif type == "aws_dx_lag":
elif type == "aws_dx_macsec_key_association":
elif type == "aws_dx_private_virtual_interface":
elif type == "aws_dx_public_virtual_interface":
elif type == "aws_dx_transit_virtual_interface":
elif type == "aws_dynamodb_contributor_insights":
elif type == "aws_dynamodb_global_table":
elif type == "aws_dynamodb_kinesis_streaming_destination":
elif type == "aws_dynamodb_table":
elif type == "aws_dynamodb_table_item":
elif type == "aws_dynamodb_table_replica":
elif type == "aws_dynamodb_tag":
elif type == "aws_ebs_default_kms_key":
elif type == "aws_ebs_encryption_by_default":
elif type == "aws_ebs_snapshot":
elif type == "aws_ebs_snapshot_copy":
elif type == "aws_ebs_snapshot_import":
elif type == "aws_ebs_volume":
elif type == "aws_ec2_availability_zone_group":
elif type == "aws_ec2_capacity_reservation":
elif type == "aws_ec2_carrier_gateway":
elif type == "aws_ec2_client_vpn_authorization_rule":
elif type == "aws_ec2_client_vpn_endpoint":
elif type == "aws_ec2_client_vpn_network_association":
elif type == "aws_ec2_client_vpn_route":
elif type == "aws_ec2_coip_pool":
elif type == "aws_ec2_fleet":
elif type == "aws_ec2_host":
elif type == "aws_ec2_image_block_public_access":
elif type == "aws_ec2_instance_connect_endpoint":
elif type == "aws_ec2_instance_state":
elif type == "aws_ec2_local_gateway":
elif type == "aws_ec2_local_gateway_route":
elif type == "aws_ec2_local_gateway_route_table":
elif type == "aws_ec2_local_gateway_route_table_vpc_<=":
elif type == "aws_ec2_local_gateway_route_tables":
elif type == "aws_ec2_local_gateway_virtual_interface":
elif type == "aws_ec2_local_gateway_virtual_interface_<wbr=":
elif type == "aws_ec2_local_gateways":
elif type == "aws_ec2_managed_prefix_list":
elif type == "aws_ec2_managed_prefix_list_entry":
elif type == "aws_ec2_managed_prefix_lists":
elif type == "aws_ec2_subnet_cidr_reservation":
elif type == "aws_ec2_tag":
elif type == "aws_ec2_traffic_mirror_filter":
elif type == "aws_ec2_traffic_mirror_filter_rule":
elif type == "aws_ec2_traffic_mirror_session":
elif type == "aws_ec2_traffic_mirror_target":
elif type == "aws_ec2_transit_gateway":
elif type == "aws_ec2_transit_gateway_attachment":
elif type == "aws_ec2_transit_gateway_attachments":
elif type == "aws_ec2_transit_gateway_connect":
elif type == "aws_ec2_transit_gateway_connect_peer":
elif type == "aws_ec2_transit_gateway_dx_gateway_atta=":
elif type == "aws_ec2_transit_gateway_multicast_domain":
elif type == "aws_ec2_transit_gateway_multicast_domain_<wb=":
elif type == "aws_ec2_transit_gateway_multicast_group_<wbr=":
elif type == "aws_ec2_transit_gateway_peering_attachment":
elif type == "aws_ec2_transit_gateway_peering_attachment_<=":
elif type == "aws_ec2_transit_gateway_policy_table":
elif type == "aws_ec2_transit_gateway_policy_table_as=":
elif type == "aws_ec2_transit_gateway_prefix_list_ref=":
elif type == "aws_ec2_transit_gateway_route":
elif type == "aws_ec2_transit_gateway_route_table":
elif type == "aws_ec2_transit_gateway_route_table_ass=":
elif type == "aws_ec2_transit_gateway_route_table_pro=":
elif type == "aws_ec2_transit_gateway_route_table_rou=":
elif type == "aws_ec2_transit_gateway_route_tables":
elif type == "aws_ec2_transit_gateway_vpc_attachment":
elif type == "aws_ec2_transit_gateway_vpc_attachment_=":
elif type == "aws_ec2_transit_gateway_vpc_attachments":
elif type == "aws_ec2_transit_gateway_vpn_attachment":
elif type == "aws_ecr_authorization_token":
elif type == "aws_ecr_image":
elif type == "aws_ecr_lifecycle_policy":
elif type == "aws_ecr_pull_through_cache_rule":
elif type == "aws_ecr_registry_policy":
elif type == "aws_ecr_registry_scanning_configuration":
elif type == "aws_ecr_replication_configuration":
elif type == "aws_ecr_repositories":
elif type == "aws_ecr_repository":
elif type == "aws_ecr_repository_policy":
elif type == "aws_ecrpublic_authorization_token":
elif type == "aws_ecrpublic_repository":
elif type == "aws_ecrpublic_repository_policy":
elif type == "aws_ecs_account_setting_default":
elif type == "aws_ecs_capacity_provider":
elif type == "aws_ecs_cluster":
elif type == "aws_ecs_cluster_capacity_providers":
elif type == "aws_ecs_container_definition":
elif type == "aws_ecs_service":
elif type == "aws_ecs_tag":
elif type == "aws_ecs_task_definition":
elif type == "aws_ecs_task_execution":
elif type == "aws_ecs_task_set":
elif type == "aws_efs_access_point":
elif type == "aws_efs_backup_policy":
elif type == "aws_efs_file_system":
elif type == "aws_efs_file_system_policy":
elif type == "aws_efs_mount_target":
elif type == "aws_efs_replication_configuration":
elif type == "aws_egress_only_internet_gateway":
elif type == "aws_eip":
elif type == "aws_eip_association":
elif type == "aws_eks_addon":
elif type == "aws_eks_addon_version":
elif type == "aws_eks_cluster":
elif type == "aws_eks_cluster_auth":
elif type == "aws_eks_fargate_profile":
elif type == "aws_eks_identity_provider_config":
elif type == "aws_eks_node_group":
elif type == "aws_eks_pod_identity_association":
elif type == "aws_elastic_beanstalk_application":
elif type == "aws_elastic_beanstalk_application_version":
elif type == "aws_elastic_beanstalk_configuration_template":
elif type == "aws_elastic_beanstalk_environment":
elif type == "aws_elastic_beanstalk_hosted_zone":
elif type == "aws_elastic_beanstalk_solution_stack":
elif type == "aws_elasticache_cluster":
elif type == "aws_elasticache_global_replication_group":
elif type == "aws_elasticache_parameter_group":
elif type == "aws_elasticache_replication_group":
elif type == "aws_elasticache_subnet_group":
elif type == "aws_elasticache_user":
elif type == "aws_elasticache_user_group":
elif type == "aws_elasticache_user_group_association":
elif type == "aws_elasticsearch_domain":
elif type == "aws_elasticsearch_domain_policy":
elif type == "aws_elasticsearch_domain_saml_options":
elif type == "aws_elasticsearch_vpc_endpoint":
elif type == "aws_elastictranscoder_pipeline":
elif type == "aws_elastictranscoder_preset":
elif type == "aws_elb":
elif type == "aws_elb_attachment":
elif type == "aws_elb_hosted_zone_id":
elif type == "aws_elb_service_account":
elif type == "aws_emr_block_public_access_configuration":
elif type == "aws_emr_cluster":
elif type == "aws_emr_instance_fleet":
elif type == "aws_emr_instance_group":
elif type == "aws_emr_managed_scaling_policy":
elif type == "aws_emr_release_labels":
elif type == "aws_emr_security_configuration":
elif type == "aws_emr_studio":
elif type == "aws_emr_studio_session_mapping":
elif type == "aws_emr_supported_instance_types":
elif type == "aws_emrcontainers_job_template":
elif type == "aws_emrcontainers_virtual_cluster":
elif type == "aws_emrserverless_application":
elif type == "aws_evidently_feature":
elif type == "aws_evidently_launch":
elif type == "aws_evidently_project":
elif type == "aws_evidently_segment":
elif type == "aws_finspace_kx_cluster":
elif type == "aws_finspace_kx_database":
elif type == "aws_finspace_kx_dataview":
elif type == "aws_finspace_kx_environment":
elif type == "aws_finspace_kx_scaling_group":
elif type == "aws_finspace_kx_user":
elif type == "aws_finspace_kx_volume":
elif type == "aws_fis_experiment_template":
elif type == "aws_flow_log":
elif type == "aws_fms_admin_account":
elif type == "aws_fms_policy":
elif type == "aws_fsx_backup":
elif type == "aws_fsx_data_repository_association":
elif type == "aws_fsx_file_cache":
elif type == "aws_fsx_lustre_file_system":
elif type == "aws_fsx_ontap_file_system":
elif type == "aws_fsx_ontap_storage_virtual_machine":
elif type == "aws_fsx_ontap_storage_virtual_machines":
elif type == "aws_fsx_ontap_volume":
elif type == "aws_fsx_openzfs_file_system":
elif type == "aws_fsx_openzfs_snapshot":
elif type == "aws_fsx_openzfs_volume":
elif type == "aws_fsx_windows_file_system":
elif type == "aws_gamelift_alias":
elif type == "aws_gamelift_build":
elif type == "aws_gamelift_fleet":
elif type == "aws_gamelift_game_server_group":
elif type == "aws_gamelift_game_session_queue":
elif type == "aws_gamelift_script":
elif type == "aws_glacier_vault":
elif type == "aws_glacier_vault_lock":
elif type == "aws_globalaccelerator_accelerator":
elif type == "aws_globalaccelerator_custom_routing_accelerator":
elif type == "aws_globalaccelerator_custom_routing_endpoint_<wb=":
elif type == "aws_globalaccelerator_custom_routing_listener":
elif type == "aws_globalaccelerator_endpoint_group":
elif type == "aws_globalaccelerator_listener":
elif type == "aws_glue_catalog_database":
elif type == "aws_glue_catalog_table":
elif type == "aws_glue_classifier":
elif type == "aws_glue_connection":
elif type == "aws_glue_crawler":
elif type == "aws_glue_data_catalog_encryption_settings":
elif type == "aws_glue_data_quality_ruleset":
elif type == "aws_glue_dev_endpoint":
elif type == "aws_glue_job":
elif type == "aws_glue_ml_transform":
elif type == "aws_glue_partition":
elif type == "aws_glue_partition_index":
elif type == "aws_glue_registry":
elif type == "aws_glue_resource_policy":
elif type == "aws_glue_schema":
elif type == "aws_glue_script":
elif type == "aws_glue_security_configuration":
elif type == "aws_glue_trigger":
elif type == "aws_glue_user_defined_function":
elif type == "aws_glue_workflow":
elif type == "aws_grafana_license_association":
elif type == "aws_grafana_role_association":
elif type == "aws_grafana_workspace":
elif type == "aws_grafana_workspace_api_key":
elif type == "aws_grafana_workspace_saml_configuration":
elif type == "aws_guardduty_detector":
elif type == "aws_guardduty_detector_feature":
elif type == "aws_guardduty_filter":
elif type == "aws_guardduty_finding_ids":
elif type == "aws_guardduty_invite_accepter":
elif type == "aws_guardduty_ipset":
elif type == "aws_guardduty_member":
elif type == "aws_guardduty_organization_admin_account":
elif type == "aws_guardduty_organization_configuration":
elif type == "aws_guardduty_organization_configuration_feature":
elif type == "aws_guardduty_publishing_destination":
elif type == "aws_guardduty_threatintelset":
elif type == "aws_iam_access_key":
elif type == "aws_iam_access_keys":
elif type == "aws_iam_account_alias":
elif type == "aws_iam_account_password_policy":
elif type == "aws_iam_group":
elif type == "aws_iam_group_membership":
elif type == "aws_iam_group_policy":
elif type == "aws_iam_group_policy_attachment":
elif type == "aws_iam_instance_profile":
elif type == "aws_iam_instance_profiles":
elif type == "aws_iam_openid_connect_provider":
elif type == "aws_iam_policy":
elif type == "aws_iam_policy_attachment":
elif type == "aws_iam_policy_document":

elif type == "aws_iam_principal_policy_simulation":
elif type == "aws_iam_role":
elif type == "aws_iam_role_policy":
elif type == "aws_iam_role_policy_attachment":
elif type == "aws_iam_roles":
elif type == "aws_iam_saml_provider":
elif type == "aws_iam_security_token_service_preferences":
elif type == "aws_iam_server_certificate":
elif type == "aws_iam_service_linked_role":
elif type == "aws_iam_service_specific_credential":
elif type == "aws_iam_session_context":
elif type == "aws_iam_signing_certificate":
elif type == "aws_iam_user":
elif type == "aws_iam_user_group_membership":
elif type == "aws_iam_user_login_profile":
elif type == "aws_iam_user_policy":
elif type == "aws_iam_user_policy_attachment":
elif type == "aws_iam_user_ssh_key":
elif type == "aws_iam_users":
elif type == "aws_iam_virtual_mfa_device":
elif type == "aws_identitystore_group":
elif type == "aws_identitystore_group_membership":
elif type == "aws_identitystore_user":
elif type == "aws_imagebuilder_component":
elif type == "aws_imagebuilder_components":
elif type == "aws_imagebuilder_container_recipe":
elif type == "aws_imagebuilder_container_recipes":
elif type == "aws_imagebuilder_distribution_configuration":
elif type == "aws_imagebuilder_distribution_configurations":
elif type == "aws_imagebuilder_image":
elif type == "aws_imagebuilder_image_pipeline":
elif type == "aws_imagebuilder_image_pipelines":
elif type == "aws_imagebuilder_image_recipe":
elif type == "aws_imagebuilder_image_recipes":
elif type == "aws_imagebuilder_infrastructure_configuration":
elif type == "aws_imagebuilder_infrastructure_configurations":
elif type == "aws_inspector2_delegated_admin_account":
elif type == "aws_inspector2_enabler":
elif type == "aws_inspector2_member_association":
elif type == "aws_inspector2_organization_configuration":
elif type == "aws_inspector_assessment_target":
elif type == "aws_inspector_assessment_template":
elif type == "aws_inspector_resource_group":
elif type == "aws_inspector_rules_packages":
elif type == "aws_instance":
elif type == "aws_internet_gateway":
elif type == "aws_internet_gateway_attachment":
elif type == "aws_internetmonitor_monitor":
elif type == "aws_iot_authorizer":
elif type == "aws_iot_billing_group":
elif type == "aws_iot_ca_certificate":
elif type == "aws_iot_certificate":
elif type == "aws_iot_domain_configuration":
elif type == "aws_iot_endpoint":
elif type == "aws_iot_event_configurations":
elif type == "aws_iot_indexing_configuration":
elif type == "aws_iot_logging_options":
elif type == "aws_iot_policy":
elif type == "aws_iot_policy_attachment":
elif type == "aws_iot_provisioning_template":
elif type == "aws_iot_registration_code":
elif type == "aws_iot_role_alias":
elif type == "aws_iot_thing":
elif type == "aws_iot_thing_group":
elif type == "aws_iot_thing_group_membership":
elif type == "aws_iot_thing_principal_attachment":
elif type == "aws_iot_thing_type":
elif type == "aws_iot_topic_rule":
elif type == "aws_iot_topic_rule_destination":
elif type == "aws_ip_ranges":
elif type == "aws_ivs_channel":
elif type == "aws_ivs_playback_key_pair":
elif type == "aws_ivs_recording_configuration":
elif type == "aws_ivs_stream_key":
elif type == "aws_ivschat_logging_configuration":
elif type == "aws_ivschat_room":
elif type == "aws_kendra_data_source":
elif type == "aws_kendra_experience":
elif type == "aws_kendra_faq":
elif type == "aws_kendra_index":
elif type == "aws_kendra_query_suggestions_block_list":
elif type == "aws_kendra_thesaurus":
elif type == "aws_key_pair":
elif type == "aws_keyspaces_keyspace":
elif type == "aws_keyspaces_table":
elif type == "aws_kinesis_analytics_application":
elif type == "aws_kinesis_firehose_delivery_stream":
elif type == "aws_kinesis_stream":
elif type == "aws_kinesis_stream_consumer":
elif type == "aws_kinesis_video_stream":
elif type == "aws_kinesisanalyticsv2_application":
elif type == "aws_kinesisanalyticsv2_application_snapshot":
elif type == "aws_kms_alias":
elif type == "aws_kms_ciphertext":
elif type == "aws_kms_custom_key_store":
elif type == "aws_kms_external_key":
elif type == "aws_kms_grant":
elif type == "aws_kms_key":
elif type == "aws_kms_key_policy":
elif type == "aws_kms_public_key":
elif type == "aws_kms_replica_external_key":
elif type == "aws_kms_replica_key":
elif type == "aws_kms_secret":
elif type == "aws_kms_secrets":
elif type == "aws_lakeformation_data_lake_settings":
elif type == "aws_lakeformation_lf_tag":
elif type == "aws_lakeformation_permissions":
elif type == "aws_lakeformation_resource":
elif type == "aws_lakeformation_resource_lf_tags":
elif type == "aws_lambda_alias":
elif type == "aws_lambda_code_signing_config":
elif type == "aws_lambda_event_source_mapping":
elif type == "aws_lambda_function":
elif type == "aws_lambda_function_event_invoke_config":
elif type == "aws_lambda_function_url":
elif type == "aws_lambda_functions":
elif type == "aws_lambda_invocation":
elif type == "aws_lambda_layer_version":
elif type == "aws_lambda_layer_version_permission":
elif type == "aws_lambda_permission":
elif type == "aws_lambda_provisioned_concurrency_config":
elif type == "aws_launch_configuration":
elif type == "aws_launch_template":
elif type == "aws_lb":
elif type == "aws_lb_cookie_stickiness_policy":
elif type == "aws_lb_hosted_zone_id":
elif type == "aws_lb_listener":
elif type == "aws_lb_listener_certificate":
elif type == "aws_lb_listener_rule":
elif type == "aws_lb_ssl_negotiation_policy":
elif type == "aws_lb_target_group":
elif type == "aws_lb_target_group_attachment":
elif type == "aws_lb_trust_store":
elif type == "aws_lb_trust_store_revocation":
elif type == "aws_lbs":
elif type == "aws_lex_bot":
elif type == "aws_lex_bot_alias":
elif type == "aws_lex_intent":
elif type == "aws_lex_slot_type":
elif type == "aws_lexv2models_bot":
elif type == "aws_lexv2models_bot_locale":
elif type == "aws_lexv2models_bot_version":
elif type == "aws_licensemanager_association":
elif type == "aws_licensemanager_grant":
elif type == "aws_licensemanager_grant_accepter":
elif type == "aws_licensemanager_grants":
elif type == "aws_licensemanager_license_configuration":
elif type == "aws_licensemanager_received_license":
elif type == "aws_licensemanager_received_licenses":
elif type == "aws_lightsail_bucket":
elif type == "aws_lightsail_bucket_access_key":
elif type == "aws_lightsail_bucket_resource_access":
elif type == "aws_lightsail_certificate":
elif type == "aws_lightsail_container_service":
elif type == "aws_lightsail_container_service_deployment_v=":
elif type == "aws_lightsail_database":
elif type == "aws_lightsail_disk":
elif type == "aws_lightsail_disk_attachment":
elif type == "aws_lightsail_distribution":
elif type == "aws_lightsail_domain":
elif type == "aws_lightsail_domain_entry":
elif type == "aws_lightsail_instance":
elif type == "aws_lightsail_instance_public_ports":
elif type == "aws_lightsail_key_pair":
elif type == "aws_lightsail_lb":
elif type == "aws_lightsail_lb_attachment":
elif type == "aws_lightsail_lb_certificate":
elif type == "aws_lightsail_lb_certificate_attachment":
elif type == "aws_lightsail_lb_https_redirection_policy":
elif type == "aws_lightsail_lb_stickiness_policy":
elif type == "aws_lightsail_static_ip":
elif type == "aws_lightsail_static_ip_attachment":
elif type == "aws_load_balancer_backend_server_policy":
elif type == "aws_load_balancer_listener_policy":
elif type == "aws_load_balancer_policy":
elif type == "aws_location_geofence_collection":
elif type == "aws_location_map":
elif type == "aws_location_place_index":
elif type == "aws_location_route_calculator":
elif type == "aws_location_tracker":
elif type == "aws_location_tracker_association":
elif type == "aws_location_tracker_associations":
elif type == "aws_macie2_account":
elif type == "aws_macie2_classification_export_configuration":
elif type == "aws_macie2_classification_job":
elif type == "aws_macie2_custom_data_identifier":
elif type == "aws_macie2_findings_filter":
elif type == "aws_macie2_invitation_accepter":
elif type == "aws_macie2_member":
elif type == "aws_macie2_organization_admin_account":
elif type == "aws_main_route_table_association":
elif type == "aws_media_convert_queue":
elif type == "aws_media_package_channel":
elif type == "aws_media_store_container":
elif type == "aws_media_store_container_policy":
elif type == "aws_medialive_channel":
elif type == "aws_medialive_input":
elif type == "aws_medialive_input_security_group":
elif type == "aws_medialive_multiplex":
elif type == "aws_medialive_multiplex_program":
elif type == "aws_memorydb_acl":
elif type == "aws_memorydb_cluster":
elif type == "aws_memorydb_parameter_group":
elif type == "aws_memorydb_snapshot":
elif type == "aws_memorydb_subnet_group":
elif type == "aws_memorydb_user":
elif type == "aws_mq_broker":
elif type == "aws_mq_broker_instance_type_offerings":
elif type == "aws_mq_configuration":
elif type == "aws_msk_broker_nodes":
elif type == "aws_msk_cluster":
elif type == "aws_msk_cluster_policy":
elif type == "aws_msk_configuration":
elif type == "aws_msk_kafka_version":
elif type == "aws_msk_replicator":
elif type == "aws_msk_scram_secret_association":
elif type == "aws_msk_serverless_cluster":
elif type == "aws_msk_vpc_connection":
elif type == "aws_mskconnect_connector":
elif type == "aws_mskconnect_custom_plugin":
elif type == "aws_mskconnect_worker_configuration":
elif type == "aws_mwaa_environment":
elif type == "aws_nat_gateway":
elif type == "aws_nat_gateways":
elif type == "aws_neptune_cluster":
elif type == "aws_neptune_cluster_endpoint":
elif type == "aws_neptune_cluster_instance":
elif type == "aws_neptune_cluster_parameter_group":
elif type == "aws_neptune_cluster_snapshot":
elif type == "aws_neptune_engine_version":
elif type == "aws_neptune_event_subscription":
elif type == "aws_neptune_global_cluster":
elif type == "aws_neptune_orderable_db_instance":
elif type == "aws_neptune_parameter_group":
elif type == "aws_neptune_subnet_group":
elif type == "aws_network_acl":
elif type == "aws_network_acl_association":
elif type == "aws_network_acl_rule":
elif type == "aws_network_acls":
elif type == "aws_network_interface":
elif type == "aws_network_interface_attachment":
elif type == "aws_network_interface_sg_attachment":
elif type == "aws_network_interfaces":
elif type == "aws_networkfirewall_firewall":
elif type == "aws_networkfirewall_firewall_policy":
elif type == "aws_networkfirewall_logging_configuration":
elif type == "aws_networkfirewall_resource_policy":
elif type == "aws_networkfirewall_rule_group":
elif type == "aws_networkmanager_attachment_accepter":
elif type == "aws_networkmanager_connect_attachment":
elif type == "aws_networkmanager_connect_peer":
elif type == "aws_networkmanager_connection":
elif type == "aws_networkmanager_connections":
elif type == "aws_networkmanager_core_network":
elif type == "aws_networkmanager_core_network_policy_attac=":
elif type == "aws_networkmanager_core_network_policy_docum=":
elif type == "aws_networkmanager_customer_gateway_association":
elif type == "aws_networkmanager_device":
elif type == "aws_networkmanager_devices":
elif type == "aws_networkmanager_global_network":
elif type == "aws_networkmanager_global_networks":
elif type == "aws_networkmanager_link":
elif type == "aws_networkmanager_link_association":
elif type == "aws_networkmanager_links":
elif type == "aws_networkmanager_site":
elif type == "aws_networkmanager_site_to_site_vpn_att=":
elif type == "aws_networkmanager_sites":
elif type == "aws_networkmanager_transit_gateway_connect_p=":
elif type == "aws_networkmanager_transit_gateway_peering":
elif type == "aws_networkmanager_transit_gateway_registration":
elif type == "aws_networkmanager_transit_gateway_route_tab=":
elif type == "aws_networkmanager_vpc_attachment":
elif type == "aws_oam_link":
elif type == "aws_oam_sink":
elif type == "aws_oam_sink_policy":
elif type == "aws_opensearch_domain":
elif type == "aws_opensearch_domain_policy":
elif type == "aws_opensearch_domain_saml_options":
elif type == "aws_opensearch_inbound_connection_accepter":
elif type == "aws_opensearch_outbound_connection":
elif type == "aws_opensearch_package":
elif type == "aws_opensearch_package_association":
elif type == "aws_opensearch_vpc_endpoint":
elif type == "aws_opensearchserverless_access_policy":
elif type == "aws_opensearchserverless_collection":
elif type == "aws_opensearchserverless_lifecycle_policy":
elif type == "aws_opensearchserverless_security_config":
elif type == "aws_opensearchserverless_security_policy":
elif type == "aws_opensearchserverless_vpc_endpoint":
elif type == "aws_opsworks_application":
elif type == "aws_opsworks_custom_layer":
elif type == "aws_opsworks_ecs_cluster_layer":
elif type == "aws_opsworks_ganglia_layer":
elif type == "aws_opsworks_haproxy_layer":
elif type == "aws_opsworks_instance":
elif type == "aws_opsworks_java_app_layer":
elif type == "aws_opsworks_memcached_layer":
elif type == "aws_opsworks_mysql_layer":
elif type == "aws_opsworks_nodejs_app_layer":
elif type == "aws_opsworks_permission":
elif type == "aws_opsworks_php_app_layer":
elif type == "aws_opsworks_rails_app_layer":
elif type == "aws_opsworks_rds_db_instance":
elif type == "aws_opsworks_stack":
elif type == "aws_opsworks_static_web_layer":
elif type == "aws_opsworks_user_profile":
elif type == "aws_organizations_account":
elif type == "aws_organizations_delegated_administrator":
elif type == "aws_organizations_delegated_administrators":
elif type == "aws_organizations_delegated_services":
elif type == "aws_organizations_organization":
elif type == "aws_organizations_organizational_unit":
elif type == "aws_organizations_organizational_unit_child_=":
elif type == "aws_organizations_organizational_unit_descendant_=":
elif type == "aws_organizations_organizational_units":
elif type == "aws_organizations_policies":
elif type == "aws_organizations_policies_for_target":
elif type == "aws_organizations_policy":
elif type == "aws_organizations_policy_attachment":
elif type == "aws_organizations_resource_policy":
elif type == "aws_organizations_resource_tags":
elif type == "aws_outposts_asset":
elif type == "aws_outposts_assets":
elif type == "aws_outposts_outpost":
elif type == "aws_outposts_outpost_instance_type":
elif type == "aws_outposts_outpost_instance_types":
elif type == "aws_outposts_outposts":
elif type == "aws_outposts_site":
elif type == "aws_outposts_sites":
elif type == "aws_partition":
elif type == "aws_pinpoint_adm_channel":
elif type == "aws_pinpoint_apns_channel":
elif type == "aws_pinpoint_apns_sandbox_channel":
elif type == "aws_pinpoint_apns_voip_channel":
elif type == "aws_pinpoint_apns_voip_sandbox_channel":
elif type == "aws_pinpoint_app":
elif type == "aws_pinpoint_baidu_channel":
elif type == "aws_pinpoint_email_channel":
elif type == "aws_pinpoint_event_stream":
elif type == "aws_pinpoint_gcm_channel":
elif type == "aws_pinpoint_sms_channel":
elif type == "aws_pipes_pipe":
elif type == "aws_placement_group":
elif type == "aws_polly_voices":
elif type == "aws_prefix_list":
elif type == "aws_pricing_product":
elif type == "aws_prometheus_alert_manager_definition":
elif type == "aws_prometheus_rule_group_namespace":
elif type == "aws_prometheus_workspace":
elif type == "aws_proxy_protocol_policy":
elif type == "aws_qldb_ledger":
elif type == "aws_qldb_stream":
elif type == "aws_quicksight_account_subscription":
elif type == "aws_quicksight_analysis":
elif type == "aws_quicksight_dashboard":
elif type == "aws_quicksight_data_set":
elif type == "aws_quicksight_data_source":
elif type == "aws_quicksight_folder":
elif type == "aws_quicksight_folder_membership":
elif type == "aws_quicksight_group":
elif type == "aws_quicksight_group_membership":
elif type == "aws_quicksight_iam_policy_assignment":
elif type == "aws_quicksight_ingestion":
elif type == "aws_quicksight_namespace":
elif type == "aws_quicksight_refresh_schedule":
elif type == "aws_quicksight_template":
elif type == "aws_quicksight_template_alias":
elif type == "aws_quicksight_theme":
elif type == "aws_quicksight_user":
elif type == "aws_quicksight_vpc_connection":
elif type == "aws_ram_principal_association":
elif type == "aws_ram_resource_association":
elif type == "aws_ram_resource_share":
elif type == "aws_ram_resource_share_accepter":
elif type == "aws_ram_sharing_with_organization":

elif type == "aws_rbin_rule":
    clfn="route53resolver";descfn="list_resolver_rules";topkey="ResolverRules";key="Id";filterid=key
elif type == "aws_rds_certificate":
    clfn="rds";descfn="describe_certificates";topkey="Certificates";key="CertificateIdentifier";filterid=key

elif type == "aws_rds_cluster": clfn="rds";descfn="describe_db_clusters";topkey="DBClusters";key="DBClusterIdentifier";filterid=key
elif type == "aws_rds_cluster_activity_stream": 
    clfn="rds";descfn="describe_db_cluster_activity_stream";topkey="ActivityStream";key="ActivityStreamId";filterid=key
elif type == "aws_rds_cluster_endpoint":
    clfn="rds";descfn="describe_db_cluster_endpoints";topkey="DBClusterEndpoints";key="DBClusterEndpointIdentifier";filterid=key
elif type == "aws_rds_cluster_instance":
    clfn="rds";descfn="describe_db_cluster_instances";topkey="DBClusterInstances";key="DBInstanceIdentifier";filterid=key
elif type == "aws_rds_cluster_parameter_group":
    clfn="rds";descfn="describe_db_cluster_parameter_groups";topkey="DBClusterParameterGroups";key="DBClusterParameterGroupName";filterid=key
elif type == "aws_rds_cluster_role_association":
    clfn="rds";descfn="describe_db_cluster_role_associations";topkey="DBClusterRoleAssociations";key="DBClusterRoleAssociationId";filterid=key
elif type == "aws_rds_clusters":
    clfn="rds";descfn="describe_db_clusters";topkey="DBClusters";key="DBClusterIdentifier";filterid=key
elif type == "aws_rds_custom_db_engine_version": 
    clfn="rds";descfn="describe_custom_db_engine_versions";topkey="CustomDBEngineVersions";key="EngineVersion";filterid=key
elif type == "aws_rds_engine_version":
    clfn="rds";descfn="describe_db_engine_versions";topkey="DBEngineVersions";key="EngineVersion";filterid=key
elif type == "aws_rds_export_task":
    clfn="rds";descfn="describe_export_tasks";topkey="ExportTasks";key="ExportTaskIdentifier";filterid=key
elif type == "aws_rds_global_cluster":
    clfn="rds";descfn="describe_global_clusters";topkey="GlobalClusters";key="GlobalClusterIdentifier";filterid=key
elif type == "aws_rds_orderable_db_instance":
    clfn="rds";descfn="describe_orderable_db_instance_options";topkey="OrderableDBInstanceOptions";key="Engine";filterid=key
elif type == "aws_rds_reserved_instance":
    clfn="rds";descfn="describe_reserved_db_instances";topkey="ReservedDBInstances";key="ReservedDBInstanceId";filterid=key

elif type == "aws_rds_reserved_instance_offering":
    clfn="rds";descfn="describe_reserved_db_instance_offerings";topkey="ReservedDBInstanceOfferings";key="ReservedDBInstancesOfferingId";filterid=key
elif type == "aws_redshift_authentication_profile":
    clfn="redshift";descfn="describe_authentication_profiles";topkey="AuthenticationProfiles";key="AuthenticationProfileName";filterid=key
elif type == "aws_redshift_cluster":
    clfn="redshift";descfn="describe_clusters";topkey="Clusters";key="ClusterIdentifier";filterid=key
elif type == "aws_redshift_cluster_credentials":
    clfn="redshift";descfn="describe_cluster_credentials";topkey="ClusterCredentials";key="DbUser";filterid=key
elif type == "aws_redshift_cluster_iam_roles":
    clfn="redshift";descfn="describe_cluster_iam_roles";topkey="ClusterIamRoles";key="ClusterIdentifier";filterid=key

elif type == "aws_redshift_cluster_snapshot":
    clfn="redshift";descfn="describe_cluster_snapshots";topkey="Snapshots";key="SnapshotIdentifier";filterid=key
elif type == "aws_redshift_endpoint_access":
    clfn="redshift";descfn="describe_endpoint_access";topkey="EndpointAccess";key="EndpointName";filterid=key
elif type == "aws_redshift_endpoint_authorization":
    clfn="redshift";descfn="describe_endpoint_authorization";topkey="EndpointAuthorization";key="EndpointName";filterid=key
elif type == "aws_redshift_event_subscription":
    clfn="redshift";descfn="describe_event_subscriptions";topkey="EventSubscriptionsList";key="SubscriptionName";filterid=key
elif type == "aws_redshift_hsm_client_certificate":
    clfn="redshift";descfn="describe_hsm_client_certificates";topkey="HsmClientCertificates";key="HsmClientCertificateIdentifier";filterid=key
elif type == "aws_redshift_hsm_configuration":
    clfn="redshift";descfn="describe_hsm_configurations";topkey="HsmConfigurations";key="HsmConfigurationIdentifier";filterid=key
elif type == "aws_redshift_orderable_cluster":
    clfn="redshift";descfn="describe_orderable_cluster_options";topkey="OrderableClusterOptions";key="ClusterType";filterid=key
elif type == "aws_redshift_parameter_group":
    clfn="redshift";descfn="describe_cluster_parameters";topkey="Parameters";key="ParameterName";filterid=key
elif type == "aws_redshift_partner":
    clfn="redshift";descfn="describe_partners";topkey="Partners";key="PartnerName";filterid=key
elif type == "aws_redshift_resource_policy":
    clfn="redshift";descfn="describe_resource_policies";topkey="ResourcePolicies";key="ResourcePolicyId";filterid=key
elif type == "aws_redshift_scheduled_action":
    clfn="redshift";descfn="describe_scheduled_actions";topkey="ScheduledActions";key="ScheduledActionName";filterid=key
elif type == "aws_redshift_service_account":
    clfn="redshift";descfn="describe_service_accounts";topkey="ServiceAccounts";key="ServiceAccountName";filterid=key
elif type == "aws_redshift_snapshot_copy_grant":
    clfn="redshift";descfn="describe_snapshot_copy_grants";topkey="SnapshotCopyGrants";key="SnapshotCopyGrantName";filterid=key
elif type == "aws_redshift_snapshot_schedule":
    clfn="redshift";descfn="describe_snapshot_schedules";topkey="SnapshotSchedules";key="ScheduleIdentifier";filterid=key
elif type == "aws_redshift_snapshot_schedule_association":
    clfn="redshift";descfn="describe_snapshot_schedule_associations";topkey="SnapshotScheduleAssociations";key="ScheduleAssociationId";filterid=key
elif type == "aws_redshift_subnet_group":
    clfn="redshift";descfn="describe_cluster_subnet_groups";topkey="ClusterSubnetGroups";key="ClusterSubnetGroupName";filterid=key
elif type == "aws_redshift_usage_limit":
    clfn="redshift";descfn="describe_usage_limits";topkey="UsageLimits";key="UsageLimitId";filterid=key
elif type == "aws_redshiftdata_statement":
    clfn="redshift-data";descfn="describe_statement";topkey="Statement";key="Id";filterid=key
elif type == "aws_redshiftserverless_credentials":
    clfn="redshift-serverless";descfn="describe_credentials";topkey="Credentials";key="Name";filterid=key
elif type == "aws_redshiftserverless_endpoint_access":
    clfn="redshift-serverless";descfn="describe_endpoint_access";topkey="EndpointAccess";key="EndpointName";filterid=key
elif type == "aws_redshiftserverless_namespace":
    clfn="redshift-serverless";descfn="describe_namespaces";topkey="Namespaces";key="NamespaceName";filterid=key
elif type == "aws_redshiftserverless_resource_policy":
    clfn="redshift-serverless";descfn="describe_resource_policies";topkey="ResourcePolicies";key="ResourcePolicyId";filterid=key
elif type == "aws_redshiftserverless_snapshot":
    clfn="redshift-serverless";descfn="describe_snapshots";topkey="Snapshots";key="SnapshotName";filterid=key
elif type == "aws_redshiftserverless_usage_limit":
    clfn="redshift-serverless";descfn="describe_usage_limits";topkey="UsageLimits";key="UsageLimitId";filterid=key
elif type == "aws_redshiftserverless_workgroup":
    clfn="redshift-serverless";descfn="describe_workgroups";topkey="Workgroups";key="WorkgroupName";filterid=key
elif type == "aws_region":
    clfn="ec2";descfn="describe_regions";topkey="Regions";key="RegionName";filterid=key
elif type == "aws_regions":
    clfn="ec2";descfn="describe_regions";topkey="Regions";key="RegionName";filterid=key
elif type == "aws_resourceexplorer2_index":
    clfn="resource-explorer2";descfn="list_indices";topkey="Indices";key="Name";filterid=key

elif type == "aws_resourceexplorer2_view":
    clfn="resource-explorer2";descfn="list_views";topkey="Views";key="Name";filterid=key
elif type == "aws_resourcegroups_group":
    clfn="resource-groups";descfn="list_groups";topkey="GroupIdentifiers";key="GroupName";filterid=key
elif type == "aws_resourcegroups_resource":
    clfn="resource-groups";descfn="list_resources";topkey="ResourceIdentifiers";key="ResourceArn";filterid=key
elif type == "aws_resourcegroupstaggingapi_resources":
    clfn="resourcegroupstaggingapi";descfn="get_resources";topkey="ResourceTagMappingList";key="ResourceARN";filterid=key
elif type == "aws_rolesanywhere_profile":
    clfn="rolesanywhere";descfn="list_profiles";topkey="Profiles";key="ProfileName";filterid=key
elif type == "aws_rolesanywhere_trust_anchor":
    clfn="rolesanywhere";descfn="list_trust_anchors";topkey="TrustAnchors";key="TrustAnchorId";filterid=key
elif type == "aws_route":
    clfn="ec2";descfn="describe_route_tables";topkey="RouteTables";key="RouteTableId";filterid=key
elif type == "aws_route53_cidr_collection":
    clfn="route53";descfn="list_cidr_collections";topkey="CidrCollections";key="Id";filterid=key
elif type == "aws_route53_cidr_location":
    clfn="route53";descfn="list_cidr_locations";topkey="CidrLocations";key="Id";filterid=key
elif type == "aws_route53_delegation_set":
    clfn="route53";descfn="list_delegation_sets";topkey="DelegationSets";key="Id";filterid=key
elif type == "aws_route53_health_check":
    clfn="route53";descfn="list_health_checks";topkey="HealthChecks";key="Id";filterid=key
elif type == "aws_route53_hosted_zone_dnssec":
    clfn="route53";descfn="list_hosted_zone_dnssec";topkey="HostedZoneDNSSEC";key="Id";filterid=key
elif type == "aws_route53_key_signing_key":
    clfn="route53";descfn="list_key_signing_keys";topkey="KeySigningKeys";key="Id";filterid=key
elif type == "aws_route53_query_log":
    clfn="route53";descfn="list_query_logs";topkey="QueryLogs";key="Id";filterid=key
elif type == "aws_route53_record":
    clfn="route53";descfn="list_resource_record_sets";topkey="ResourceRecordSets";key="Name";filterid=key
elif type == "aws_route53_resolver_config":
    clfn="route53";descfn="list_resolver_configs";topkey="ResolverConfigs";key="Id";filterid=key
elif type == "aws_route53_resolver_dnssec_config":
    clfn="route53";descfn="list_resolver_dnssec_configs";topkey="ResolverDNSSECConfigs";key="Id";filterid=key
elif type == "aws_route53_resolver_endpoint":
    clfn="route53";descfn="list_resolver_endpoints";topkey="ResolverEndpoints";key="Id";filterid=key
elif type == "aws_route53_resolver_firewall_config":
    clfn="route53";descfn="list_resolver_firewall_configs";topkey="ResolverFirewallConfigs";key="Id";filterid=key
elif type == "aws_route53_resolver_firewall_domain_list":
    clfn="route53";descfn="list_resolver_firewall_domain_lists";topkey="ResolverFirewallDomainLists";key="Id";filterid=key
elif type == "aws_route53_resolver_firewall_rule":
    clfn="route53";descfn="list_resolver_firewall_rules";topkey="ResolverFirewallRules";key="Id";filterid=key
elif type == "aws_route53_resolver_firewall_rule_group":
    clfn="route53";descfn="list_resolver_firewall_rule_groups";topkey="ResolverFirewallRuleGroups";key="Id";filterid=key
elif type == "aws_route53_resolver_firewall_rule_groups":
    clfn="route53";descfn="list_resolver_firewall_rule_groups";topkey="ResolverFirewallRuleGroups";key="Id";filterid=key
elif type == "aws_route53_resolver_firewall_rules":
    clfn="route53";descfn="list_resolver_firewall_rules";topkey="ResolverFirewallRules";key="Id";filterid=key
elif type == "aws_route53_resolver_query_log_config":
    clfn="route53";descfn="list_resolver_query_log_configs";topkey="ResolverQueryLogConfigs";key="Id";filterid=key
elif type == "aws_route53_resolver_query_log_config_a=":
    clfn="route53";descfn="list_resolver_query_log_config_associations";topkey="ResolverQueryLogConfigAssociations";key="Id";filterid=key
elif type == "aws_route53_resolver_rule":
    clfn="route53";descfn="list_resolver_rules";topkey="ResolverRules";key="Id";filterid=key
elif type == "aws_route53_resolver_rule_association":
    clfn="route53";descfn="list_resolver_rule_associations";topkey="ResolverRuleAssociations";key="Id";filterid=key
elif type == "aws_route53_resolver_rules":
    clfn="route53";descfn="list_resolver_rules";topkey="ResolverRules";key="Id";filterid=key
elif type == "aws_route53_traffic_policy":
    clfn="route53";descfn="list_traffic_policies";topkey="TrafficPolicies";key="Id";filterid=key
elif type == "aws_route53_traffic_policy_document":
    clfn="route53";descfn="list_traffic_policy_documents";topkey="TrafficPolicyDocuments";key="Id";filterid=key
elif type == "aws_route53_traffic_policy_instance":
    clfn="route53";descfn="list_traffic_policy_instances";topkey="TrafficPolicyInstances";key="Id";filterid=key
elif type == "aws_route53_vpc_association_authorization":
    clfn="route53";descfn="list_vpc_associations_authorization";topkey="VPCAssociations";key="Id";filterid=key
elif type == "aws_route53_zone":
    clfn="route53";descfn="list_hosted_zones";topkey="HostedZones";key="Name";filterid=key
elif type == "aws_route53_zone_association":
    clfn="route53";descfn="list_hosted_zone_associations";topkey="HostedZoneAssociations";key="Id";filterid=key
elif type == "aws_route53domains_registered_domain":
    clfn="route53domains";descfn="list_domains";topkey="Domains";key="DomainName";filterid=key
elif type == "aws_route53recoverycontrolconfig_cluster":
    clfn="route53recoverycontrolconfig";descfn="list_clusters";topkey="Clusters";key="ClusterArn";filterid=key
elif type == "aws_route53recoverycontrolconfig_control_panel":
    clfn="route53recoverycontrolconfig";descfn="list_control_panels";topkey="ControlPanels";key="ControlPanelArn";filterid=key
elif type == "aws_route53recoverycontrolconfig_routing_control":
    clfn="route53recoverycontrolconfig";descfn="list_routing_controls";topkey="RoutingControls";key="RoutingControlArn";filterid=key
elif type == "aws_route53recoverycontrolconfig_safety_rule":
    clfn="route53recoverycontrolconfig";descfn="list_safety_rules";topkey="SafetyRules";key="SafetyRuleArn";filterid=key
elif type == "aws_route53recoveryreadiness_cell":
    clfn="route53recoveryreadiness";descfn="list_cells";topkey="Cells";key="CellArn";filterid=key
elif type == "aws_route53recoveryreadiness_readiness_check":
    clfn="route53recoveryreadiness";descfn="list_readiness_checks";topkey="ReadinessChecks";key="ReadinessCheckArn";filterid=key
elif type == "aws_route53recoveryreadiness_recovery_group":
    clfn="route53recoveryreadiness";descfn="list_recovery_groups";topkey="RecoveryGroups";key="RecoveryGroupArn";filterid=key
elif type == "aws_route53recoveryreadiness_resource_set":
    clfn="route53recoveryreadiness";descfn="list_resource_sets";topkey="ResourceSets";key="ResourceSetArn";filterid=key
elif type == "aws_route_table":
    clfn="ec2";descfn="describe_route_tables";topkey="RouteTables";key="RouteTableId";filterid=key
elif type == "aws_route_table_association":
    clfn="ec2";descfn="describe_route_tables";topkey="Associations";key="RouteTableAssociationId";filterid=key
elif type == "aws_route_tables":
    clfn="ec2";descfn="describe_route_tables";topkey="RouteTables";key="RouteTableId";filterid=key
elif type == "aws_rum_app_monitor":
    clfn="rum";descfn="list_app_monitors";topkey="AppMonitors";key="Name";filterid=key
elif type == "aws_rum_metrics_destination":
    clfn="rum";descfn="list_metrics_destinations";topkey="MetricsDestinations";key="Name";filterid=key
elif type == "aws_s3_access_point":
    clfn="s3";descfn="list_access_points";topkey="AccessPoints";key="Name";filterid=key
elif type == "aws_s3_account_public_access_block":
    clfn="s3";descfn="get_public_access_block";topkey="PublicAccessBlockConfiguration";key="BlockPublicAcls";filterid=key
elif type == "aws_s3_bucket":
    clfn="s3";descfn="list_buckets";topkey="Buckets";key="Name";filterid=key
elif type == "aws_s3_bucket_accelerate_configuration":
    clfn="s3";descfn="get_bucket_accelerate_configuration";topkey="Status";key="Status";filterid=key
elif type == "aws_s3_bucket_acl":
    clfn="s3";descfn="get_bucket_acl";topkey="Grants";key="Grantee.DisplayName";filterid=key
elif type == "aws_s3_bucket_analytics_configuration":
    clfn="s3";descfn="get_bucket_analytics_configuration";topkey="AnalyticsConfiguration";key="Id";filterid=key
elif type == "aws_s3_bucket_cors_configuration":
    clfn="s3";descfn="get_bucket_cors_configuration";topkey="CORSRules";key="AllowedMethods";filterid=key
elif type == "aws_s3_bucket_intelligent_tiering_configurat=":
    clfn="s3";descfn="get_bucket_intelligent_tiering_configuration";topkey="IntelligentTieringConfiguration";key="Id";filterid=key
elif type == "aws_s3_bucket_inventory":
    clfn="s3";descfn="get_bucket_inventory_configuration";topkey="InventoryConfiguration";key="Id";filterid=key
elif type == "aws_s3_bucket_lifecycle_configuration":
    clfn="s3";descfn="get_bucket_lifecycle_configuration";topkey="Rules";key="ID";filterid=key
elif type == "aws_s3_bucket_logging":
    clfn="s3";descfn="get_bucket_logging";topkey="LoggingEnabled";key="TargetBucket";filterid=key
elif type == "aws_s3_bucket_metric":
    clfn="s3";descfn="get_bucket_metrics_configuration";topkey="MetricsConfiguration";key="Id";filterid=key
elif type == "aws_s3_bucket_notification":
    clfn="s3";descfn="get_bucket_notification_configuration";topkey="TopicConfigurations";key="Topic";filterid=key
elif type == "aws_s3_bucket_object":
elif type == "aws_s3_bucket_object_lock_configuration":
elif type == "aws_s3_bucket_objects":
elif type == "aws_s3_bucket_ownership_controls":
elif type == "aws_s3_bucket_policy":
elif type == "aws_s3_bucket_public_access_block":
elif type == "aws_s3_bucket_replication_configuration":
elif type == "aws_s3_bucket_request_payment_configuration":
elif type == "aws_s3_bucket_server_side_encryption_co=":
elif type == "aws_s3_bucket_versioning":
elif type == "aws_s3_bucket_website_configuration":
elif type == "aws_s3_directory_bucket":
elif type == "aws_s3_directory_buckets":
elif type == "aws_s3_object":
elif type == "aws_s3_object_copy":
elif type == "aws_s3_objects":
elif type == "aws_s3control_access_grant":
elif type == "aws_s3control_access_grants_instance":
elif type == "aws_s3control_access_grants_instance_resourc=":
elif type == "aws_s3control_access_grants_location":
elif type == "aws_s3control_access_point_policy":
elif type == "aws_s3control_bucket":
elif type == "aws_s3control_bucket_lifecycle_configuration":
elif type == "aws_s3control_bucket_policy":
elif type == "aws_s3control_multi_region_access_point":
elif type == "aws_s3control_multi_region_access_point_<wbr=":
elif type == "aws_s3control_object_lambda_access_point":
elif type == "aws_s3control_object_lambda_access_point_<wb=":
elif type == "aws_s3control_storage_lens_configuration":
elif type == "aws_s3outposts_endpoint":
elif type == "aws_sagemaker_app":
    clfn="sagemaker";descfn="list_apps";topkey="Apps";key="AppArn";filterid=key
elif type == "aws_sagemaker_app_image_config":
    clfn="sagemaker";descfn="list_app_image_configs";topkey="AppImageConfigs";key="AppImageConfigArn";filterid=key
elif type == "aws_sagemaker_code_repository":
    clfn="sagemaker";descfn="list_code_repositories";topkey="CodeRepositories";key="CodeRepositoryArn";filterid=key
elif type == "aws_sagemaker_data_quality_job_definition":
    clfn="sagemaker";descfn="list_data_quality_job_definitions";topkey="DataQualityJobDefinitions";key="DataQualityJobDefinitionArn";filterid=key
elif type == "aws_sagemaker_device":
    clfn="sagemaker";descfn="list_devices";topkey="Devices";key="DeviceArn";filterid=key
elif type == "aws_sagemaker_device_fleet":
    clfn="sagemaker";descfn="list_device_fleets";topkey="DeviceFleets";key="DeviceFleetArn";filterid=key
elif type == "aws_sagemaker_domain":
    clfn="sagemaker";descfn="list_domains";topkey="Domains";key="DomainArn";filterid=key
elif type == "aws_sagemaker_endpoint":
    clfn="sagemaker";descfn="list_endpoints";topkey="Endpoints";key="EndpointArn";filterid=key
elif type == "aws_sagemaker_endpoint_configuration":
    clfn="sagemaker";descfn="list_endpoint_configurations";topkey="EndpointConfigurations";key="EndpointConfigurationArn";filterid=key
elif type == "aws_sagemaker_feature_group":
    clfn="sagemaker";descfn="list_feature_groups";topkey="FeatureGroups";key="FeatureGroupArn";filterid=key
elif type == "aws_sagemaker_flow_definition":
    clfn="sagemaker";descfn="list_flow_definitions";topkey="FlowDefinitions";key="FlowDefinitionArn";filterid=key
elif type == "aws_sagemaker_human_task_ui":
    clfn="sagemaker";descfn="list_human_task_uis";topkey="HumanTaskUIs";key="HumanTaskUiArn";filterid=key
elif type == "aws_sagemaker_image":
    clfn="sagemaker";descfn="list_images";topkey="Images";key="ImageArn";filterid=key
elif type == "aws_sagemaker_image_version":
    clfn="sagemaker";descfn="list_image_versions";topkey="ImageVersions";key="ImageVersionArn";filterid=key
elif type == "aws_sagemaker_model":
    clfn="sagemaker";descfn="list_models";topkey="Models";key="ModelArn";filterid=key
elif type == "aws_sagemaker_model_package_group":
    clfn="sagemaker";descfn="list_model_package_groups";topkey="ModelPackageGroups";key="ModelPackageGroupArn";filterid=key
elif type == "aws_sagemaker_model_package_group_policy":
    clfn="sagemaker";descfn="get_model_package_group_policy";topkey="Policy";key="Policy";filterid=key
elif type == "aws_sagemaker_monitoring_schedule":
    clfn="sagemaker";descfn="list_monitoring_schedules";topkey="MonitoringSchedules";key="MonitoringScheduleArn";filterid=key
elif type == "aws_sagemaker_notebook_instance":
    clfn="sagemaker";descfn="list_notebook_instances";topkey="NotebookInstances";key="NotebookInstanceArn";filterid=key
elif type == "aws_sagemaker_notebook_instance_lifecycle_co=":
    clfn="sagemaker";descfn="list_notebook_instance_lifecycle_configs";topkey="NotebookInstanceLifecycleConfigs";key="NotebookInstanceLifecycleConfigArn";filterid=key
elif type == "aws_sagemaker_pipeline":
    clfn="sagemaker";descfn="list_pipelines";topkey="Pipelines";key="PipelineArn";filterid=key
elif type == "aws_sagemaker_prebuilt_ecr_image":
    clfn="sagemaker";descfn="list_prebuilt_ecr_images";topkey="PrebuiltEcrImages";key="PrebuiltEcrImageArn";filterid=key
elif type == "aws_sagemaker_project":
    clfn="sagemaker";descfn="list_projects";topkey="Projects";key="ProjectArn";filterid=key
elif type == "aws_sagemaker_servicecatalog_portfolio_status":
    clfn="sagemaker";descfn="get_service_catalog_portfolio_status";topkey="Status";key="Status";filterid=key
elif type == "aws_sagemaker_space":
    clfn="sagemaker";descfn="list_spaces";topkey="Spaces";key="SpaceArn";filterid=key
elif type == "aws_sagemaker_studio_lifecycle_config":
    clfn="sagemaker";descfn="list_studio_lifecycle_configs";topkey="StudioLifecycleConfigs";key="StudioLifecycleConfigArn";filterid=key
elif type == "aws_sagemaker_user_profile":
    clfn="sagemaker";descfn="list_user_profiles";topkey="UserProfiles";key="UserProfileArn";filterid=key
elif type == "aws_sagemaker_workforce":
    clfn="sagemaker";descfn="list_workforces";topkey="Workforces";key="WorkforceArn";filterid=key
elif type == "aws_sagemaker_workteam":
    clfn="sagemaker";descfn="list_workteams";topkey="Workteams";key="WorkteamArn";filterid=key
elif type == "aws_scheduler_schedule":
elif type == "aws_scheduler_schedule_group":
elif type == "aws_schemas_discoverer":
elif type == "aws_schemas_registry":
elif type == "aws_schemas_registry_policy":
elif type == "aws_schemas_schema":
elif type == "aws_secretsmanager_random_password":
elif type == "aws_secretsmanager_secret":
elif type == "aws_secretsmanager_secret_policy":
elif type == "aws_secretsmanager_secret_rotation":
elif type == "aws_secretsmanager_secret_version":
elif type == "aws_secretsmanager_secrets":
elif type == "aws_security_group":
elif type == "aws_security_group_rule":
elif type == "aws_security_groups":
elif type == "aws_securityhub_account":
elif type == "aws_securityhub_action_target":
elif type == "aws_securityhub_finding_aggregator":
elif type == "aws_securityhub_insight":
elif type == "aws_securityhub_invite_accepter":
elif type == "aws_securityhub_member":
elif type == "aws_securityhub_organization_admin_account":
elif type == "aws_securityhub_organization_configuration":
elif type == "aws_securityhub_product_subscription":
elif type == "aws_securityhub_standards_control":
elif type == "aws_securityhub_standards_subscription":
elif type == "aws_securitylake_data_lake":
elif type == "aws_serverlessapplicationrepository_application":
elif type == "aws_serverlessapplicationrepository_cloudformation_sta=":
elif type == "aws_service_discovery_http_namespace":
elif type == "aws_service_discovery_instance":
elif type == "aws_service_discovery_private_dns_namespace":
elif type == "aws_service_discovery_public_dns_namespace":
elif type == "aws_service_discovery_service":
elif type == "aws_servicecatalog_budget_resource_association":
elif type == "aws_servicecatalog_constraint":
elif type == "aws_servicecatalog_launch_paths":
elif type == "aws_servicecatalog_organizations_access":
elif type == "aws_servicecatalog_portfolio":
elif type == "aws_servicecatalog_portfolio_constraints":
elif type == "aws_servicecatalog_portfolio_share":
elif type == "aws_servicecatalog_principal_portfolio_association":
elif type == "aws_servicecatalog_product":
elif type == "aws_servicecatalog_product_portfolio_association":
elif type == "aws_servicecatalog_provisioned_product":
elif type == "aws_servicecatalog_provisioning_artifact":
elif type == "aws_servicecatalog_provisioning_artifacts":
elif type == "aws_servicecatalog_service_action":
elif type == "aws_servicecatalog_tag_option":
elif type == "aws_servicecatalog_tag_option_resource_association":
elif type == "aws_servicequotas_service":
elif type == "aws_servicequotas_service_quota":
elif type == "aws_servicequotas_template":
elif type == "aws_servicequotas_template_association":
elif type == "aws_servicequotas_templates":
elif type == "aws_ses_active_receipt_rule_set":
elif type == "aws_ses_configuration_set":
elif type == "aws_ses_domain_dkim":
elif type == "aws_ses_domain_identity":
elif type == "aws_ses_domain_identity_verification":
elif type == "aws_ses_domain_mail_from":
elif type == "aws_ses_email_identity":
elif type == "aws_ses_event_destination":
elif type == "aws_ses_identity_notification_topic":
elif type == "aws_ses_identity_policy":
elif type == "aws_ses_receipt_filter":
elif type == "aws_ses_receipt_rule":
elif type == "aws_ses_receipt_rule_set":
elif type == "aws_ses_template":
elif type == "aws_sesv2_account_vdm_attributes":
elif type == "aws_sesv2_configuration_set":
elif type == "aws_sesv2_configuration_set_event_destinatio=":
elif type == "aws_sesv2_contact_list":
elif type == "aws_sesv2_dedicated_ip_assignment":
elif type == "aws_sesv2_dedicated_ip_pool":
elif type == "aws_sesv2_email_identity":
elif type == "aws_sesv2_email_identity_feedback_attributes":
elif type == "aws_sesv2_email_identity_mail_from_attr=":
elif type == "aws_sfn_activity":
elif type == "aws_sfn_alias":
elif type == "aws_sfn_state_machine":
elif type == "aws_sfn_state_machine_versions":
elif type == "aws_shield_application_layer_automatic_respo=":
elif type == "aws_shield_drt_access_log_bucket_associ=":
elif type == "aws_shield_drt_access_role_arn_associat=":
elif type == "aws_shield_protection":
elif type == "aws_shield_protection_group":
elif type == "aws_shield_protection_health_check_associati=":
elif type == "aws_signer_signing_job":
elif type == "aws_signer_signing_profile":
elif type == "aws_signer_signing_profile_permission":
elif type == "aws_simpledb_domain":
elif type == "aws_snapshot_create_volume_permission":
elif type == "aws_sns_platform_application":
elif type == "aws_sns_sms_preferences":
elif type == "aws_sns_topic":
elif type == "aws_sns_topic_data_protection_policy":
elif type == "aws_sns_topic_policy":
elif type == "aws_sns_topic_subscription":
elif type == "aws_spot_datafeed_subscription":
elif type == "aws_spot_fleet_request":
elif type == "aws_spot_instance_request":
elif type == "aws_sqs_queue":
elif type == "aws_sqs_queue_policy":
elif type == "aws_sqs_queue_redrive_allow_policy":
elif type == "aws_sqs_queue_redrive_policy":
elif type == "aws_sqs_queues":
elif type == "aws_ssm_activation":
elif type == "aws_ssm_association":
elif type == "aws_ssm_default_patch_baseline":
elif type == "aws_ssm_document":
elif type == "aws_ssm_instances":
elif type == "aws_ssm_maintenance_window":
elif type == "aws_ssm_maintenance_window_target":
elif type == "aws_ssm_maintenance_window_task":
elif type == "aws_ssm_maintenance_windows":
elif type == "aws_ssm_parameter":
elif type == "aws_ssm_parameters_by_path":
elif type == "aws_ssm_patch_baseline":
elif type == "aws_ssm_patch_group":
elif type == "aws_ssm_resource_data_sync":
elif type == "aws_ssm_service_setting":
elif type == "aws_ssmcontacts_contact":
elif type == "aws_ssmcontacts_contact_channel":
elif type == "aws_ssmcontacts_plan":
elif type == "aws_ssmincidents_replication_set":
elif type == "aws_ssmincidents_response_plan":
elif type == "aws_ssoadmin_account_assignment":
elif type == "aws_ssoadmin_application":
elif type == "aws_ssoadmin_application_assignment":
elif type == "aws_ssoadmin_application_assignment_configuration":
elif type == "aws_ssoadmin_application_assignments":
elif type == "aws_ssoadmin_application_providers":
elif type == "aws_ssoadmin_customer_managed_policy_attachm=":
elif type == "aws_ssoadmin_instance_access_control_attribu=":
elif type == "aws_ssoadmin_instances":
elif type == "aws_ssoadmin_managed_policy_attachment":
elif type == "aws_ssoadmin_permission_set":
elif type == "aws_ssoadmin_permission_set_inline_policy":
elif type == "aws_ssoadmin_permissions_boundary_attachment":
elif type == "aws_ssoadmin_principal_application_assignments":
elif type == "aws_ssoadmin_trusted_token_issuer":
elif type == "aws_storagegateway_cache":
elif type == "aws_storagegateway_cached_iscsi_volume":
elif type == "aws_storagegateway_file_system_association":
elif type == "aws_storagegateway_gateway":
elif type == "aws_storagegateway_local_disk":
elif type == "aws_storagegateway_nfs_file_share":
elif type == "aws_storagegateway_smb_file_share":
elif type == "aws_storagegateway_stored_iscsi_volume":
elif type == "aws_storagegateway_tape_pool":
elif type == "aws_storagegateway_upload_buffer":
elif type == "aws_storagegateway_working_storage":
elif type == "aws_subnet":
elif type == "aws_swf_domain":
elif type == "aws_synthetics_canary":
elif type == "aws_synthetics_group":
elif type == "aws_synthetics_group_association":
elif type == "aws_timestreamwrite_database":
elif type == "aws_timestreamwrite_table":
elif type == "aws_transcribe_language_model":
elif type == "aws_transcribe_medical_vocabulary":
elif type == "aws_transcribe_vocabulary":
elif type == "aws_transcribe_vocabulary_filter":
elif type == "aws_transfer_access":
elif type == "aws_transfer_agreement":
elif type == "aws_transfer_certificate":
elif type == "aws_transfer_connector":
elif type == "aws_transfer_profile":
elif type == "aws_transfer_server":
elif type == "aws_transfer_ssh_key":
elif type == "aws_transfer_tag":
elif type == "aws_transfer_user":
elif type == "aws_transfer_workflow":
elif type == "aws_verifiedaccess_endpoint":
elif type == "aws_verifiedaccess_group":
elif type == "aws_verifiedaccess_instance":
elif type == "aws_verifiedaccess_instance_logging_configuration":
elif type == "aws_verifiedaccess_instance_trust_provider_a=":
elif type == "aws_verifiedaccess_trust_provider":
elif type == "aws_volume_attachment":
elif type == "aws_vpc":
elif type == "aws_vpc_dhcp_options":
elif type == "aws_vpc_dhcp_options_association":
elif type == "aws_vpc_endpoint":
elif type == "aws_vpc_endpoint_connection_accepter":
elif type == "aws_vpc_endpoint_connection_notification":
elif type == "aws_vpc_endpoint_policy":
elif type == "aws_vpc_endpoint_route_table_association":
elif type == "aws_vpc_endpoint_security_group_association":
elif type == "aws_vpc_endpoint_service":
elif type == "aws_vpc_endpoint_service_allowed_principal":
elif type == "aws_vpc_endpoint_subnet_association":
elif type == "aws_vpc_ipam":
elif type == "aws_vpc_ipam_organization_admin_account":
elif type == "aws_vpc_ipam_pool":
elif type == "aws_vpc_ipam_pool_cidr":
elif type == "aws_vpc_ipam_pool_cidr_allocation":
elif type == "aws_vpc_ipam_preview_next_cidr":
elif type == "aws_vpc_ipam_resource_discovery":
elif type == "aws_vpc_ipam_resource_discovery_association":
elif type == "aws_vpc_ipam_scope":
elif type == "aws_vpc_ipv4_cidr_block_association":
elif type == "aws_vpc_ipv6_cidr_block_association":
elif type == "aws_vpc_network_performance_metric_subscript=":
elif type == "aws_vpc_peering_connection":
elif type == "aws_vpc_peering_connection_accepter":
elif type == "aws_vpc_peering_connection_options":
elif type == "aws_vpc_security_group_egress_rule":
elif type == "aws_vpc_security_group_ingress_rule":
elif type == "aws_vpclattice_access_log_subscription":
elif type == "aws_vpclattice_auth_policy":
elif type == "aws_vpclattice_listener":
elif type == "aws_vpclattice_listener_rule":
elif type == "aws_vpclattice_resource_policy":
elif type == "aws_vpclattice_service":
elif type == "aws_vpclattice_service_network":
elif type == "aws_vpclattice_service_network_service_association":
elif type == "aws_vpclattice_service_network_vpc_association":
elif type == "aws_vpclattice_target_group":
elif type == "aws_vpclattice_target_group_attachment":
elif type == "aws_vpn_connection":
elif type == "aws_vpn_connection_route":
elif type == "aws_vpn_gateway":
elif type == "aws_vpn_gateway_attachment":
elif type == "aws_vpn_gateway_route_propagation":
elif type == "aws_waf_byte_match_set":
elif type == "aws_waf_geo_match_set":
elif type == "aws_waf_ipset":
elif type == "aws_waf_rate_based_rule":
elif type == "aws_waf_regex_match_set":
elif type == "aws_waf_regex_pattern_set":
elif type == "aws_waf_rule":
elif type == "aws_waf_rule_group":
elif type == "aws_waf_size_constraint_set":
elif type == "aws_waf_sql_injection_match_set":
elif type == "aws_waf_web_acl":
elif type == "aws_waf_xss_match_set":
elif type == "aws_wafregional_byte_match_set":
elif type == "aws_wafregional_geo_match_set":
elif type == "aws_wafregional_ipset":
elif type == "aws_wafregional_rate_based_rule":
elif type == "aws_wafregional_regex_match_set":
elif type == "aws_wafregional_regex_pattern_set":
elif type == "aws_wafregional_rule":
elif type == "aws_wafregional_rule_group":
elif type == "aws_wafregional_size_constraint_set":
elif type == "aws_wafregional_sql_injection_match_set":
elif type == "aws_wafregional_web_acl":
elif type == "aws_wafregional_web_acl_association":
elif type == "aws_wafregional_xss_match_set":
elif type == "aws_wafv2_ip_set":
elif type == "aws_wafv2_regex_pattern_set":
elif type == "aws_wafv2_rule_group":
elif type == "aws_wafv2_web_acl":
elif type == "aws_wafv2_web_acl_association":
elif type == "aws_wafv2_web_acl_logging_configuration":
elif type == "aws_worklink_fleet":
elif type == "aws_worklink_website_certificate_authority_association":
elif type == "aws_workspaces_connection_alias":
elif type == "aws_workspaces_directory":
elif type == "aws_workspaces_ip_group":
elif type == "aws_workspaces_workspace":
elif type == "aws_xray_encryption_config":
elif type == "aws_xray_group":
elif type == "aws_xray_sampling_rule":

