---
inclusion: always
---

# New Resource Testing Procedure

This document defines the testing procedure for new AWS resource types in the aws2tf tool. Follow these steps sequentially when adding support for a new resource type.

## Prerequisites Check

Before testing a new resource type (e.g., `aws_vpc`), verify these conditions in order:

### 0. Check for Existing Test Results

**FIRST:** Check if a test-results.md file already exists in the test directory:

```bash
cat code/.automation/test_<resource_type>/test-results.md
```

**If test-results.md exists and shows basic tests passed:**
- Review the test summary section
- If "Resource deployment (basic): ✓" and "Type-level import (basic): ✓" and "Specific import (basic): ✓" are all present
- **SKIP to Step 5.8 (Comprehensive Configuration Test)** - No need to repeat basic tests
- Use the existing test infrastructure or create new comprehensive test configuration
- After comprehensive tests pass, update the existing test-results.md with comprehensive test results

**If test-results.md does not exist OR basic tests failed:**
- Continue with all steps below starting from Step 1

**If test-results.md shows comprehensive tests already passed:**
- No further testing needed unless you're debugging or adding new features
- Document any additional work in the existing test-results.md

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
- **CRITICAL: If found and uncommented, you MUST comment it out to enable testing**
  - Add `#` at the start of the line to comment it out
  - Example: Change `"aws_api_gateway_api_key": True,` to `#"aws_api_gateway_api_key": True,`
  - **This is required** - aws2tf will block the resource if it's in the notimplemented dictionary
  - **LOGIC:** Resources in this dictionary are BLOCKED. Comment out = enable testing.
- If found and already commented out, the resource is already enabled
- **STOP** if the resource cannot be found in either file

### 2.5. Check aws_no_import.py Status
- Open `code/fixtf_aws_resources/aws_no_import.py`
- Search for the resource type
- **CRITICAL: If found and uncommented (marked True), STOP IMMEDIATELY**
  - Resources in aws_no_import.py cannot be imported via Terraform
  - These resources can only be created/managed, not imported from existing infrastructure
  - **Mark in to-test.md as:** `(SKIPPED - no import support)`
  - **Document reason:** Create test-skipped.md explaining the resource cannot be imported
  - **Example resources:** Default resources, singleton resources without import support
- If found and commented out, the resource has import support - continue testing
- If not found in the file, the resource has import support - continue testing

**Why this matters:**
- aws_no_import.py contains resources that Terraform doesn't support importing
- Testing these resources would fail at the import step
- Early detection saves time and provides clear documentation

### 3. Verify Import ID Format

**CRITICAL:** The import documentation is the source of truth for ID format throughout the system.

- Navigate to `code/.automation/terraform-provider-aws/website/docs/r/<resource>.html.markdown`
- Locate the import block example
- **The `id` field value determines everything:**
  - What format the get function must write imports with
  - What format resource names will use
  - What format dependent resources must reference
- Check if the `id` field contains composite identifiers with `,` separators

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
  id = "subnet-12345,rtb-67890"  # Comma = composite ID
}
```

**IMPORTANT: Import ID vs API Response Mismatch**

Sometimes the API returns a different identifier format than what Terraform import expects:

**Example: Prometheus Workspace**
- API returns: `arn:aws:aps:us-east-1:123456789012:workspace/ws-abc123` (ARN)
- Import expects: `ws-abc123` (workspace ID)
- aws_dict.py has: `key: "workspaceId"`, `filterid: "arn"` (conflicting!)

**Solution:** Create custom get function that writes imports using the format from import docs:
```python
def get_aws_prometheus_workspace(type, id, clfn, descfn, topkey, key, filterid):
    # ...
    for j in response:
        # Write import using workspace ID (from import docs)
        # NOT using ARN (from filterid)
        common.write_import(type, j['workspaceId'], None)
```

**Why this matters:**
- Resource names are based on the import ID format
- Dependent resources reference by resource name
- If get function uses ARN but import expects ID, references break
- Handler in dependent resource: `aws_prometheus_workspace.<workspace_id>.id` ✓
- If using ARN: `aws_prometheus_workspace.arn_aws_aps_...` ✗ (unpredictable, breaks)

**Rule:** Always write imports using the ID format from Terraform import documentation, even if the API returns something different (ARN, composite structure, etc.). Extract or transform the API response to match the import format.

**If composite ID detected:**
- **DO NOT immediately stop and document as unsupported**
- **ATTEMPT to implement composite ID support** by creating a custom get function
- Composite IDs can be supported with proper get function implementation
- See successful examples: `aws_ec2_subnet_cidr_reservation`, `aws_opensearchserverless_security_policy`, `aws_route53_resolver_firewall_rule`, `aws_s3tables_table_policy`
- Only mark as unsupported after attempting implementation (up to 4 attempts)
- Document the composite ID format and implementation approach in test-results.md

## Testing Steps

Execute these steps only if all prerequisites are met AND basic tests haven't already passed (check Step 0):

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
2. **For most resources:** Use `version = "~> 6.0"` to get the latest 6.x version
3. If marked `### TODO 6.27.0` or similar, you can use `version = "~> 6.27"` for that specific version
4. **IMPORTANT:** Always use version 6.x or later - do NOT use version 5.x (this is non-negotiable for consistency)
5. For older resources without TODO comments, still use `version = "~> 6.0"`

**Finding example code:**
1. Check `code/.automation/terraform-provider-aws/website/docs/r/<resource>.html.markdown` for official examples
2. Use the simplest example that creates a functional resource
3. Include only essential supporting resources (e.g., VPC for subnet testing)
4. Add `provider.tf` with AWS provider configuration
5. Add `outputs.tf` to capture the resource ID

**For resources with dependencies:**
- **It is expected and acceptable to create dependent resources** for testing
- **ALWAYS attempt to create prerequisites** rather than skipping complex resources
- Include only the minimal required parent resources
- Use the simplest configuration for parent resources
- Example: Testing `aws_s3vectors_index` requires `aws_s3vectors_vector_bucket`
- Example: Testing `aws_subnet` requires `aws_vpc`
- Example: Testing `aws_api_gateway_documentation_part` requires `aws_api_gateway_rest_api`
- Example: Testing `aws_lambda_function_recursion_config` requires `aws_lambda_function` and `aws_iam_role`
- Example: Testing `aws_redshiftserverless_endpoint_access` requires VPC, subnets, namespace, and workgroup
- Example: Testing `aws_sagemaker_flow_definition` requires S3 bucket, IAM role, and human task UI
- Example: Testing `aws_opensearchserverless_collection` requires encryption and network security policies

**Creating dependency infrastructure:**
When a resource requires parent resources (REST API, VPC, Lambda function, etc.):
1. **Include parent resources in the same main.tf** - Don't create separate test directories
2. **Use minimal parent configuration** - Only required arguments for parent resources
3. **Create supporting resources as needed** - IAM roles, zip files, certificates, S3 buckets, etc.
4. **Check AWS documentation for IAM permissions** - Search for managed policies or required permissions
5. **Use dummy/sample artifacts when needed** - Create minimal HTML templates, JSON configs, XML metadata, etc.
6. **Attempt up to 4 times to get prerequisites working** - Don't give up on first failure
7. **Only skip after exhausting attempts** - Document what was tried and why it couldn't work
5. **Prefer AWS managed policies** - Use AWS managed policies (e.g., AWSLambdaManagedEC2ResourceOperator) instead of custom policies when available
6. **Create multiple instances if needed** - Test different configurations of the target resource
7. **Document dependencies** - Note which parent resources were created in test-results.md
8. **Clean up all resources** - Terraform destroy will handle all resources in the configuration
9. **Don't avoid testing due to dependencies** - Most AWS resources have dependencies; this is normal

**Finding required IAM permissions:**
When a resource requires an IAM role with specific permissions:
1. **Search AWS documentation first** - Use AWS documentation search for "[service] IAM permissions" or "[resource] operator role"
2. **Look for managed policies** - AWS often provides managed policies with all required permissions
3. **Check error messages** - If deployment fails with permission errors, the error message lists the missing permission
4. **Iterate if needed** - Add permissions incrementally (max 4 attempts per failure point)
5. **Document the solution** - Note which managed policy or permissions were required in test-results.md

**Example: Lambda Capacity Provider IAM role**
- Searched: "Lambda Capacity Provider IAM permissions operator role"
- Found: AWS managed policy `AWSLambdaManagedEC2ResourceOperator`
- Result: Single policy attachment instead of custom policy with trial-and-error permissions

**Example: Testing recursion_config with Lambda function dependency:**
```hcl
# Parent resource (minimal configuration)
resource "aws_api_gateway_rest_api" "test" {
  name        = "test-api-20250101"
  description = "Test REST API for documentation part testing"
}

# Target resource being tested (comprehensive configuration)
resource "aws_api_gateway_documentation_part" "test" {
  rest_api_id = aws_api_gateway_rest_api.test.id
  
  location {
    type = "API"
  }
  
  properties = jsonencode({
    description = "Comprehensive test API documentation"
    info = {
      version = "1.0.0"
      title   = "Test API"
    }
  })
}

# Additional instance to test different location types
resource "aws_api_gateway_documentation_part" "test_method" {
  rest_api_id = aws_api_gateway_rest_api.test.id
  
  location {
    type   = "METHOD"
    method = "GET"
    path   = "/"
  }
  
  properties = jsonencode({
    description = "GET method documentation"
  })
}
```

**Example: Testing recursion_config with Lambda function dependency:**
```hcl
# IAM role for Lambda (required dependency)
resource "aws_iam_role" "lambda_role" {
  name = "test-lambda-recursion-role-20250101"
  
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

# Lambda function (parent resource - minimal configuration)
resource "aws_lambda_function" "test" {
  filename      = "lambda_function.zip"  # Create simple zip with index.py
  function_name = "test-recursion-function-20250101"
  role          = aws_iam_role.lambda_role.arn
  handler       = "index.handler"
  runtime       = "python3.12"
  
  source_code_hash = filebase64sha256("lambda_function.zip")
}

# Target resource being tested (comprehensive configuration)
resource "aws_lambda_function_recursion_config" "test_allow" {
  function_name  = aws_lambda_function.test.function_name
  recursive_loop = "Allow"
}
```

**For resources that can be referenced by other resources:**
- It is acceptable to create additional related resources that reference the resource being tested
- This helps verify the resource exports the correct attributes for use by other resources
- Example: Testing `aws_workspacesweb_network_settings` can include `aws_workspacesweb_network_settings_association` to verify the ARN is exported correctly
- Example: Testing `aws_s3_bucket` can include `aws_s3_bucket_policy` to verify the bucket can be referenced
- Document these additional resources in test-results.md

**Required files:**
- `main.tf` - Resource definitions
- `provider.tf` - AWS provider configuration (with correct version)
- `outputs.tf` - Output the resource ID for testing

**Example provider.tf (use latest 6.x):**
```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"  # Use latest 6.x version
    }
  }
}

provider "aws" {
  region = "us-east-1"  # Remember this region for aws2tf.py -r flag
}
```

**Example provider.tf for specific version:**
```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.27"  # Match specific version from aws_not_implemented.py if needed
    }
  }
}

provider "aws" {
  region = "us-east-1"
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

**Important: Terraform Operation Timeouts**
- Some resources can take up to 20 minutes to create, update, or destroy
- Common slow operations:
  - Route53 Resolver DNSSEC configs: 2-4 minutes to create/destroy
  - Route53 Resolver configs: 1-2 minutes to create/update
  - Route53 Resolver rule associations: 1-2 minutes to create/destroy
  - VPC Block Public Access resources: 3-4 minutes to create/destroy
  - VPC Route Server endpoints: 1-2 minutes to create
  - Redshift Serverless workgroups: 1-2 minutes to create, 1-2 minutes to destroy
  - Redshift Serverless namespaces: 1-2 minutes to create, 2-3 minutes to destroy
  - OpenSearch Serverless collections: 1-2 minutes to create, 30-60 seconds to destroy
  - SageMaker device fleets: 10+ minutes to create (may timeout)
  - Some complex resources with multiple dependencies: up to 20 minutes
- Use timeout of at least 960000ms (16 minutes) for terraform apply/destroy commands
- For particularly slow resources or complex setups, use 1200000ms (20 minutes) timeout
- If a command times out, check `terraform show` to see if the operation completed
- Operations will continue in the background even if the command times out

**Capture the resource ID** from the output or state:
```bash
terraform output <resource_id_output_name>
# OR
terraform state show <resource_address> | grep "^id"
```

### Step 4: Test Type-Level Import

**REQUIRED TEST #1:** Test aws2tf's ability to discover and import all resources of this type.

Test aws2tf's ability to discover and import all resources of this type:

```bash
cd <workspace_root>
./aws2tf.py -r <region> -t <resource_type>
```

**CRITICAL: Region Consistency**
- **ALWAYS use the `-r` flag** to specify the same region as in your `provider.tf`
- Example: If `provider.tf` has `region = "us-east-1"`, use `./aws2tf.py -r us-east-1 -t <resource_type>`
- Without `-r`, aws2tf uses your default AWS CLI region, which may differ from where you created the test resource

**Important: Command Timeouts and Performance**
- aws2tf commands can take 30-60 seconds or longer depending on account size
- Use timeout of at least 120000ms (2 minutes) when running commands
- The tool performs initial resource discovery which scans 9 core resource types (~10 seconds)
- Progress bar shows: "Fetching resource lists: X% | S3 buckets, Lambda functions, etc."
- This discovery happens even when testing a single resource type
- Don't assume timeout = failure; check for generated files in `generated/` directory
- If command times out but files were generated, the import likely succeeded

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

**REQUIRED TEST #2:** Test aws2tf's ability to import a specific resource by ID.

**IMPORTANT:** This test is REQUIRED even if Step 4 passed. Do not skip this step!

Test aws2tf's ability to import a specific resource by ID:

```bash
./aws2tf.py -r <region> -t <resource_type> -i <actual_resource_id>
```

Example: `./aws2tf.py -r us-east-1 -t aws_vpc -i vpc-09d8b4321d497f01b`

**Why both tests are required:**
- Type-level test (`-t` only): Validates discovery and listing logic
- Specific test (`-t -i`): Validates get-by-ID logic and ID format handling
- Both code paths are different and both must work correctly
- Some resources are in needid_dict and ONLY support specific import (no type-level discovery)

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

**F. Dereference parent resource IDs and add dependencies:**

When a resource references a parent resource by ID, you need to:
1. Transform the ID field to reference the parent resource
2. Add the parent as a dependency so aws2tf imports it automatically

**Pattern:**
```python
def aws_<resource>(t1, tt1, tt2, flag1, flag2):
    skip = 0
    
    # Extract parent ID from resource name when resource block starts
    if t1.startswith("resource"):
        context.parent_id = t1.split("r-")[1].split("_")[0]
    
    # Transform parent ID field to resource reference and add dependency
    if tt1 == "parent_resource_id" and tt2 != "null":
        # Transform: parent_resource_id = "abc123"
        # Into: parent_resource_id = aws_parent_resource.r-abc123.id
        t1 = tt1 + " = aws_parent_resource.r-" + str(context.parent_id) + ".id\n"
        
        # Add parent as dependency so aws2tf imports it automatically
        common.add_dependancy("aws_parent_resource", str(context.parent_id))
    
    return skip, t1, flag1, flag2
```

**Real Example: API Gateway Documentation Part**
```python
def aws_api_gateway_documentation_part(t1, tt1, tt2, flag1, flag2):
    skip = 0
    
    # Extract REST API ID from resource name
    if t1.startswith("resource"):
        context.apigwrestapiid = t1.split("r-")[1].split("_")[0]
    
    # Transform rest_api_id field and add REST API as dependency
    if tt1 == "rest_api_id" and tt2 != "null":
        t1 = tt1 + " = aws_api_gateway_rest_api.r-" + str(context.apigwrestapiid) + ".id\n"
        common.add_dependancy("aws_api_gateway_rest_api", str(context.apigwrestapiid))
    
    return skip, t1, flag1, flag2
```

**Why this is needed:**
- Generated Terraform initially has: `rest_api_id = "29bg9hqtq7"` (string literal)
- Handler transforms to: `rest_api_id = aws_api_gateway_rest_api.r-29bg9hqtq7.id` (resource reference)
- `common.add_dependancy()` tells aws2tf to import the REST API automatically
- Without this, validation fails with "Reference to undeclared resource"

**Common parent resource patterns:**
- API Gateway resources → REST API (`aws_api_gateway_rest_api`)
- VPC resources → VPC (`aws_vpc`)
- Subnet resources → VPC (`aws_vpc`)
- Security group rules → Security group (`aws_security_group`)
- Route table associations → Route table (`aws_route_table`)

**Note:** Policy resources (like `aws_s3_bucket_policy`, `aws_iam_role_policy`, `aws_s3vectors_vector_bucket_policy`) often have JSON normalization issues where Terraform and AWS return different key ordering. Always add lifecycle blocks to ignore the policy field.

### Step 5.5b: Resources in needid_dict - Dependency Management

Some resources are listed in `code/fixtf_aws_resources/needid_dict.py` because they require a parent resource ID parameter to list their resources.

**Check if your resource is in needid_dict:**
```bash
grep "aws_<resource_type>" code/fixtf_aws_resources/needid_dict.py
```

**If found, you MUST implement both:**

**1. Get function that accepts parent ID:**
```python
def get_aws_<resource>(type, id, clfn, descfn, topkey, key, filterid):
    if id is not None:
        # id parameter contains the parent resource ID
        paginator = client.get_paginator(descfn)
        for page in paginator.paginate(parentId=id):
            for j in page[topkey]:
                # Build composite ID if needed
                child_id = id + '/' + j[key]
                common.write_import(type, child_id, None)
    else:
        log.debug("Must pass parentId for "+type)
```

**2. Handler function that adds parent dependency:**
```python
def aws_<resource>(t1, tt1, tt2, flag1, flag2):
    skip = 0
    
    # Extract parent ID from resource name
    if t1.startswith("resource"):
        context.parent_id = t1.split("r-")[1].split("_")[0]
    
    # Transform parent ID field and add dependency
    if tt1 == "parent_id_field" and tt2 != "null":
        t1 = tt1 + " = aws_parent_resource.r-" + str(context.parent_id) + ".id\n"
        common.add_dependancy("aws_parent_resource", str(context.parent_id))
    
    return skip, t1, flag1, flag2
```

**Why both are needed:**
- Get function: Lists child resources given parent ID
- Handler function: Transforms parent ID references and triggers automatic parent import
- Without handler: Validation fails with "Reference to undeclared resource"
- With handler: aws2tf automatically imports parent resources

**Testing command for needid_dict resources:**
```bash
./aws2tf.py -r us-east-1 -t <resource_type> -i <parent_resource_id>
```

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

Some resources can only be listed within a parent resource context (e.g., indexes require a vector bucket name, documentation parts require a REST API ID).

**Pattern A: Parent resource parameter required for listing (e.g., S3 Vectors indexes):**

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
- `aws_api_gateway_documentation_part` (requires restApiId to list)

**Pattern B: Composite ID format with parent (e.g., API Gateway documentation parts):**

Some resources use composite IDs that include the parent resource ID (e.g., `restApiId/docPartId`):

```python
def get_aws_<resource>(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # First get all parent resources
            parent_paginator = client.get_paginator('get_<parents>')
            parents = []
            for page in parent_paginator.paginate():
                parents = parents + page['items']
            
            # Then list children for each parent
            for parent in parents:
                try:
                    child_paginator = client.get_paginator(descfn)
                    for page in child_paginator.paginate(parentId=parent['id']):
                        for j in page[topkey]:
                            # Build composite ID: parentId/childId
                            composite_id = parent['id'] + '/' + j[key]
                            common.write_import(type, composite_id, None)
                except Exception as e:
                    if context.debug: log.debug(f"Error listing for parent {parent['id']}: {e}")
                    continue
        else:
            # Get specific resource by composite ID
            if '/' in id:
                parent_id, child_id = id.split('/', 1)
                response = client.get_<resource>(parentId=parent_id, childId=child_id)
                if response:
                    common.write_import(type, id, None)
            else:
                if context.debug: log.debug("Must pass parentId/childId for "+type)
    
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
    return True
```

**Examples:**
- `aws_api_gateway_documentation_part` (restApiId/docPartId)
- `aws_api_gateway_deployment` (restApiId/deploymentId)
- `aws_api_gateway_stage` (restApiId/stageName)

### Step 5.7b: Check if Get Function Already Exists

**IMPORTANT:** Before creating a new get function file, check if the service file already exists:

```bash
ls code/get_aws_resources/aws_<service>.py
```

**If the file exists:**
1. Open the file and search for your specific resource function
2. Search for: `def get_aws_<resource_type>`
3. **If function doesn't exist:** Add it to the existing file (don't create a new file)
4. **If function exists:** Verify it's correct and skip creation
5. Follow the same patterns as other functions in the file

**Example:** For `aws_api_gateway_api_key`:
- File `code/get_aws_resources/aws_apigateway.py` already exists ✓
- Function `get_aws_api_gateway_api_key` didn't exist
- Added function to existing file (didn't create new aws_apigateway.py)
- Followed the pattern of other functions in the file

**If the file doesn't exist:**
- Create new file following the patterns in Step 5.7
- Remember to register it in common.py (Step 5.7 final section)

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

### Step 5.8: Comprehensive Configuration Test (Required)

**Check if basic tests already passed:**
```bash
# If test-results.md exists and shows basic tests passed, start here
cat code/.automation/test_<resource_type>/test-results.md | grep "Resource deployment (basic): ✓"
```

After the basic tests pass (or if they've already passed from a previous run), you MUST create a comprehensive test to verify all optional features work correctly:

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
- List any additional related resources created to verify attribute exports
- If resource has no optional arguments, explicitly state: "Resource has no optional arguments - only required fields tested"
```

**When to simplify the comprehensive test:**
- Resource has no optional arguments (document this in test-results.md)
- Resource is very simple with only required fields (still run the test to confirm)
- Skip features requiring complex dependent resources (e.g., KMS keys with service-specific policies)
- Skip features requiring additional IAM roles or complex permissions
- Focus on features that can be tested with simple configuration
- Document excluded features in test-results.md

**Why this step is required:**
- Confirms handler works with complex configurations
- Validates nested block handling
- Ensures no edge cases cause drift
- Provides confidence for production use
- Verifies all optional features are correctly imported
- Tests that the resource can be referenced by other resources (if applicable)

**IMPORTANT:** This step is mandatory for all resource tests. Even if a resource has no optional arguments, you must still run this step to confirm and document that fact.

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

Create or update documentation in the test directory:

**If updating existing test-results.md (basic tests already passed):**
- Keep the existing basic test results
- Add a new section "## Comprehensive Configuration Test Results" 
- Update the Test Summary section to mark comprehensive tests as complete
- Add timestamp for when comprehensive tests were completed
- Document all comprehensive features tested

**If creating new test-results.md (full test run):**

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
- Comprehensive configuration: ✓
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

### Step 7.1: Update Tracking Files (MANDATORY)

**CRITICAL:** After completing a test (success or failure), you MUST update the tracking files immediately:

**For successful tests:**

1. **Update to-test.md** - Mark resource as completed:
```bash
# Change from:
- [ ] `aws_resource_name`
# To:
- [x] `aws_resource_name`
```

2. **Update to-test-completed.md** - Add entry with link:
```markdown
### aws_service

- [x] `aws_resource_name` - ✓ PASSED (YYYY-MM-DD) - [test results](test_aws_resource_name/test-results.md)
```

3. **Update total count** in to-test-completed.md:
```markdown
**Total Completed:** X  # Increment by 1
**Last Updated:** YYYY-MM-DD
```

**For failed/skipped tests:**

1. **Update to-test.md** - Mark as attempted:
```bash
- [x] `aws_resource_name` (FAILED - see test directory)
# OR
- [x] `aws_resource_name` (SKIPPED - requires EKS cluster)
```

2. **Do NOT add to to-test-completed.md** - only successful tests go there

3. **Re-enable in aws_not_implemented.py** - Uncomment the resource with explanation:
```python
# In code/fixtf_aws_resources/aws_not_implemented.py
# Change from:
#    "aws_resource_name": True,
# Back to:
    "aws_resource_name": True,  ### Reason for failure (e.g., AWS API limitation - destination block not returned)
```

**Examples of failure reasons to document:**
- `### AWS API limitation - destination block not returned by describe_<resource>`
- `### Composite ID format not supported`
- `### Requires EKS cluster - too complex for automated testing`
- `### Requires domain ownership and SSL certificates`
- `### API method does not exist in boto3`

**Why this is critical:**
- Tracks progress across sessions
- Prevents re-testing completed resources
- Provides quick status overview
- Essential for resumable bulk testing

**REMEMBER:** Update these files IMMEDIATELY after Step 7, before moving to the next resource!

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
- Composite ID format detected → **ATTEMPT to implement support first** (up to 4 attempts), only stop if implementation fails
- 4 failed fix attempts per failure point → Stop and document
- Physical hardware required (AWS Outposts) → Stop and document
- Account-level service enablement required (Security Lake) → Stop and document after 2 attempts

## Complete Example: Testing aws_workspacesweb_network_settings (Comprehensive Only)

This example shows running only the comprehensive test when basic tests have already passed:

```bash
# Step 0: Check existing test results
cat code/.automation/test_aws_workspacesweb_network_settings/test-results.md
# Shows: "Resource deployment (basic): ✓" - basic tests already passed!

# Skip to Step 5.8: Update main.tf with comprehensive configuration
cd code/.automation/test_aws_workspacesweb_network_settings

# Update main.tf to add all optional features
cat > main.tf << 'EOF'
# ... comprehensive configuration with all optional arguments ...
EOF

# Deploy comprehensive configuration
terraform init
terraform validate
terraform apply -auto-approve

# Test imports with comprehensive configuration
cd ../../..
./aws2tf.py -r us-east-1 -t aws_workspacesweb_network_settings
./aws2tf.py -r us-east-1 -t aws_workspacesweb_network_settings -i "<resource_arn>"

# Verify - should show 0 changes after import

# Cleanup
cd code/.automation/test_aws_workspacesweb_network_settings
terraform destroy -auto-approve
rm -rf .terraform .terraform.lock.hcl

# Update test-results.md with comprehensive test results
# Add new section documenting comprehensive features tested
```

## Complete Example: Testing aws_vpc (Full Test Run)

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

## API Response Structure Patterns

Understanding API response patterns saves hours of debugging. Here are the common patterns discovered across 40+ tested resources:

### Pattern A: List Returns Objects
- Response: `{topkey: [{id: "x", name: "y"}, ...]}`
- Example: list_resolver_configs → ResolverConfigs (list of objects)
- Use: Standard key field from aws_dict.py
- Most common pattern

### Pattern B: List Returns Strings (ARNs)
- Response: `{topkey: ["arn:...", "arn:..."]}`
- Example: list_services → serviceArns (list of strings)
- Requires: Custom get function to handle string list
- Cannot use standard key extraction

### Pattern C: Get Returns Wrapped Object
- Response: `{singular_key: {data}}`
- Example: get_portal → {portal: {...}}
- Use: `j = response.get('singular_key', response)`
- Common with "get" operations

### Pattern D: Regional Singleton
- No list operation, uses region as ID
- Example: aws_vpc_block_public_access_options
- Requires: Custom get function that writes region as ID
- Import ID is the region name

### Pattern E: Policy-Type (No List Operation)
- Must iterate parent resources and try to get each
- Example: aws_s3tables_table_bucket_replication, aws_s3_bucket_policy
- Requires: Custom get function with exception handling for NotFoundException
- Pattern: list parents → try get policy for each → handle exceptions

## Service-Specific Naming Requirements

Certain AWS services have strict naming requirements that cause validation errors if not followed:

### Kinesis Streams for WorkSpaces Web
- **MUST** start with "amazon-workspaces-web-"
- Example: "amazon-workspaces-web-test-20250102"
- Error if not: "ValidationException: Kinesis stream must start with amazon-workspaces-web-"

### S3 Buckets for Logging
- **Avoid** AWS-reserved prefixes: "aws", "amazon", "aws2tf"
- **Use:** "test-{purpose}-{date}-{account_id}"
- Example: "test-session-logger-20250102-566972129213"

### Browser Policies (WorkSpaces Web)
- **MUST** use "chromePolicies" format
- **NOT** "AdditionalSettings" format
- Example: `chromePolicies: { DownloadRestrictions: { value: 3 } }`

### Certificate Format
- **MUST** be valid PEM format with proper headers
- Use Amazon Root CA 1 for testing (provided in examples)
- Invalid format causes immediate validation error

## Resources Requiring Account-Level Enablement

These resources cannot be tested without special account configuration. Identify and skip early to save time:

### Security Lake (All Resources)
- **Error:** "AccessDeniedException: account not authorized"
- **Requires:** Security Lake enabled at account/organization level
- **Skip all:** aws_securitylake_* (5 resources)
- **Not an IAM issue** - requires service enablement

### Similar Patterns to Watch For
- **GuardDuty:** May require organization-level enablement
- **Detective:** Requires AWS Organizations
- **Macie:** Requires service enablement
- **Control Tower:** Requires organization setup

**Early Detection:**
- If you see "AccessDeniedException" with "account not authorized"
- And IAM permissions look correct
- It's likely an account-level enablement issue
- Document and skip the entire service group

## Known AWS API Limitations

Document API limitations to prevent repeated debugging efforts:

### aws_networkflowmonitor_monitor
- **Issue:** get_monitor API does not return scopeArn field
- **Impact:** Cannot dereference scope dependency (required field)
- **Result:** Import generates `scope_arn = null` → validation error
- **Status:** Blocked until AWS adds scopeArn to API response
- **Workaround:** None available

### Pattern: Missing Required Fields in API Response
If a Terraform resource requires a field that the AWS API doesn't return:
1. Verify the API response structure with boto3
2. Check if field exists in list vs get operations
3. If truly missing, document as API limitation
4. Re-comment in aws_not_implemented.py with explanation
5. Create test-failed.md documenting the API gap

**This is not an aws2tf bug - it's an AWS API limitation.**

## Troubleshooting Common Issues

### Issue: "Not supported by aws2tf currently" message
**Symptom:** aws2tf says "Not supported by aws2tf currently: aws_<resource>" and exits
**Cause:** Resource is still uncommented in `aws_not_implemented.py`
**Solution:** 
- Open `code/fixtf_aws_resources/aws_not_implemented.py`
- Find the resource line (e.g., `"aws_api_gateway_api_key": True,`)
- Comment it out by adding `#` at the start: `#"aws_api_gateway_api_key": True,`
- This is a **required step** - aws2tf blocks resources in the notimplemented dictionary
- Re-run aws2tf after commenting out the resource

### Issue: Specific import returns "NOT FOUND"
**Symptom:** `./aws2tf.py -t <type> -i <id>` returns "NOT FOUND: aws_<resource> <id> check if it exists"
**Cause:** The get function's specific ID handling may be incorrect, or resource doesn't exist
**Solution:**
1. Verify the resource still exists in your test directory
2. Check the get function handles the `id is not None` case correctly
3. Verify the boto3 get method parameter name matches the API
   - Example: `get_api_key(apiKey=id)` not `get_api_key(id=id)`
4. Test the boto3 API directly: `python3 -c "import boto3; client = boto3.client('<service>'); print(client.get_<resource>(<param>='<id>'))"`
5. Ensure the get function extracts the correct key from the response

### Issue: Resource not in aws_dict.py
**Solution:** Add the resource to `aws_dict.py` first using the pattern from `new-capability.md`

### Issue: Wrong key field in aws_dict.py
**Symptom:** Import files are generated but with wrong IDs, or Terraform import fails
**Solution:** 
- Check the boto3 API response structure
- **Check the Terraform import documentation for expected ID format** (this is the source of truth!)
- Update the `key` field in aws_dict.py to match (e.g., use ARN field instead of name field)
- If API returns different format than import expects, create custom get function

### Issue: Import ID format mismatch (API returns ARN, import expects ID)
**Symptom:** 
- Dependent resources can't find parent resource
- Error: "Not found aws_<parent_resource>.<id>" 
- aws_dict.py has `filterid: "arn"` but import docs show simple ID

**Cause:** API returns ARN but Terraform import expects simpler ID (workspace ID, function name, etc.)

**Solution:** Create custom get function that writes imports using the format from import documentation:

**Example: Prometheus Workspace**
- API returns: `{"arn": "arn:aws:aps:region:account:workspace/ws-abc123", "workspaceId": "ws-abc123"}`
- Import docs show: `id = "ws-abc123"` (workspace ID, not ARN)
- aws_dict.py has: `filterid: "arn"` (wrong for this case!)

**Fix:**
```python
def get_aws_prometheus_workspace(type, id, clfn, descfn, topkey, key, filterid):
    # ...
    for j in response:
        # Write import using workspace ID (from import docs)
        # NOT using ARN (from filterid)
        common.write_import(type, j['workspaceId'], None)
    
    # Handle both ARN and workspace ID when getting specific resource
    if id.startswith("arn:"):
        workspace_id = id.split('/')[-1]  # Extract ID from ARN
    elif id.startswith("ws-"):
        workspace_id = id
```

**Why this is critical:**
- Resource names are based on import ID format
- Dependent resources reference: `aws_prometheus_workspace.<workspace_id>.id`
- If using ARN: resource name becomes `arn_aws_aps_...` (unpredictable, breaks references)
- If using workspace ID: resource name is `ws-abc123` (predictable, references work)

**Rule:** The Terraform import documentation `id =` value is the source of truth. Always write imports using that format, even if aws_dict.py or the API suggests otherwise.

### Issue: Composite ID format
**Solution:** Implement composite ID support with a custom get function

**Composite ID resources CAN be supported** - don't immediately mark as unsupported!

**Common composite ID formats:**
- Colon separator: `parent-id:child-id` (e.g., `subnet-id:reservation-id`)
- Slash separator: `name/type` (e.g., `policy-name/encryption`)
- Semicolon separator: `arn;namespace;name` (e.g., S3 Tables table policy)
- Multi-part: `type/account/name` (e.g., `saml/123456789012/config-name`)

**Implementation approach:**
1. Create custom get function that builds composite IDs
2. Handle both type-level (list all) and specific import cases
3. Parse composite ID in specific import case
4. See successful examples in `code/get_aws_resources/`:
   - `aws_ec2.py`: `get_aws_ec2_subnet_cidr_reservation` (colon separator)
   - `aws_opensearchserverless.py`: `get_aws_opensearchserverless_security_policy` (slash separator)
   - `aws_route53resolver.py`: `get_aws_route53_resolver_firewall_rule` (colon separator)
   - `aws_s3tables.py`: `get_aws_s3tables_table_policy` (semicolon separator)

**Example pattern for composite IDs:**
```python
def get_aws_resource(type, id, clfn, descfn, topkey, key, filterid):
    try:
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all parent resources
            for parent in list_parents():
                # List children for each parent
                for child in list_children(parent_id):
                    # Build composite ID
                    composite_id = f"{parent_id}:{child_id}"
                    common.write_import(type, composite_id, None)
        else:
            # Handle composite ID in specific import
            if ':' in id:  # or '/' or ';' depending on format
                parent_id, child_id = id.split(':', 1)
                # Verify resource exists
                # Write import if found
                common.write_import(type, id, None)
```

**Only mark as unsupported if:**
- Implementation attempts fail after 4 tries
- AWS API doesn't provide necessary data to build composite ID
- Composite ID format is too complex (3+ parts with unclear structure)

**Note:** aws2tf.py may reject certain characters (like semicolons) in command-line IDs, but type-level import will still work perfectly.

### Issue: Terraform validation fails
**Solution:** Review the example in the Terraform docs, ensure all required arguments are provided

### Issue: "Reference to undeclared resource" after import
**Symptom:** Terraform validation fails with "Reference to undeclared resource" for a parent resource
**Cause:** Generated Terraform references a parent resource that wasn't imported
**Solution:** Add a handler function that:
1. Transforms the parent ID field to a resource reference
2. Calls `common.add_dependancy()` to trigger automatic import of the parent

**Example:** For `aws_api_gateway_documentation_part` referencing `rest_api_id`:
```python
def aws_api_gateway_documentation_part(t1, tt1, tt2, flag1, flag2):
    skip = 0
    
    # Extract parent ID from resource name
    if t1.startswith("resource"):
        context.apigwrestapiid = t1.split("r-")[1].split("_")[0]
    
    # Transform rest_api_id and add dependency
    if tt1 == "rest_api_id" and tt2 != "null":
        t1 = tt1 + " = aws_api_gateway_rest_api.r-" + str(context.apigwrestapiid) + ".id\n"
        common.add_dependancy("aws_api_gateway_rest_api", str(context.apigwrestapiid))
    
    return skip, t1, flag1, flag2
```

This transforms `rest_api_id = "29bg9hqtq7"` into `rest_api_id = aws_api_gateway_rest_api.r-29bg9hqtq7.id` and automatically imports the REST API.

### Issue: Resource in needid_dict requires parent ID
**Symptom:** aws2tf says "can not have null id must pass parameter <paramName>"
**Cause:** Resource is in `needid_dict` and requires a parent resource ID to list
**Solution:**
- Check `code/fixtf_aws_resources/needid_dict.py` to see what parameter is required
- Pass the parent resource ID using `-i` flag: `./aws2tf.py -t <type> -i <parent_id>`
- Example: `./aws2tf.py -t aws_api_gateway_documentation_part -i <rest_api_id>`
- The get function should handle the parent ID and list all child resources
- Add handler function to dereference parent and add dependency (see above)

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







