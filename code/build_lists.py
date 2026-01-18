"""
AWS Resource List Building Module

This module builds lists of AWS resources using parallel API calls via ThreadPoolExecutor.
It discovers core resources (VPCs, Lambda functions, S3 buckets, etc.) and stores them
in the context module for later processing.

Thread Safety Notes:
- Dictionary updates (context.vpclist[id] = True) are GIL-protected and thread-safe
- Attribute assignments (context.vpcs = response) happen in separate threads
- Each fetch function writes to different context attributes (no conflicts)
- Assumption: No two fetch functions write to the same context attribute
"""

import boto3
import context
import concurrent.futures
import json
import datetime
import logging
from botocore.config import Config
from tqdm import tqdm

log = logging.getLogger('aws2tf')

# Boto3 retry configuration for resilience
BOTO3_RETRY_CONFIG = Config(
    retries={'max_attempts': 10, 'mode': 'standard'}
)


def build_lists():
    log.info("Stage 2 of 10, Building core resource lists ...")
    context.tracking_message="Stage 2 of 10, Building core resource lists ..."
    
    
    
    def fetch_lambda_data():
        try:
            client = boto3.client('lambda', config=BOTO3_RETRY_CONFIG)
            response = []
            paginator = client.get_paginator('list_functions')
            for page in paginator.paginate():
                response.extend(page['Functions'])
            return {
                'resource_type': 'lambda',
                'items': [{'id': j['FunctionName'], 'data': j} for j in response],
                'metadata': {}
            }
        except Exception as e:
            log.error("Error fetching Lambda data: %s", e)
            return {'resource_type': 'lambda', 'items': [], 'metadata': {}}
      
    
    def fetch_vpc_data():
        try:
            client = boto3.client('ec2', config=BOTO3_RETRY_CONFIG)
            response = []
            paginator = client.get_paginator('describe_vpcs')
            for page in paginator.paginate():
                response.extend(page['Vpcs'])
            context.vpcs = response
            return {
                'resource_type': 'vpc',
                'items': [{'id': j['VpcId'], 'data': j} for j in response],
                'metadata': {'full_data': response}
            }
        except Exception as e:
            log.error("Error fetching ec2 data: %s", e)
            return {'resource_type': 'vpc', 'items': [], 'metadata': {}}
    
    def fetch_s3_data():
        try:
            client = boto3.client('s3', config=BOTO3_RETRY_CONFIG)
            response = []
            paginator = client.get_paginator('list_buckets')
            for page in paginator.paginate(BucketRegion=context.region):
                response.extend(page['Buckets'])
            
            # Validate buckets in this thread (parallel execution)
            validated_items = []
            for bucket_data in response:
                bucket_name = bucket_data['Name']
                try:
                    # Validate bucket is accessible
                    client.list_objects_v2(Bucket=bucket_name, MaxKeys=1)
                    validated_items.append({'id': bucket_name, 'data': bucket_data})
                except Exception as e:
                    log.debug("S3 bucket %s not accessible: %s", bucket_name, e)
                    continue
            
            return {
                'resource_type': 's3',
                'items': validated_items,
                'metadata': {}
            }
        except Exception as e:
            log.error("Error fetching s3 data: %s", e)
            return {'resource_type': 's3', 'items': [], 'metadata': {}}

    def fetch_sg_data():
        try:
            client = boto3.client('ec2', config=BOTO3_RETRY_CONFIG)
            response = []
            paginator = client.get_paginator('describe_security_groups')
            for page in paginator.paginate():
                response.extend(page['SecurityGroups'])
            return {
                'resource_type': 'sg',
                'items': [{'id': j['GroupId'], 'data': j} for j in response],
                'metadata': {}
            }
        except Exception as e:
            log.error("Error fetching SG data: %s", e)
            return {'resource_type': 'sg', 'items': [], 'metadata': {}}
        

    def fetch_subnet_data():
        try:
            client = boto3.client('ec2', config=BOTO3_RETRY_CONFIG)
            response = []
            paginator = client.get_paginator('describe_subnets')
            for page in paginator.paginate():
                response.extend(page['Subnets'])
            context.subnets = response
            return {
                'resource_type': 'subnet',
                'items': [{'id': j['SubnetId'], 'data': j} for j in response],
                'metadata': {'full_data': response}
            }
        except Exception as e:
            log.error("Error fetching subnet data: %s", e)
            return {'resource_type': 'subnet', 'items': [], 'metadata': {}}

    def fetch_tgw_data():
        try:
            client = boto3.client('ec2', config=BOTO3_RETRY_CONFIG)
            response = []
            paginator = client.get_paginator('describe_transit_gateways')
            for page in paginator.paginate():
                response.extend(page['TransitGateways'])
            return {
                'resource_type': 'tgw',
                'items': [{'id': j['TransitGatewayId'], 'data': j} for j in response],
                'metadata': {}
            }
        except Exception as e:
            log.error("Error fetching transit gateways: %s", e)
            return {'resource_type': 'tgw', 'items': [], 'metadata': {}}

    def fetch_roles_data():
        try:
            client = boto3.client('iam', region_name='us-east-1', config=BOTO3_RETRY_CONFIG)
            response = []
            paginator = client.get_paginator('list_roles')
            for page in paginator.paginate():
                response.extend(page['Roles'])
            return {
                'resource_type': 'iam',
                'items': [{'id': j['RoleName'], 'data': j} for j in response],
                'metadata': {'full_data': response}
            }
        except Exception as e:
            log.error("Error fetching IAM roles data: %s", e)
            return {'resource_type': 'iam', 'items': [], 'metadata': {}}
    
    def fetch_policies_data():
        try:
            client = boto3.client('iam', region_name='us-east-1', config=BOTO3_RETRY_CONFIG)
            response = []
            paginator = client.get_paginator('list_policies')
            for page in paginator.paginate(Scope='Local'):
                response.extend(page['Policies'])
            return {
                'resource_type': 'pol',
                'items': [{'id': j['Arn'], 'data': j} for j in response],
                'metadata': {}
            }
        except Exception as e:
            log.error("Error fetching IAM policies data: %s", e)
            return {'resource_type': 'pol', 'items': [], 'metadata': {}}

    def fetch_instprof_data():
        try:
            client = boto3.client('iam', region_name='us-east-1', config=BOTO3_RETRY_CONFIG)
            response = []
            paginator = client.get_paginator('list_instance_profiles')
            for page in paginator.paginate():
                response.extend(page['InstanceProfiles'])
            return {
                'resource_type': 'inp',
                'items': [{'id': j['InstanceProfileName'], 'data': j} for j in response],
                'metadata': {}
            }
        except Exception as e:
            log.error("Error fetching instance profiles data: %s", e)
            return {'resource_type': 'inp', 'items': [], 'metadata': {}}

    def fetch_launch_templates():
        try:
            client = boto3.client('ec2', config=BOTO3_RETRY_CONFIG)
            response = []
            paginator = client.get_paginator('describe_launch_templates')
            for page in paginator.paginate():
                response.extend(page['LaunchTemplates'])
            return {
                'resource_type': 'lt',
                'items': [{'id': j['LaunchTemplateId'], 'data': j} for j in response],
                'metadata': {}
            }
        except Exception as e:
            log.error("Error fetching launch templates: %s", e)
            return {'resource_type': 'lt', 'items': [], 'metadata': {}}

    # Result processing handler functions
    def _process_vpc_result(items, metadata):
        """Process VPC fetch results."""
        context.vpcs = metadata.get('full_data', [])
        for item in items:
            context.vpclist[item['id']] = True
    
    def _process_lambda_result(items, metadata):
        """Process Lambda fetch results."""
        for item in items:
            context.lambdalist[item['id']] = True
    
    def _process_s3_result(items, metadata):
        """Process S3 fetch results (already validated)."""
        for item in items:
            context.s3list[item['id']] = True
    
    def _process_sg_result(items, metadata):
        """Process security group fetch results."""
        for item in items:
            context.sglist[item['id']] = True
    
    def _process_subnet_result(items, metadata):
        """Process subnet fetch results."""
        context.subnets = metadata.get('full_data', [])
        for item in items:
            context.subnetlist[item['id']] = True
    
    def _process_tgw_result(items, metadata):
        """Process transit gateway fetch results."""
        for item in items:
            context.tgwlist[item['id']] = True
    
    def _process_iam_result(items, metadata):
        """Process IAM role fetch results."""
        for item in items:
            context.rolelist[item['id']] = True
    
    def _process_pol_result(items, metadata):
        """Process IAM policy fetch results."""
        for item in items:
            context.policylist[item['id']] = True
    
    def _process_inp_result(items, metadata):
        """Process instance profile fetch results."""
        for item in items:
            context.inplist[item['id']] = True
    
    def _process_lt_result(items, metadata):
        """Process launch template fetch results."""
        for item in items:
            context.ltlist[item['id']] = True
    
    def _process_single_result(result):
        """Process a single fetch result using the dispatch table.
        
        Args:
            result: Result dictionary from a fetch function
            
        Returns:
            int: Number of resources found (for progress reporting)
        """
        if not isinstance(result, dict):
            return 0
        
        resource_count = len(result.get('items', []))
        resource_type = result.get('resource_type')
        items = result.get('items', [])
        metadata = result.get('metadata', {})
        
        # Get handler from dispatch table and execute
        handler = RESULT_HANDLERS.get(resource_type)
        if handler:
            try:
                handler(items, metadata)
            except Exception as e:
                log.error("Error processing %s results: %s", resource_type, e)
        
        return resource_count
    
    def _write_resource_files(results):
        """Write resource data to JSON files after all fetches complete.
        
        Args:
            results: List of result dictionaries from fetch functions
        """
        files_to_write = {
            'imported/subnets.json': None,
            'imported/roles.json': None,
        }
        
        # Collect data from results
        for result in results:
            if result.get('resource_type') == 'subnet':
                files_to_write['imported/subnets.json'] = result.get('metadata', {}).get('full_data')
            elif result.get('resource_type') == 'iam':
                files_to_write['imported/roles.json'] = result.get('metadata', {}).get('full_data')
        
        # Write files with UTF-8 encoding
        for filepath, data in files_to_write.items():
            if data:
                try:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        json.dump(data, f, indent=2, default=str)
                except Exception as e:
                    log.error("Error writing %s: %s", filepath, e)
    
    # Dispatch table for result processing
    RESULT_HANDLERS = {
        'vpc': _process_vpc_result,
        'lambda': _process_lambda_result,
        's3': _process_s3_result,
        'sg': _process_sg_result,
        'subnet': _process_subnet_result,
        'tgw': _process_tgw_result,
        'iam': _process_iam_result,
        'pol': _process_pol_result,
        'inp': _process_inp_result,
        'lt': _process_lt_result,
    }

    # Use ThreadPoolExecutor to parallelize API calls with progress bar
    fetch_tasks = [
        ('VPCs', fetch_vpc_data),
        ('Lambda functions', fetch_lambda_data),
        ('S3 buckets', fetch_s3_data),
        ('Security groups', fetch_sg_data),
        ('Subnets', fetch_subnet_data),
        ('Transit gateways', fetch_tgw_data),
        ('IAM roles', fetch_roles_data),
        ('IAM policies', fetch_policies_data),
        ('Instance profiles', fetch_instprof_data),
        ('Launch templates', fetch_launch_templates)
    ]
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=context.cores) as executor:
        # Submit all tasks
        future_to_name = {
            executor.submit(func): name 
            for name, func in fetch_tasks
        }
        
        # Collect results for file writing
        all_results = []
        
        # Process results with progress bar
        with tqdm(total=len(fetch_tasks),
            desc="Fetching resource lists",
            unit="type",leave=False) as pbar:
            
            for future in concurrent.futures.as_completed(future_to_name):
                resource_name = future_to_name[future]
                result = future.result()
                
                # Store result for file writing
                all_results.append(result)
                
                # Process result and get resource count
                resource_count = _process_single_result(result)
                pbar.set_postfix_str(f"{resource_name}: {resource_count} found")
                pbar.update(1)
    
    # Write resource files after thread pool completes
    _write_resource_files(all_results)
    # slower - 3m 29s
    ####    role attachments stuff


    #with ThreadPoolExecutor(max_workers=context.cores) as executor14:
    #with ThreadPoolExecutor(max_workers=1) as executor14:
    #    futures = [
    #        executor14.submit(apl_threaded(rn))
    #        for rn in context.rolelist.keys()
    #    ]
    #                #return [f.result() for f in futures]
         
    return True

def build_secondary_lists(id=None):
    if id is None:
        st1 = datetime.datetime.now()
        log.info("Building secondary IAM resource lists ...")
        context.esttime = (len(context.rolelist) * 3) / 4
        context.tracking_message = "Stage 2 of 10, Building secondary IAM resource lists ..."
        
        def fetch_role_policies(role_name):
            client = boto3.client('iam', region_name='us-east-1', config=BOTO3_RETRY_CONFIG)
            try:
                # Get attached policies
                attached_policies = client.list_attached_role_policies(RoleName=role_name)
                
                # Get inline policies
                inline_policies = client.list_role_policies(RoleName=role_name)
                
                return {
                    'role_name': role_name,
                    'attached_policies': attached_policies['AttachedPolicies'] if attached_policies['AttachedPolicies'] else False,
                    'inline_policies': inline_policies['PolicyNames'] if inline_policies['PolicyNames'] else False
                }
            except Exception as e:
                log.error("Error fetching policies for role %s: %s", role_name, e)
                return {
                    'role_name': role_name,
                    'attached_policies': False,
                    'inline_policies': False
                }
        
        # Use ThreadPoolExecutor to parallelize API calls
        rcl = len(context.rolelist)
        log.debug("Fetching policies for %s IAM roles...", rcl)
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=context.cores) as executor:
            # Submit all role policy fetch tasks
            future_to_role = {
                executor.submit(fetch_role_policies, role_name): role_name 
                for role_name in context.rolelist.keys()
            }
            
            # Process results with progress bar
            for future in tqdm(concurrent.futures.as_completed(future_to_role),
                              total=len(future_to_role),
                              desc="Fetching IAM policies",
                              unit="role",leave=False):
                try:
                    result = future.result()
                    role_name = result['role_name']
                    context.attached_role_policies_list[role_name] = result['attached_policies']
                    context.role_policies_list[role_name] = result['inline_policies']
                except Exception as e:
                    log.error("Error processing result: %s", e)
        
        st2 = datetime.datetime.now()
        log.debug("secondary lists built in %s", str(st2 - st1))
    
    return