#!/usr/bin/env python3
"""
Fix topkey Values in aws_dict.py

Reads aws_dict_verification2.md and extracts the correct topkey values from API responses,
then updates aws_dict.py accordingly.
"""

import re
import os

print("=" * 70)
print("AWS Dictionary topkey Value Fixer")
print("=" * 70)

# File paths
report_path = os.path.join(os.path.dirname(__file__), 'aws_dict_verification2.md')
aws_dict_path = os.path.join(os.path.dirname(__file__), '..', 'fixtf_aws_resources', 'aws_dict.py')

print(f"\n📖 Reading verification report: {report_path}")
with open(report_path, 'r') as f:
    content = f.read()
print(f"✓ Read {len(content):,} characters")

print("\n🔍 Extracting topkey_incorrect errors...")
print("  → Parsing report line by line...")

# Parse line by line for better performance
topkey_fixes = []
current_resource = None
current_incorrect_topkey = None

lines = content.split('\n')
total_lines = len(lines)
print(f"  → Processing {total_lines:,} lines...")

for idx, line in enumerate(lines):
    if idx % 10000 == 0 and idx > 0:
        print(f"    [{idx:,}/{total_lines:,}] lines processed, found {len(topkey_fixes)} errors so far...")
    
    # Look for resource header
    if line.startswith('### `aws_'):
        match = re.match(r'### `(aws_\w+)`', line)
        if match:
            current_resource = match.group(1)
            current_incorrect_topkey = None
    
    # Look for topkey error in Issues section
    # Format: - topkey 'FleetStackAssociations' not found in response. Available keys: ['Fleets', 'ResponseMetadata']
    elif current_resource and "- topkey '" in line and "' not found in response" in line:
        # Extract incorrect topkey and available keys
        match = re.search(r"- topkey '([^']+)' not found in response\. Available keys: \[([^\]]+)\]", line)
        if match:
            incorrect = match.group(1)
            available_str = match.group(2)
            # Parse available keys
            available_keys = [k.strip().strip("'\"") for k in available_str.split(',')]
            # Filter out ResponseMetadata
            available_keys = [k for k in available_keys if k != 'ResponseMetadata']
            
            topkey_fixes.append({
                'resource': current_resource,
                'incorrect': incorrect,
                'available_keys': available_keys
            })
            if len(topkey_fixes) % 10 == 0:
                print(f"    Found error #{len(topkey_fixes)}: {current_resource}")

print(f"✓ Found {len(topkey_fixes)} resources with topkey_incorrect errors")

print("\n📋 Listing all resources with topkey errors:")
for idx, fix in enumerate(topkey_fixes, 1):
    print(f"  [{idx}/{len(topkey_fixes)}] {fix['resource']}")
    print(f"      Incorrect: {fix['incorrect']}")
    print(f"      Available: {', '.join(fix['available_keys'][:5])}")
    if len(fix['available_keys']) > 5:
        print(f"                 ... and {len(fix['available_keys']) - 5} more")

# Save fixes to a file for review
fixes_path = os.path.join(os.path.dirname(__file__), 'topkey_fixes.txt')
print(f"\n📝 Writing fixes to: {fixes_path}")

with open(fixes_path, 'w') as f:
    f.write("# topkey Value Fixes\n\n")
    f.write("# Instructions:\n")
    f.write("# - Review each resource and select the correct topkey from available keys\n")
    f.write("# - The correct topkey is usually the plural form that contains the list of resources\n")
    f.write("# - Edit this file and replace 'CHOOSE_FROM_AVAILABLE' with the correct key\n")
    f.write("# - Then run apply_topkey_fixes.py to apply the changes\n\n")
    
    for fix in topkey_fixes:
        f.write(f"## {fix['resource']}\n")
        f.write(f"- Incorrect: {fix['incorrect']}\n")
        f.write(f"- Available: {', '.join(fix['available_keys'])}\n")
        f.write(f"- Correct: CHOOSE_FROM_AVAILABLE\n")
        f.write("\n")

print(f"✅ Fixes written to {fixes_path}")
print("\n" + "=" * 70)
print("Next steps:")
print("1. Review topkey_fixes.txt")
print("2. For each resource, replace 'CHOOSE_FROM_AVAILABLE' with the correct key")
print("3. Run apply_topkey_fixes.py to apply the changes")
print("=" * 70)
