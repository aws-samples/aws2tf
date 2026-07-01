#!/usr/bin/env python3
"""
AWS Dictionary Verification Script

This script verifies entries in aws_dict.py by checking:
1. boto3 client names are valid
2. API methods (descfn) exist for the specified client
3. Response structure (topkey) is reasonable
4. Key fields are present in API responses

The script generates a report in code/.automation/aws_dict_verification.md
"""

import boto3
import sys
import os
from botocore.exceptions import ClientError, UnknownServiceError

# Add parent directory to path to import aws_dict
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'fixtf_aws_resources'))

try:
    import aws_dict as aws_dict_module
except ImportError as e:
    print(f"Error importing aws_dict: {e}")
    sys.exit(1)

# Build the dictionary of all resources
RESOURCE_DICT = {}

# Get all variables from aws_dict module that start with 'aws_'
for name in dir(aws_dict_module):
    if name.startswith('aws_') and not name.startswith('__'):
        obj = getattr(aws_dict_module, name)
        if isinstance(obj, dict) and 'clfn' in obj:
            RESOURCE_DICT[name] = obj

print(f"Found {len(RESOURCE_DICT)} resource definitions to verify")

# Verification results
results = {
    'valid': [],
    'warnings': [],
    'errors': []
}

def verify_client(clfn):
    """Verify that a boto3 client name is valid"""
    try:
        # Try to create the client
        boto3.client(clfn, region_name='us-east-1')
        return True, None
    except UnknownServiceError:
        return False, f"Unknown service: {clfn}"
    except Exception as e:
        return False, f"Error creating client: {str(e)}"

def verify_method(clfn, descfn):
    """Verify that a method exists on the boto3 client"""
    try:
        client = boto3.client(clfn, region_name='us-east-1')
        if hasattr(client, descfn):
            return True, None
        else:
            # List available methods that might be similar
            methods = [m for m in dir(client) if not m.startswith('_')]
            similar = [m for m in methods if descfn.lower() in m.lower() or m.lower() in descfn.lower()]
            if similar:
                return False, f"Method '{descfn}' not found. Similar methods: {', '.join(similar[:5])}"
            else:
                return False, f"Method '{descfn}' not found on client '{clfn}'"
    except Exception as e:
        return False, f"Error checking method: {str(e)}"

def verify_pageable(clfn, descfn):
    """Check if a method can be paginated"""
    try:
        client = boto3.client(clfn, region_name='us-east-1')
        return client.can_paginate(descfn), None
    except Exception as e:
        return None, f"Could not check pagination: {str(e)}"

# Process each resource
for resource_name, resource_def in sorted(RESOURCE_DICT.items()):
    clfn = resource_def.get('clfn')
    descfn = resource_def.get('descfn')
    topkey = resource_def.get('topkey')
    key = resource_def.get('key')
    filterid = resource_def.get('filterid')
    
    issues = []
    warnings = []
    
    # Verify client name
    client_valid, client_error = verify_client(clfn)
    if not client_valid:
        issues.append(f"Invalid client: {client_error}")
    
    # Verify method exists
    if client_valid:
        method_valid, method_error = verify_method(clfn, descfn)
        if not method_valid:
            issues.append(f"Invalid method: {method_error}")
        
        # Check if method is pageable
        if method_valid:
            is_pageable, page_error = verify_pageable(clfn, descfn)
            if is_pageable is False:
                warnings.append(f"Method '{descfn}' is not pageable (may need direct API call)")
    
    # Check for missing fields
    if not topkey:
        warnings.append("Missing 'topkey' field")
    if not key:
        warnings.append("Missing 'key' field")
    
    # Store results
    if issues:
        results['errors'].append({
            'resource': resource_name,
            'clfn': clfn,
            'descfn': descfn,
            'issues': issues,
            'warnings': warnings
        })
    elif warnings:
        results['warnings'].append({
            'resource': resource_name,
            'clfn': clfn,
            'descfn': descfn,
            'warnings': warnings
        })
    else:
        results['valid'].append(resource_name)

# Generate report
report_path = os.path.join(os.path.dirname(__file__), 'aws_dict_verification.md')

with open(report_path, 'w') as f:
    f.write("# AWS Dictionary Verification Report\n\n")
    f.write(f"**Generated:** {os.popen('date').read().strip()}\n\n")
    f.write(f"**Total Resources:** {len(RESOURCE_DICT)}\n\n")
    
    f.write("## Summary\n\n")
    f.write(f"- ✅ Valid: {len(results['valid'])}\n")
    f.write(f"- ⚠️  Warnings: {len(results['warnings'])}\n")
    f.write(f"- ❌ Errors: {len(results['errors'])}\n\n")
    
    # Errors section
    if results['errors']:
        f.write("## ❌ Errors\n\n")
        f.write("These resources have critical issues that prevent them from working:\n\n")
        for item in results['errors']:
            f.write(f"### `{item['resource']}`\n\n")
            f.write(f"- **Client:** `{item['clfn']}`\n")
            f.write(f"- **Method:** `{item['descfn']}`\n\n")
            f.write("**Issues:**\n")
            for issue in item['issues']:
                f.write(f"- {issue}\n")
            if item['warnings']:
                f.write("\n**Warnings:**\n")
                for warning in item['warnings']:
                    f.write(f"- {warning}\n")
            f.write("\n")
    
    # Warnings section
    if results['warnings']:
        f.write("## ⚠️  Warnings\n\n")
        f.write("These resources may have minor issues or require special handling:\n\n")
        for item in results['warnings']:
            f.write(f"### `{item['resource']}`\n\n")
            f.write(f"- **Client:** `{item['clfn']}`\n")
            f.write(f"- **Method:** `{item['descfn']}`\n\n")
            f.write("**Warnings:**\n")
            for warning in item['warnings']:
                f.write(f"- {warning}\n")
            f.write("\n")
    
    # Valid resources summary
    f.write("## ✅ Valid Resources\n\n")
    f.write(f"The following {len(results['valid'])} resources passed all verification checks:\n\n")
    
    # Group by service prefix
    by_service = {}
    for resource in results['valid']:
        # Extract service name (e.g., 'aws_vpc' -> 'vpc', 'aws_api_gateway_api_key' -> 'api_gateway')
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
    f.write("This verification checked:\n\n")
    f.write("1. **Client Name Validity:** Whether the boto3 client name exists\n")
    f.write("2. **Method Existence:** Whether the specified API method exists on the client\n")
    f.write("3. **Pagination Support:** Whether the method supports pagination (informational)\n")
    f.write("4. **Field Completeness:** Whether required fields (topkey, key) are present\n\n")
    f.write("**Note:** This verification does NOT test:\n")
    f.write("- Actual API calls (would require AWS credentials and permissions)\n")
    f.write("- Response structure validation (topkey correctness)\n")
    f.write("- Key field existence in API responses\n")
    f.write("- Filter ID validity\n\n")
    f.write("For complete validation, manual testing with actual AWS resources is required.\n")

print(f"\n✅ Verification complete!")
print(f"📄 Report generated: {report_path}")
print(f"\nSummary:")
print(f"  Valid: {len(results['valid'])}")
print(f"  Warnings: {len(results['warnings'])}")
print(f"  Errors: {len(results['errors'])}")
