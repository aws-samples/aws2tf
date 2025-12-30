"""
LOGS Resource Handlers - Optimized with __getattr__

This file contains ONLY LOGS resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 1 functions
Optimized: 1 functions + __getattr__
Reduction: 0% less code
"""

import logging
import common
import fixtf
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# LOGS Resources with Custom Logic (1 functions)
# ============================================================================

def aws_cloudwatch_log_group(t1,tt1,tt2,flag1,flag2):


    skip=0
    if tt1 == "name":
        
        if len(tt2) > 0: flag1=True

    #CIRCULAR reference problems:
    ##if tt1 == "security_groups": t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)
  
    if tt1 == "name_prefix" and flag1 is True: skip=1

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
	
	All simple LOGS resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_logs' has no attribute '{name}'")


log.debug(f"LOGS handlers: 1 custom functions + __getattr__ for 0 simple resources")