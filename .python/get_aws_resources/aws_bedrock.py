import common
import boto3
import globals
import inspect,sys


def get_aws_bedrock_model_invocation_logging_configuration(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        j=[]
        response = client.get_model_invocation_logging_configuration()
        try:
            j=response[topkey]
        except KeyError:
            if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
            return True
        if j == []: 
            if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
            return True
        common.write_import(type,globals.region,None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
        if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
        return True
    return True


def get_aws_bedrock_guardrail(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            for j in response:
                resp2 = client.list_guardrails(guardrailIdentifier=j[key])
                for k in resp2[topkey]:
                    try:
                        tresp=client.list_tags_for_resource(resourceARN=k['arn'])
                        print(str(tresp))
                    except Exception as e:
                        exc_type, exc_obj, exc_tb = sys.exc_info()
                        exn=str(exc_type.__name__)
                        if exn=="AccessDeniedException":
                            print("No Access to tags for "+k['arn']+" returning ...")
                            pkey=type+"."+k[key]
                            globals.rproc[pkey]=True
                            return True
                    tkey=k[key]+","+k['version']
                    common.write_import(type,tkey,None) 
                    pkey=type+"."+k[key]
                    globals.rproc[pkey]=True


        else:      
            response = client.list_guardrails(guardrailIdentifier=id)
            pkey=type+"."+id
            if response == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
                pkey=type+"."+id
                globals.rproc[pkey]=True
                return True
           
            for j in response[topkey]:
                tkey=j[key]+","+j['version']
                try:
                    tresp=client.list_tags_for_resource(resourceARN=j['arn'])
                    print(str(tresp))
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    exn=str(exc_type.__name__)
                    if exn=="AccessDeniedException":
                        print("No Access to tags for "+j['arn']+" returning ...")
                        pkey=type+"."+j[key]
                        globals.rproc[pkey]=True
                        return True
                common.write_import(type,tkey,None)
                globals.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


