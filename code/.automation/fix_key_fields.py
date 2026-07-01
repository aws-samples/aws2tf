#!/usr/bin/env python3
"""
Fix key Field Values in aws_dict.py

Reads aws_dict_verification2.md and extracts the correct key field values from API responses,
then updates aws_dict.py accordingly.
"""

import re
import os

print("=" * 70)
print("AWS Dictionary key Field Fixer")
print("=" * 70)

# File paths
report_path = os.path.join(os.path.dirname(__file__), 'aws_dict_verification2.md')
aws_dict_path = os.path.join(os.path.dirname(__file__), '..', 'fixtf_aws_resources', 'aws_dict.py')

print(f"\n📖 Reading verification report: {report_path}")
with open(report_path, 'r') as f:
    content = f.read()
print(f"✓ Read {len(content):,} characters")

print("\n🔍 Extracting key_field_missing errors...")
print("  → Parsing report line by line...")

# Parse line by line for better performance
key_fixes = []
current_resource = None

lines = content.split('\n')
total_lines = len(lines)
print(f"  → Processing {total_lines:,} lines...")

for idx, line in enumerate(lines):
    if idx % 10000 == 0 and idx > 0:
        print(f"    [{idx:,}/{total_lines:,}] lines processed, found {len(key_fixes)} errors so far...")
    
    # Look for resource header
    if line.startswith('### `aws_'):
        match = re.match(r'### `(aws_\w+)`', line)
        if match:
            current_resource = match.group(1)
    
    # Look for key field error in Issues section
    # Format: - key field 'ARN' not found in response object. Available fields: ['Id', 'Name', 'ResponseMetadata']
    # Or: - key field 'ARN' not found in response items. Available fields: ['Id', 'Name']
    elif current_resource and "- key field '" in line and "' not found in response" in line:
        # Extract incorrect key and available keys
        match = re.search(r"- key field '([^']+)' not found in response (?:object|items)\. Available fields: \[([^\]]+)\]", line)
        if match:
            incorrect = match.group(1)
            available_str = match.group(2)
            # Parse available keys
            available_keys = [k.strip().strip("'\"") for k in available_str.split(',')]
            # Filter out ResponseMetadata and common pagination fields
            available_keys = [k for k in available_keys if k not in ['ResponseMetadata', 'NextToken', 'Marker', 'MaxItems', 'IsTruncated', 'Quantity', 'hasMoreResults']]
            
            key_fixes.append({
                'resource': current_resource,
                'incorrect': incorrect,
                'available_keys': available_keys
            })
            if len(key_fixes) % 10 == 0:
                print(f"    Found error #{len(key_fixes)}: {current_resource}")

print(f"✓ Found {len(key_fixes)} resources with key_field_missing errors")

print("\n📋 Listing all resources with key field errors:")
for idx, fix in enumerate(key_fixes, 1):
    print(f"  [{idx}/{len(key_fixes)}] {fix['resource']}")
    print(f"      Incorrect: {fix['incorrect']}")
    print(f"      Available: {', '.join(fix['available_keys'][:5])}")
    if len(fix['available_keys']) > 5:
        print(f"                 ... and {len(fix['available_keys']) - 5} more")

# Save fixes to a file for review
fixes_path = os.path.join(os.path.dirname(__file__), 'key_field_fixes.txt')
print(f"\n📝 Writing fixes to: {fixes_path}")

with open(fixes_path, 'w') as f:
    f.write("# key Field Fixes\n\n")
    
    for fix in key_fixes:
        f.write(f"## {fix['resource']}\n")
        f.write(f"- Incorrect: {fix['incorrect']}\n")
        f.write(f"- Available: {', '.join(fix['available_keys'])}\n")
        f.write("\n")

print(f"✅ Fixes written to {fixes_path}")

# Now apply the fixes automatically
print("\n🔧 Auto-selecting and applying fixes...")

changes_made = 0
comments_added = 0

# Read aws_dict.py
with open(aws_dict_path, 'r') as f:
    aws_dict_content = f.read()

for fix in key_fixes:
    resource = fix['resource']
    incorrect = fix['incorrect']
    available = fix['available_keys']
    
    print(f"\n  Processing: {resource}")
    print(f"    Incorrect key: {incorrect}")
    
    if len(available) == 0:
        # No available keys - add comment
        print(f"    → No available keys - adding 'Needs manual investigation' comment")
        
        resource_pattern = rf'({resource} = \{{)'
        comment = f'### Needs manual investigation - key field: {incorrect} (no keys available)\n'
        
        new_content = re.sub(resource_pattern, comment + r'\1', aws_dict_content)
        
        if new_content != aws_dict_content:
            aws_dict_content = new_content
            comments_added += 1
            print(f"    ✓ Comment added!")
        else:
            print(f"    ⚠️  Resource definition not found")
    
    elif len(available) == 1:
        # Only one available key - use it
        correct = available[0]
        print(f"    ✓ Auto-selected: {correct}")
        
        # Find and replace the key in aws_dict.py
        pattern = rf'({resource} = \{{[^}}]*?"key":\s*")({re.escape(incorrect)})(")'
        
        new_content = re.sub(pattern, rf'\1{correct}\3', aws_dict_content)
        
        if new_content != aws_dict_content:
            aws_dict_content = new_content
            changes_made += 1
            print(f"    ✓ Changed!")
        else:
            print(f"    ⚠️  Pattern not found in aws_dict.py")
    
    else:
        # Multiple available keys - try to find best match
        incorrect_lower = incorrect.lower()
        best_match = None
        best_score = 0
        
        for key in available:
            key_lower = key.lower()
            score = 0
            
            # Exact match (case-insensitive)
            if key_lower == incorrect_lower:
                score = 100
            # Contains or is contained
            elif incorrect_lower in key_lower or key_lower in incorrect_lower:
                score = 50
            # Common patterns: Id, Arn, Name
            elif 'id' in key_lower and 'id' in incorrect_lower:
                score = 40
            elif 'arn' in key_lower and 'arn' in incorrect_lower:
                score = 40
            elif 'name' in key_lower and 'name' in incorrect_lower:
                score = 40
            
            if score > best_score:
                best_score = score
                best_match = key
        
        # If no good match, prefer Id > Arn > Name > first available
        if not best_match or best_score < 30:
            for preferred in ['Id', 'id', 'Arn', 'arn', 'ARN', 'Name', 'name']:
                if preferred in available:
                    best_match = preferred
                    break
            if not best_match:
                best_match = available[0]
        
        correct = best_match
        print(f"    ✓ Auto-selected: {correct} (from {len(available)} options)")
        
        # Find and replace the key in aws_dict.py
        pattern = rf'({resource} = \{{[^}}]*?"key":\s*")({re.escape(incorrect)})(")'
        
        new_content = re.sub(pattern, rf'\1{correct}\3', aws_dict_content)
        
        if new_content != aws_dict_content:
            aws_dict_content = new_content
            changes_made += 1
            print(f"    ✓ Changed!")
        else:
            print(f"    ⚠️  Pattern not found in aws_dict.py")

print("\n💾 Writing updated aws_dict.py...")
with open(aws_dict_path, 'w') as f:
    f.write(aws_dict_content)

print("\n" + "=" * 70)
print(f"✅ Fixes applied successfully!")
print(f"📊 Summary:")
print(f"  • key field values changed: {changes_made}")
print(f"  • Comments added for manual investigation: {comments_added}")
print(f"  • Total fixes processed: {len(key_fixes)}")
print("=" * 70)
