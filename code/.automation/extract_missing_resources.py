#!/usr/bin/env python3
"""
Extract the list of missing resources from resources-not-in-dict.md
"""

import re

with open('code/.automation/resources-not-in-dict.md', 'r') as f:
    content = f.read()

# Extract resources from the table
pattern = r'\| \d+ \| `(aws_[a-z_0-9]+)` \| ([a-z]+) \|'
matches = re.findall(pattern, content)

print(f"Found {len(matches)} missing resources")

# Save to a simple list file
with open('code/.automation/missing_resources_list.txt', 'w') as f:
    for resource, service in matches:
        f.write(f"{resource}\t{service}\n")

print("Saved to missing_resources_list.txt")

# Print first 10
print("\nFirst 10 missing resources:")
for i, (resource, service) in enumerate(matches[:10], 1):
    print(f"{i}. {resource} (service: {service})")
