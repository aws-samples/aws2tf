# Bulk Resource Testing Plan

This document provides instructions for systematically testing all resources in `to-test.md` following the procedures defined in `.kiro/steering/new-resource-testing.md`.

## Overview

**Goal:** Test all 454 resources in `to-test.md` one by one, moving completed resources to `to-test-completed.md`.

**Process:** This is designed to be **resumable** - you can stop at any time and pick up where you left off in a new session.

## Prerequisites

Before starting:
1. Ensure you have AWS credentials configured
2. Terraform is installed and working
3. Python 3 and boto3 are available
4. You're in the workspace root directory

## Testing Workflow

### Step 1: Select Next Resource

Open `to-test.md` and identify the **first unchecked resource** in the file. This is your current test target.

**Example:**
```markdown
### aws_workspacesweb

**Base Resources (test first):**
- [ ] `aws_workspacesweb_browser_settings`  <-- Start here
- [ ] `aws_workspacesweb_ip_access_settings`
```

### Step 2: Run New Resource Test

Follow the complete testing procedure from `.kiro/steering/new-resource-testing.md`:

**Command to initiate:**
```
Test the resource: aws_<resource_name>
Follow the new resource testing procedure including:
- Prerequisites check
- Create test environment
- Deploy test resources
- Test type-level import
- Test resource-specific import
- Comprehensive configuration test
- Cleanup
- Document results
```

**Important:** Always run the **comprehensive test** (Step 5.8) even if basic tests already passed.

### Step 3: Record Results

After testing completes (success or failure):

#### On Success:

1. **Update to-test-completed.md:**
   - Add the resource with timestamp and status
   - Include link to test directory

2. **Update to-test.md:**
   - Change `- [ ]` to `- [x]` for the completed resource
   - Or remove the line entirely if you prefer

**Example entry for to-test-completed.md:**
```markdown
### aws_workspacesweb

- [x] `aws_workspacesweb_browser_settings` - ✓ PASSED (2025-01-01) - [test results](test_aws_workspacesweb_browser_settings/test-results.md)
```

#### On Failure:

1. **Document in test directory:**
   - Create `test-failed.md` in the test directory
   - Document the failure reason and attempts made

2. **Update to-test.md:**
   - Change `- [ ]` to `- [x]` to mark as attempted
   - Add a note: `(FAILED - see test directory)`

3. **Do NOT add to to-test-completed.md** - only successful tests go there

### Step 4: Commit Progress (Optional but Recommended)

After each successful test, consider committing:
```bash
git add code/.automation/test_<resource_name>/
git add code/.automation/to-test.md
git add code/.automation/to-test-completed.md
git commit -m "Tested: aws_<resource_name> - PASSED"
```

This creates checkpoints you can return to.

### Step 5: Continue or Pause

**To continue:** Return to Step 1 and select the next unchecked resource.

**To pause:** Simply stop. Your progress is saved in:
- Checked boxes in `to-test.md`
- Entries in `to-test-completed.md`
- Test directories in `code/.automation/test_*/`

## Resuming After a Break

When resuming in a new session:

1. **Open `to-test.md`**
2. **Find the first unchecked resource** (or first resource without `[x]`)
3. **Continue from Step 2** of the workflow above

The process is completely resumable because:
- Progress is tracked in markdown files
- Test results are saved in test directories
- Each resource test is independent

## Handling Issues

### Context Window Exhaustion

If you run out of context window during a test:

1. **Note where you stopped** in the current test procedure
2. **In new session, say:**
   ```
   Continue testing aws_<resource_name> from step <X>
   Previous session completed: [list what was done]
   ```

### Resource Limits / Rate Limiting

If you hit AWS rate limits:

1. **Wait 5-10 minutes**
2. **Resume with:** "Continue testing aws_<resource_name>"
3. **Consider adding delays** between tests if this happens frequently

### Test Failures

If a test fails after 4 fix attempts:

1. **Document the failure** in `test-failed.md`
2. **Mark as attempted** in `to-test.md`
3. **Move to next resource** - don't get stuck on one resource

## Progress Tracking

### Check Overall Progress

At any time, run:
```bash
# Count completed
grep -c "^\- \[x\]" code/.automation/to-test.md

# Count remaining
grep -c "^\- \[ \]" code/.automation/to-test.md

# List completed resources
grep "^\- \[x\]" code/.automation/to-test.md
```

### View Completion Rate

```bash
python3 << 'EOF'
with open('code/.automation/to-test.md', 'r') as f:
    content = f.read()
    total = content.count('- [ ]') + content.count('- [x]')
    completed = content.count('- [x]')
    remaining = content.count('- [ ]')
    
print(f"Progress: {completed}/{total} ({100*completed/total:.1f}%)")
print(f"Remaining: {remaining}")
EOF
```

## Service Group Strategy

Resources are organized by service groups. Recommended approach:

1. **Complete one service group at a time** (e.g., all `aws_workspacesweb_*` resources)
2. **Start with base resources** before complex ones (marked in to-test.md)
3. **Skip composite ID resources** (they're in the excluded section)

### Priority Order

Suggested service priority (but you can do any order):

1. **aws_workspacesweb** - Base resources are straightforward
2. **aws_s3** - Common service, good to have working
3. **aws_lambda** - Widely used
4. **aws_iam** - Core service
5. **Continue alphabetically** or by your preference

## Batch Processing Tips

### Testing Multiple Resources in One Session

You can test multiple resources in sequence:

```
Test these resources in order:
1. aws_workspacesweb_browser_settings
2. aws_workspacesweb_ip_access_settings
3. aws_workspacesweb_data_protection_settings

For each resource:
- Run full new resource test including comprehensive test
- Update to-test-completed.md on success
- Mark as [x] in to-test.md
- Continue to next resource
```

### Stopping Mid-Batch

If you need to stop mid-batch:
- The last completed resource will be marked `[x]`
- The in-progress resource may have partial test files
- Next session: Resume from the first unchecked resource

## File Structure

After testing, your `.automation` directory will look like:

```
code/.automation/
├── bulk-to-test-plan.md          (this file)
├── to-test.md                     (resources to test - checked off as completed)
├── to-test-completed.md           (successfully tested resources)
├── to-test-composite.md           (excluded - composite IDs)
├── to-test-deprecated.md          (excluded - deprecated services)
├── test_aws_resource_1/           (test directory)
│   ├── main.tf
│   ├── provider.tf
│   ├── outputs.tf
│   └── test-results.md
├── test_aws_resource_2/
│   └── test-results.md
└── ...
```

## Completion

When all resources are tested:
- All checkboxes in `to-test.md` will be `[x]`
- `to-test-completed.md` will have all successful tests
- Test directories will exist for all resources
- Failed tests will have `test-failed.md` files

## Quick Reference Commands

```bash
# Start testing a resource
"Test aws_<resource_name> following new resource testing procedure"

# Resume after interruption
"Continue testing aws_<resource_name> from step <X>"

# Check progress
grep -c "^\- \[x\]" code/.automation/to-test.md

# View next resource to test
grep -m 1 "^\- \[ \]" code/.automation/to-test.md

# List all completed resources
grep "^\- \[x\]" code/.automation/to-test.md | sed 's/.*`\(.*\)`.*/\1/'
```

## Notes

- **Each test is independent** - you can test resources in any order
- **Service groups are suggestions** - not requirements
- **Comprehensive tests are mandatory** - even if basic tests passed previously
- **Document everything** - future you will thank present you
- **Commit frequently** - creates recovery points
- **Don't rush** - quality over speed

## Getting Help

If you encounter issues:
1. Check `.kiro/steering/new-resource-testing.md` for detailed procedures
2. Review existing test directories for examples
3. Check `to-test-composite.md` if a resource seems to have composite IDs
4. Check `to-test-deprecated.md` if a resource seems outdated

---

**Ready to start?** Open `to-test.md`, find the first `- [ ]` resource, and begin testing!
