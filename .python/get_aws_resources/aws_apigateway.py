import common
import boto3
import globals
import os
import sys
import inspect

def get_aws_api_gateway_account(type, id, clfn, descfn, topkey, key, filterid):

    if globals.debug:
        print("--> get_aws_api_gateway_account  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:         
            response = client.get_account()
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response
            common.write_import(type,"api-gateway-account",None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
            

    return True