#!/usr/bin/env python3
"""
Apply Method Name Fixes to aws_dict.py

Reads method_fixes.txt and applies fixes to aws_dict.py:
- If there's exactly one suggestion, update the method name
- If there are no suggestions, add a comment "### Needs manual investigation"
"""

import re
import os

print("=" * 70)
print("AWS Dictionary Method Name Fix Applicator")
print("=" * 70)

# File paths
fixes_path = os.path.join(os.path.dirname(__file__), 'method_fixes.txt')
aws_dict_path = os.path.join(os.path.dirname(__file__), '..', 'fixtf_aws_resources', 'aws_dict.py')

print(f"\n📖 Reading fixes file: {fixes_path}")
with open(fixes_path, 'r') as f:
    fixes_content = f.read()

print(f"📖 Reading aws_dict.py: {aws_dict_path}")
with open(aws_dict_path, 'r') as f:
    aws_dict_content = f.read()

print("\n🔍 Parsing fixes...")
# Parse the fixes file
fixes = {}
current_resource = None
current_incorrect = None
current_suggestions = None

for line in fixes_content.split('\n'):
    if line.startswith('## aws_'):
        current_resource = line[3:].strip()
    elif line.startswith('- Incorrect:'):
        current_incorrect = line.split(':', 1)[1].strip()
    elif line.startswith('- Suggestions:'):
        suggestions_str = line.split(':', 1)[1].strip()
        if suggestions_str == 'NONE - Needs manual investigation':
            current_suggestions = []
        else:
            # Split by comma and clean up
            current_suggestions = [s.strip() for s in suggestions_str.split(',')]
        
        # Save the fix
        if current_resource and current_incorrect:
            fixes[current_resource] = {
                'incorrect': current_incorrect,
                'suggestions': current_suggestions
            }

print(f"✓ Parsed {len(fixes)} fixes")

print("\n🔧 Applying fixes to aws_dict.py...")
changes_made = 0
comments_added = 0

for resource, fix_info in sorted(fixes.items()):
    incorrect = fix_info['incorrect']
    suggestions = fix_info['suggestions']
    
    print(f"\n  Processing: {resource}")
    print(f"    Incorrect method: {incorrect}")
    
    # Find the resource definition in aws_dict.py
    # Pattern: resource_name = {\n\t"clfn":\t\t"...",\n\t"descfn":\t"incorrect_method",
    pattern = rf'({resource} = \{{[^}}]*?"descfn":\s*")({re.escape(incorrect)})(")'
    
    if len(suggestions) == 1:
        # Apply the fix
        correct_method = suggestions[0]
        print(f"    ✓ Applying fix: {correct_method}")
        
        new_content = re.sub(pattern, rf'\1{correct_method}\3', aws_dict_content)
        
        if new_content != aws_dict_content:
            aws_dict_content = new_content
            changes_made += 1
            print(f"    ✓ Changed!")
        else:
            print(f"    ⚠️  Pattern not found in aws_dict.py")
    
    elif len(suggestions) == 0:
        # Add comment for manual investigation
        print(f"    → Adding 'Needs manual investigation' comment")
        
        # Find the resource definition and add comment before it
        resource_pattern = rf'({resource} = \{{)'
        comment = f'### Needs manual investigation - method: {incorrect}\n'
        
        new_content = re.sub(resource_pattern, comment + r'\1', aws_dict_content)
        
        if new_content != aws_dict_content:
            aws_dict_content = new_content
            comments_added += 1
            print(f"    ✓ Comment added!")
        else:
            print(f"    ⚠️  Resource definition not found in aws_dict.py")
    
    else:
        # Multiple suggestions - skip
        print(f"    ⚠️  Multiple suggestions ({len(suggestions)}), skipping")
        print(f"       Suggestions: {', '.join(suggestions[:3])}")

print("\n💾 Writing updated aws_dict.py...")
with open(aws_dict_path, 'w') as f:
    f.write(aws_dict_content)

print("\n" + "=" * 70)
print(f"✅ Fixes applied successfully!")
print(f"📊 Summary:")
print(f"  • Method names changed: {changes_made}")
print(f"  • Comments added for manual investigation: {comments_added}")
print(f"  • Total fixes processed: {len(fixes)}")
print("=" * 70)
