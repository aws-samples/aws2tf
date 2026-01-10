"""
LIGHTSAIL Resource Handlers - Optimized with __getattr__

This file contains ONLY LIGHTSAIL resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 0 functions
Optimized: 1 functions + __getattr__
Reduction: 0% less code
"""

import logging
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# Custom Handlers
# ============================================================================

def aws_lightsail_database(t1, tt1, tt2, flag1, flag2):
	"""
	Handler for aws_lightsail_database
	- Sets master_password to a placeholder value (sensitive field not returned by API)
	- Adds lifecycle block to ignore changes to master_password
	"""
	skip = 0
	
	# Set master_password to a placeholder value
	if tt1 == "master_password":
		t1 = tt1 + ' = "PLACEHOLDER_PASSWORD_CHANGE_ME"\n'
	
	# Add lifecycle block after relational_database_name
	elif tt1 == "relational_database_name":
		t1 = t1 + "\n lifecycle {\n   ignore_changes = [master_password]\n}\n"
	
	return skip, t1, flag1, flag2


# ============================================================================
# Magic method for backward compatibility with getattr()
# ============================================================================

def __getattr__(name):
	"""
	Dynamically provide default handler for resources without custom logic.
	
	This allows getattr(module, "aws_resource") to work even if the
	function doesn't exist, by returning the default handler.
	
	All LIGHTSAIL resources automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_lightsail' has no attribute '{name}'")


log.debug(f"LIGHTSAIL handlers: __getattr__ for all 1 resources")