#!/usr/bin/env python3
"""
Create missing fixtf_*.py files for boto3 clients that don't have them.

This ensures every boto3 client in aws_dict.py has a corresponding handler file.
"""

import os
import re


# Mapping of boto3 client names to file names (handle special cases)
CLIENT_TO_FILE = {
    'bcm-data-exports': 'bcm_data_exports',
    'bedrock-agent-runtime': 'bedrock_agent_runtime',
    'cloudfront-keyvaluestore': 'cloudfront_keyvaluestore',
    'compute-optimizer': 'compute_optimizer',
    'cost-optimization-hub': 'cost_optimization_hub',
    'devops-guru': 'devops_guru',
    'emr-serverless': 'emrserverless',  # Already exists
    'lex-models': 'lex_models',
    'neptune-graph': 'neptune_graph',
    'payment-cryptography': 'payment_cryptography',
    'pinpoint-email': 'pinpoint_email',
    'pinpoint-sms-voice-v2': 'pinpoint_sms_voice_v2',
    'service-quotas': 'service_quotas',
    'servicecatalog-appregistry': 'servicecatalog_appregistry',
    'timestream-influxdb': 'timestream_influxdb',
    'timestream-query': 'timestream_query',
    'timestream-write': 'timestreamwrite',  # Already exists
    'workspaces-web': 'workspaces_web',
}


def normalize_client_name(client_name):
    """Convert boto3 client name to file name."""
    if client_name in CLIENT_TO_FILE:
        return CLIENT_TO_FILE[client_name]
    return client_name.replace('-', '_')


def create_stub_file(client_name, service_name):
    """Create a stub fixtf_*.py file for a service."""
    
    content = f'''"""
{service_name.upper()} Resource Handlers - Optimized with __getattr__

This file contains {service_name.upper()} resource handlers.
All resources use the default handler via __getattr__.

Auto-generated stub file.
"""

import logging
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# Magic method for backward compatibility with getattr()
# ============================================================================

def __getattr__(name):
\t"""
\tDynamically provide default handler for all {service_name.upper()} resources.
\t
\tThis allows getattr(module, "aws_resource") to work by returning
\tthe default handler for all resources.
\t"""
\tif name.startswith("aws_"):
\t\treturn BaseResourceHandler.default_handler
\traise AttributeError(f"module 'fixtf_{service_name}' has no attribute '{{name}}'")


log.debug(f"{service_name.upper()} handlers: __getattr__ for all resources")
'''
    
    return content


def main():
    """Main function to create missing files."""
    
    # Extract all unique clfn values from aws_dict.py
    with open('code/fixtf_aws_resources/aws_dict.py', 'r') as f:
        content = f.read()
        clfn_values = set(re.findall(r'"clfn":\s*"([^"]+)"', content))
    
    # Check which ones have corresponding fixtf_*.py files
    fixtf_files = [f.replace('fixtf_', '').replace('.py', '') 
                   for f in os.listdir('code/fixtf_aws_resources') 
                   if f.startswith('fixtf_') and f.endswith('.py')]
    
    # Find missing files
    missing = []
    for clfn in sorted(clfn_values):
        normalized = normalize_client_name(clfn)
        if normalized not in fixtf_files:
            missing.append((clfn, normalized))
    
    print(f"Found {len(missing)} missing fixtf_*.py files")
    print()
    
    # Create missing files
    created = []
    for client_name, service_name in missing:
        filepath = f'code/fixtf_aws_resources/fixtf_{service_name}.py'
        
        if os.path.exists(filepath):
            print(f"  ⚠️  {filepath} already exists, skipping")
            continue
        
        content = create_stub_file(client_name, service_name)
        
        with open(filepath, 'w') as f:
            f.write(content)
        
        created.append(filepath)
        print(f"  ✅ Created {filepath}")
    
    print()
    print(f"✅ Created {len(created)} new fixtf_*.py files")
    print()
    print("All boto3 clients now have corresponding handler files!")


if __name__ == '__main__':
    main()
