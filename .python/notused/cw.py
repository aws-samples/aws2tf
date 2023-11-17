import boto3
import common

#                                        botokey                                jsonid          filterid
#if type == "aws_nat_gateway": return 'NatGateways', "describe_nat_gateways", "NatGatewayId","nat-gateway-id"
# no filters on this describe so use name prefix


def cwlogs(type,id,botokey,jsonid,filterid):
    clfn="describe_log_groups"
    client = boto3.client('logs')   
    dfn = getattr(client, clfn)
    print("doing "+ type + ' with id ' + str(id))
    if id is None:
      response=dfn() 
    else:
        print("calling with filter id="+filterid + " and id=" + id)
        response=dfn(logGroupNamePrefix=id) 
 
    fn="import__"+type+".tf"
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