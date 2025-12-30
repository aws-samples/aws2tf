"""
STEPFUNCTIONS Resource Handlers - Optimized with __getattr__

This file contains ONLY STEPFUNCTIONS resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 1 functions
Optimized: 1 functions + __getattr__
Reduction: 0% less code
"""

import logging
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# STEPFUNCTIONS Resources with Custom Logic (1 functions)
# ============================================================================

def aws_sfn_state_machine(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="definition":
				t1="\n lifecycle {\n   ignore_changes = [definition]\n}\n" + t1
	if tt1=="kms_data_key_reuse_period_seconds" and tt2=="0": skip=1
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
	
	All simple STEPFUNCTIONS resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_stepfunctions' has no attribute '{name}'")


log.debug(f"STEPFUNCTIONS handlers: 1 custom functions + __getattr__ for 0 simple resources")