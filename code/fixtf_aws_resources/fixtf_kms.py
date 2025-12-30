"""
KMS Resource Handlers - Optimized with __getattr__

This file contains ONLY KMS resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 2 functions
Optimized: 2 functions + __getattr__
Reduction: 0% less code
"""

import logging
import fixtf
import sys
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# KMS Resources with Custom Logic (2 functions)
# ============================================================================

def aws_kms_key(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1 == "policy": t1=fixtf.globals_replace(t1,tt1,tt2)
	elif tt1=="rotation_period_in_days" and tt2=="0": skip=1
	return skip,t1,flag1,flag2 



def aws_kms_alias(t1,tt1,tt2,flag1,flag2):


    skip=0
    if tt1 == "policy": t1=fixtf.globals_replace(t1,tt1,tt2)
    #if tt1 == "target_key_id":    
    #    t1=tt1 + " = aws_kms_key.k-" + tt2 + ".id\n"
    #    common.add_dependancy("aws_kms_key","k-"+tt2)
	
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
	
	All simple KMS resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_kms' has no attribute '{name}'")


log.debug(f"KMS handlers: 2 custom functions + __getattr__ for 0 simple resources")