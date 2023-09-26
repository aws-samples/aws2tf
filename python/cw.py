
import boto3
import common
import fixtf
import os

#                                        botokey                                jsonid          filterid
#if type == "aws_nat_gateway": return 'NatGateways', "describe_nat_gateways", "NatGatewayId","nat-gateway-id"
# no filters on this describe so use name prefix


def cwlogs(type,id,botokey,jsonid,filterid):
    print("cw-logs")
    client = boto3.client('logs')   
    print("calling get_resource with id="+str(id))
    logs=client.describe_log_groups()

    print("doing "+ type + ' with id ' + str(id))
    if id is None:
      response=client.describe_log_groups()  
    else:
        print("calling with filter id="+filterid + " and id=" + id)
        response=client.describe_log_groups(logGroupNamePrefix=id) 
 
    fn=type+"_import.tf"
    with open(fn, "w") as f:
            for item in response[botokey]:
                theid=item[jsonid]
                f.write('import {\n')
                f.write('  to = ' +type + '.' + theid + '\n')
                f.write('  id = "'+ theid + '"\n')
                f.write('}\n')
    f.close()

    common.tfplan(type)
    rf=type+"_resources.out"

    if os.path.isfile("tfplan"):
         com="cp " + rf + " aws_s3.tf"
         rout=common.rc(com)

    else:
         print("could not find expected tfplan file - exiting")
         exit()