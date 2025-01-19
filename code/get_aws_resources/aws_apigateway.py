import common
import boto3
from botocore.config import Config
import globals
import inspect

def get_aws_api_gateway_account(type, id, clfn, descfn, topkey, key, filterid):

    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:         
            response = client.get_account()
            if response == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                pkey=type+"."+id
                globals.rproc[pkey]=True
                return True
            j=response
            common.write_import(type,"api-gateway-account",None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
            

    return True

def get_aws_api_gateway_deployment(type, id, clfn, descfn, topkey, key, filterid):

    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is not None:  
            response = client.get_deployments(restApiId=id)
            if response[topkey] == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                pkey=type+"."+id
                globals.rproc[pkey]=True 
                return True
            for j in response[topkey]:
                pkey=id+"/"+j[key]
                altk="r-"+pkey
            
                common.write_import(type,pkey,altk)
                pkey=type+"."+id
                globals.rproc[pkey]=True
        else:
            print("Must pass id for "+type+" returning")
            return True

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
            if response == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                altk="r-"+j[key]
                common.write_import(type,j[key],altk) 
                common.add_dependancy("aws_api_gateway_deployment", j[key])
                common.add_dependancy("aws_api_gateway_stage", j[key])
                common.add_dependancy("aws_api_gateway_authorizer", j[key])
                common.add_dependancy("aws_api_gateway_resource", j[key])

        else:      
            response = client.get_rest_api(restApiId=id)
            if response == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            j=response
            altk="r-"+j[key]
            common.write_import(type,j[key],altk)
            common.add_dependancy("aws_api_gateway_deployment", j[key])
            common.add_dependancy("aws_api_gateway_stage", j[key])
            common.add_dependancy("aws_api_gateway_resource", j[key])
            common.add_dependancy("aws_api_gateway_authorizer", j[key])


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
            

    return True

def get_aws_api_gateway_stage(type, id, clfn, descfn, topkey, key, filterid):

    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)    
    try:
        response = []
        client = boto3.client(clfn)
        if id is not None:  
            response = client.get_stages(restApiId=id)
            if response[topkey] == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                pkey=type+"."+id
                globals.rproc[pkey]=True
                return True
            for j in response[topkey]:
                pkey=id+"/"+j[key]
                altk="r-"+pkey
                common.write_import(type,pkey,altk)
                pkey=type+"."+id
                globals.rproc[pkey]=True
        else:
            print("Must pass id for "+type+" returning")
            return True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
            
    return True

def get_aws_api_gateway_authorizer(type, id, clfn, descfn, topkey, key, filterid):

    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)    
    try:
        response = []
        client = boto3.client(clfn)
        if id is not None:  
            response = client.get_authorizers(restApiId=id)
            if response[topkey] == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
                pkey=type+"."+id
                globals.rproc[pkey]=True
                return True
            for j in response[topkey]:
                pkey=id+"/"+j[key]
                altk="r-"+pkey
                common.write_import(type,pkey,altk)
                pkey=type+"."+id
                globals.rproc[pkey]=True
        else:
            print("Must pass id for "+type+" returning")
            return True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
            
    return True

def get_aws_api_gateway_resource(type, id, clfn, descfn, topkey, key, filterid):

    if globals.debug:
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
        if id is not None:  
            response = client.get_resources(restApiId=id)
            if response[topkey] == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                pkey=type+"."+id
                globals.rproc[pkey]=True
                return True
            for j in response[topkey]:
                pkey=id+"/"+j[key]
                altk="r-"+pkey
                common.write_import(type,pkey,altk)
                common.add_dependancy("aws_api_gateway_method", id+"/"+j[key])
                pkey=type+"."+id
                globals.rproc[pkey]=True
        else:
            print("Must pass id for "+type+" returning")
            return True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
            
    return True

def get_aws_api_gateway_method(type, id, clfn, descfn, topkey, key, filterid):

    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)    
    try:
        response = []
        client = boto3.client(clfn)
        if id is not None and "/" in id:  
            restid=id.split("/")[0]
            resid=id.split("/")[1]
            #print("restid="+restid+" resid="+resid)
            try:
                response = client.get_method(restApiId=restid,resourceId=resid,httpMethod='GET')
                if response == []: 
                    if globals.debug: print("Empty GET response for "+type+ " id="+str(id))
                    pkey=type+"."+id
                    globals.rproc[pkey]=True
                    return True
                j=response
                pkey=restid+"/"+resid+"/"+j[key]
                altk="r-"+pkey
                common.write_import(type,pkey,altk)
            except:
                if globals.debug: print("Empty GET response for "+type+ " id="+str(id))
                

            ## POST
            try:
                response = client.get_method(restApiId=restid,resourceId=resid,httpMethod='POST')
                if response == []: 
                    if globals.debug: print("Empty POST response for "+type+ " id="+str(id))
                    pkey=type+"."+id
                    globals.rproc[pkey]=True
                    return True
                j=response
                pkey=restid+"/"+resid+"/"+j[key]
                altk="r-"+pkey
                common.write_import(type,pkey,altk)
            except:
                if globals.debug: print("Empty POST response for "+type+ " id="+str(id))

            ## PUT
            try:
                response = client.get_method(restApiId=restid,resourceId=resid,httpMethod='PUT')
                if response == []: 
                    if globals.debug: print("Empty PUT response for "+type+ " id="+str(id))
                    pkey=type+"."+id
                    globals.rproc[pkey]=True
                    return True
                j=response
                pkey=restid+"/"+resid+"/"+j[key]
                altk="r-"+pkey
                common.write_import(type,pkey,altk)
            except:
                if globals.debug: print("Empty PUT response for "+type+ " id="+str(id))

            ## DELETE
            try:
                response = client.get_method(restApiId=restid,resourceId=resid,httpMethod='DELETE')
                if response == []: 
                    if globals.debug: print("Empty DELETE response for "+type+ " id="+str(id))
                    pkey=type+"."+id
                    globals.rproc[pkey]=True
                    return True
                j=response
                pkey=restid+"/"+resid+"/"+j[key]
                altk="r-"+pkey
                common.write_import(type,pkey,altk)
            except:
                if globals.debug: print("Empty DELETE response for "+type+ " id="+str(id))


            ## PATCH
            try:
                response = client.get_method(restApiId=restid,resourceId=resid,httpMethod='PATCH')
                if response == []: 
                    if globals.debug: print("Empty PATCH response for "+type+ " id="+str(id))
                    pkey=type+"."+id
                    globals.rproc[pkey]=True
                    return True
                j=response
                pkey=restid+"/"+resid+"/"+j[key]
                altk="r-"+pkey
                common.write_import(type,pkey,altk)
            except:
                if globals.debug: print("Empty PATCH response for "+type+ " id="+str(id))


            
            pkey=restid+"/"+resid
            pkey=type+"."+pkey
            globals.rproc[pkey]=True

        else:
            print("Must pass Rest api id / Resource id for "+type+" returning")
            return True

    except Exception as e:
        print("--Error in "+str(inspect.currentframe().f_code.co_name)+" doing " + clfn + ' with id ' + str(id),str(descfn),str(topkey))
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
            
    return True