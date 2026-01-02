"""
EVENTS Resource Handlers - Optimized with __getattr__

This file contains ONLY EVENTS resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 2 functions
Optimized: 2 functions + __getattr__
Reduction: 0% less code
"""

import logging
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# EVENTS Resources with Custom Logic (3 functions)
# ============================================================================

def aws_cloudwatch_event_connection(t1, tt1, tt2, flag1, flag2):
	"""Handler for aws_cloudwatch_event_connection resource"""
	skip = 0
	
	# Replace sensitive null value with placeholder - it's write-only
	if "value = null # sensitive" in t1:
		t1 = t1.replace("value = null # sensitive", 'value = "PLACEHOLDER_VALUE_CHANGE_ME" # sensitive - original value not returned by API')
	
	# Add lifecycle block to ignore auth_parameters changes (sensitive values)
	if tt1 == "name" and tt2 != "null":
		t1 = t1 + "\nlifecycle {\n   ignore_changes = [auth_parameters]\n}\n"
	
	return skip, t1, flag1, flag2

def aws_cloudwatch_event_rule(t1,tt1,tt2,flag1,flag2):


	skip=0
	if "name_prefix" in tt1: skip=1

	return skip,t1,flag1,flag2



def aws_cloudwatch_event_target(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1 == "arn":
		t1=t1+"\nlifecycle {\n" + "   ignore_changes = [input_transformer]\n" +  "}\n"
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
	
	All simple EVENTS resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_events' has no attribute '{name}'")


log.debug(f"EVENTS handlers: 3 custom functions + __getattr__ for 0 simple resources")