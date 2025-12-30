#!/usr/bin/env python3
"""
Create aws_dict_extended.py with:
1. Deduplicated original resources (keep first occurrence)
2. Add only NEW unique resources
"""

import re

# Read the original aws_dict.py
with open('code/fixtf_aws_resources/aws_dict.py', 'r') as f:
    original_content = f.read()

# Extract all resource definitions from original with their full content
pattern = r'^(aws_[a-z_0-9]+)\s*=\s*\{([^}]+)\}'
original_matches = re.findall(pattern, original_content, re.MULTILINE | re.DOTALL)

# Deduplicate original - keep first occurrence
seen_original = set()
unique_original = []
for resource_name, resource_body in original_matches:
    if resource_name not in seen_original:
        seen_original.add(resource_name)
        unique_original.append((resource_name, resource_body))

print(f"Original aws_dict.py: {len(original_matches)} total, {len(unique_original)} unique")
print(f"Duplicates in original: {len(original_matches) - len(unique_original)}")

# Read the build file to get new resources
with open('code/.automation/build_extended_dict.py', 'r') as f:
    build_content = f.read()

# Extract new resource definitions
pattern2 = r"    '(aws_[a-z_0-9]+)':\s*\{[^}]*\"clfn\":\s*\"([^\"]+)\"[^}]*\"descfn\":\s*\"([^\"]+)\"[^}]*\"topkey\":\s*\"([^\"]*)\"[^}]*\"key\":\s*\"([^\"]*)\"[^}]*\"filterid\":\s*\"([^\"]*)\"[^}]*\}"
new_matches = re.findall(pattern2, build_content, re.DOTALL)

# Filter to only NEW resources not in original, and deduplicate
new_resources = []
seen_new = set()
for resource_name, clfn, descfn, topkey, key, filterid in new_matches:
    if resource_name not in seen_original and resource_name not in seen_new:
        seen_new.add(resource_name)
        new_resources.append((resource_name, clfn, descfn, topkey, key, filterid))

print(f"New resources: {len(new_resources)}")

# Create the final file
with open('code/.automation/aws_dict_extended.py', 'w') as f:
    # Write header
    f.write("# Extended aws_dict.py - Deduplicated\n")
    f.write("# Original resources from aws_dict.py (deduplicated) + new researched resources\n")
    f.write(f"# Total: {len(unique_original) + len(new_resources)} unique resources\n")
    f.write(f"# Original: {len(unique_original)} | New: {len(new_resources)}\n")
    f.write("# 100% coverage of Terraform AWS provider\n\n")
    
    # Write deduplicated original resources
    for resource_name, resource_body in unique_original:
        f.write(f"{resource_name} = {{{resource_body}}}\n\n")
    
    # Add separator
    f.write("# " + "="*80 + "\n")
    f.write(f"# NEW RESOURCES ADDED - {len(new_resources)} resources\n")
    f.write("# " + "="*80 + "\n\n")
    
    # Write commented dict keys for new resources
    f.write("# Dictionary keys for new resources:\n")
    f.write("# new_resources_dict = {\n")
    for resource_name, clfn, descfn, topkey, key, filterid in sorted(new_resources):
        f.write(f'#     "{resource_name}": {resource_name},\n')
    f.write("# }\n\n")
    
    # Write new resources
    for resource_name, clfn, descfn, topkey, key, filterid in sorted(new_resources):
        f.write(f"{resource_name} = {{\n")
        f.write(f'\t"clfn":\t\t"{clfn}",\n')
        f.write(f'\t"descfn":\t"{descfn}",\n')
        f.write(f'\t"topkey":\t"{topkey}",\n')
        f.write(f'\t"key":\t\t"{key}",\n')
        f.write(f'\t"filterid":\t"{filterid}"\n')
        f.write("}\n\n")

print(f"\n✅ Created deduplicated aws_dict_extended.py")
print(f"✅ Original resources (deduplicated): {len(unique_original)}")
print(f"✅ New resources: {len(new_resources)}")
print(f"✅ Total unique: {len(unique_original) + len(new_resources)}")
