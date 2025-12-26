import common
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect

def get_aws_securityhub_account(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        try:
            client.list_members()
        except:
            log.info("No access to "+type+" returning")
            return True

        if id is None:
            common.write_import(type,context.acc,"a-"+context.acc) 
        else:
            common.write_import(type,id,"a-"+id) 



    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_securityhub_organization_configuration(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)

        try:    
            response = client.describe_organization_configuration()
        except Exception as e:
            log.info("NO access returning")
            return True

        if response == []: 
            log.debug("Empty response for "+type+ " id="+str(id)+" returning")
            return True
        j=response
        common.write_import(type,j[key],None) 


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True