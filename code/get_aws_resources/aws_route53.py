import common
import boto3
import context
import inspect

def get_aws_route53_zone(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []:
                print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                common.write_import(type,j[key],None)
                common.add_dependancy("aws_route53_record",j[key])

        else:
            response = client.get_hosted_zone(Id=id)
            if response['HostedZone'] == []:
                print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            j=response['HostedZone']
            common.write_import(type,j[key],None)
            common.add_dependancy("aws_route53_record",j[key])

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_route53_record(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            print("WARNING: No id or invalid provided for "+type)
        else:
            rkey=type+"."+id
            context.rproc[rkey]=True
            if id.startswith("/hostedzone/"): id=id.split("/")[2]
            #print("id="+id)
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(HostedZoneId=id):
                response = response + page[topkey]
            if response == []:
                print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                #print("j="+str(j))
                r53name=j['Name']
                r53type=j['Type']
                if r53name.endswith("."): r53name=r53name[:-1]
                if r53type=="A":
                    import_id = id+"_"+r53name+"_"+r53type
                    import_id = import_id.replace("\\052", "*")
                    resource_name = id+"_"+r53name.replace("*", "star").replace("\\052", "star")+"_"+r53type

                    common.write_import(type, import_id, resource_name)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True