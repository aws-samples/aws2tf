import boto3
import globals
import concurrent.futures
import json
import datetime


def build_lists():
    print("Building core resource lists ...")
    globals.tracking_message="Stage 2 of 10, Building core resource lists ..."
    def fetch_vpc_data():
        try:
            client = boto3.client('ec2')
            response = []
            paginator = client.get_paginator('describe_vpcs')
            for page in paginator.paginate():
                response.extend(page['Vpcs'])
            
            return [('vpc', j['VpcId']) for j in response]
        except Exception as e:
            print("Error fetching vpc data:", e)
            return []
    
    def fetch_s3_data():
        try:
            client = boto3.client('s3')
            response = []
            paginator = client.get_paginator('list_buckets')
            for page in paginator.paginate(BucketRegion=globals.region):
                response.extend(page['Buckets'])
            return [('s3', j['Name']) for j in response]
        except Exception as e:
            print("Error fetching vpc data:", e)
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
            print("Error fetching vpc data:", e)
            return []

    def fetch_subnet_data():
        try:
            client = boto3.client('ec2')
            response = []
            paginator = client.get_paginator('describe_subnets')
            for page in paginator.paginate():
                response.extend(page['Subnets'])
            globals.subnets=response
            # save response
            with open('imported/subnets.json', 'w') as f:
               json.dump(response, f, indent=2, default=str)
            return [('subnet', j['SubnetId']) for j in response]
        except Exception as e:
            print("Error fetching vpc data:", e)
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
            print("Error fetching transit gateways:", e)
            return []

    def fetch_roles_data():
        try:
            client = boto3.client('iam')
            response = []
            paginator = client.get_paginator('list_roles')
            for page in paginator.paginate():
                response.extend(page['Roles'])
            # save
            return [('iam', j['RoleName']) for j in response]
        except Exception as e:
            print("Error fetching vpc data:", e)
            return []
    
    def fetch_policies_data():
        try:
            client = boto3.client('iam')
            response = []
            paginator = client.get_paginator('list_policies')
            for page in paginator.paginate(Scope='Local'):
                response.extend(page['Policies'])
            return [('pol', j['Arn']) for j in response]
        except Exception as e:
            print("Error fetching vpc data:", e)
            return []


    # Use ThreadPoolExecutor to parallelize API calls
    with concurrent.futures.ThreadPoolExecutor(max_workers=globals.cores) as executor:
        futures = [
            executor.submit(fetch_vpc_data),
            executor.submit(fetch_s3_data),
            executor.submit(fetch_sg_data),
            executor.submit(fetch_subnet_data),
            executor.submit(fetch_tgw_data),
            executor.submit(fetch_roles_data),
            executor.submit(fetch_policies_data)
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
                            globals.vpclist[vpc_id] = True
                    elif resource_type == 's3':
                        for _, bucket in result:
                            globals.s3list[bucket] = True
                    elif resource_type == 'sg':
                        for _, sg_id in result:
                            globals.sglist[sg_id] = True
                    elif resource_type == 'subnet':
                        for _, subnet_id in result:
                            globals.subnetlist[subnet_id] = True
                    elif resource_type == 'tgw':
                        for _, tgw_id in result:
                            globals.tgwlist[tgw_id] = True
                    elif resource_type == 'iam':
                        for _, role_name in result:
                            globals.rolelist[role_name] = True
                    elif resource_type == 'pol':
                        for _, policy_arn in result:
                            globals.policylist[policy_arn] = True
                else:
                    # Handle roles data
                    with open('imported/roles.json', 'w') as f:
                        json.dump(result, f, indent=2, default=str)

    # slower - 3m 29s
    ####    role attachments stuff


    #with ThreadPoolExecutor(max_workers=globals.cores) as executor14:
    #with ThreadPoolExecutor(max_workers=1) as executor14:
    #    futures = [
    #        executor14.submit(apl_threaded(rn))
    #        for rn in globals.rolelist.keys()
    #    ]
    #                #return [f.result() for f in futures]
         
    return True

def build_secondary_lists(id):
    if id is None:
        st1 = datetime.datetime.now()
        print("Building secondary IAM resource lists ...")
        globals.esttime=(len(globals.rolelist)*3)/4
        globals.tracking_message="Stage 2 of 10, Building secondary IAM resource lists ..."
        client = boto3.client('iam')
        # attached_role_policies
        rcl=len(globals.rolelist)
        rc=1
        for rn in globals.rolelist.keys():
            response=[]
            response1=[]
            #paginator = client.get_paginator('list_attached_role_policies')
            #paginator2 = client.get_paginator('list_role_policies')
            try:
                response=client.list_attached_role_policies(RoleName=rn)
                response1 = client.list_role_policies(RoleName=rn)
            except Exception as e:  
                print(f"{e=}")
            #print(str(response)+"\n")
            if response['AttachedPolicies'] == []: 
                globals.attached_role_policies_list[rn]=False
            else:
                globals.attached_role_policies_list[rn]=response['AttachedPolicies']
            
            if response1['PolicyNames'] == []: 
                globals.role_policies_list[rn]=False
            else:
                globals.role_policies_list[rn]=response1['PolicyNames']

            globals.tracking_message="Stage 2 of 10, Building secondary IAM resource lists... "+str(rc)+" of "+str(rcl)
            rc=rc+1

        
        st2 = datetime.datetime.now()
        print("secondary lists built in "+ str(st2 - st1))

    return