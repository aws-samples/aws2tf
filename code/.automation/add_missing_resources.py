#!/usr/bin/env python3
"""
Systematically add missing resources to aws_dict_extended.py
This script will research each resource and add proper boto3 mappings
"""

# New resources to add with their boto3 mappings
# Format: resource_name: {clfn, descfn, topkey, key, filterid}

new_resources = {}

# 1. aws_account_region - Uses EC2 describe_regions
new_resources['aws_account_region'] = {
    "clfn": "ec2",
    "descfn": "describe_regions",
    "topkey": "Regions",
    "key": "RegionName",
    "filterid": "RegionName"
}

# 2. aws_alb - This is an alias for aws_lb (Application Load Balancer)
new_resources['aws_alb'] = {
    "clfn": "elbv2",
    "descfn": "describe_load_balancers",
    "topkey": "LoadBalancers",
    "key": "LoadBalancerArn",
    "filterid": "Names"
}

print(f"Prepared {len(new_resources)} new resources")
print("Resources to add:")
for name in new_resources:
    print(f"  - {name}")
