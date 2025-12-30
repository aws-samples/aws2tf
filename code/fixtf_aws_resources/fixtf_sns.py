"""
SNS Resource Handlers - Optimized with __getattr__

This file contains ONLY SNS resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 2 functions
Optimized: 2 functions + __getattr__
Reduction: 0% less code
"""

import logging
import common
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# SNS Resources with Custom Logic (2 functions)
# ============================================================================

def aws_sns_topic(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1 == "signature_version":
		if tt2 == "0": skip=1 
	
	return skip,t1,flag1,flag2




def aws_sns_topic_subscription(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="topic_arn":
		#tn=tt2.replace(":","_")
		#t1=tt1 + " = aws_sns_topic." + tn + ".arn\n"
		t1=t1+"\n lifecycle {\n   ignore_changes = [confirmation_timeout_in_minutes,endpoint_auto_confirms]\n}\n"
		common.add_dependancy("aws_sns_topic",tt2)


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
	
	All simple SNS resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_sns' has no attribute '{name}'")


log.debug(f"SNS handlers: 2 custom functions + __getattr__ for 0 simple resources")