"""
APPSTREAM Resource Handlers - Optimized with __getattr__

This file contains ONLY APPSTREAM resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 3 functions
Optimized: 3 functions + __getattr__
Reduction: 0% less code
"""

import logging
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# APPSTREAM Resources with Custom Logic (3 functions)
# ============================================================================

def aws_appstream_fleet(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="desired_sessions" and tt2=="0": skip=1
	if tt1=="desired_instancess" and tt2=="0": skip=1

	return skip,t1,flag1,flag2



def aws_appstream_stack(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="embed_host_domains" and tt2=="[]": skip=1
	return skip,t1,flag1,flag2



def aws_appstream_user(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="send_email_notification" and tt2=="null":
		t1=tt1+" = true\n"
		t1=t1+"\nlifecycle {\n" + "   ignore_changes = [send_email_notification]\n" +  "}\n"
		
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
	
	All simple APPSTREAM resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_appstream' has no attribute '{name}'")


log.debug(f"APPSTREAM handlers: 3 custom functions + __getattr__ for 0 simple resources")