"""
MEMORYDB Resource Handlers - Optimized with __getattr__

This file contains ONLY MEMORYDB resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 0 functions
Optimized: 1 functions + __getattr__
Reduction: N/A
"""

import logging
import context
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# Custom handlers for resources requiring transformation
# ============================================================================

def aws_memorydb_user(t1, tt1, tt2, flag1, flag2):
	"""Handler for aws_memorydb_user resource"""
	skip = 0
	
	# Track authentication_mode block with no-password type
	if tt1 == "authentication_mode":
		context.in_auth_mode_block = 0
		if "{" in t1:
			context.in_auth_mode_block = 1
	
	# Check if type is no-password inside authentication_mode block
	if tt1 == "type" and tt2 == '"no-password"':
		context.skip_auth_mode_block = True
		skip = 1
	
	# Skip entire authentication_mode block if it has no-password type
	if hasattr(context, 'in_auth_mode_block') and context.in_auth_mode_block > 0:
		if hasattr(context, 'skip_auth_mode_block') and context.skip_auth_mode_block:
			skip = 1
		
		# Track nested braces
		if "{" in t1:
			context.in_auth_mode_block += 1
		if "}" in t1:
			context.in_auth_mode_block -= 1
			if context.in_auth_mode_block == 0:
				context.skip_auth_mode_block = False
	
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