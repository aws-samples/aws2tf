import common
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect
from botocore.config import Config

def get_aws_codedeploy_app(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        paginator = client.get_paginator(descfn)
        for page in paginator.paginate():
            response = response + page[topkey]
        if response == []: 
            log.debug("Empty response for "+type+ " id="+str(id)+" returning")
            return True
        
        for j in response:
            log.debug(str(j))
            if id is None: 
                common.write_import(type,j,None) 
            elif j==id:
                common.write_import(type,j,None) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_codedeploy_deployment_config(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        paginator = client.get_paginator(descfn)
        for page in paginator.paginate():
            response = response + page[topkey]
        if response == []: 
            log.debug("Empty response for "+type+ " id="+str(id)+" returning")
            return True
        
        for j in response:
            # Skip AWS default deployment configs (they can't be managed by Terraform)
            if j.startswith("CodeDeployDefault"):
                if context.debug: log.debug(f"Skipping AWS default config: {j}")
                continue
                
            log.debug(str(j))
            if id is None: 
                common.write_import(type,j,None) 
            elif j==id:
                common.write_import(type,j,None) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True
