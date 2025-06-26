import common
import boto3
from botocore.config import Config
import globals
import inspect

def get_aws_elasticache_cluster(type, id, clfn, descfn, topkey, key, filterid):
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

        else:      
            response = client.describe_cache_clusters(CacheClusterId=id)
            if response['CacheClusters'] == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            j=response['CacheClusters']
            common.write_import(type,j[key],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

# aws_elasticache_serverless_cache

def get_aws_elasticache_serverless_cache(type, id, clfn, descfn, topkey, key, filterid):
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

        else:      
            response = client.describe_serverless_caches(ServerlessCacheName=id)
            if response['ServerlessCaches'] == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            j=response['ServerlessCaches']
            common.write_import(type,j[key],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True