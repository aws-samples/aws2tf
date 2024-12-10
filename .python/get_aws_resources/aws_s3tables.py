import common
import boto3
from botocore.config import Config
import globals
import inspect

def get_aws_s3tables_table_bucket(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn,config=config)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            for j in response:
                common.write_import(type,j[key],None) 
                common.add_known_dependancy("aws_s3tables_namespace",j[key])

        else:      
            response = client.get_table_bucket(tableBucketARN=id)
            if response == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            j=response
            common.write_import(type,j[key],None)
            common.add_known_dependancy("aws_s3tables_namespace",j[key])

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_s3tables_namespace(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn,config=config)
        if id is None:
            print("WARNING: must pass table bucket ARN as parameter")
            return True

        else:      
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(tableBucketARN=id):
                response = response + page[topkey]
            if response == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
                pkey=type+"."+id
                globals.rproc[pkey]=True
                return True
            #print("response="+str(response))
            for j in response:
                for k in j[key]:
                    theid=id+";"+k
                    common.write_import(type,theid,None) 
                    common.add_dependancy("aws_s3tables_table", theid)
            pkey=type+"."+id
            globals.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_s3tables_table(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn,config=config)
        if id is None:
            print("WARNING: must pass table bucket ARN and namespace as parameters")
            return True

        else:   
            if ";" not in id:
                print("WARNING: must pass table bucket ARN and namespace as parameters")
                return True  
            barn=id.split(";")[0]
            namespace=id.split(";")[1] 
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(tableBucketARN=barn,namespace=namespace):
                response = response + page[topkey]
            if response == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
                pkey=type+"."+id
                globals.rproc[pkey]=True
                return True
            for j in response:
                theid=id+";"+j[key]
                common.write_import(type,theid,None) 
            pkey=type+"."+id
            globals.rproc[pkey]=True
            

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True