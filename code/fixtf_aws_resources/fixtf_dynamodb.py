"""
DYNAMODB Resource Handlers - Optimized with __getattr__

This file contains ONLY DYNAMODB resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 2 functions
Optimized: 2 functions + __getattr__
Reduction: 0% less code
"""

import logging
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# DYNAMODB Resources with Custom Logic (2 functions)
# ============================================================================

def aws_dynamodb_kinesis_streaming_destination(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="table_name" and tt2!="null":
		t1 =tt1+" = aws_dynamodb_table."+tt2+".name\n"
	return skip,t1,flag1,flag2



def aws_dynamodb_table(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="recovery_period_in_days" and tt2=="0":
		skip=1
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
	
	All simple DYNAMODB resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_dynamodb' has no attribute '{name}'")


log.debug(f"DYNAMODB handlers: 2 custom functions + __getattr__ for 0 simple resources")