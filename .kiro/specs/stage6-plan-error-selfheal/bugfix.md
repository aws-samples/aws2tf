# Bugfix Requirements Document

## Introduction

The Stage 6 `tfplan1()` function in `code/terraform_runner.py` has a broken error detection mechanism that prevents all self-healing logic from ever executing. The string match `'@level": "error"'` includes a space after the colon that never appears in Terraform's compact `-json` output (`"@level":"error"`). This means unrecoverable plan errors (non-existent remote objects, VPC Lattice 404s, AccessDenied) are never detected or removed, causing Stage 7 to abort the entire run. Additionally, the message parsing logic reads the "next line" (`f2.readline()`) expecting multi-line output, but Terraform JSON output is one complete JSON object per line — so the message extraction and `split('(')` parsing is also broken.

The fix must be surgical: only genuinely unrecoverable errors should trigger file removal. Config-generation errors (`Conflicting configuration arguments`, `Missing required argument`) are recoverable via `fixtf` and must NOT trigger removal.

## Bug Analysis

### Current Behavior (Defect)

1.1 WHEN `plan1.json` contains Terraform JSON error lines (compact format `"@level":"error"`) THEN the system never detects them because the string match `'@level": "error"'` includes a spurious space that never appears in Terraform's compact JSON output

1.2 WHEN a plan1 error line contains `"Cannot import non-existent remote object"` THEN the system never removes the corresponding import file because error detection at 1.1 never triggers

1.3 WHEN a plan1 error line contains a VPC Lattice 404 error THEN the system never removes the corresponding import file because error detection at 1.1 never triggers

1.4 WHEN the error detection block fires (hypothetically) THEN the message parsing reads the next line via `f2.readline()` instead of parsing the current JSON line, extracting no useful resource address since Terraform JSON output is one object per line

1.5 WHEN the generic error handler [p3] fires THEN it removes import files for ALL errors including recoverable config-generation errors (`Conflicting configuration arguments`, `Missing required argument`) that `fixtf` can repair in subsequent iterations

1.6 WHEN many non-existent remote object errors accumulate undetected in Stage 6 THEN Stage 7 encounters them all at once and aborts the entire run with `exit 021`

### Expected Behavior (Correct)

2.1 WHEN `plan1.json` contains Terraform JSON error lines THEN the system SHALL parse each line as JSON and detect errors by checking the `@level` field equals `"error"`

2.2 WHEN a parsed error line contains `"Cannot import non-existent remote object"` in the `@message` or `diagnostic.detail` field THEN the system SHALL extract the resource address from the JSON diagnostic structure and move the corresponding `import__*.tf` file to `notimported/`

2.3 WHEN a parsed error line contains a VPC Lattice 404 error THEN the system SHALL extract the resource address from the JSON diagnostic structure and move the corresponding `import__*.tf` file to `notimported/`

2.4 WHEN a parsed error line contains an AccessDenied or read failure error THEN the system SHALL extract the resource address from the JSON diagnostic structure and move the corresponding `import__*.tf` file to `notimported/`

2.5 WHEN a parsed error line contains a recoverable config-generation error (`Conflicting configuration arguments`, `Missing required argument`, or similar) THEN the system SHALL NOT remove the import file, allowing `fixtf` to repair it in subsequent iterations

2.6 WHEN unrecoverable errors are detected and their import files removed THEN the system SHALL log each removal with the error category ([p1], [p2], or [p3]) and resource identifier, and the run SHALL continue past Stage 6 without aborting at Stage 7

### Unchanged Behavior (Regression Prevention)

3.1 WHEN `plan1.json` contains no error lines THEN the system SHALL CONTINUE TO proceed normally through the plan1 phase without modifications

3.2 WHEN `plan1.json` contains only recoverable config-generation errors THEN the system SHALL CONTINUE TO leave all import files in place for `fixtf` to repair in subsequent iterations

3.3 WHEN an import file is moved to `notimported/` THEN the system SHALL CONTINUE TO add the resource identifier to `context.badlist` to track removed resources

3.4 WHEN errors are detected THEN the system SHALL CONTINUE TO log error details and preserve `plan1.json` for debugging

3.5 WHEN no `import*.tf` files exist THEN the system SHALL CONTINUE TO exit with the appropriate message about no files to import

3.6 WHEN `move_to_notimported()` is called THEN the system SHALL CONTINUE TO use the existing glob-based file move implementation from PR #164

---

## Bug Condition (Formal)

```pascal
FUNCTION isBugCondition(X)
  INPUT: X of type Plan1JsonLine
  OUTPUT: boolean
  
  // Returns true when the line is an error line in Terraform's compact JSON format
  RETURN X.contains('"@level":"error"') AND (
    X.contains("Cannot import non-existent remote object") OR
    X.contains("VPC Lattice") AND X.contains("404") OR
    X.contains("AccessDenied")
  )
END FUNCTION
```

```pascal
// Property: Fix Checking - Unrecoverable errors are detected and self-healed
FOR ALL X WHERE isBugCondition(X) DO
  result ← tfplan1'(X)
  ASSERT error_detected(result) = true
  ASSERT resource_address_extracted(result) != ""
  ASSERT import_file_moved_to_notimported(result) = true
END FOR
```

```pascal
// Property: Preservation Checking - Recoverable errors are NOT removed
FOR ALL X WHERE NOT isBugCondition(X) AND X.contains('"@level":"error"') DO
  // Recoverable errors (config-generation) must not trigger removal
  ASSERT F(X) = F'(X)  // No import files removed
END FOR
```

```pascal
// Property: Preservation Checking - Non-error lines unchanged
FOR ALL X WHERE NOT X.contains('"@level":"error"') DO
  ASSERT F(X) = F'(X)  // Behavior identical for non-error lines
END FOR
```
