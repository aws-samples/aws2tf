"""
REDSHIFT Resource Handlers - Optimized with __getattr__

This file contains ONLY REDSHIFT resources with custom transformation logic.
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
# REDSHIFT Resources with Custom Logic (1 functions)
# ============================================================================

def aws_redshift_cluster(t1,tt1,tt2,flag1,flag2):


	skip=0

	if tt1 == "cluster_subnet_group_name":
        
		t1=tt1 + " = aws_redshift_subnet_group." + tt2 + ".id\n"
		common.add_dependancy("aws_redshift_subnet_group",tt2)
	elif tt1 == "cluster_parameter_group_name" and tt2 != "null":
		if not tt2.startswith("default"):
			t1=tt1 + " = aws_redshift_parameter_group." + tt2 + ".id\n"
			common.add_dependancy("aws_redshift_parameter_group",tt2)
	elif tt1 == "apply_immediately":
		if tt2=="null":
			t1=tt1+" = false \n lifecycle {\n   ignore_changes = [apply_immediately,cluster_version]\n}\n"
        
	if tt1 == "endpoint": skip=1
    
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
	
	All simple REDSHIFT resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_redshift' has no attribute '{name}'")


log.debug(f"REDSHIFT handlers: 1 custom functions + __getattr__ for 0 simple resources")