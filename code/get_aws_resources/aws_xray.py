import common
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect
from botocore.config import Config

def get_aws_xray_sampling_rule(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)

        paginator = client.get_paginator(descfn)
        for page in paginator.paginate():
                response = response + page[topkey]
        if response == []: 
            if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
            return True
        for j in response:
            theid=j['SamplingRule'][key]
            if theid != "Default":
                common.write_import(type,theid,None) 



    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_xray_encryption_config(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        common.write_import(type,context.region,None) 



    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_xray_group(type, id, clfn, descfn, topkey, key, filterid):
    """
    Get X-Ray groups
    """
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all groups
            paginator = client.get_paginator(descfn)
            response = []
            for page in paginator.paginate():
                response = response + page[topkey]
            for j in response:
                # Write import using GroupARN (Terraform expects ARN for import)
                common.write_import(type, j['GroupARN'], None)
        else:
            # Get specific group by ARN
            if id.startswith('arn:'):
                # Already have ARN, use it directly
                common.write_import(type, id, None)
            else:
                # Have name, need to get ARN
                resp = client.get_group(GroupName=id)
                if resp and 'Group' in resp:
                    common.write_import(type, resp['Group']['GroupARN'], None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True
