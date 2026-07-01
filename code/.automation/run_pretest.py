#!/usr/bin/env python3
"""
PRE-TEST Stage: Assess CloudFormation resources for Terraform and aws2tf support
"""

import re
import sys

# Read the files
with open('code/.automation/to-test-stack.md', 'r') as f:
    content = f.read()

with open('code/fixtf_aws_resources/aws_not_implemented.py', 'r') as f:
    not_implemented = f.read()

with open('code/fixtf_aws_resources/aws_no_import.py', 'r') as f:
    no_import = f.read()

# Statistics
stats = {
    'total': 0,
    'no_terraform': 0,
    'not_supported': 0,
    'no_import': 0,
    'ready': 0,
    'already_checked': 0
}

# Known mappings of CloudFormation to Terraform resources that don't exist
# Based on AWS services that are not in Terraform AWS provider
NO_TERRAFORM_RESOURCES = {
    # Services not in Terraform
    'AWS::AIOps::': 'aws_aiops_',  # CloudWatch Investigations - new service
    'AWS::ApplicationSignals::': 'aws_applicationsignals_',  # New service
    'AWS::AppTest::': 'aws_apptest_',  # Mainframe Modernization Testing
    'AWS::ARCRegionSwitch::': 'aws_arcregionswitch_',  # New service
    'AWS::ASK::': 'aws_ask_',  # Alexa Skills Kit
    'AWS::BCMDataExports::': 'aws_bcmdataexports_',  # New service
    'AWS::BedrockAgentCore::': 'aws_bedrock_agent_core_',  # New service
    'AWS::Billing::': 'aws_billing_',  # New service
    'AWS::Cases::': 'aws_cases_',  # Connect Cases
    'AWS::CleanRoomsML::': 'aws_cleanroomsml_',  # New service
    'AWS::CodeConnections::': 'aws_codeconnections_',  # Replaces CodeStarConnections
    'AWS::ConnectCampaignsV2::': 'aws_connectcampaignsv2_',  # New version
    'AWS::CUR::': 'aws_cur_',  # Cost and Usage Report
    'AWS::Deadline::': 'aws_deadline_',  # New service
    'AWS::DevOpsAgent::': 'aws_devopsagent_',  # New service
    'AWS::DSQL::': 'aws_dsql_',  # Aurora DSQL
    'AWS::EVS::': 'aws_evs_',  # Elastic VMware Service
    'AWS::GameLiftStreams::': 'aws_gameliftstreams_',  # New service
    'AWS::IoTFleetWise::': 'aws_iotfleetwise_',  # IoT FleetWise
    'AWS::IoTManagedIntegrations::': 'aws_iotmanagedintegrations_',  # New service
    'AWS::Invoicing::': 'aws_invoicing_',  # New service
    'AWS::LaunchWizard::': 'aws_launchwizard_',  # Launch Wizard
    'AWS::LookoutEquipment::': 'aws_lookoutequipment_',  # Lookout for Equipment
    'AWS::MPA::': 'aws_mpa_',  # Multi-party approval
    'AWS::Notifications::': 'aws_notifications_',  # New service
    'AWS::NotificationsContacts::': 'aws_notificationscontacts_',  # New service
    'AWS::ObservabilityAdmin::': 'aws_observabilityadmin_',  # New service
    'AWS::ODB::': 'aws_odb_',  # Oracle Database@AWS
    'AWS::PCAConnectorSCEP::': 'aws_pcaconnectorscep_',  # New service
    'AWS::PCS::': 'aws_pcs_',  # Parallel Computing Service
    'AWS::QBusiness::': 'aws_qbusiness_',  # Amazon Q Business
    'AWS::Rbin::': 'aws_rbin_',  # Recycle Bin
    'AWS::Route53Profiles::': 'aws_route53profiles_',  # New service
    'AWS::RTBFabric::': 'aws_rtbfabric_',  # New service
    'AWS::SMSVOICE::': 'aws_smsvoice_',  # End User Messaging SMS
    'AWS::SSMGuiConnect::': 'aws_ssmguiconnect_',  # New service
    'AWS::SSMQuickSetup::': 'aws_ssmquicksetup_',  # New service
}

def cfn_to_terraform_name(cfn_type):
    """Convert CloudFormation type to expected Terraform resource name"""
    # AWS::Service::ResourceType -> aws_service_resource_type
    parts = cfn_type.split('::')
    if len(parts) != 3:
        return None
    
    service = parts[1].lower()
    resource = parts[2]
    
    # Convert CamelCase to snake_case
    resource_snake = re.sub('([a-z0-9])([A-Z])', r'\1_\2', resource).lower()
    
    return f"aws_{service}_{resource_snake}"

def check_terraform_exists(cfn_type):
    """Check if this CloudFormation type likely has Terraform support"""
    # Check against known non-existent services
    for prefix, _ in NO_TERRAFORM_RESOURCES.items():
        if cfn_type.startswith(prefix):
            return False
    return True

def check_not_implemented(tf_name):
    """Check if resource is in aws_not_implemented.py"""
    # Look for uncommented entry
    pattern = rf'^\s*"{tf_name}":\s*True'
    return bool(re.search(pattern, not_implemented, re.MULTILINE))

def check_no_import(tf_name):
    """Check if resource is in aws_no_import.py"""
    # Look for uncommented entry
    pattern = rf'^\s*"{tf_name}":\s*True'
    return bool(re.search(pattern, no_import, re.MULTILINE))

# Process the markdown file
lines = content.split('\n')
output_lines = []
in_resources_section = False

for line in lines:
    # Check if we're in the resources section
    if line.startswith('### ') and '(' in line and 'resources)' in line:
        in_resources_section = True
        output_lines.append(line)
        continue
    
    # Check if we've left resources section
    if line.startswith('## ') and in_resources_section:
        in_resources_section = False
    
    # Process resource lines
    if in_resources_section and line.startswith('- [ ] `AWS::'):
        stats['total'] += 1
        
        # Extract CloudFormation type
        match = re.search(r'`(AWS::[^`]+)`', line)
        if not match:
            output_lines.append(line)
            continue
        
        cfn_type = match.group(1)
        tf_name = cfn_to_terraform_name(cfn_type)
        
        if not tf_name:
            output_lines.append(line)
            continue
        
        # Step 2: Check Terraform support
        if not check_terraform_exists(cfn_type):
            stats['no_terraform'] += 1
            new_line = f"- [x] `{cfn_type}` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->"
            output_lines.append(new_line)
            continue
        
        # Step 3: Check aws2tf support
        if check_not_implemented(tf_name):
            stats['not_supported'] += 1
            new_line = f"- [x] `{cfn_type}` <!-- NOT SUPPORTED: {tf_name} is in aws_not_implemented.py -->"
            output_lines.append(new_line)
            continue
        
        if check_no_import(tf_name):
            stats['no_import'] += 1
            new_line = f"- [x] `{cfn_type}` <!-- NO IMPORT SUPPORT: {tf_name} - Terraform does not support importing this resource type -->"
            output_lines.append(new_line)
            continue
        
        # Step 4: Mark as ready
        stats['ready'] += 1
        new_line = f"- [x] `{cfn_type}` <!-- READY: {tf_name} can be implemented in aws2tf -->"
        output_lines.append(new_line)
    
    elif in_resources_section and line.startswith('- [x] `AWS::'):
        # Already checked
        stats['already_checked'] += 1
        output_lines.append(line)
    else:
        output_lines.append(line)

# Write updated file
with open('code/.automation/to-test-stack.md', 'w') as f:
    f.write('\n'.join(output_lines))

# Print statistics
print("=" * 60)
print("PRE-TEST STAGE COMPLETE")
print("=" * 60)
print(f"\nTotal resources assessed: {stats['total']}")
print(f"Already checked (skipped): {stats['already_checked']}")
print(f"\nResults:")
print(f"  NO TERRAFORM SUPPORT:     {stats['no_terraform']:4d}")
print(f"  NOT SUPPORTED (aws2tf):   {stats['not_supported']:4d}")
print(f"  NO IMPORT SUPPORT:        {stats['no_import']:4d}")
print(f"  READY for implementation: {stats['ready']:4d}")
print(f"\nTotal processed: {stats['no_terraform'] + stats['not_supported'] + stats['no_import'] + stats['ready']}")
print(f"\nResults saved to: code/.automation/to-test-stack.md")
print("\n" + "=" * 60)
print("STOPPING - PRE-TEST stage complete as instructed")
print("=" * 60)
