import common
import boto3
import globals
import inspect

def get_aws_neptune_subnet_group(type, id, clfn, descfn, topkey, key, filterid):
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

def get_aws_neptune_cluster_endpoint(type, id, clfn, descfn, topkey, key, filterid):
    #if globals.debug:
    print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    
    try:
        response = []
        client = boto3.client(clfn)
        paginator = client.get_paginator(descfn)
        if id is None:
            for page in paginator.paginate():
                response = response + page[topkey] 
        else:
            for page in paginator.paginate(DBClusterIdentifier=id):
                response = response + page[topkey]
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        print(str(response))
        for j in response:
            print(str(j))
            clid=j['DBClusterIdentifier']
            pkey=clid+":"+j[key]
            common.write_import(type,pkey,None) 



    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True