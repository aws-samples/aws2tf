import common
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect
from botocore.config import Config


def get_aws_opensearchserverless_collection(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all collections - not pageable
            response = client.list_collections()
            for j in response[topkey]:
                common.write_import(type, j[key], None)
        else:
            # Get specific collection
            response = client.batch_get_collection(ids=[id])
            if response.get('collectionDetails'):
                common.write_import(type, id, None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True


def get_aws_opensearchserverless_security_policy(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all security policies (all types) - not pageable
            for policy_type in ['encryption', 'network']:
                response = client.list_security_policies(type=policy_type)
                for j in response[topkey]:
                    # Build composite ID: name/type
                    composite_id = f"{j['name']}/{policy_type}"
                    common.write_import(type, composite_id, None)
        else:
            # Specific import - id should be composite: name/type
            if '/' in id:
                name, policy_type = id.split('/', 1)
                response = client.get_security_policy(name=name, type=policy_type)
                if response.get('securityPolicyDetail'):
                    common.write_import(type, id, None)
            else:
                # If just name provided, try both types
                for policy_type in ['encryption', 'network']:
                    try:
                        response = client.get_security_policy(name=id, type=policy_type)
                        if response.get('securityPolicyDetail'):
                            composite_id = f"{id}/{policy_type}"
                            common.write_import(type, composite_id, None)
                    except:
                        continue
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True


def get_aws_opensearchserverless_access_policy(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all access policies (data type) - not pageable
            response = client.list_access_policies(type='data')
            for j in response[topkey]:
                # Build composite ID: name/data
                composite_id = f"{j['name']}/data"
                common.write_import(type, composite_id, None)
        else:
            # Specific import - id should be composite: name/type
            if '/' in id:
                name, policy_type = id.split('/', 1)
                response = client.get_access_policy(name=name, type=policy_type)
                if response.get('accessPolicyDetail'):
                    common.write_import(type, id, None)
            else:
                # If just name provided, assume data type
                response = client.get_access_policy(name=id, type='data')
                if response.get('accessPolicyDetail'):
                    composite_id = f"{id}/data"
                    common.write_import(type, composite_id, None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True


def get_aws_opensearchserverless_lifecycle_policy(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all lifecycle policies (retention type) - not pageable
            response = client.list_lifecycle_policies(type='retention')
            for j in response[topkey]:
                # Build composite ID: name/retention
                composite_id = f"{j['name']}/retention"
                common.write_import(type, composite_id, None)
        else:
            # Specific import - id should be composite: name/type
            if '/' in id:
                name, policy_type = id.split('/', 1)
                response = client.batch_get_lifecycle_policy(identifiers=[{'name': name, 'type': policy_type}])
                if response.get('lifecyclePolicyDetails'):
                    common.write_import(type, id, None)
            else:
                # If just name provided, assume retention type
                response = client.batch_get_lifecycle_policy(identifiers=[{'name': id, 'type': 'retention'}])
                if response.get('lifecyclePolicyDetails'):
                    composite_id = f"{id}/retention"
                    common.write_import(type, composite_id, None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True


def get_aws_opensearchserverless_security_config(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        # Get account ID
        sts_client = boto3.client('sts')
        account_id = sts_client.get_caller_identity()['Account']
        
        if id is None:
            # List all security configs (saml type) - not pageable
            response = client.list_security_configs(type='saml')
            for j in response[topkey]:
                # Build composite ID: saml/account_id/name
                composite_id = f"saml/{account_id}/{j['id']}"
                common.write_import(type, composite_id, None)
        else:
            # Specific import - id should be composite: type/account_id/name
            if '/' in id:
                parts = id.split('/')
                if len(parts) == 3:
                    config_type, acc_id, config_id = parts
                    response = client.get_security_config(id=config_id)
                    if response.get('securityConfigDetail'):
                        common.write_import(type, id, None)
            else:
                # If just name provided, build composite with saml and account
                response = client.get_security_config(id=id)
                if response.get('securityConfigDetail'):
                    composite_id = f"saml/{account_id}/{id}"
                    common.write_import(type, composite_id, None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True
