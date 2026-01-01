import common
from common import log_warning
import logging
log = logging.getLogger('aws2tf')
import boto3
from botocore.config import Config
from botocore.exceptions import ClientError
import context
import inspect

def get_aws_signer_signing_profile(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all signing profiles
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []:
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                common.write_import(type, j[key], None)
        else:
            # Get specific signing profile
            response = client.get_signing_profile(profileName=id)
            if response:
                common.write_import(type, id, None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_signer_signing_job(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all signing jobs
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []:
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                # Prefix with s- because job IDs can start with numbers
                common.write_import(type, j[key], "s-"+j[key])
        else:
            # Get specific signing job
            response = client.describe_signing_job(jobId=id)
            if response:
                # Prefix with s- because job IDs can start with numbers
                common.write_import(type, id, "s-"+id)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_signer_signing_profile_permission(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all signing profiles first
            profile_paginator = client.get_paginator('list_signing_profiles')
            profiles = []
            for page in profile_paginator.paginate():
                profiles = profiles + page['profiles']
            
            # Get permissions for each profile
            for profile in profiles:
                try:
                    perm_response = client.list_profile_permissions(profileName=profile['profileName'])
                    if perm_response.get('permissions'):
                        for perm in perm_response['permissions']:
                            # ID format is profileName/statementId
                            perm_id = profile['profileName'] + '/' + perm['statementId']
                            common.write_import(type, perm_id, None)
                except ClientError as e:
                    if e.response['Error']['Code'] == 'ResourceNotFoundException':
                        continue
                    raise
        else:
            # Get specific profile's permissions
            # id could be just profileName or profileName/statementId
            if '/' in id:
                profile_name = id.split('/')[0]
                statement_id = id.split('/')[1]
                # Get all permissions and filter for this statement
                perm_response = client.list_profile_permissions(profileName=profile_name)
                if perm_response.get('permissions'):
                    for perm in perm_response['permissions']:
                        if perm['statementId'] == statement_id:
                            common.write_import(type, id, None)
            else:
                # Just profile name - get all permissions
                perm_response = client.list_profile_permissions(profileName=id)
                if perm_response.get('permissions'):
                    for perm in perm_response['permissions']:
                        perm_id = id + '/' + perm['statementId']
                        common.write_import(type, perm_id, None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True
