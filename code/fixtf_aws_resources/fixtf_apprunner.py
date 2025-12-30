"""
APPRUNNER Resource Handlers - Optimized with __getattr__

This file contains ONLY APPRUNNER resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 1 functions
Optimized: 1 functions + __getattr__
Reduction: 0% less code
"""

import context
import logging
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# APPRUNNER Resources with Custom Logic (1 functions)
# ============================================================================

def aws_apprunner_service(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="auto_scaling_configuration_arn":
		if "autoscalingconfiguration/DefaultConfiguration/1" in tt2: skip=1
	if tt1=="image_identifier":
		log.debug(tt2)
		if tt2.startswith(context.acc) and context.region in tt2:
			backend=tt2.split("/")[-1]
			t1=tt1 + " = format(\"%s.dkr.ecr.%s.amazonaws.com/%s\",data.aws_caller_identity.current.account_id,data.aws_region.current.region,\""+backend+"\")\n"
			
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
	
	All simple APPRUNNER resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_apprunner' has no attribute '{name}'")


log.debug(f"APPRUNNER handlers: 1 custom functions + __getattr__ for 0 simple resources")