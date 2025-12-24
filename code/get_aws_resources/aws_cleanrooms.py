import common
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect

def get_aws_cleanrooms_collaboration(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: 
                log.info("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                common.write_import(type,j[key],"c-"+j[key]) 

        else:      
            response = client.get_collaboration(collaborationIdentifier=id)
            if response['response'] == []: 
                log.info("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            j=response['collaboration']
            common.write_import(type,j[key],"c-"+j[key])

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True