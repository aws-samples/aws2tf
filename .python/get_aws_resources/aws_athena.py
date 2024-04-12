import common
import boto3
import globals
import os
import sys
import inspect



def get_aws_athena_workgroup(type, id, clfn, descfn, topkey, key, filterid):

    if globals.debug:
        print("--> In get_aws_glue_trigger  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_work_groups()
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response['WorkGroups']:
                pkey=j[key]
                common.write_import(type,pkey,None) 

        else:          
            response = client.get_work_group(WorkGroup=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response[topkey]
            pkey=j[key]
            common.write_import(type,pkey,None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
            

    return True