import boto3
import common
import os

#                                        botokey                                jsonid          filterid
#if type == "aws_nat_gateway": return 'NatGateways', "describe_nat_gateways", "NatGatewayId","nat-gateway-id"
# no filters on this describe so use name prefix


def rules(type,id,botokey,jsonid,filterid):
    client = boto3.client('config')   
    print("doing "+ type + ' with id ' + str(id))
    if id is None:
      response=client.describe_config_rules()  
    else:
      print("calling with filter id="+filterid + " and id=" + id)
      response=client.describe_config_rules(ConfigRuleNames=[id])
 
    fn=type+"_import.tf"
    with open(fn, "w") as f:
            for item in response[botokey]:
                theid=item[jsonid]
                tfid=theid.replace("/","_")
                f.write('import {\n')
                f.write('  to = ' +type + '.' + tfid + '\n')
                f.write('  id = "'+ theid + '"\n')
                f.write('}\n')
    f.close()

    common.tfplan(type)
    #rf=type+"_resources.out"

    #if os.path.isfile("tfplan"):
    #     com="cp " + rf + " "+ type + ".tf"
    #     rout=common.rc(com)

    #else:
    #     print("could not find expected tfplan file - exiting")
    #     exit()