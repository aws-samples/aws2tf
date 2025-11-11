import common
import boto3
from botocore.config import Config
import context
import inspect
import os

def get_aws_apigatewayv2_api(type, id, clfn, descfn, topkey, key, filterid):
    #if context.debug:
    print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(
            retries = {
                'max_attempts': 10,
                'mode': 'standard'
            }
        )
        client = boto3.client(clfn,config=config)
        
        paginator = client.get_paginator(descfn)
        for page in paginator.paginate():
            response = response + page[topkey]
        if response == []: 
            if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
            return True
        for j in response:
            if id is None:   
                common.write_import(type,j[key],None) 
                apigw2_dep(j[key])
            elif j[key] == id:  
                common.write_import(type, j[key], None)
                apigw2_dep(j[key])
 


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def apigw2_dep(id):
    try:
        for j in ["aws_apigatewayv2_authorizer","aws_apigatewayv2_deployment","aws_apigatewayv2_integration","aws_apigatewayv2_model","aws_apigatewayv2_route","aws_apigatewayv2_stage"]:
            common.add_dependancy(j,id)

    except Exception as e:
        print("in apigw2_dep: type="+type)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(f"{e=}", fname, exc_tb.tb_lineno)
    return


def get_aws_apigatewayv2_integration(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +  " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:   
        response = common.call_boto3(type,clfn, descfn, topkey, key, id)
        if response == []: 
            if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
            ue
        for j in response:
            retid = j[key]
            theid = id+"/"+retid
            common.write_import(type, theid, None)
        pkey=type+"."+id
        context.rproc[pkey]=True
                    
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_apigatewayv2_authorizer(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +  " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:   
        response = common.call_boto3(type,clfn, descfn, topkey, key, id)
        if response == []: 
            if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
            return True
        for j in response:
            retid = j[key]
            theid = id+"/"+retid
            common.write_import(type, theid, None)
        pkey=type+"."+id
        context.rproc[pkey]=True
                    
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_apigatewayv2_deployment(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +  " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:   
        response = common.call_boto3(type,clfn, descfn, topkey, key, id)
        if response == []: 
            if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
            return True
        for j in response:
            retid = j[key]
            theid = id+"/"+retid
            common.write_import(type, theid, None)
        pkey=type+"."+id
        context.rproc[pkey]=True
                    
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_apigatewayv2_model(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +  " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:   
        response = common.call_boto3(type,clfn, descfn, topkey, key, id)
        if response == []: 
            if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
            return True
        for j in response:
            retid = j[key]
            theid = id+"/"+retid
            common.write_import(type, theid, None)
        pkey=type+"."+id
        context.rproc[pkey]=True
                    
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_apigatewayv2_stage(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +  " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:   
        response = common.call_boto3(type,clfn, descfn, topkey, key, id)
        if response == []: 
            if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
            return True
        for j in response:
            retid = j[key]
            theid = id+"/"+retid
            common.write_import(type, theid, None)
        pkey=type+"."+id
        context.rproc[pkey]=True
                    
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_apigatewayv2_route(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +  " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:   
        response = common.call_boto3(type,clfn, descfn, topkey, key, id)
        if response == []: 
            if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
            return True
        for j in response:
            retid = j[key]
            theid = id+"/"+retid
            common.write_import(type, theid, None)
        pkey=type+"."+id
        context.rproc[pkey]=True
                    
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_apigatewayv2_domain_name(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +  " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:   
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.get_domain_names(MaxResults="32")
            if response == []: 
                if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
                return True

            for j in response[topkey]:
                retid = j[key]
                theid = retid
                common.write_import(type, theid, None)
                pkey=type+"."+theid
                context.rproc[pkey]=True
        else:          
            response = client.get_domain_name(DomainName=id)
            if response == []: 
                if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            j=response    
            retid = j[key]
            theid = retid
            common.write_import(type, theid, None)
            pkey=type+"."+theid
            context.rproc[pkey]=True
                    
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

