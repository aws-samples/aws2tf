import common
from common import log_warning
import logging
log = logging.getLogger('aws2tf')
import boto3
from botocore.config import Config
import context
import inspect

def get_aws_api_gateway_account(type, id, clfn, descfn, topkey, key, filterid):

    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:         
            response = client.get_account()
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                pkey=type+"."+id
                context.rproc[pkey]=True
                return True
            j=response
            common.write_import(type,"api-gateway-account",None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
            

    return True

def get_aws_api_gateway_api_key(type, id, clfn, descfn, topkey, key, filterid):

    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all API keys
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []:
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                common.write_import(type, j[key], None)
        else:
            # Get specific API key
            response = client.get_api_key(apiKey=id)
            if response == []:
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            j = response
            common.write_import(type, j[key], None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_api_gateway_client_certificate(type, id, clfn, descfn, topkey, key, filterid):

    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all client certificates
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []:
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                common.write_import(type, j[key], None)
        else:
            # Get specific client certificate
            response = client.get_client_certificate(clientCertificateId=id)
            if response == []:
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            j = response
            common.write_import(type, j[key], None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_api_gateway_documentation_part(type, id, clfn, descfn, topkey, key, filterid):

    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is not None:
            # List documentation parts for the given REST API
            doc_paginator = client.get_paginator(descfn)
            for page in doc_paginator.paginate(restApiId=id):
                response = response + page[topkey]
            if response == []:
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                pkey=type+"."+id
                context.rproc[pkey]=True
                return True
            for j in response:
                # ID format is restApiId/documentationPartId
                pkey = id + '/' + j[key]
                altk = "r-" + pkey
                common.write_import(type, pkey, altk)
                pkey=type+"."+id
                context.rproc[pkey]=True
        else:
            log.debug("Must pass restApiId for "+type+" returning")
            return True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_api_gateway_model(type, id, clfn, descfn, topkey, key, filterid):

    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is not None:
            # List models for the given REST API
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(restApiId=id):
                response = response + page[topkey]
            if response == []:
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                pkey=type+"."+id
                context.rproc[pkey]=True
                return True
            for j in response:
                # ID format is restApiId/modelName
                pkey = id + '/' + j['name']
                altk = "r-" + pkey
                common.write_import(type, pkey, altk)
                pkey=type+"."+id
                context.rproc[pkey]=True
        else:
            log.debug("Must pass restApiId for "+type+" returning")
            return True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_api_gateway_request_validator(type, id, clfn, descfn, topkey, key, filterid):

    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is not None:
            # List request validators for the given REST API
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(restApiId=id):
                response = response + page[topkey]
            if response == []:
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                pkey=type+"."+id
                context.rproc[pkey]=True
                return True
            for j in response:
                # ID format is restApiId/validatorId
                pkey = id + '/' + j[key]
                altk = "r-" + pkey
                common.write_import(type, pkey, altk)
                pkey=type+"."+id
                context.rproc[pkey]=True
        else:
            log.debug("Must pass restApiId for "+type+" returning")
            return True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_api_gateway_deployment(type, id, clfn, descfn, topkey, key, filterid):

    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is not None:  
            response = client.get_deployments(restApiId=id)
            if response[topkey] == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                pkey=type+"."+id
                context.rproc[pkey]=True 
                return True
            for j in response[topkey]:
                pkey=id+"/"+j[key]
                altk="r-"+pkey
            
                common.write_import(type,pkey,altk)
                pkey=type+"."+id
                context.rproc[pkey]=True
        else:
            log.debug("Must pass id for "+type+" returning")
            return True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
            
    return True

def get_aws_api_gateway_rest_api(type, id, clfn, descfn, topkey, key, filterid):

    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:

        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
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
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
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

    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)    
    try:
        response = []
        client = boto3.client(clfn)
        if id is not None:  
            response = client.get_stages(restApiId=id)
            if response[topkey] == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                pkey=type+"."+id
                context.rproc[pkey]=True
                return True
            for j in response[topkey]:
                pkey=id+"/"+j[key]
                altk="r-"+pkey
                common.write_import(type,pkey,altk)
                pkey=type+"."+id
                context.rproc[pkey]=True
        else:
            log.debug("Must pass id for "+type+" returning")
            return True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
            
    return True

def get_aws_api_gateway_authorizer(type, id, clfn, descfn, topkey, key, filterid):

    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)    
    try:
        response = []
        client = boto3.client(clfn)
        if id is not None:  
            response = client.get_authorizers(restApiId=id)
            if response[topkey] == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
                pkey=type+"."+id
                context.rproc[pkey]=True
                return True
            for j in response[topkey]:
                pkey=id+"/"+j[key]
                altk="r-"+pkey
                common.write_import(type,pkey,altk)
                pkey=type+"."+id
                context.rproc[pkey]=True
        else:
            log.debug("Must pass id for "+type+" returning")
            return True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
            
    return True

def get_aws_api_gateway_resource(type, id, clfn, descfn, topkey, key, filterid):

    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
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
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                pkey=type+"."+id
                context.rproc[pkey]=True
                return True
            for j in response[topkey]:
                pkey=id+"/"+j[key]
                altk="r-"+pkey
                common.write_import(type,pkey,altk)
                common.add_dependancy("aws_api_gateway_method", id+"/"+j[key])
                pkey=type+"."+id
                context.rproc[pkey]=True
        else:
            log.debug("Must pass id for "+type+" returning")
            return True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
            
    return True

def get_aws_api_gateway_method(type, id, clfn, descfn, topkey, key, filterid):

    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)    
    try:
        response = []
        client = boto3.client(clfn)
        if id is not None and "/" in id:  
            restid=id.split("/")[0]
            resid=id.split("/")[1]
            try:
                response = client.get_method(restApiId=restid,resourceId=resid,httpMethod='GET')
                if response == []: 
                    if context.debug: log.debug("Empty GET response for "+type+ " id="+str(id))
                    pkey=type+"."+id
                    context.rproc[pkey]=True
                    return True
                j=response
                pkey=restid+"/"+resid+"/"+j[key]
                altk="r-"+pkey
                common.write_import(type,pkey,altk)
            except:
                if context.debug: log.debug("Empty GET response for "+type+ " id="+str(id))
                

            ## POST
            try:
                response = client.get_method(restApiId=restid,resourceId=resid,httpMethod='POST')
                if response == []: 
                    if context.debug: log.debug("Empty POST response for "+type+ " id="+str(id))
                    pkey=type+"."+id
                    context.rproc[pkey]=True
                    return True
                j=response
                pkey=restid+"/"+resid+"/"+j[key]
                altk="r-"+pkey
                common.write_import(type,pkey,altk)
            except:
                if context.debug: log.debug("Empty POST response for "+type+ " id="+str(id))

            ## PUT
            try:
                response = client.get_method(restApiId=restid,resourceId=resid,httpMethod='PUT')
                if response == []: 
                    if context.debug: log.debug("Empty PUT response for "+type+ " id="+str(id))
                    pkey=type+"."+id
                    context.rproc[pkey]=True
                    return True
                j=response
                pkey=restid+"/"+resid+"/"+j[key]
                altk="r-"+pkey
                common.write_import(type,pkey,altk)
            except:
                if context.debug: log.debug("Empty PUT response for "+type+ " id="+str(id))

            ## DELETE
            try:
                response = client.get_method(restApiId=restid,resourceId=resid,httpMethod='DELETE')
                if response == []: 
                    if context.debug: log.debug("Empty DELETE response for "+type+ " id="+str(id))
                    pkey=type+"."+id
                    context.rproc[pkey]=True
                    return True
                j=response
                pkey=restid+"/"+resid+"/"+j[key]
                altk="r-"+pkey
                common.write_import(type,pkey,altk)
            except:
                if context.debug: log.debug("Empty DELETE response for "+type+ " id="+str(id))


            ## PATCH
            try:
                response = client.get_method(restApiId=restid,resourceId=resid,httpMethod='PATCH')
                if response == []: 
                    if context.debug: log.debug("Empty PATCH response for "+type+ " id="+str(id))
                    pkey=type+"."+id
                    context.rproc[pkey]=True
                    return True
                j=response
                pkey=restid+"/"+resid+"/"+j[key]
                altk="r-"+pkey
                common.write_import(type,pkey,altk)
            except:
                if context.debug: log.debug("Empty PATCH response for "+type+ " id="+str(id))


            
            pkey=restid+"/"+resid
            pkey=type+"."+pkey
            context.rproc[pkey]=True

        else:
            log.debug("Must pass Rest api id / Resource id for "+type+" returning")
            return True

    except Exception as e:
        log.info("--Error in "+str(inspect.currentframe().f_code.co_name)+" doing " + clfn + ' with id ' + str(id),str(descfn),str(topkey))
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
            
    return True