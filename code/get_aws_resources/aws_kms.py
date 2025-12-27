import common
from common import log_warning
import logging
log = logging.getLogger('aws2tf')
import context
import os
import sys
import boto3
import botocore
import inspect


def get_aws_kms_key(type,id,clfn,descfn,topkey,key,filterid):
    keyclient=boto3.client('kms')
    if id is not None and "arn:" in id:
        id=id.split("/")[-1]
    if id is not None and id.startswith("k-"):
        id=id.split("k-")[1]
    if context.debug: 
        log.debug("--> In get_aws_kms_key    doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    response=common.call_boto3(type,clfn,descfn,topkey,key,id)
    if response == []: 
        if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
        pkey=type+"."+id
        if not context.rproc[pkey]:
            context.rproc[pkey]=True
        return True
   
    try:
        for j in response: 
            theid=j[key]
            ka="k-"+theid
            # if doesnt start with a k add k- to the start of id
            if id is not None and not id.startswith("k-"): id="k-"+id
            if id is not None and id != ka:
                continue
            else:
                # got to check status of key is "Enabled"
                try:
                    kresp=keyclient.describe_key(KeyId=theid)
             
                    kstatus=kresp['KeyMetadata']['KeyState']
                    kman=kresp['KeyMetadata']['KeyManager']
                    if kstatus == "Enabled" or kstatus == "Disabled":
                        if kman == "AWS":
                            if context.debug: log.debug("key "+str(theid)+" is managed by AWS")
                            pkey=type+"."+theid
                            if not context.rproc[pkey]:
                                context.rproc[pkey]=True
                            pkey=type+"."+ka
                            if not context.rproc[pkey]:
                                context.rproc[pkey]=True
                            continue 
                        common.write_import(type,theid,ka) 
                        # unset tracker
                        pkey=type+"."+ka
                        if not context.rproc[pkey]:
                            context.rproc[pkey]=True
                        pkey=type+"."+theid
                        if not context.rproc[pkey]:
                            context.rproc[pkey]=True
                        common.add_dependancy("aws_kms_alias","k-"+theid)
                    else:
                        log_warning("WARNING: key is not enabled or is managed by AWS")
                        continue
                except Exception as e:
                    if context.debug: log_warning("WARNING: can't access key %s", theid)
                    #exc_type, exc_obj, exc_tb = sys.exc_info()
                    #fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    continue
                
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_kms_alias(type,id,clfn,descfn,topkey,key,filterid):
    if context.debug:
        log.debug("--> In get_aws_kms_alias  doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    response = []
    client = boto3.client(clfn)
    paginator = client.get_paginator(descfn)
    for page in paginator.paginate():
        response = response + page[topkey]
    if response == []: 
        if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
        pkey=type+".k-"+theid
        context.rproc[pkey]=True
        return True
    
    #pkey=type+"."+id
    #if not context.rproc[pkey]:
    #    context.rproc[pkey]=True
    #return True 
    #aws_kms_alias = {"clfn":"kms","descfn":"list_aliases",	"topkey":"Aliases",	"key":"TargetKeyId","filterid":	"AliasName"}

    try:
        for j in response: 
            try:
                theid=j[key] # this will be an id
                aliasname=j['AliasName']
                if aliasname.startswith("alias/aws"):
                    if context.debug: log.debug("Skipping "+aliasname+" "+theid)
                    if id is not None: 
                        if not id.startswith("k-"): id="k-"+id
                        pkey=type+"."+id
                        context.rproc[pkey]=True
                    continue
            except KeyError:
                continue

            ka="k-"+theid

            # if there's an alias match - good enough
            if id is not None:
                if id==aliasname or "alias/"+id==aliasname:
                    if context.debug: log.debug("KMS ALAIS: Alias match importing  %s", id)
                    common.write_import(type,aliasname,ka) 
                    pkey=type+".k-"+theid
                    context.rproc[pkey]=True
                    return True

            # if doesnt start with a k add k- to the start of id
            if id is not None and not id.startswith("k-"): id="k-"+id
            if id is not None and id != ka:
                
                continue
            else:
                if context.debug: log.debug("KMS ALAIS: Id match importing  %s", id)

                common.write_import(type,aliasname,ka) 



    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True