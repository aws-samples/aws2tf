---
inclusion: always
---
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

### 2. Check aws_not_implemented.py Status
- Open `code/fixtf_aws_resources/aws_not_implemented.py`
- Search for the resource type
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

**Finding example code:**
1. Check `code/.automation/terraform-provider-aws/website/docs/r/<resource>.html.markdown` for official examples
2. Use the simplest example that creates a functional resource
3. Include only essential supporting resources (e.g., VPC for subnet testing)
4. Add `provider.tf` with AWS provider configuration
5. Add `outputs.tf` to capture the resource ID

**Required files:**
- `main.tf` - Resource definitions
- `provider.tf` - AWS provider configuration
- `outputs.tf` - Output the resource ID for testing

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
./aws2tf.py -t <resource_type>
```

Example: `./aws2tf.py -t aws_vpc`

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
./aws2tf.py -t <resource_type> -i <actual_resource_id>
```

Example: `./aws2tf.py -t aws_vpc -i vpc-09d8b4321d497f01b`

**Expected behavior:**
- Tool should import only the specified resource
- Generate Terraform configuration
- Create import statement

**On failure:**
- Review error messages
- Check if the ID format matches documentation
- Make 2-3 fix attempts
- Document failure and proceed to cleanup

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
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
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
./aws2tf.py -t aws_vpc

# Step 11: Test specific import
./aws2tf.py -t aws_vpc -i $VPC_ID

# Step 12: Verify generated files
ls -la generated/tf-*/aws_vpc__*.tf

# Step 13: Cleanup
cd code/.automation/test_aws_vpc
terraform destroy -auto-approve
terraform state list  # Should be empty

# Step 14: Document results
cd ..
# Create test-results.md or test-failed.md as appropriate
```

## Troubleshooting Common Issues

### Issue: Resource not in aws_dict.py
**Solution:** Add the resource to `aws_dict.py` first using the pattern from `new-capability.md`

### Issue: Composite ID format
**Solution:** Document in test-failed.md - these require special handling in the codebase

### Issue: Terraform validation fails
**Solution:** Review the example in the Terraform docs, ensure all required arguments are provided

### Issue: aws2tf.py crashes
**Solution:** Check `aws2tf.log`, verify the handler file exists (`code/fixtf_aws_resources/fixtf_<service>.py`)

### Issue: Import generates incorrect Terraform
**Solution:** Review the handler's `get_<resource>_data()` method, ensure all attributes are captured correctly







