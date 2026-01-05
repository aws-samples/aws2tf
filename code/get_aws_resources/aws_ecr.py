import common
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect
import botocore

def get_aws_ecr_registry_policy(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.get_registry_policy()
            if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response
            common.write_import(type,j[key],None) 
    except client.exceptions.RegistryPolicyNotFoundException:
        pass


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

#aws_ecr_registry_scanning_configuration  client.get_registry_scanning_configuration()

def get_aws_ecr_registry_scanning_configuration(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.get_registry_policy()
            if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response
            common.write_import(type,j[key],None) 
    except client.exceptions.RegistryPolicyNotFoundException:
        pass


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True





# aws_ecr_replication_configuration   client.describe_image_replication_status(  repositoryName='string',

def get_aws_ecr_replication_configuration(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        response=client.describe_replication_configuration() ## ???

        common.write_import(type,context.acc,"r-"+context.acc) 
    
    except client.exceptions.RegistryPolicyNotFoundException:
        pass


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_ecr_pull_through_cache_rule(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response=client.describe_pull_through_cache_rules() ## ???
        else:
            response=client.describe_pull_through_cache_rules(ecrRepositoryPrefixes=[id]) ## ???
        for j in response[topkey]:

            common.write_import(type, j[key], None)

    
    except client.exceptions.RegistryPolicyNotFoundException:
        pass


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

# aws_ecr_repository
def get_aws_ecr_repository(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.describe_repositories()
            if response[topkey] == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                common.write_import(type, j[key], None)
        else:
            response = client.describe_repositories(repositoryNames=[id])
            if response[topkey] == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                common.write_import(type, j[key], None)

    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True





def get_aws_ecr_account_setting(type, id, clfn, descfn, topkey, key, filterid):
    """
    ECR account settings are singleton resources - there are only 2 possible settings:
    - BASIC_SCAN_TYPE_VERSION
    - REGISTRY_POLICY_SCOPE
    """
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        client = boto3.client(clfn)
        
        if id is None:
            # List all possible account settings
            setting_names = ['BASIC_SCAN_TYPE_VERSION', 'REGISTRY_POLICY_SCOPE']
            for setting_name in setting_names:
                try:
                    response = client.get_account_setting(name=setting_name)
                    # Write import using the setting name
                    common.write_import(type, response['name'], None)
                except Exception as e:
                    if context.debug:
                        log.debug(f"Setting {setting_name} not found or error: {e}")
                    continue
        else:
            # Get specific account setting
            response = client.get_account_setting(name=id)
            common.write_import(type, response['name'], None)
            
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True

def get_aws_ecr_repository_creation_template(type, id, clfn, descfn, topkey, key, filterid):
    """
    ECR repository creation templates
    """
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        from botocore.config import Config
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all repository creation templates
            paginator = client.get_paginator(descfn)
            response = []
            for page in paginator.paginate():
                response = response + page[topkey]
            for j in response:
                common.write_import(type, j[key], None)
        else:
            # Get specific template
            response = client.describe_repository_creation_templates(prefixes=[id])
            if response[topkey]:
                j = response[topkey][0]
                common.write_import(type, j[key], None)
                
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True
