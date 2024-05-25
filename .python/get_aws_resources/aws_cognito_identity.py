import common
import boto3
import globals
import inspect


# aws_cognito_identity_pool
def get_aws_cognito_identity_pool(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        paginator = client.get_paginator(descfn)
        for page in paginator.paginate(MaxResults=32):
            response = response + page[topkey]
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response:
            if id is None: 
                common.write_import(type,j[key],None) 
                common.add_known_dependancy("aws_cognito_user_group", j[key])
                common.add_known_dependancy("aws_cognito_user_pool_client", j[key])
            elif j[key] == id:
                common.write_import(type,j[key],None) 
                common.add_known_dependancy("aws_cognito_user_group", j[key])
                common.add_known_dependancy("aws_cognito_user_pool_client", j[key])


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True