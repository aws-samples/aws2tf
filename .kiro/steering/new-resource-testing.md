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

### 1.5. Verify boto3 API Method Names

After checking aws_dict.py, verify the actual boto3 API method exists and matches:

```bash
python3 -c "import boto3; client = boto3.client('<service>', region_name='<region>'); print([m for m in dir(client) if '<keyword>' in m.lower()])"
```

**Example for s3vectors indexes:**
```bash
python3 -c "import boto3; client = boto3.client('s3vectors', region_name='us-east-1'); print([m for m in dir(client) if 'index' in m.lower()])"
# Output: ['create_index', 'delete_index', 'get_index', 'list_indexes']
```

**If the method name in aws_dict.py doesn't match the actual boto3 method:**
- Update the `descfn` field in aws_dict.py before proceeding
- Common mistake: `list_vector_indexes` vs `list_indexes`

### 1.5b. Check if List Operation is Pageable

Not all list operations support pagination. Check before implementing:

```bash
python3 -c "import boto3; client = boto3.client('<service>', region_name='<region>'); print(client.can_paginate('list_<resources>'))"
```

**Example:**
```bash
python3 -c "import boto3; client = boto3.client('workspaces-web', region_name='us-east-1'); print(client.can_paginate('list_portals'))"
# Output: False
```

If `False`, use direct API call instead of paginator in the get function (see Step 5.7).

### 1.6. Verify Correct Key Field in aws_dict.py

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

### 1.7. Verify Terraform Resource Attributes

Before writing test configuration, verify what attributes the resource actually exports:

```bash
grep -A 10 "## Attribute Reference" code/.automation/terraform-provider-aws/website/docs/r/<resource>.html.markdown
```

**Common mistakes:**
- Assuming `.arn` exists when the actual attribute is `.vector_bucket_arn`
- Assuming `.id` exists when the resource exports no additional attributes
- Using intuitive names instead of checking documentation

**Example:**
```hcl
# WRONG - assumes generic attribute name
vector_bucket_arn = aws_s3vectors_vector_bucket.test.arn  # ❌

# CORRECT - uses actual exported attribute
vector_bucket_arn = aws_s3vectors_vector_bucket.test.vector_bucket_arn  # ✓
```

**For resources with no exported attributes:**
- Documentation will say "This resource exports no additional attributes"
- Don't try to output `.id` - it won't exist
- Use the parent resource's identifier or input arguments for testing

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

**For resources with dependencies:**
- Include only the minimal required parent resources
- Use the simplest configuration for parent resources
- Example: Testing `aws_s3vectors_index` requires `aws_s3vectors_vector_bucket`
- Example: Testing `aws_subnet` requires `aws_vpc`

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

**Fix validation errors** - Iterate until `terraform validate` succeeds (maximum 4 attempts).

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
- Make up to 4 fix attempts in the relevant handler file (`code/fixtf_aws_resources/fixtf_<service>.py`)
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
- Make up to 4 fix attempts
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

**E. Handle JSON normalization drift (for policy resources):**
```python
# For resources with JSON fields (policy, assume_role_policy, etc.)
# JSON key ordering causes perpetual drift - ignore it
elif tt1 == "vector_bucket_arn":  # Use the parent resource identifier field
    t1 = t1 + "\n lifecycle {\n   ignore_changes = [policy]\n}\n"
```

**Note:** Policy resources (like `aws_s3_bucket_policy`, `aws_iam_role_policy`, `aws_s3vectors_vector_bucket_policy`) often have JSON normalization issues where Terraform and AWS return different key ordering. Always add lifecycle blocks to ignore the policy field.

### Step 5.6: Register Handler Module (if new service)

**IMPORTANT: Check if handler file already exists**

Before creating a new handler file, check if it already exists:
```bash
ls code/fixtf_aws_resources/fixtf_<service>.py
```

If the file exists but you're getting "Module not found in registry" errors:
- The file exists but isn't registered in `code/fixtf.py`
- Skip file creation and go directly to registration steps
- This commonly happens with newer services that have stub files

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

**For pageable list operations:**
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

**For non-pageable list operations:**

If the list operation is not pageable (check with Step 1.5b), use a direct API call:

```python
def get_aws_<resource>(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all resources - not pageable
            response = client.list_<resources>()
            for j in response[topkey]:
                common.write_import(type, j[key], None)
        else:
            # Get specific resource
            response = client.get_<resource>(<param>=id)
            j = response.get('<singular_key>', response)
            common.write_import(type, j[key], None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True
```

**Example:** `aws_workspacesweb_portal` uses non-pageable `list_portals`

**Note on API Response Structures:**
- **List operations** typically return: `{topkey: [items]}`
  - Example: `list_indexes` → `{indexes: [...]}`
- **Get operations** may return:
  - Wrapped: `{singular_key: item}` (e.g., `{index: {...}}`)
  - Direct: `item` (just the object itself)

**Always check the response structure:**
```bash
# Test list operation
python3 -c "import boto3; client = boto3.client('<service>', region_name='<region>'); response = client.<list_method>(); print(response.keys())"

# Test get operation
python3 -c "import boto3; client = boto3.client('<service>', region_name='<region>'); response = client.<get_method>(<param>='<id>'); print(response.keys())"
```

**Handle both cases in get function:**
```python
# For get operations, check for singular key
j = response.get('index', response)  # Try singular key, fallback to response
```

**For resources that require parent resource parameters:**

Some resources can only be listed within a parent resource context (e.g., indexes require a vector bucket name).

**Pattern for dependent resources:**
```python
def get_aws_<resource>(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn,config=config)
        
        if id is None:
            # First get all parent resources
            parent_paginator = client.get_paginator('list_parents')
            parents = []
            for page in parent_paginator.paginate():
                parents = parents + page['parents']
            
            # Then list children for each parent
            response = []
            for parent in parents:
                try:
                    child_paginator = client.get_paginator(descfn)
                    for page in child_paginator.paginate(parentParam=parent['parentKey']):
                        response = response + page[topkey]
                except Exception as e:
                    if context.debug: log.debug(f"Error listing for parent {parent['parentKey']}: {e}")
                    continue
            
            for j in response:
                common.write_import(type,j[key],None)
        else:
            # Get specific resource by ID/ARN
            response = client.get_<resource>(<param>=id)
            j = response.get('<singular_key>', response)
            common.write_import(type,j[key],None)
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
    return True
```

**Examples of dependent resources:**
- `aws_s3vectors_index` (requires vectorBucketName to list)
- `aws_route_table_association` (requires route table or subnet)

**Pattern for resources without list operations (policy resources):**

Some resources don't have a list operation - they can only be retrieved individually (e.g., bucket policies). For these:

```python
def get_aws_<resource>_policy(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn,config=config)
        
        if id is None:
            # First get all parent resources
            parent_paginator = client.get_paginator('list_parents')
            parents = []
            for page in parent_paginator.paginate():
                parents = parents + page['parents']
            
            # Then try to get policy for each parent
            for parent in parents:
                parent_arn = parent['parentArn']  # Use ARN as import ID
                try:
                    # Try to get the policy - will fail if it doesn't exist
                    policy_response = client.get_<resource>_policy(parentArn=parent_arn)
                    # Policy exists for this parent
                    common.write_import(type, parent_arn, None)
                except client.exceptions.NoSuch<Resource>Policy:
                    # No policy for this parent, skip it
                    if context.debug: log.debug(f"No policy for {parent_arn}")
                    continue
                except Exception as e:
                    if context.debug: log.debug(f"Error getting policy for {parent_arn}: {e}")
                    continue

        else:
            # Get specific policy by parent ARN
            response = client.get_<resource>_policy(parentArn=id)
            # Use the parent ARN as the import ID
            common.write_import(type, id, None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True
```

**Key characteristics of policy resources:**
- No list operation (e.g., no `list_bucket_policies`)
- Must iterate through parent resources and try to get each policy
- Handle `NoSuch*Policy` exceptions gracefully
- Use parent resource ARN/ID as the import identifier
- Policy may not exist for all parent resources

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

**CRITICAL: Service Name with Hyphens**

When the boto3 client name contains hyphens (e.g., `workspaces-web`), use the hyphenated name as the dictionary key:

```python
# In common.py AWS_RESOURCE_MODULES dictionary:
'workspaces-web': aws_workspaces_web,  # ✓ Correct - matches clfn from aws_dict.py

# NOT:
'workspaces_web': aws_workspaces_web,  # ❌ Wrong - won't match
```

The key must exactly match the `clfn` value from aws_dict.py.

### Step 5.8: Comprehensive Configuration Test (Optional but Recommended)

After the basic tests pass, create a more comprehensive test to verify all optional features work correctly:

**1. Update main.tf with comprehensive configuration:**
- Review the Terraform documentation for all available arguments
- Add as many optional features as practical
- Include nested blocks (if applicable)
- Add multiple tags
- Test timeout/limit settings
- Test complex data structures (lists, maps, nested blocks)

**Example for aws_workspacesweb_user_settings:**
```hcl
resource "aws_workspacesweb_user_settings" "test" {
  # Required fields
  copy_allowed     = "Enabled"
  download_allowed = "Enabled"
  paste_allowed    = "Enabled"
  print_allowed    = "Enabled"
  upload_allowed   = "Enabled"
  
  # Optional fields
  deep_link_allowed                  = "Enabled"
  disconnect_timeout_in_minutes      = 30
  idle_disconnect_timeout_in_minutes = 15
  
  # Nested blocks
  cookie_synchronization_configuration {
    allowlist {
      domain = "example.com"
      path   = "/app"
      name   = "session"
    }
    allowlist {
      domain = "test.example.com"
      path   = "/"
    }
    blocklist {
      domain = "blocked.com"
    }
  }
  
  toolbar_configuration {
    toolbar_type           = "Docked"
    visual_mode            = "Dark"
    hidden_toolbar_items   = ["Webcam", "Microphone"]
    max_display_resolution = "size1920X1080"
  }
  
  tags = {
    Name        = "comprehensive-test"
    Environment = "Test"
    Purpose     = "Testing"
  }
}
```

**2. Deploy and test:**
```bash
terraform validate
terraform apply -auto-approve
```

**3. Run both import tests again:**
```bash
cd <workspace_root>
./aws2tf.py -r <region> -t <resource_type>
./aws2tf.py -r <region> -t <resource_type> -i <resource_id>
```

**4. Verify comprehensive import:**
- Check that all nested blocks are captured
- Verify all optional fields are present
- Ensure no drift in post-import plan (0 changes)
- Review generated .tf file for completeness

**5. Document comprehensive test results:**
Add to test-results.md:
```markdown
## Comprehensive Configuration Tested
- List all optional features tested
- Note any nested blocks included
- Document any features that couldn't be tested (e.g., KMS keys requiring complex policies)
```

**When to skip this step:**
- Resource has no optional arguments
- Resource is very simple (only required fields)
- Time constraints (but document this decision)

**When to simplify the comprehensive test:**
- Skip features requiring complex dependent resources (e.g., KMS keys with service-specific policies)
- Skip features requiring additional IAM roles or complex permissions
- Focus on features that can be tested with simple configuration
- Document excluded features in test-results.md

**Benefits:**
- Confirms handler works with complex configurations
- Validates nested block handling
- Ensures no edge cases cause drift
- Provides confidence for production use

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
- Resource deployment (basic): ✓
- Type-level import (basic): ✓
- Specific import (basic): ✓
- Comprehensive configuration (optional): ✓
- Type-level import (comprehensive): ✓
- Specific import (comprehensive): ✓
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
- **Maximum 4 fix attempts per failure point** (not per test step)
- A "failure point" is a distinct issue that needs fixing
- Examples of separate failure points:
  - Terraform validation errors (e.g., wrong attribute name)
  - Resource deployment errors (e.g., invalid principal format)
  - Import errors (e.g., wrong key field in aws_dict.py)
  - Handler implementation issues (e.g., missing lifecycle block)
- Each failure point gets its own 4 attempts
- If a step has multiple distinct issues, you can fix each one (up to 4 attempts per issue)
- Example: Step 4 has both a validation error AND a deployment error = 2 failure points = 8 total attempts possible
- Do not loop indefinitely trying to fix issues
- Document failures and move on after exhausting attempts

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
- 4 failed fix attempts per failure point → Stop and document

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

## Complete Example: Testing aws_workspacesweb_portal (Non-Pageable)

This example shows handling a resource with a non-pageable list operation and existing handler file:

```bash
# Step 1: Check prerequisites
grep '"aws_workspacesweb_portal"' code/fixtf_aws_resources/aws_dict.py
# Expected: Entry exists with workspaces-web client and list_portals method

# Step 1.5b: Check if list operation is pageable
python3 -c "import boto3; client = boto3.client('workspaces-web', region_name='us-east-1'); print(client.can_paginate('list_portals'))"
# Output: False - means we need direct API call, not paginator

# Step 2: Check if handler file exists
ls code/fixtf_aws_resources/fixtf_workspaces_web.py
# File exists! Check if it's registered in fixtf.py

grep 'fixtf_workspaces_web' code/fixtf.py
# Not found - needs registration

# Step 3: Register handler in fixtf.py
# Add import: from fixtf_aws_resources import fixtf_workspaces_web
# Add to registry: 'fixtf_workspaces_web': fixtf_workspaces_web

# Step 4: Create get function for non-pageable operation
cat > code/get_aws_resources/aws_workspaces_web.py << 'EOF'
import boto3
import common
import inspect
from botocore.config import Config

def get_aws_workspacesweb_portal(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all portals - not pageable
            response = client.list_portals()
            for j in response[topkey]:
                common.write_import(type, j[key], None)
        else:
            # Get specific portal
            response = client.get_portal(portalArn=id)
            j = response.get('portal', response)
            common.write_import(type, j[key], None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True
EOF

# Step 5: Register get function in common.py
# Add import: from get_aws_resources import aws_workspaces_web
# Add to AWS_RESOURCE_MODULES: 'workspaces-web': aws_workspaces_web
# Note: Use hyphenated name to match clfn in aws_dict.py

# Step 6: Create test directory
mkdir -p code/.automation/test_aws_workspacesweb_portal
cd code/.automation/test_aws_workspacesweb_portal

# Step 7: Create Terraform files
cat > main.tf << 'EOF'
resource "aws_workspacesweb_portal" "test" {
  display_name  = "test-portal-20250101"
  instance_type = "standard.regular"

  tags = {
    Name    = "aws2tf-test-portal"
    Purpose = "Testing"
  }
}
EOF

cat > provider.tf << 'EOF'
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.27"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}
EOF

cat > outputs.tf << 'EOF'
output "portal_arn" {
  value = aws_workspacesweb_portal.test.portal_arn
}
EOF

# Step 8: Deploy
terraform init
terraform validate
terraform apply -auto-approve

# Step 9: Test imports
cd ../../..
./aws2tf.py -r us-east-1 -t aws_workspacesweb_portal
./aws2tf.py -r us-east-1 -t aws_workspacesweb_portal -i "arn:aws:workspaces-web:us-east-1:566972129213:portal/5b24f2e6-cc7b-4781-add8-c7dfcccee8c9"

# Step 10: Verify - should show 0 changes after import
# This resource needs no custom handler logic!

# Step 11: Cleanup
cd code/.automation/test_aws_workspacesweb_portal
terraform destroy -auto-approve
rm -rf .terraform .terraform.lock.hcl
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

### Issue: boto3 API method not found
**Symptom:** `KeyError('list_vector_indexes')` or similar when calling boto3
**Cause:** The method name in aws_dict.py doesn't match the actual boto3 API
**Solution:**
- List available methods: `python3 -c "import boto3; client = boto3.client('<service>'); print([m for m in dir(client) if '<keyword>' in m.lower()])"`
- Update the `descfn` field in aws_dict.py to match the actual method name
- Example: Change `list_vector_indexes` to `list_indexes`

### Issue: OperationNotPageableError
**Symptom:** `OperationNotPageableError('Operation cannot be paginated: list_<resources>')` when testing
**Cause:** Not all AWS list operations support pagination
**Solution:** 
- Use direct API call instead of paginator
- Example:
```python
# Instead of:
paginator = client.get_paginator(descfn)
for page in paginator.paginate():
    response = response + page[topkey]

# Use:
response = client.list_<resources>()
for j in response[topkey]:
    common.write_import(type, j[key], None)
```
**How to detect:** Check with `client.can_paginate('list_<resources>')` (see Step 1.5b)
**Example:** `aws_workspacesweb_portal` uses non-pageable `list_portals`

### Issue: Resource requires parent resource parameter
**Symptom:** API error like "Must specify vectorBucketName" or "Missing required parameter"
**Cause:** Some resources can only be listed within a parent resource context
**Solution:**
- Implement a get function that first lists parent resources, then iterates to list child resources
- See the "For resources that require parent resource parameters" section in Step 5.7
- Example: `list_indexes` requires `vectorBucketName`, so list all vector buckets first

### Issue: Resource name validation errors
**Symptom:** "The requested bucket name is reserved" or similar naming errors during deployment
**Solution:**
- Avoid AWS-reserved prefixes like "aws", "aws2tf", "amazon"
- Use simple, lowercase names with hyphens
- Add timestamp suffix for uniqueness: `test-resource-20250101`
- Try up to 4 different naming patterns before documenting as a failure
- Check AWS service-specific naming requirements in the documentation

### Issue: Invalid principal in policy
**Symptom:** "Invalid principal in policy" or "ValidationException: Invalid principal" during deployment
**Cause:** Policy principal format is incorrect
**Solution:**
- Use full ARN format: `arn:aws:iam::ACCOUNT_ID:root`
- Don't use just the account ID: `"123456789012"` ❌
- Get your account ID: `aws sts get-caller-identity --query Account --output text`
- Example: `"AWS": "arn:aws:iam::566972129213:root"` ✓

### Issue: KMS key permission errors
**Symptom:** "The provided KMS Key does not provide sufficient permissions for [Service]" or "ValidationException: KMS key policy"
**Cause:** Service-specific KMS key policies require explicit permissions for the AWS service to use the key
**Solution:**

**Step 1: Search AWS documentation for service-specific KMS requirements**
- Use AWS documentation search to find KMS key policy requirements
- Search for: "[service name] KMS key policy" or "[service name] customer managed key"
- Example searches:
  - "WorkSpaces Web KMS key policy"
  - "S3 customer managed key permissions"
  - "Lambda KMS encryption key policy"
- Look for documentation sections on:
  - "Encryption at rest"
  - "Customer managed keys"
  - "Key policies"
  - "Required permissions"

**Step 2: Check the Terraform resource documentation**
- Review the `customer_managed_key` or similar argument description
- Often includes links to AWS documentation about required permissions
- May include example key policies

**Step 3: Create KMS key with proper permissions**
- KMS keys need policies that grant both IAM user permissions AND service permissions
- Add a data source for account ID: `data "aws_caller_identity" "current" {}`
- Create a comprehensive key policy:
```hcl
resource "aws_kms_key" "test" {
  description             = "KMS key for [Service]"
  deletion_window_in_days = 7

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "Enable IAM User Permissions"
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:root"
        }
        Action   = "kms:*"
        Resource = "*"
      },
      {
        Sid    = "Allow [Service] to use the key"
        Effect = "Allow"
        Principal = {
          Service = "[service].amazonaws.com"
        }
        Action = [
          "kms:Decrypt",
          "kms:GenerateDataKey",
          "kms:CreateGrant",
          "kms:DescribeKey"
        ]
        Resource = "*"
        # Some services may require Condition blocks - check documentation
      }
    ]
  })
}
```

**Step 4: If KMS setup is too complex**
- Skip KMS-related features in testing and document this limitation
- After 2-3 failed attempts or if requirements are unclear, move on
- **Example:** `aws_workspacesweb_user_settings` with `customer_managed_key` requires complex KMS policies
- Focus on testing other features instead of spending excessive time on KMS configuration

**When to skip KMS testing:**
- KMS policy requirements are unclear or undocumented
- Service requires additional IAM roles, conditions, or grants
- After 2-3 failed attempts to configure KMS correctly
- Documentation search yields no clear guidance
- Document in test-results.md: "KMS encryption excluded - requires complex policy setup"

**Common KMS permission patterns:**
- Most services need: `kms:Decrypt`, `kms:GenerateDataKey`, `kms:CreateGrant`
- Some services need: `kms:DescribeKey`, `kms:RetireGrant`, `kms:ReEncrypt*`
- Some services require condition keys like `kms:ViaService` or `kms:EncryptionContext`

### Issue: Unsupported attribute in Terraform configuration
**Symptom:** `Error: Unsupported attribute` or `This object has no argument, nested block, or exported attribute named "X"`
**Cause:** Using wrong attribute name (e.g., `.arn` instead of `.vector_bucket_arn`)
**Solution:**
- Check the "Attribute Reference" section in Terraform docs
- Use the exact attribute name from documentation
- Don't assume generic names like `.arn` or `.id` exist
- Example: Use `.vector_bucket_arn` not `.arn`

### Issue: Resource exports no additional attributes
**Symptom:** Cannot output `.id` or other attributes from resource
**Cause:** Some resources (especially policy resources) export no additional attributes
**Solution:**
- Check documentation: "This resource exports no additional attributes"
- Use input arguments or parent resource attributes for testing
- Example: For bucket policy, output the bucket ARN instead of policy ID

## Special Resource Types

### Resources That Need No Custom Handler Logic

Some resources import perfectly without any custom field handling:
- All attributes are correctly captured
- No computed fields cause drift
- No lifecycle blocks needed
- Post-import plan shows 0 changes

**Example:** `aws_workspacesweb_portal`

When this happens:
- The existing stub handler (via `__getattr__`) is sufficient
- No need to add custom logic to the handler file
- Document this in test-results.md as a clean import
- This is the ideal outcome for any resource test

### Policy Resources

Policy resources have unique characteristics that require special handling:

**Identification:**
- Resource names ending in `_policy` (e.g., `aws_s3_bucket_policy`, `aws_s3vectors_vector_bucket_policy`)
- Attach policies to parent resources (buckets, roles, etc.)

**Key characteristics:**
1. **No unique ID** - Use parent resource ARN/ID as the import identifier
2. **No list operation** - Must iterate through parents and try to get each policy
3. **May not exist** - Not all parent resources have policies attached
4. **JSON normalization drift** - Key ordering differences cause perpetual plan changes

**Required implementation patterns:**

**In aws_dict.py:**
```python
aws_<service>_<resource>_policy = {
    "clfn": "<service>",
    "descfn": "get_<resource>_policy",  # Note: get, not list
    "topkey": "policy",
    "key": "<parentResourceArn>",  # Use parent's ARN field
    "filterid": "<parentResourceArn>"
}
```

**In get function:**
```python
# Must iterate through parents and handle NoSuchPolicy exceptions
for parent in parents:
    try:
        policy_response = client.get_<resource>_policy(parentArn=parent_arn)
        common.write_import(type, parent_arn, None)  # Use parent ARN
    except client.exceptions.NoSuch<Resource>Policy:
        continue  # Policy doesn't exist for this parent
```

**In handler function:**
```python
# Always add lifecycle block to ignore JSON key ordering
elif tt1 == "<parent_identifier_field>":
    t1 = t1 + "\n lifecycle {\n   ignore_changes = [policy]\n}\n"
```

**Testing considerations:**
- Must create parent resource first
- Policy document must have valid format (proper principal ARNs, etc.)
- Expect JSON key ordering changes in plan (handled by lifecycle block)
- Cannot output `.id` - use parent resource identifier instead







