---
inclusion: always
---

# New Resource Testing Procedure

This document defines the testing procedure for new AWS resource types in the aws2tf tool. Follow these steps sequentially when adding support for a new resource type.

## Prerequisites Check

Before testing a new resource type (e.g., `aws_vpc`), verify these conditions in order:

### 1. Check aws_dict.py Entry
- Open `code/fixtf_aws_resources/aws_dict.py`
- Search for the resource type (e.g., `"aws_vpc"`)
- **STOP IMMEDIATELY** if the resource is not found - it must be added first
- If found, note the boto3 client and API method defined

### 1.5. Verify Correct Key Field in aws_dict.py

The `key` field in aws_dict.py must match what Terraform expects for import:

**Check the boto3 API response:**
```bash
python3 -c "import boto3; client = boto3.client('<service>', region_name='<region>'); response = client.<list_method>(); print(response)"
```

**Determine the correct key:**
- Check the Terraform docs import section to see what ID format is expected
- If Terraform imports by ARN → use the ARN field (e.g., `vectorBucketArn`)
- If Terraform imports by ID → use the ID field (e.g., `vpcId`)
- If Terraform imports by name → use the name field

**Example:**
```python
# WRONG - uses name when Terraform expects ARN
aws_s3vectors_vector_bucket = {
    "key": "vectorBucketName",  # ❌
}

# CORRECT - uses ARN for import
aws_s3vectors_vector_bucket = {
    "key": "vectorBucketArn",  # ✓
}
```

### 2. Check aws_not_implemented.py Status
- Open `code/fixtf_aws_resources/aws_not_implemented.py`
- Search for the resource type
- **Note the TODO version** (e.g., `### TODO 6.27.0`) - you'll need this for provider.tf
- If found and commented out, uncomment it to enable testing
- If found and not commented, the resource is already enabled
- **STOP** if the resource cannot be found in either file

### 3. Verify Import ID Format
- Navigate to `code/.automation/terraform-provider-aws/website/docs/r/<resource>.html.markdown`
- Locate the import block example
- Check if the `id` field contains composite identifiers with `,` or `/` separators

**Example of simple ID (supported):**
```hcl
import {
  to = aws_vpc.test_vpc
  id = "vpc-a01106c2"
}
```

**Example of composite ID (NOT supported):**
```hcl
import {
  to = aws_route_table_association.example
  id = "subnet-12345,rtb-67890"
}
```

**If composite ID detected:**
- **STOP testing**
- Create `code/.automation/test_<resource_type>/test-failed.md`
- Document that the resource uses composite IDs and requires special handling
- Note the exact ID format from the documentation

## Testing Steps

Execute these steps only if all prerequisites are met:

### Step 1: Create Test Environment

Create the test directory structure:
```bash
mkdir -p code/.automation/test_<resource_type>
cd code/.automation/test_<resource_type>
```

Example: `mkdir -p code/.automation/test_aws_vpc`

### Step 2: Create Terraform Configuration

Create a minimal but complete Terraform configuration that demonstrates the resource.

**Determine AWS Provider Version:**
1. Check the TODO comment in `code/fixtf_aws_resources/aws_not_implemented.py`
2. If marked `### TODO 6.27.0`, use `version = "~> 6.27"`
3. If marked `### TODO 5.x.x`, use `version = "~> 5.0"`
4. For older resources without TODO comments, use `version = "~> 5.0"`

**Finding example code:**
1. Check `code/.automation/terraform-provider-aws/website/docs/r/<resource>.html.markdown` for official examples
2. Use the simplest example that creates a functional resource
3. Include only essential supporting resources (e.g., VPC for subnet testing)
4. Add `provider.tf` with AWS provider configuration
5. Add `outputs.tf` to capture the resource ID

**Required files:**
- `main.tf` - Resource definitions
- `provider.tf` - AWS provider configuration (with correct version)
- `outputs.tf` - Output the resource ID for testing

**Example provider.tf for new resources (6.27.0+):**
```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.27"  # Match version from aws_not_implemented.py
    }
  }
}

provider "aws" {
  region = "us-east-1"  # Remember this region for aws2tf.py -r flag
}
```

**Validation:**
```bash
terraform init
terraform validate
```

**Fix validation errors** - Iterate until `terraform validate` succeeds (maximum 3 attempts).

### Step 3: Deploy Test Resources

Execute deployment:
```bash
terraform plan
```

Review the plan carefully. Fix any errors and re-run.

```bash
terraform apply -auto-approve
```

**Capture the resource ID** from the output or state:
```bash
terraform output <resource_id_output_name>
# OR
terraform state show <resource_address> | grep "^id"
```

### Step 4: Test Type-Level Import

Test aws2tf's ability to discover and import all resources of this type:

```bash
cd <workspace_root>
./aws2tf.py -r <region> -t <resource_type>
```

**CRITICAL: Region Consistency**
- **ALWAYS use the `-r` flag** to specify the same region as in your `provider.tf`
- Example: If `provider.tf` has `region = "us-east-1"`, use `./aws2tf.py -r us-east-1 -t <resource_type>`
- Without `-r`, aws2tf uses your default AWS CLI region, which may differ from where you created the test resource

Example: `./aws2tf.py -r us-east-1 -t aws_vpc`

**Expected behavior:**
- Tool should discover the test resource
- Generate Terraform files in `generated/` directory
- Create import statements

**On failure:**
- Review error messages in console output
- Check `aws2tf.log` for detailed errors
- Make 2-3 fix attempts in the relevant handler file (`code/fixtf_aws_resources/fixtf_<service>.py`)
- If still failing, document and proceed to cleanup

### Step 5: Test Resource-Specific Import

Test aws2tf's ability to import a specific resource by ID:

```bash
./aws2tf.py -r <region> -t <resource_type> -i <actual_resource_id>
```

Example: `./aws2tf.py -r us-east-1 -t aws_vpc -i vpc-09d8b4321d497f01b`

**Expected behavior:**
- Tool should import only the specified resource
- Generate Terraform configuration
- Create import statement

**Note on plan changes:**
- It's normal for the initial import to show changes for fields with defaults (e.g., `+ force_destroy = false`)
- The `lifecycle.ignore_changes` block prevents these from showing in future plans
- A plan showing "1 to import, 0 to add, 1 to change" is acceptable if:
  - The change is only adding a default value
  - A lifecycle block is present to ignore future changes
  - After the first `terraform apply`, subsequent plans should show no changes

**On failure:**
- Review error messages
- Check if the ID format matches documentation
- Make 2-3 fix attempts
- Document failure and proceed to cleanup

### Step 5.5: Implement Handler (if needed)

If the resource requires custom handling, create or update `code/fixtf_aws_resources/fixtf_<service>.py`:

**A. Skip computed/read-only fields:**
```python
def aws_<resource>(t1, tt1, tt2, flag1, flag2):
    skip = 0
    
    # Skip fields that AWS populates automatically
    if tt1 in ["creation_time", "arn", "id", "tags_all"]:
        skip = 1
    
    return skip, t1, flag1, flag2
```

**B. Handle fields with defaults that cause plan drift:**
```python
# Set explicit value instead of skipping null
if tt1 == "force_destroy" and tt2 == "null":
    t1 = tt1 + " = false\n"
```

**C. Add lifecycle ignore_changes for fields that drift:**
```python
# Add lifecycle block after a required field (NOT at closing brace)
elif tt1 == "vector_bucket_name":  # Use a required field
    t1 = t1 + "\n lifecycle {\n   ignore_changes = [force_destroy]\n}\n"
```

**IMPORTANT:** Append lifecycle blocks to specific field lines, NOT to closing braces. Replacing `}` will insert the block in wrong places (inside nested blocks).

**D. Skip entire blocks with computed defaults:**
```python
# Skip blocks like encryption_configuration that have computed defaults
elif tt1 == "encryption_configuration" or context.lbc > 0:
    if tt2 == "[]":
        skip = 1
    if "[" in t1:
        context.lbc = context.lbc + 1
    if "]" in t1:
        context.lbc = context.lbc - 1
    
    if context.lbc > 0:
        skip = 1
    if context.lbc == 0 and "]" in t1.strip():
        skip = 1
```

### Step 5.6: Register Handler Module (if new service)

If you created a new service handler file, register it in `code/fixtf.py`:

**1. Add import (alphabetically):**
```python
from fixtf_aws_resources import fixtf_<service>
```

**2. Add to registry dictionary (alphabetically):**
```python
'fixtf_<service>': fixtf_<service>,
```

### Step 5.7: Implement Get Function (if new service)

If you created a new service, implement `code/get_aws_resources/aws_<service>.py`:

```python
def get_aws_<resource>(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn,config=config)
        
        if id is None:
            # List all resources
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            for j in response:
                common.write_import(type,j[key],None)
        else:
            # Get specific resource
            response = client.get_<resource>(<param>=id)
            # Check response structure - may have singular key
            j = response.get('<singular_key>', response)
            common.write_import(type,j[key],None)
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
    return True
```

**Note:** List operations return `{topkey: [items]}`, but get operations may return `{singular_key: item}` or just `item`. Check the boto3 API response structure.

**IMPORTANT: Register the get function in common.py**

After creating the get function file, you must register it in two places in `code/common.py`:

**1. Add the import (alphabetically):**
```python
from get_aws_resources import aws_<service>
```

Example location (find the s3 imports section):
```python
from get_aws_resources import aws_s3
from get_aws_resources import aws_s3control
from get_aws_resources import aws_s3tables
from get_aws_resources import aws_s3vectors  # Add new service here
```

**2. Add to AWS_RESOURCE_MODULES dictionary (alphabetically):**

Find the `AWS_RESOURCE_MODULES` dictionary (around line 687) and add your service:
```python
AWS_RESOURCE_MODULES = {
    ...
    's3': aws_s3,
    's3control': aws_s3control,
    's3tables': aws_s3tables,
    's3vectors': aws_s3vectors,  # Add new service here
    'sagemaker': aws_sagemaker,
    ...
}
```

**Note:** The key should match the `clfn` value from aws_dict.py (e.g., if `"clfn": "s3vectors"`, use `'s3vectors'` as the key).

### Step 6: Cleanup Test Resources

**ALWAYS destroy test resources**, even if tests failed:

```bash
cd code/.automation/test_<resource_type>
terraform destroy -auto-approve
```

Verify all resources are destroyed:
```bash
terraform state list
# Should return empty
```

**Clean up Terraform files:**
```bash
rm -rf .terraform .terraform.lock.hcl
```

This removes the Terraform state directory and lock file, keeping the test directory clean.

### Step 7: Document Test Results

Create documentation in the test directory:

**On Success** - Create `test-results.md`:
```markdown
# Test Results: <resource_type>

**Date:** YYYY-MM-DD HH:MM:SS
**Status:** PASSED

## Test Summary
- Prerequisites: ✓
- Terraform validation: ✓
- Resource deployment: ✓
- Type-level import: ✓
- Specific import: ✓
- Cleanup: ✓

## Resource Details
- Resource Type: <resource_type>
- Test Resource ID: <id>
- AWS Region: <region>

## Commands Executed
1. terraform init
2. terraform validate
3. terraform apply -auto-approve
4. ./aws2tf.py -t <resource_type>
5. ./aws2tf.py -t <resource_type> -i <id>
6. terraform destroy -auto-approve

## Notes
<Any observations or issues resolved>
```

**On Failure** - Create `test-failed.md`:
```markdown
# Test Failure: <resource_type>

**Date:** YYYY-MM-DD HH:MM:SS
**Status:** FAILED

## Failure Point
<Which step failed>

## Error Details
<Error messages and stack traces>

## Root Cause
<Analysis of why it failed>

## Fix Attempts
1. <First attempt and result>
2. <Second attempt and result>
3. <Third attempt and result>

## Recommendation
<Next steps or whether resource should remain unsupported>

## Composite ID Detection
<If applicable, note the composite ID format>
```

**If resource cannot be supported:**
- Re-comment the entry in `code/fixtf_aws_resources/aws_not_implemented.py`
- Add a comment explaining why (e.g., "# Composite ID format not supported")

## Constraints and Best Practices

### Iteration Limits
- **Maximum 3 fix attempts** per failure point
- Do not loop indefinitely trying to fix issues
- Document failures and move on

### Resource Cleanup
- **ALWAYS run `terraform destroy`** regardless of test outcome
- Verify cleanup with `terraform state list`
- Check AWS console if uncertain

### Documentation Requirements
- **ALWAYS create** either `test-results.md` or `test-failed.md`
- Include timestamps, commands, and outcomes
- Provide enough detail for future debugging

### Early Exit Conditions
- Missing entry in `aws_dict.py` → Stop immediately
- Composite ID format detected → Stop and document
- 3 failed fix attempts → Stop and document

## Complete Example: Testing aws_vpc

```bash
# Step 1: Check prerequisites
grep '"aws_vpc"' code/fixtf_aws_resources/aws_dict.py
# Expected: Entry exists with ec2 client and describe_vpcs method

grep 'aws_vpc' code/fixtf_aws_resources/aws_not_implemented.py
# If found commented, uncomment it

# Step 2: Check import format
cat code/.automation/terraform-provider-aws/website/docs/r/vpc.html.markdown | grep -A 3 "import {"
# Verify ID format is simple (no commas or slashes)

# Step 3: Create test directory
mkdir -p code/.automation/test_aws_vpc
cd code/.automation/test_aws_vpc

# Step 4: Create main.tf
cat > main.tf << 'EOF'
resource "aws_vpc" "test" {
  cidr_block = "10.0.0.0/16"
  
  tags = {
    Name = "aws2tf-test-vpc"
    Purpose = "Testing"
  }
}
EOF

# Step 5: Create provider.tf
cat > provider.tf << 'EOF'
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"  # Use ~> 6.27 for newer resources
    }
  }
}

provider "aws" {
  region = "us-east-1"  # Remember to use -r us-east-1 with aws2tf.py
}
EOF

# Step 6: Create outputs.tf
cat > outputs.tf << 'EOF'
output "vpc_id" {
  value = aws_vpc.test.id
}
EOF

# Step 7: Initialize and validate
terraform init
terraform validate

# Step 8: Deploy
terraform plan
terraform apply -auto-approve

# Step 9: Capture resource ID
VPC_ID=$(terraform output -raw vpc_id)
echo "Test VPC ID: $VPC_ID"

# Step 10: Test type-level import
cd ../../..
./aws2tf.py -r us-east-1 -t aws_vpc  # Always use -r flag with region

# Step 11: Test specific import
./aws2tf.py -r us-east-1 -t aws_vpc -i $VPC_ID

# Step 12: Verify generated files
ls -la generated/tf-*/aws_vpc__*.tf

# Step 13: Cleanup
cd code/.automation/test_aws_vpc
terraform destroy -auto-approve
terraform state list  # Should be empty
rm -rf .terraform .terraform.lock.hcl  # Clean up Terraform files

# Step 14: Document results
cd ..
# Create test-results.md or test-failed.md as appropriate
```

## Troubleshooting Common Issues

### Issue: Resource not in aws_dict.py
**Solution:** Add the resource to `aws_dict.py` first using the pattern from `new-capability.md`

### Issue: Wrong key field in aws_dict.py
**Symptom:** Import files are generated but with wrong IDs, or Terraform import fails
**Solution:** 
- Check the boto3 API response structure
- Verify the Terraform import documentation for expected ID format
- Update the `key` field in aws_dict.py to match (e.g., use ARN field instead of name field)

### Issue: Composite ID format
**Solution:** Document in test-failed.md - these require special handling in the codebase

### Issue: Terraform validation fails
**Solution:** Review the example in the Terraform docs, ensure all required arguments are provided

### Issue: Wrong AWS provider version
**Symptom:** `Error: Invalid resource type` or resource not found
**Solution:** 
- Check the TODO comment in `aws_not_implemented.py`
- Update `provider.tf` to use the correct version (e.g., `~> 6.27` for new resources)
- Run `terraform init -upgrade`

### Issue: aws2tf.py crashes
**Solution:** Check `aws2tf.log`, verify the handler file exists (`code/fixtf_aws_resources/fixtf_<service>.py`)

### Issue: Import generates incorrect Terraform
**Solution:** Review the handler's `get_<resource>_data()` method, ensure all attributes are captured correctly

### Issue: KeyError when testing specific resource import
**Symptom:** `KeyError('prefix')` or similar when using `-i` flag
**Cause:** The get function needs different handling for list vs. get operations
**Solution:** 
- Check the boto3 API response structure for the get operation
- Update the get function to handle the singular response key
- Example: `j = response.get('vectorBucket', response)` instead of `j = response`

### Issue: Module not found error
**Symptom:** `Module not found in registry for callfn=fixtf_<service>`
**Solution:**
- Verify the handler file exists at `code/fixtf_aws_resources/fixtf_<service>.py`
- Check that it's imported in `code/fixtf.py`
- Check that it's registered in the module registry dictionary in `code/fixtf.py`

### Issue: Plan shows unexpected changes after import
**Symptom:** Terraform plan shows changes like `+ force_destroy = false`
**Solution:** This is expected for initial imports with default values
- Ensure a `lifecycle.ignore_changes` block is present in the handler
- After the first `terraform apply`, subsequent plans should show no changes
- If changes persist, the lifecycle block may be in the wrong location (should be appended to a field line, not a closing brace)







