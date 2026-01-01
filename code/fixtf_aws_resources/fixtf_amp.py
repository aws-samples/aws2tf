"""
AMP Resource Handlers - Optimized with __getattr__

This file contains ONLY AMP resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 1 functions
Optimized: 1 functions + __getattr__
Reduction: 0% less code
"""

import logging
import common
import context
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# AMP Resources with Custom Logic (1 function)
# ============================================================================

def aws_prometheus_query_logging_configuration(t1, tt1, tt2, flag1, flag2):
	skip = 0
	
	# Transform workspace_id field and add workspace as dependency
	if tt1 == "workspace_id" and tt2 != "null":
		workspace_id = tt2.strip('"')
		# Construct ARN-based resource name for workspace
		# Format: arn_aws_aps_us-east-1_566972129213_workspace_ws-<id>
		# We need to get the ARN, but we only have workspace ID
		# For now, add dependency with workspace ID and let aws2tf handle it
		t1="workspace_id = aws_prometheus_workspace."+workspace_id+".id\n"
		common.add_dependancy("aws_prometheus_workspace", workspace_id)
	
	return skip, t1, flag1, flag2


# ============================================================================
# Magic method for backward compatibility with getattr()
# ============================================================================

def __getattr__(name):
	"""
	Dynamically provide default handler for resources without custom logic.
	
	This allows getattr(module, "aws_resource") to work even if the
	function doesn't exist, by returning the default handler.
	
	All other AMP resources automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_amp' has no attribute '{name}'")


log.debug(f"AMP handlers: 1 custom + __getattr__ for remaining resources")




