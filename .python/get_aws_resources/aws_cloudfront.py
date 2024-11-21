import common
import boto3
import globals
import inspect

def get_aws_cloudfront_distribution(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                try:
                    response = response + page['DistributionList']['Items']
                except KeyError:
                    print("No DistributionList in response for "+type+ " id="+str(id)+" returning"); 
                    return True
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                common.write_import(type,j[key],None) 

        else:      
            response = client.get_distribution(Id=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response['Distribution']
            common.write_import(type,j[key],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_cloudfront_origin_access_identity(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                try:
                    response = response + page[topkey]['Items']
                except KeyError:
                    print("No "+str(topkey)+" items in response for "+type+ " id="+str(id)+" returning")
                    return True
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                common.write_import(type,j[key],None) 

        else:      
            response = client.get_cloud_front_origin_access_identity(Id=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response['CloudFrontOriginAccessIdentity']
            common.write_import(type,j[key],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_cloudfront_cache_policy(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_cache_policies()
            if response[topkey]['Items'] == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]['Items']:
                oid=j['CachePolicy']['Id']
                common.write_import(type,oid,"o-"+oid) 

        else:      
            response = client.get_cache_policy(Id=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            common.write_import(type,id,"o-"+id) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_cloudfront_continuous_deployment_policy(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_continuous_deployment_policies()
            if response[topkey]['Items'] == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        
            for j in response[topkey]['Items']:    
                oid=j['ContinuousDeploymentPolicy']['Id']
                common.write_import(type,oid,"o-"+oid) 

        else:      
            response = client.get_continuous_deployment_policy(Id=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True

            common.write_import(type,id,"o-"+id) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_cloudfront_field_level_encryption_config(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_field_level_encryption_configs()
            try:
                resp2=response[topkey]['Items']
            except KeyError:
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            if response[topkey]['Items'] == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]['Items']:
                oid=j[key]
                common.write_import(type,oid,"o-"+oid) 

        else:      
            response = client.get_field_level_encryption_config(Id=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            common.write_import(type,id,"o-"+id) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_cloudfront_field_level_encryption_profile(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_field_level_encryption_profiles()
            try:
                resp2=response[topkey]['Items']
            except KeyError:
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            if response[topkey]['Items'] == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]['Items']:
                oid=j[key]
                common.write_import(type,oid,"o-"+oid) 

        else:      
            response = client.get_field_level_encryption_profile(Id=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            common.write_import(type,id,"o-"+id) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True



 
#aws_cloudfront_response_headers_policy
def get_aws_cloudfront_response_headers_policy(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_response_headers_policies()
            try:
                resp2=response[topkey]['Items']
            except KeyError:
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            
            if response[topkey]['Items'] == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]['Items']:
                oid=j['ResponseHeadersPolicy'][key]
                common.write_import(type,oid,"o-"+oid) 

        else:      
            response = client.get_response_headers_policy(Id=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            common.write_import(type,id,"o-"+id) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

##aws_cloudfront_function
def get_aws_cloudfront_function(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_functions()
            try:
                resp2=response[topkey]['Items']
            except KeyError:
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            
            if response[topkey]['Items'] == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]['Items']:
                oid=j[key]
                common.write_import(type,oid,None) 

        else:      
            response = client.get_function(Name=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            common.write_import(type,id) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

##aws_cloudfront_key_group
def get_aws_cloudfront_key_group(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_key_groups()
            try:
                resp2=response[topkey]['Items']
            except KeyError:
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            
            if response[topkey]['Items'] == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]['Items']:
                oid=j['KeyGroup'][key]
                common.write_import(type,oid,"o-"+oid)

        else:      
            response = client.get_key_group(Name=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            common.write_import(type,id,"o-"+id) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


## aws_cloudfront_origin_access_control
def get_aws_cloudfront_origin_access_control(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_origin_access_controls()
            try:
                resp2=response[topkey]['Items']
            except KeyError:
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            
            if response[topkey]['Items'] == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]['Items']:
                oid=j[key]
                common.write_import(type,oid,"o-"+oid)

        else:      
            response = client.get_origin_access_control(Id=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            common.write_import(type,id,"o-"+id) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

## aws_cloudfront_origin_request_policy
def get_aws_cloudfront_origin_request_policy(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_origin_request_policies()
            try:
                resp2=response[topkey]['Items']
            except KeyError:
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            
            if response[topkey]['Items'] == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]['Items']:
                oid=j['OriginRequestPolicy'][key]
                common.write_import(type,oid,"o-"+oid)

        else:      
            response = client.get_origin_request_policy(Id=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            common.write_import(type,id,"o-"+id) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

## aws_cloudfront_public_key
def get_aws_cloudfront_public_key(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_public_keys()
            try:
                resp2=response[topkey]['Items']
            except KeyError:
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            
            if response[topkey]['Items'] == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]['Items']:
                oid=j[key]
                common.write_import(type,oid,"o-"+oid)

        else:      
            response = client.get_public_key(Id=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            common.write_import(type,id,"o-"+id) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

## aws_cloudfront_realtime_log_config
def get_aws_cloudfront_realtime_log_config(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_realtime_log_configs()
            try:
                resp2=response[topkey]['Items']
            except KeyError:
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            
            if response[topkey]['Items'] == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]['Items']:
                oid=j[key]
                common.write_import(type,oid,"o-"+oid)

        else:      
            response = client.get_realtime_log_config(Id=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            common.write_import(type,id,"o-"+id) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True