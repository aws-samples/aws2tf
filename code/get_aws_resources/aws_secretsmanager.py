import common
import logging
log = logging.getLogger('aws2tf')
import fixtf
import base64
import boto3
import sys
import os
import context
import inspect

def get_aws_secretsmanager_secret(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In get_aws_secretsmanager_secret  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            # calls list_secrets
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(IncludePlannedDeletion=False):
                response = response + page[topkey]
            if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                sarn=j[key]
                sn=sarn.split(":")[-1]
                if sn.startswith("rds!"):
                    log.info("INFO: skipping rds managed secret "+sn+" ...")
                    return True
                else:
                    common.write_import(type,j[key],None) 
                    #common.add_dependancy("aws_secretsmanager_secret_version",j[key])
                    try:
                        log.info(j['RotationEnabled'])
                        common.add_dependancy("aws_secretsmanager_secret_rotation",j[key])
                    except KeyError:
                        log.info("INFO: No rotation config")


        else:
            response = client.describe_secret(SecretId=id)
            if response == []: 
                log.info("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            j=response
            common.write_import(type,j[key],None)
            common.add_dependancy("aws_secretsmanager_secret_version",j[key])
            try:
                #print(j['RotationEnabled'])
                common.add_dependancy("aws_secretsmanager_secret_rotation",j[key])
            except KeyError:
                log.info("INFO: No rotation config")
            


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True



def get_aws_secretsmanager_secret_rotation(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In get_aws_secretsmanager_secret_rotation  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            log.info("ERROR: get_aws_secretsmanager_secret_rotation must be called with SecretID as parameter")
        else:
            pkey=type+"."+id
            response = client.describe_secret(SecretId=id)
            try:
                roten=response['RotationEnabled']
            except KeyError:
                log.info("INFO: No rotation config")
                
                context.rproc[pkey]=True
                return True
            common.write_import(type,id,None)
            context.rproc[pkey]=True
         
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_secretsmanager_secret_version(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In get_aws_secretsmanager_secret_version  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            # calls list_secret_version
            log.info("ERROR: get_aws_secretsmanager_secret_verion must be called with SecretID as parameter")
        else:
            response = client.list_secret_version_ids(SecretId=id,IncludeDeprecated=False)
            if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
            #print(response)

            for j in response[topkey]:
                #print(j[key])
                try:
                    sresponse = client.get_secret_value(SecretId=id,VersionId=j[key])
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    exn=str(exc_type.__name__)
                    #print(exn,str(e))
                    if "(AccessDeniedException) when calling the GetSecretValue" in str(e):
                        log.info("INFO: get_secret_value failed - not authorized skipping",type,id.split(':')[-1])
                        pkey=type+"."+id
                        context.rproc[pkey]=True
                        return True
                
                sv=sresponse['SecretString']
                #print(str(sv))
                pkey=id+"|"+j[key]
                common.write_import(type,pkey,None) 
            pkey=type+"."+id
            context.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_secretsmanager_secret_policy(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In get_aws_secretsmanager_secret_policy  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        log.info("INFO: aws_secretsmanager_policy - policy embedded in aws_secretmager_secret by aws2tf")


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True