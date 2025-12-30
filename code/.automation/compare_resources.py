#!/usr/bin/env python3
"""
Compare master-aws-resource-list.md with aws_dict.py to find missing resources
"""

import re

# Read the master list of all Terraform AWS resources
with open('code/.automation/master-aws-resource-list.md', 'r') as f:
    master_resources = set(line.strip() for line in f if line.strip())

print(f"Found {len(master_resources)} resources in master list")

# Read the aws_dict.py file to get existing resources
with open('code/fixtf_aws_resources/aws_dict.py', 'r') as f:
    dict_content = f.read()

# Extract all resource names that are already defined in aws_dict.py
existing_pattern = r'^(aws_[a-z_0-9]+)\s*=\s*\{'
existing_resources = set(re.findall(existing_pattern, dict_content, re.MULTILINE))

print(f"Found {len(existing_resources)} resources in aws_dict.py")

# Find missing resources
missing_resources = sorted(master_resources - existing_resources)

print(f"Found {len(missing_resources)} missing resources")

# Organize by service prefix for better readability
from collections import defaultdict
by_service = defaultdict(list)

for resource in missing_resources:
    # Extract service name from resource (e.g., aws_ec2_instance -> ec2)
    parts = resource.split('_')
    if len(parts) >= 2:
        service = parts[1]  # aws_SERVICE_resource
        by_service[service].append(resource)
    else:
        by_service['other'].append(resource)

# Generate markdown output
output = []
output.append("# AWS Terraform Resources NOT in aws_dict.py")
output.append("")
output.append("This file lists Terraform AWS resources from the official provider documentation")
output.append("that are NOT yet defined in `aws_dict.py`.")
output.append("")
output.append(f"**Total Missing Resources:** {len(missing_resources)}")
output.append(f"**Total Existing Resources:** {len(existing_resources)}")
output.append(f"**Total Master List Resources:** {len(master_resources)}")
output.append(f"**Coverage:** {len(existing_resources) / len(master_resources) * 100:.1f}%")
output.append("")
output.append("---")
output.append("")
output.append("## Summary by Service")
output.append("")
output.append("| Service | Missing Resources |")
output.append("|---------|------------------|")

for service in sorted(by_service.keys()):
    count = len(by_service[service])
    output.append(f"| {service} | {count} |")

output.append("")
output.append("---")
output.append("")
output.append("## All Missing Resources")
output.append("")
output.append("These resources need to be added to `aws_dict.py` with:")
output.append("- Terraform resource name")
output.append("- Boto3 client name (clfn)")
output.append("- Boto3 describe/list API method (descfn)")
output.append("- Top-level key in API response (topkey)")
output.append("- Resource identifier key (key)")
output.append("- Filter ID (filterid)")
output.append("")
output.append("| # | Terraform Resource | Service |")
output.append("|---|-------------------|---------|")

for idx, resource in enumerate(missing_resources, 1):
    parts = resource.split('_')
    service = parts[1] if len(parts) >= 2 else 'unknown'
    output.append(f"| {idx} | `{resource}` | {service} |")

output.append("")
output.append("---")
output.append("")
output.append("## Missing Resources by Service")
output.append("")

for service in sorted(by_service.keys()):
    resources = by_service[service]
    output.append(f"### {service.upper()} ({len(resources)} resources)")
    output.append("")
    for resource in sorted(resources):
        output.append(f"- `{resource}`")
    output.append("")

output.append("---")
output.append("")
output.append("## How to Add a Missing Resource")
output.append("")
output.append("For each missing resource, follow these steps:")
output.append("")
output.append("### 1. Find Terraform Documentation")
output.append("")
output.append("URL format: `https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/<resource_name>`")
output.append("")
output.append("Example: `https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/vpc`")
output.append("")
output.append("### 2. Identify the AWS Service")
output.append("")
output.append("Determine which AWS service this resource belongs to (e.g., EC2, S3, Lambda, RDS)")
output.append("")
output.append("### 3. Find the Boto3 Client Name")
output.append("")
output.append("The boto3 client name usually matches the service name in lowercase with hyphens.")
output.append("")
output.append("Examples:")
output.append("- EC2 → `ec2`")
output.append("- S3 → `s3`")
output.append("- Lambda → `lambda`")
output.append("- RDS → `rds`")
output.append("- API Gateway → `apigateway`")
output.append("- API Gateway V2 → `apigatewayv2`")
output.append("")
output.append("Reference: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html")
output.append("")
output.append("### 4. Find the Boto3 API Method")
output.append("")
output.append("Look for the appropriate `describe_*` or `list_*` method that returns all resources of this type.")
output.append("")
output.append("Examples:")
output.append("- VPCs → `describe_vpcs`")
output.append("- Lambda Functions → `list_functions`")
output.append("- RDS Instances → `describe_db_instances`")
output.append("- S3 Buckets → `list_buckets`")
output.append("")
output.append("### 5. Determine Response Structure")
output.append("")
output.append("Call the API method and examine the response to find:")
output.append("- **topkey**: The top-level key containing the list of resources")
output.append("- **key**: The field that uniquely identifies each resource")
output.append("- **filterid**: The parameter name used to filter by ID")
output.append("")
output.append("### 6. Add Entry to aws_dict.py")
output.append("")
output.append("Add the resource definition to `code/fixtf_aws_resources/aws_dict.py`:")
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
output.append("")
output.append("### Example: Adding aws_subnet")
output.append("")
output.append("1. **Terraform docs**: https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/subnet")
output.append("2. **AWS Service**: EC2")
output.append("3. **Boto3 client**: `ec2`")
output.append("4. **Boto3 method**: `describe_subnets`")
output.append("5. **Response structure**:")
output.append("   ```python")
output.append("   {")
output.append('       "Subnets": [')
output.append("           {")
output.append('               "SubnetId": "subnet-12345",')
output.append("               ...")
output.append("           }")
output.append("       ]")
output.append("   }")
output.append("   ```")
output.append("6. **Entry**:")
output.append("   ```python")
output.append("   aws_subnet = {")
output.append('       "clfn":     "ec2",')
output.append('       "descfn":   "describe_subnets",')
output.append('       "topkey":   "Subnets",')
output.append('       "key":      "SubnetId",')
output.append('       "filterid": "SubnetId"')
output.append("   }")
output.append("   ```")

# Write to file
output_file = 'code/.automation/resources-not-in-dict.md'
with open(output_file, 'w') as f:
    f.write('\n'.join(output))

print(f"\nGenerated {output_file}")
print(f"Coverage: {len(existing_resources) / len(master_resources) * 100:.1f}%")
