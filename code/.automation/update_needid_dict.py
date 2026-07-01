#!/usr/bin/env python3
"""
Update needid_dict.py with Resources Requiring Parent IDs

Reads aws_dict_verification2.md and extracts resources that require parent parameters,
then adds them to needid_dict.py.
"""

import re
import os

print("=" * 70)
print("needid_dict.py Updater")
print("=" * 70)

# File paths
report_path = os.path.join(os.path.dirname(__file__), 'aws_dict_verification2.md')
needid_dict_path = os.path.join(os.path.dirname(__file__), '..', 'fixtf_aws_resources', 'needid_dict.py')

print(f"\n📖 Reading verification report: {report_path}")
with open(report_path, 'r') as f:
    content = f.read()
print(f"✓ Read {len(content):,} characters")

print(f"\n📖 Reading needid_dict.py: {needid_dict_path}")
with open(needid_dict_path, 'r') as f:
    needid_content = f.read()
print(f"✓ Read {len(needid_content):,} characters")

print("\n🔍 Extracting resources requiring parent parameters...")
print("  → Parsing report line by line...")

# Parse line by line for better performance
needid_additions = {}
current_resource = None
current_client = None
current_params = []

lines = content.split('\n')
total_lines = len(lines)
print(f"  → Processing {total_lines:,} lines...")

for idx, line in enumerate(lines):
    if idx % 10000 == 0 and idx > 0:
        print(f"    [{idx:,}/{total_lines:,}] lines processed, found {len(needid_additions)} resources so far...")
    
    # Look for resource header
    if line.startswith('### `aws_'):
        match = re.match(r'### `(aws_\w+)`', line)
        if match:
            current_resource = match.group(1)
            current_client = None
            current_params = []
    
    # Look for client
    elif '- **Client:**' in line:
        match = re.search(r'- \*\*Client:\*\* `(\w+)`', line)
        if match:
            current_client = match.group(1)
    
    # Look for missing required parameters
    elif current_resource and 'Missing required parameter in input:' in line:
        # Extract parameter name
        match = re.search(r'Missing required parameter in input: "([^"]+)"', line)
        if match:
            param = match.group(1)
            if param not in current_params:
                current_params.append(param)
    
    # When we hit "Action Needed:" we know we've collected all params for this resource
    elif current_resource and current_client and current_params and '**Action Needed:**' in line:
        # Check if this resource is already in needid_dict.py
        resource_pattern = rf'^{re.escape(current_resource)} = \{{'
        if not re.search(resource_pattern, needid_content, re.MULTILINE):
            # Not in needid_dict.py, add it
            needid_additions[current_resource] = {
                'params': current_params.copy(),
                'client': current_client
            }
            if len(needid_additions) % 10 == 0:
                print(f"    Found resource #{len(needid_additions)}: {current_resource}")
        
        # Reset for next resource
        current_params = []

print(f"✓ Found {len(needid_additions)} resources needing needid_dict.py entries")

print("\n📋 Listing all resources to be added:")
for idx, (resource, info) in enumerate(sorted(needid_additions.items()), 1):
    params_str = ','.join(info['params'])
    print(f"  [{idx}/{len(needid_additions)}] {resource}")
    print(f"      Params: {params_str}")
    print(f"      Client: {info['client']}")

# Now add these entries to needid_dict.py
print(f"\n🔧 Adding {len(needid_additions)} entries to needid_dict.py...")

# Find the end of the file (before any closing braces or comments)
# We'll add new entries at the end
additions_text = "\n# Auto-generated additions from verification report\n"

for resource, info in sorted(needid_additions.items()):
    params_str = ','.join(info['params'])
    additions_text += f"\n{resource} = {{\n"
    additions_text += f'  "param": "{params_str}",\n'
    additions_text += f'  "clfn": "{info["client"]}"\n'
    additions_text += "}\n"

# Append to the end of needid_dict.py
needid_content += additions_text

print("\n💾 Writing updated needid_dict.py...")
with open(needid_dict_path, 'w') as f:
    f.write(needid_content)

print("\n" + "=" * 70)
print(f"✅ Updates applied successfully!")
print(f"📊 Summary:")
print(f"  • Entries added to needid_dict.py: {len(needid_additions)}")
print(f"  • These resources require parent IDs to list/describe")
print("=" * 70)

# Save a summary file
summary_path = os.path.join(os.path.dirname(__file__), 'needid_additions.txt')
print(f"\n📝 Writing summary to: {summary_path}")

with open(summary_path, 'w') as f:
    f.write("# needid_dict.py Additions Summary\n\n")
    f.write(f"Total resources added: {len(needid_additions)}\n\n")
    
    for resource, info in sorted(needid_additions.items()):
        params_str = ','.join(info['params'])
        f.write(f"## {resource}\n")
        f.write(f"- Parameters: {params_str}\n")
        f.write(f"- Client: {info['client']}\n")
        f.write("\n")

print(f"✅ Summary written to {summary_path}")
