import common
import boto3
import globals
import inspect


def get_aws_amplify_app(type, id, clfn, descfn, topkey, key, filterid):
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
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                theid=j[key]
                common.write_import(type,theid,None) 
                common.add_dependancy("aws_amplify_branch", theid)

        else:      
            response = client.get_app(appId=id)
            if response['app'] == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response['app']
            common.write_import(type,j[key],None)
            common.add_dependancy("aws_amplify_branch", j[key])

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_amplify_branch(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is not None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(appId=id):
                response = response + page[topkey]
            if response == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                theid=id+"/"+j[key]
                common.write_import(type,theid,None) 
                pkey="aws_amplify_branch."+id
                globals.rproc[pkey]=True

        else:      
            print("Must pass id for "+type+" returning"); return True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True