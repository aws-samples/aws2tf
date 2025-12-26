import common
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect

def get_aws_backup_region_settings(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        common.write_import(type,context.region,None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_backup_vault(type, id, clfn, descfn, topkey, key, filterid):
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
                log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                if "/" not in j[key]:
                    common.write_import(type,j[key],None) 

        else:      
            response = client.describe_backup_vault(BackupVaultName=id)
            if response == []: 
                log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            j=response
            common.write_import(type,j[key],None)



    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_backup_plan(type, id, clfn, descfn, topkey, key, filterid):
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
                log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                if "/" not in j['BackupPlanName']:
                    common.write_import(type,j[key],None) 

        else:      
            response = client.get_backup_plan(BackupPlanId=id)
            if response == []: 
                log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            j=response
            common.write_import(type,j[key],None)



    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True