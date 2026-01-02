import boto3
import common
import inspect
from botocore.config import Config

def get_aws_workspacesweb_portal(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all portals - not pageable
            response = client.list_portals()
            for j in response[topkey]:
                common.write_import(type, j[key], None)
        else:
            # Get specific portal
            response = client.get_portal(portalArn=id)
            j = response.get('portal', response)
            common.write_import(type, j[key], None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True

def get_aws_workspacesweb_user_settings(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all user settings - not pageable
            response = client.list_user_settings()
            for j in response[topkey]:
                common.write_import(type, j[key], None)
        else:
            # Get specific user settings
            response = client.get_user_settings(userSettingsArn=id)
            j = response.get('userSettings', response)
            common.write_import(type, j[key], None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True

def get_aws_workspacesweb_network_settings(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all network settings - not pageable
            response = client.list_network_settings()
            for j in response[topkey]:
                common.write_import(type, j[key], None)
        else:
            # Get specific network settings
            response = client.get_network_settings(networkSettingsArn=id)
            j = response.get('networkSettings', response)
            common.write_import(type, j[key], None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True


def get_aws_workspacesweb_identity_provider(type, id, clfn, descfn, topkey, key, filterid):
    try:
        from botocore.config import Config
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all portals first
            response = client.list_portals()
            portals = response.get('portals', [])
            
            # For each portal, list identity providers
            for portal in portals:
                portal_arn = portal['portalArn']
                try:
                    idp_response = client.list_identity_providers(portalArn=portal_arn)
                    for idp in idp_response.get('identityProviders', []):
                        common.write_import(type, idp['identityProviderArn'], None)
                except Exception as e:
                    if context.debug: log.debug(f"Error listing identity providers for {portal_arn}: {e}")
                    continue
        else:
            # Get specific identity provider by ARN
            response = client.get_identity_provider(identityProviderArn=id)
            if response:
                common.write_import(type, id, None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True
