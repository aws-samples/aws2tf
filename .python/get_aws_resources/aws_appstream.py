import common
import boto3
import globals
import inspect

def get_aws_appstream_user(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(AuthenticationType='USERPOOL'):
                response = response + page[topkey]
            if response == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                theid=j[key]+"/"+"USERPOOL"
                pkey=theid.replace("@","_")
                common.write_import(type,theid,pkey) 

        else:      
            response = client.describe_users(AuthenticationType=id)
            if response == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response
            theid=j[key]+"/"+"USERPOOL"
            pkey=theid.replace("@","_")
            common.write_import(type,theid,pkey)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True