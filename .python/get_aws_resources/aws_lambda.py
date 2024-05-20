import common
import boto3
import requests
import globals
import botocore
import inspect


def get_aws_lambda_layer(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator('list_layers')
            for page in paginator.paginate():
                response = response + page['Layers']
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                common.write_import(type,j['LayerArn'],None) 

        else:    
            if "arn:" in id:
                id=id.split(":")[6]  
            response = client.list_layer_versions(LayerName=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                common.write_import(type,j[key],None) 
        

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_lambda_layer_version(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            print("WARNING: Must pass LayerName as parameter")

        else:    
            if "arn:" in id:
                id=id.split(":")[6]  
            response = client.list_layer_versions(LayerName=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                common.write_import(type,j[key],None) 
        

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_lambda_function(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_lambda_function doing " + type + ' with id ' + str(id) +
            " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    response = common.call_boto3(type,clfn, descfn, topkey, key, id)
    #print("-9a->"+str(response))
    
    try:
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
 
        for j in response: 
            fn=j[key]
            if id is not None and id!=fn: continue
            else:
                common.write_import(type, fn, None)
                get_lambda_code(fn)
                common.add_known_dependancy("aws_lambda_alias",fn)
                common.add_known_dependancy("aws_lambda_permission",fn)
                common.add_known_dependancy("aws_lambda_function_event_invoke_config",fn)
                common.add_known_dependancy("aws_lambda_event_source_mapping",fn)


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
        

    return True


def get_lambda_code(fn):
    
    try:
        lc = boto3.client("lambda") 
        resp=lc.get_function(FunctionName=fn)
        if resp['Code']['RepositoryType']=="S3":
            s3loc=resp['Code']['Location']
            r=requests.get(s3loc)
            with open("aws_lambda_function__"+fn+".zip", 'wb') as f:
                f.write(r.content)

    
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)


    return True
    
def get_aws_lambda_alias(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_lambda_alias doing " + type + ' with id ' + str(id) +
            " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    response = common.call_boto3(type,clfn, descfn, topkey, key, id)
    #print("-9a->"+str(response))
    
    try:
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        
        for j in response: 
            #print(str(j))
            fn=j['Name']
            theid=id+"/"+fn
            common.write_import(type, theid, None)
        

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_lambda_permission(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_lambda_permission doing " + type + ' with id ' + str(id) +
            " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    #response = common.call_boto3(type,clfn, descfn, topkey, key, id)
    #print("-9a->"+str(response))
    try:
        # this one no paginate

        client = boto3.client(clfn) 
        if globals.debug: print("client")
        getfn = getattr(client, descfn)
        try:
            response1 = getfn(FunctionName=id)
            response=response1[topkey]
        except client.exceptions.ResourceNotFoundException:
            print("WARNING: ResourceNotFoundException for "+type+ " "+str(id)+" returning")
            return True

        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True

        
        #print("-42a-"+str(response))
           
        fn=response.split('Sid":')[-1].split(',')[0].strip('"')
        #print(str(fn))
        theid=id+"/"+fn
        common.write_import(type, theid, None)
        

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
    
    return True


def get_aws_lambda_function_event_invoke_config(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_lambda_function_event_invoke_config doing " + type + ' with id ' + str(id) +
            " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    #response = common.call_boto3(type,clfn, descfn, topkey, key, id)
    #print("-9a->"+str(response))
    try:
        # this one no paginate

        client = boto3.client(clfn) 
        if globals.debug: print("client")
        getfn = getattr(client, descfn)
        response1 = getfn(FunctionName=id)
        response=response1[topkey]

        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        
        for j in response: 
            print(str(j))
            fn=j['Name']
            theid=id+"/"+fn
            common.write_import(type, theid, None)
        

        
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
        
    return True




def get_aws_lambda_event_source_mapping(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_lambda_event_source_mapping doing " + type + ' with id ' + str(id) +
            " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    #response = common.call_boto3(type,clfn, descfn, topkey, key, id)
    #print("-9a->"+str(response))
    try:
        # this one no paginate

        client = boto3.client(clfn) 
        if globals.debug: print("client")
        getfn = getattr(client, descfn)
        response1 = getfn(FunctionName=id)
        response=response1[topkey]

        if response == []:
            print("Empty response for "+type+ " "+str(id)+" returning")
            return True
        
        for j in response: 
            print(str(j))
            fn=j['UUID']
            theid="l-"+fn

            common.write_import(type, fn, theid)
        

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
    

    return True

def get_aws_lambda_layer_version_permission(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_lambda_layer_version_permission 1 doing " + type + ' with id ' + str(id) +
            " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    #print("-9a->"+str(response))
    try:
        # this one no paginate

        client = boto3.client(clfn) 
        if globals.debug: print("client")
        getfn = getattr(client, descfn)
        try:
            response1 = getfn(LayerName=id)
            response=response1[topkey]
        except client.exceptions.ResourceNotFoundException:
            print("WARNING: ResourceNotFoundException for "+type+ " "+str(id)+" returning")
            return True

        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True

        
        print("-42a-"+str(response))
        ### id = "arn:aws:lambda:us-west-2:123456654321:layer:test_layer1,1"
        
        for j in response:
            layn=j['LayerVersionArn']
            ver=j['Version']
            theid=id+","+str(ver)
            altid=theid.replace(",", "_").replace(":", "_").replace("|", "_")
            common.write_import(type, theid, altid)
        

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
    
    return True
