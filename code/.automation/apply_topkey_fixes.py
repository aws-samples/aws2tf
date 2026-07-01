#!/usr/bin/env python3
"""
Apply topkey Fixes to aws_dict.py

Automatically selects the most likely correct topkey and applies fixes.
"""

import re
import os

print("=" * 70)
print("AWS Dictionary topkey Fix Applicator")
print("=" * 70)

# File paths
fixes_path = os.path.join(os.path.dirname(__file__), 'topkey_fixes.txt')
aws_dict_path = os.path.join(os.path.dirname(__file__), '..', 'fixtf_aws_resources', 'aws_dict.py')

print(f"\n📖 Reading fixes file: {fixes_path}")
with open(fixes_path, 'r') as f:
    fixes_content = f.read()

print(f"📖 Reading aws_dict.py: {aws_dict_path}")
with open(aws_dict_path, 'r') as f:
    aws_dict_content = f.read()

print("\n🔍 Parsing fixes and auto-selecting correct topkeys...")
# Parse the fixes file
fixes = {}
current_resource = None
current_incorrect = None
current_available = None

for line in fixes_content.split('\n'):
    if line.startswith('## aws_'):
        current_resource = line[3:].strip()
    elif line.startswith('- Incorrect:'):
        current_incorrect = line.split(':', 1)[1].strip()
    elif line.startswith('- Available:'):
        available_str = line.split(':', 1)[1].strip()
        if available_str:
            current_available = [k.strip() for k in available_str.split(',')]
        else:
            current_available = []
        
        # Auto-select the correct topkey
        if current_resource and current_incorrect and current_available is not None:
            # If there's only one available key, use it
            if len(current_available) == 1:
                correct = current_available[0]
            # If there are multiple, try to find the best match
            elif len(current_available) > 1:
                # Prefer keys that are similar to the incorrect one (case-insensitive)
                incorrect_lower = current_incorrect.lower()
                best_match = None
                best_score = 0
                
                for key in current_available:
                    key_lower = key.lower()
                    # Calculate similarity score
                    score = 0
                    if key_lower == incorrect_lower:
                        score = 100
                    elif incorrect_lower in key_lower or key_lower in incorrect_lower:
                        score = 50
                    elif key_lower.replace('_', '') == incorrect_lower.replace('_', ''):
                        score = 90
                    
                    if score > best_score:
                        best_score = score
                        best_match = key
                
                # If no good match, use the first available key
                correct = best_match if best_match else current_available[0]
            else:
                # No available keys - mark for manual investigation
                correct = None
            
            fixes[current_resource] = {
                'incorrect': current_incorrect,
                'available': current_available,
                'correct': correct
            }

print(f"✓ Parsed {len(fixes)} fixes")

print("\n🔧 Applying fixes to aws_dict.py...")
changes_made = 0
comments_added = 0

for resource, fix_info in sorted(fixes.items()):
    incorrect = fix_info['incorrect']
    correct = fix_info['correct']
    available = fix_info['available']
    
    print(f"\n  Processing: {resource}")
    print(f"    Incorrect topkey: {incorrect}")
    
    if correct:
        print(f"    ✓ Auto-selected: {correct}")
        
        # Find and replace the topkey in aws_dict.py
        # Pattern: resource_name = {\n...\n\t"topkey":\t\t"incorrect_topkey",
        pattern = rf'({resource} = \{{[^}}]*?"topkey":\s*")({re.escape(incorrect)})(")'
        
        new_content = re.sub(pattern, rf'\1{correct}\3', aws_dict_content)
        
        if new_content != aws_dict_content:
            aws_dict_content = new_content
            changes_made += 1
            print(f"    ✓ Changed!")
        else:
            print(f"    ⚠️  Pattern not found in aws_dict.py")
    
    else:
        # No available keys - add comment for manual investigation
        print(f"    → No available keys - adding 'Needs manual investigation' comment")
        
        # Find the resource definition and add comment before it
        resource_pattern = rf'({resource} = \{{)'
        comment = f'### Needs manual investigation - topkey: {incorrect} (no keys available)\n'
        
        new_content = re.sub(resource_pattern, comment + r'\1', aws_dict_content)
        
        if new_content != aws_dict_content:
            aws_dict_content = new_content
            comments_added += 1
            print(f"    ✓ Comment added!")
        else:
            print(f"    ⚠️  Resource definition not found in aws_dict.py")

print("\n💾 Writing updated aws_dict.py...")
with open(aws_dict_path, 'w') as f:
    f.write(aws_dict_content)

print("\n" + "=" * 70)
print(f"✅ Fixes applied successfully!")
print(f"📊 Summary:")
print(f"  • topkey values changed: {changes_made}")
print(f"  • Comments added for manual investigation: {comments_added}")
print(f"  • Total fixes processed: {len(fixes)}")
print("=" * 70)
