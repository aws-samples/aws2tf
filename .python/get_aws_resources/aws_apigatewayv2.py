import common
import boto3
import globals
import inspect
import os



def get_aws_apigatewayv2_api(type, id, clfn, descfn, topkey, key, filterid):
    #if globals.debug:
    print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        
        paginator = client.get_paginator(descfn)
        for page in paginator.paginate():
            response = response + page[topkey]
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
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
        #for j in ["aws_apigatewayv2_authorizer","aws_apigatewayv2_deployment","aws_apigatewayv2_integration","aws_apigatewayv2_model","aws_apigatewayv2_route","aws_apigatewayv2_stage"]:
        for j in ["aws_apigatewayv2_deployment","aws_apigatewayv2_integration","aws_apigatewayv2_authorizer"]:

            common.add_dependancy(j,id)

            #print("------------"+str(pkey))
            #globals.rproc[pkey]=True
    except Exception as e:
        print("in apigw2_dep: type="+type)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(f"{e=}", fname, exc_tb.tb_lineno)
    return


def get_aws_apigatewayv2_integration(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +  " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:   
        response = common.call_boto3(type,clfn, descfn, topkey, key, id)
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response:
            retid = j[key]
            theid = id+"/"+retid
            common.write_import(type, theid, None)
        pkey=type+"."+id
        globals.rproc[pkey]=True
                    
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_apigatewayv2_authorizer(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +  " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:   
        response = common.call_boto3(type,clfn, descfn, topkey, key, id)
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response:
            retid = j[key]
            theid = id+"/"+retid
            common.write_import(type, theid, None)
        pkey=type+"."+id
        globals.rproc[pkey]=True
                    
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_apigatewayv2_deployment(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +  " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:   
        response = common.call_boto3(type,clfn, descfn, topkey, key, id)
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response:
            retid = j[key]
            theid = id+"/"+retid
            common.write_import(type, theid, None)
        pkey=type+"."+id
        globals.rproc[pkey]=True
                    
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

