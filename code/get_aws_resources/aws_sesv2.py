import boto3
import common
import inspect
from botocore.config import Config

def get_aws_sesv2_configuration_set(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all configuration sets - returns list of strings
            response = client.list_configuration_sets()
            for config_set_name in response[topkey]:
                common.write_import(type, config_set_name, None)
        else:
            # Get specific configuration set
            response = client.get_configuration_set(ConfigurationSetName=id)
            if response:
                common.write_import(type, id, None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True

def get_aws_sesv2_email_identity(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all email identities
            paginator = client.get_paginator(descfn)
            response = []
            for page in paginator.paginate():
                response = response + page[topkey]
            for j in response:
                common.write_import(type, j[key], None)
        else:
            # Get specific email identity
            response = client.get_email_identity(EmailIdentity=id)
            if response:
                common.write_import(type, id, None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True

def get_aws_sesv2_contact_list(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all contact lists
            response = client.list_contact_lists()
            for j in response[topkey]:
                common.write_import(type, j[key], None)
        else:
            # Get specific contact list
            response = client.get_contact_list(ContactListName=id)
            if response:
                common.write_import(type, id, None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True

def get_aws_sesv2_dedicated_ip_pool(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all dedicated IP pools
            response = client.list_dedicated_ip_pools()
            for pool_name in response[topkey]:
                common.write_import(type, pool_name, None)
        else:
            # Get specific dedicated IP pool
            response = client.get_dedicated_ip_pool(PoolName=id)
            if response:
                common.write_import(type, id, None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True

def get_aws_sesv2_account_vdm_attributes(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        # This is a singleton resource - always use the fixed ID
        # Works for both id=None (type-level) and id="ses-account-vdm-attributes" (specific)
        try:
            response = client.get_account()
            if response and 'VdmAttributes' in response:
                common.write_import(type, "ses-account-vdm-attributes", None)
        except Exception as e:
            # Account VDM attributes may not be configured
            if common.context.debug:
                common.log.debug(f"Account VDM attributes not configured: {e}")
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True

def get_aws_sesv2_account_suppression_attributes(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        sts_client = boto3.client('sts')
        
        # Get the account ID
        account_id = sts_client.get_caller_identity()['Account']
        
        # This is a singleton resource - uses account ID as import ID
        # Works for both id=None (type-level) and id=account_id (specific)
        if id is None or id == account_id:
            try:
                response = client.get_account()
                if response and 'SuppressionAttributes' in response:
                    common.write_import(type, account_id, None)
            except Exception as e:
                # Suppression attributes may not be configured
                if common.context.debug:
                    common.log.debug(f"Account suppression attributes not configured: {e}")
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True

def get_aws_sesv2_email_identity_policy(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all email identities, then get policies for each
            response = client.list_email_identities()
            identities = response.get('EmailIdentities', [])
            
            for identity in identities:
                identity_name = identity['IdentityName']
                try:
                    # Get policies for this identity - returns dict of {policy_name: policy_json}
                    policy_response = client.get_email_identity_policies(EmailIdentity=identity_name)
                    policies_dict = policy_response.get('Policies', {})
                    for policy_name in policies_dict.keys():
                        composite_id = f"{identity_name}|{policy_name}"
                        common.write_import(type, composite_id, None)
                except Exception as e:
                    if common.context.debug:
                        common.log.debug(f"No policies for identity {identity_name}: {e}")
                    continue
        else:
            # Handle composite ID: email_identity|policy_name
            if '|' in id:
                identity_name, policy_name = id.split('|', 1)
                try:
                    response = client.get_email_identity_policies(EmailIdentity=identity_name)
                    policies_dict = response.get('Policies', {})
                    if policy_name in policies_dict:
                        common.write_import(type, id, None)
                except Exception as e:
                    if common.context.debug:
                        common.log.debug(f"Policy not found: {e}")
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True

def get_aws_sesv2_tenant(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all tenants
            response = client.list_tenants()
            for j in response[topkey]:
                common.write_import(type, j[key], None)
        else:
            # Get specific tenant
            response = client.get_tenant(TenantName=id)
            if response:
                common.write_import(type, id, None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True
