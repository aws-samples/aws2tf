import common
import boto3
import globals
import inspect


def get_aws_bedrock_model_invocation_logging_configuration(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
    
        response = client.get_model_invocation_logging_configuration()

        try:
            j=response[topkey]
        except KeyError:
            print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        common.write_import(type,globals.region,None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
        print("Empty response for "+type+ " id="+str(id)+" returning"); return True
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
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                resp2 = client.list_guardrails(guardrailIdentifier=j[key])
                for k in resp2[topkey]:
                    tkey=k[key]+","+k['version']
                    common.write_import(type,tkey,None) 

        else:      
            response = client.list_guardrails(guardrailIdentifier=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
           
            for j in response[topkey]:
                tkey=j[key]+","+j['version']
                common.write_import(type,tkey,None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


