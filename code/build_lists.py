import boto3
import context
import concurrent.futures
import json
import datetime
import logging
from tqdm import tqdm

log = logging.getLogger('aws2tf')


def build_lists():
    log.info("Building core resource lists ...")
    context.tracking_message="Stage 2 of 10, Building core resource lists ..."
    
    
    
    def fetch_lambda_data():
        try:
            client = boto3.client('lambda')
            response = []
            paginator = client.get_paginator('list_functions')
            for page in paginator.paginate():
                response.extend(page['Functions'])
            return [('lambda', j['FunctionName']) for j in response]
        except Exception as e:
            log.error("Error fetching Lambda data: %s %s",  e)
            return []
      
    
    def fetch_vpc_data():
        try:
            client = boto3.client('ec2')
            response = []
            paginator = client.get_paginator('describe_vpcs')
            for page in paginator.paginate():
                response.extend(page['Vpcs'])
            context.vpcs=response
            return [('vpc', j['VpcId']) for j in response]
        except Exception as e:
            log.error("Error fetching ec2 data: %s %s",  e)
            return []
    
    def fetch_s3_data():
        try:
            client = boto3.client('s3')
            response = []
            paginator = client.get_paginator('list_buckets')
            for page in paginator.paginate(BucketRegion=context.region):
                response.extend(page['Buckets'])
            return [('s3', j['Name']) for j in response]
        except Exception as e:
            log.error("Error fetching s3 data: %s %s",  e)
            return []

    def fetch_sg_data():
        try:
            client = boto3.client('ec2')
            response = []
            paginator = client.get_paginator('describe_security_groups')
            for page in paginator.paginate():
                response.extend(page['SecurityGroups'])
            return [('sg', j['GroupId']) for j in response]
        except Exception as e:
            log.error("Error fetching SG data: %s %s",  e)
            return []
        

    def fetch_subnet_data():
        try:
            client = boto3.client('ec2')
            response = []
            paginator = client.get_paginator('describe_subnets')
            for page in paginator.paginate():
                response.extend(page['Subnets'])
            context.subnets=response
            # save response
            with open('imported/subnets.json', 'w') as f:
               json.dump(response, f, indent=2, default=str)
            return [('subnet', j['SubnetId']) for j in response]
        except Exception as e:
            log.error("Error fetching vpc data: %s %s",  e)
            return []

    def fetch_tgw_data():
        try:
            client = boto3.client('ec2')
            response = []
            paginator = client.get_paginator('describe_transit_gateways')
            for page in paginator.paginate():
                response.extend(page['TransitGateways'])
            return [('tgw', j['TransitGatewayId']) for j in response]
        except Exception as e:
            log.error("Error fetching transit gateways: %s %s",  e)
            return []

    def fetch_roles_data():
        try:
            client = boto3.client('iam',region_name='us-east-1')
            response = []
            paginator = client.get_paginator('list_roles')
            for page in paginator.paginate():
                response.extend(page['Roles'])
            # save
            with open('imported/roles.json', 'w') as f:
               json.dump(response, f, indent=2, default=str)
            return [('iam', j['RoleName']) for j in response]
        except Exception as e:
            log.error("Error fetching vpc data: %s %s",  e)
            return []
    
    def fetch_policies_data():
        try:
            client = boto3.client('iam',region_name='us-east-1')
            response = []
            paginator = client.get_paginator('list_policies')
            for page in paginator.paginate(Scope='Local'):
                response.extend(page['Policies'])
            return [('pol', j['Arn']) for j in response]
        except Exception as e:
            log.error("Error fetching vpc data: %s %s",  e)
            return []

    def fetch_instprof_data():
        try:
            client = boto3.client('iam',region_name='us-east-1')
            response = []
            paginator = client.get_paginator('list_instance_profiles')
            for page in paginator.paginate():
                response.extend(page['InstanceProfiles'])
            return [('inp', j['InstanceProfileName']) for j in response]
        except Exception as e:
            log.error("Error fetching vpc data: %s %s",  e)
            return []


    # Use ThreadPoolExecutor to parallelize API calls
    with concurrent.futures.ThreadPoolExecutor(max_workers=context.cores) as executor:
        futures = [
            executor.submit(fetch_vpc_data),
            executor.submit(fetch_lambda_data),
            executor.submit(fetch_s3_data),
            executor.submit(fetch_sg_data),
            executor.submit(fetch_subnet_data),
            executor.submit(fetch_tgw_data),
            executor.submit(fetch_roles_data),
            executor.submit(fetch_policies_data),
            executor.submit(fetch_instprof_data)
        ]
        
        # Process results as they complete
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if isinstance(result, list):
                if result and isinstance(result[0], tuple):
                    # Handle resource ID lists
                    resource_type = result[0][0]
                    if resource_type == 'vpc':
                        for _, vpc_id in result:
                            context.vpclist[vpc_id] = True

                    if resource_type == 'lambda':
                        for _, lambda_id in result:
                            context.lambdalist[lambda_id] = True

                    elif resource_type == 's3':
                        client = boto3.client('s3')
                        for _, bucket in result:
                            #here ? 
                            #print("Buck from result=",bucket)   
                            try:
                                ####### problematic call
                                objs = client.list_objects_v2(Bucket=bucket,MaxKeys=1)      
                            except Exception as e:
                                log.error(f"Error details: {e}")
                                continue

                            context.s3list[bucket] = True
                    elif resource_type == 'sg':
                        for _, sg_id in result:
                            context.sglist[sg_id] = True
                    elif resource_type == 'subnet':
                        for _, subnet_id in result:
                            context.subnetlist[subnet_id] = True
                    elif resource_type == 'tgw':
                        for _, tgw_id in result:
                            context.tgwlist[tgw_id] = True
                    elif resource_type == 'iam':
                        for _, role_name in result:
                            context.rolelist[role_name] = True
                    elif resource_type == 'pol':
                        for _, policy_arn in result:
                            context.policylist[policy_arn] = True
                    elif resource_type == 'inp':
                        for _, inst_prof in result:
                            context.inplist[inst_prof] = True
                else:
                    # Handle roles data
                    with open('imported/roles.json', 'w') as f:
                        json.dump(result, f, indent=2, default=str)
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
            client = boto3.client('iam',region_name='us-east-1')
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
                log.error(f"Error fetching policies for role {role_name}: {e}")
                return {
                    'role_name': role_name,
                    'attached_policies': False,
                    'inline_policies': False
                }
        
        # Use ThreadPoolExecutor to parallelize API calls
        rcl = len(context.rolelist)
        log.info(f"Fetching policies for {rcl} IAM roles...")
        
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
                              unit="role"):
                try:
                    result = future.result()
                    role_name = result['role_name']
                    context.attached_role_policies_list[role_name] = result['attached_policies']
                    context.role_policies_list[role_name] = result['inline_policies']
                except Exception as e:
                    log.error(f"Error processing result: {e}")
        
        st2 = datetime.datetime.now()
        log.info("secondary lists built in " + str(st2 - st1))
    
    return