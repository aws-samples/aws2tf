import common
import boto3
import globals
import os
import sys

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
            print(f"{e=}")
            print("ERROR: -2->unexpected error in get_aws_api_gateway_account")
            print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            exit()

    return True