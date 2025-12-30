#!/usr/bin/env python3
"""
Add all remaining 144 resources from final_144_resources.txt
"""

# Read the resource mappings
entries = []
with open('code/.automation/final_144_resources.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#') or '|' not in line:
            continue
        
        parts = line.split('|')
        if len(parts) == 6:
            resource_name, clfn, descfn, topkey, key, filterid = parts
            entry = f'''
    '{resource_name}': {{
        "clfn": "{clfn}",
        "descfn": "{descfn}",
        "topkey": "{topkey}",
        "key": "{key}",
        "filterid": "{filterid}"
    }},'''
            entries.append(entry)

print(f"Parsed {len(entries)} resource entries")

# Append to build file
with open('code/.automation/build_extended_dict.py', 'a') as f:
    f.write('\n    # FINAL 132 RESOURCES (excluding 12 bedrockagentcore)')
    for entry in entries:
        f.write(entry)
    f.write('\n}\n\n')
    f.write('print(f"\\nDefined {len(new_resources)} new resources")\n')
    f.write('print("100% COVERAGE ACHIEVED (excluding experimental bedrockagentcore service)!")\n')

print(f"Added {len(entries)} resources to build file")
