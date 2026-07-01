#!/usr/bin/env python3
import boto3

client = boto3.client('sesv2', region_name='us-east-1')
all_methods = [m for m in dir(client) if not m.startswith('_')]

# Updated methods from aws_dict.py (after fixes)
dict_methods = [
    "get_account",  # was describe_account_vdm_attributes
    "list_configuration_sets",
    "get_configuration_set_event_destinations",
    "list_contact_lists",
    "get_dedicated_ips",  # was describe_dedicated_ip_assignment
    "list_dedicated_ip_pools",
    "list_email_identities",
    "get_email_identity",  # used by multiple resources
    "get_account",  # used by account_suppression_attributes
    "get_email_identity_policies",
    "list_tenants"
]

print("Checking UPDATED sesv2 methods in aws_dict.py:\n")
missing = []
for method in dict_methods:
    exists = method in all_methods
    status = "✓" if exists else "✗ MISSING"
    print(f"{status} {method}")
    if not exists:
        missing.append(method)

if missing:
    print("\n\n❌ STILL HAVE MISSING METHODS!")
else:
    print("\n\n✅ ALL METHODS EXIST IN BOTO3!")

print("\n\nSummary of fixes applied:")
print("  1. aws_sesv2_account_vdm_attributes: describe_account_vdm_attributes → get_account")
print("  2. aws_sesv2_configuration_set_event_destination: describe_configuration_set_event_destination → get_configuration_set_event_destinations")
print("  3. aws_sesv2_dedicated_ip_assignment: describe_dedicated_ip_assignment → get_dedicated_ips")
print("  4. aws_sesv2_email_identity: list_email_identities (changed from paginator to direct call)")
print("  5. aws_sesv2_email_identity_feedback_attributes: describe_email_identity_feedback_attributes → get_email_identity")
print("  6. aws_sesv2_email_identity_mail_from_attributes: describe_email_identity_mail_from_attributes → get_email_identity")

