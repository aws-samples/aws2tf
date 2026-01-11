# Stack Resource Testing Procedure

This document defines the testing procedure for importing resources from existing AWS CloudFormation stacks using the aws2tf tool's stack import feature (`./aws2tf.py -t stack -i <stack-name>`).

**Note:** Before testing stack resources, you may want to run the PRE-TEST assessment. See `code/.automation/stack-pre-test-procedure.md` for details.

## Testing Stages Overview

Stack resource testing follows these stages:

1. **Stage 1: Create and Deploy Test Stack** - Create a working CloudFormation stack with the resource
2. **Stage 2: Import Stack Resources** - Use aws2tf to import the stack
3. **Stage 3: Verify and Validate** - Ensure Terraform generation is correct
4. **Stage 4: Cleanup** - Destroy the test stack

---

## Stage 1: Create and Deploy Test Stack

### Purpose

Create a fully functional CloudFormation stack containing the resource type being tested. This validates that the resource can be created and provides a real resource to import.

### Directory Structure

Create a test directory using the CloudFormation resource type name with `::` replaced by `_`:

**Format:** `code/.automation/test_<CloudFormation_Type_With_Underscores>`

**Examples:**
- `AWS::Backup::BackupPlan` → `code/.automation/test_AWS_Backup_BackupPlan`
- `AWS::EC2::VPC` → `code/.automation/test_AWS_EC2_VPC`
- `AWS::Lambda::Function` → `code/.automation/test_AWS_Lambda_Function`

### Step 1.1: Create Test Directory

```bash
# Example for AWS::Backup::BackupPlan
mkdir -p code/.automation/test_AWS_Backup_BackupPlan
cd code/.automation/test_AWS_Backup_BackupPlan
```

### Step 1.2: Determine Terraform Resource Name and Check Support

**CRITICAL:** Before creating the CloudFormation template, verify the resource can be imported.

#### Convert CloudFormation Type to Terraform Resource Name

From the CloudFormation resource type (e.g., `AWS::Logs::QueryDefinition`):
- Service: `Logs`
- Resource: `QueryDefinition`
- Expected Terraform resource name: `aws_cloudwatch_query_definition` or `aws_logs_query_definition`

**Naming patterns:**
- Most resources: `aws_<service_lowercase>_<resource_snake_case>`
- CloudWatch Logs: Often use `aws_cloudwatch_` prefix
- Check aws_dict.py to confirm exact name

#### Check aws_not_implemented.py

```bash
grep "aws_cloudwatch_query_definition" code/fixtf_aws_resources/aws_not_implemented.py
```

**If found and UNCOMMENTED:**
- Resource is marked as not implemented in aws2tf
- **STOP:** Document as NOT SUPPORTED and skip to next resource
- Do not create CloudFormation stack

#### Check aws_no_import.py (CRITICAL)

```bash
grep "aws_cloudwatch_query_definition" code/fixtf_aws_resources/aws_no_import.py
```

**If found and UNCOMMENTED:**
- Resource cannot be imported via Terraform
- **STOP:** Document as NO IMPORT SUPPORT and skip to next resource
- Do not create CloudFormation stack
- Update tracking files and move to next resource

**Example - Resource Cannot Be Imported:**
```markdown
# In test directory, create TEST_SKIPPED.md:

# Test Skipped: AWS::Logs::QueryDefinition

**Date:** 2026-01-11
**Status:** SKIPPED - NO IMPORT SUPPORT

## Reason

The Terraform resource `aws_cloudwatch_query_definition` is listed in 
`code/fixtf_aws_resources/aws_no_import.py`, which means Terraform does 
not support importing this resource type.

## Actions Taken

1. Moved from to-test-stack.md to stack-unsupported.md
2. Marked with NO IMPORT SUPPORT status
3. No CloudFormation stack created (saved time)

## Recommendation

This resource cannot be tested via stack import. It can only be managed 
if created by Terraform, not imported from existing infrastructure.
```

#### Check aws_dict.py Entry Exists

```bash
grep "aws_cloudwatch_query_definition" code/fixtf_aws_resources/aws_dict.py
```

**If not found:**
- Resource needs to be added to aws_dict.py first
- Follow standard resource testing procedure
- **STOP:** Document that aws_dict.py entry is required

**If found:** Verify the entry details:
- Note the `clfn` (boto3 client name)
- Note the `descfn` (API method name)
- Note the `key` (ID field name)

#### Verify Get Function Exists

```bash
find code/get_aws_resources/ -name "*.py" -exec grep -l "def get_aws_cloudwatch_query_definition" {} \;
```

**If not found:**
- Get function needs to be created
- Note this for Stage 2 implementation
- Can proceed with stack creation (will implement in Stage 2)

#### Optional: Verify boto3 API

**Recommended for complex resources:**

```bash
python3 << 'EOF'
import boto3

# Check client and method exist
client = boto3.client('logs', region_name='us-east-1')

# List available methods
methods = [m for m in dir(client) if 'query' in m.lower()]
print("Available methods:", methods)

# Test the describe method
response = client.describe_query_definitions(maxResults=10)
print(f"API works! Found {len(response['queryDefinitions'])} query definitions")
EOF
```

**This helps identify:**
- Correct client name
- Correct API method name
- Required parameters
- Response structure

#### If Resource Can Be Imported - Proceed

If the resource passes all checks:
- ✅ NOT in aws_not_implemented.py
- ✅ NOT in aws_no_import.py
- ✅ EXISTS in aws_dict.py (or will be added)
- ✅ Get function exists (or will be created)

Proceed to Step 1.3.

### Step 1.3: Create CloudFormation Template

Create a YAML file named `template.yaml` with a working CloudFormation template.

**Template Requirements:**
- Must include the resource type being tested
- Should use a minimal but complete configuration
- Must be deployable to `us-east-1` region
- Can include prerequisite resources if needed
- Should use descriptive resource names

**Example Template Structure:**
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: 'Test stack for AWS::Backup::BackupPlan'

Resources:
  # Prerequisite resources (if needed)
  TestVault:
    Type: AWS::Backup::BackupVault
    Properties:
      BackupVaultName: test-backup-vault-20260111
  
  # Main resource being tested
  TestBackupPlan:
    Type: AWS::Backup::BackupPlan
    Properties:
      BackupPlan:
        BackupPlanName: test-backup-plan-20260111
        BackupPlanRule:
          - RuleName: DailyBackup
            TargetBackupVault: !Ref TestVault
            ScheduleExpression: "cron(0 5 ? * * *)"
            StartWindowMinutes: 60
            CompletionWindowMinutes: 120
            Lifecycle:
              DeleteAfterDays: 30

Outputs:
  BackupPlanId:
    Description: Backup Plan ID
    Value: !Ref TestBackupPlan
  BackupPlanArn:
    Description: Backup Plan ARN
    Value: !GetAtt TestBackupPlan.BackupPlanArn
```

**Guidelines for Creating Templates:**

1. **Search AWS Documentation** for the resource type
2. **Use minimal configuration** - only required properties
3. **Include prerequisites** - create dependent resources in the same template
4. **Add unique identifiers** - use timestamps or unique names (e.g., `test-resource-20260111`)
5. **Add outputs** - capture resource IDs and ARNs for verification
6. **Test incrementally** - start simple, add complexity if needed

### Step 1.4: Deploy the Stack

Deploy the CloudFormation stack to `us-east-1` region. **IMPORTANT:** Stack names must use hyphens, not underscores.

```bash
# Stack name: Use hyphens to match directory name pattern
# Directory: test_AWS_CloudWatch_Dashboard
# Stack name: test-AWS-CloudWatch-Dashboard (underscores replaced with hyphens)

STACK_NAME="test-AWS-CloudWatch-Dashboard"

# Deploy the stack
aws cloudformation create-stack \
  --stack-name ${STACK_NAME} \
  --template-body file://template.yaml \
  --region us-east-1 \
  --capabilities CAPABILITY_IAM

# Wait for stack creation to complete (REQUIRED - do not skip this step)
aws cloudformation wait stack-create-complete \
  --stack-name ${STACK_NAME} \
  --region us-east-1
```

**Critical Notes:**
- ⚠️ **Stack naming:** CloudFormation stack names cannot contain underscores. Use hyphens instead.
  - Directory: `test_AWS_CloudWatch_Dashboard` (underscores OK)
  - Stack name: `test-AWS-CloudWatch-Dashboard` (must use hyphens)
- ⚠️ **Always use `aws cloudformation wait`** - This command blocks until CREATE_COMPLETE status
- Use `--capabilities CAPABILITY_IAM` if the stack creates IAM resources
- Use `--capabilities CAPABILITY_NAMED_IAM` if creating named IAM resources
- Some resources may take several minutes to create
- The wait command will timeout after 30 minutes by default

### Step 1.5: Verify Stack Deployment

Verify the stack was created successfully:

```bash
# Check stack status
aws cloudformation describe-stacks \
  --stack-name ${STACK_NAME} \
  --region us-east-1 \
  --query 'Stacks[0].StackStatus'

# Expected output: "CREATE_COMPLETE"

# List stack resources
aws cloudformation list-stack-resources \
  --stack-name ${STACK_NAME} \
  --region us-east-1
```

### Step 1.6: Document Stack Creation

Create a `README.md` in the test directory documenting:

```markdown
# Test Stack: AWS::Backup::BackupPlan

**Created:** 2026-01-11
**Region:** us-east-1
**Stack Name:** test_AWS_Backup_BackupPlan

## Resources Created

- AWS::Backup::BackupVault (prerequisite)
- AWS::Backup::BackupPlan (target resource)

## Deployment

\`\`\`bash
aws cloudformation create-stack \
  --stack-name test_AWS_Backup_BackupPlan \
  --template-body file://template.yaml \
  --region us-east-1 \
  --capabilities CAPABILITY_IAM

aws cloudformation wait stack-create-complete \
  --stack-name test_AWS_Backup_BackupPlan \
  --region us-east-1
\`\`\`

## Outputs

- BackupPlanId: plan-abc123...
- BackupPlanArn: arn:aws:backup:us-east-1:123456789012:backup-plan:...

## Notes

- Backup vault is required prerequisite
- Plan includes daily backup rule
- 30-day retention policy
```

### Stage 1 Completion Criteria

Stage 1 is complete when:
- ✅ Test directory created
- ✅ Checked aws_not_implemented.py (not blocked)
- ✅ Checked aws_no_import.py (import supported) **CRITICAL**
- ✅ Verified resource in aws_dict.py (or noted for Stage 2)
- ✅ Verified get function exists (or noted for Stage 2)
- ✅ CloudFormation template created
- ✅ Stack deployed successfully
- ✅ Stack status is CREATE_COMPLETE
- ✅ Target resource exists
- ✅ README.md documented

**IMPORTANT:** Do not proceed to Stage 2 until Stage 1 is complete.

### Handling Prerequisites

Many CloudFormation resources require prerequisite resources. This is expected and acceptable:

**Common Prerequisites:**
- **IAM Roles** - For Lambda, ECS, etc.
- **VPCs/Subnets** - For network-dependent resources
- **S3 Buckets** - For logging, artifacts
- **KMS Keys** - For encryption
- **Security Groups** - For network resources

**Best Practices:**
1. Create prerequisites in the same template
2. Use minimal configuration for prerequisites
3. Use `!Ref` and `!GetAtt` to reference prerequisites
4. Document all prerequisites in README.md
5. Keep the template as simple as possible

### Troubleshooting Stage 1

**Issue: Stack name validation error**
```
ValidationError: Member must satisfy regular expression pattern: [a-zA-Z][-a-zA-Z0-9]*
```
- **Cause:** Stack name contains underscores
- **Solution:** Replace underscores with hyphens in stack name
- **Example:** `test_AWS_CloudWatch_Dashboard` → `test-AWS-CloudWatch-Dashboard`

**Issue: Stack creation fails**
- Check CloudFormation events: `aws cloudformation describe-stack-events --stack-name <name>`
- Review error messages in the events
- Fix template and retry (delete failed stack first)

**Issue: Resource requires complex prerequisites**
- Start with minimal prerequisites
- Add complexity incrementally
- Document what's required in README.md

**Issue: Resource not available in us-east-1**
- Check AWS service availability
- Try alternative region if necessary
- Document region requirements

**Issue: Wait command times out**
- Check stack status manually: `aws cloudformation describe-stacks --stack-name <name>`
- Some resources take longer than 30 minutes
- Consider using `--no-wait` and checking status separately

### Lessons Learned from Testing

**From AWS::CloudWatch::Dashboard test (2026-01-11):**

1. **Stack Naming Convention**
   - Directory names use underscores: `test_AWS_CloudWatch_Dashboard`
   - Stack names must use hyphens: `test-AWS-CloudWatch-Dashboard`
   - CloudFormation regex pattern: `[a-zA-Z][-a-zA-Z0-9]*`

2. **Wait Command is Critical**
   - Always use `aws cloudformation wait stack-create-complete`
   - This command blocks until CREATE_COMPLETE status
   - Do not proceed to Stage 2 without confirming CREATE_COMPLETE

3. **Simple Resources Work Best**
   - CloudWatch Dashboard had zero dependencies
   - Deployed in seconds
   - Perfect for initial testing

4. **Template Best Practices**
   - Use inline JSON/YAML for simple content (like dashboard body)
   - Add descriptive outputs for verification
   - Include timestamp in resource names for uniqueness

5. **Verification Steps**
   - Use `aws cloudformation describe-stacks` to confirm status
   - Use `aws cloudformation list-stack-resources` to see all resources
   - Check physical resource IDs match expected values

---

## Stage 2: Update stacks.py and Import Stack

### Purpose

Update the stacks.py mapping to use the correct Terraform resource type instead of `aws_null`, then import the CloudFormation stack using aws2tf to generate Terraform configuration.

### Step 2.1: Check PhysicalResourceId Format

Determine whether to use `pid` or `parn` in stacks.py by examining the PhysicalResourceId:

```bash
aws cloudformation describe-stack-resource \
  --stack-name test-AWS-CloudWatch-Dashboard \
  --region us-east-1 \
  --logical-resource-id <LogicalResourceId> \
  --query 'StackResourceDetail.[ResourceType,PhysicalResourceId]' \
  --output table
```

**Decision Rule:**
- If PhysicalResourceId **starts with "arn:"** → Use `parn`
- If PhysicalResourceId **does NOT start with "arn:"** → Use `pid`

**Examples:**
- `test-cloudwatch-dashboard-20260111` → Use `pid`
- `arn:aws:sns:us-east-1:123456789012:my-topic` → Use `parn`

### Step 2.2: Verify Terraform Resource in aws_dict.py

Check if the Terraform resource type is already defined:

```bash
grep "aws_cloudwatch_dashboard" code/fixtf_aws_resources/aws_dict.py
```

**If found:** Note the resource name and proceed to Step 2.3

**If not found:** You must first implement the resource following the standard resource testing procedure in `.kiro/steering/new-resource-testing.md`

### Step 2.3: Update stacks.py Entry

Find and update the CloudFormation resource mapping in `code/stacks.py`:

**Before (placeholder):**
```python
elif type == "AWS::CloudWatch::Dashboard": common.call_resource("aws_null", type+" "+pid)
```

**After (using pid):**
```python
elif type == "AWS::CloudWatch::Dashboard": common.call_resource("aws_cloudwatch_dashboard", pid)
```

**After (using parn - if PhysicalResourceId is an ARN):**
```python
elif type == "AWS::SNS::Topic": common.call_resource("aws_sns_topic", parn)
```

**Important:**
- Use the exact Terraform resource name from aws_dict.py
- Use `pid` or `parn` based on Step 2.1 determination
- Maintain alphabetical ordering in stacks.py

### Step 2.4: Run aws2tf Stack Import

Import the CloudFormation stack:

```bash
cd <workspace_root>
./aws2tf.py -r us-east-1 -t stack -i test-AWS-CloudWatch-Dashboard
```

**Expected Output:**
```
Stage 1 of 10, Terraform Initialise ... PASSED
Stage 2 of 10, Building core resource lists ...
Stage 3 of 10 getting resources ...
...
Stage 7 of 10, Penultimate Terraform Plan ...
Plan: 1 to import, 0 to add, 0 to change, 0 to destroy
...
Stage 10 of 10, Passed post import check - No changes in plan
```

**Success Criteria:**
- ✅ All 10 stages pass
- ✅ Resource is discovered and imported
- ✅ Terraform files generated in `generated/tf-<account>-<region>/`
- ✅ Post-import plan shows 0 changes (no drift)

### Step 2.5: Verify Generated Terraform

Check the generated Terraform configuration:

```bash
ls -la generated/tf-*/aws_cloudwatch_dashboard*.tf
cat generated/tf-*/aws_cloudwatch_dashboard*.tf
```

**Verify:**
- ✅ Resource type matches expected Terraform resource
- ✅ Resource name is based on PhysicalResourceId
- ✅ All properties are captured correctly
- ✅ No syntax errors

### Step 2.6: Validate Post-Import Plan

```bash
cd generated/tf-<account>-<region>
terraform plan
```

**Expected Result:**
```
Plan: 0 to import, 0 to add, 0 to change, 0 to destroy
```

**If plan shows changes:**
- Review what fields are changing
- May need to add handler in `code/fixtf_aws_resources/fixtf_<service>.py`
- May need lifecycle blocks to ignore computed fields
- Document any drift issues

### Stage 2 Completion Criteria

Stage 2 is complete when:
- ✅ PhysicalResourceId format determined (pid vs parn)
- ✅ Terraform resource verified in aws_dict.py
- ✅ Resource added to aws_dict.py dictionary (if missing)
- ✅ Get function created (if missing)
- ✅ stacks.py updated with correct resource mapping
- ✅ aws2tf import completed successfully (all 10 stages passed)
- ✅ Terraform files generated
- ✅ Post-import plan shows 0 changes (or documented drift)
- ✅ Results documented

### Troubleshooting Stage 2

**Issue: "Can not import type: aws_resource_name"**
- **Symptom:** Warning message during import, no import files generated
- **Cause:** Resource is in aws_no_import.py
- **Solution:** 
  - This should have been caught in Stage 1, Step 1.2
  - Delete the stack immediately
  - Move resource to stack-unsupported.md with NO IMPORT SUPPORT status
  - Create TEST_SKIPPED.md documenting why
  - STOP testing this resource

**Issue: "ERROR: clfn is None with type=aws_resource_name"**
- **Symptom:** Import fails with clfn is None error
- **Cause:** Resource not in aws_dict.py dictionary (only defined as variable)
- **Solution:** 
  - Find the resource variable definition in aws_dict.py
  - Add it to the dictionary at the end of the file (alphabetically)
  - Example: `"aws_cloudwatch_contributor_insight_rule": aws_cloudwatch_contributor_insight_rule,`
  - Retry import

**Issue: "Parameter validation failed: Unknown parameter"**
- **Symptom:** boto3 API rejects parameters in get function
- **Cause:** API doesn't support the parameters being used
- **Solution:** 
  - Test API directly with boto3 to find correct parameters
  - Update get function to use correct parameters
  - Some APIs require `maxResults`, others don't support filtering by ID
  - May need to list all and filter manually
  - Example: `describe_query_definitions(maxResults=1000)`

**Issue: Validation fails with "required field is null"**
- **Symptom:** Terraform validation fails: `Must set a configuration value for the X attribute`
- **Cause:** API response field name doesn't match Terraform attribute name
- **Examples:**
  - API returns `Definition`, Terraform expects `rule_definition`
  - API returns `State`, Terraform expects `rule_state`
- **Solution:** 
  - Check API response structure with AWS CLI or boto3
  - Create custom handler in `fixtf_<service>.py` to map fields
  - May require significant handler logic
  - Consider if resource is worth the effort (max 4 attempts)

**Issue: Wrong boto3 client name in aws_dict.py**
- **Symptom:** Get function not called, or API errors
- **Cause:** aws_dict.py has wrong `clfn` value
- **Examples:**
  - `cloudwatch` vs `logs` for CloudWatch Logs resources
  - `cloudwatch` vs `cloudwatch-logs` for some services
- **Solution:**
  - Test with boto3: `boto3.client('<client_name>')`
  - Update `clfn` in aws_dict.py
  - Retry import

**Issue: Resource not found during import**
- Verify stack name matches exactly (use hyphens, not underscores)
- Check region is correct (`-r us-east-1`)
- Verify stack still exists and is in CREATE_COMPLETE state

**Issue: Wrong resource type imported**
- Check stacks.py entry uses correct Terraform resource name
- Verify spelling matches aws_dict.py exactly

**Issue: Post-import plan shows changes**
- Review which fields are changing
- Check if fields are computed/read-only
- May need handler to skip computed fields
- May need lifecycle block to ignore changes
- Document the drift and reason

**Issue: Import fails with "aws_null"**
- Forgot to update stacks.py
- Check that you changed `aws_null` to actual resource type

### Lessons Learned from Testing

**From AWS::CloudWatch::Dashboard test (2026-01-11) - SUCCESS:**

1. **PhysicalResourceId Determines pid vs parn**
   - Dashboard uses dashboard name (simple ID) → Use `pid`
   - SNS Topic uses ARN → Use `parn`
   - Always check before updating stacks.py

2. **Clean Imports Are Possible**
   - CloudWatch Dashboard imported with zero drift
   - No handler needed
   - No lifecycle blocks needed
   - Post-import plan: 0 changes

3. **aws2tf Execution Time**
   - Simple resources: ~45 seconds
   - Includes all 10 stages
   - Most time in Terraform operations

4. **Generated File Naming**
   - Pattern: `aws_<resource>__<physical-id>.tf`
   - Example: `aws_cloudwatch_dashboard__test-cloudwatch-dashboard-20260111.tf`

**From AWS::Logs::QueryDefinition test (2026-01-11) - FAILED (NO IMPORT SUPPORT):**

1. **aws_no_import.py Check is Critical**
   - Should be done in Stage 1, Step 1.2 BEFORE creating stack
   - Saves time by not creating unnecessary stacks
   - QueryDefinition was in aws_no_import.py - caught too late

2. **boto3 Client Name Must Be Correct**
   - aws_dict.py had `cloudwatch` but should be `logs`
   - Wrong client name causes "clfn is None" errors
   - Always verify client name with boto3

3. **API Parameter Requirements Vary**
   - `describe_query_definitions` requires `maxResults` parameter
   - Cannot call without it (returns 0 results)
   - Not all APIs support filtering by ID
   - May need to list all and filter manually

4. **Dictionary Registration Required**
   - Resource variable can exist in aws_dict.py
   - But must also be in the dictionary at the end of the file
   - Missing from dictionary causes "clfn is None" error
   - Always add to dictionary alphabetically

**From AWS::CloudWatch::InsightRule test (2026-01-11) - PARTIAL (Field Mapping Issues):**

1. **Field Name Mapping Issues**
   - API returns `Definition`, Terraform expects `rule_definition`
   - API returns `State`, Terraform expects `rule_state`
   - Requires custom handler to map fields
   - Cannot rely on automatic field mapping

2. **Complex Resources Need Handlers**
   - Some resources need custom field transformation
   - Generic handler may not work for all fields
   - May require multiple iterations to get right
   - Consider effort vs value (max 4 attempts)

3. **Import Can Succeed But Validation Fail**
   - Resource imported successfully
   - Terraform files generated
   - But validation fails due to null required fields
   - Indicates handler is needed

### Quick Fail Criteria

**STOP testing immediately if:**

1. ✅ **Resource in aws_no_import.py** → Mark as NO IMPORT SUPPORT, move to stack-unsupported.md
2. ✅ **Resource in aws_not_implemented.py** → Mark as NOT SUPPORTED, move to stack-unsupported.md
3. ✅ **No Terraform resource exists** → Mark as NO TERRAFORM SUPPORT, move to stack-unsupported.md
4. ✅ **After 4 failed fix attempts** → Document issues, consider marking as complex/deferred

**Do NOT:**
- Create CloudFormation stacks for resources that can't be imported
- Spend excessive time on complex field mapping issues
- Continue after 4 failed attempts per issue

### Stage 2 Decision Tree

When a test fails in Stage 2, follow this decision tree:

```
Import failed?
├─ "Can not import type" → Resource in aws_no_import.py
│  └─ Action: Move to stack-unsupported.md, delete stack, STOP
│
├─ "clfn is None" → Resource not in aws_dict.py dictionary
│  └─ Action: Add to dictionary, retry import
│
├─ "Parameter validation failed" → Wrong API parameters
│  └─ Action: Fix get function parameters, retry import
│
├─ "Validation failed: required field is null" → Field mapping issue
│  └─ Action: Create handler to map fields, retry (max 4 attempts)
│
└─ Other errors → Review logs, fix incrementally (max 4 attempts)
```

---

## Stage 3: Cleanup and Documentation

### Purpose

Clean up test resources and update tracking files to mark the resource as tested.

### Step 3.1: Delete CloudFormation Stack

Delete the test stack:

```bash
aws cloudformation delete-stack \
  --stack-name test-AWS-CloudWatch-Dashboard \
  --region us-east-1

# Wait for deletion to complete (REQUIRED)
aws cloudformation wait stack-delete-complete \
  --stack-name test-AWS-CloudWatch-Dashboard \
  --region us-east-1
```

**Verify Deletion:**
```bash
aws cloudformation describe-stacks \
  --stack-name test-AWS-CloudWatch-Dashboard \
  --region us-east-1
```

**Expected:** `ValidationError: Stack with id ... does not exist`

### Step 3.2: Update Tracking File

Update `code/.automation/to-test-stack.md`:

**Before:**
```markdown
- [ ] `AWS::CloudWatch::Dashboard` <!-- READY: aws_cloudwatch_dashboard can be implemented in aws2tf -->
```

**After:**
```markdown
- [x] `AWS::CloudWatch::Dashboard` <!-- COMPLETED: Test Successful -->
```

### Step 3.3: Document Test Results

Create a summary document in the test directory:

**File:** `code/.automation/test_AWS_CloudWatch_Dashboard/STAGE3_CLEANUP.md`

**Include:**
- Test date and status
- All three stage results
- Key metrics (prerequisites, import success, drift)
- Changes made to aws2tf (stacks.py updates)
- Lessons learned
- Test artifacts and file locations

### Step 3.4: Preserve Test Artifacts

**Keep these files for reference:**
- `template.yaml` - CloudFormation template
- `README.md` - Initial setup documentation
- `STAGE2_RESULTS.md` - Import test results
- `STAGE3_CLEANUP.md` - Final summary

**Optional: Clean up generated Terraform**
```bash
rm -rf generated/tf-<account>-<region>
```

### Stage 3 Completion Criteria

Stage 3 is complete when:
- ✅ CloudFormation stack deleted
- ✅ Stack deletion verified
- ✅ Tracking file updated (marked [x] with COMPLETED comment)
- ✅ Test results documented
- ✅ Test artifacts preserved

### Troubleshooting Stage 3

**Issue: Stack deletion fails**
- Check for resources with deletion protection
- Review stack events for specific errors
- May need to manually delete dependent resources first

**Issue: Stack deletion hangs**
- Some resources take time to delete (up to 30 minutes)
- Check stack status: `aws cloudformation describe-stacks`
- Review DELETE_IN_PROGRESS events

### Complete Test Summary Template

After completing all stages, your test directory should contain:

```
code/.automation/test_AWS_CloudWatch_Dashboard/
├── template.yaml              # CloudFormation template
├── README.md                  # Stage 1 documentation
├── STAGE2_RESULTS.md         # Stage 2 import results
└── STAGE3_CLEANUP.md         # Final summary
```

### Success Metrics

A successful test should achieve:
- ✅ Stack deployed in Stage 1
- ✅ Clean import in Stage 2 (all 10 stages passed)
- ✅ Zero drift (post-import plan: 0 changes)
- ✅ Stack cleaned up in Stage 3
- ✅ Documentation complete

**If drift detected:**
- Document the specific fields causing drift
- Note if handler or lifecycle blocks are needed
- Still mark as COMPLETED if import works (drift can be fixed later)

---

## What is Stack Resource Import?

Stack resource import is a feature that allows aws2tf to discover and import all AWS resources that were created by a CloudFormation stack. Instead of importing resources one-by-one by type, you can import an entire stack's resources at once.

**Key characteristics:**
- Imports resources from **existing, deployed** CloudFormation stacks
- Discovers resources by querying the stack's resource list via CloudFormation API
- Maps CloudFormation resource types (e.g., `AWS::EC2::VPC`) to Terraform resource types (e.g., `aws_vpc`)
- Handles nested stacks automatically
- Some resources are fetched implicitly as part of their parent resources

## How Stack Import Works

The stack import feature is implemented in `code/stacks.py` and works as follows:

1. **Entry Point**: `./aws2tf.py -t stack -i <stack-name>`
2. **Stack Discovery**: Calls `stacks.get_stacks(stack_name)` which:
   - Queries CloudFormation API to get stack resources
   - Discovers nested stacks recursively (up to 2 levels)
   - Builds a list of all stacks to process
3. **Resource Mapping**: For each resource in the stack:
   - Gets the CloudFormation resource type (e.g., `AWS::EC2::VPC`)
   - Maps it to the corresponding Terraform resource type (e.g., `aws_vpc`)
   - Calls `common.call_resource(terraform_type, resource_id)` to import it
4. **Implicit Resources**: Some resources are marked as "fetched implicitly" because they're imported as part of their parent resource

## Prerequisites Check

Before testing stack import for a new CloudFormation resource type:

### 1. Check if CloudFormation Type is Mapped in stacks.py
- Open `code/stacks.py`
- Search for the CloudFormation resource type (e.g., `"AWS::EC2::VPC"`)
- **If not found**: You need to add a mapping in the `getstackresources()` function
- **If found**: Note whether it's:
  - Explicitly imported: `common.call_resource("aws_vpc", pid)`
  - Implicitly imported: `f3.write(type+" "+pid+" fetched as part of parent..\n")`
  - Skipped: `f3.write(type+" "+pid+" skipped ...\n")`
  - Not yet supported: `common.call_resource("aws_null", type+" "+pid)`

### 2. Check if Terraform Resource Type Exists in aws_dict.py
- The Terraform resource type must be defined in `code/fixtf_aws_resources/aws_dict.py`
- If missing, follow the standard resource testing procedure first
- Stack import depends on the underlying resource type being supported

### 3. Understand Resource Dependencies
- Some CloudFormation resources are imported as part of their parent
- Example: `AWS::EC2::SecurityGroupIngress` is fetched as part of `AWS::EC2::SecurityGroup`
- Example: `AWS::Lambda::Permission` is fetched as part of `AWS::Lambda::Function`
- Check `stacks.py` to see if the resource should be implicit or explicit

## CloudFormation Resource Type Patterns

### Pattern A: Explicitly Imported Resources
Resources that are imported individually by aws2tf:
```python
elif type == "AWS::EC2::VPC": common.call_resource("aws_vpc", pid)
elif type == "AWS::Lambda::Function": common.call_resource("aws_lambda_function", pid)
elif type == "AWS::S3::Bucket": common.call_resource("aws_s3_bucket", pid)
```

**Characteristics:**
- Each resource is imported separately
- Uses the physical resource ID from CloudFormation
- Generates individual Terraform resource blocks

### Pattern B: Implicitly Imported Resources
Resources that are imported as part of their parent resource:
```python
elif type == "AWS::EC2::SecurityGroupIngress": f3.write(type+" fetched as part of SecurityGroup..\n")
elif type == "AWS::Lambda::Permission": f3.write(type+" "+pid+" as part of function..\n")
elif type == "AWS::EC2::Route": f3.write(type+" "+pid+" fetched as part of RouteTable...\n")
```

**Characteristics:**
- Not imported separately
- Parent resource's get function fetches these automatically
- Reduces redundant API calls
- Logged to `stack-fetched-implicit.log`

### Pattern C: Skipped Resources
Resources that aws2tf intentionally skips:
```python
elif "AWS::CloudFormation::WaitCondition" in type: f3.write("skipping "+type+"\n")
elif type == "AWS::CDK::Metadata": f3.write(type+" "+pid+" skipped only relevant to CDK .. \n")
```

**Characteristics:**
- Not relevant for Terraform import
- CloudFormation-specific constructs
- Metadata or temporary resources

### Pattern D: Not Yet Supported
Resources that need implementation:
```python
elif type == "AWS::NewService::NewResource": common.call_resource("aws_null", type+" "+pid)
```

**Characteristics:**
- Placeholder for future support
- Logged to `stack-fetched-explicit.log`
- Needs mapping to Terraform resource type

### Pattern E: Custom Resources
CloudFormation custom resources:
```python
elif type == "AWS::CloudFormation::CustomResource": f5.write("Type="+type+ " pid="+pid+ " parn="+parn+"\n")
```

**Characteristics:**
- Logged to `stack-custom-resources.log`
- Cannot be imported (custom Lambda-backed resources)
- Stack-specific implementation

## Testing Steps for Stack Import

### Step 1: Create a Test CloudFormation Stack

Deploy a CloudFormation stack that includes the resource type you want to test:

```bash
# Create a simple CloudFormation template
cat > test-stack-template.yaml << 'EOF'
AWSTemplateFormatVersion: '2010-09-09'
Description: 'Test stack for aws2tf stack import testing'

Resources:
  TestVPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      Tags:
        - Key: Name
          Value: test-stack-vpc
        - Key: Purpose
          Value: aws2tf-testing

  TestSubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref TestVPC
      CidrBlock: 10.0.1.0/24
      AvailabilityZone: !Select [0, !GetAZs '']
      Tags:
        - Key: Name
          Value: test-stack-subnet
EOF

# Deploy the stack
aws cloudformation create-stack \
  --stack-name test-aws2tf-stack-20250111 \
  --template-body file://test-stack-template.yaml \
  --region us-east-1

# Wait for stack creation to complete
aws cloudformation wait stack-create-complete \
  --stack-name test-aws2tf-stack-20250111 \
  --region us-east-1

# Verify stack is created
aws cloudformation describe-stacks \
  --stack-name test-aws2tf-stack-20250111 \
  --region us-east-1 \
  --query 'Stacks[0].StackStatus'
# Should return: "CREATE_COMPLETE"
```

### Step 2: Test Stack Import

Test aws2tf's ability to import all resources from the stack:

```bash
cd <workspace_root>
./aws2tf.py -r us-east-1 -t stack -i test-aws2tf-stack-20250111
```

**Expected behavior:**
- Tool discovers all resources in the stack
- Maps CloudFormation types to Terraform types
- Generates Terraform files in `generated/` directory
- Creates import statements for each resource
- Logs implicit resources to `stack-fetched-implicit.log`
- Logs explicit resources to `stack-fetched-explicit.log`

**Check the logs:**
```bash
# View what was imported explicitly
cat stack-fetched-explicit.log

# View what was imported implicitly
cat stack-fetched-implicit.log

# View any custom resources
cat stack-custom-resources.log
```

### Step 3: Verify Generated Terraform

Check that the generated Terraform is correct:

```bash
cd generated/tf-<timestamp>

# Initialize Terraform
terraform init

# Validate the configuration
terraform validate

# Check the plan (should show resources to import)
terraform plan
```

**Expected results:**
- All stack resources should have corresponding Terraform files
- No validation errors
- Plan should show resources ready to import

### Step 4: Test Nested Stack Handling (Optional)

If testing nested stacks, create a parent stack that includes a nested stack:

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  NestedStack:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: https://s3.amazonaws.com/bucket/nested-template.yaml
```

The stack import should automatically discover and process nested stacks up to 2 levels deep.

### Step 5: Cleanup Stack Resources

**ALWAYS destroy the test stack:**

```bash
# Delete the CloudFormation stack
aws cloudformation delete-stack \
  --stack-name test-aws2tf-stack-20250111 \
  --region us-east-1

# Wait for deletion to complete
aws cloudformation wait stack-delete-complete \
  --stack-name test-aws2tf-stack-20250111 \
  --region us-east-1

# Verify stack is deleted
aws cloudformation describe-stacks \
  --stack-name test-aws2tf-stack-20250111 \
  --region us-east-1
# Should return error: Stack does not exist
```

### Step 6: Document Test Results

Create documentation in `code/.automation/test_stack_<resource_type>/test-results.md`:

```markdown
# Stack Import Test Results: <CloudFormation Resource Type>

**Date:** YYYY-MM-DD HH:MM:SS
**Status:** PASSED/FAILED

## Test Summary
- CloudFormation stack created: ✓
- Stack import executed: ✓
- Resources discovered: ✓
- Terraform generated: ✓
- Terraform validation: ✓
- Cleanup completed: ✓

## Stack Details
- Stack Name: test-aws2tf-stack-20250111
- CloudFormation Resource Type: AWS::EC2::VPC
- Terraform Resource Type: aws_vpc
- Physical Resource ID: vpc-xxxxx
- AWS Region: us-east-1

## Import Behavior
- [ ] Explicitly imported (separate resource)
- [ ] Implicitly imported (part of parent)
- [ ] Skipped (not relevant)
- [ ] Not yet supported (needs implementation)

## Commands Executed
1. aws cloudformation create-stack ...
2. aws cloudformation wait stack-create-complete ...
3. ./aws2tf.py -r us-east-1 -t stack -i test-aws2tf-stack-20250111
4. terraform init && terraform validate
5. aws cloudformation delete-stack ...

## Notes
<Any observations or issues>
```

## Adding Support for New CloudFormation Resource Types

If you need to add support for a new CloudFormation resource type in stack import:

### Step 1: Identify the Mapping

Determine:
1. **CloudFormation type**: e.g., `AWS::NewService::NewResource`
2. **Terraform type**: e.g., `aws_newservice_new_resource`
3. **Physical resource ID format**: What CloudFormation uses as the resource ID

### Step 2: Add Mapping to stacks.py

Add an entry in the `getstackresources()` function in `code/stacks.py`:

```python
elif type == "AWS::NewService::NewResource": 
    common.call_resource("aws_newservice_new_resource", pid)
```

**Placement guidelines:**
- Add alphabetically by AWS service name
- Group related resources together
- Use consistent formatting with existing entries

### Step 3: Determine Import Strategy

Choose the appropriate pattern:

**Explicit Import** (most common):
```python
elif type == "AWS::EC2::VPC": 
    common.call_resource("aws_vpc", pid)
```

**Implicit Import** (resource is part of parent):
```python
elif type == "AWS::EC2::SecurityGroupIngress": 
    f3.write(type+" fetched as part of SecurityGroup..\n")
```

**Skip** (not relevant for Terraform):
```python
elif type == "AWS::CloudFormation::WaitCondition": 
    f3.write("skipping "+type+"\n")
```

**Not Yet Supported** (placeholder):
```python
elif type == "AWS::NewService::NewResource": 
    common.call_resource("aws_null", type+" "+pid)
```

### Step 4: Handle Special ID Formats

Some resources need special handling for their physical resource ID:

**Use ARN instead of ID:**
```python
elif type == "AWS::SNS::Topic": 
    common.call_resource("aws_sns_topic", parn)  # Use parn (ARN) not pid (ID)
```

**Use composite ID:**
```python
elif type == "AWS::ServiceCatalog::PortfolioPrincipalAssociation": 
    tarn = parn.split('|')[0]
    common.call_resource("aws_null", tarn)
```

### Step 5: Test the Mapping

1. Create a CloudFormation stack with the new resource type
2. Run stack import: `./aws2tf.py -r us-east-1 -t stack -i <stack-name>`
3. Verify the resource is discovered and imported correctly
4. Check generated Terraform files
5. Run `terraform validate` to ensure correctness

### Step 6: Document the Mapping

Add comments in `stacks.py` if the mapping is non-obvious:

```python
# Use ARN for SNS topics as Terraform expects ARN for import
elif type == "AWS::SNS::Topic": 
    common.call_resource("aws_sns_topic", parn)
```

## Troubleshooting Stack Import

### Issue: Resource not discovered in stack
**Symptom:** Stack import completes but specific resource is missing
**Solution:** 
- Check if resource type is mapped in `stacks.py`
- Verify resource exists in stack: `aws cloudformation list-stack-resources --stack-name <name>`
- Check if resource is marked as implicit (part of parent)

### Issue: Wrong resource ID used for import
**Symptom:** Import fails with "resource not found" error
**Solution:**
- Check if resource needs ARN (`parn`) instead of ID (`pid`)
- Verify the physical resource ID format in CloudFormation
- Some resources need composite IDs or special formatting

### Issue: Nested stacks not imported
**Symptom:** Only top-level stack resources are imported
**Solution:**
- Nested stacks are automatically discovered up to 2 levels
- Check `stacks.sh` file for nested stack import commands
- Verify nested stack status is CREATE_COMPLETE

### Issue: Resource imported but Terraform validation fails
**Symptom:** Generated Terraform has syntax or reference errors
**Solution:**
- The underlying Terraform resource type may need handler fixes
- Follow standard resource testing procedure for that resource type
- Check if resource has dependencies that weren't imported

### Issue: Stack in CREATE_FAILED state
**Symptom:** Stack import skips failed resources
**Solution:**
- Stack import only processes CREATE_COMPLETE resources
- Failed resources are logged with warnings
- Fix the stack or delete failed resources before importing

### Issue: Custom resources in stack
**Symptom:** Custom resources logged but not imported
**Solution:**
- Custom resources (Lambda-backed) cannot be imported
- They are logged to `stack-custom-resources.log`
- These are stack-specific and don't have Terraform equivalents

## Special Considerations

### 1. Nested Stack Handling
- Stack import automatically discovers nested stacks
- Processes up to 2 levels of nesting
- Generates `stacks.sh` with commands for each nested stack
- Each nested stack is imported separately

### 2. Resource Status Filtering
- Only imports resources with CREATE_COMPLETE status
- Skips resources with CREATE_FAILED status (with warning)
- Ignores resources in transition states

### 3. Implicit vs Explicit Resources
- Many resources are imported as part of their parent
- Example: Security group rules are part of security groups
- Example: Lambda permissions are part of Lambda functions
- This reduces redundant API calls and simplifies import

### 4. Physical Resource IDs
- CloudFormation provides PhysicalResourceId for each resource
- Some resources use ID, others use ARN
- Stack import uses the appropriate identifier for each resource type
- Check `stacks.py` to see which identifier is used (pid vs parn)

### 5. Resource Dependencies
- Stack import doesn't automatically handle cross-resource references
- Generated Terraform may need manual adjustment for dependencies
- Use `common.add_dependancy()` in handlers to auto-import dependencies

### 6. Log Files
Stack import creates several log files:
- `stack-fetched-explicit.log`: Resources imported explicitly
- `stack-fetched-implicit.log`: Resources imported as part of parent
- `stack-custom-resources.log`: Custom resources (cannot import)
- `stacks.sh`: Commands for importing nested stacks

## Testing Checklist for Stack Import

- [ ] CloudFormation stack created successfully
- [ ] Stack status is CREATE_COMPLETE
- [ ] Stack import command executed: `./aws2tf.py -t stack -i <stack-name>`
- [ ] All expected resources discovered
- [ ] CloudFormation types mapped to Terraform types correctly
- [ ] Generated Terraform files exist in `generated/` directory
- [ ] Terraform validation passes (`terraform validate`)
- [ ] Implicit resources logged correctly
- [ ] Explicit resources logged correctly
- [ ] Nested stacks handled (if applicable)
- [ ] Resource IDs are correct (pid vs parn)
- [ ] No import errors in logs
- [ ] Stack deleted cleanly after testing

## Example: Complete Stack Import Test

```bash
# 1. Create CloudFormation template
cat > test-stack.yaml << 'EOF'
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  TestVPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      Tags:
        - Key: Name
          Value: test-vpc
  TestSubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref TestVPC
      CidrBlock: 10.0.1.0/24
      AvailabilityZone: !Select [0, !GetAZs '']
EOF

# 2. Deploy stack
aws cloudformation create-stack \
  --stack-name test-stack-20250111 \
  --template-body file://test-stack.yaml \
  --region us-east-1

aws cloudformation wait stack-create-complete \
  --stack-name test-stack-20250111 \
  --region us-east-1

# 3. Import stack resources
./aws2tf.py -r us-east-1 -t stack -i test-stack-20250111

# 4. Check logs
cat stack-fetched-explicit.log
cat stack-fetched-implicit.log

# 5. Verify generated Terraform
cd generated/tf-*
terraform init
terraform validate

# 6. Cleanup
aws cloudformation delete-stack \
  --stack-name test-stack-20250111 \
  --region us-east-1

aws cloudformation wait stack-delete-complete \
  --stack-name test-stack-20250111 \
  --region us-east-1
```

## Integration with Standard Resource Testing

Stack import testing complements standard resource testing:

1. **Standard Resource Testing** (from `new-resource-testing.md`):
   - Tests individual resource types: `./aws2tf.py -t aws_vpc`
   - Validates aws_dict.py entries
   - Tests get functions and handlers
   - Ensures resource can be imported by type

2. **Stack Import Testing** (this document):
   - Tests CloudFormation → Terraform mapping
   - Validates stacks.py entries
   - Tests bulk import of related resources
   - Ensures resource can be imported from stacks

**When to use each:**
- Use standard testing when adding a new Terraform resource type
- Use stack testing when adding CloudFormation resource type mapping
- Both are needed for complete coverage

**Testing order:**
1. First: Standard resource testing (ensure `aws_vpc` works)
2. Then: Stack import testing (ensure `AWS::EC2::VPC` → `aws_vpc` mapping works)

## Summary

Stack import testing validates that:
1. CloudFormation resource types are correctly mapped to Terraform types in `stacks.py`
2. Resources can be discovered from existing CloudFormation stacks
3. Physical resource IDs are used correctly (pid vs parn)
4. Implicit resources are handled properly (not imported separately)
5. Nested stacks are discovered and processed
6. Generated Terraform is valid and importable

The stack import feature (`./aws2tf.py -t stack -i <stack-name>`) provides a convenient way to import entire CloudFormation stacks into Terraform, making it easier to migrate from CloudFormation to Terraform or to import existing infrastructure that was deployed via CloudFormation.
