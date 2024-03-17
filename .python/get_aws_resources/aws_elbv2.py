import common
import globals
import sys
import os
import boto3
import botocore

def get_aws_lb_listener(type,id,clfn,descfn,topkey,key,filterid):

    if globals.debug:
        print("--> get_aws_lb_listener  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        client = boto3.client(clfn)
        response = []
        response = client.describe_listeners(ListenerArns=[id])
        response=response[topkey]
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        
        for j in response: 
            retid=j[key] # no key
            common.write_import(type,id,None) 

    except Exception as e:
            print(f"{e=}")
            print("ERROR: -2->unexpected error in get_aws_lb_listener")
            print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            exit()

    return True