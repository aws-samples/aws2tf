import common
import logging
log = logging.getLogger('aws2tf')
import boto3
from botocore.config import Config
import context
import inspect

def get_aws_transfer_server(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
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
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            for j in response:
                common.write_import(type,j[key],None) 

        else:      
            response = client.describe_server(ServerId=id)
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            j=response['Server']
            common.write_import(type,j[key],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True