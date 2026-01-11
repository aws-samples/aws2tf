# Stack Resource Testing Procedure

This document defines the testing procedure for importing resources from existing AWS CloudFormation stacks using the aws2tf tool's stack import feature (`./aws2tf.py -t stack -i <stack-name>`).

**Note:** Before testing stack resources, you may want to run the PRE-TEST assessment. See `code/.automation/stack-pre-test-procedure.md` for details.

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
