#!/usr/bin/env python3
"""
Split to-test-stack.md into READY resources and unsupported resources
"""

import re
from collections import defaultdict

# Read the file
with open('code/.automation/to-test-stack.md', 'r') as f:
    lines = f.readlines()

# Separate resources
ready_resources = []
unsupported_resources = []
header_lines = []
footer_lines = []
current_service = None
in_resources = False
in_footer = False

ready_by_service = defaultdict(list)
unsupported_by_service = defaultdict(list)

for line in lines:
    line = line.rstrip('\n')
    
    # Detect sections
    if line.startswith('## Resources by Service'):
        in_resources = True
        continue
    
    if in_resources and line.startswith('## Implementation Checklist'):
        in_footer = True
        in_resources = False
    
    # Collect header (before resources section)
    if not in_resources and not in_footer and '## Resources by Service' not in line:
        header_lines.append(line)
        continue
    
    # Collect footer (after resources section)
    if in_footer:
        footer_lines.append(line)
        continue
    
    # Process resources section
    if in_resources:
        # Track current service
        if line.startswith('### '):
            current_service = line
            continue
        
        # Process resource lines
        if line.startswith('- [x] `AWS::'):
            if '<!-- READY:' in line:
                ready_by_service[current_service].append(line)
            else:
                unsupported_by_service[current_service].append(line)
        elif line.strip() == '':
            # Keep blank lines with their service
            continue

# Count statistics
ready_count = sum(len(resources) for resources in ready_by_service.values())
unsupported_count = sum(len(resources) for resources in unsupported_by_service.values())

# Generate READY resources file (to-test-stack.md)
ready_output = []
ready_output.extend(header_lines)
ready_output.append('')
ready_output.append(f'**Total Resources:** {ready_count}')
ready_output.append(f'**Services:** {len(ready_by_service)}')
ready_output.append('')
ready_output.append('## Resources by Service')
ready_output.append('')

for service in sorted(ready_by_service.keys()):
    resources = ready_by_service[service]
    ready_output.append(service)
    ready_output.append('')
    for resource in resources:
        ready_output.append(resource)
    ready_output.append('')

ready_output.extend(footer_lines)

# Generate unsupported resources file
unsupported_output = []
unsupported_output.append('# CloudFormation Stack Resources - Unsupported')
unsupported_output.append('')
unsupported_output.append('This file lists all CloudFormation resource types that cannot currently be implemented in aws2tf due to:')
unsupported_output.append('- No Terraform AWS provider support')
unsupported_output.append('- Marked as not implemented in aws2tf (aws_not_implemented.py)')
unsupported_output.append('- No import support in Terraform (aws_no_import.py)')
unsupported_output.append('')
unsupported_output.append(f'**Total Unsupported Resources:** {unsupported_count}')
unsupported_output.append(f'**Services:** {len(unsupported_by_service)}')
unsupported_output.append('')
unsupported_output.append('## Status Categories')
unsupported_output.append('')
unsupported_output.append('- **NO TERRAFORM SUPPORT**: Terraform AWS provider does not have an equivalent resource')
unsupported_output.append('- **NOT SUPPORTED**: Resource exists in Terraform but is in aws_not_implemented.py')
unsupported_output.append('- **NO IMPORT SUPPORT**: Terraform can create but cannot import this resource type')
unsupported_output.append('')
unsupported_output.append('## Unsupported Resources by Service')
unsupported_output.append('')

for service in sorted(unsupported_by_service.keys()):
    resources = unsupported_by_service[service]
    unsupported_output.append(service)
    unsupported_output.append('')
    for resource in resources:
        unsupported_output.append(resource)
    unsupported_output.append('')

unsupported_output.append('## Notes')
unsupported_output.append('')
unsupported_output.append('### NO TERRAFORM SUPPORT Resources')
unsupported_output.append('')
unsupported_output.append('These resources are from AWS services that are not yet supported by the Terraform AWS provider.')
unsupported_output.append('They cannot be implemented in aws2tf until Terraform adds support.')
unsupported_output.append('')
unsupported_output.append('**Action Required:** Monitor Terraform AWS provider releases for new resource support.')
unsupported_output.append('')
unsupported_output.append('### NOT SUPPORTED Resources')
unsupported_output.append('')
unsupported_output.append('These resources have Terraform support but are marked as not implemented in aws2tf.')
unsupported_output.append('They are listed in `code/fixtf_aws_resources/aws_not_implemented.py`.')
unsupported_output.append('')
unsupported_output.append('**Action Required:** Follow the standard resource testing procedure to implement these resources.')
unsupported_output.append('')
unsupported_output.append('### NO IMPORT SUPPORT Resources')
unsupported_output.append('')
unsupported_output.append('These resources can be created by Terraform but cannot be imported from existing infrastructure.')
unsupported_output.append('They are listed in `code/fixtf_aws_resources/aws_no_import.py`.')
unsupported_output.append('')
unsupported_output.append('**Action Required:** These resources cannot be imported via aws2tf. They can only be managed if created by Terraform.')

# Write files
with open('code/.automation/to-test-stack.md', 'w') as f:
    f.write('\n'.join(ready_output))

with open('code/.automation/stack-unsupported.md', 'w') as f:
    f.write('\n'.join(unsupported_output))

# Print statistics
print("=" * 60)
print("RESOURCE SPLIT COMPLETE")
print("=" * 60)
print(f"\nREADY resources (to-test-stack.md):")
print(f"  Total: {ready_count}")
print(f"  Services: {len(ready_by_service)}")
print(f"\nUNSUPPORTED resources (stack-unsupported.md):")
print(f"  Total: {unsupported_count}")
print(f"  Services: {len(unsupported_by_service)}")
print(f"\nFiles created:")
print(f"  - code/.automation/to-test-stack.md (READY resources only)")
print(f"  - code/.automation/stack-unsupported.md (unsupported resources)")
print("=" * 60)
