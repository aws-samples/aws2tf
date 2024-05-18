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