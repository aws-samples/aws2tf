"""
ACM Resource Handlers - Optimized with __getattr__

This file contains ONLY ACM resources with custom transformation logic.
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
# ACM Resources with Custom Logic (1 functions)
# ============================================================================

def aws_acm_certificate(t1,tt1,tt2,skipipv6,flag2):


    skip = 0
    if tt1 == "validation_method":
        
        if tt2 == "NONE": skip=1

        
    return skip,t1,skipipv6,flag2


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
	
	All simple ACM resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_acm' has no attribute '{name}'")


log.debug(f"ACM handlers: 1 custom functions + __getattr__ for 0 simple resources")