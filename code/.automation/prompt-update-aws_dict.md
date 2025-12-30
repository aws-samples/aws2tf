# Prompt: Update aws_dict.py with Latest Terraform AWS Resources

## Objective
Update `code/fixtf_aws_resources/aws_dict.py` to include all AWS resources from the latest Terraform AWS provider, ensuring 100% coverage with proper boto3 API mappings.

## Prerequisites
- Access to `code/.automation/gettfdocs.sh` script
- AWS boto3 documentation access
- Terraform provider documentation access

## Step-by-Step Process

### Step 1: Get Latest Terraform Provider Documentation
```bash
cd code/.automation
bash gettfdocs.sh
```
This clones the terraform-provider-aws repository into `code/.automation/terraform-provider-aws/`

### Step 2: Extract Master Resource List
```bash
cd terraform-provider-aws/website/docs/r
grep 'resource "aws_' *.markdown | cut -f2 -d'"' | sort -u > ../../../master-aws-resource-list.md
```
This creates a master list of all AWS Terraform resources from the official documentation.

### Step 3: Identify Missing Resources
Create a Python script to compare the master list with existing `aws_dict.py`:

```python
import re

# Read master list
with open('code/.automation/master-aws-resource-list.md', 'r') as f:
    master_resources = set(line.strip() for line in f if line.strip())

# Read existing aws_dict.py
with open('code/fixtf_aws_resources/aws_dict.py', 'r') as f:
    existing_resources = set(re.findall(r'^(aws_[a-z_0-9]+)\s*=\s*\{', f.read(), re.MULTILINE))

# Find missing
missing_resources = sorted(master_resources - existing_resources)

# Save to file
with open('code/.automation/resources-not-in-dict.md', 'w') as f:
    f.write(f"# Missing Resources: {len(missing_resources)}\n\n")
    for i, resource in enumerate(missing_resources, 1):
        f.write(f"{i}. {resource}\n")

print(f"Found {len(missing_resources)} missing resources")
```

### Step 4: Research Each Missing Resource
For EACH missing resource, you must determine:

1. **Terraform resource name**: e.g., `aws_vpc`
2. **Boto3 client name (clfn)**: e.g., `ec2`
3. **Boto3 API method (descfn)**: e.g., `describe_vpcs`
4. **Response top-level key (topkey)**: e.g., `Vpcs`
5. **Resource identifier key (key)**: e.g., `VpcId`
6. **Filter ID (filterid)**: e.g., `VpcId`

#### Research Process:
- Use AWS boto3 documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/
- Search for the service API operations
- Look for `describe_*` or `list_*` methods
- Examine the response structure to identify keys

#### Example Research:
For `aws_vpc`:
- Terraform docs: https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/vpc
- AWS Service: EC2
- Boto3 client: `ec2`
- Boto3 method: `describe_vpcs`
- Response structure:
  ```json
  {
    "Vpcs": [
      {
        "VpcId": "vpc-12345",
        ...
      }
    ]
  }
  ```
- Entry:
  ```python
  aws_vpc = {
      "clfn":     "ec2",
      "descfn":   "describe_vpcs",
      "topkey":   "Vpcs",
      "key":      "VpcId",
      "filterid": "VpcId"
  }
  ```

### Step 5: Create Extended Dictionary
Create a Python script to build the extended dictionary:

```python
#!/usr/bin/env python3
import re

# Dictionary of new resources with boto3 mappings
new_resources = {
    'aws_resource_name': {
        "clfn": "service-name",
        "descfn": "list_or_describe_method",
        "topkey": "TopLevelKey",
        "key": "ResourceIdKey",
        "filterid": "FilterParameter"
    },
    # ... add all missing resources
}

# Read original aws_dict.py
with open('code/fixtf_aws_resources/aws_dict.py', 'r') as f:
    original_content = f.read()

# Extract and deduplicate original resources
pattern = r'^(aws_[a-z_0-9]+)\s*=\s*\{([^}]+)\}'
original_matches = re.findall(pattern, original_content, re.MULTILINE | re.DOTALL)

seen = set()
unique_original = []
for resource_name, resource_body in original_matches:
    if resource_name not in seen:
        seen.add(resource_name)
        unique_original.append((resource_name, resource_body))

# Create extended dictionary
with open('code/.automation/aws_dict_extended.py', 'w') as f:
    f.write("# Extended aws_dict.py\n")
    f.write(f"# Total: {len(unique_original) + len(new_resources)} unique resources\n\n")
    
    # Write deduplicated original
    for resource_name, resource_body in unique_original:
        f.write(f"{resource_name} = {{{resource_body}}}\n\n")
    
    # Write new resources
    f.write("# NEW RESOURCES\n\n")
    for resource_name, details in sorted(new_resources.items()):
        f.write(f"{resource_name} = {{\n")
        f.write(f'\t"clfn":\t\t"{details["clfn"]}",\n')
        f.write(f'\t"descfn":\t"{details["descfn"]}",\n')
        f.write(f'\t"topkey":\t"{details["topkey"]}",\n')
        f.write(f'\t"key":\t\t"{details["key"]}",\n')
        f.write(f'\t"filterid":\t"{details["filterid"]}"\n')
        f.write("}\n\n")
```

### Step 6: Verify Coverage
```python
import re

with open('code/.automation/aws_dict_extended.py', 'r') as f:
    extended = set(re.findall(r'^(aws_[a-z_0-9]+)\s*=\s*\{', f.read(), re.MULTILINE))

with open('code/.automation/master-aws-resource-list.md', 'r') as f:
    master = set(line.strip() for line in f if line.strip())

coverage = len(extended & master) / len(master) * 100
print(f"Coverage: {coverage:.1f}%")
print(f"Missing: {len(master - extended)} resources")
```

### Step 7: Create Added Resources List
```python
import re

with open('code/.automation/aws_dict_extended.py', 'r') as f:
    extended = set(re.findall(r'^(aws_[a-z_0-9]+)\s*=\s*\{', f.read(), re.MULTILINE))

with open('code/fixtf_aws_resources/aws_dict.py', 'r') as f:
    original = set(re.findall(r'^(aws_[a-z_0-9]+)\s*=\s*\{', f.read(), re.MULTILINE))

new_resources = sorted(extended - original)

with open('code/.automation/added-resources.md', 'w') as f:
    for resource in new_resources:
        f.write(f'{resource}\n')
```

## Important Notes

### Resource Definition Format
Each resource MUST follow this exact format:
```python
aws_resource_name = {
	"clfn":		"boto3-client-name",
	"descfn":	"boto3_api_method",
	"topkey":	"ResponseTopLevelKey",
	"key":		"ResourceIdentifierKey",
	"filterid":	"FilterParameterName"
}
```

### Common Boto3 Client Names
- EC2 resources: `ec2`
- VPC resources: `ec2`
- S3 resources: `s3`
- Lambda resources: `lambda`
- RDS resources: `rds`
- IAM resources: `iam`
- ECS resources: `ecs`
- EKS resources: `eks`
- API Gateway: `apigateway`
- API Gateway V2: `apigatewayv2`
- CloudWatch Logs: `logs`
- CloudWatch: `cloudwatch`
- Step Functions: `stepfunctions`
- DynamoDB: `dynamodb`
- Kinesis: `kinesis`
- SNS: `sns`
- SQS: `sqs`
- Route53: `route53`
- ELB v2: `elbv2`

### Common API Method Patterns
- List operations: `list_*` (e.g., `list_functions`, `list_buckets`)
- Describe operations: `describe_*` (e.g., `describe_vpcs`, `describe_instances`)
- Get operations: `get_*` (e.g., `get_policy`, `get_bucket_policy`)

### Handling Duplicates
- The original `aws_dict.py` may contain duplicates
- Always deduplicate by keeping the FIRST occurrence
- Use this pattern:
  ```python
  seen = set()
  unique = []
  for resource_name, resource_body in matches:
      if resource_name not in seen:
          seen.add(resource_name)
          unique.append((resource_name, resource_body))
  ```

### Validation Steps
1. **Syntax check**: `python3 -m py_compile code/.automation/aws_dict_extended.py`
2. **Import check**: `python3 -c "import sys; sys.path.insert(0, 'code/.automation'); import aws_dict_extended"`
3. **Duplicate check**: Count occurrences of each resource name
4. **Coverage check**: Compare against master list
5. **Specific resource check**: Verify critical resources like `aws_s3vectors_index`

## Common Issues and Solutions

### Issue 1: Duplicates in Output
**Cause**: Resources added multiple times or original file has duplicates  
**Solution**: Deduplicate both original and new resources before combining

### Issue 2: Syntax Errors
**Cause**: Dictionary not properly closed or indentation issues  
**Solution**: Ensure dictionary has matching braces and proper Python indentation

### Issue 3: Missing Resources
**Cause**: Regex not matching all resources or incomplete research  
**Solution**: Verify regex patterns and systematically research each missing resource

### Issue 4: Import Errors
**Cause**: Dictionary references variables before they're defined  
**Solution**: Ensure all resource definitions come before any dictionary that references them

## Final Checklist

- [ ] Ran `gettfdocs.sh` to get latest Terraform docs
- [ ] Created `master-aws-resource-list.md` with all resources
- [ ] Identified all missing resources
- [ ] Researched boto3 API for each missing resource
- [ ] Created extended dictionary with all resources
- [ ] Deduplicated all resources (original + new)
- [ ] Verified 100% coverage of master list
- [ ] Verified no duplicates exist
- [ ] Verified file is valid Python
- [ ] Verified specific resources (e.g., aws_s3vectors_index)
- [ ] Created `added-resources.md` with list of new resources

## Expected Output Files

1. `code/.automation/master-aws-resource-list.md` - All Terraform AWS resources
2. `code/.automation/resources-not-in-dict.md` - Resources missing from aws_dict.py
3. `code/.automation/aws_dict_extended.py` - Extended dictionary with 100% coverage
4. `code/.automation/added-resources.md` - Simple list of new resources added

## Success Criteria

- ✅ 100% coverage of Terraform AWS provider resources
- ✅ No duplicate resource definitions
- ✅ Valid Python syntax
- ✅ All original resources preserved
- ✅ Each new resource has proper boto3 API mappings
- ✅ File imports successfully in Python
