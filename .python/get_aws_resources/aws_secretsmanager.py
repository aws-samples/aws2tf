import common
import fixtf
import base64
import boto3
import sys
import os
import globals
import inspect

def get_aws_secretsmanager_secret(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_secretsmanager_secret  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            # calls list_secrets
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(IncludePlannedDeletion=False):
                response = response + page[topkey]
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                
                common.write_import(type,j[key],None) 
                common.add_dependancy("aws_secretsmanager_secret_version",j[key])
                try:
                    print(j['RotationEnabled'])
                    common.add_dependancy("aws_secretsmanager_secret_rotation",j[key])
                except KeyError:
                    print("INFO: No rotation config")


        else:
            response = client.describe_secret(SecretId=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response
            common.write_import(type,j[key],None)
            common.add_dependancy("aws_secretsmanager_secret_rotation",j[key])
            #common.add_dependancy("aws_secretsmanager_secret_version",j[key])


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True



def get_aws_secretsmanager_secret_rotation(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_secretsmanager_secret_rotation  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            print("ERROR: get_aws_secretsmanager_secret_rotation must be called with SecretID as parameter")
        else:
            common.write_import(type,id,None)
         
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True




def get_aws_secretsmanager_secret_version(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_secretsmanager_secret_version  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            # calls list_secret_version
            print("ERROR: get_aws_secretsmanager_secret_verion must be called with SecretID as parameter")
        else:
            response = client.list_secret_version_ids(SecretId=id,IncludeDeprecated=False)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            #print(response)
            for j in response[topkey]:
                pkey=id+"|"+j[key]
                common.write_import(type,pkey,None) 
            pkey=type+"."+id
            globals.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_secretsmanager_secret_policy(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_secretsmanager_secret_policy  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        print("INFO: aws_secretsmanager_policy - policy embedded in aws_secretmager_secret by aws2tf")


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True