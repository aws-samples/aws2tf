#!/usr/bin/env python3
"""
1. Uncomment all entries in aws_dict_extended.py
2. Add them to aws_not_implemented.py
"""

import re

# Read aws_dict_extended.py
with open('code/.automation/aws_dict_extended.py', 'r') as f:
    content = f.read()

# Find all commented dict entries
pattern = r'#     "(aws_[a-z_0-9]+)": (aws_[a-z_0-9]+),'
matches = re.findall(pattern, content)

print(f"Found {len(matches)} commented entries")

# Uncomment them
for key, value in matches:
    old_line = f'#     "{key}": {value},'
    new_line = f'    "{key}": {value},'
    content = content.replace(old_line, new_line)

# Write back to aws_dict_extended.py
with open('code/.automation/aws_dict_extended.py', 'w') as f:
    f.write(content)

print(f"✅ Uncommented {len(matches)} entries in aws_dict_extended.py")

# Read aws_not_implemented.py
with open('code/fixtf_aws_resources/aws_not_implemented.py', 'r') as f:
    not_impl_content = f.read()

# Find where to insert (before the closing brace)
lines = not_impl_content.split('\n')

# Find the last closing brace
insert_index = None
for i in range(len(lines) - 1, -1, -1):
    if lines[i].strip() == '}':
        insert_index = i
        break

if insert_index is None:
    print("❌ Could not find closing brace in aws_not_implemented.py")
    exit(1)

# Create new entries
new_entries = []
for key, value in sorted(matches):
    new_entries.append(f'    "{key}": True,  ### TODO 6.27.0')

# Insert new entries before closing brace
lines.insert(insert_index, '\n    # New resources added from aws_dict_extended.py')
for entry in new_entries:
    lines.insert(insert_index + 1, entry)
    insert_index += 1

# Write back
with open('code/fixtf_aws_resources/aws_not_implemented.py', 'w') as f:
    f.write('\n'.join(lines))

print(f"✅ Added {len(matches)} entries to aws_not_implemented.py")
print(f"\n✅ COMPLETE!")
print(f"   - Uncommented {len(matches)} entries in aws_dict_extended.py")
print(f"   - Added {len(matches)} entries to aws_not_implemented.py")
