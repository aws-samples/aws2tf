"""
SCHEDULER Resource Handlers - Optimized with __getattr__

This file contains ONLY SCHEDULER resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 1 functions
Optimized: 1 functions + __getattr__
Reduction: 0% less code
"""

import logging
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# SCHEDULER Resources with Custom Logic (1 functions)
# ============================================================================

def aws_scheduler_schedule(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="maximum_window_in_minutes" and tt2=="0": skip=1
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
	
	All simple SCHEDULER resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_scheduler' has no attribute '{name}'")


log.debug(f"SCHEDULER handlers: 1 custom functions + __getattr__ for 0 simple resources")