#!/usr/bin/env python3
"""
Get functions for AWS Bedrock AgentCore Control resources
Service: bedrock-agentcore-control
"""

import boto3
import common
import inspect
from botocore.config import Config

def get_aws_bedrockagentcore_agent_runtime(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all agent runtimes
            paginator = client.get_paginator(descfn)
            response = []
            for page in paginator.paginate():
                response = response + page[topkey]
            for j in response:
                common.write_import(type, j[key], None)
        else:
            # Get specific agent runtime
            response = client.get_agent_runtime(agentRuntimeId=id)
            j = response.get('agentRuntime', response)
            common.write_import(type, j[key], None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True

def get_aws_bedrockagentcore_workload_identity(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all workload identities
            paginator = client.get_paginator(descfn)
            response = []
            for page in paginator.paginate():
                response = response + page[topkey]
            for j in response:
                common.write_import(type, j[key], None)
        else:
            # Get specific workload identity
            response = client.get_workload_identity(name=id)
            j = response.get('workloadIdentity', response)
            common.write_import(type, j[key], None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True

def get_aws_bedrockagentcore_memory(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all memories
            paginator = client.get_paginator(descfn)
            response = []
            for page in paginator.paginate():
                response = response + page[topkey]
            for j in response:
                common.write_import(type, j[key], None)
        else:
            # Get specific memory
            response = client.get_memory(memoryId=id)
            j = response.get('memory', response)
            common.write_import(type, j[key], None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True

def get_aws_bedrockagentcore_gateway(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all gateways
            paginator = client.get_paginator(descfn)
            response = []
            for page in paginator.paginate():
                response = response + page[topkey]
            for j in response:
                common.write_import(type, j[key], None)
        else:
            # Get specific gateway
            response = client.get_gateway(gatewayId=id)
            j = response.get('gateway', response)
            common.write_import(type, j[key], None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True

def get_aws_bedrockagentcore_browser(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all browsers
            paginator = client.get_paginator(descfn)
            response = []
            for page in paginator.paginate():
                response = response + page[topkey]
            for j in response:
                common.write_import(type, j[key], None)
        else:
            # Get specific browser
            response = client.get_browser(browserId=id)
            j = response.get('browser', response)
            common.write_import(type, j[key], None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True

def get_aws_bedrockagentcore_code_interpreter(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all code interpreters
            paginator = client.get_paginator(descfn)
            response = []
            for page in paginator.paginate():
                response = response + page[topkey]
            for j in response:
                common.write_import(type, j[key], None)
        else:
            # Get specific code interpreter
            response = client.get_code_interpreter(codeInterpreterId=id)
            j = response.get('codeInterpreter', response)
            common.write_import(type, j[key], None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True

def get_aws_bedrockagentcore_token_vault_cmk(type, id, clfn, descfn, topkey, key, filterid):
    """
    Token vault CMK is a singleton resource - one per region
    Uses get_token_vault (no list operation)
    Import ID is the token_vault_id (defaults to 'default')
    """
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # No list operation - get the default token vault
            response = client.get_token_vault()
            vault_id = response.get('tokenVaultId', 'default')
            common.write_import(type, vault_id, None)
        else:
            # Get specific token vault by ID
            response = client.get_token_vault(tokenVaultId=id)
            vault_id = response.get('tokenVaultId', id)
            common.write_import(type, vault_id, None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True
