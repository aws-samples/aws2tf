"""
MEMORYDB Resource Handlers - Optimized with __getattr__

This file contains ONLY MEMORYDB resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 0 functions
Optimized: 1 functions + __getattr__
Reduction: N/A
"""

import logging
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# Custom handlers for resources requiring transformation
# ============================================================================

def aws_memorydb_user(t1, tt1, tt2, flag1, flag2):
	"""Handler for aws_memorydb_user resource"""
	skip = 0
	
	# Fix authentication_mode type - AWS API returns "no-password" but Terraform only accepts "password" or "iam"
	if tt1 == "type" and tt2 == '"no-password"':
		# Skip the no-password type as it's not valid in Terraform
		# The authentication_mode block will be skipped entirely
		skip = 1
	
	# Skip the entire authentication_mode block if it contains no-password
	if tt1 == "authentication_mode" and "no-password" in t1:
		skip = 1
	
	return skip, t1, flag1, flag2


# ============================================================================
# Magic method for backward compatibility with getattr()
# ============================================================================

def __getattr__(name):
	"""
	Dynamically provide default handler for resources without custom logic.
	
	This allows getattr(module, "aws_resource") to work even if the
	function doesn't exist, by returning the default handler.
	
	All MEMORYDB resources automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_memorydb' has no attribute '{name}'")


log.debug(f"MEMORYDB handlers: 1 custom + __getattr__ for remaining resources")