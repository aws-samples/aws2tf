import common
import boto3
import context
import inspect
import botocore

def get_aws_ecrpublic_repository(type, id, clfn, descfn, topkey, key, filterid):
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
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                common.write_import(type,j[key],None) 
        else:
            response = client.describe_repositories(repositoryNames=[id])
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response['repositories']
            if j[key]==id:
                common.write_import(type,j[key],None)
    
    except client.exceptions.RegistryPolicyNotFoundException:
        pass


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True