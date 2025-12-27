import common
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect

def get_aws_cognito_user_pool(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        paginator = client.get_paginator(descfn)
        for page in paginator.paginate(MaxResults=32):
            response = response + page[topkey]
        if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response:
            if id is None: 
                #print("---->>>>>"+str(j))
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

def get_aws_cognito_user_group(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id=' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        if id is None: 
            log_warning("Warrning must pass UserPoolId as parameter for"+type); 
            return True
        if ":" in id:
            log.info("Unexpected id in "+type+" id="+id)
            return True
        response = []
        client = boto3.client(clfn)
        
        paginator = client.get_paginator(descfn)
        for page in paginator.paginate(UserPoolId=id):
            response = response + page[topkey]

        if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response:
            pkey=id+"/"+j[key]
            common.write_import(type,pkey,None) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_cognito_user_pool_client(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        if id is None: 
            log_warning("Warrning must pass UserPoolId as parameter for"+type); 
            return True
        if ":" in id:
            log.info("Unexpected id in "+type+" id="+id)
            return True
        response = []
        client = boto3.client(clfn)

        paginator = client.get_paginator(descfn)
        for page in paginator.paginate(UserPoolId=id):
            response = response + page[topkey]
        if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response:
            pkey=id+"/"+j[key]
            common.write_import(type,pkey,None) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

# aws_cognito_identity_pool
def get_aws_cognito_identity_pool(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        paginator = client.get_paginator(descfn)
        for page in paginator.paginate(MaxResults=32):
            response = response + page[topkey]
        if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
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



