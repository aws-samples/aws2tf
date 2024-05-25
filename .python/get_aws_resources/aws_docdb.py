import common
import boto3
import globals
import inspect

def get_aws_docdb_cluster_parameter_group(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    
    try:
        response = []
        client = boto3.client(clfn)
        ## id filter here
   
        paginator = client.get_paginator(descfn)
        for page in paginator.paginate():
                response = response + page[topkey]
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        #print(str(response))
        for j in response:
            if id is None:
                if "default." not in j[key]:
                    common.write_import(type,j[key],None) 
            else:
                if "default." not in id:  
                    if id==j[key]:
                        common.write_import(type,j[key],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_docdb_subnet_group(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    
    try:
        response = []
        client = boto3.client(clfn)
        ## id filter here
   
        paginator = client.get_paginator(descfn)
        for page in paginator.paginate():
                response = response + page[topkey]
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        #print(str(response))
        for j in response:
            if id is None:
                if "default" != j[key]:
                    common.write_import(type,j[key],None) 
            else:
                if "default" != id:  
                    if id==j[key]:
                        common.write_import(type,j[key],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True