import common
import boto3
import globals
import inspect

def get_aws_ssm_document(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(Filters=[{'Key': 'Owner','Values': ['Self']}]):
                response = response + page[topkey]
            if response == []: 
                print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                common.write_import(type,j[key],None) 

        else:      
            response = client.describe_document(Name=id)
            if response == []: 
                print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            j=response['Document']
            common.write_import(type,id,None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_ssm_association(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is not None and "-" in id:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(AssociationFilterList=[{'key': 'AssociationId','value': id}]):
                response = response + page[topkey]
            if response == []: 
                print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                print("Here ......."+j[key])
                common.write_import(type,j[key],"a-"+j[key]) 

        else:      
            print("WARNING: No id or invalid provided for "+type)
            return True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_ssm_default_patch_baseline(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.get_default_patch_baseline()
            if response == []: 
                print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            j= response
            common.write_import(type,j['BaselineId'],None) 

        else:      
            response = client.get_default_patch_baseline(OperatingSystem=id)
            if response == []: 
                print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            j= response
            common.write_import(type,j['BaselineId'],None) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_ssm_patch_baseline(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: 
                print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                theid=j[key]
                if theid.startswith("pb-"):
                    common.write_import(type,j[key],None) 

        else:      
            response = client.get_patch_baseline(BaselineId=id)
            if response == []: 
                print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            j= response
            common.write_import(type,j['BaselineId'],None) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

