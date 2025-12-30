"""
CLOUD9 Resource Handlers - Optimized with __getattr__

This file contains ONLY CLOUD9 resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 1 functions
Optimized: 1 functions + __getattr__
Reduction: 0% less code
"""

import logging
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# CLOUD9 Resources with Custom Logic (1 functions)
# ============================================================================

def aws_cloud9_environment_ec2(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="instance_type" and tt2=="null": skip=1
	if tt1=="image_id" and tt2=="null": skip=1
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
	
	All simple CLOUD9 resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_cloud9' has no attribute '{name}'")


log.debug(f"CLOUD9 handlers: 1 custom functions + __getattr__ for 0 simple resources")