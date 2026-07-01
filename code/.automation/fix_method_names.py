#!/usr/bin/env python3
"""
Fix Method Names in aws_dict.py

Reads aws_dict_verification2.md and fixes incorrect method names in aws_dict.py
by looking up the correct methods in boto3 documentation.
"""

import re
import os
import boto3

print("=" * 70)
print("AWS Dictionary Method Name Fixer")
print("=" * 70)

# File paths
report_path = os.path.join(os.path.dirname(__file__), 'aws_dict_verification2.md')
aws_dict_path = os.path.join(os.path.dirname(__file__), '..', 'fixtf_aws_resources', 'aws_dict.py')

print(f"\n📖 Reading verification report: {report_path}")
with open(report_path, 'r') as f:
    content = f.read()
print(f"✓ Read {len(content):,} characters")

print("\n🔍 Extracting method_not_found errors...")
print("  → Parsing report line by line...")

# Parse line by line for better performance
matches = []
current_resource = None
current_client = None
current_method = None
current_error_type = None

lines = content.split('\n')
total_lines = len(lines)
print(f"  → Processing {total_lines:,} lines...")

for idx, line in enumerate(lines):
    if idx % 10000 == 0 and idx > 0:
        print(f"    [{idx:,}/{total_lines:,}] lines processed, found {len(matches)} errors so far...")
    
    # Look for resource header
    if line.startswith('### `aws_'):
        match = re.match(r'### `(aws_\w+)`', line)
        if match:
            current_resource = match.group(1)
            current_client = None
            current_method = None
            current_error_type = None
    
    # Look for client
    elif '- **Client:**' in line:
        match = re.search(r'- \*\*Client:\*\* `(\w+)`', line)
        if match:
            current_client = match.group(1)
    
    # Look for method
    elif '- **Method:**' in line:
        match = re.search(r'- \*\*Method:\*\* `(\w+)`', line)
        if match:
            current_method = match.group(1)
    
    # Look for error type
    elif '- **Error Type:**' in line:
        match = re.search(r'- \*\*Error Type:\*\* `(\w+)`', line)
        if match:
            current_error_type = match.group(1)
            
            # If we have all the info and it's a method_not_found error, save it
            if (current_error_type == 'method_not_found' and 
                current_resource and current_client and current_method):
                matches.append((current_resource, current_client, current_method))
                if len(matches) % 10 == 0:
                    print(f"    Found error #{len(matches)}: {current_resource}")

print(f"✓ Found {len(matches)} resources with method_not_found errors")

print("\n📋 Listing all resources with method errors:")
for idx, (resource, client, method) in enumerate(matches, 1):
    print(f"  [{idx}/{len(matches)}] {resource} - {client}.{method}")

print("\n📊 Grouping by AWS service...")
# Group by client to minimize boto3 client creation
by_client = {}
for resource, client, method in matches:
    if client not in by_client:
        by_client[client] = []
    by_client[client].append((resource, method))

print(f"✓ Grouped into {len(by_client)} AWS services:")
for client_name, resources in sorted(by_client.items()):
    print(f"  • {client_name}: {len(resources)} resource(s)")

print(f"\n🔧 Analyzing {len(by_client)} AWS services...")

# Store fixes
fixes = {}

service_count = 0
total_services = len(by_client)

for client_name, resources in sorted(by_client.items()):
    service_count += 1
    print(f"\n[{service_count}/{total_services}] Service: {client_name} ({len(resources)} resources)")
    
    try:
        print(f"  → Creating boto3 client for '{client_name}'...")
        # Create boto3 client to inspect available methods
        client = boto3.client(client_name, region_name='us-east-1')
        available_methods = [m for m in dir(client) if not m.startswith('_')]
        print(f"  ✓ Found {len(available_methods)} available methods")
        
        resource_count = 0
        for resource, incorrect_method in resources:
            resource_count += 1
            print(f"  [{resource_count}/{len(resources)}] Processing: {resource}")
            print(f"      Incorrect method: {incorrect_method}")
            
            # Try to find similar method names
            suggestions = []
            
            # Common patterns to try
            base_name = incorrect_method.replace('list_', '').replace('describe_', '').replace('get_', '')
            print(f"      Searching for methods containing: '{base_name}'...")
            
            for method in available_methods:
                if base_name in method:
                    suggestions.append(method)
            
            if suggestions:
                print(f"      ✓ Found {len(suggestions)} suggestion(s): {', '.join(suggestions[:5])}")
                if len(suggestions) > 5:
                    print(f"        ... and {len(suggestions) - 5} more")
                fixes[resource] = {
                    'client': client_name,
                    'incorrect': incorrect_method,
                    'suggestions': suggestions
                }
            else:
                print(f"      ⚠️  No suggestions found - needs manual investigation")
                fixes[resource] = {
                    'client': client_name,
                    'incorrect': incorrect_method,
                    'suggestions': []
                }
                
    except Exception as e:
        print(f"  ❌ Error creating client: {e}")
        for resource, incorrect_method in resources:
            print(f"    • {resource}: {incorrect_method} - ERROR")
            fixes[resource] = {
                'client': client_name,
                'incorrect': incorrect_method,
                'suggestions': [],
                'error': str(e)
            }

print("\n" + "=" * 70)
print(f"✅ Analysis complete!")
print(f"📊 Found {len(fixes)} resources needing fixes")
print("=" * 70)

# Save fixes to a file for review
fixes_path = os.path.join(os.path.dirname(__file__), 'method_fixes.txt')
print(f"\n📝 Writing fixes to: {fixes_path}")

with open(fixes_path, 'w') as f:
    f.write("# Method Name Fixes\n\n")
    for resource, fix_info in sorted(fixes.items()):
        f.write(f"## {resource}\n")
        f.write(f"- Client: {fix_info['client']}\n")
        f.write(f"- Incorrect: {fix_info['incorrect']}\n")
        if fix_info['suggestions']:
            f.write(f"- Suggestions: {', '.join(fix_info['suggestions'][:5])}\n")
        else:
            f.write(f"- Suggestions: NONE - Needs manual investigation\n")
        f.write("\n")

print(f"✅ Fixes written to {fixes_path}")
print("\nNext steps:")
print("1. Review method_fixes.txt")
print("2. Manually verify correct methods in boto3 docs")
print("3. Update aws_dict.py with correct method names")
