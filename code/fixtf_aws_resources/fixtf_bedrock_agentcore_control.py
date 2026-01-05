#!/usr/bin/env python3
"""
Handler for AWS Bedrock AgentCore Control resources
Service: bedrock-agentcore-control
"""

import context

def aws_bedrockagentcore_agent_runtime(t1, tt1, tt2, flag1, flag2):
    """Handler for aws_bedrockagentcore_agent_runtime resource"""
    skip = 0
    return skip, t1, flag1, flag2

def aws_bedrockagentcore_agent_runtime_endpoint(t1, tt1, tt2, flag1, flag2):
    """Handler for aws_bedrockagentcore_agent_runtime_endpoint resource"""
    skip = 0
    return skip, t1, flag1, flag2

def aws_bedrockagentcore_api_key_credential_provider(t1, tt1, tt2, flag1, flag2):
    """Handler for aws_bedrockagentcore_api_key_credential_provider resource"""
    skip = 0
    
    # Skip api_key and api_key_wo fields when null - they are sensitive/write-only
    # One of them is required, but we can't retrieve the actual value
    if tt1 in ["api_key", "api_key_wo", "api_key_wo_version"] and tt2 == "null":
        skip = 1
    
    return skip, t1, flag1, flag2

def aws_bedrockagentcore_browser(t1, tt1, tt2, flag1, flag2):
    """Handler for aws_bedrockagentcore_browser resource"""
    skip = 0
    return skip, t1, flag1, flag2

def aws_bedrockagentcore_code_interpreter(t1, tt1, tt2, flag1, flag2):
    """Handler for aws_bedrockagentcore_code_interpreter resource"""
    skip = 0
    return skip, t1, flag1, flag2

def aws_bedrockagentcore_gateway(t1, tt1, tt2, flag1, flag2):
    """Handler for aws_bedrockagentcore_gateway resource"""
    skip = 0
    return skip, t1, flag1, flag2

def aws_bedrockagentcore_gateway_target(t1, tt1, tt2, flag1, flag2):
    """Handler for aws_bedrockagentcore_gateway_target resource"""
    skip = 0
    return skip, t1, flag1, flag2

def aws_bedrockagentcore_memory(t1, tt1, tt2, flag1, flag2):
    """Handler for aws_bedrockagentcore_memory resource"""
    skip = 0
    return skip, t1, flag1, flag2

def aws_bedrockagentcore_memory_strategy(t1, tt1, tt2, flag1, flag2):
    """Handler for aws_bedrockagentcore_memory_strategy resource"""
    skip = 0
    return skip, t1, flag1, flag2

def aws_bedrockagentcore_oauth2_credential_provider(t1, tt1, tt2, flag1, flag2):
    """Handler for aws_bedrockagentcore_oauth2_credential_provider resource"""
    skip = 0
    return skip, t1, flag1, flag2

def aws_bedrockagentcore_token_vault_cmk(t1, tt1, tt2, flag1, flag2):
    """Handler for aws_bedrockagentcore_token_vault_cmk resource"""
    skip = 0
    return skip, t1, flag1, flag2

def aws_bedrockagentcore_workload_identity(t1, tt1, tt2, flag1, flag2):
    """Handler for aws_bedrockagentcore_workload_identity resource"""
    skip = 0
    return skip, t1, flag1, flag2
