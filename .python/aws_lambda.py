import common
import os
import sys
import boto3
import requests
import globals
import botocore

def get_aws_lambda_function(type, id, clfn, descfn, topkey, key, filterid):
    #if globals.debug:
    print("--> In get_aws_lambda_function doing " + type + ' with id ' + str(id) +
            " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    response = common.call_boto3(clfn, descfn, topkey, id)
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
        print(f"{e=}")
        print("ERROR: -2->unexpected error in get_aws_lambda_function")
        print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        exit()

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
        print(f"{e=}")
        print("ERROR: -2->unexpected error in get_lambda_code")
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        exit()

    return True
    
def get_aws_lambda_alias(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_lambda_alias doing " + type + ' with id ' + str(id) +
            " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    response = common.call_boto3(clfn, descfn, topkey, id)
    #print("-9a->"+str(response))
    
    try:
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        
        for j in response: 
            #print(str(j))
            fn=j['Name']
            theid=id+"/"+fn
            common.write_import(type, theid, None)
        

    except Exception as e:
        print(f"{e=}")
        print("ERROR: -2->unexpected error in get_aws_lambda_function")
        print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        exit()

    return True


def get_aws_lambda_permission(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_lambda_permission doing " + type + ' with id ' + str(id) +
            " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    #response = common.call_boto3(clfn, descfn, topkey, id)
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
        print(f"{e=}")
        print("ERROR: -2->unexpected error in get_aws_lambda_function")
        print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        exit()

    return True


def get_aws_lambda_function_event_invoke_config(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_lambda_function_event_invoke_config doing " + type + ' with id ' + str(id) +
            " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    #response = common.call_boto3(clfn, descfn, topkey, id)
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
        print(f"{e=}")
        print("ERROR: -2->unexpected error in get_aws_lambda_function")
        print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        exit()

    return True




def get_aws_lambda_event_source_mapping(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_lambda_event_source_mapping doing " + type + ' with id ' + str(id) +
            " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    #response = common.call_boto3(clfn, descfn, topkey, id)
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
            theid=fn
            common.write_import(type, theid, None)
        

    except Exception as e:
        print(f"{e=}")
        print("ERROR: -2->unexpected error in get_aws_lambda_function")
        print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        exit()

    return True