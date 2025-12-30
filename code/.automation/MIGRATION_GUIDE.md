# Migration Guide: Refactoring fixtf_*.py Files

## Overview

This guide walks through the automated migration process to refactor all 201 fixtf_*.py files to use the new handler system, reducing code by 86%.

## Prerequisites

✅ Base handler system implemented:
- `code/fixtf_aws_resources/base_handler.py`
- `code/fixtf_aws_resources/handler_registry.py`

✅ Proof of concept tested:
- `code/fixtf_aws_resources/fixtf_ec2_refactored.py`
- `code/fixtf_aws_resources/test_refactored_ec2.py`

## Migration Process

### Step 1: Run Migration Script

This analyzes all fixtf_*.py files and creates refactored versions:

```bash
python3 code/.automation/migrate_fixtf_files.py
```

**What it does:**
- Analyzes each of the 201 fixtf_*.py files
- Identifies functions with custom logic (14%)
- Identifies boilerplate functions (86%)
- Creates `*_refactored.py` versions with only custom logic
- Backs up original files
- Generates migration report

**Output:**
- `code/fixtf_aws_resources/*_refactored.py` - Refactored versions
- `code/fixtf_aws_resources/backup_YYYYMMDD_HHMMSS/` - Backup directory
- `code/.automation/migration_report.md` - Detailed statistics

**Expected results:**
```
Found 201 fixtf_*.py files to migrate

Migrating fixtf_accessanalyzer.py...
  Total functions: 2
  Custom logic: 0
  Boilerplate: 2
  Reduction: 100.0%
  ✅ Created code/fixtf_aws_resources/fixtf_accessanalyzer_refactored.py

Migrating fixtf_ec2.py...
  Total functions: 128
  Custom logic: 24
  Boilerplate: 104
  Reduction: 81.3%
  ✅ Created code/fixtf_aws_resources/fixtf_ec2_refactored.py

...

MIGRATION SUMMARY
Files migrated: 201
Total functions: 1,443
Custom logic functions: 202 (14.0%)
Boilerplate functions: 1,241 (86.0%)
Code reduction: 86.0%
```

### Step 2: Review Refactored Files

Spot-check a few refactored files to ensure quality:

```bash
# Compare original vs refactored
diff code/fixtf_aws_resources/fixtf_s3.py code/fixtf_aws_resources/fixtf_s3_refactored.py

# Check a file with no custom logic
cat code/fixtf_aws_resources/fixtf_accessanalyzer_refactored.py

# Check a file with custom logic
cat code/fixtf_aws_resources/fixtf_lambda_refactored.py
```

**What to look for:**
- ✅ All custom logic functions preserved
- ✅ Boilerplate functions removed
- ✅ Registry imports added
- ✅ Handlers registered at end
- ✅ Valid Python syntax

### Step 3: Test Refactored Files

Run comprehensive tests on all refactored files:

```bash
python3 code/.automation/test_all_refactored.py
```

**What it does:**
- Imports all refactored files
- Verifies valid Python syntax
- Checks handlers are registered
- Tests default and custom handlers
- Generates test report

**Expected output:**
```
Testing 201 refactored files...

✅ accessanalyzer: 0 handlers
✅ ec2: 24 handlers
✅ s3: 5 handlers
✅ lambda: 4 handlers
...

TEST SUMMARY
✅ Successful: 201/201
❌ Failed: 0/201
📊 Total custom handlers: 202

🎉 ALL TESTS PASSED!
```

### Step 4: Replace Original Files

**⚠️ IMPORTANT: Only proceed if all tests pass!**

```bash
python3 code/.automation/replace_original_files.py
```

**What it does:**
1. Verifies all refactored files one more time
2. Creates final backup of all original files
3. Replaces original files with refactored versions
4. Removes temporary `*_refactored.py` files
5. Generates completion report

**Interactive prompts:**
```
Found 201 refactored files

Verifying refactored files...
  ✅ fixtf_accessanalyzer_refactored.py
  ✅ fixtf_ec2_refactored.py
  ...

✅ All refactored files are valid Python

⚠️  WARNING: This will replace all original fixtf_*.py files!

Proceed with replacement? (yes/no): yes

Creating final backup in code/fixtf_aws_resources/backup_final_20250101_120000...
  ✅ Replaced fixtf_accessanalyzer.py
  ✅ Replaced fixtf_ec2.py
  ...

REPLACEMENT COMPLETE
✅ Replaced 201 files
✅ Backup saved to code/fixtf_aws_resources/backup_final_20250101_120000
```

### Step 5: Update Calling Code

Update the code that calls these handlers to use the registry:

**Find calling code:**
```bash
grep -r "getattr.*fixtf_" code/*.py
```

**Before:**
```python
import fixtf_ec2

# Get handler by attribute lookup
handler = getattr(fixtf_ec2, resource_name)
skip, t1, flag1, flag2 = handler(t1, tt1, tt2, flag1, flag2)
```

**After:**
```python
from fixtf_aws_resources.handler_registry import registry

# Get handler from registry
handler = registry.get_handler(resource_name)
skip, t1, flag1, flag2 = handler(t1, tt1, tt2, flag1, flag2)
```

### Step 6: Test Application

Run your application's test suite:

```bash
# Run your existing tests
python3 -m pytest tests/

# Or run manual tests
python3 aws2tf.py --test
```

### Step 7: Rollback (if needed)

If issues occur, restore from backup:

```bash
# Find the backup directory
ls -la code/fixtf_aws_resources/backup_final_*

# Restore all files
cp code/fixtf_aws_resources/backup_final_YYYYMMDD_HHMMSS/*.py code/fixtf_aws_resources/
```

## Migration Scripts Reference

### migrate_fixtf_files.py

**Purpose**: Analyze and create refactored versions

**Usage**: `python3 code/.automation/migrate_fixtf_files.py`

**Output**:
- `*_refactored.py` files
- `backup_YYYYMMDD_HHMMSS/` directory
- `migration_report.md`

**Safe**: Does not modify original files

### test_all_refactored.py

**Purpose**: Test all refactored files

**Usage**: `python3 code/.automation/test_all_refactored.py`

**Output**:
- Console test results
- `test_report.md`

**Safe**: Read-only testing

### replace_original_files.py

**Purpose**: Replace originals with refactored versions

**Usage**: `python3 code/.automation/replace_original_files.py`

**Output**:
- Replaces original files
- Creates `backup_final_YYYYMMDD_HHMMSS/`
- Removes `*_refactored.py` files

**⚠️ DESTRUCTIVE**: Modifies original files (but creates backup)

## Expected Results

### Code Metrics

| Metric | Before | After | Reduction |
|--------|--------|-------|-----------|
| Total functions | 1,443 | ~200 | 86% |
| Lines of code | ~40,000 | ~5,000 | 87% |
| Files | 201 | 203 | +2 (base_handler, registry) |

### File Size Reduction

| File | Before | After | Reduction |
|------|--------|-------|-----------|
| fixtf_ec2.py | ~3,500 lines | ~500 lines | 86% |
| fixtf_s3.py | ~800 lines | ~150 lines | 81% |
| fixtf_lambda.py | ~400 lines | ~100 lines | 75% |
| fixtf_iam.py | ~1,200 lines | ~300 lines | 75% |
| Average | ~200 lines | ~25 lines | 87% |

### Maintenance Impact

- **Before**: Maintain 1,443 functions across 201 files
- **After**: Maintain ~200 functions + 2 base files
- **Effort reduction**: 86%

## Troubleshooting

### Issue: Import errors during migration

**Symptom**: `ImportError: No module named 'common'`

**Solution**: Ensure Python path includes the `code/` directory

### Issue: Syntax errors in refactored files

**Symptom**: `SyntaxError: invalid syntax`

**Solution**: 
1. Check the migration report for the specific file
2. Manually review the function extraction
3. Fix the refactored file
4. Re-run tests

### Issue: Handler not registered

**Symptom**: Custom handler not found in registry

**Solution**:
1. Check the refactored file has `registry.register()` calls
2. Ensure the file is imported
3. Check for typos in resource names

### Issue: Tests fail after replacement

**Symptom**: Application behaves differently

**Solution**:
1. Restore from backup immediately
2. Compare original vs refactored for the failing resource
3. Check if custom logic was incorrectly classified as boilerplate
4. Manually fix the refactored file
5. Re-test before replacing again

## Validation Checklist

Before replacing original files:

- [ ] All 201 files migrated successfully
- [ ] Migration report shows expected statistics
- [ ] All refactored files are valid Python
- [ ] Test script passes for all files
- [ ] Spot-checked 5-10 refactored files manually
- [ ] Backup directory created
- [ ] Ready to proceed with replacement

After replacing original files:

- [ ] Application imports successfully
- [ ] Registry has ~200 custom handlers
- [ ] Application runs without errors
- [ ] Output matches expected results
- [ ] Performance is acceptable
- [ ] Backup is available for rollback

## Timeline

Estimated time for complete migration:

1. **Run migration script**: 2-5 minutes
2. **Review refactored files**: 30-60 minutes
3. **Run tests**: 5-10 minutes
4. **Replace files**: 1 minute
5. **Update calling code**: 30-60 minutes
6. **Test application**: 30-60 minutes

**Total**: 2-3 hours

## Success Criteria

✅ All 201 files refactored  
✅ 86% code reduction achieved  
✅ All tests pass  
✅ Application works correctly  
✅ No functionality lost  
✅ Easier to maintain  
✅ Easier to add new resources  

## Support

If you encounter issues:

1. Check the migration report for statistics
2. Review the test report for failures
3. Examine specific refactored files
4. Restore from backup if needed
5. Manually fix problematic files
6. Re-run migration for specific files

## Next Steps After Migration

1. **Update documentation**: Document the new handler system
2. **Train team**: Ensure team understands new pattern
3. **Add new resources**: Use simplified process
4. **Monitor**: Watch for any issues in production
5. **Iterate**: Improve base handler utilities based on usage

## Rollback Plan

If migration causes issues:

1. **Immediate rollback**:
   ```bash
   cp code/fixtf_aws_resources/backup_final_YYYYMMDD_HHMMSS/*.py code/fixtf_aws_resources/
   ```

2. **Identify issue**: Determine which resource/file caused the problem

3. **Fix refactored version**: Manually correct the issue

4. **Re-test**: Run tests again

5. **Re-migrate**: Replace just the fixed file

## Conclusion

The migration process is:
- ✅ Automated
- ✅ Safe (multiple backups)
- ✅ Tested
- ✅ Reversible
- ✅ Well-documented

Follow the steps carefully and you'll achieve 86% code reduction while maintaining all functionality.
