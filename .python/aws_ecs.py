import common
import globals
import sys
import os
import boto3

def get_aws_ecs_cluster(type,id,clfn,descfn,topkey,key,filterid):

    if globals.debug:
        print("--> get_aws_ecs_cluster  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        
        response = []
        response=common.call_boto3(type,clfn,descfn,topkey,id)
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        
        for j in response: 
            retid=j # no key
            cln=retid.split('/')[1]
            common.write_import(type,cln,None) 

    except Exception as e:
            print(f"{e=}")
            print("ERROR: -2->unexpected error in get_aws_ecs_cluster")
            print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            exit()

    return True


def get_aws_ecs_service(type,id,clfn,descfn,topkey,key,filterid):

    if globals.debug:
        print("--> get_aws_ecs_service  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:         
            response = client.list_services()
        else:
            response = client.list_services(cluster=id) 

        response=response[topkey]
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        print(str(response))
        for j in response: 
            retid=j # no key
            cln=retid.split('/')[1]
            common.write_import(type,cln,None) 

    except Exception as e:
            print(f"{e=}")
            print("ERROR: -2->unexpected error in get_aws_ecs_service")
            print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            exit()

    return True