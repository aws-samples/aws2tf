---
inclusion: always
---
---
inclusion: always
---

# New Resource Testing Procedure

This document defines the testing procedure for new AWS resource types in the aws2tf tool.

## Prerequisites

Before testing a new resource type (e.g., `aws_vpc`):
- Verify the resource exists in `code/fixtf_aws_resources/aws_dict.py` - **STOP if not found**
- Check if the resource is commented out in `code/fixtf_aws_resources/aws_not_implemented.py` - if so, uncomment it

## Testing Steps

### 1. Create Test Environment

Create a test directory: `code/.automation/test_<resource_type>`

Example: `code/.automation/test_aws_vpc`

### 2. Create Terraform Test Configuration

In the test directory, create working Terraform files that demonstrate the resource:

**Finding example code:**
- Check `code/.automation/terraform-provider-aws/website/docs/r/<resource>.html.markdown` for examples
- Use AWS Terraform provider documentation
- Include supporting resources if needed for a complete working example

**Validation:**
```bash
cd code/.automation/test_<resource_type>
terraform init
terraform validate
```
Fix any validation errors and re-run until successful.

### 3. Test Terraform Deployment

```bash
terraform plan
```
Review the plan. If errors occur, fix and re-run.

```bash
terraform apply -auto-approve
```
Verify successful deployment. Note the resource ID from the output.

### 4. Test aws2tf Type-Level Import

Run the type-level test:
```bash
./aws2tf.py -t <resource_type>
```

Example: `./aws2tf.py -t aws_vpc`

**If this fails:** Make 2-3 attempts to fix the issue, then document failure and proceed to cleanup.

### 5. Test aws2tf Resource-Specific Import

**Finding the resource ID format:**
Look in the Terraform documentation markdown file for the import block:

```hcl
import {
  to = aws_vpc.test_vpc
  id = "vpc-a01106c2"
}
```

The `id` value shows the expected format (e.g., `vpc-*` for VPCs).

**Get the actual resource ID:**
- From `terraform apply` output, OR
- Run `terraform state show <resource_address>` in the test directory

**Run the specific import test:**
```bash
./aws2tf.py -t <resource_type> -i <actual_resource_id>
```

Example: `./aws2tf.py -t aws_vpc -i vpc-09d8b4321d497f01b`

**If this fails:** Make 2-3 attempts to fix the issue, then document failure and proceed to cleanup.

### 6. Cleanup

Always destroy test resources:
```bash
cd code/.automation/test_<resource_type>
terraform destroy -auto-approve
```

### 7. Document Results

**On Success:**
Create `code/.automation/test_<resource_type>/test-results.md` documenting:
- Test date and time
- Commands executed
- Test outcomes (pass/fail for each step)
- Any issues encountered and how they were resolved

**On Failure:**
Create `code/.automation/test_<resource_type>/test-failed.md` documenting:
- What failed and why
- Error messages
- Attempts made to fix
- Recommendation for next steps

If the resource cannot be supported, re-comment the entry in `code/fixtf_aws_resources/aws_not_implemented.py`.

## Important Constraints

- **Do not loop extensively** - Make 2-3 fix attempts maximum per failure
- **Always run terraform destroy** - Even on test failure, clean up resources
- **Document everything** - Create test-results.md or test-failed.md
- **Stop early if blocked** - If aws_dict.py doesn't have the resource, stop immediately

## Example: Testing aws_vpc

```bash
# 1. Check prerequisites
grep "aws_vpc" code/fixtf_aws_resources/aws_dict.py
grep "aws_vpc" code/fixtf_aws_resources/aws_not_implemented.py

# 2. Create test directory
mkdir -p code/.automation/test_aws_vpc
cd code/.automation/test_aws_vpc

# 3. Create main.tf with VPC example
# (create terraform configuration)

# 4. Validate and deploy
terraform init
terraform validate
terraform plan
terraform apply -auto-approve

# 5. Note the VPC ID from output (e.g., vpc-09d8b4321d497f01b)

# 6. Test type-level import
cd ../../..
./aws2tf.py -t aws_vpc

# 7. Test specific import
./aws2tf.py -t aws_vpc -i vpc-09d8b4321d497f01b

# 8. Cleanup
cd code/.automation/test_aws_vpc
terraform destroy -auto-approve

# 9. Document in test-results.md or test-failed.md
```







