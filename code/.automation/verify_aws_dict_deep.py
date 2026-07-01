#!/usr/bin/env python3
"""
AWS Dictionary Deep Verification Script

This script performs comprehensive validation of aws_dict.py entries by:
1. Making actual AWS API calls (requires credentials)
2. Validating response structure (topkey correctness)
3. Checking key field existence in API responses
4. Testing pagination support

WARNING: This script makes real AWS API calls and requires:
- Valid AWS credentials configured
- Appropriate IAM permissions for list/describe operations
- May incur minimal AWS costs for API calls
"""

import boto3
import sys
import os
from botocore.exceptions import ClientError, UnknownServiceError, NoCredentialsError
from botocore.config import Config
import time

# Add parent directory to path to import aws_dict
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'fixtf_aws_resources'))

try:
    import aws_dict as aws_dict_module
except ImportError as e:
    print(f"Error importing aws_dict: {e}")
    sys.exit(1)

# Build the dictionary of all resources
RESOURCE_DICT = {}
for name in dir(aws_dict_module):
    if name.startswith('aws_') and not name.startswith('__'):
        obj = getattr(aws_dict_module, name)
        if isinstance(obj, dict) and 'clfn' in obj:
            RESOURCE_DICT[name] = obj

print(f"Found {len(RESOURCE_DICT)} resource definitions to verify")

# Configuration
REGION = 'us-east-1'
MAX_RETRIES = 3
RATE_LIMIT_DELAY = 0.5  # seconds between API calls
TEST_LIMIT = None  # Set to a number to limit testing (e.g., 50 for quick test)

# Resources to skip (add resource names here to skip testing them)
SKIP_RESOURCES = [
    'aws_ami',  # Skip AMI tests (can return large amounts of data)
    'aws_ami_copy',
    'aws_ami_from_instance',
]

# Verification results
results = {
    'valid': [],
    'warnings': [],
    'errors': [],
    'api_errors': [],
    'permission_errors': [],
    'skipped': []
}

# Statistics
stats = {
    'total': 0,
    'tested': 0,
    'api_calls_made': 0,
    'api_calls_failed': 0,
    'topkey_correct': 0,
    'topkey_incorrect': 0,
    'key_field_found': 0,
    'key_field_missing': 0,
}

def test_api_call(clfn, descfn, topkey, key, resource_name):
    """Make actual API call and validate response structure"""
    
    try:
        config = Config(
            retries={'max_attempts': MAX_RETRIES, 'mode': 'standard'},
            region_name=REGION
        )
        client = boto3.client(clfn, config=config)
        
        # Get the method
        if not hasattr(client, descfn):
            return {
                'success': False,
                'error': f"Method '{descfn}' not found on client '{clfn}'",
                'error_type': 'method_not_found'
            }
        
        method = getattr(client, descfn)
        
        # Try to call the method with minimal parameters
        # Some methods require parameters, we'll handle common cases
        required_params = []
        try:
            # Try without parameters first
            response = method()
            stats['api_calls_made'] += 1
        except TypeError as e:
            # Method requires parameters, try common ones
            error_msg = str(e)
            
            # Extract required parameter names from error message
            if 'required positional argument' in error_msg or 'missing' in error_msg.lower():
                # Parse parameter names from error message
                import re
                param_matches = re.findall(r"'(\w+)'", error_msg)
                if param_matches:
                    required_params = param_matches
                
                # Try with MaxResults/Limit for list operations
                try:
                    if 'list' in descfn or 'describe' in descfn:
                        # Try MaxResults (common in newer APIs)
                        try:
                            response = method(MaxResults=10)
                            stats['api_calls_made'] += 1
                        except:
                            # Try Limit (common in older APIs)
                            try:
                                response = method(Limit=10)
                                stats['api_calls_made'] += 1
                            except:
                                # Try maxResults (lowercase variant)
                                try:
                                    response = method(maxResults=10)
                                    stats['api_calls_made'] += 1
                                except:
                                    return {
                                        'success': False,
                                        'error': f"Method requires parameters: {error_msg}",
                                        'error_type': 'requires_parameters',
                                        'required_params': required_params,
                                        'suggestion': 'Method may require parent resource ID or specific parameters'
                                    }
                    else:
                        return {
                            'success': False,
                            'error': f"Method requires parameters: {error_msg}",
                            'error_type': 'requires_parameters',
                            'required_params': required_params
                        }
                except Exception as inner_e:
                    return {
                        'success': False,
                        'error': f"Method requires parameters: {str(inner_e)}",
                        'error_type': 'requires_parameters',
                        'required_params': required_params
                    }
            else:
                raise
        except ClientError as e:
            # Check if it's a parameter validation error
            error_code = e.response['Error']['Code']
            error_msg = e.response['Error']['Message']
            
            if 'Parameter validation failed' in str(e) or 'Missing required parameter' in str(e):
                # Extract parameter names from the error
                import re
                param_matches = re.findall(r'Missing required parameter in input: "(\w+)"', str(e))
                if param_matches:
                    required_params = param_matches
                
                return {
                    'success': False,
                    'error': f"Parameter validation failed: Missing required parameters: {', '.join(required_params)}",
                    'error_type': 'requires_parameters',
                    'required_params': required_params,
                    'suggestion': f'Add to needid_dict.py with required parameters: {required_params}'
                }
            else:
                raise
        
        # Validate response structure
        issues = []
        
        # Check if topkey exists in response
        if topkey:
            if topkey not in response:
                issues.append(f"topkey '{topkey}' not found in response. Available keys: {list(response.keys())}")
                stats['topkey_incorrect'] += 1
                
                # Try to suggest correct topkey (exclude ResponseMetadata as it's never the right key)
                possible_keys = [k for k in response.keys() 
                               if isinstance(response[k], (list, dict)) 
                               and k != 'ResponseMetadata']
                if possible_keys:
                    issues.append(f"Possible correct topkey values: {possible_keys}")
            else:
                stats['topkey_correct'] += 1
                
                # Check if key field exists in the response data
                if key and key != '':
                    topkey_data = response[topkey]
                    
                    # Handle different response structures
                    if isinstance(topkey_data, list) and len(topkey_data) > 0:
                        # Check first item in list
                        first_item = topkey_data[0]
                        if isinstance(first_item, dict):
                            # Handle nested keys (e.g., ".Associations.0.SubnetId")
                            if key.startswith('.'):
                                # Complex nested key - just note it
                                issues.append(f"Complex nested key '{key}' - manual verification needed")
                            elif key not in first_item:
                                issues.append(f"key field '{key}' not found in response items. Available fields: {list(first_item.keys())}")
                                stats['key_field_missing'] += 1
                                
                                # Try to suggest correct key
                                possible_keys = [k for k in first_item.keys() if 'id' in k.lower() or 'name' in k.lower() or 'arn' in k.lower()]
                                if possible_keys:
                                    issues.append(f"Possible correct key values: {possible_keys}")
                            else:
                                stats['key_field_found'] += 1
                        elif isinstance(first_item, str):
                            # List of strings (e.g., cluster names) - this is OK, no issue to report
                            stats['key_field_found'] += 1
                    elif isinstance(topkey_data, dict):
                        # Single object response
                        if key and key not in topkey_data:
                            issues.append(f"key field '{key}' not found in response object. Available fields: {list(topkey_data.keys())}")
                            stats['key_field_missing'] += 1
                        else:
                            stats['key_field_found'] += 1
                    # Empty response - don't report as issue, just note we couldn't validate
                    elif len(topkey_data) == 0:
                        stats['key_field_found'] += 1  # Count as OK since structure is correct
        
        if issues:
            return {
                'success': True,
                'has_issues': True,
                'issues': issues,
                'response_keys': list(response.keys())
            }
        else:
            return {
                'success': True,
                'has_issues': False,
                'response_keys': list(response.keys())
            }
            
    except NoCredentialsError:
        return {
            'success': False,
            'error': 'No AWS credentials found',
            'error_type': 'no_credentials'
        }
    except ClientError as e:
        error_code = e.response['Error']['Code']
        error_msg = e.response['Error']['Message']
        
        if error_code in ['AccessDenied', 'AccessDeniedException', 'UnauthorizedOperation']:
            return {
                'success': False,
                'error': f"Permission denied: {error_msg}",
                'error_type': 'permission_denied',
                'error_code': error_code
            }
        elif error_code in ['InvalidParameterValue', 'InvalidParameter', 'ValidationException']:
            return {
                'success': False,
                'error': f"Invalid parameters: {error_msg}",
                'error_type': 'invalid_parameters',
                'error_code': error_code
            }
        elif error_code in ['Throttling', 'ThrottlingException', 'TooManyRequestsException']:
            stats['api_calls_failed'] += 1
            return {
                'success': False,
                'error': f"Rate limited: {error_msg}",
                'error_type': 'rate_limited',
                'error_code': error_code
            }
        else:
            stats['api_calls_failed'] += 1
            return {
                'success': False,
                'error': f"API error ({error_code}): {error_msg}",
                'error_type': 'api_error',
                'error_code': error_code
            }
    except Exception as e:
        stats['api_calls_failed'] += 1
        return {
            'success': False,
            'error': f"Unexpected error: {str(e)}",
            'error_type': 'unexpected_error'
        }

# Process each resource
print("\nStarting deep verification (making actual API calls)...")
print("This may take several minutes...\n")

# Open report file for incremental writing
report_path = os.path.join(os.path.dirname(__file__), 'aws_dict_verification2.md')
report_file = open(report_path, 'w')

# Write report header
report_file.write("# AWS Dictionary Deep Verification Report\n\n")
report_file.write(f"**Generated:** {os.popen('date').read().strip()}\n")
report_file.write(f"**Region:** {REGION}\n")
report_file.write(f"**Status:** In Progress...\n\n")
report_file.write("## Progress\n\n")
report_file.write("Testing resources... (this section updates as tests run)\n\n")
report_file.write("---\n\n")
report_file.write("## Results\n\n")
report_file.flush()

for idx, (resource_name, resource_def) in enumerate(sorted(RESOURCE_DICT.items())):
    stats['total'] += 1
    
    # Skip resources in skip list
    if resource_name in SKIP_RESOURCES:
        results['skipped'].append({
            'resource': resource_name,
            'reason': 'Skipped - in SKIP_RESOURCES list'
        })
        print(f"[{idx+1}/{len(RESOURCE_DICT)}] Skipping {resource_name} (in skip list)")
        continue
    
    # Limit testing if configured
    if TEST_LIMIT and idx >= TEST_LIMIT:
        results['skipped'].append({
            'resource': resource_name,
            'reason': f'Skipped - test limit reached ({TEST_LIMIT})'
        })
        continue
    
    clfn = resource_def.get('clfn')
    descfn = resource_def.get('descfn')
    topkey = resource_def.get('topkey')
    key = resource_def.get('key')
    
    # Console output for each resource being tested
    print(f"[{idx+1}/{len(RESOURCE_DICT)}] Testing {resource_name}...")
    print(f"    Client: {clfn}, Method: {descfn}")
    
    # Progress summary every 10 resources
    if idx % 10 == 0 and idx > 0:
        progress_msg = f"\n=== Progress Summary: {idx}/{len(RESOURCE_DICT)} ===\n"
        progress_msg += f"  ✅ Valid: {len(results['valid'])}\n"
        progress_msg += f"  ⚠️  Warnings: {len(results['warnings'])}\n"
        progress_msg += f"  ❌ Errors: {len(results['errors'])}\n"
        progress_msg += f"  🔒 Permission: {len(results['permission_errors'])}\n"
        progress_msg += f"  🔴 API Errors: {len(results['api_errors'])}\n"
        print(progress_msg)
        
        # Update progress in file
        report_file.seek(0)
        report_file.write("# AWS Dictionary Deep Verification Report\n\n")
        report_file.write(f"**Generated:** {os.popen('date').read().strip()}\n")
        report_file.write(f"**Region:** {REGION}\n")
        report_file.write(f"**Status:** In Progress - {idx}/{len(RESOURCE_DICT)} tested\n\n")
        report_file.write("## Progress\n\n")
        report_file.write(f"- Tested: {idx}/{len(RESOURCE_DICT)}\n")
        report_file.write(f"- Valid: {len(results['valid'])}\n")
        report_file.write(f"- Warnings: {len(results['warnings'])}\n")
        report_file.write(f"- Errors: {len(results['errors'])}\n")
        report_file.write(f"- Permission Errors: {len(results['permission_errors'])}\n")
        report_file.write(f"- API Errors: {len(results['api_errors'])}\n\n")
        report_file.write("---\n\n")
        report_file.write("## Latest Results\n\n")
        report_file.flush()
    
    # Rate limiting
    if idx > 0:
        time.sleep(RATE_LIMIT_DELAY)
    
    # Test the API call
    result = test_api_call(clfn, descfn, topkey, key, resource_name)
    stats['tested'] += 1
    
    # Write result to file immediately and show in console
    if result['success']:
        if result.get('has_issues'):
            results['warnings'].append({
                'resource': resource_name,
                'clfn': clfn,
                'descfn': descfn,
                'topkey': topkey,
                'key': key,
                'issues': result['issues'],
                'response_keys': result.get('response_keys', [])
            })
            # Console output
            print(f"    ⚠️  WARNING: Structure issues")
            for issue in result['issues']:
                print(f"        - {issue}")
            # Write warning to file
            report_file.write(f"⚠️  **{resource_name}**: Structure issues found\n")
            for issue in result['issues']:
                report_file.write(f"   - {issue}\n")
            report_file.write("\n")
        else:
            results['valid'].append(resource_name)
            print(f"    ✅ VALID")
            report_file.write(f"✅ **{resource_name}**: Valid\n")
    else:
        error_type = result.get('error_type')
        
        if error_type == 'permission_denied':
            results['permission_errors'].append({
                'resource': resource_name,
                'clfn': clfn,
                'descfn': descfn,
                'error': result['error'],
                'error_code': result.get('error_code')
            })
            print(f"    🔒 PERMISSION DENIED: {result.get('error_code')}")
            report_file.write(f"🔒 **{resource_name}**: Permission denied\n")
        elif error_type in ['method_not_found', 'requires_parameters']:
            results['errors'].append({
                'resource': resource_name,
                'clfn': clfn,
                'descfn': descfn,
                'topkey': topkey,
                'key': key,
                'error': result['error'],
                'error_type': error_type,
                'suggestion': result.get('suggestion', ''),
                'required_params': result.get('required_params', [])
            })
            print(f"    ❌ ERROR: {result['error'][:80]}...")
            if result.get('required_params'):
                print(f"        Required params: {', '.join(result['required_params'])}")
            report_file.write(f"❌ **{resource_name}**: {result['error']}\n")
        else:
            results['api_errors'].append({
                'resource': resource_name,
                'clfn': clfn,
                'descfn': descfn,
                'error': result['error'],
                'error_type': error_type,
                'error_code': result.get('error_code', '')
            })
            print(f"    🔴 API ERROR: {error_type}")
            report_file.write(f"🔴 **{resource_name}**: API error\n")
    
    report_file.flush()

# Close the incremental report file
report_file.close()

print(f"\n✅ Deep verification complete!")
print(f"📄 Generating final report...")

# Generate report
report_path = os.path.join(os.path.dirname(__file__), 'aws_dict_verification2.md')

with open(report_path, 'w') as f:
    f.write("# AWS Dictionary Deep Verification Report\n\n")
    f.write(f"**Generated:** {os.popen('date').read().strip()}\n")
    f.write(f"**Region:** {REGION}\n\n")
    
    f.write("## Summary\n\n")
    f.write(f"- **Total Resources:** {stats['total']}\n")
    f.write(f"- **Tested:** {stats['tested']}\n")
    f.write(f"- **Skipped:** {len(results['skipped'])}\n\n")
    
    f.write("### Results\n\n")
    f.write(f"- ✅ **Valid:** {len(results['valid'])} (API call successful, structure correct)\n")
    f.write(f"- ⚠️  **Warnings:** {len(results['warnings'])} (API call successful, but structure issues)\n")
    f.write(f"- ❌ **Errors:** {len(results['errors'])} (Method not found or requires parameters)\n")
    f.write(f"- 🔒 **Permission Errors:** {len(results['permission_errors'])} (Access denied)\n")
    f.write(f"- 🔴 **API Errors:** {len(results['api_errors'])} (Other API failures)\n\n")
    
    f.write("### API Call Statistics\n\n")
    f.write(f"- **API Calls Made:** {stats['api_calls_made']}\n")
    f.write(f"- **API Calls Failed:** {stats['api_calls_failed']}\n")
    f.write(f"- **Success Rate:** {(stats['api_calls_made'] / (stats['api_calls_made'] + stats['api_calls_failed']) * 100) if (stats['api_calls_made'] + stats['api_calls_failed']) > 0 else 0:.1f}%\n\n")
    
    f.write("### Structure Validation\n\n")
    f.write(f"- **topkey Correct:** {stats['topkey_correct']}\n")
    f.write(f"- **topkey Incorrect:** {stats['topkey_incorrect']}\n")
    f.write(f"- **key Field Found:** {stats['key_field_found']}\n")
    f.write(f"- **key Field Missing:** {stats['key_field_missing']}\n\n")
    
    # Errors section
    if results['errors']:
        f.write("## ❌ Errors (Method Issues)\n\n")
        f.write("These resources have method-related issues:\n\n")
        for item in results['errors']:
            f.write(f"### `{item['resource']}`\n\n")
            f.write(f"- **Client:** `{item['clfn']}`\n")
            f.write(f"- **Method:** `{item['descfn']}`\n")
            f.write(f"- **Current topkey:** `{item['topkey']}`\n")
            f.write(f"- **Current key:** `{item['key']}`\n")
            f.write(f"- **Error Type:** `{item['error_type']}`\n")
            if item.get('required_params'):
                f.write(f"- **Required Parameters:** {', '.join([f'`{p}`' for p in item['required_params']])}\n")
            f.write("\n")
            f.write(f"**Error:** {item['error']}\n\n")
            if item.get('suggestion'):
                f.write(f"**Suggestion:** {item['suggestion']}\n\n")
            
            # Add action needed
            if item['error_type'] == 'method_not_found':
                f.write("**Action Needed:**\n")
                f.write("1. Find the correct boto3 method name for this resource\n")
                f.write("2. Update the `descfn` field in aws_dict.py\n")
                f.write("3. Re-run verification to confirm fix\n\n")
            elif item['error_type'] == 'requires_parameters':
                f.write("**Action Needed:**\n")
                f.write("1. This resource requires parent resource ID(s) to list\n")
                if item.get('required_params'):
                    f.write(f"2. Add to needid_dict.py: `\"{item['resource']}\": \"{item['required_params'][0]}\"`\n")
                else:
                    f.write("2. Add to needid_dict.py with appropriate parent parameter\n")
                f.write("3. Ensure get function accepts parent ID parameter\n")
                f.write("4. This is expected behavior - not an error in aws_dict.py\n\n")
    
    # Warnings section
    if results['warnings']:
        f.write("## ⚠️  Warnings (Structure Issues)\n\n")
        f.write("These resources have API calls that succeed but have structure validation issues:\n\n")
        for item in results['warnings']:
            f.write(f"### `{item['resource']}`\n\n")
            f.write(f"- **Client:** `{item['clfn']}`\n")
            f.write(f"- **Method:** `{item['descfn']}`\n")
            f.write(f"- **Current topkey:** `{item['topkey']}`\n")
            f.write(f"- **Current key:** `{item['key']}`\n")
            f.write(f"- **Actual Response Keys:** {', '.join([f'`{k}`' for k in item['response_keys']])}\n\n")
            f.write("**Issues:**\n")
            for issue in item['issues']:
                f.write(f"- {issue}\n")
            f.write("\n")
            
            # Add fix recommendation
            f.write("**Recommended Fix:**\n")
            f.write("```python\n")
            f.write(f"{item['resource']} = {{\n")
            f.write(f"    \"clfn\": \"{item['clfn']}\",\n")
            f.write(f"    \"descfn\": \"{item['descfn']}\",\n")
            
            # Suggest correct topkey based on issues
            if any('topkey' in issue and 'not found' in issue for issue in item['issues']):
                # Extract suggested topkey from issues
                for issue in item['issues']:
                    if 'Possible correct topkey values:' in issue:
                        suggested = issue.split('[')[1].split(']')[0].replace("'", "").split(', ')
                        if suggested:
                            f.write(f"    \"topkey\": \"{suggested[0]}\",  # CHANGED from \"{item['topkey']}\"\n")
                            break
                else:
                    f.write(f"    \"topkey\": \"\",  # CHANGED from \"{item['topkey']}\" - no wrapper key\n")
            else:
                f.write(f"    \"topkey\": \"{item['topkey']}\",\n")
            
            f.write(f"    \"key\": \"{item['key']}\",\n")
            f.write(f"    \"filterid\": \"{item['key']}\"\n")
            f.write("}\n")
            f.write("```\n\n")
    
    # Permission errors section
    if results['permission_errors']:
        f.write("## 🔒 Permission Errors\n\n")
        f.write("These resources require additional IAM permissions:\n\n")
        for item in results['permission_errors']:
            f.write(f"### `{item['resource']}`\n\n")
            f.write(f"- **Client:** `{item['clfn']}`\n")
            f.write(f"- **Method:** `{item['descfn']}`\n")
            f.write(f"- **Error Code:** `{item['error_code']}`\n\n")
            f.write(f"**Error:** {item['error']}\n\n")
            f.write("**Action Needed:**\n")
            f.write("1. Grant IAM permissions for this service\n")
            f.write(f"2. Required permission: `{item['clfn']}:{item['descfn']}`\n")
            f.write("3. Re-run verification after granting permissions\n")
            f.write("4. This is NOT an error in aws_dict.py - configuration is likely correct\n\n")
    
    # API errors section
    if results['api_errors']:
        f.write("## 🔴 API Errors\n\n")
        f.write("These resources encountered API errors:\n\n")
        for item in results['api_errors']:
            f.write(f"### `{item['resource']}`\n\n")
            f.write(f"- **Client:** `{item['clfn']}`\n")
            f.write(f"- **Method:** `{item['descfn']}`\n")
            if item.get('error_code'):
                f.write(f"- **Error Code:** `{item['error_code']}`\n")
            f.write(f"- **Error Type:** `{item['error_type']}`\n\n")
            f.write(f"**Error:** {item['error']}\n\n")
            
            # Add context about what this means
            if 'Missing required parameter' in item['error']:
                f.write("**Action Needed:**\n")
                f.write("1. This resource requires parent resource ID(s) to list\n")
                f.write("2. Verify it's documented in needid_dict.py\n")
                f.write("3. Ensure get function accepts parent ID parameter\n")
                f.write("4. This is expected behavior - not an error in aws_dict.py\n\n")
            else:
                f.write("**Action Needed:**\n")
                f.write("1. Investigate the API error\n")
                f.write("2. May need different parameters or approach\n")
                f.write("3. Check AWS documentation for this API method\n\n")
    
    # Valid resources summary
    f.write("## ✅ Valid Resources\n\n")
    f.write(f"The following {len(results['valid'])} resources passed all validation checks:\n\n")
    
    # Group by service prefix
    by_service = {}
    for resource in results['valid']:
        parts = resource.split('_')
        if len(parts) >= 2:
            service = '_'.join(parts[1:3]) if len(parts) > 2 else parts[1]
            if service not in by_service:
                by_service[service] = []
            by_service[service].append(resource)
    
    for service in sorted(by_service.keys()):
        f.write(f"### {service}\n\n")
        for resource in sorted(by_service[service]):
            f.write(f"- `{resource}`\n")
        f.write("\n")
    
    f.write("## Verification Details\n\n")
    f.write("This deep verification performed:\n\n")
    f.write("1. **Actual API Calls:** Made real AWS API calls to validate methods work\n")
    f.write("2. **Response Structure Validation:** Checked that topkey exists in responses\n")
    f.write("3. **Key Field Validation:** Verified that key fields exist in response items\n")
    f.write("4. **Error Handling:** Categorized different types of failures\n\n")
    
    f.write("### Limitations\n\n")
    f.write("- Some methods require specific parameters (parent resource IDs) that couldn't be tested\n")
    f.write("- Permission errors may indicate missing IAM permissions rather than incorrect configuration\n")
    f.write("- Empty responses (no resources in account) prevent key field validation\n")
    f.write("- Rate limiting may cause some tests to fail\n\n")
    
    f.write("### Recommendations\n\n")
    f.write("1. **Fix Errors First:** Address resources with method not found errors\n")
    f.write("2. **Review Warnings:** Update topkey and key fields based on actual API responses\n")
    f.write("3. **Grant Permissions:** Add IAM permissions for resources with permission errors\n")
    f.write("4. **Retest:** Run verification again after fixes to confirm improvements\n\n")
    
    # Add machine-readable fixes section
    f.write("## Automated Fixes\n\n")
    f.write("This section provides machine-readable fix data for automated correction:\n\n")
    
    if results['warnings']:
        f.write("### Structure Fixes Needed\n\n")
        f.write("```python\n")
        f.write("# Copy these fixes into a fix script or apply manually\n")
        f.write("STRUCTURE_FIXES = {\n")
        for item in results['warnings']:
            # Only include if there's an actual topkey issue
            if any('topkey' in issue and 'not found' in issue for issue in item['issues']):
                f.write(f"    '{item['resource']}': {{\n")
                f.write(f"        'current_topkey': '{item['topkey']}',\n")
                
                # Extract suggested topkey
                suggested_topkey = ""
                for issue in item['issues']:
                    if 'Possible correct topkey values:' in issue:
                        suggested = issue.split('[')[1].split(']')[0].replace("'", "").split(', ')
                        if suggested:
                            suggested_topkey = suggested[0]
                            break
                
                if suggested_topkey:
                    f.write(f"        'correct_topkey': '{suggested_topkey}',\n")
                else:
                    f.write(f"        'correct_topkey': '',  # No wrapper key\n")
                
                f.write(f"        'clfn': '{item['clfn']}',\n")
                f.write(f"        'descfn': '{item['descfn']}',\n")
                f.write(f"        'key': '{item['key']}'\n")
                f.write(f"    }},\n")
        f.write("}\n")
        f.write("```\n\n")
    
    if results['errors']:
        f.write("### Method Fixes Needed\n\n")
        f.write("```python\n")
        f.write("# These resources need method name corrections\n")
        f.write("METHOD_FIXES = {\n")
        for item in results['errors']:
            if item['error_type'] == 'method_not_found':
                f.write(f"    '{item['resource']}': {{\n")
                f.write(f"        'current_method': '{item['descfn']}',\n")
                f.write(f"        'correct_method': 'NEEDS_INVESTIGATION',  # Check boto3 docs\n")
                f.write(f"        'clfn': '{item['clfn']}',\n")
                f.write(f"        'topkey': '{item['topkey']}',\n")
                f.write(f"        'key': '{item['key']}'\n")
                f.write(f"    }},\n")
        f.write("}\n")
        f.write("```\n\n")
    
    # Add needid_dict updates section
    needs_parent_id = [item for item in results['errors'] + results['api_errors'] 
                       if item.get('error_type') == 'requires_parameters' 
                       and item.get('required_params')]
    
    if needs_parent_id:
        f.write("### needid_dict.py Updates Needed\n\n")
        f.write("These resources require parent resource IDs and should be added to needid_dict.py:\n\n")
        f.write("```python\n")
        f.write("# Add these entries to code/fixtf_aws_resources/needid_dict.py\n")
        f.write("NEEDID_ADDITIONS = {\n")
        for item in needs_parent_id:
            params = item.get('required_params', [])
            if params:
                f.write(f"    '{item['resource']}': {{\n")
                f.write(f"        'required_params': {params},\n")
                f.write(f"        'clfn': '{item['clfn']}',\n")
                f.write(f"        'descfn': '{item['descfn']}',\n")
                f.write(f"        'topkey': '{item.get('topkey', '')}',\n")
                f.write(f"        'key': '{item.get('key', '')}'\n")
                f.write(f"    }},\n")
        f.write("}\n")
        f.write("```\n\n")
        
        f.write("**How to use this information:**\n\n")
        f.write("1. Review each resource's required parameters\n")
        f.write("2. Add entry to `code/fixtf_aws_resources/needid_dict.py` if not already present\n")
        f.write("3. Update the get function to accept parent ID parameter\n")
        f.write("4. Example format in needid_dict.py:\n")
        f.write("```python\n")
        f.write('"aws_api_gateway_authorizer": "restApiId",  # Requires REST API ID\n')
        f.write("```\n\n")

print(f"📄 Report generated: {report_path}")
print(f"\nSummary:")
print(f"  Valid: {len(results['valid'])}")
print(f"  Warnings: {len(results['warnings'])}")
print(f"  Errors: {len(results['errors'])}")
print(f"  Permission Errors: {len(results['permission_errors'])}")
print(f"  API Errors: {len(results['api_errors'])}")
print(f"  API Calls Made: {stats['api_calls_made']}")
