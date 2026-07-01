#!/usr/bin/env python3
"""
AWS Dictionary Fix Script

This script automatically fixes known boto3 client and method name errors in aws_dict.py
based on the verification report findings.
"""

import re
import sys
import os

# Define fixes based on verification report
FIXES = {
    # API Gateway - singular vs plural
    'aws_api_gateway_integration_response': {
        'descfn': ('get_integration_responses', 'get_integration_response')
    },
    'aws_api_gateway_method_settings': {
        'descfn': ('get_method_settings', 'get_stage')  # method_settings is part of stage
    },
    
    # AppStream - methods don't exist, use describe instead
    'aws_appstream_directory_config': {
        'descfn': ('list_directory_configs', 'describe_directory_configs')
    },
    'aws_appstream_fleet_stack_association': {
        'descfn': ('list_fleet_stack_associations', 'describe_fleet_stack_associations')
    },
    'aws_appstream_user_stack_association': {
        'descfn': ('list_user_stack_associations', 'describe_user_stack_associations')
    },
    
    # AppSync - methods don't exist
    'aws_appsync_api_cache': {
        'descfn': ('list_api_caches', 'get_api_cache')
    },
    'aws_appsync_domain_name_api_association': {
        'descfn': ('list_domain_name_api_associations', 'get_domain_name')
    },
    
    # AuditManager - different method names
    'aws_auditmanager_account_registration': {
        'descfn': ('list_account_registrations', 'get_account_status')
    },
    'aws_auditmanager_assessment_delegation': {
        'descfn': ('list_assessment_delegations', 'get_delegations')
    },
    'aws_auditmanager_framework': {
        'descfn': ('list_frameworks', 'list_assessment_frameworks')
    },
    'aws_auditmanager_framework_share': {
        'descfn': ('list_framework_shares', 'list_assessment_framework_share_requests')
    },
    'aws_auditmanager_organization_admin_account_registration': {
        'descfn': ('list_organization_admin_accounts', 'get_organization_admin_account')
    },
    
    # AutoScaling - methods don't exist
    'aws_autoscaling_attachment': {
        'descfn': ('list_attachments', 'describe_auto_scaling_groups')  # attachments are part of ASG
    },
    'aws_autoscaling_notification': {
        'descfn': ('list_notifications', 'describe_notification_configurations')
    },
    'aws_autoscaling_traffic_source_attachment': {
        'descfn': ('list_traffic_source_attachments', 'describe_traffic_sources')
    },
    
    # Bedrock Agent Core - method doesn't exist
    'aws_bedrockagentcore_memory_strategy': {
        'descfn': ('list_memory_strategies', 'list_memories')
    },
    
    # Budgets - different method names
    'aws_budgets_budget': {
        'descfn': ('list_budgets', 'describe_budgets')
    },
    'aws_budgets_budget_action': {
        'descfn': ('list_budget_actions', 'describe_budget_actions_for_budget')
    },
    
    # Cost Explorer - different method names
    'aws_ce_anomaly_monitor': {
        'descfn': ('list_anomaly_monitors', 'get_anomaly_monitors')
    },
    'aws_ce_anomaly_subscription': {
        'descfn': ('list_anomaly_subscriptions', 'get_anomaly_subscriptions')
    },
    'aws_ce_cost_category': {
        'descfn': ('list_cost_categories', 'list_cost_category_definitions')
    },
    
    # Chime SDK Voice - methods don't exist
    'aws_chime_voice_connector_logging': {
        'descfn': ('list_voice_connector_logging_configurations', 'get_voice_connector_logging_configuration')
    },
    'aws_chime_voice_connector_origination': {
        'descfn': ('list_voice_connector_origination_configurations', 'get_voice_connector_origination')
    },
    'aws_chime_voice_connector_streaming': {
        'descfn': ('list_voice_connector_streaming_configurations', 'get_voice_connector_streaming_configuration')
    },
    'aws_chime_voice_connector_termination': {
        'descfn': ('list_voice_connector_termination_configurations', 'get_voice_connector_termination')
    },
    
    # Chime SDK Media Pipelines
    'aws_chimesdkmediapipelines_media_insights_pipeline_configuration': {
        'descfn': ('list_media_insights_pipelines', 'list_media_insights_pipeline_configurations')
    },
    
    # Chime SDK Voice Global Settings
    'aws_chimesdkvoice_global_settings': {
        'descfn': ('list_global_settings', 'get_global_settings')
    },
    
    # CloudFormation
    'aws_cloudformation_stack_set_instance': {
        'descfn': ('list_stack_set_instances', 'list_stack_instances')
    },
    
    # CloudFront
    'aws_cloudfront_monitoring_subscription': {
        'descfn': ('list_monitoring_subscriptions', 'get_monitoring_subscription')
    },
    
    # CloudSearch
    'aws_cloudsearch_domain': {
        'descfn': ('list_domains', 'describe_domains')
    },
    'aws_cloudsearch_domain_service_access_policy': {
        'descfn': ('list_domain_service_access_policies', 'describe_service_access_policies')
    },
    
    # CodeArtifact
    'aws_codeartifact_domain_permissions_policy': {
        'descfn': ('list_domain_permissions_policies', 'get_domain_permissions_policy')
    },
    'aws_codeartifact_repository_permissions_policy': {
        'descfn': ('list_repository_permissions_policies', 'get_repository_permissions_policy')
    },
    
    # CodeBuild
    'aws_codebuild_webhook': {
        'descfn': ('list_webhooks', 'batch_get_projects')  # webhooks are part of project
    },
    
    # CodeCommit
    'aws_codecommit_approval_rule_template_association': {
        'descfn': ('list_associated_approval_rule_templates', 'list_associated_approval_rule_templates_for_repository')
    },
    'aws_codecommit_trigger': {
        'descfn': ('list_repository_triggers', 'get_repository_triggers')
    },
    
    # Cognito Identity
    'aws_cognito_identity_pool_provider_principal_tag': {
        'descfn': ('list_identity_pool_roles', 'get_principal_tag_attribute_map')
    },
    'aws_cognito_identity_pool_roles_attachment': {
        'descfn': ('list_identity_pool_roles_attachments', 'get_identity_pool_roles')
    },
    
    # Cognito IDP
    'aws_cognito_risk_configuration': {
        'descfn': ('list_risk_configurations', 'describe_risk_configuration')
    },
    'aws_cognito_user_pool_domain': {
        'descfn': ('list_user_pool_domains', 'describe_user_pool_domain')
    },
    'aws_cognito_user_pool_ui_customization': {
        'descfn': ('list_user_pool_uis', 'get_ui_customization')
    },
    
    # Connect
    'aws_connect_user_hierarchy_structure': {
        'descfn': ('list_user_hierarchy_structures', 'describe_user_hierarchy_structure')
    },
    
    # Control Tower
    'aws_controltower_control': {
        'descfn': ('list_controls', 'list_enabled_controls')
    },
    
    # Cost Optimization Hub
    'aws_costoptimizationhub_enrollment_status': {
        'descfn': ('get_enrollment_status', 'get_preferences')
    },
    
    # CUR (Cost and Usage Report)
    'aws_cur_report_definition': {
        'descfn': ('list_report_definitions', 'describe_report_definitions')
    },
    
    # Customer Profiles
    'aws_customerprofiles_profile': {
        'descfn': ('list_profiles', 'search_profiles')
    },
    
    # Data Exchange
    'aws_dataexchange_revision': {
        'descfn': ('list_revisions', 'list_data_set_revisions')
    },
    
    # Data Pipeline
    'aws_datapipeline_pipeline_definition': {
        'descfn': ('list_pipeline_definition', 'get_pipeline_definition')
    },
    
    # DataSync - all location methods
    'aws_datasync_location_azure_blob': {
        'descfn': ('list_location_s3', 'list_locations')
    },
    'aws_datasync_location_efs': {
        'descfn': ('list_location_efs', 'list_locations')
    },
    'aws_datasync_location_fsx_lustre_file_system': {
        'descfn': ('list_location_fsx_lustre', 'list_locations')
    },
    'aws_datasync_location_fsx_ontap_file_system': {
        'descfn': ('list_location_fsx_ontap', 'list_locations')
    },
    'aws_datasync_location_fsx_openzfs_file_system': {
        'descfn': ('list_location_fsx_openzfs', 'list_locations')
    },
    'aws_datasync_location_fsx_windows_file_system': {
        'descfn': ('list_location_fsx_windows', 'list_locations')
    },
    'aws_datasync_location_hdfs': {
        'descfn': ('list_location_hdfs', 'list_locations')
    },
    'aws_datasync_location_nfs': {
        'descfn': ('list_location_nfs', 'list_locations')
    },
    'aws_datasync_location_object_storage': {
        'descfn': ('list_location_object_storage', 'list_locations')
    },
    'aws_datasync_location_s3': {
        'descfn': ('list_location_s3', 'list_locations')
    },
    'aws_datasync_location_smb': {
        'descfn': ('list_location_smb', 'list_locations')
    },
    
    # DAX
    'aws_dax_cluster': {
        'descfn': ('list_clusters', 'describe_clusters')
    },
    'aws_dax_parameter_group': {
        'descfn': ('list_parameter_groups', 'describe_parameter_groups')
    },
    'aws_dax_subnet_group': {
        'descfn': ('list_subnet_groups', 'describe_subnet_groups')
    },
    
    # RDS
    'aws_db_instance_role_association': {
        'descfn': ('describe_db_instance_role_associations', 'describe_db_instances')
    },
    'aws_db_proxy_default_target_group': {
        'descfn': ('describe_db_proxy_default_target_groups', 'describe_db_proxy_target_groups')
    },
    
    # EC2
    'aws_default_vpc_dhcp_options': {
        'descfn': ('describe_vpc_dhcp_options', 'describe_dhcp_options')
    },
    
    # Detective
    'aws_detective_invitation_accepter': {
        'descfn': ('list_invitation_accepters', 'list_invitations')
    },
    'aws_detective_organization_configuration': {
        'descfn': ('list_organization_configurations', 'describe_organization_configuration')
    },
    
    # Directory Service
    'aws_directory_service_conditional_forwarder': {
        'descfn': ('list_conditional_forwarders', 'describe_conditional_forwarders')
    },
    'aws_directory_service_radius_settings': {
        'descfn': ('list_radius_settings', 'describe_directories')
    },
    'aws_directory_service_region': {
        'descfn': ('list_regions', 'describe_regions')
    },
    'aws_directory_service_shared_directory': {
        'descfn': ('list_shared_directories', 'describe_shared_directories')
    },
    'aws_directory_service_trust': {
        'descfn': ('list_trusts', 'describe_trusts')
    },
    
    # DLM
    'aws_dlm_lifecycle_policy': {
        'descfn': ('list_policies', 'get_lifecycle_policies')
    },
    
    # DMS
    'aws_dms_s3_endpoint': {
        'descfn': ('describe_s3_endpoints', 'describe_endpoints')
    },
    
    # DocDB Elastic
    'aws_docdbelastic_cluster': {
        'descfn': ('describe_clusters', 'list_clusters')
    },
    
    # DSQL
    'aws_dsql_cluster_peering': {
        'descfn': ('list_cluster_peerings', 'list_clusters')
    },
    
    # Direct Connect - multiple resources
    'aws_dx_bgp_peer': {
        'descfn': ('describe_bgp_peers', 'describe_virtual_interfaces')
    },
    'aws_dx_connection_association': {
        'descfn': ('describe_connection_associations', 'describe_connections')
    },
    'aws_dx_connection_confirmation': {
        'descfn': ('describe_confirmations', 'describe_connections')
    },
    'aws_dx_hosted_connection': {
        'descfn': ('describe_gateway_association_proposals', 'describe_connections')
    },
    'aws_dx_hosted_private_virtual_interface': {
        'descfn': ('describe_hosted_private_virtual_interfaces', 'describe_virtual_interfaces')
    },
    'aws_dx_hosted_private_virtual_interface_accepter': {
        'descfn': ('describe_hosted_private_virtual_interfaces', 'describe_virtual_interfaces')
    },
    'aws_dx_hosted_public_virtual_interface': {
        'descfn': ('describe_hosted_public_virtual_interfaces', 'describe_virtual_interfaces')
    },
    'aws_dx_hosted_public_virtual_interface_accepter': {
        'descfn': ('describe_hosted_public_virtual_interfaces', 'describe_virtual_interfaces')
    },
    'aws_dx_hosted_transit_virtual_interface': {
        'descfn': ('describe_hosted_transit_virtual_interfaces', 'describe_virtual_interfaces')
    },
    'aws_dx_hosted_transit_virtual_interface_accepter': {
        'descfn': ('describe_hosted_transit_virtual_interfaces', 'describe_virtual_interfaces')
    },
    'aws_dx_macsec_key_association': {
        'descfn': ('describe_macsec_key_associations', 'describe_connections')
    },
    'aws_dx_private_virtual_interface': {
        'descfn': ('describe_private_virtual_interfaces', 'describe_virtual_interfaces')
    },
    'aws_dx_public_virtual_interface': {
        'descfn': ('describe_public_virtual_interfaces', 'describe_virtual_interfaces')
    },
    'aws_dx_transit_virtual_interface': {
        'descfn': ('describe_transit_virtual_interfaces', 'describe_virtual_interfaces')
    },
    
    # DynamoDB
    'aws_dynamodb_global_table': {
        'descfn': ('describe_global_tables', 'list_global_tables')
    },
    
    # EBS
    'aws_ebs_snapshot_copy': {
        'descfn': ('describe_snapshot_copy_grants', 'describe_snapshots')
    },
    'aws_ebs_snapshot_import': {
        'descfn': ('describe_snapshot_import_tasks', 'describe_import_snapshot_tasks')
    },
    
    # ElastiCache
    'aws_elasticache_user_group_association': {
        'descfn': ('describe_user_group_memberships', 'describe_user_groups')
    },
    
    # Elasticsearch
    'aws_elasticsearch_domain_policy': {
        'descfn': ('describe_elasticsearch_domain_policy', 'describe_elasticsearch_domain_config')
    },
    
    # EMR
    'aws_emr_block_public_access_configuration': {
        'descfn': ('describe_block_public_access_configurations', 'get_block_public_access_configuration')
    },
    'aws_emr_instance_fleet': {
        'descfn': ('describe_instance_fleets', 'list_instance_fleets')
    },
    'aws_emr_studio': {
        'descfn': ('describe_studios', 'list_studios')
    },
    'aws_emr_studio_session_mapping': {
        'descfn': ('describe_studio_session_mappings', 'list_studio_session_mappings')
    },
}

def fix_aws_dict(input_file, output_file=None):
    """Fix aws_dict.py based on known issues"""
    
    if output_file is None:
        output_file = input_file
    
    with open(input_file, 'r') as f:
        content = f.read()
    
    fixes_applied = 0
    
    # Apply each fix
    for resource_name, fixes in FIXES.items():
        if 'descfn' in fixes:
            old_method, new_method = fixes['descfn']
            
            # Find the resource definition
            pattern = rf'({resource_name}\s*=\s*{{[^}}]*"descfn":\s*")({old_method})(")'
            
            if re.search(pattern, content):
                content = re.sub(pattern, rf'\1{new_method}\3', content)
                fixes_applied += 1
                print(f"✓ Fixed {resource_name}: {old_method} → {new_method}")
    
    # Write the fixed content
    with open(output_file, 'w') as f:
        f.write(content)
    
    return fixes_applied

if __name__ == '__main__':
    input_file = os.path.join(os.path.dirname(__file__), '..', 'fixtf_aws_resources', 'aws_dict.py')
    
    print("Fixing aws_dict.py...")
    print(f"Input file: {input_file}")
    
    fixes_applied = fix_aws_dict(input_file)
    
    print(f"\n✅ Applied {fixes_applied} fixes to aws_dict.py")
    print("\nRun verify_aws_dict.py again to check remaining issues.")
