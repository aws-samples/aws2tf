"""
SQS Resource Handlers - Optimized with __getattr__

This file contains ONLY SQS resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 0 functions
Optimized: 0 functions + __getattr__
Reduction: 0% less code
"""

import logging
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


def aws_sqs_queue(t1, tt1, tt2, flag1, flag2):
	skip = 0
	# kms_master_key_id conflicts with sqs_managed_sse_enabled. Keep whichever is
	# actually set: drop a null kms key, and drop sqs_managed_sse_enabled=false
	# (its default) so a queue using a real KMS key validates.
	if tt1 == "kms_master_key_id" and tt2 == "null":
		skip = 1
	elif tt1 == "sqs_managed_sse_enabled" and tt2 == "false":
		skip = 1
	return skip, t1, flag1, flag2


# ============================================================================
# Magic method for backward compatibility with getattr()
# ============================================================================

def __getattr__(name):
	"""
	Dynamically provide default handler for resources without custom logic.
	
	This allows getattr(module, "aws_resource") to work even if the
	function doesn't exist, by returning the default handler.
	
	All SQS resources automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_sqs' has no attribute '{name}'")


log.debug(f"SQS handlers: __getattr__ for all 0 resources")