import common
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect

def get_aws_cloud9_environment_membership(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: 
                log.info("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                uarn=j['userArn']
                pkey=j[key]+"#"+uarn
                common.write_import(type,pkey,"m-"+pkey) 

        else:      
            response = client.describe_environment_memberships(environmentId=id)
            if response == []: 
                log.info("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response[topkey]:
                uarn=j['userArn']
                pkey=j[key]+"#"+uarn
                common.write_import(type,pkey,"m-"+pkey) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_cloud9_environment_ec2(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_environments()
            #print(response)
            if response == []: 
                log.info("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response['environmentIds']:
                common.write_import(type,j,None) 
                response2 = client.describe_environments(environmentIds=[j])
                for k in response2['environments']:    
                    log.info(str(k))


        else:      
            response = client.describe_environments(environmentIds=[id])
            if response == []: 
                log.info("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response['environments']:
                common.write_import(type,j[id],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True