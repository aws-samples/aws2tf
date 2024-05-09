import common
import boto3
import globals
import inspect

def get_aws_api_gateway_account(type, id, clfn, descfn, topkey, key, filterid):

    if globals.debug:
        print("--> get_aws_api_gateway_account  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:         
            response = client.get_account()
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response
            common.write_import(type,"api-gateway-account",None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
            

    return True

def get_aws_api_gateway_deployment(type, id, clfn, descfn, topkey, key, filterid):

    if globals.debug:
        print("--> get_aws_api_gateway_account  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is not None:  
            response = client.get_deployments(restApiId=id)
            if response[topkey] == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                print(str(j))
                pkey=id+"/"+j[key]
                common.write_import(type,pkey,None)
                pkey=type+"."+id
                globals.rproc[pkey]=True
        else:
            print("Must pass id for "+type+" returning"); return True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
            

    return True

def get_aws_api_gateway_rest_api(type, id, clfn, descfn, topkey, key, filterid):

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
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                common.write_import(type,j[key],None) 
                common.add_dependancy("aws_api_gateway_deployment", j[key])

        else:      
            response = client.get_rest_api(restApiId=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response
            common.write_import(type,j[key],None)
            common.add_dependancy("aws_api_gateway_deployment", j[key])


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
            

    return True