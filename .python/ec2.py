#!/usr/bin/env python3

import common
import resources

# called by aws2tf.py
def ec2_resources(type,id):   # aws_vpc , vpc-xxxxxxxxx called from main.py
   #ec2client = boto3.client('ec2')   
   #resources.resource_data       if type == "aws_vpc": return 'ec2', 'Vpcs', "describe_vpcs", "VpcId", "vpc-id" 
   clfn,descfn,topkey,key,filterid=resources.resource_data(type,id)
   print("calling getresource with type="+type+" id="+str(id)+" -- clfn="+clfn + " descfn="+descfn+  "topkey="+topkey + "key="+key +"filterid="+filterid)
   common.getresource(clfn,descfn,topkey,key,filterid)

   #print("Done ec2_resources")


# aws_vpc, vpc-xxxx, 'Vpcs', ec2client.describe_vpcs, "VpcId", "vpc-id"




