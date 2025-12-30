#!/usr/bin/env python3
"""
Generate a comprehensive list of AWS Terraform resources
organized by service with boto3 client information
"""

import re
from collections import defaultdict

# Read the aws_dict.py file
with open('code/fixtf_aws_resources/aws_dict.py', 'r') as f:
    content = f.read()

# Extract all resource definitions
pattern = r'(aws_[a-z_]+)\s*=\s*\{[^}]*"clfn":\s*"([^"]+)"[^}]*"descfn":\s*"([^"]+)"[^}]*\}'
matches = re.findall(pattern, content, re.MULTILINE | re.DOTALL)

# Organize by service (boto3 client)
resources_by_service = defaultdict(list)
for resource_name, boto3_client, boto3_api in matches:
    resources_by_service[boto3_client].append({
        'terraform_resource': resource_name,
        'boto3_client': boto3_client,
        'boto3_api': boto3_api
    })

# Generate markdown output
output = []
output.append("# AWS Terraform Provider Resources")
output.append("")
output.append("Complete list of AWS resources from the Terraform AWS Provider")
output.append(f"Total Resources: {len(matches)}")
output.append(f"Total Services: {len(resources_by_service)}")
output.append("")
output.append("---")
output.append("")

# Table of Contents
output.append("## Table of Contents")
output.append("")
for service in sorted(resources_by_service.keys()):
    service_anchor = service.replace('-', '').replace('_', '')
    output.append(f"- [{service}](#{service_anchor})")
output.append("")
output.append("---")
output.append("")

# Detailed listings
for service in sorted(resources_by_service.keys()):
    output.append(f"## {service}")
    output.append("")
    output.append(f"**Boto3 Client:** `{service}`")
    output.append("")
    output.append("| Terraform Resource | Boto3 API Method |")
    output.append("|-------------------|------------------|")
    
    for resource in sorted(resources_by_service[service], key=lambda x: x['terraform_resource']):
        output.append(f"| `{resource['terraform_resource']}` | `{resource['boto3_api']}` |")
    
    output.append("")

# Write to file
with open('terraform-aws-resources-list.md', 'w') as f:
    f.write('\n'.join(output))

print(f"Generated terraform-aws-resources-list.md")
print(f"Total resources: {len(matches)}")
print(f"Total services: {len(resources_by_service)}")
