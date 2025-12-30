import common
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect,sys


def get_aws_bedrock_model_invocation_logging_configuration(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        j=[]
        response = client.get_model_invocation_logging_configuration()
        try:
            j=response[topkey]
        except KeyError:
            if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
            return True
        if j == []: 
            if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
            return True
        common.write_import(type,context.region,None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
        if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
        return True
    return True


def get_aws_bedrock_guardrail(type, id, clfn, descfn, topkey, key, filterid):
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
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            for j in response:
                resp2 = client.list_guardrails(guardrailIdentifier=j[key])
                for k in resp2[topkey]:
                    try:
                        tresp=client.list_tags_for_resource(resourceARN=k['arn'])
                    except Exception as e:
                        exc_type, exc_obj, exc_tb = sys.exc_info()
                        exn=str(exc_type.__name__)
                        if exn=="AccessDeniedException":
                            log.info("No Access to tags for "+k['arn']+" returning ...")
                            pkey=type+"."+k[key]
                            context.rproc[pkey]=True
                            return True
                    tkey=k[key]+","+k['version']
                    common.write_import(type,tkey,None) 
                    pkey=type+"."+k[key]
                    context.rproc[pkey]=True


        else:      
            response = client.list_guardrails(guardrailIdentifier=id)
            pkey=type+"."+id
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
                pkey=type+"."+id
                context.rproc[pkey]=True
                return True
           
            for j in response[topkey]:
                tkey=j[key]+","+j['version']
                try:
                    tresp=client.list_tags_for_resource(resourceARN=j['arn'])
                    log.debug(str(tresp))
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    exn=str(exc_type.__name__)
                    if exn=="AccessDeniedException":
                        log.info("No Access to tags for "+j['arn']+" returning ...")
                        pkey=type+"."+j[key]
                        context.rproc[pkey]=True
                        return True
                common.write_import(type,tkey,None)
                context.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


