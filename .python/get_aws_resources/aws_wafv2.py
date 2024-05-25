import common
import boto3
import globals
import inspect

def get_aws_wafv2_ip_set(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None: # assume scope = cloudfront

            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(Scope='CLOUDFRONT'):
                response = response + page[topkey]
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                common.write_import(type,j[key],None) 

        else: 
            nm=id.split("|")[0]
            idd=id.split("|")[1]
            sc=id.split("|")[2]  
            response = client.get_ip_set(Scope=sc,Name=nm,Id=idd)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response['IPSet']
            pkey=idd+"/"+nm+"/"+sc
            common.write_import(type,pkey,"i-"+pkey.replace("/","_"))

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True



def get_aws_wafv2_web_acl(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None: # assume scope = cloudfront

            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(Scope='CLOUDFRONT'):
                response = response + page[topkey]
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                common.write_import(type,j[key],None) 

        else: 
            nm=id.split("|")[0]
            idd=id.split("|")[1]
            sc=id.split("|")[2]  
            response = client.get_web_acl(Scope=sc,Name=nm,Id=idd)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response['WebACL']
            pkey=idd+"/"+nm+"/"+sc
            common.write_import(type,pkey,"w-"+pkey.replace("/","_"))

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

