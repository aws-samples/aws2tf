"""
CLOUDTRAIL Resource Handlers - Optimized with __getattr__

This file contains ONLY CLOUDTRAIL resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 2 functions
Optimized: 2 functions + __getattr__
Reduction: 0% less code
"""

import logging
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# CLOUDTRAIL Resources with Custom Logic (2 functions)
# ============================================================================

def aws_cloudtrail(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="ends_with" and tt2=="[]": skip=1
	if tt1=="not_ends_with" and tt2=="[]": skip=1
	if tt1=="starts_with" and tt2=="[]": skip=1
	if tt1=="not_starts_with" and tt2=="[]": skip=1
	if tt1=="not_equals" and tt2=="[]": skip=1
	if tt1=="equals" and tt2=="[]": skip=1

	return skip,t1,flag1,flag2



def aws_cloudtrail_event_data_store(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="ends_with" and tt2=="[]": skip=1
	if tt1=="not_ends_with" and tt2=="[]": skip=1
	if tt1=="starts_with" and tt2=="[]": skip=1
	if tt1=="not_starts_with" and tt2=="[]": skip=1
	if tt1=="not_equals" and tt2=="[]": skip=1
	if tt1=="equals" and tt2=="[]": skip=1
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
	
	All simple CLOUDTRAIL resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_cloudtrail' has no attribute '{name}'")


log.debug(f"CLOUDTRAIL handlers: 2 custom functions + __getattr__ for 0 simple resources")