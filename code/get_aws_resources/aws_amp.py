import common
from common import log_warning
import logging
log = logging.getLogger('aws2tf')
import boto3
from botocore.config import Config
from botocore.exceptions import ClientError
import context
import inspect

def get_aws_prometheus_query_logging_configuration(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all Prometheus workspaces first
            paginator = client.get_paginator('list_workspaces')
            workspaces = []
            for page in paginator.paginate():
                workspaces = workspaces + page['workspaces']
            
            # Check each workspace for query logging configuration
            for workspace in workspaces:
                try:
                    response = client.describe_query_logging_configuration(workspaceId=workspace['workspaceId'])
                    # If query logging is configured, import it
                    if response.get('queryLoggingConfiguration'):
                        common.write_import(type, workspace['workspaceId'], None)
                except ClientError as e:
                    if e.response['Error']['Code'] == 'ResourceNotFoundException':
                        continue
                    raise
        else:
            # Get specific workspace's query logging configuration
            response = client.describe_query_logging_configuration(workspaceId=id)
            if response.get('queryLoggingConfiguration'):
                common.write_import(type, id, None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_prometheus_workspace(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all workspaces
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []:
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                common.write_import(type, j['workspaceId'], None)
        else:
            # Get specific workspace - handle both ARN and workspace ID
            if id.startswith("arn:"):
                # ID is an ARN - extract workspace ID
                workspace_id = id.split('/')[-1]
            elif id.startswith("ws-"):
                # ID is a workspace ID
                workspace_id = id
            else:
                if context.debug: log.debug("Invalid workspace ID format: "+id)
                return True
            
            # Get the workspace
            response = client.describe_workspace(workspaceId=workspace_id)
            if response.get('workspace'):
                j = response['workspace']
                common.write_import(type, j['workspaceId'], None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_prometheus_resource_policy(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all Prometheus workspaces first
            paginator = client.get_paginator('list_workspaces')
            workspaces = []
            for page in paginator.paginate():
                workspaces = workspaces + page['workspaces']
            
            # Try to get resource policy for each workspace
            for workspace in workspaces:
                workspace_id = workspace['workspaceId']
                try:
                    response = client.describe_resource_policy(workspaceId=workspace_id)
                    # Policy exists for this workspace
                    # Import using workspace ID (from import docs)
                    common.write_import(type, workspace_id, None)
                except ClientError as e:
                    if e.response['Error']['Code'] in ['ResourceNotFoundException', 'AccessDeniedException']:
                        continue
                    raise
        else:
            # Get specific workspace's resource policy
            # Handle both ARN and workspace ID
            if id.startswith("arn:"):
                # Extract workspace ID from ARN
                workspace_id = id.split('/')[-1]
            elif id.startswith("ws-"):
                workspace_id = id
            else:
                if context.debug: log.debug("Invalid workspace ID format: "+id)
                return True
            
            try:
                response = client.describe_resource_policy(workspaceId=workspace_id)
                # Import using workspace ID
                common.write_import(type, workspace_id, None)
            except ClientError as e:
                if e.response['Error']['Code'] in ['ResourceNotFoundException', 'AccessDeniedException']:
                    if context.debug: log.debug("No policy for workspace: "+id)
                else:
                    raise

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_prometheus_workspace_configuration(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all Prometheus workspaces first
            paginator = client.get_paginator('list_workspaces')
            workspaces = []
            for page in paginator.paginate():
                workspaces = workspaces + page['workspaces']
            
            # Check each workspace for configuration
            for workspace in workspaces:
                try:
                    response = client.describe_workspace_configuration(workspaceId=workspace['workspaceId'])
                    # If configuration exists, import it
                    if response.get('workspaceConfiguration'):
                        common.write_import(type, workspace['workspaceId'], None)
                except ClientError as e:
                    if e.response['Error']['Code'] == 'ResourceNotFoundException':
                        continue
                    raise
        else:
            # Get specific workspace's configuration
            response = client.describe_workspace_configuration(workspaceId=id)
            if response.get('workspaceConfiguration'):
                common.write_import(type, id, None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True
