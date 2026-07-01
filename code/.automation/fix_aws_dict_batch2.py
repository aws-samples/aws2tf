#!/usr/bin/env python3
"""
AWS Dictionary Fix Script - Batch 2

This script fixes the remaining boto3 client and method name errors.
"""

import re
import sys
import os

# Define additional fixes based on second verification
FIXES_BATCH2 = {
    # AppStream - method still doesn't exist
    'aws_appstream_fleet_stack_association': {
        'descfn': ('describe_fleet_stack_associations', 'describe_fleets')  # associations are part of fleet
    },
    
    # EBS - wrong client, should be ec2
    'aws_ebs_snapshot_copy': {
        'clfn': ('ebs', 'ec2')
    },
    'aws_ebs_snapshot_import': {
        'clfn': ('ebs', 'ec2')
    },
    
    # FinSpace - wrong client, should be finspace-data
    'aws_finspace_kx_cluster': {
        'clfn': ('finspace', 'finspace-data')
    },
    'aws_finspace_kx_database': {
        'clfn': ('finspace', 'finspace-data')
    },
    'aws_finspace_kx_dataview': {
        'clfn': ('finspace', 'finspace-data')
    },
    'aws_finspace_kx_scaling_group': {
        'clfn': ('finspace', 'finspace-data')
    },
    'aws_finspace_kx_user': {
        'clfn': ('finspace', 'finspace-data')
    },
    'aws_finspace_kx_volume': {
        'clfn': ('finspace', 'finspace-data')
    },
    
    # FMS
    'aws_fms_admin_account': {
        'descfn': ('list_admin_accounts', 'list_admin_accounts_for_organization')
    },
    
    # GameLift
    'aws_gamelift_game_session_queue': {
        'descfn': ('list_game_session_queues', 'describe_game_session_queues')
    },
    
    # Glacier
    'aws_glacier_vault_lock': {
        'descfn': ('list_vault_locks', 'get_vault_lock')
    },
    
    # Glue
    'aws_glue_partition': {
        'descfn': ('list_partitions', 'get_partitions')
    },
    'aws_glue_resource_policy': {
        'descfn': ('list_resource_policies', 'get_resource_policy')
    },
    
    # Grafana
    'aws_grafana_license_association': {
        'descfn': ('list_license_associations', 'describe_workspace')  # license is part of workspace
    },
    'aws_grafana_role_association': {
        'descfn': ('list_role_associations', 'list_permissions')
    },
    'aws_grafana_workspace_api_key': {
        'descfn': ('list_workspace_api_keys', 'list_workspaces')  # API keys managed separately
    },
    
    # GuardDuty
    'aws_guardduty_detector_feature': {
        'descfn': ('list_detector_features', 'get_detector')
    },
    'aws_guardduty_invite_accepter': {
        'descfn': ('list_invitation_accepters', 'list_invitations')
    },
    'aws_guardduty_organization_configuration': {
        'descfn': ('list_organization_configurations', 'describe_organization_configuration')
    },
    'aws_guardduty_organization_configuration_feature': {
        'descfn': ('list_organization_configuration_features', 'describe_organization_configuration')
    },
    
    # IAM
    'aws_iam_security_token_service_preferences': {
        'descfn': ('get_account_token_version', 'get_account_summary')
    },
    
    # Inspector2
    'aws_inspector2_enabler': {
        'descfn': ('list_enablers', 'batch_get_account_status')
    },
    'aws_inspector2_member_association': {
        'descfn': ('list_member_associations', 'list_members')
    },
    'aws_inspector2_organization_configuration': {
        'descfn': ('list_organization_configurations', 'describe_organization_configuration')
    },
    
    # Inspector (v1)
    'aws_inspector_resource_group': {
        'descfn': ('list_resource_groups', 'list_assessment_targets')
    },
    
    # EC2 - Internet Gateway
    'aws_internet_gateway_attachment': {
        'descfn': ('describe_internet_gateway_attachments', 'describe_internet_gateways')
    },
    
    # IoT
    'aws_iot_event_configurations': {
        'descfn': ('list_event_configurations', 'describe_event_configurations')
    },
    'aws_iot_indexing_configuration': {
        'descfn': ('list_indexing_configurations', 'get_indexing_configuration')
    },
    'aws_iot_logging_options': {
        'descfn': ('describe_logging_options', 'get_v2_logging_options')
    },
    'aws_iot_thing_group_membership': {
        'descfn': ('list_thing_group_memberships', 'list_things_in_thing_group')
    },
    'aws_iot_thing_principal_attachment': {
        'descfn': ('list_thing_principal_attachments', 'list_thing_principals')
    },
    
    # Lake Formation
    'aws_lakeformation_resource_lf_tags': {
        'descfn': ('list_resource_lf_tags', 'get_resource_lf_tags')
    },
    
    # License Manager
    'aws_licensemanager_association': {
        'descfn': ('list_associations', 'list_associations_for_license_configuration')
    },
    'aws_licensemanager_grant': {
        'descfn': ('list_grants', 'list_received_grants')
    },
    'aws_licensemanager_grant_accepter': {
        'descfn': ('list_grant_accepters', 'list_received_grants')
    },
    
    # Lightsail
    'aws_lightsail_bucket_resource_access': {
        'descfn': ('get_bucket_resources', 'get_buckets')
    },
    'aws_lightsail_disk_attachment': {
        'descfn': ('get_disk_attachments', 'get_disks')
    },
    'aws_lightsail_domain_entry': {
        'descfn': ('get_domain_entries', 'get_domains')
    },
    'aws_lightsail_instance_public_ports': {
        'descfn': ('get_instance_public_ports', 'get_instance_port_states')
    },
    'aws_lightsail_key_pair': {
        'descfn': ('get_instance_public_ports', 'get_key_pairs')
    },
    'aws_lightsail_lb_certificate_attachment': {
        'descfn': ('get_load_balancer_certificates', 'get_load_balancer_tls_certificates')
    },
    'aws_lightsail_lb_stickiness_policy': {
        'descfn': ('get_load_balancer_https_redirection_policies', 'get_load_balancers')
    },
    
    # ELB (classic)
    'aws_load_balancer_backend_server_policy': {
        'descfn': ('describe_backend_server_policies', 'describe_load_balancers')
    },
    'aws_load_balancer_policy': {
        'descfn': ('describe_load_balancer_policies', 'describe_load_balancer_policy_types')
    },
    
    # Location Service
    'aws_location_tracker_association': {
        'descfn': ('list_tracker_associations', 'list_tracker_consumers')
    },
    
    # Macie2
    'aws_macie2_account': {
        'descfn': ('list_account_settings', 'get_macie_session')
    },
    'aws_macie2_classification_job': {
        'descfn': ('list_classification_jobs', 'list_jobs')
    },
    'aws_macie2_custom_data_identifier': {
        'descfn': ('list_custom_data_identifiers', 'list_custom_data_identifiers')  # correct
    },
    'aws_macie2_findings_filter': {
        'descfn': ('list_findings_filters', 'list_findings_filters')  # correct
    },
    'aws_macie2_invitation_accepter': {
        'descfn': ('list_invitation_accepters', 'list_invitations')
    },
    'aws_macie2_member': {
        'descfn': ('list_members', 'list_members')  # correct
    },
    'aws_macie2_organization_admin_account': {
        'descfn': ('list_organization_admin_accounts', 'list_organization_admin_accounts')  # correct
    },
    
    # MediaConnect
    'aws_media_connect_flow_entitlement': {
        'descfn': ('list_flow_entitlements', 'list_entitlements')
    },
    'aws_media_connect_flow_output': {
        'descfn': ('list_flow_outputs', 'describe_flow')
    },
    'aws_media_connect_flow_source': {
        'descfn': ('list_flow_sources', 'describe_flow')
    },
    'aws_media_connect_flow_vpc_interface': {
        'descfn': ('list_flow_vpc_interfaces', 'describe_flow')
    },
    
    # MediaConvert
    'aws_media_convert_queue': {
        'descfn': ('list_queues', 'list_queues')  # correct
    },
    
    # MediaLive
    'aws_media_live_channel': {
        'descfn': ('list_channels', 'list_channels')  # correct
    },
    'aws_media_live_input': {
        'descfn': ('list_inputs', 'list_inputs')  # correct
    },
    'aws_media_live_input_security_group': {
        'descfn': ('list_input_security_groups', 'list_input_security_groups')  # correct
    },
    'aws_media_live_multiplex': {
        'descfn': ('list_multiplexes', 'list_multiplexes')  # correct
    },
    
    # MediaPackage
    'aws_media_package_channel': {
        'descfn': ('list_channels', 'list_channels')  # correct
    },
    
    # MediaStore
    'aws_media_store_container': {
        'descfn': ('list_containers', 'list_containers')  # correct
    },
    'aws_media_store_container_policy': {
        'descfn': ('list_container_policies', 'get_container_policy')
    },
    
    # MQ
    'aws_mq_broker': {
        'descfn': ('list_brokers', 'list_brokers')  # correct
    },
    'aws_mq_configuration': {
        'descfn': ('list_configurations', 'list_configurations')  # correct
    },
    
    # MSK
    'aws_msk_cluster': {
        'descfn': ('list_clusters', 'list_clusters_v2')
    },
    'aws_msk_configuration': {
        'descfn': ('list_configurations', 'list_configurations')  # correct
    },
    'aws_msk_scram_secret_association': {
        'descfn': ('list_scram_secret_associations', 'list_scram_secrets')
    },
    'aws_msk_serverless_cluster': {
        'descfn': ('list_serverless_clusters', 'list_clusters_v2')
    },
    
    # Neptune
    'aws_neptune_cluster': {
        'descfn': ('describe_db_clusters', 'describe_db_clusters')  # correct
    },
    'aws_neptune_cluster_endpoint': {
        'descfn': ('describe_db_cluster_endpoints', 'describe_db_cluster_endpoints')  # correct
    },
    'aws_neptune_cluster_instance': {
        'descfn': ('describe_db_instances', 'describe_db_instances')  # correct
    },
    'aws_neptune_cluster_parameter_group': {
        'descfn': ('describe_db_cluster_parameter_groups', 'describe_db_cluster_parameter_groups')  # correct
    },
    'aws_neptune_cluster_snapshot': {
        'descfn': ('describe_db_cluster_snapshots', 'describe_db_cluster_snapshots')  # correct
    },
    'aws_neptune_event_subscription': {
        'descfn': ('describe_event_subscriptions', 'describe_event_subscriptions')  # correct
    },
    'aws_neptune_global_cluster': {
        'descfn': ('describe_global_clusters', 'describe_global_clusters')  # correct
    },
    'aws_neptune_parameter_group': {
        'descfn': ('describe_db_parameter_groups', 'describe_db_parameter_groups')  # correct
    },
    'aws_neptune_subnet_group': {
        'descfn': ('describe_db_subnet_groups', 'describe_db_subnet_groups')  # correct
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
    for resource_name, fixes in FIXES_BATCH2.items():
        if 'descfn' in fixes:
            old_method, new_method = fixes['descfn']
            
            # Find the resource definition
            pattern = rf'({resource_name}\s*=\s*{{[^}}]*"descfn":\s*")({old_method})(")'
            
            if re.search(pattern, content):
                content = re.sub(pattern, rf'\1{new_method}\3', content)
                fixes_applied += 1
                print(f"✓ Fixed {resource_name}: {old_method} → {new_method}")
        
        if 'clfn' in fixes:
            old_client, new_client = fixes['clfn']
            
            # Find the resource definition
            pattern = rf'({resource_name}\s*=\s*{{[^}}]*"clfn":\s*")({old_client})(")'
            
            if re.search(pattern, content):
                content = re.sub(pattern, rf'\1{new_client}\3', content)
                fixes_applied += 1
                print(f"✓ Fixed {resource_name}: client {old_client} → {new_client}")
    
    # Write the fixed content
    with open(output_file, 'w') as f:
        f.write(content)
    
    return fixes_applied

if __name__ == '__main__':
    input_file = os.path.join(os.path.dirname(__file__), '..', 'fixtf_aws_resources', 'aws_dict.py')
    
    print("Fixing aws_dict.py (Batch 2)...")
    print(f"Input file: {input_file}")
    
    fixes_applied = fix_aws_dict(input_file)
    
    print(f"\n✅ Applied {fixes_applied} fixes to aws_dict.py")
    print("\nRun verify_aws_dict.py again to check remaining issues.")
