import common
import boto3
import globals
import inspect

def get_aws_directory_service_directory(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        paginator = client.get_paginator(descfn)
        if id is None:  
            for page in paginator.paginate(): response = response + page[topkey]
        else:
            for page in paginator.paginate(DirectoryIds=[id]): response = response + page[topkey]
        
        if response == []: 
            if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
            return True
        for j in response:
            common.write_import(type,j[key],None) 
        if id is not None:
            pkey=type+"."+id
            globals.rproc[pkey] = True


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True