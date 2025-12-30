"""
CLOUDFRONT Resource Handlers - Optimized with __getattr__

This file contains ONLY CLOUDFRONT resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 2 functions
Optimized: 2 functions + __getattr__
Reduction: 0% less code
"""

import logging
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# CLOUDFRONT Resources with Custom Logic (2 functions)
# ============================================================================

def aws_cloudfront_distribution(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="cache_policy_id" and tt2 != "null":
		t1=tt1+" = aws_cloudfront_cache_policy.o-"+tt2+".id\n"
	return skip,t1,flag1,flag2



def aws_cloudfront_function(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="publish" and tt2=="null": 
		#t1=t1+"\n lifecycle {\n   ignore_changes = [publish]\n}\n"
		t1=tt1+" = true\n" 
		t1=t1+"\n lifecycle {\n   ignore_changes = [publish]\n}\n"
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
	
	All simple CLOUDFRONT resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_cloudfront' has no attribute '{name}'")


log.debug(f"CLOUDFRONT handlers: 2 custom functions + __getattr__ for 0 simple resources")