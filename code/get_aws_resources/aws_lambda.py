import common
from common import log_warning
import logging
log = logging.getLogger('aws2tf')
import boto3
import requests
import context
import botocore
import inspect
import sys
from botocore.config import Config
from botocore.exceptions import ClientError


def get_aws_lambda_layer(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator('list_layers')
            for page in paginator.paginate():
                response = response + page['Layers']
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                common.write_import(type,j['LayerArn'],None) 

        else:    
            if "arn:" in id:
                id=id.split(":")[6]  
            response = client.list_layer_versions(LayerName=id)
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response[topkey]:
                common.write_import(type,j[key],None) 
        

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_lambda_layer_version(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        tarn=""
        if id is None:
            log_warning("WARNING: Must pass LayerName/ARN as parameter")
        
        else:    
            if id.startswith("arn:"):
                larn=id.split(":")[:-1]
                myarn=""
                for ta in larn:
                    myarn=myarn+ta+":"
              
                myarn=myarn.rstrip(":")
            
                try:
                    response = client.list_layer_versions(LayerName=myarn)
                except botocore.exceptions.ClientError as e:

                    log.info("\nERROR: Lambda function is referencing Lambda Layer - "+ myarn+ " which does not exist")
                    log.info("ERROR: This will cause problems later on and should be addressed\n")
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    exn=str(exc_type.__name__)
                    #if "AccessDeniedException" in exn:
                    pkey=type+"."+id
                    context.rproc[pkey]=True
                    return True
                
                if response[topkey] == []: 
                    if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
                    log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
                    pkey=type+"."+id
                    context.rproc[pkey]=True
                    return True
                for j in response[topkey]:
                    get_lambdalayer_code(j[key])
                    common.write_import(type,j[key],None) 
                    tarn=j['LayerVersionArn']
                    pkey=type+"."+tarn
                    context.rproc[pkey]=True
        

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_lambda_function(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn,config=config)
        if id is None:
            for fn in context.lambdalist.keys():
                ## try access here first 
                common.write_import(type, fn, None)
                get_lambda_code(fn)
                common.add_known_dependancy("aws_lambda_alias",fn)
                common.add_known_dependancy("aws_lambda_permission",fn)
                common.add_known_dependancy("aws_lambda_function_event_invoke_config",fn)
                common.add_known_dependancy("aws_lambda_event_source_mapping",fn)
                common.write_import(type,fn,None) 
                #pkey=type+"."+fn
                #context.rproc[pkey]=True
                #pkey=type+"."+j['FunctionArn']
                pkey=type+"."+fn
                context.rproc[pkey]=True

        else:      
            if id.startswith("arn:"): 
                farn=id
                id=id.split(":")[-1]

            try:
                if context.lambdalist[id]:
                    fn=id
                    common.write_import(type, fn, None)
                    get_lambda_code(fn)
                    common.add_known_dependancy("aws_lambda_alias",fn)
                    common.add_known_dependancy("aws_lambda_permission",fn)
                    common.add_known_dependancy("aws_lambda_function_event_invoke_config",fn)
                    common.add_known_dependancy("aws_lambda_event_source_mapping",fn)
                    #pkey=type+"."+j['FunctionArn']
                    pkey=type+"."+fn
                    context.rproc[pkey]=True


            except KeyError:
                    log_warning("WARNING: function not in lambda list " + id+ " Resource may be referencing a lambda that no longer exists") 
                    pkey=type+"."+id
                    context.rproc[pkey]=True


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True




def get_aws_lambda_function_old(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn,config=config)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            for j in response:
                fn=j[key]
                ## try access here first 
                common.write_import(type, fn, None)
                get_lambda_code(fn)
                common.add_known_dependancy("aws_lambda_alias",fn)
                common.add_known_dependancy("aws_lambda_permission",fn)
                common.add_known_dependancy("aws_lambda_function_event_invoke_config",fn)
                common.add_known_dependancy("aws_lambda_event_source_mapping",fn)
                common.write_import(type,j[key],None) 
                #pkey=type+"."+fn
                #context.rproc[pkey]=True
                pkey=type+"."+j['FunctionArn']
                context.rproc[pkey]=True


        else:      
            if id.startswith("arn:"): 
                farn=id
                id=id.split(":")[-1]

            response = client.get_function(FunctionName=id)
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            j=response['Configuration']
            fn=j[key]
            common.write_import(type, fn, None)
            get_lambda_code(fn)
            common.add_known_dependancy("aws_lambda_alias",fn)
            common.add_known_dependancy("aws_lambda_permission",fn)
            common.add_known_dependancy("aws_lambda_function_event_invoke_config",fn)
            common.add_known_dependancy("aws_lambda_event_source_mapping",fn)
            pkey=type+"."+j['FunctionArn']
            context.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_lambda_code(fn):
    
    try:
        clfn="lambda"
        lc = boto3.client(clfn) 
        resp=lc.get_function(FunctionName=fn)
        if resp['Code']['RepositoryType']=="S3":
            s3loc=resp['Code']['Location']
            r=requests.get(s3loc)
            with open("aws_lambda_function__"+fn+".zip", 'wb') as f:
                f.write(r.content)

    except Exception as e:
        descfn="get_lambda_code"
        topkey=fn
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_lambdalayer_code(fn):
    
    try:
        if fn.startswith("arn:"):
            tarn=fn.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_")
            clfn="lambda" 
            lc = boto3.client(clfn) 
            resp=lc.get_layer_version_by_arn(Arn=fn)
            s3loc=resp['Content']['Location']
            r=requests.get(s3loc)
            with open("aws_lambda_layer_version__"+tarn+".zip", 'wb') as f:
                f.write(r.content)

    except Exception as e:
        descfn="get_lambdalayer_code"
        topkey=fn
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True



def get_aws_lambda_alias(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In get_aws_lambda_alias doing " + type + ' with id ' + str(id) +
            " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    response = common.call_boto3(type,clfn, descfn, topkey, key, id)
    
    try:
        if response == []: 
            if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
            return True
        
        for j in response: 
            fn=j['Name']
            theid=id+"/"+fn
            common.write_import(type, theid, None)
        

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_lambda_permission(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In get_aws_lambda_permission doing " + type + ' with id ' + str(id) +
            " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        # this one no paginate

        client = boto3.client(clfn) 
        if context.debug: log.debug("client")
        getfn = getattr(client, descfn)
        try:
            response1 = getfn(FunctionName=id)
            response=response1[topkey]
        except client.exceptions.ResourceNotFoundException:
            if context.debug: log_warning("WARNING: ResourceNotFoundException for "+type+ " "+str(id)+" returning")
            return True

        if response == []: 
            if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
            return True

        
           
        fn=response.split('Sid":')[-1].split(',')[0].strip('"')
        theid=id+"/"+fn
        common.write_import(type, theid, None)
        

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
    
    return True


def get_aws_lambda_function_event_invoke_config(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In get_aws_lambda_function_event_invoke_config doing " + type + ' with id ' + str(id) +
            " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    try:
        # this one no paginate

        client = boto3.client(clfn) 
        if context.debug: log.debug("client")
        getfn = getattr(client, descfn)
        response1 = getfn(FunctionName=id)
        response=response1[topkey]

        if response == []: 
            if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
            return True
        
        for j in response: 
            fn=j['FunctionArn']
            theid=fn
            common.write_import(type, theid, None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
        
    return True




def get_aws_lambda_event_source_mapping(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In get_aws_lambda_event_source_mapping doing " + type + ' with id ' + str(id) +
            " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    #response = common.call_boto3(type,clfn, descfn, topkey, key, id)
    try:
        # this one no paginate

        client = boto3.client(clfn) 
        if context.debug: log.debug("client")
        getfn = getattr(client, descfn)
        response1 = getfn(FunctionName=id)
        response=response1[topkey]

        if response == []:
            if context.debug: log.debug("Empty response for "+type+ " "+str(id)+" returning")
            return True
        
        for j in response: 
            fn=j['UUID']
            theid="l-"+fn

            common.write_import(type, fn, theid)
        

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
    

    return True

def get_aws_lambda_layer_version_permission(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In get_aws_lambda_layer_version_permission 1 doing " + type + ' with id ' + str(id) +
            " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    try:
        # this one no paginate

        client = boto3.client(clfn) 
        if context.debug: log.debug("client")
        getfn = getattr(client, descfn)
        try:
            response1 = getfn(LayerName=id)
            response=response1[topkey]
        except client.exceptions.ResourceNotFoundException:
            if context.debug: log_warning("WARNING: ResourceNotFoundException for "+type+ " "+str(id)+" returning")
            return True

        if response == []: 
            if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
            return True

        
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


def get_aws_lambda_function_recursion_config(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all Lambda functions first
            paginator = client.get_paginator('list_functions')
            functions = []
            for page in paginator.paginate():
                functions = functions + page['Functions']
            
            # Get recursion config for each function
            for func in functions:
                try:
                    response = client.get_function_recursion_config(FunctionName=func['FunctionName'])
                    # Only import if recursion config is explicitly set (not default)
                    if response.get('RecursiveLoop'):
                        common.write_import(type, func['FunctionName'], None)
                except ClientError as e:
                    if e.response['Error']['Code'] == 'ResourceNotFoundException':
                        continue
                    raise
        else:
            # Get specific function's recursion config
            response = client.get_function_recursion_config(FunctionName=id)
            if response.get('RecursiveLoop'):
                common.write_import(type, id, None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_lambda_capacity_provider(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all capacity providers
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []:
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                # Extract name from ARN: arn:aws:lambda:region:account:capacity-provider:name
                arn = j[key]
                name = arn.split(':')[-1]
                common.write_import(type, name, None)
        else:
            # Get specific capacity provider
            response = client.get_capacity_provider(Name=id)
            if response.get('CapacityProvider'):
                j = response['CapacityProvider']
                arn = j[key]
                name = arn.split(':')[-1]
                common.write_import(type, name, None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True
