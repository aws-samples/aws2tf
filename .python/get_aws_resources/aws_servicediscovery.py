import common
import boto3
import globals
import inspect

def get_aws_service_discovery_private_dns_namespace(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                # get a vpc-id
                if j['Type']=="DNS_PRIVATE":
                    print(str(j))
                    #common.write_import(type,j[key],None) 

        else:      
            response = client.get_namespace(Id=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response['Namespace']
            if j['Type']=="DNS_PRIVATE":
            # get a vpc-id
                print(str(j))
                #common.write_import(type,j[key],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_service_discovery_public_dns_namespace(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                if j['Type']=="DNS_PUBLIC":
                    common.write_import(type,j[key],"n-"+j[key]) 

        else:      
            response = client.get_namespace(Id=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response['Namespace']
            if j['Type']=="DNS_PUBLIC":
                common.write_import(type,j[key],"n-"+j[key])

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True