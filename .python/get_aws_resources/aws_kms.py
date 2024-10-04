import common
import globals
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
    if globals.debug: 
        print("--> In get_aws_kms_key    doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    response=common.call_boto3(type,clfn,descfn,topkey,key,id)
    #print("-9a->"+str(response))
    if response == []: 
        print("Empty response for "+type+ " id="+str(id)+" returning")
        pkey=type+"."+id
        if not globals.rproc[pkey]:
            globals.rproc[pkey]=True
        return True
   
    try:
        for j in response: 
            theid=j[key]
            ka="k-"+theid
            #print("ka="+str(ka)+" id="+str(id)+" theid="+str(theid))
            # if doesnt start with a k add k- to the start of id
            if id is not None and not id.startswith("k-"): id="k-"+id
            #print("---k1--- ka="+str(ka)+" id="+str(id)+" theid="+str(theid))
            if id is not None and id != ka:
                continue
            else:
                #print("---k2--- ka="+str(ka)+" id="+str(id)+" theid="+str(theid))
                # got to check status of key is "Enabled"
                try:
                    kresp=keyclient.describe_key(KeyId=theid)
             
                    kstatus=kresp['KeyMetadata']['KeyState']
                    kman=kresp['KeyMetadata']['KeyManager']
                    #print(str(kresp))
                    if kstatus == "Enabled" or kstatus == "Disabled":
                        if kman == "AWS":
                            print("key "+str(theid)+" is managed by AWS")
                            pkey=type+"."+theid
                            if not globals.rproc[pkey]:
                                globals.rproc[pkey]=True
                            pkey=type+"."+ka
                            if not globals.rproc[pkey]:
                                globals.rproc[pkey]=True
                            continue 
                        common.write_import(type,theid,ka) 
                        # unset tracker
                        pkey=type+"."+ka
                        if not globals.rproc[pkey]:
                            globals.rproc[pkey]=True
                        pkey=type+"."+theid
                        if not globals.rproc[pkey]:
                            globals.rproc[pkey]=True
                        common.add_dependancy("aws_kms_alias","k-"+theid)
                    else:
                        print("WARNING: key is not enabled or is managed by AWS")
                        #print(str(kresp))
                        continue
                except Exception as e:
                    print("WARNING: can't access key",theid)
                    #print(f"{e=} [k1]")
                    #exc_type, exc_obj, exc_tb = sys.exc_info()
                    #fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    #print(exc_type, fname, exc_tb.tb_lineno) 
                    continue
                
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_kms_alias(type,id,clfn,descfn,topkey,key,filterid):
    if globals.debug:
        print("--> In get_aws_kms_alias  doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    response = []
    client = boto3.client(clfn)
    paginator = client.get_paginator(descfn)
    for page in paginator.paginate():
        response = response + page[topkey]
    if response == []: 
        print("Empty response for "+type+ " id="+str(id)+" returning"); 
        pkey=type+".k-"+theid
        globals.rproc[pkey]=True
        return True
    
    #pkey=type+"."+id
    #if not globals.rproc[pkey]:
    #    globals.rproc[pkey]=True
    #return True 
    #aws_kms_alias = {"clfn":"kms","descfn":"list_aliases",	"topkey":"Aliases",	"key":"TargetKeyId","filterid":	"AliasName"}

    try:
        for j in response: 
            #print(str(j))
            try:
                theid=j[key] # this will be an id
                aliasname=j['AliasName']
                if aliasname.startswith("alias/aws"):
                    if globals.debug: print("Skipping "+aliasname+" "+theid)
                    if id is not None: 
                        if not id.startswith("k-"): id="k-"+id
                        pkey=type+"."+id
                        globals.rproc[pkey]=True
                    continue
            except KeyError:
                continue

            ka="k-"+theid

            # if there's an alias match - good enough
            if id is not None:
                if id==aliasname or "alias/"+id==aliasname:
                    print("KMS ALAIS: Alias match importing ",id)
                    common.write_import(type,aliasname,ka) 
                    pkey=type+".k-"+theid
                    globals.rproc[pkey]=True
                    return True

            #print("ka="+str(ka)+" id="+str(id)+" theid="+str(theid))
            # if doesnt start with a k add k- to the start of id
            if id is not None and not id.startswith("k-"): id="k-"+id
            if id is not None and id != ka:
                #print("id not equal to ka")
                #print("id="+str(id)+" ka="+str(ka))
                #print("skipping") 
                
                continue
            else:
                print("KMS ALAIS: Id match importing ",id)

                common.write_import(type,aliasname,ka) 



    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True