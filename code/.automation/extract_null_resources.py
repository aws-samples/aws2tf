#!/usr/bin/env python3
"""
Extract all CloudFormation resource types from stacks.py that have placeholder entries
calling common.call_resource("aws_null", ...)
"""

import re
from collections import defaultdict

# Read stacks.py
with open('code/stacks.py', 'r') as f:
    content = f.read()

# Pattern to match lines with aws_null
pattern = r'elif type == "(AWS::[^"]+)":\s+common\.call_resource\("aws_null",\s*type\s*\+\s*"\s*"\s*\+\s*pid\)'

matches = re.findall(pattern, content)

# Group by service
resources_by_service = defaultdict(list)
for resource_type in sorted(matches):
    # Extract service name (e.g., AWS::EC2::Instance -> EC2)
    parts = resource_type.split('::')
    if len(parts) >= 2:
        service = parts[1]
        resources_by_service[service].append(resource_type)

# Generate markdown
output = []
output.append("# CloudFormation Stack Resources - To Test")
output.append("")
output.append("This file lists all CloudFormation resource types in `code/stacks.py` that currently have placeholder entries using `common.call_resource(\"aws_null\", ...)`. These resources are recognized but not yet fully implemented.")
output.append("")
output.append(f"**Total Resources:** {len(matches)}")
output.append(f"**Services:** {len(resources_by_service)}")
output.append("")
output.append("## Purpose")
output.append("")
output.append("These placeholder entries allow aws2tf to:")
output.append("1. Recognize the resource type when importing CloudFormation stacks")
output.append("2. Log the resource to `stack-fetched-explicit.log`")
output.append("3. Avoid \"UNPROCESSED\" errors")
output.append("")
output.append("To fully implement any of these resources, follow the stack resource testing procedure in `.kiro/steering/stack-resource-testing.md`.")
output.append("")
output.append("## Resources by Service")
output.append("")

# Output by service
for service in sorted(resources_by_service.keys()):
    resources = resources_by_service[service]
    output.append(f"### {service} ({len(resources)} resources)")
    output.append("")
    for resource in resources:
        output.append(f"- [ ] `{resource}`")
    output.append("")

output.append("## Implementation Checklist")
output.append("")
output.append("For each resource type, the implementation process involves:")
output.append("")
output.append("1. **Check Terraform Support**")
output.append("   - Verify the resource exists in [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)")
output.append("   - Note the Terraform resource name (e.g., `aws_bedrock_agent`)")
output.append("")
output.append("2. **Add to aws_dict.py**")
output.append("   - Define boto3 client name (e.g., `bedrock-agent`)")
output.append("   - Define API method for listing (e.g., `list_agents`)")
output.append("   - Define response key and ID field")
output.append("")
output.append("3. **Create Get Function**")
output.append("   - Implement in `code/get_aws_resources/aws_<service>.py`")
output.append("   - Handle both list all and get specific cases")
output.append("   - Register in `code/common.py`")
output.append("")
output.append("4. **Create Handler (if needed)**")
output.append("   - Implement in `code/fixtf_aws_resources/fixtf_<service>.py`")
output.append("   - Handle computed fields, defaults, and lifecycle blocks")
output.append("   - Register in `code/fixtf.py`")
output.append("")
output.append("5. **Test with CloudFormation Stack**")
output.append("   - Create test CloudFormation stack with the resource")
output.append("   - Run: `./aws2tf.py -r <region> -t stack -i <stack-name>`")
output.append("   - Verify Terraform generation and import")
output.append("   - Document results in test directory")
output.append("")
output.append("6. **Update stacks.py**")
output.append("   - Replace `common.call_resource(\"aws_null\", type+\" \"+pid)`")
output.append("   - With: `common.call_resource(\"aws_<resource_type>\", pid)` or `parn`")
output.append("")
output.append("## Priority Recommendations")
output.append("")
output.append("### High Priority (Common Services)")
output.append("- AWS::Bedrock::* - AI/ML services gaining adoption")
output.append("- AWS::QBusiness::* - Amazon Q Business")
output.append("- AWS::Notifications::* - Cross-service notifications")
output.append("- AWS::Route53Profiles::* - DNS management")
output.append("")
output.append("### Medium Priority (Specialized Services)")
output.append("- AWS::Deadline::* - Media rendering workloads")
output.append("- AWS::IoTFleetWise::* - Automotive IoT")
output.append("- AWS::BillingConductor::* - Cost management")
output.append("")
output.append("### Low Priority (Niche Services)")
output.append("- AWS::EVS::* - VMware migration")
output.append("- AWS::ODB::* - Oracle database")
output.append("- AWS::PCS::* - Parallel computing")
output.append("")

# Write output
with open('code/.automation/to-test-stack.md', 'w') as f:
    f.write('\n'.join(output))

print(f"Generated to-test-stack.md with {len(matches)} resources across {len(resources_by_service)} services")
