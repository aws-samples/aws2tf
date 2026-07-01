# Reverted PRs requiring rework: #155 and #158

## Summary

PRs #155 and #158 were reverted during testing on 2026-06-30 due to errors introduced in the full account import (`./aws2tf.py -v`). They need to be reworked before re-merging.

## PR #155 — fix/restore-imported-tf. ( `glob.glob()` + `shutil.copy()`)

**Branch:** `ecukalla/fix/restore-imported-tf`  
**Merge commit:** `18aafa9f`  
**Reverted at:** `52dfe906`

### What it did
Added Python `glob.glob()` + `shutil.copy()` to restore `imported/aws_*.tf` files into the working directory before `terraform plan -generate-config-out`. This replaced a `cp imported/aws_*.tf .` shell command that was a silent no-op because `rc()` doesn't expand globs.

### Why it was reverted
Caused failures during full account import. The copied-back files from `imported/` appear to conflict with or interfere with freshly-generated resources during the plan stages.

### Suggested fix approach
- Investigate which specific files being copied back cause conflicts
- Consider only restoring files for resources that are *referenced* but not being re-imported in the current run
- Add filtering to skip files that already exist (the code had `if not os.path.exists(dst)` but this may not be sufficient)

## Files changed by these PRs

### PR #155
- `code/common.py` (2 blocks in `tfplan1()` and `tfplan3()`)

---

## PR #158 — fix/nat-computed-only-changes

**Branch:** `ecukalla/fix/nat-computed-only-changes`  
**Merge commit:** `e12394d3`  
**Reverted at:** `5ccdc592`

### What it did
Added "computed-only" change detection in `tfplan3()` — identifies plan changes where `before == after` (driven by read-only/computed attributes like `aws_nat_gateway.regional_nat_gateway_address` on provider 6.27+) and treats them as non-consequential.

### Why it was reverted
Reverted during bisection testing while identifying PR #155 as the culprit. PR #158 was not confirmed as causing issues independently, but was not re-tested after #155 was identified. The `fixtf_ec2.py` changes from #158

### Suggested fix approach
- The `computed-only` detection logic in `common.py` may be safe to re-merge independently
- Test in isolation on a full account import after PR #155 is resolved
- The VPN connection handler changes are already covered by PR #160

---



### PR #158
- `code/common.py` (computed-only detection in `tfplan3()`)

