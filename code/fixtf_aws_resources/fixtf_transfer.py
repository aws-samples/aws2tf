"""
TRANSFER Resource Handlers - Optimized with __getattr__

This file contains ONLY TRANSFER resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 0 functions
Optimized: 0 functions + __getattr__
Reduction: 0% less code
"""

import logging
import context
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


def aws_transfer_server(t1, tt1, tt2, flag1, flag2):
	skip = 0
	# vpc_endpoint_id is only valid for the (deprecated) VPC_ENDPOINT endpoint
	# type; for the VPC endpoint type it conflicts with address_allocation_ids.
	# endpoint_type appears before endpoint_details, so remember it.
	if tt1 == "endpoint_type":
		context.transfer_endpoint_type = tt2
	elif tt1 == "vpc_endpoint_id":
		if getattr(context, "transfer_endpoint_type", "") != "VPC_ENDPOINT":
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
	
	All TRANSFER resources automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_transfer' has no attribute '{name}'")


log.debug(f"TRANSFER handlers: __getattr__ for all 0 resources")