#!/usr/bin/env python3
"""
Summarize AWS Dictionary Verification Report

Analyzes aws_dict_verification2.md and produces a summary with error type counts.
"""

import re
import os

print("=" * 70)
print("AWS Dictionary Verification Summary Generator")
print("=" * 70)

report_path = os.path.join(os.path.dirname(__file__), 'aws_dict_verification2.md')
summary_path = os.path.join(os.path.dirname(__file__), 'aws_dict_verification2_summary.md')

print(f"\n📖 Reading report file: {report_path}")
# Read the report
with open(report_path, 'r') as f:
    content = f.read()
print(f"✓ Read {len(content):,} characters from report")

print("\n📊 Extracting summary statistics...")
# Extract summary statistics
summary_match = re.search(r'- ✅ \*\*Valid:\*\* (\d+)', content)
warnings_match = re.search(r'- ⚠️  \*\*Warnings:\*\* (\d+)', content)
errors_match = re.search(r'- ❌ \*\*Errors:\*\* (\d+)', content)
permission_match = re.search(r'- 🔒 \*\*Permission Errors:\*\* (\d+)', content)
api_errors_match = re.search(r'- 🔴 \*\*API Errors:\*\* (\d+)', content)
tested_match = re.search(r'- \*\*Tested:\*\* (\d+)', content)
total_match = re.search(r'- \*\*Total Resources:\*\* (\d+)', content)

valid_count = int(summary_match.group(1)) if summary_match else 0
warnings_count = int(warnings_match.group(1)) if warnings_match else 0
errors_count = int(errors_match.group(1)) if errors_match else 0
permission_count = int(permission_match.group(1)) if permission_match else 0
api_errors_count = int(api_errors_match.group(1)) if api_errors_match else 0
tested_count = int(tested_match.group(1)) if tested_match else 0
total_count = int(total_match.group(1)) if total_match else 0

print(f"  ✓ Valid: {valid_count}")
print(f"  ✓ Warnings: {warnings_count}")
print(f"  ✓ Errors: {errors_count}")
print(f"  ✓ Permission Errors: {permission_count}")
print(f"  ✓ API Errors: {api_errors_count}")
print(f"  ✓ Tested: {tested_count}/{total_count}")

print("\n🔍 Analyzing error types...")
# Count different error types
error_types = {
    'requires_parameters': 0,
    'method_not_found': 0,
    'topkey_incorrect': 0,
    'key_field_missing': 0,
    'permission_denied': 0,
    'api_error': 0
}

print("  → Counting 'requires_parameters' errors...")
# Count requires_parameters errors
requires_params = re.findall(r'Missing required parameter in input: "(\w+)"', content)
error_types['requires_parameters'] = len(set(requires_params))
print(f"    Found {error_types['requires_parameters']} unique parameter requirements")

print("  → Counting 'method_not_found' errors...")
# Count method not found
method_not_found = re.findall(r"Method '(\w+)' not found", content)
error_types['method_not_found'] = len(method_not_found)
print(f"    Found {error_types['method_not_found']} method errors")

print("  → Counting 'topkey_incorrect' errors...")
# Count topkey issues
topkey_issues = re.findall(r"topkey '(\w+)' not found in response", content)
error_types['topkey_incorrect'] = len(topkey_issues)
print(f"    Found {error_types['topkey_incorrect']} topkey errors")

print("  → Counting 'key_field_missing' errors...")
# Count key field issues
key_issues = re.findall(r"key field '(\w+)' not found", content)
error_types['key_field_missing'] = len(key_issues)
print(f"    Found {error_types['key_field_missing']} key field errors")

print("  → Recording permission and API errors...")
# Count permission errors
error_types['permission_denied'] = permission_count

# Count API errors
error_types['api_error'] = api_errors_count
print(f"    Permission errors: {permission_count}, API errors: {api_errors_count}")

print("\n🔎 Extracting resources requiring parameters...")
# Extract specific resources by category
requires_params_resources = []
for match in re.finditer(r'### `(aws_\w+)`.*?Missing required parameter in input: "(\w+)"', content, re.DOTALL):
    resource = match.group(1)
    param = match.group(2)
    # Find all params for this resource
    resource_section = content[match.start():match.start()+500]
    params = re.findall(r'Missing required parameter in input: "(\w+)"', resource_section)
    requires_params_resources.append((resource, params))
print(f"  ✓ Found {len(requires_params_resources)} resources requiring parent IDs")

print(f"\n📝 Generating summary report: {summary_path}")
# Generate summary report - write incrementally
with open(summary_path, 'w') as f:
    print("  → Writing header and overall statistics...")
    f.write("# AWS Dictionary Verification Summary Report\n\n")
    f.write(f"**Source:** aws_dict_verification2.md\n")
    f.write(f"**Generated:** {os.popen('date').read().strip()}\n\n")
    
    f.write("## Overall Statistics\n\n")
    f.write(f"- **Total Resources in aws_dict.py:** {total_count}\n")
    f.write(f"- **Resources Tested:** {tested_count}\n")
    f.write(f"- **Resources Skipped:** {total_count - tested_count}\n\n")
    f.flush()  # Flush to disk
    
    print("  → Writing test results table...")
    f.write("## Test Results\n\n")
    f.write(f"| Category | Count | Percentage |\n")
    f.write(f"|----------|-------|------------|\n")
    f.write(f"| ✅ Valid | {valid_count} | {(valid_count/tested_count*100):.1f}% |\n")
    f.write(f"| ⚠️  Warnings | {warnings_count} | {(warnings_count/tested_count*100):.1f}% |\n")
    f.write(f"| ❌ Errors | {errors_count} | {(errors_count/tested_count*100):.1f}% |\n")
    f.write(f"| 🔒 Permission Errors | {permission_count} | {(permission_count/tested_count*100):.1f}% |\n")
    f.write(f"| 🔴 API Errors | {api_errors_count} | {(api_errors_count/tested_count*100):.1f}% |\n\n")
    f.flush()  # Flush to disk
    
    print("  → Writing error type breakdown...")
    f.write("## Error Type Breakdown\n\n")
    f.write(f"| Error Type | Count | Description |\n")
    f.write(f"|------------|-------|-------------|\n")
    f.write(f"| Requires Parameters | {error_types['requires_parameters']} | Resources needing parent IDs (needid_dict.py) |\n")
    f.write(f"| Method Not Found | {error_types['method_not_found']} | Invalid boto3 method names |\n")
    f.write(f"| Incorrect topkey | {error_types['topkey_incorrect']} | Response structure mismatch |\n")
    f.write(f"| Missing key Field | {error_types['key_field_missing']} | Key field not in API response |\n")
    f.write(f"| Permission Denied | {error_types['permission_denied']} | IAM permissions needed |\n")
    f.write(f"| Other API Errors | {error_types['api_error']} | Various API failures |\n\n")
    f.flush()  # Flush to disk
    
    print("  → Writing priority actions...")
    f.write("## Priority Actions\n\n")
    
    # Priority 1: Method not found
    if error_types['method_not_found'] > 0:
        print(f"    → Priority 1: Method names ({error_types['method_not_found']} resources)...")
        f.write(f"### Priority 1: Fix Method Names ({error_types['method_not_found']} resources)\n\n")
        f.write("These resources have incorrect boto3 method names and need immediate correction:\n\n")
        unique_methods = set(method_not_found)
        total_methods = len(unique_methods)
        print(f"      Processing {total_methods} unique methods...")
        for idx, method in enumerate(unique_methods, 1):
            if idx % 10 == 0 or idx == 1:
                print(f"        [{idx}/{total_methods}] Processing method: {method}")
            resources = re.findall(rf'### `(aws_\w+)`.*?Method \'{method}\' not found', content, re.DOTALL)
            if resources:
                f.write(f"- **Method:** `{method}` - Used by: {', '.join([f'`{r}`' for r in resources[:3]])}")
                if len(resources) > 3:
                    f.write(f" and {len(resources)-3} more")
                f.write("\n")
        print(f"      ✓ Completed all {total_methods} methods")
        f.write("\n")
        f.flush()  # Flush to disk
    
    # Priority 2: Incorrect topkey
    if error_types['topkey_incorrect'] > 0:
        print(f"    → Priority 2: topkey values ({error_types['topkey_incorrect']} resources)...")
        f.write(f"### Priority 2: Fix topkey Values ({error_types['topkey_incorrect']} resources)\n\n")
        f.write("These resources have incorrect topkey values:\n\n")
        unique_topkeys = set(topkey_issues)
        total_topkeys = len(unique_topkeys)
        print(f"      Processing {total_topkeys} unique topkeys...")
        for idx, topkey in enumerate(unique_topkeys, 1):
            if idx % 10 == 0 or idx == 1:
                print(f"        [{idx}/{total_topkeys}] Processing topkey: {topkey}")
            resources = re.findall(rf'### `(aws_\w+)`.*?topkey \'{topkey}\' not found', content, re.DOTALL)
            if resources:
                f.write(f"- **topkey:** `{topkey}` - Used by: {', '.join([f'`{r}`' for r in resources[:3]])}")
                if len(resources) > 3:
                    f.write(f" and {len(resources)-3} more")
                f.write("\n")
        print(f"      ✓ Completed all {total_topkeys} topkeys")
        f.write("\n")
        f.flush()  # Flush to disk
    
    # Priority 3: Missing key fields
    if error_types['key_field_missing'] > 0:
        print(f"    → Priority 3: key fields ({error_types['key_field_missing']} resources)...")
        f.write(f"### Priority 3: Fix key Fields ({error_types['key_field_missing']} resources)\n\n")
        f.write("These resources have incorrect key field names:\n\n")
        unique_keys = set(key_issues)
        total_keys = len(unique_keys)
        print(f"      Processing {total_keys} unique key fields...")
        for idx, key in enumerate(unique_keys, 1):
            if idx % 10 == 0 or idx == 1:
                print(f"        [{idx}/{total_keys}] Processing key: {key}")
            resources = re.findall(rf'### `(aws_\w+)`.*?key field \'{key}\' not found', content, re.DOTALL)
            if resources:
                f.write(f"- **key:** `{key}` - Used by: {', '.join([f'`{r}`' for r in resources[:3]])}")
                if len(resources) > 3:
                    f.write(f" and {len(resources)-3} more")
                f.write("\n")
        print(f"      ✓ Completed all {total_keys} key fields")
        f.write("\n")
        f.flush()  # Flush to disk
    
    # Priority 4: Requires parameters (needid_dict.py updates)
    if requires_params_resources:
        print(f"    → Priority 4: needid_dict.py ({len(requires_params_resources)} resources)...")
        f.write(f"### Priority 4: Update needid_dict.py ({len(requires_params_resources)} resources)\n\n")
        f.write("These resources require parent IDs and should be documented in needid_dict.py:\n\n")
        
        print(f"      Grouping resources by parameter...")
        # Group by parameter name
        by_param = {}
        for resource, params in requires_params_resources:
            param_key = ', '.join(params)
            if param_key not in by_param:
                by_param[param_key] = []
            by_param[param_key].append(resource)
        
        total_param_groups = len(by_param)
        print(f"      Writing {total_param_groups} parameter groups...")
        for idx, (param_key, resources) in enumerate(sorted(by_param.items()), 1):
            if idx % 20 == 0 or idx == 1:
                print(f"        [{idx}/{total_param_groups}] Writing group: {param_key}")
            f.write(f"**Parameter(s): `{param_key}`**\n")
            for resource in resources[:5]:
                f.write(f"- `{resource}`\n")
            if len(resources) > 5:
                f.write(f"- ... and {len(resources)-5} more\n")
            f.write("\n")
        print(f"      ✓ Completed all {total_param_groups} parameter groups")
        f.flush()  # Flush to disk
    
    # Priority 5: Permission errors
    if error_types['permission_denied'] > 0:
        print(f"    → Priority 5: IAM permissions ({error_types['permission_denied']} resources)...")
        f.write(f"### Priority 5: Grant IAM Permissions ({error_types['permission_denied']} resources)\n\n")
        f.write("These resources need IAM permissions. This is NOT an aws_dict.py issue.\n\n")
        f.flush()  # Flush to disk
    
    # Priority 6: Other API errors
    if error_types['api_error'] > 0:
        print(f"    → Priority 6: API errors ({error_types['api_error']} resources)...")
        f.write(f"### Priority 6: Investigate API Errors ({error_types['api_error']} resources)\n\n")
        f.write("These resources have various API errors that need investigation.\n\n")
        f.flush()  # Flush to disk
    
    print("  → Writing quick stats...")
    f.write("## Quick Stats\n\n")
    f.write(f"- **Success Rate:** {(valid_count/tested_count*100):.1f}% of tested resources are fully valid\n")
    f.write(f"- **Issues Requiring aws_dict.py Changes:** {error_types['method_not_found'] + error_types['topkey_incorrect'] + error_types['key_field_missing']}\n")
    f.write(f"- **Issues Requiring needid_dict.py Updates:** {len(requires_params_resources)}\n")
    f.write(f"- **Issues Requiring IAM Permissions:** {error_types['permission_denied']}\n")
    f.write(f"- **Issues Requiring Investigation:** {error_types['api_error']}\n\n")
    f.flush()  # Flush to disk
    
    print("  → Writing next steps...")
    f.write("## Next Steps\n\n")
    f.write("1. **Fix method names** - Update descfn fields for resources with method_not_found errors\n")
    f.write("2. **Fix topkey values** - Update topkey fields based on actual API responses\n")
    f.write("3. **Fix key fields** - Update key fields based on actual API response structure\n")
    f.write("4. **Update needid_dict.py** - Add entries for resources requiring parent IDs\n")
    f.write("5. **Grant permissions** - Add IAM permissions for permission_denied errors\n")
    f.write("6. **Re-run verification** - Confirm all fixes work correctly\n\n")
    f.flush()  # Flush to disk
    
    print("  → Writing detailed breakdown...")
    f.write("## Detailed Breakdown by Error Type\n\n")
    
    # Resources requiring parameters
    if requires_params_resources:
        print(f"    → Listing {len(requires_params_resources)} resources requiring parent IDs...")
        f.write("### Resources Requiring Parent IDs\n\n")
        f.write("These resources need to be added to needid_dict.py:\n\n")
        total_resources = len(requires_params_resources)
        for idx, (resource, params) in enumerate(sorted(requires_params_resources), 1):
            if idx % 50 == 0 or idx == 1:
                print(f"        [{idx}/{total_resources}] Writing resource: {resource}")
            f.write(f"- `{resource}` - Requires: {', '.join([f'`{p}`' for p in params])}\n")
        print(f"      ✓ Completed all {total_resources} resources")
        f.write("\n")
        f.flush()  # Flush to disk

print("\n" + "=" * 70)
print(f"✅ Summary report generated successfully!")
print(f"📄 Output file: {summary_path}")
print("=" * 70)
