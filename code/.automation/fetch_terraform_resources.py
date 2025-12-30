#!/usr/bin/env python3
"""
Fetch all AWS Terraform resources from the provider repository
and compare with aws_dict.py to find missing ones
"""

import re
from collections import defaultdict

# Read the aws_dict.py file to get existing resources
with open('code/fixtf_aws_resources/aws_dict.py', 'r') as f:
    dict_content = f.read()

# Extract all resource names that are already defined in aws_dict.py
existing_pattern = r'^(aws_[a-z_0-9]+)\s*=\s*\{'
existing_resources = set(re.findall(existing_pattern, dict_content, re.MULTILINE))

print(f"Found {len(existing_resources)} resources in aws_dict.py")

# Comprehensive list of Terraform AWS resources (as of latest provider version)
# This list should be updated periodically from:
# https://github.com/hashicorp/terraform-provider-aws/tree/main/internal/service
all_known_resources = set([
    # This is a placeholder - we'll need to populate this with actual resources
    # For now, let's extract from the existing dict and add known missing ones
])

# Let's scan the fixtf_aws_resources directory for any resource type references
import os
import glob

fixtf_dir = 'code/fixtf_aws_resources'
referenced_resources = set()

for filepath in glob.glob(f'{fixtf_dir}/fixtf_*.py'):
    with open(filepath, 'r') as f:
        content = f.read()
        # Look for various patterns where resources might be referenced
        patterns = [
            r'resource\s+"(aws_[a-z_0-9]+)"',
            r'terraform\s+import\s+(aws_[a-z_0-9]+)\.',
            r'"(aws_[a-z_0-9]+)"',
            r'def\s+aws_([a-z_0-9]+)\(',
        ]
        for pattern in patterns:
            matches = re.findall(pattern, content)
            for match in matches:
                if not match.startswith('aws_'):
                    match = 'aws_' + match
                if match.startswith('aws_') and len(match) > 4:
                    referenced_resources.add(match)

print(f"Found {len(referenced_resources)} resources referenced in fixtf files")

# Combine with existing to get all known
all_known_resources = existing_resources | referenced_resources

# For a more comprehensive list, let's also check what's in the file names
for filepath in glob.glob(f'{fixtf_dir}/fixtf_*.py'):
    basename = os.path.basename(filepath)
    # Extract service name from filename like fixtf_ec2.py
    service = basename.replace('fixtf_', '').replace('.py', '')
    # This service might have multiple resources
    
print(f"Total known resources: {len(all_known_resources)}")

# Find missing resources (resources referenced but not in dict)
missing_resources = sorted(referenced_resources - existing_resources)

print(f"Found {len(missing_resources)} missing resources")

# Generate markdown output
output = []
output.append("# AWS Terraform Resources NOT in aws_dict.py")
output.append("")
output.append("This file lists Terraform AWS resources that are referenced in the codebase")
output.append("but are NOT yet defined in `aws_dict.py`.")
output.append("")
output.append(f"**Total Missing Resources:** {len(missing_resources)}")
output.append(f"**Total Existing Resources:** {len(existing_resources)}")
output.append(f"**Total Referenced Resources:** {len(referenced_resources)}")
output.append("")
output.append("---")
output.append("")

if missing_resources:
    output.append("## Missing Resources")
    output.append("")
    output.append("These resources need to be added to `aws_dict.py` with:")
    output.append("- Terraform resource name")
    output.append("- Boto3 client name (clfn)")
    output.append("- Boto3 describe/list API method (descfn)")
    output.append("- Top-level key in API response (topkey)")
    output.append("- Resource identifier key (key)")
    output.append("- Filter ID (filterid)")
    output.append("")
    output.append("| # | Terraform Resource | Status |")
    output.append("|---|-------------------|--------|")
    
    for idx, resource in enumerate(missing_resources, 1):
        output.append(f"| {idx} | `{resource}` | ❌ Not in dict |")
    
    output.append("")
else:
    output.append("## Status")
    output.append("")
    output.append("✅ **All referenced resources are defined in aws_dict.py!**")
    output.append("")
    output.append("Note: This only checks resources that are explicitly referenced in the fixtf_*.py files.")
    output.append("There may be additional AWS Terraform resources available in the provider that are not yet implemented.")

output.append("")
output.append("---")
output.append("")
output.append("## How to Add a Missing Resource")
output.append("")
output.append("For each missing resource, follow these steps:")
output.append("")
output.append("1. **Find Terraform documentation:**")
output.append("   - URL: `https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/<resource_name>`")
output.append("")
output.append("2. **Identify the AWS service:**")
output.append("   - Example: EC2, S3, Lambda, RDS, etc.")
output.append("")
output.append("3. **Find the boto3 client name:**")
output.append("   - Example: `ec2`, `s3`, `lambda`, `rds`")
output.append("   - Reference: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html")
output.append("")
output.append("4. **Find the boto3 API method:**")
output.append("   - Look for `describe_*` or `list_*` methods")
output.append("   - Example: `describe_vpcs`, `list_functions`, `describe_db_instances`")
output.append("")
output.append("5. **Add entry to `code/fixtf_aws_resources/aws_dict.py`:**")
output.append("")
output.append("### Example Entry:")
output.append("")
output.append("```python")
output.append("aws_vpc = {")
output.append('    "clfn":     "ec2",              # boto3 client name')
output.append('    "descfn":   "describe_vpcs",    # boto3 API method')
output.append('    "topkey":   "Vpcs",             # top-level key in response')
output.append('    "key":      "VpcId",            # resource identifier')
output.append('    "filterid": "VpcId"             # filter parameter name')
output.append("}")
output.append("```")

# Write to file
output_file = 'code/.automation/resources-not-in-dict.md'
with open(output_file, 'w') as f:
    f.write('\n'.join(output))

print(f"\nGenerated {output_file}")
