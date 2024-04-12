import common
import boto3
import globals
import inspect


def get_aws_db_parameter_group(type, id, clfn, descfn, topkey, key, filterid):


    if globals.debug:
        print("--> In get_aws_db_parameter_group  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        ## id filter here
   
        paginator = client.get_paginator(descfn)
        for page in paginator.paginate():
                response = response + page[topkey]
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        #print(str(response))
        for j in response:
            if id is None:
                common.write_import(type,j[key],None) 
            else:
                if "default." not in id: 
                    did="default."+id
                if did==j[key]: 
                    common.write_import(type,j[key],None)
                else:
                    if id==j[key]:
                        common.write_import(type,j[key],None)

   

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


