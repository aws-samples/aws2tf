# AWS Terraform Provider Resources

Complete list of AWS resources from the Terraform AWS Provider
Total Resources: 1146
Total Services: 179

---

## Table of Contents

- [accessanalyzer](#accessanalyzer)
- [acm](#acm)
- [acm-pca](#acmpca)
- [amp](#amp)
- [amplify](#amplify)
- [apigateway](#apigateway)
- [appconfig](#appconfig)
- [appflow](#appflow)
- [appintegrations](#appintegrations)
- [application-autoscaling](#applicationautoscaling)
- [application-insights](#applicationinsights)
- [appmesh](#appmesh)
- [apprunner](#apprunner)
- [appstream](#appstream)
- [appsync](#appsync)
- [athena](#athena)
- [auditmanager](#auditmanager)
- [autoscaling](#autoscaling)
- [autoscaling-plans](#autoscalingplans)
- [backup](#backup)
- [batch](#batch)
- [bedrock](#bedrock)
- [bedrock-agent](#bedrockagent)
- [budgets](#budgets)
- [ce](#ce)
- [chime-sdk-media-pipelines](#chimesdkmediapipelines)
- [chime-sdk-voice](#chimesdkvoice)
- [cleanrooms](#cleanrooms)
- [cloudcontrol](#cloudcontrol)
- [cloudformation](#cloudformation)
- [cloudfront](#cloudfront)
- [cloudsearch](#cloudsearch)
- [cloudtrail](#cloudtrail)
- [cloudwatch](#cloudwatch)
- [codeartifact](#codeartifact)
- [codebuild](#codebuild)
- [codecatalyst](#codecatalyst)
- [codecommit](#codecommit)
- [codedeploy](#codedeploy)
- [codeguru-reviewer](#codegurureviewer)
- [codeguruprofiler](#codeguruprofiler)
- [codepipeline](#codepipeline)
- [codestar-connections](#codestarconnections)
- [codestar-notifications](#codestarnotifications)
- [cognito-identity](#cognitoidentity)
- [cognito-idp](#cognitoidp)
- [comprehend](#comprehend)
- [config](#config)
- [connect](#connect)
- [controltower](#controltower)
- [cur](#cur)
- [customer-profiles](#customerprofiles)
- [dataexchange](#dataexchange)
- [datapipeline](#datapipeline)
- [datasync](#datasync)
- [datazone](#datazone)
- [dax](#dax)
- [detective](#detective)
- [devicefarm](#devicefarm)
- [directconnect](#directconnect)
- [dlm](#dlm)
- [dms](#dms)
- [docdb](#docdb)
- [docdb-elastic](#docdbelastic)
- [ds](#ds)
- [dynamodb](#dynamodb)
- [ebs](#ebs)
- [ec2](#ec2)
- [ecr](#ecr)
- [ecr-public](#ecrpublic)
- [ecs](#ecs)
- [efs](#efs)
- [eks](#eks)
- [elasticache](#elasticache)
- [elasticbeanstalk](#elasticbeanstalk)
- [elastictranscoder](#elastictranscoder)
- [elb](#elb)
- [elbv2](#elbv2)
- [emr](#emr)
- [emr-containers](#emrcontainers)
- [emr-serverless](#emrserverless)
- [es](#es)
- [events](#events)
- [evidently](#evidently)
- [finspace](#finspace)
- [firehose](#firehose)
- [fis](#fis)
- [fms](#fms)
- [fsx](#fsx)
- [gamelift](#gamelift)
- [glacier](#glacier)
- [globalaccelerator](#globalaccelerator)
- [glue](#glue)
- [grafana](#grafana)
- [guardduty](#guardduty)
- [iam](#iam)
- [identitystore](#identitystore)
- [imagebuilder](#imagebuilder)
- [inspector](#inspector)
- [internetmonitor](#internetmonitor)
- [iot](#iot)
- [ivs](#ivs)
- [ivschat](#ivschat)
- [kafka](#kafka)
- [kafkaconnect](#kafkaconnect)
- [kendra](#kendra)
- [keyspaces](#keyspaces)
- [kinesis](#kinesis)
- [kinesisanalytics](#kinesisanalytics)
- [kinesisvideo](#kinesisvideo)
- [kms](#kms)
- [lakeformation](#lakeformation)
- [lambda](#lambda)
- [lex-models](#lexmodels)
- [license-manager](#licensemanager)
- [lightsail](#lightsail)
- [location](#location)
- [logs](#logs)
- [mediaconvert](#mediaconvert)
- [medialive](#medialive)
- [mediapackage](#mediapackage)
- [mediastore](#mediastore)
- [memorydb](#memorydb)
- [mq](#mq)
- [mwaa](#mwaa)
- [neptune](#neptune)
- [network-firewall](#networkfirewall)
- [networkmanager](#networkmanager)
- [opensearch](#opensearch)
- [opensearchserverless](#opensearchserverless)
- [opsworks](#opsworks)
- [organizations](#organizations)
- [pinpoint](#pinpoint)
- [pipes](#pipes)
- [qldb](#qldb)
- [quicksight](#quicksight)
- [ram](#ram)
- [rbin](#rbin)
- [rds](#rds)
- [redshift](#redshift)
- [redshift-data](#redshiftdata)
- [redshift-serverless](#redshiftserverless)
- [resource-groups](#resourcegroups)
- [rolesanywhere](#rolesanywhere)
- [rum](#rum)
- [sagemaker](#sagemaker)
- [scheduler](#scheduler)
- [schemas](#schemas)
- [sdb](#sdb)
- [secretsmanager](#secretsmanager)
- [securityhub](#securityhub)
- [securitylake](#securitylake)
- [serverlessrepo](#serverlessrepo)
- [service-quotas](#servicequotas)
- [servicecatalog](#servicecatalog)
- [servicediscovery](#servicediscovery)
- [ses](#ses)
- [shield](#shield)
- [signer](#signer)
- [sns](#sns)
- [sqs](#sqs)
- [ssm](#ssm)
- [ssm-contacts](#ssmcontacts)
- [ssm-incidents](#ssmincidents)
- [sso-admin](#ssoadmin)
- [stepfunctions](#stepfunctions)
- [storagegateway](#storagegateway)
- [swf](#swf)
- [synthetics](#synthetics)
- [timestream-write](#timestreamwrite)
- [transcribe](#transcribe)
- [transfer](#transfer)
- [vpc-lattice](#vpclattice)
- [waf](#waf)
- [waf-regional](#wafregional)
- [wafv2](#wafv2)
- [worklink](#worklink)
- [workspaces](#workspaces)
- [xray](#xray)

---

## accessanalyzer

**Boto3 Client:** `accessanalyzer`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_accessanalyzer_analyzer` | `list_analyzers` |
| `aws_accessanalyzer_archive_rule` | `list_archive_rules` |

## acm

**Boto3 Client:** `acm`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_acm_certificate` | `list_certificates` |
| `aws_acm_certificate_validation` | `list_certificates` |

## acm-pca

**Boto3 Client:** `acm-pca`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_acmpca_certificate` | `get_certificate` |
| `aws_acmpca_certificate_authority` | `list_certificate_authorities` |
| `aws_acmpca_certificate_authority_certificate` | `list_certificate_authorities` |
| `aws_acmpca_permission` | `list_permissions` |
| `aws_acmpca_policy` | `get_policy` |

## amp

**Boto3 Client:** `amp`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_prometheus_alert_manager_definition` | `describe_alert_manager_definition` |
| `aws_prometheus_rule_group_namespace` | `list_rule_groups_namespaces` |
| `aws_prometheus_workspace` | `list_workspaces` |

## amplify

**Boto3 Client:** `amplify`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_amplify_app` | `list_apps` |
| `aws_amplify_backend_environment` | `list_backend_environments` |
| `aws_amplify_branch` | `list_branches` |
| `aws_amplify_domain_association` | `list_domain_associations` |
| `aws_amplify_webhook` | `list_webhooks` |

## apigateway

**Boto3 Client:** `apigateway`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_api_gateway_account` | `get_account` |
| `aws_api_gateway_api_key` | `get_api_keys` |
| `aws_api_gateway_authorizer` | `get_authorizers` |
| `aws_api_gateway_base_path_mapping` | `get_base_path_mappings` |
| `aws_api_gateway_client_certificate` | `get_client_certificates` |
| `aws_api_gateway_deployment` | `get_deployments` |
| `aws_api_gateway_documentation_part` | `get_documentation_parts` |
| `aws_api_gateway_documentation_version` | `get_documentation_versions` |
| `aws_api_gateway_domain_name` | `get_domain_names` |
| `aws_api_gateway_gateway_response` | `get_gateway_responses` |
| `aws_api_gateway_integration` | `get_integration` |
| `aws_api_gateway_integration_response` | `get_integration_responses` |
| `aws_api_gateway_method` | `get_method` |
| `aws_api_gateway_method_response` | `get_method_response` |
| `aws_api_gateway_method_settings` | `get_method_settings` |
| `aws_api_gateway_model` | `get_models` |
| `aws_api_gateway_request_validator` | `get_request_validators` |
| `aws_api_gateway_resource` | `get_resources` |
| `aws_api_gateway_rest_api` | `get_rest_apis` |
| `aws_api_gateway_rest_api_policy` | `get_rest_api` |
| `aws_api_gateway_stage` | `get_stages` |
| `aws_api_gateway_usage_plan` | `get_usage_plans` |
| `aws_api_gateway_usage_plan_key` | `get_usage_plan_keys` |
| `aws_api_gateway_vpc_link` | `get_vpc_links` |

## appconfig

**Boto3 Client:** `appconfig`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_appconfig_application` | `list_applications` |
| `aws_appconfig_configuration_profile` | `list_configuration_profiles` |
| `aws_appconfig_deployment` | `list_deployments` |
| `aws_appconfig_deployment_strategy` | `list_deployment_strategies` |
| `aws_appconfig_environment` | `list_environments` |
| `aws_appconfig_extension_association` | `list_extension_associations` |
| `aws_appconfig_hosted_configuration_version` | `list_hosted_configuration_versions` |

## appflow

**Boto3 Client:** `appflow`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_appflow_connector_profile` | `describe_connector_profiles` |
| `aws_appflow_flow` | `list_flows` |

## appintegrations

**Boto3 Client:** `appintegrations`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_appintegrations_data_integration` | `list_data_integrations` |
| `aws_appintegrations_event_integration` | `list_event_integrations` |

## application-autoscaling

**Boto3 Client:** `application-autoscaling`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_appautoscaling_policy` | `describe_scaling_policies` |
| `aws_appautoscaling_scheduled_action` | `describe_scheduled_actions` |
| `aws_appautoscaling_target` | `describe_scalable_targets` |

## application-insights

**Boto3 Client:** `application-insights`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_applicationinsights_application` | `list_applications` |

## appmesh

**Boto3 Client:** `appmesh`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_appmesh_gateway_route` | `list_gateway_routes` |
| `aws_appmesh_mesh` | `list_meshes` |
| `aws_appmesh_route` | `list_routes` |
| `aws_appmesh_virtual_gateway` | `list_virtual_gateways` |
| `aws_appmesh_virtual_node` | `list_virtual_nodes` |
| `aws_appmesh_virtual_router` | `list_virtual_routers` |
| `aws_appmesh_virtual_service` | `list_virtual_services` |

## apprunner

**Boto3 Client:** `apprunner`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_apprunner_auto_scaling_configuration_version` | `describe_auto_scaling_configuration` |
| `aws_apprunner_connection` | `list_connections` |
| `aws_apprunner_custom_domain_association` | `describe_custom_domains` |
| `aws_apprunner_default_auto_scaling_configuration_version` | `describe_auto_scaling_configuration` |
| `aws_apprunner_observability_configuration` | `list_observability_configurations` |
| `aws_apprunner_service` | `list_services` |
| `aws_apprunner_vpc_connector` | `list_vpc_connectors` |
| `aws_apprunner_vpc_ingress_connection` | `list_vpc_ingress_connections` |

## appstream

**Boto3 Client:** `appstream`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_appstream_directory_config` | `list_directory_configs` |
| `aws_appstream_fleet` | `describe_fleets` |
| `aws_appstream_fleet_stack_association` | `list_fleet_stack_associations` |
| `aws_appstream_image_builder` | `describe_image_builders` |
| `aws_appstream_stack` | `describe_stacks` |
| `aws_appstream_user` | `describe_users` |
| `aws_appstream_user_stack_association` | `list_user_stack_associations` |

## appsync

**Boto3 Client:** `appsync`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_appsync_api_cache` | `list_api_caches` |
| `aws_appsync_api_key` | `list_api_keys` |
| `aws_appsync_datasource` | `list_data_sources` |
| `aws_appsync_domain_name` | `list_domain_names` |
| `aws_appsync_domain_name_api_association` | `list_domain_name_api_associations` |
| `aws_appsync_function` | `list_functions` |
| `aws_appsync_graphql_api` | `list_graphql_apis` |
| `aws_appsync_resolver` | `list_resolvers` |
| `aws_appsync_type` | `list_types` |

## athena

**Boto3 Client:** `athena`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_athena_data_catalog` | `list_data_catalogs` |
| `aws_athena_database` | `list_databases` |
| `aws_athena_named_query` | `list_named_queries` |
| `aws_athena_prepared_statement` | `list_prepared_statements` |
| `aws_athena_workgroup` | `get_work_group` |

## auditmanager

**Boto3 Client:** `auditmanager`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_auditmanager_account_registration` | `list_account_registrations` |
| `aws_auditmanager_assessment` | `list_assessments` |
| `aws_auditmanager_assessment_delegation` | `list_assessment_delegations` |
| `aws_auditmanager_assessment_report` | `list_assessment_reports` |
| `aws_auditmanager_control` | `list_controls` |
| `aws_auditmanager_framework` | `list_frameworks` |
| `aws_auditmanager_framework_share` | `list_framework_shares` |
| `aws_auditmanager_organization_admin_account_registration` | `list_organization_admin_accounts` |

## autoscaling

**Boto3 Client:** `autoscaling`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_autoscaling_attachment` | `list_attachments` |
| `aws_autoscaling_group` | `describe_auto_scaling_groups` |
| `aws_autoscaling_group_tag` | `describe_tags` |
| `aws_autoscaling_lifecycle_hook` | `describe_lifecycle_hooks` |
| `aws_autoscaling_notification` | `list_notifications` |
| `aws_autoscaling_policy` | `describe_policies` |
| `aws_autoscaling_schedule` | `describe_scheduled_actions` |
| `aws_autoscaling_traffic_source_attachment` | `list_traffic_source_attachments` |
| `aws_launch_configuration` | `describe_launch_configurations` |

## autoscaling-plans

**Boto3 Client:** `autoscaling-plans`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_autoscalingplans_scaling_plan` | `describe_scaling_plans` |

## backup

**Boto3 Client:** `backup`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_backup_framework` | `list_frameworks` |
| `aws_backup_global_settings` | `describe_global_settings` |
| `aws_backup_plan` | `list_backup_plans` |
| `aws_backup_region_settings` | `describe_region_settings` |
| `aws_backup_report_plan` | `list_report_plans` |
| `aws_backup_selection` | `list_backup_selections` |
| `aws_backup_vault` | `list_backup_vaults` |
| `aws_backup_vault_lock_configuration` | `describe_backup_vault` |
| `aws_backup_vault_notifications` | `get_backup_vault_notifications` |
| `aws_backup_vault_policy` | `get_backup_vault_access_policy` |

## batch

**Boto3 Client:** `batch`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_batch_compute_environment` | `describe_compute_environments` |
| `aws_batch_job_definition` | `describe_job_definitions` |
| `aws_batch_job_queue` | `describe_job_queues` |
| `aws_batch_scheduling_policy` | `list_scheduling_policies` |

## bedrock

**Boto3 Client:** `bedrock`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_bedrock_guardrail` | `list_guardrails` |
| `aws_bedrock_model_invocation_logging_configuration` | `get_model_invocation_logging_configuration` |

## bedrock-agent

**Boto3 Client:** `bedrock-agent`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_bedrockagent_agent` | `list_agents` |
| `aws_bedrockagent_agent_action_group` | `list_agent_action_groups` |
| `aws_bedrockagent_agent_alias` | `list_agent_aliases` |
| `aws_bedrockagent_agent_knowledge_base_association` | `list_agent_knowledge_bases` |
| `aws_bedrockagent_data_source` | `list_data_sources` |
| `aws_bedrockagent_knowledge_base` | `list_knowledge_bases` |

## budgets

**Boto3 Client:** `budgets`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_budgets_budget` | `list_budgets` |
| `aws_budgets_budget_action` | `list_budget_actions` |

## ce

**Boto3 Client:** `ce`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_ce_anomaly_monitor` | `list_anomaly_monitors` |
| `aws_ce_anomaly_subscription` | `list_anomaly_subscriptions` |
| `aws_ce_cost_allocation_tag` | `list_cost_allocation_tags` |
| `aws_ce_cost_category` | `list_cost_categories` |

## chime-sdk-media-pipelines

**Boto3 Client:** `chime-sdk-media-pipelines`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_chimesdkmediapipelines_media_insights_pipeline_configuration` | `list_media_insights_pipelines` |

## chime-sdk-voice

**Boto3 Client:** `chime-sdk-voice`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_chime_voice_connector` | `list_voice_connectors` |
| `aws_chime_voice_connector_group` | `list_voice_connector_groups` |
| `aws_chime_voice_connector_logging` | `list_voice_connector_logging_configurations` |
| `aws_chime_voice_connector_origination` | `list_voice_connector_origination_configurations` |
| `aws_chime_voice_connector_streaming` | `list_voice_connector_streaming_configurations` |
| `aws_chime_voice_connector_termination` | `list_voice_connector_termination_configurations` |
| `aws_chime_voice_connector_termination_credentials` | `list_voice_connector_termination_credentials` |
| `aws_chimesdkvoice_global_settings` | `list_global_settings` |
| `aws_chimesdkvoice_sip_media_application` | `list_sip_media_applications` |
| `aws_chimesdkvoice_sip_rule` | `list_sip_rules` |
| `aws_chimesdkvoice_voice_profile_domain` | `list_voice_profile_domains` |

## cleanrooms

**Boto3 Client:** `cleanrooms`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_cleanrooms_collaboration` | `list_collaborations` |
| `aws_cleanrooms_configured_table` | `list_configured_tables` |

## cloudcontrol

**Boto3 Client:** `cloudcontrol`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_cloudcontrolapi_resource` | `list_resources` |

## cloudformation

**Boto3 Client:** `cloudformation`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_cloudformation_stack` | `list_stacks` |
| `aws_cloudformation_stack_set` | `list_stack_sets` |
| `aws_cloudformation_stack_set_instance` | `list_stack_set_instances` |
| `aws_cloudformation_type` | `list_types` |

## cloudfront

**Boto3 Client:** `cloudfront`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_cloudfront_cache_policy` | `list_cache_policies` |
| `aws_cloudfront_continuous_deployment_policy` | `list_continuous_deployment_policies` |
| `aws_cloudfront_distribution` | `list_distributions` |
| `aws_cloudfront_field_level_encryption_config` | `list_field_level_encryption_configs` |
| `aws_cloudfront_field_level_encryption_profile` | `list_field_level_encryption_profiles` |
| `aws_cloudfront_function` | `list_functions` |
| `aws_cloudfront_key_group` | `list_key_groups` |
| `aws_cloudfront_monitoring_subscription` | `list_monitoring_subscriptions` |
| `aws_cloudfront_origin_access_control` | `list_origin_access_controls` |
| `aws_cloudfront_origin_access_identity` | `list_cloud_front_origin_access_identities` |
| `aws_cloudfront_origin_request_policy` | `list_cloud_front_origin_access_identities` |
| `aws_cloudfront_public_key` | `list_public_keys` |
| `aws_cloudfront_realtime_log_config` | `list_realtime_log_configs` |
| `aws_cloudfront_response_headers_policy` | `list_response_headers_policies` |

## cloudsearch

**Boto3 Client:** `cloudsearch`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_cloudsearch_domain` | `list_domains` |
| `aws_cloudsearch_domain_service_access_policy` | `list_domain_service_access_policies` |

## cloudtrail

**Boto3 Client:** `cloudtrail`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_cloudtrail` | `list_trails` |
| `aws_cloudtrail_event_data_store` | `list_event_data_stores` |

## cloudwatch

**Boto3 Client:** `cloudwatch`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_cloudwatch_composite_alarm` | `list_composite_alarms` |
| `aws_cloudwatch_dashboard` | `list_dashboards` |
| `aws_cloudwatch_metric_alarm` | `describe_alarms` |
| `aws_cloudwatch_metric_stream` | `list_metric_streams` |
| `aws_cloudwatch_query_definition` | `describe_query_definitions` |

## codeartifact

**Boto3 Client:** `codeartifact`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_codeartifact_domain` | `list_domains` |
| `aws_codeartifact_domain_permissions_policy` | `list_domain_permissions_policies` |
| `aws_codeartifact_repository` | `list_repositories` |
| `aws_codeartifact_repository_permissions_policy` | `list_repository_permissions_policies` |

## codebuild

**Boto3 Client:** `codebuild`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_codebuild_project` | `list_projects` |
| `aws_codebuild_report_group` | `list_report_groups` |
| `aws_codebuild_resource_policy` | `list_resource_policies` |
| `aws_codebuild_source_credential` | `list_source_credentials` |
| `aws_codebuild_webhook` | `list_webhooks` |

## codecatalyst

**Boto3 Client:** `codecatalyst`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_codecatalyst_dev_environment` | `list_dev_environments` |
| `aws_codecatalyst_project` | `list_projects` |
| `aws_codecatalyst_source_repository` | `list_source_repositories` |

## codecommit

**Boto3 Client:** `codecommit`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_codecommit_approval_rule_template` | `list_approval_rule_templates` |
| `aws_codecommit_approval_rule_template_association` | `list_associated_approval_rule_templates` |
| `aws_codecommit_repository` | `list_repositories` |
| `aws_codecommit_trigger` | `list_repository_triggers` |

## codedeploy

**Boto3 Client:** `codedeploy`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_codedeploy_app` | `list_apps` |
| `aws_codedeploy_deployment_config` | `list_deployment_configs` |
| `aws_codedeploy_deployment_group` | `list_deployment_groups` |

## codeguru-reviewer

**Boto3 Client:** `codeguru-reviewer`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_codegurureviewer_repository_association` | `list_repository_associations` |

## codeguruprofiler

**Boto3 Client:** `codeguruprofiler`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_codeguruprofiler_profiling_group` | `list_profiling_groups` |

## codepipeline

**Boto3 Client:** `codepipeline`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_codepipeline` | `list_pipelines` |
| `aws_codepipeline_custom_action_type` | `list_custom_action_types` |
| `aws_codepipeline_webhook` | `list_webhooks` |

## codestar-connections

**Boto3 Client:** `codestar-connections`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_codestarconnections_connection` | `list_connections` |
| `aws_codestarconnections_host` | `list_hosts` |

## codestar-notifications

**Boto3 Client:** `codestar-notifications`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_codestarnotifications_notification_rule` | `list_notification_rules` |

## cognito-identity

**Boto3 Client:** `cognito-identity`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_cognito_identity_pool` | `list_identity_pools` |
| `aws_cognito_identity_pool_provider_principal_tag` | `list_identity_pool_roles` |
| `aws_cognito_identity_pool_roles_attachment` | `list_identity_pool_roles_attachments` |

## cognito-idp

**Boto3 Client:** `cognito-idp`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_cognito_identity_provider` | `list_identity_providers` |
| `aws_cognito_managed_user_pool_client` | `list_user_pool_clients` |
| `aws_cognito_resource_server` | `list_resource_servers` |
| `aws_cognito_risk_configuration` | `list_risk_configurations` |
| `aws_cognito_user` | `list_users` |
| `aws_cognito_user_group` | `list_groups` |
| `aws_cognito_user_in_group` | `list_users_in_group` |
| `aws_cognito_user_pool` | `list_user_pools` |
| `aws_cognito_user_pool_client` | `list_user_pool_clients` |
| `aws_cognito_user_pool_domain` | `list_user_pool_domains` |
| `aws_cognito_user_pool_ui_customization` | `list_user_pool_uis` |

## comprehend

**Boto3 Client:** `comprehend`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_comprehend_document_classifier` | `list_document_classifiers` |
| `aws_comprehend_entity_recognizer` | `list_entity_recognizers` |

## config

**Boto3 Client:** `config`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_config_aggregate_authorization` | `describe_aggregation_authorizations` |
| `aws_config_config_rule` | `describe_config_rules` |
| `aws_config_configuration_aggregator` | `describe_configuration_aggregators` |
| `aws_config_configuration_recorder` | `describe_configuration_recorders` |
| `aws_config_configuration_recorder_status` | `describe_configuration_recorder_status` |
| `aws_config_conformance_pack` | `describe_conformance_packs` |
| `aws_config_delivery_channel` | `describe_delivery_channels` |
| `aws_config_organization_conformance_pack` | `describe_organization_conformance_packs` |
| `aws_config_organization_custom_policy_rule` | `describe_organization_config_rules` |
| `aws_config_organization_custom_rule` | `describe_organization_config_rules` |
| `aws_config_organization_managed_rule` | `describe_organization_config_rules` |
| `aws_config_remediation_configuration` | `describe_remediation_configurations` |

## connect

**Boto3 Client:** `connect`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_connect_bot_association` | `list_bots` |
| `aws_connect_contact_flow` | `list_contact_flows` |
| `aws_connect_contact_flow_module` | `list_contact_flow_modules` |
| `aws_connect_hours_of_operation` | `list_hours_of_operations` |
| `aws_connect_instance` | `list_instances` |
| `aws_connect_instance_storage_config` | `list_instance_storage_configs` |
| `aws_connect_lambda_function_association` | `list_lambda_functions` |
| `aws_connect_phone_number` | `list_phone_numbers` |
| `aws_connect_queue` | `list_queues` |
| `aws_connect_quick_connect` | `list_quick_connects` |
| `aws_connect_routing_profile` | `list_routing_profiles` |
| `aws_connect_security_profile` | `list_security_profiles` |
| `aws_connect_user` | `list_users` |
| `aws_connect_user_hierarchy_group` | `list_user_hierarchy_groups` |
| `aws_connect_user_hierarchy_structure` | `list_user_hierarchy_structures` |
| `aws_connect_vocabulary` | `search_vocabularies` |

## controltower

**Boto3 Client:** `controltower`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_controltower_control` | `list_controls` |

## cur

**Boto3 Client:** `cur`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_cur_report_definition` | `list_report_definitions` |

## customer-profiles

**Boto3 Client:** `customer-profiles`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_customerprofiles_domain` | `list_domains` |
| `aws_customerprofiles_profile` | `list_profiles` |

## dataexchange

**Boto3 Client:** `dataexchange`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_dataexchange_data_set` | `list_data_sets` |
| `aws_dataexchange_revision` | `list_revisions` |

## datapipeline

**Boto3 Client:** `datapipeline`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_datapipeline_pipeline` | `list_pipelines` |
| `aws_datapipeline_pipeline_definition` | `list_pipeline_definition` |

## datasync

**Boto3 Client:** `datasync`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_datasync_agent` | `list_agents` |
| `aws_datasync_location_azure_blob` | `list_location_s3` |
| `aws_datasync_location_efs` | `list_location_efs` |
| `aws_datasync_location_fsx_lustre_file_system` | `list_location_fsx_lustre` |
| `aws_datasync_location_fsx_ontap_file_system` | `list_location_fsx_ontap` |
| `aws_datasync_location_fsx_openzfs_file_system` | `list_location_fsx_openzfs` |
| `aws_datasync_location_fsx_windows_file_system` | `list_location_fsx_windows` |
| `aws_datasync_location_hdfs` | `list_location_hdfs` |
| `aws_datasync_location_nfs` | `list_location_nfs` |
| `aws_datasync_location_object_storage` | `list_location_object_storage` |
| `aws_datasync_location_smb` | `list_location_smb` |
| `aws_datasync_task` | `list_tasks` |

## datazone

**Boto3 Client:** `datazone`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_datazone_asset_type` | `search_types` |
| `aws_datazone_domain` | `list_domains` |
| `aws_datazone_environment` | `list_environments` |
| `aws_datazone_environment_blueprint_configuration` | `list_environment_blueprint_configurations` |
| `aws_datazone_environment_profile` | `list_environment_profiles` |
| `aws_datazone_form_type` | `search_types` |
| `aws_datazone_glossary` | `search` |
| `aws_datazone_glossary_term` | `search` |
| `aws_datazone_project` | `list_projects` |
| `aws_datazone_user_profile` | `search_user_profiles` |

## dax

**Boto3 Client:** `dax`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_dax_cluster` | `list_clusters` |
| `aws_dax_parameter_group` | `list_parameter_groups` |
| `aws_dax_subnet_group` | `list_subnet_groups` |

## detective

**Boto3 Client:** `detective`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_detective_graph` | `list_graphs` |
| `aws_detective_invitation_accepter` | `list_invitation_accepters` |
| `aws_detective_member` | `list_members` |
| `aws_detective_organization_admin_account` | `list_organization_admin_accounts` |
| `aws_detective_organization_configuration` | `list_organization_configurations` |

## devicefarm

**Boto3 Client:** `devicefarm`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_devicefarm_device_pool` | `list_device_pools` |
| `aws_devicefarm_instance_profile` | `list_instance_profiles` |
| `aws_devicefarm_network_profile` | `list_network_profiles` |
| `aws_devicefarm_project` | `list_projects` |
| `aws_devicefarm_test_grid_project` | `list_test_grid_projects` |
| `aws_devicefarm_upload` | `list_uploads` |

## directconnect

**Boto3 Client:** `directconnect`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_dx_bgp_peer` | `describe_bgp_peers` |
| `aws_dx_connection` | `describe_connections` |
| `aws_dx_connection_association` | `describe_connection_associations` |
| `aws_dx_connection_confirmation` | `describe_confirmations` |
| `aws_dx_gateway` | `describe_gateways` |
| `aws_dx_gateway_association` | `describe_gateway_associations` |
| `aws_dx_gateway_association_proposal` | `describe_gateway_association_proposals` |
| `aws_dx_hosted_connection` | `describe_gateway_association_proposals` |
| `aws_dx_hosted_private_virtual_interface` | `describe_hosted_private_virtual_interfaces` |
| `aws_dx_hosted_private_virtual_interface_accepter` | `describe_hosted_private_virtual_interfaces` |
| `aws_dx_hosted_public_virtual_interface` | `describe_hosted_public_virtual_interfaces` |
| `aws_dx_hosted_public_virtual_interface_accepter` | `describe_hosted_public_virtual_interfaces` |
| `aws_dx_hosted_transit_virtual_interface` | `describe_hosted_transit_virtual_interfaces` |
| `aws_dx_hosted_transit_virtual_interface_accepter` | `describe_hosted_transit_virtual_interfaces` |
| `aws_dx_lag` | `describe_lags` |
| `aws_dx_macsec_key_association` | `describe_macsec_key_associations` |
| `aws_dx_private_virtual_interface` | `describe_private_virtual_interfaces` |
| `aws_dx_public_virtual_interface` | `describe_public_virtual_interfaces` |
| `aws_dx_transit_virtual_interface` | `describe_transit_virtual_interfaces` |

## dlm

**Boto3 Client:** `dlm`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_dlm_lifecycle_policy` | `list_policies` |

## dms

**Boto3 Client:** `dms`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_dms_certificate` | `describe_certificates` |
| `aws_dms_endpoint` | `describe_endpoints` |
| `aws_dms_event_subscription` | `describe_event_subscriptions` |
| `aws_dms_replication_config` | `describe_replication_configs` |
| `aws_dms_replication_instance` | `describe_replication_instances` |
| `aws_dms_replication_subnet_group` | `describe_replication_subnet_groups` |
| `aws_dms_replication_task` | `describe_replication_tasks` |

## docdb

**Boto3 Client:** `docdb`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_docdb_cluster` | `describe_db_clusters` |
| `aws_docdb_cluster_instance` | `describe_db_instances` |
| `aws_docdb_cluster_parameter_group` | `describe_db_cluster_parameter_groups` |
| `aws_docdb_cluster_snapshot` | `describe_db_cluster_snapshots` |
| `aws_docdb_event_subscription` | `describe_event_subscriptions` |
| `aws_docdb_global_cluster` | `describe_global_clusters` |
| `aws_docdb_subnet_group` | `describe_db_subnet_groups` |

## docdb-elastic

**Boto3 Client:** `docdb-elastic`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_docdbelastic_cluster` | `describe_clusters` |

## ds

**Boto3 Client:** `ds`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_directory_service_conditional_forwarder` | `list_conditional_forwarders` |
| `aws_directory_service_directory` | `describe_directories` |
| `aws_directory_service_log_subscription` | `list_log_subscriptions` |
| `aws_directory_service_radius_settings` | `list_radius_settings` |
| `aws_directory_service_region` | `list_regions` |
| `aws_directory_service_shared_directory` | `list_shared_directories` |
| `aws_directory_service_trust` | `list_trusts` |

## dynamodb

**Boto3 Client:** `dynamodb`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_dynamodb_contributor_insights` | `describe_contributor_insights` |
| `aws_dynamodb_global_table` | `describe_global_tables` |
| `aws_dynamodb_kinesis_streaming_destination` | `describe_kinesis_streaming_destination` |
| `aws_dynamodb_table` | `describe_table` |
| `aws_dynamodb_table_item` | `describe_table` |
| `aws_dynamodb_table_replica` | `describe_table_replica_auto_scaling` |
| `aws_dynamodb_tag` | `list_tags_of_resource` |

## ebs

**Boto3 Client:** `ebs`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_ebs_snapshot_copy` | `describe_snapshot_copy_grants` |
| `aws_ebs_snapshot_import` | `describe_snapshot_import_tasks` |

## ec2

**Boto3 Client:** `ec2`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_ami` | `describe_images` |
| `aws_ami_copy` | `describe_images` |
| `aws_ami_from_instance` | `describe_images` |
| `aws_ami_launch_permission` | `describe_image_attribute` |
| `aws_customer_gateway` | `describe_customer_gateways` |
| `aws_default_network_acl` | `describe_network_acls` |
| `aws_default_route_table` | `describe_route_tables` |
| `aws_default_security_group` | `describe_security_groups` |
| `aws_default_vpc_dhcp_options` | `describe_vpc_dhcp_options` |
| `aws_ebs_default_kms_key` | `get_ebs_default_kms_key_id` |
| `aws_ebs_encryption_by_default` | `get_ebs_encryption_by_default` |
| `aws_ebs_snapshot` | `describe_snapshots` |
| `aws_ebs_volume` | `describe_volumes` |
| `aws_egress_only_internet_gateway` | `describe_egress_only_internet_gateways` |
| `aws_eip` | `describe_addresses` |
| `aws_eip_association` | `describe_addresses` |
| `aws_flow_log` | `describe_flow_logs` |
| `aws_instance` | `describe_instances` |
| `aws_internet_gateway` | `describe_internet_gateways` |
| `aws_internet_gateway_attachment` | `describe_internet_gateway_attachments` |
| `aws_key_pair` | `describe_key_pairs` |
| `aws_launch_template` | `describe_launch_templates` |
| `aws_main_route_table_association` | `describe_route_tables` |
| `aws_nat_gateway` | `describe_nat_gateways` |
| `aws_network_acl` | `describe_network_acls` |
| `aws_network_acl_association` | `describe_network_acls` |
| `aws_network_acl_rule` | `describe_network_acls` |
| `aws_network_interface` | `describe_network_interfaces` |
| `aws_network_interface_attachment` | `describe_network_interfaces` |
| `aws_network_interface_sg_attachment` | `describe_network_interfaces` |
| `aws_placement_group` | `describe_placement_groups` |
| `aws_route` | `describe_route_tables` |
| `aws_route_table` | `describe_route_tables` |
| `aws_route_table_association` | `describe_route_tables` |
| `aws_security_group` | `describe_security_groups` |
| `aws_security_group_rule` | `describe_security_group_rules` |
| `aws_snapshot_create_volume_permission` | `describe_create_volume_permissions` |
| `aws_spot_datafeed_subscription` | `describe_spot_datafeed_subscription` |
| `aws_spot_fleet_request` | `describe_spot_fleet_requests` |
| `aws_spot_instance_request` | `describe_spot_instance_requests` |
| `aws_subnet` | `describe_subnets` |
| `aws_verifiedaccess_endpoint` | `describe_verified_access_endpoints` |
| `aws_verifiedaccess_group` | `describe_verified_access_groups` |
| `aws_verifiedaccess_instance` | `describe_verified_access_instances` |
| `aws_verifiedaccess_instance_logging_configuration` | `describe_verified_access_instance_logging_configurations` |
| `aws_verifiedaccess_instance_trust_provider_attachment` | `describe_verified_access_trust_providers` |
| `aws_verifiedaccess_trust_provider` | `describe_verified_access_trust_providers` |
| `aws_volume_attachment` | `describe_volume_status` |
| `aws_vpc` | `describe_vpcs` |
| `aws_vpc_dhcp_options` | `describe_dhcp_options` |
| `aws_vpc_dhcp_options_association` | `describe_dhcp_options_associations` |
| `aws_vpc_endpoint` | `describe_vpc_endpoints` |
| `aws_vpc_endpoint_connection_accepter` | `describe_vpc_endpoint_connections` |
| `aws_vpc_endpoint_connection_notification` | `describe_vpc_endpoint_connection_notifications` |
| `aws_vpc_endpoint_policy` | `describe_vpc_endpoints` |
| `aws_vpc_endpoint_route_table_association` | `describe_vpc_endpoints` |
| `aws_vpc_endpoint_security_group_association` | `describe_vpc_endpoints` |
| `aws_vpc_endpoint_service` | `describe_vpc_endpoint_services` |
| `aws_vpc_endpoint_service_allowed_principal` | `describe_vpc_endpoint_service_allowed_principals` |
| `aws_vpc_endpoint_subnet_association` | `describe_vpc_endpoint_subnet_associations` |
| `aws_vpc_ipam` | `describe_ipams` |
| `aws_vpc_ipam_organization_admin_account` | `describe_ipam_organization_admin_accounts` |
| `aws_vpc_ipam_pool` | `describe_ipam_pools` |
| `aws_vpc_ipam_pool_cidr` | `get_ipam_pool_cidrs` |
| `aws_vpc_ipam_pool_cidr_allocation` | `get_ipam_pool_allocations` |
| `aws_vpc_ipam_preview_next_cidr` | `describe_ipam_preview_next_cidrs` |
| `aws_vpc_ipam_resource_discovery` | `describe_ipam_resource_discoveries` |
| `aws_vpc_ipam_resource_discovery_association` | `describe_ipam_resource_discovery_associations` |
| `aws_vpc_ipam_scope` | `describe_ipam_scopes` |
| `aws_vpc_network_performance_metric_subscription` | `describe_network_insights_path_subscriptions` |
| `aws_vpc_peering_connection` | `describe_vpc_peering_connections` |
| `aws_vpc_peering_connection_accepter` | `describe_vpc_peering_connections` |
| `aws_vpc_peering_connection_options` | `describe_vpc_peering_connections` |
| `aws_vpc_security_group_egress_rule` | `describe_security_group_rules` |
| `aws_vpc_security_group_ingress_rule` | `describe_security_group_rules` |
| `aws_vpn_connection` | `describe_vpn_connections` |
| `aws_vpn_connection_route` | `describe_vpn_connection_routes` |
| `aws_vpn_gateway` | `describe_vpn_gateways` |
| `aws_vpn_gateway_attachment` | `describe_vpn_gateway_attachments` |
| `aws_vpn_gateway_route_propagation` | `describe_vpn_gateway_route_propagations` |

## ecr

**Boto3 Client:** `ecr`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_ecr_lifecycle_policy` | `get_lifecycle_policy` |
| `aws_ecr_pull_through_cache_rule` | `describe_pull_through_cache_rules` |
| `aws_ecr_registry_policy` | `get_registry_policy` |
| `aws_ecr_registry_scanning_configuration` | `get_registry_scanning_configuration` |
| `aws_ecr_replication_configuration` | `get_registry_policy` |
| `aws_ecr_repository` | `describe_repositories` |
| `aws_ecr_repository_policy` | `get_repository_policy` |

## ecr-public

**Boto3 Client:** `ecr-public`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_ecrpublic_repository` | `describe_repositories` |
| `aws_ecrpublic_repository_policy` | `get_repository_policy` |

## ecs

**Boto3 Client:** `ecs`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_ecs_account_setting_default` | `list_account_settings` |
| `aws_ecs_capacity_provider` | `describe_capacity_providers` |
| `aws_ecs_cluster` | `list_clusters` |
| `aws_ecs_cluster_capacity_providers` | `describe_capacity_providers` |
| `aws_ecs_service` | `list_services` |
| `aws_ecs_tag` | `list_tags_for_resource` |
| `aws_ecs_task_definition` | `describe_task_definition` |
| `aws_ecs_task_set` | `describe_task_sets` |

## efs

**Boto3 Client:** `efs`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_efs_access_point` | `describe_access_points` |
| `aws_efs_backup_policy` | `describe_backup_policy` |
| `aws_efs_file_system` | `describe_file_systems` |
| `aws_efs_file_system_policy` | `describe_file_system_policy` |
| `aws_efs_mount_target` | `describe_mount_targets` |
| `aws_efs_replication_configuration` | `describe_replication_configurations` |

## eks

**Boto3 Client:** `eks`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_eks_access_entry` | `list_access_entries` |
| `aws_eks_access_policy_association` | `list_associated_access_policies` |
| `aws_eks_addon` | `list_addons` |
| `aws_eks_cluster` | `list_clusters` |
| `aws_eks_fargate_profile` | `list_fargate_profiles` |
| `aws_eks_identity_provider_config` | `list_identity_provider_configs` |
| `aws_eks_node_group` | `list_nodegroups` |
| `aws_eks_pod_identity_association` | `list_pod_identity_associations` |

## elasticache

**Boto3 Client:** `elasticache`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_elasticache_cluster` | `describe_cache_clusters` |
| `aws_elasticache_global_replication_group` | `describe_global_replication_groups` |
| `aws_elasticache_parameter_group` | `describe_cache_parameter_groups` |
| `aws_elasticache_replication_group` | `describe_replication_groups` |
| `aws_elasticache_serverless_cache` | `describe_serverless_caches` |
| `aws_elasticache_subnet_group` | `describe_cache_subnet_groups` |
| `aws_elasticache_user` | `describe_users` |
| `aws_elasticache_user_group` | `describe_user_groups` |
| `aws_elasticache_user_group_association` | `describe_user_group_memberships` |

## elasticbeanstalk

**Boto3 Client:** `elasticbeanstalk`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_elastic_beanstalk_application` | `describe_applications` |
| `aws_elastic_beanstalk_application_version` | `describe_application_versions` |
| `aws_elastic_beanstalk_configuration_template` | `describe_configuration_settings` |
| `aws_elastic_beanstalk_environment` | `describe_environments` |

## elastictranscoder

**Boto3 Client:** `elastictranscoder`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_elastictranscoder_pipeline` | `list_pipelines` |
| `aws_elastictranscoder_preset` | `list_presets` |

## elb

**Boto3 Client:** `elb`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_app_cookie_stickiness_policy` | `describe_load_balancers` |
| `aws_elb` | `describe_load_balancers` |
| `aws_elb_attachment` | `describe_load_balancer_attributes` |

## elbv2

**Boto3 Client:** `elbv2`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_lb` | `describe_load_balancers` |
| `aws_lb_cookie_stickiness_policy` | `describe_load_balancers` |
| `aws_lb_listener` | `describe_listeners` |
| `aws_lb_listener_certificate` | `describe_listener_certificates` |
| `aws_lb_listener_rule` | `describe_rules` |
| `aws_lb_ssl_negotiation_policy` | `describe_ssl_policies` |
| `aws_lb_target_group` | `describe_target_groups` |
| `aws_lb_target_group_attachment` | `describe_target_group_attributes` |
| `aws_lb_trust_store` | `describe_load_balancer_attributes` |
| `aws_lb_trust_store_revocation` | `describe_load_balancer_attributes` |
| `aws_load_balancer_backend_server_policy` | `describe_backend_server_policies` |
| `aws_load_balancer_listener_policy` | `describe_listeners` |
| `aws_load_balancer_policy` | `describe_load_balancer_policies` |

## emr

**Boto3 Client:** `emr`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_emr_block_public_access_configuration` | `describe_block_public_access_configurations` |
| `aws_emr_cluster` | `list_clusters` |
| `aws_emr_instance_fleet` | `describe_instance_fleets` |
| `aws_emr_instance_group` | `list_instance_groups` |
| `aws_emr_managed_scaling_policy` | `get_managed_scaling_policy` |
| `aws_emr_security_configuration` | `list_security_configurations` |
| `aws_emr_studio` | `describe_studios` |
| `aws_emr_studio_session_mapping` | `describe_studio_session_mappings` |

## emr-containers

**Boto3 Client:** `emr-containers`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_emrcontainers_job_template` | `list_job_templates` |
| `aws_emrcontainers_virtual_cluster` | `list_virtual_clusters` |

## emr-serverless

**Boto3 Client:** `emr-serverless`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_emrserverless_application` | `list_applications` |

## es

**Boto3 Client:** `es`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_elasticsearch_domain` | `describe_elasticsearch_domains` |
| `aws_elasticsearch_domain_policy` | `describe_elasticsearch_domain_policy` |
| `aws_elasticsearch_vpc_endpoint` | `describe_vpc_endpoints` |

## events

**Boto3 Client:** `events`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_cloudwatch_event_api_destination` | `list_api_destinations` |
| `aws_cloudwatch_event_archive` | `list_archives` |
| `aws_cloudwatch_event_bus` | `list_event_buses` |
| `aws_cloudwatch_event_bus_policy` | `list_event_bus_policies` |
| `aws_cloudwatch_event_connection` | `list_connections` |
| `aws_cloudwatch_event_endpoint` | `list_endpoints` |
| `aws_cloudwatch_event_permission` | `list_permissions` |
| `aws_cloudwatch_event_rule` | `list_rules` |
| `aws_cloudwatch_event_target` | `list_targets_by_rule` |

## evidently

**Boto3 Client:** `evidently`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_evidently_feature` | `list_features` |
| `aws_evidently_launch` | `list_launches` |
| `aws_evidently_project` | `list_projects` |
| `aws_evidently_segment` | `list_segments` |

## finspace

**Boto3 Client:** `finspace`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_finspace_kx_cluster` | `list_clusters` |
| `aws_finspace_kx_database` | `list_databases` |
| `aws_finspace_kx_dataview` | `list_data_views` |
| `aws_finspace_kx_environment` | `list_environments` |
| `aws_finspace_kx_scaling_group` | `list_scaling_groups` |
| `aws_finspace_kx_user` | `list_users` |
| `aws_finspace_kx_volume` | `list_volumes` |

## firehose

**Boto3 Client:** `firehose`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_kinesis_firehose_delivery_stream` | `list_delivery_streams` |

## fis

**Boto3 Client:** `fis`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_fis_experiment_template` | `list_experiment_templates` |

## fms

**Boto3 Client:** `fms`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_fms_admin_account` | `list_admin_accounts` |
| `aws_fms_policy` | `list_policies` |

## fsx

**Boto3 Client:** `fsx`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_fsx_backup` | `describe_backups` |
| `aws_fsx_data_repository_association` | `describe_data_repository_associations` |
| `aws_fsx_file_cache` | `describe_file_caches` |
| `aws_fsx_lustre_file_system` | `describe_file_systems` |
| `aws_fsx_ontap_file_system` | `describe_file_systems` |
| `aws_fsx_ontap_storage_virtual_machine` | `describe_storage_virtual_machines` |
| `aws_fsx_ontap_volume` | `describe_volumes` |
| `aws_fsx_openzfs_file_system` | `describe_file_systems` |
| `aws_fsx_openzfs_snapshot` | `describe_snapshots` |
| `aws_fsx_openzfs_volume` | `describe_volumes` |
| `aws_fsx_windows_file_system` | `describe_file_systems` |

## gamelift

**Boto3 Client:** `gamelift`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_gamelift_alias` | `list_aliases` |
| `aws_gamelift_build` | `list_builds` |
| `aws_gamelift_fleet` | `list_fleets` |
| `aws_gamelift_game_server_group` | `list_game_server_groups` |
| `aws_gamelift_game_session_queue` | `list_game_session_queues` |
| `aws_gamelift_script` | `list_scripts` |

## glacier

**Boto3 Client:** `glacier`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_glacier_vault` | `list_vaults` |
| `aws_glacier_vault_lock` | `list_vault_locks` |

## globalaccelerator

**Boto3 Client:** `globalaccelerator`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_globalaccelerator_accelerator` | `list_accelerators` |
| `aws_globalaccelerator_custom_routing_accelerator` | `list_accelerators` |
| `aws_globalaccelerator_custom_routing_endpoint_group` | `list_endpoint_groups` |
| `aws_globalaccelerator_custom_routing_listener` | `list_listeners` |
| `aws_globalaccelerator_endpoint_group` | `list_endpoint_groups` |
| `aws_globalaccelerator_listener` | `list_listeners` |

## glue

**Boto3 Client:** `glue`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_glue_catalog_database` | `get_databases` |
| `aws_glue_catalog_table` | `get_tables` |
| `aws_glue_classifier` | `get_classifiers` |
| `aws_glue_connection` | `get_connections` |
| `aws_glue_crawler` | `get_crawlers` |
| `aws_glue_data_catalog_encryption_settings` | `get_data_catalog_encryption_settings` |
| `aws_glue_data_quality_ruleset` | `list_data_quality_rulesets` |
| `aws_glue_dev_endpoint` | `list_dev_endpoints` |
| `aws_glue_job` | `list_jobs` |
| `aws_glue_ml_transform` | `list_ml_transforms` |
| `aws_glue_partition` | `list_partitions` |
| `aws_glue_partition_index` | `list_partition_indexes` |
| `aws_glue_registry` | `list_registries` |
| `aws_glue_resource_policy` | `list_resource_policies` |
| `aws_glue_schema` | `list_schemas` |
| `aws_glue_security_configuration` | `get_security_configurations` |
| `aws_glue_trigger` | `get_trigger` |
| `aws_glue_user_defined_function` | `list_user_defined_functions` |
| `aws_glue_workflow` | `list_workflows` |

## grafana

**Boto3 Client:** `grafana`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_grafana_license_association` | `list_license_associations` |
| `aws_grafana_role_association` | `list_role_associations` |
| `aws_grafana_workspace` | `list_workspaces` |
| `aws_grafana_workspace_api_key` | `list_workspace_api_keys` |
| `aws_grafana_workspace_saml_configuration` | `describe_workspace_authentication` |

## guardduty

**Boto3 Client:** `guardduty`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_guardduty_detector` | `list_detectors` |
| `aws_guardduty_detector_feature` | `list_detector_features` |
| `aws_guardduty_filter` | `list_filters` |
| `aws_guardduty_invite_accepter` | `list_invitation_accepters` |
| `aws_guardduty_ipset` | `list_ip_sets` |
| `aws_guardduty_member` | `list_members` |
| `aws_guardduty_organization_admin_account` | `list_organization_admin_accounts` |
| `aws_guardduty_organization_configuration` | `list_organization_configurations` |
| `aws_guardduty_organization_configuration_feature` | `list_organization_configuration_features` |
| `aws_guardduty_publishing_destination` | `list_publishing_destinations` |
| `aws_guardduty_threatintelset` | `list_threat_intel_sets` |

## iam

**Boto3 Client:** `iam`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_iam_access_key` | `list_access_keys` |
| `aws_iam_account_alias` | `list_account_aliases` |
| `aws_iam_account_password_policy` | `get_account_password_policy` |
| `aws_iam_group` | `list_groups` |
| `aws_iam_group_membership` | `get_group` |
| `aws_iam_group_policy` | `list_group_policies` |
| `aws_iam_group_policy_attachment` | `list_attached_group_policies` |
| `aws_iam_instance_profile` | `get_instance_profile` |
| `aws_iam_openid_connect_provider` | `list_open_id_connect_providers` |
| `aws_iam_policy` | `list_policies` |
| `aws_iam_policy_attachment` | `get_policy` |
| `aws_iam_role` | `list_roles` |
| `aws_iam_role_policy` | `list_role_policies` |
| `aws_iam_role_policy_attachment` | `list_attached_role_policies` |
| `aws_iam_saml_provider` | `list_saml_providers` |
| `aws_iam_security_token_service_preferences` | `get_account_token_version` |
| `aws_iam_server_certificate` | `list_server_certificates` |
| `aws_iam_service_linked_role` | `list_roles` |
| `aws_iam_service_specific_credential` | `list_service_specific_credentials` |
| `aws_iam_signing_certificate` | `list_signing_certificates` |
| `aws_iam_user` | `list_users` |
| `aws_iam_user_group_membership` | `get_group` |
| `aws_iam_user_login_profile` | `get_login_profile` |
| `aws_iam_user_policy` | `list_user_policies` |
| `aws_iam_user_policy_attachment` | `list_attached_user_policies` |
| `aws_iam_user_ssh_key` | `list_ssh_public_keys` |
| `aws_iam_virtual_mfa_device` | `list_virtual_mfa_devices` |

## identitystore

**Boto3 Client:** `identitystore`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_identitystore_group` | `list_groups` |
| `aws_identitystore_group_membership` | `list_group_memberships` |
| `aws_identitystore_user` | `list_users` |

## imagebuilder

**Boto3 Client:** `imagebuilder`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_imagebuilder_component` | `list_components` |
| `aws_imagebuilder_container_recipe` | `list_container_recipes` |
| `aws_imagebuilder_distribution_configuration` | `list_distribution_configurations` |
| `aws_imagebuilder_image` | `list_images` |
| `aws_imagebuilder_image_pipeline` | `list_image_pipelines` |
| `aws_imagebuilder_image_recipe` | `list_image_recipes` |
| `aws_imagebuilder_infrastructure_configuration` | `list_infrastructure_configurations` |

## inspector

**Boto3 Client:** `inspector`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_inspector_assessment_target` | `list_assessment_targets` |
| `aws_inspector_assessment_template` | `list_assessment_templates` |
| `aws_inspector_resource_group` | `list_resource_groups` |

## internetmonitor

**Boto3 Client:** `internetmonitor`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_internetmonitor_monitor` | `list_monitors` |

## iot

**Boto3 Client:** `iot`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_iot_authorizer` | `list_authorizers` |
| `aws_iot_billing_group` | `list_billing_groups` |
| `aws_iot_ca_certificate` | `list_ca_certificates` |
| `aws_iot_certificate` | `list_certificates` |
| `aws_iot_domain_configuration` | `list_domain_configurations` |
| `aws_iot_event_configurations` | `list_event_configurations` |
| `aws_iot_indexing_configuration` | `list_indexing_configurations` |
| `aws_iot_logging_options` | `describe_logging_options` |
| `aws_iot_policy` | `list_policies` |
| `aws_iot_policy_attachment` | `list_policies` |
| `aws_iot_provisioning_template` | `list_provisioning_templates` |
| `aws_iot_role_alias` | `list_role_aliases` |
| `aws_iot_thing` | `list_things` |
| `aws_iot_thing_group` | `list_thing_groups` |
| `aws_iot_thing_group_membership` | `list_thing_group_memberships` |
| `aws_iot_thing_principal_attachment` | `list_thing_principal_attachments` |
| `aws_iot_thing_type` | `list_thing_types` |
| `aws_iot_topic_rule` | `list_topic_rules` |
| `aws_iot_topic_rule_destination` | `list_topic_rule_destinations` |

## ivs

**Boto3 Client:** `ivs`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_ivs_channel` | `list_channels` |
| `aws_ivs_playback_key_pair` | `list_playback_key_pairs` |
| `aws_ivs_recording_configuration` | `list_recording_configurations` |

## ivschat

**Boto3 Client:** `ivschat`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_ivschat_logging_configuration` | `list_logging_configurations` |
| `aws_ivschat_room` | `list_rooms` |

## kafka

**Boto3 Client:** `kafka`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_msk_cluster` | `list_clusters_v2` |
| `aws_msk_cluster_policy` | `list_cluster_policies` |
| `aws_msk_configuration` | `list_configurations` |
| `aws_msk_replicator` | `list_replicators` |
| `aws_msk_scram_secret_association` | `list_scram_secrets` |
| `aws_msk_serverless_cluster` | `list_clusters_v2` |
| `aws_msk_vpc_connection` | `list_vpc_connections` |

## kafkaconnect

**Boto3 Client:** `kafkaconnect`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_mskconnect_connector` | `list_connectors` |
| `aws_mskconnect_custom_plugin` | `list_custom_plugins` |
| `aws_mskconnect_worker_configuration` | `list_worker_configurations` |

## kendra

**Boto3 Client:** `kendra`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_kendra_data_source` | `list_data_sources` |
| `aws_kendra_experience` | `list_experiences` |
| `aws_kendra_faq` | `list_faqs` |
| `aws_kendra_index` | `list_indices` |
| `aws_kendra_query_suggestions_block_list` | `list_query_suggestions_block_lists` |
| `aws_kendra_thesaurus` | `list_thesauri` |

## keyspaces

**Boto3 Client:** `keyspaces`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_keyspaces_keyspace` | `list_keyspaces` |
| `aws_keyspaces_table` | `list_tables` |

## kinesis

**Boto3 Client:** `kinesis`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_kinesis_stream` | `list_streams` |
| `aws_kinesis_stream_consumer` | `list_stream_consumers` |

## kinesisanalytics

**Boto3 Client:** `kinesisanalytics`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_kinesis_analytics_application` | `list_applications` |

## kinesisvideo

**Boto3 Client:** `kinesisvideo`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_kinesis_video_stream` | `list_streams` |

## kms

**Boto3 Client:** `kms`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_kms_alias` | `list_aliases` |
| `aws_kms_ciphertext` | `list_grants` |
| `aws_kms_custom_key_store` | `describe_custom_key_stores` |
| `aws_kms_external_key` | `list_keys` |
| `aws_kms_grant` | `list_grants` |
| `aws_kms_key` | `list_keys` |
| `aws_kms_key_policy` | `list_key_policies` |
| `aws_kms_replica_external_key` | `list_keys` |
| `aws_kms_replica_key` | `list_keys` |

## lakeformation

**Boto3 Client:** `lakeformation`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_lakeformation_data_lake_settings` | `get_data_lake_settings` |
| `aws_lakeformation_lf_tag` | `list_lf_tags` |
| `aws_lakeformation_permissions` | `list_permissions` |
| `aws_lakeformation_resource` | `list_resources` |
| `aws_lakeformation_resource_lf_tags` | `list_resource_lf_tags` |

## lambda

**Boto3 Client:** `lambda`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_lambda_alias` | `list_aliases` |
| `aws_lambda_code_signing_config` | `list_code_signing_configs` |
| `aws_lambda_event_source_mapping` | `list_event_source_mappings` |
| `aws_lambda_function` | `list_functions` |
| `aws_lambda_function_event_invoke_config` | `list_function_event_invoke_configs` |
| `aws_lambda_function_url` | `list_function_url_configs` |
| `aws_lambda_invocation` | `list_functions` |
| `aws_lambda_layer_version` | `list_layer_versions` |
| `aws_lambda_layer_version_permission` | `list_layer_versions` |
| `aws_lambda_permission` | `get_policy` |
| `aws_lambda_provisioned_concurrency_config` | `list_provisioned_concurrency_configs` |

## lex-models

**Boto3 Client:** `lex-models`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_lex_bot` | `get_bots` |
| `aws_lex_bot_alias` | `get_bot_aliases` |
| `aws_lex_intent` | `get_intents` |
| `aws_lex_slot_type` | `get_slot_types` |

## license-manager

**Boto3 Client:** `license-manager`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_licensemanager_association` | `list_associations` |
| `aws_licensemanager_grant` | `list_grants` |
| `aws_licensemanager_grant_accepter` | `list_grant_accepters` |
| `aws_licensemanager_license_configuration` | `list_license_configurations` |

## lightsail

**Boto3 Client:** `lightsail`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_lightsail_bucket` | `get_buckets` |
| `aws_lightsail_bucket_access_key` | `get_bucket_access_keys` |
| `aws_lightsail_bucket_resource_access` | `get_bucket_resources` |
| `aws_lightsail_certificate` | `get_certificates` |
| `aws_lightsail_container_service` | `get_container_services` |
| `aws_lightsail_container_service_deployment_version` | `get_container_service_deployments` |
| `aws_lightsail_database` | `get_databases` |
| `aws_lightsail_disk` | `get_disks` |
| `aws_lightsail_disk_attachment` | `get_disk_attachments` |
| `aws_lightsail_distribution` | `get_distributions` |
| `aws_lightsail_domain` | `get_domains` |
| `aws_lightsail_domain_entry` | `get_domain_entries` |
| `aws_lightsail_instance` | `get_instances` |
| `aws_lightsail_instance_public_ports` | `get_instance_public_ports` |
| `aws_lightsail_key_pair` | `get_instance_public_ports` |
| `aws_lightsail_lb` | `get_key_pairs` |
| `aws_lightsail_lb_attachment` | `get_load_balancers` |
| `aws_lightsail_lb_certificate` | `get_key_pairs` |
| `aws_lightsail_lb_certificate_attachment` | `get_load_balancer_certificates` |
| `aws_lightsail_lb_https_redirection_policy` | `get_key_pairs` |
| `aws_lightsail_lb_stickiness_policy` | `get_load_balancer_https_redirection_policies` |
| `aws_lightsail_static_ip` | `get_key_pairs` |
| `aws_lightsail_static_ip_attachment` | `get_static_ips` |

## location

**Boto3 Client:** `location`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_location_geofence_collection` | `list_geofence_collections` |
| `aws_location_map` | `list_maps` |
| `aws_location_place_index` | `list_place_indexes` |
| `aws_location_route_calculator` | `list_route_calculators` |
| `aws_location_tracker` | `list_trackers` |
| `aws_location_tracker_association` | `list_tracker_associations` |

## logs

**Boto3 Client:** `logs`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_cloudwatch_log_data_protection_policy` | `list_data_protection_policies` |
| `aws_cloudwatch_log_destination` | `describe_destinations` |
| `aws_cloudwatch_log_destination_policy` | `list_destination_policies` |
| `aws_cloudwatch_log_group` | `describe_log_groups` |
| `aws_cloudwatch_log_metric_filter` | `list_metric_filters` |
| `aws_cloudwatch_log_resource_policy` | `list_resource_policies` |
| `aws_cloudwatch_log_stream` | `describe_log_streams` |
| `aws_cloudwatch_log_subscription_filter` | `list_subscription_filters` |

## mediaconvert

**Boto3 Client:** `mediaconvert`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_media_convert_queue` | `list_queues` |

## medialive

**Boto3 Client:** `medialive`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_medialive_channel` | `list_channels` |
| `aws_medialive_input` | `list_inputs` |
| `aws_medialive_input_security_group` | `list_input_security_groups` |
| `aws_medialive_multiplex` | `list_multiplexes` |
| `aws_medialive_multiplex_program` | `list_multiplex_programs` |

## mediapackage

**Boto3 Client:** `mediapackage`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_media_package_channel` | `list_channels` |

## mediastore

**Boto3 Client:** `mediastore`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_media_store_container` | `list_containers` |
| `aws_media_store_container_policy` | `list_container_policies` |

## memorydb

**Boto3 Client:** `memorydb`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_memorydb_acl` | `list_acls` |
| `aws_memorydb_cluster` | `list_clusters` |
| `aws_memorydb_parameter_group` | `list_parameter_groups` |
| `aws_memorydb_snapshot` | `list_snapshots` |
| `aws_memorydb_subnet_group` | `list_subnet_groups` |
| `aws_memorydb_user` | `list_users` |

## mq

**Boto3 Client:** `mq`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_mq_broker` | `list_brokers` |
| `aws_mq_configuration` | `list_configurations` |

## mwaa

**Boto3 Client:** `mwaa`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_mwaa_environment` | `list_environments` |

## neptune

**Boto3 Client:** `neptune`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_neptune_cluster` | `describe_db_clusters` |
| `aws_neptune_cluster_endpoint` | `describe_db_cluster_endpoints` |
| `aws_neptune_cluster_instance` | `describe_db_cluster_instances` |
| `aws_neptune_cluster_parameter_group` | `describe_db_cluster_parameter_groups` |
| `aws_neptune_cluster_snapshot` | `describe_db_cluster_snapshots` |
| `aws_neptune_event_subscription` | `describe_event_subscriptions` |
| `aws_neptune_global_cluster` | `describe_global_clusters` |
| `aws_neptune_parameter_group` | `describe_db_parameter_groups` |
| `aws_neptune_subnet_group` | `describe_db_subnet_groups` |

## network-firewall

**Boto3 Client:** `network-firewall`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_networkfirewall_firewall` | `list_firewalls` |
| `aws_networkfirewall_firewall_policy` | `list_firewall_policies` |
| `aws_networkfirewall_logging_configuration` | `list_logging_configurations` |
| `aws_networkfirewall_resource_policy` | `list_resource_policies` |
| `aws_networkfirewall_rule_group` | `list_rule_groups` |

## networkmanager

**Boto3 Client:** `networkmanager`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_networkmanager_attachment_accepter` | `list_attachment_accepters` |
| `aws_networkmanager_connect_attachment` | `list_connect_attachments` |
| `aws_networkmanager_connect_peer` | `list_connect_peers` |
| `aws_networkmanager_connection` | `list_connections` |
| `aws_networkmanager_core_network` | `list_core_networks` |
| `aws_networkmanager_core_network_policy_attachment` | `list_core_network_policy_attachments` |
| `aws_networkmanager_customer_gateway_association` | `list_customer_gateway_associations` |
| `aws_networkmanager_device` | `get_devices` |
| `aws_networkmanager_global_network` | `describe_global_networks` |
| `aws_networkmanager_link` | `list_links` |
| `aws_networkmanager_link_association` | `list_link_associations` |
| `aws_networkmanager_site` | `get_sites` |
| `aws_networkmanager_site_to_site_vpn_attachment` | `list_site_to_site_vpn_attachments` |
| `aws_networkmanager_transit_gateway_connect_peer_association` | `list_transit_gateway_connect_peers` |
| `aws_networkmanager_transit_gateway_peering` | `list_transit_gateway_peerings` |
| `aws_networkmanager_transit_gateway_registration` | `get_transit_gateway_registrations` |
| `aws_networkmanager_transit_gateway_route_table_attachment` | `list_transit_gateway_route_tables` |
| `aws_networkmanager_vpc_attachment` | `list_vpc_attachments` |
| `aws_oam_link` | `list_links` |
| `aws_oam_sink` | `list_links` |
| `aws_oam_sink_policy` | `list_links` |

## opensearch

**Boto3 Client:** `opensearch`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_opensearch_domain` | `list_domain_names` |
| `aws_opensearch_domain_policy` | `list_domain_names` |
| `aws_opensearch_domain_saml_options` | `list_domain_names` |
| `aws_opensearch_inbound_connection_accepter` | `list_inbound_connection_accepters` |
| `aws_opensearch_outbound_connection` | `list_inbound_connection_accepters` |
| `aws_opensearch_package` | `list_packages` |
| `aws_opensearch_package_association` | `list_packages` |
| `aws_opensearch_vpc_endpoint` | `list_vpc_endpoints` |

## opensearchserverless

**Boto3 Client:** `opensearchserverless`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_opensearchserverless_access_policy` | `list_access_policies` |
| `aws_opensearchserverless_collection` | `list_collections` |
| `aws_opensearchserverless_lifecycle_policy` | `list_lifecycle_policies` |
| `aws_opensearchserverless_security_config` | `list_security_configs` |
| `aws_opensearchserverless_security_policy` | `list_security_policies` |
| `aws_opensearchserverless_vpc_endpoint` | `list_vpc_endpoints` |

## opsworks

**Boto3 Client:** `opsworks`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_opsworks_application` | `list_applications` |
| `aws_opsworks_custom_layer` | `list_custom_layers` |
| `aws_opsworks_ecs_cluster_layer` | `describe_ecs_clusters` |
| `aws_opsworks_ganglia_layer` | `list_ganglia_layers` |
| `aws_opsworks_haproxy_layer` | `list_haproxy_layers` |
| `aws_opsworks_instance` | `list_instances` |
| `aws_opsworks_java_app_layer` | `list_java_app_layers` |
| `aws_opsworks_memcached_layer` | `list_memcached_layers` |
| `aws_opsworks_mysql_layer` | `list_mysql_layers` |
| `aws_opsworks_nodejs_app_layer` | `list_nodejs_app_layers` |
| `aws_opsworks_permission` | `list_permissions` |
| `aws_opsworks_php_app_layer` | `list_php_app_layers` |
| `aws_opsworks_rails_app_layer` | `list_rails_app_layers` |
| `aws_opsworks_rds_db_instance` | `list_rds_db_instances` |
| `aws_opsworks_stack` | `list_stacks` |
| `aws_opsworks_static_web_layer` | `list_static_web_layers` |
| `aws_opsworks_user_profile` | `list_user_profiles` |

## organizations

**Boto3 Client:** `organizations`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_account_alternate_contact` | `describe_account` |
| `aws_account_primary_contact` | `describe_account` |
| `aws_organizations_account` | `list_accounts` |
| `aws_organizations_delegated_administrator` | `list_delegated_administrators` |
| `aws_organizations_organization` | `describe_organization` |
| `aws_organizations_organizational_unit` | `describe_organizational_unit` |
| `aws_organizations_policy` | `list_policies` |
| `aws_organizations_policy_attachment` | `list_targets_for_policy` |
| `aws_organizations_resource_policy` | `describe_resource_policy` |

## pinpoint

**Boto3 Client:** `pinpoint`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_pinpoint_adm_channel` | `list_adm_channels` |
| `aws_pinpoint_apns_channel` | `list_apns_channels` |
| `aws_pinpoint_apns_sandbox_channel` | `list_apns_sandbox_channels` |
| `aws_pinpoint_apns_voip_channel` | `list_apns_voip_channels` |
| `aws_pinpoint_apns_voip_sandbox_channel` | `list_apns_voip_sandbox_channels` |
| `aws_pinpoint_app` | `list_apps` |
| `aws_pinpoint_baidu_channel` | `list_baidu_channels` |
| `aws_pinpoint_email_channel` | `list_email_channels` |
| `aws_pinpoint_event_stream` | `list_event_streams` |
| `aws_pinpoint_gcm_channel` | `list_gcm_channels` |
| `aws_pinpoint_sms_channel` | `list_sms_channels` |

## pipes

**Boto3 Client:** `pipes`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_pipes_pipe` | `list_pipes` |

## qldb

**Boto3 Client:** `qldb`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_qldb_ledger` | `list_ledgers` |
| `aws_qldb_stream` | `list_streams` |

## quicksight

**Boto3 Client:** `quicksight`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_quicksight_account_subscription` | `list_account_subscriptions` |
| `aws_quicksight_analysis` | `list_analyses` |
| `aws_quicksight_dashboard` | `list_dashboards` |
| `aws_quicksight_data_set` | `list_data_sets` |
| `aws_quicksight_data_source` | `list_data_sources` |
| `aws_quicksight_folder` | `list_folders` |
| `aws_quicksight_folder_membership` | `list_folder_memberships` |
| `aws_quicksight_group` | `list_groups` |
| `aws_quicksight_group_membership` | `list_group_memberships` |
| `aws_quicksight_iam_policy_assignment` | `list_iam_policy_assignments` |
| `aws_quicksight_ingestion` | `list_ingestions` |
| `aws_quicksight_namespace` | `list_namespaces` |
| `aws_quicksight_refresh_schedule` | `list_refresh_schedules` |
| `aws_quicksight_template` | `list_templates` |
| `aws_quicksight_template_alias` | `list_template_aliases` |
| `aws_quicksight_theme` | `list_themes` |
| `aws_quicksight_user` | `list_users` |
| `aws_quicksight_vpc_connection` | `list_vpc_connections` |

## ram

**Boto3 Client:** `ram`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_ram_principal_association` | `list_principals` |
| `aws_ram_resource_association` | `list_resources` |
| `aws_ram_resource_share` | `list_resources` |
| `aws_ram_resource_share_accepter` | `list_resource_share_accepters` |
| `aws_ram_sharing_with_organization` | `list_sharing_accounts` |

## rbin

**Boto3 Client:** `rbin`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_rbin_rule` | `list_resolver_rules` |

## rds

**Boto3 Client:** `rds`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_db_cluster_snapshot` | `describe_db_cluster_snapshots` |
| `aws_db_event_subscription` | `describe_event_subscriptions` |
| `aws_db_instance` | `describe_db_instances` |
| `aws_db_instance_automated_backups_replication` | `describe_db_instance_automated_backups` |
| `aws_db_instance_role_association` | `describe_db_instance_role_associations` |
| `aws_db_option_group` | `describe_option_groups` |
| `aws_db_parameter_group` | `describe_db_parameter_groups` |
| `aws_db_proxy` | `describe_db_proxies` |
| `aws_db_proxy_default_target_group` | `describe_db_proxy_default_target_groups` |
| `aws_db_proxy_endpoint` | `describe_db_proxy_endpoints` |
| `aws_db_proxy_target` | `describe_db_proxy_targets` |
| `aws_db_snapshot` | `describe_db_snapshots` |
| `aws_db_snapshot_copy` | `describe_db_snapshot_attributes` |
| `aws_db_subnet_group` | `describe_db_subnet_groups` |
| `aws_rds_cluster` | `describe_db_clusters` |
| `aws_rds_cluster_activity_stream` | `describe_db_clusters` |
| `aws_rds_cluster_endpoint` | `describe_db_cluster_endpoints` |
| `aws_rds_cluster_instance` | `describe_db_instances` |
| `aws_rds_cluster_parameter_group` | `describe_db_cluster_parameter_groups` |
| `aws_rds_cluster_role_association` | `describe_db_clusters` |
| `aws_rds_custom_db_engine_version` | `describe_db_engine_versions` |
| `aws_rds_export_task` | `describe_export_tasks` |
| `aws_rds_global_cluster` | `describe_global_clusters` |
| `aws_rds_reserved_instance` | `describe_reserved_db_instances` |

## redshift

**Boto3 Client:** `redshift`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_redshift_authentication_profile` | `describe_authentication_profiles` |
| `aws_redshift_cluster` | `describe_clusters` |
| `aws_redshift_cluster_iam_roles` | `describe_clusters` |
| `aws_redshift_cluster_snapshot` | `describe_cluster_snapshots` |
| `aws_redshift_endpoint_access` | `describe_endpoint_access` |
| `aws_redshift_endpoint_authorization` | `describe_endpoint_authorization` |
| `aws_redshift_event_subscription` | `describe_event_subscriptions` |
| `aws_redshift_hsm_client_certificate` | `describe_hsm_client_certificates` |
| `aws_redshift_hsm_configuration` | `describe_hsm_configurations` |
| `aws_redshift_parameter_group` | `describe_cluster_parameter_groups` |
| `aws_redshift_partner` | `describe_partners` |
| `aws_redshift_resource_policy` | `get_resource_policy` |
| `aws_redshift_scheduled_action` | `describe_scheduled_actions` |
| `aws_redshift_snapshot_copy_grant` | `describe_snapshot_copy_grants` |
| `aws_redshift_snapshot_schedule` | `describe_snapshot_schedules` |
| `aws_redshift_snapshot_schedule_association` | `describe_snapshot_schedules` |
| `aws_redshift_subnet_group` | `describe_cluster_subnet_groups` |
| `aws_redshift_usage_limit` | `describe_usage_limits` |

## redshift-data

**Boto3 Client:** `redshift-data`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_redshiftdata_statement` | `describe_statement` |

## redshift-serverless

**Boto3 Client:** `redshift-serverless`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_redshiftserverless_endpoint_access` | `describe_endpoint_access` |
| `aws_redshiftserverless_namespace` | `list_namespaces` |
| `aws_redshiftserverless_resource_policy` | `describe_resource_policies` |
| `aws_redshiftserverless_snapshot` | `describe_snapshots` |
| `aws_redshiftserverless_usage_limit` | `describe_usage_limits` |
| `aws_redshiftserverless_workgroup` | `list_workgroups` |

## resource-groups

**Boto3 Client:** `resource-groups`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_resourcegroups_group` | `list_groups` |
| `aws_resourcegroups_resource` | `list_resources` |

## rolesanywhere

**Boto3 Client:** `rolesanywhere`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_rolesanywhere_profile` | `list_profiles` |
| `aws_rolesanywhere_trust_anchor` | `list_trust_anchors` |

## rum

**Boto3 Client:** `rum`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_rum_app_monitor` | `list_app_monitors` |
| `aws_rum_metrics_destination` | `list_metrics_destinations` |

## sagemaker

**Boto3 Client:** `sagemaker`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_sagemaker_app` | `list_apps` |
| `aws_sagemaker_app_image_config` | `list_app_image_configs` |
| `aws_sagemaker_code_repository` | `list_code_repositories` |
| `aws_sagemaker_data_quality_job_definition` | `list_data_quality_job_definitions` |
| `aws_sagemaker_device` | `list_devices` |
| `aws_sagemaker_device_fleet` | `list_device_fleets` |
| `aws_sagemaker_domain` | `list_domains` |
| `aws_sagemaker_endpoint` | `list_endpoints` |
| `aws_sagemaker_endpoint_configuration` | `list_endpoint_configurations` |
| `aws_sagemaker_feature_group` | `list_feature_groups` |
| `aws_sagemaker_flow_definition` | `list_flow_definitions` |
| `aws_sagemaker_human_task_ui` | `list_human_task_uis` |
| `aws_sagemaker_image` | `list_images` |
| `aws_sagemaker_image_version` | `list_image_versions` |
| `aws_sagemaker_model` | `list_models` |
| `aws_sagemaker_model_package_group` | `list_model_package_groups` |
| `aws_sagemaker_model_package_group_policy` | `get_model_package_group_policy` |
| `aws_sagemaker_monitoring_schedule` | `list_monitoring_schedules` |
| `aws_sagemaker_notebook_instance` | `list_notebook_instances` |
| `aws_sagemaker_notebook_instance_lifecycle_configuration` | `list_notebook_instance_lifecycle_configs` |
| `aws_sagemaker_pipeline` | `list_pipelines` |
| `aws_sagemaker_project` | `list_projects` |
| `aws_sagemaker_servicecatalog_portfolio_status` | `get_service_catalog_portfolio_status` |
| `aws_sagemaker_space` | `list_spaces` |
| `aws_sagemaker_studio_lifecycle_config` | `list_studio_lifecycle_configs` |
| `aws_sagemaker_user_profile` | `list_user_profiles` |
| `aws_sagemaker_workforce` | `list_workforces` |
| `aws_sagemaker_workteam` | `list_workteams` |

## scheduler

**Boto3 Client:** `scheduler`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_scheduler_schedule` | `list_schedules` |
| `aws_scheduler_schedule_group` | `list_schedule_groups` |

## schemas

**Boto3 Client:** `schemas`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_schemas_discoverer` | `list_discoverers` |
| `aws_schemas_registry` | `list_registries` |
| `aws_schemas_registry_policy` | `get_registry_policy` |
| `aws_schemas_schema` | `list_schemas` |

## sdb

**Boto3 Client:** `sdb`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_simpledb_domain` | `list_domains` |

## secretsmanager

**Boto3 Client:** `secretsmanager`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_secretsmanager_secret` | `list_secrets` |
| `aws_secretsmanager_secret_policy` | `get_resource_policy` |
| `aws_secretsmanager_secret_rotation` | `describe_secret` |
| `aws_secretsmanager_secret_version` | `list_secret_version_ids` |

## securityhub

**Boto3 Client:** `securityhub`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_securityhub_account` | `describe_hub` |
| `aws_securityhub_action_target` | `describe_action_targets` |
| `aws_securityhub_finding_aggregator` | `describe_finding_aggregators` |
| `aws_securityhub_insight` | `describe_insights` |
| `aws_securityhub_invite_accepter` | `describe_invite_accepters` |
| `aws_securityhub_member` | `describe_members` |
| `aws_securityhub_organization_admin_account` | `describe_organization_admin_account` |
| `aws_securityhub_organization_configuration` | `describe_organization_configuration` |
| `aws_securityhub_product_subscription` | `describe_product_subscriptions` |
| `aws_securityhub_standards_control` | `describe_standards_controls` |
| `aws_securityhub_standards_subscription` | `describe_standards_subscriptions` |

## securitylake

**Boto3 Client:** `securitylake`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_securitylake_data_lake` | `describe_data_lakes` |

## serverlessrepo

**Boto3 Client:** `serverlessrepo`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_serverlessapplicationrepository_cloudformation_stack` | `list_application_versions` |

## service-quotas

**Boto3 Client:** `service-quotas`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_servicequotas_service_quota` | `list_service_quotas` |
| `aws_servicequotas_template` | `list_templates` |
| `aws_servicequotas_template_association` | `list_template_associations` |

## servicecatalog

**Boto3 Client:** `servicecatalog`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_servicecatalog_budget_resource_association` | `list_budget_resource_associations` |
| `aws_servicecatalog_constraint` | `list_constraints_for_portfolio` |
| `aws_servicecatalog_organizations_access` | `list_organization_access` |
| `aws_servicecatalog_portfolio` | `list_portfolios` |
| `aws_servicecatalog_portfolio_share` | `list_portfolio_shares` |
| `aws_servicecatalog_principal_portfolio_association` | `list_principal_portfolio_associations` |
| `aws_servicecatalog_product` | `search_products_as_admin` |
| `aws_servicecatalog_product_portfolio_association` | `list_product_portfolio_associations` |
| `aws_servicecatalog_provisioned_product` | `list_provisioned_products` |
| `aws_servicecatalog_provisioning_artifact` | `list_provisioning_artifacts` |
| `aws_servicecatalog_service_action` | `list_service_actions` |
| `aws_servicecatalog_tag_option` | `list_tag_options` |
| `aws_servicecatalog_tag_option_resource_association` | `list_tag_option_resource_associations` |

## servicediscovery

**Boto3 Client:** `servicediscovery`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_service_discovery_http_namespace` | `list_namespaces` |
| `aws_service_discovery_instance` | `list_instances` |
| `aws_service_discovery_private_dns_namespace` | `list_namespaces` |
| `aws_service_discovery_public_dns_namespace` | `list_namespaces` |
| `aws_service_discovery_service` | `list_services` |

## ses

**Boto3 Client:** `ses`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_ses_active_receipt_rule_set` | `describe_active_receipt_rule_set` |
| `aws_ses_configuration_set` | `describe_configuration_sets` |
| `aws_ses_domain_dkim` | `describe_domain_dkim` |
| `aws_ses_domain_identity` | `describe_domain_identity` |
| `aws_ses_domain_identity_verification` | `describe_domain_identity_verification` |
| `aws_ses_domain_mail_from` | `describe_domain_mail_from` |
| `aws_ses_email_identity` | `describe_email_identity` |
| `aws_ses_event_destination` | `describe_event_destination` |
| `aws_ses_identity_notification_topic` | `describe_identity_notification_topic` |
| `aws_ses_identity_policy` | `describe_identity_policy` |
| `aws_ses_receipt_filter` | `describe_receipt_filter` |
| `aws_ses_receipt_rule` | `describe_receipt_rule` |
| `aws_ses_receipt_rule_set` | `describe_receipt_rule_set` |
| `aws_ses_template` | `describe_template` |

## shield

**Boto3 Client:** `shield`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_shield_application_layer_automatic_response` | `list_application_layer_automatic_response_associations` |
| `aws_shield_drt_access_log_bucket_association` | `list_drt_access_log_bucket_associations` |
| `aws_shield_drt_access_role_arn_association` | `list_drt_access_role_arn_associations` |
| `aws_shield_protection` | `list_protections` |
| `aws_shield_protection_group` | `list_protection_groups` |
| `aws_shield_protection_health_check_association` | `list_protection_health_check_associations` |

## signer

**Boto3 Client:** `signer`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_signer_signing_job` | `list_signing_jobs` |
| `aws_signer_signing_profile` | `list_signing_profiles` |
| `aws_signer_signing_profile_permission` | `list_signing_profile_permissions` |

## sns

**Boto3 Client:** `sns`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_sns_platform_application` | `list_platform_applications` |
| `aws_sns_sms_preferences` | `get_sms_preferences` |
| `aws_sns_topic` | `list_topics` |
| `aws_sns_topic_data_protection_policy` | `get_data_protection_policy` |
| `aws_sns_topic_policy` | `get_topic_attributes` |
| `aws_sns_topic_subscription` | `list_subscriptions_by_topic` |

## sqs

**Boto3 Client:** `sqs`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_sqs_queue` | `list_queues` |
| `aws_sqs_queue_policy` | `get_queue_attributes` |
| `aws_sqs_queue_redrive_allow_policy` | `get_queue_attributes` |
| `aws_sqs_queue_redrive_policy` | `get_queue_attributes` |

## ssm

**Boto3 Client:** `ssm`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_ssm_activation` | `describe_activations` |
| `aws_ssm_association` | `list_associations` |
| `aws_ssm_default_patch_baseline` | `get_default_patch_baseline` |
| `aws_ssm_document` | `list_documents` |
| `aws_ssm_maintenance_window` | `describe_maintenance_windows` |
| `aws_ssm_maintenance_window_target` | `describe_maintenance_window_targets` |
| `aws_ssm_maintenance_window_task` | `describe_maintenance_window_tasks` |
| `aws_ssm_parameter` | `describe_parameters` |
| `aws_ssm_patch_baseline` | `describe_patch_baselines` |
| `aws_ssm_patch_group` | `list_patch_groups` |
| `aws_ssm_resource_data_sync` | `list_resource_data_sync` |
| `aws_ssm_service_setting` | `get_service_setting` |

## ssm-contacts

**Boto3 Client:** `ssm-contacts`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_ssmcontacts_contact` | `list_contacts` |
| `aws_ssmcontacts_contact_channel` | `list_contact_channels` |
| `aws_ssmcontacts_plan` | `get_contact` |

## ssm-incidents

**Boto3 Client:** `ssm-incidents`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_ssmincidents_replication_set` | `list_replication_sets` |
| `aws_ssmincidents_response_plan` | `list_response_plans` |

## sso-admin

**Boto3 Client:** `sso-admin`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_ssoadmin_account_assignment` | `list_account_assignments` |
| `aws_ssoadmin_application` | `list_applications` |
| `aws_ssoadmin_application_assignment` | `list_application_assignments` |
| `aws_ssoadmin_application_assignment_configuration` | `list_application_assignment_configurations` |
| `aws_ssoadmin_customer_managed_policy_attachment` | `list_customer_managed_policy_attachments` |
| `aws_ssoadmin_instance_access_control_attributes` | `list_instance_access_control_attribute_configuration` |
| `aws_ssoadmin_instances` | `list_instances` |
| `aws_ssoadmin_managed_policy_attachment` | `list_managed_policy_attachments` |
| `aws_ssoadmin_permission_set` | `list_permission_sets` |
| `aws_ssoadmin_permission_set_inline_policy` | `list_permission_set_inline_policies` |
| `aws_ssoadmin_permissions_boundary_attachment` | `list_permissions_boundary_attachments` |
| `aws_ssoadmin_trusted_token_issuer` | `list_trusted_token_issuers` |

## stepfunctions

**Boto3 Client:** `stepfunctions`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_sfn_activity` | `list_activities` |
| `aws_sfn_alias` | `list_state_machine_aliases` |
| `aws_sfn_state_machine` | `list_state_machines` |

## storagegateway

**Boto3 Client:** `storagegateway`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_storagegateway_cache` | `describe_cache` |
| `aws_storagegateway_cached_iscsi_volume` | `describe_cached_iscsi_volumes` |
| `aws_storagegateway_file_system_association` | `describe_file_system_associations` |
| `aws_storagegateway_gateway` | `describe_gateways` |
| `aws_storagegateway_nfs_file_share` | `describe_nfs_file_shares` |
| `aws_storagegateway_smb_file_share` | `describe_smb_file_shares` |
| `aws_storagegateway_stored_iscsi_volume` | `describe_stored_iscsi_volumes` |
| `aws_storagegateway_tape_pool` | `describe_tape_pools` |
| `aws_storagegateway_upload_buffer` | `describe_upload_buffer` |
| `aws_storagegateway_working_storage` | `describe_working_storage` |

## swf

**Boto3 Client:** `swf`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_swf_domain` | `list_domains` |

## synthetics

**Boto3 Client:** `synthetics`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_synthetics_canary` | `list_canaries` |
| `aws_synthetics_group` | `list_canary_groups` |
| `aws_synthetics_group_association` | `list_group_associations` |

## timestream-write

**Boto3 Client:** `timestream-write`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_timestreamwrite_database` | `list_databases` |
| `aws_timestreamwrite_table` | `list_tables` |

## transcribe

**Boto3 Client:** `transcribe`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_transcribe_language_model` | `list_language_models` |
| `aws_transcribe_medical_vocabulary` | `list_medical_vocabularies` |
| `aws_transcribe_vocabulary` | `list_vocabularies` |
| `aws_transcribe_vocabulary_filter` | `list_vocabulary_filters` |

## transfer

**Boto3 Client:** `transfer`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_transfer_access` | `list_accesses` |
| `aws_transfer_agreement` | `list_agreements` |
| `aws_transfer_certificate` | `list_certificates` |
| `aws_transfer_connector` | `list_connectors` |
| `aws_transfer_profile` | `list_profiles` |
| `aws_transfer_server` | `list_servers` |
| `aws_transfer_ssh_key` | `list_ssh_public_keys` |
| `aws_transfer_tag` | `list_tags` |
| `aws_transfer_user` | `list_users` |
| `aws_transfer_workflow` | `list_workflows` |

## vpc-lattice

**Boto3 Client:** `vpc-lattice`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_vpclattice_access_log_subscription` | `list_access_log_subscriptions` |
| `aws_vpclattice_auth_policy` | `get_auth_policy` |
| `aws_vpclattice_listener` | `list_listeners` |
| `aws_vpclattice_listener_rule` | `list_rules` |
| `aws_vpclattice_resource_configuration` | `list_resource_configurations` |
| `aws_vpclattice_resource_gateway` | `list_resource_gateways` |
| `aws_vpclattice_resource_policy` | `get_resource_policy` |
| `aws_vpclattice_service` | `list_services` |
| `aws_vpclattice_service_network` | `list_service_networks` |
| `aws_vpclattice_service_network_resource_association` | `list_service_network_resource_associations` |
| `aws_vpclattice_service_network_service_association` | `list_service_network_service_associations` |
| `aws_vpclattice_service_network_vpc_association` | `list_service_network_vpc_associations` |
| `aws_vpclattice_target_group` | `list_target_groups` |
| `aws_vpclattice_target_group_attachment` | `list_target_group_attachments` |

## waf

**Boto3 Client:** `waf`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_waf_byte_match_set` | `list_byte_match_sets` |
| `aws_waf_geo_match_set` | `list_geo_match_sets` |
| `aws_waf_ipset` | `list_ip_sets` |
| `aws_waf_rate_based_rule` | `list_rate_based_rules` |
| `aws_waf_regex_match_set` | `list_regex_match_sets` |
| `aws_waf_regex_pattern_set` | `list_regex_pattern_sets` |
| `aws_waf_rule` | `list_rules` |
| `aws_waf_rule_group` | `list_rule_groups` |
| `aws_waf_size_constraint_set` | `list_size_constraint_sets` |
| `aws_waf_sql_injection_match_set` | `list_sql_injection_match_sets` |
| `aws_waf_web_acl` | `list_web_acls` |
| `aws_waf_xss_match_set` | `list_xss_match_sets` |

## waf-regional

**Boto3 Client:** `waf-regional`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_wafregional_byte_match_set` | `list_byte_match_sets` |
| `aws_wafregional_geo_match_set` | `list_geo_match_sets` |
| `aws_wafregional_ipset` | `list_ip_sets` |
| `aws_wafregional_rate_based_rule` | `list_rate_based_rules` |
| `aws_wafregional_regex_match_set` | `list_regex_match_sets` |
| `aws_wafregional_regex_pattern_set` | `list_regex_pattern_sets` |
| `aws_wafregional_rule` | `list_rules` |
| `aws_wafregional_rule_group` | `list_rule_groups` |
| `aws_wafregional_size_constraint_set` | `list_size_constraint_sets` |
| `aws_wafregional_sql_injection_match_set` | `list_sql_injection_match_sets` |
| `aws_wafregional_web_acl` | `list_web_acls` |
| `aws_wafregional_web_acl_association` | `list_web_acl_associations` |
| `aws_wafregional_xss_match_set` | `list_xss_match_sets` |

## wafv2

**Boto3 Client:** `wafv2`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_proxy_protocol_policy` | `list_proxy_protocol_policies` |

## worklink

**Boto3 Client:** `worklink`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_worklink_fleet` | `list_fleets` |
| `aws_worklink_website_certificate_authority_association` | `list_website_certificate_authorities` |

## workspaces

**Boto3 Client:** `workspaces`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_workspaces_connection_alias` | `describe_connection_aliases` |
| `aws_workspaces_directory` | `describe_workspace_directories` |
| `aws_workspaces_ip_group` | `describe_ip_groups` |
| `aws_workspaces_workspace` | `describe_workspaces` |

## xray

**Boto3 Client:** `xray`

| Terraform Resource | Boto3 API Method |
|-------------------|------------------|
| `aws_xray_encryption_config` | `get_encryption_config` |
| `aws_xray_group` | `get_group` |
| `aws_xray_sampling_rule` | `get_sampling_rules` |
