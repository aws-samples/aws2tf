import boto3
import common
import inspect
from botocore.config import Config

def get_aws_workspaces_connection_alias(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            response = client.describe_connection_aliases()
            for j in response[topkey]:
                common.write_import(type, j[key], None)
        else:
            response = client.describe_connection_aliases(AliasIds=[id])
            if response[topkey]:
                common.write_import(type, response[topkey][0][key], None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True


def get_aws_workspaces_directory(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            response = client.describe_workspace_directories()
            for j in response[topkey]:
                common.write_import(type, j[key], None)
        else:
            response = client.describe_workspace_directories(DirectoryIds=[id])
            if response[topkey]:
                common.write_import(type, response[topkey][0][key], None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True


def get_aws_workspaces_ip_group(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            response = client.describe_ip_groups()
            for j in response[topkey]:
                common.write_import(type, j[key], None)
        else:
            response = client.describe_ip_groups(GroupIds=[id])
            if response[topkey]:
                common.write_import(type, response[topkey][0][key], None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True


def get_aws_workspaces_workspace(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            response = client.describe_workspaces()
            for j in response[topkey]:
                common.write_import(type, j[key], None)
        else:
            response = client.describe_workspaces(WorkspaceIds=[id])
            if response[topkey]:
                common.write_import(type, response[topkey][0][key], None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True
