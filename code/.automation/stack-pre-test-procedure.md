# Stack Resource PRE-TEST Procedure

This document defines the PRE-TEST assessment procedure for CloudFormation stack resources before full implementation testing.

## Purpose

The PRE-TEST stage filters CloudFormation resources to identify which ones can actually be implemented in aws2tf by checking:
1. Terraform AWS provider support
2. aws2tf implementation status
3. Terraform import capability

## When to Run PRE-TEST

Run PRE-TEST when explicitly asked to perform:
- "pretest"
- "pre test" 
- "PRE TEST"
- "pre-test"

## PRE-TEST Procedure

For each CloudFormation resource type in `code/.automation/to-test-stack.md` that is currently marked as `- [ ]` (unchecked):

### Step 1: Extract Resource Information

From the CloudFormation resource type (e.g., `AWS::Bedrock::Agent`):
- Service: `Bedrock`
- Resource: `Agent`
- Expected Terraform resource name: `aws_bedrock_agent`

### Step 2: Check Terraform AWS Provider Support

Search the Terraform AWS Provider documentation:
```
https://registry.terraform.io/providers/hashicorp/aws/latest/docs
```

**If Terraform resource DOES NOT exist:**
1. Mark the resource as tested: `- [x]`
2. Add comment: `<!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->`
3. Move to next resource in the list

**Example:**
```markdown
- [x] `AWS::Bedrock::Agent` <!-- NO TERRAFORM SUPPORT: Terraform AWS provider does not have an equivalent resource -->
```

### Step 3: Check aws2tf Support Status

If Terraform resource exists, check if aws2tf supports it:

**Check aws_not_implemented.py:**
```bash
grep "aws_bedrock_agent" code/fixtf_aws_resources/aws_not_implemented.py
```

**If found and UNCOMMENTED (enabled):**
- Resource is marked as not implemented in aws2tf
- Mark as tested: `- [x]`
- Add comment: `<!-- NOT SUPPORTED: aws_bedrock_agent is in aws_not_implemented.py -->`
- Move to next resource

**Example:**
```markdown
- [x] `AWS::Bedrock::Agent` <!-- NOT SUPPORTED: aws_bedrock_agent is in aws_not_implemented.py -->
```

**Check aws_no_import.py:**
```bash
grep "aws_bedrock_agent" code/fixtf_aws_resources/aws_no_import.py
```

**If found and UNCOMMENTED (True):**
- Resource cannot be imported via Terraform
- Mark as tested: `- [x]`
- Add comment: `<!-- NO IMPORT SUPPORT: aws_bedrock_agent - Terraform does not support importing this resource type -->`
- Move to next resource

**Example:**
```markdown
- [x] `AWS::Bedrock::Agent` <!-- NO IMPORT SUPPORT: aws_bedrock_agent - Terraform does not support importing this resource type -->
```

### Step 4: Mark as Ready for Implementation

**If Terraform resource exists AND aws2tf does not block it:**
- Mark as tested: `- [x]`
- Add comment: `<!-- READY: aws_bedrock_agent can be implemented in aws2tf -->`

**Example:**
```markdown
- [x] `AWS::Bedrock::Agent` <!-- READY: aws_bedrock_agent can be implemented in aws2tf -->
```

## PRE-TEST Completion

**CRITICAL:** When you reach the end of the resource list in `code/.automation/to-test-stack.md` during PRE-TEST:

**STOP IMMEDIATELY. DO NOT PROCEED FURTHER.**

The PRE-TEST stage is complete. Report:
1. Total resources assessed
2. Count by status:
   - NO TERRAFORM SUPPORT
   - NOT SUPPORTED (aws_not_implemented.py)
   - NO IMPORT SUPPORT (aws_no_import.py)
   - READY for implementation
3. Summary saved to `code/.automation/to-test-stack.md`

## PRE-TEST Example Workflow

```bash
# Resource: AWS::Bedrock::Agent
# Step 1: Expected Terraform name: aws_bedrock_agent

# Step 2: Check Terraform docs
# Result: Resource exists at https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/bedrock_agent

# Step 3: Check aws2tf support
grep "aws_bedrock_agent" code/fixtf_aws_resources/aws_not_implemented.py
# Result: Not found - not blocked

grep "aws_bedrock_agent" code/fixtf_aws_resources/aws_no_import.py  
# Result: Not found - import is supported

# Step 4: Mark as READY
# Update to-test-stack.md:
# - [x] `AWS::Bedrock::Agent` <!-- READY: aws_bedrock_agent can be implemented in aws2tf -->
```

## Automated PRE-TEST Script

An automated script is available at `code/.automation/run_pretest.py` that performs the PRE-TEST assessment for all resources:

```bash
python3 code/.automation/run_pretest.py
```

This script will:
1. Read all resources from `to-test-stack.md`
2. Check each resource against Terraform and aws2tf support
3. Update the file with appropriate status comments
4. Generate statistics report
5. Split resources into READY and unsupported files

## Output Files

After running PRE-TEST:

1. **`to-test-stack.md`** - Contains only READY resources (can be implemented)
2. **`stack-unsupported.md`** - Contains unsupported resources with reasons

## Status Categories

| Status | Meaning | Action |
|--------|---------|--------|
| **NO TERRAFORM SUPPORT** | Terraform AWS provider doesn't have this resource | Wait for Terraform provider update |
| **NOT SUPPORTED** | In aws_not_implemented.py | Can be implemented following standard procedure |
| **NO IMPORT SUPPORT** | In aws_no_import.py | Cannot be imported, only created |
| **READY** | Can be implemented | Follow stack resource testing procedure |

## Next Steps After PRE-TEST

Once PRE-TEST is complete and resources are marked as READY:
1. Refer to `.kiro/steering/stack-resource-testing.md` for full testing procedure
2. Prioritize resources based on user demand and service adoption
3. Follow the implementation checklist in `to-test-stack.md`
