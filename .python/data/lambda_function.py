import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # TODO implement
    print ("Version 2")
    ec2 = boto3.client('ec2')
        
        # Get list of regions
    regions = ec2.describe_regions().get('Regions',[] )

        # Iterate over regions
    for region in regions:
            
            # Running following for a particular region
        print ("*************** Checking region  --   %s " % region['RegionName'])
        reg=region['RegionName']
        #print(reg)
                
        client = boto3.client('ec2', region_name=reg)
        response = client.describe_instances()
        #print(json.dumps(response, indent=4, separators=(',', ': ')))
        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                skip=0
                istate=instance['State']['Name']
                tags="null"
                try:
                    tags=instance['Tags']
                    for t in tags:
                        k=t['Key']
                        v=t['Value']
                        #print(k)
                        if "eks:cluster-name" in k:
                            print("skipping as eks node: " + instance['InstanceId'] + " Cluster " + v)
                            skip=1
                        if "DR1" in v:
                            print("skipping as DR Learning: " + instance['InstanceId'] + " DeepRacer " + v)
                            skip=1
                except KeyError as e:
                    print("no tags")
                
                #print(istate)
                if "running" in istate:
                    if skip == 0:
                        try:
                            print ("About to stop %s | in %s" % (instance['InstanceId'], region['RegionName']))
                            response = client.stop_instances(InstanceIds=[instance['InstanceId']])
                            print ("stopped")
                        except ClientError as e:
                            print (e.response['Error']['Message'])
                            pass
                    else:
                        print ("Exception not stoping %s | in %s" % (instance['InstanceId'], region['RegionName']))
                                                          
        
    print ("+++++++++++++ Done -----------------") 
