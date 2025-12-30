"""
BEDROCK_AGENT Resource Handlers - Optimized with __getattr__

This file contains ONLY BEDROCK_AGENT resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 5 functions
Optimized: 5 functions + __getattr__
Reduction: 0% less code
"""

import logging
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# BEDROCK_AGENT Resources with Custom Logic (5 functions)
# ============================================================================

def aws_bedrockagent_agent(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="skip_resource_in_use_check" and tt2=="null":
		t1 = tt1+" = false\n"
	elif tt1=="agent_name":
		t1 = t1 + "\n lifecycle {\n   ignore_changes = [skip_resource_in_use_check]\n}\n"
	
	return skip,t1,flag1,flag2



def aws_bedrockagent_agent_knowledge_base_association(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="agent_id" and tt2 != "null":
		t1 = tt1+" = aws_bedrockagent_agent.r-"+tt2+".id\n"
	elif tt1=="knowledge_base_id" and tt2 != "null":
		t1 = tt1+" = aws_bedrockagent_knowledge_base.r-"+tt2+".id\n"
	return skip,t1,flag1,flag2



def aws_bedrockagent_data_source(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="knowledge_base_id" and tt2 != "null":
		t1 = tt1+" = aws_bedrockagent_knowledge_base.r-"+tt2+".id\n"
	return skip,t1,flag1,flag2



def aws_bedrockagent_agent_action_group(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="skip_resource_in_use_check" and tt2=="null":
		skip=1
	#	t1 = tt1+" = false\n"
	if tt1=="agent_id":
		if tt2 != "null":
			t1 = tt1+" = aws_bedrockagent_agent.r-"+tt2+".id\n"
		#t1=t1+"skip_resource_in_use_check = false\n"
		t1=t1+"\n lifecycle {\n   ignore_changes = [skip_resource_in_use_check]\n}\n"
	return skip,t1,flag1,flag2



def aws_bedrockagent_agent_alias(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="agent_id" and tt2 != "null":
		t1 = tt1+" = aws_bedrockagent_agent.r-"+tt2+".id\n"
	return skip,t1,flag1,flag2


# ============================================================================
# Magic method for backward compatibility with getattr()
# ============================================================================



# ============================================================================
# Magic method for backward compatibility with getattr()
# ============================================================================

def __getattr__(name):
	"""
	Dynamically provide default handler for resources without custom logic.
	
	This allows getattr(module, "aws_resource") to work even if the
	function doesn't exist, by returning the default handler.
	
	All simple BEDROCK_AGENT resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_bedrock_agent' has no attribute '{name}'")


log.debug(f"BEDROCK_AGENT handlers: 5 custom functions + __getattr__ for 0 simple resources")