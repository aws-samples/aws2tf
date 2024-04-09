import common
import globals
import os
import sys
import boto3
import botocore

def get_aws_kms_key(type,id,clfn,descfn,topkey,key,filterid):
    keyclient=boto3.client('kms')
    if "arn:" in id:
        id=id.split("/")[-1]
    #if globals.debug: print("--> In get_aws_kms_key    doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    print("--> In get_aws_kms_key    doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    response=common.call_boto3(type,clfn,descfn,topkey,key,id)
    #print("-9a->"+str(response))
    if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
   
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

                    if kstatus == "Enabled": #and kman != "AWS":
                        common.write_import(type,theid,ka) 
                        # unset tracker
                        pkey=type+"."+ka
                        if not globals.rproc[pkey]:
                            globals.rproc[pkey]=True
                        common.add_dependancy("aws_kms_alias","k-"+theid)
                    else:
                        print("WARNING: key is not enabled or is managed by AWS")
                        print(str(kresp))
                        continue
                except Exception as e:
                    print("WARNING: can't access key")
                    print(f"{e=}")
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno) 
                    continue
                
    except Exception as e:
        print(f"{e=}")
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno) 

    return True

def get_aws_kms_alias(type,id,clfn,descfn,topkey,key,filterid):
    #if globals.debug: print("--> In get_aws_kms_key    doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    print("--> In get_aws_kms_alias  doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

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
            #print(str(j))
            try:
                theid=j[key]
                aliasname=j['AliasName']
                if aliasname.startswith("alias/aws"):
                    print("Skipping "+aliasname+" "+theid)
                    pkey=type+".k-"+theid
                    globals.rproc[pkey]=True
                    continue
            except KeyError:
                continue
            ka="k-"+theid
            #print("ka="+str(ka)+" id="+str(id)+" theid="+str(theid))
            # if doesnt start with a k add k- to the start of id
            if id is not None and not id.startswith("k-"): id="k-"+id
            if id is not None and id != ka:
                #print("id not equal to ka")
                #print("id="+str(id)+" ka="+str(ka))
                #print("skipping") 
                
                continue
            else:
                #print("--- id equal to ka")
                #print("ka="+str(ka)+" id="+str(id)+" theid="+str(theid))
                common.write_import(type,aliasname,ka) 

                    #write_import(type,theid,tfid)
                    #f.write('import {\n')
                    #f.write('  to = ' +type + '.' + tfid + '\n')
                    #f.write('  id = "'+ theid + '"\n')
                    #f.write('}\n')

                    #pkey=type+"."+tfid

    except Exception as e:
        print(f"{e=}")
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno) 
        exit()

    return True