import common
import boto3
from botocore.config import Config
import globals
import inspect

def get_aws_networkmanager_global_network(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config (
            retries = {
                'max_attempts': 10,
                'mode': 'standard'
            }
        )
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
                common.add_dependancy("aws_networkmanager_site", j[key])
                common.add_dependancy("aws_networkmanager_device", j[key])

        else:      
            response = client.describe_global_networks(GlobalNetworkIds=[id])
            if response == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            for j in response[topkey]:
                common.write_import(type,j[key],None) 
                common.add_dependancy("aws_networkmanager_site", j[key])
                common.add_dependancy("aws_networkmanager_device", j[key])


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_networkmanager_site(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        if id is None:
            print("WARNING: must pass global network id as parameter")
            return True
        else:  
            pkey=type+"."+id
            config = Config (retries = {'max_attempts': 10,'mode': 'standard'})
            client = boto3.client(clfn,config=config)
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(GlobalNetworkId=id):
                response = response + page[topkey]
            if response == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
                globals.rproc[pkey]=True
                return True
            for j in response:
                common.write_import(type,j[key],None) 
            globals.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_networkmanager_device(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        if id is None:
            print("WARNING: must pass global network id as parameter")
            return True
        else:  
            pkey=type+"."+id
            config = Config (retries = {'max_attempts': 10,'mode': 'standard'})
            client = boto3.client(clfn,config=config)
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(GlobalNetworkId=id):
                response = response + page[topkey]
            if response == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
                globals.rproc[pkey]=True
                return True
            for j in response:
                common.write_import(type,j[key],None) 
            globals.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True