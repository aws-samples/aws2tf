"""
S3VECTORS Resource Handlers - Optimized with __getattr__

This file contains S3VECTORS resource handlers.
"""

import logging
from .base_handler import BaseResourceHandler
import context

log = logging.getLogger('aws2tf')


def aws_s3vectors_vector_bucket(t1, tt1, tt2, flag1, flag2):
	"""Handle S3 Vectors vector bucket resource."""
	skip = 0
	
	# Set force_destroy to false if null
	if tt1 == "force_destroy" and tt2 == "null":
		t1 = tt1 + " = false\n"
	
	# Skip computed fields
	elif tt1 in ["creation_time", "vector_bucket_arn", "tags_all"]:
		skip = 1
	
	# Skip encryption_configuration entirely - it's computed and has defaults
	elif tt1 == "encryption_configuration" or context.lbc > 0:
		if tt2 == "[]":
			skip = 1
		if "[" in t1:
			context.lbc = context.lbc + 1
		if "]" in t1:
			context.lbc = context.lbc - 1
		
		# Skip everything in the block
		if context.lbc > 0:
			skip = 1
		if context.lbc == 0 and "]" in t1.strip():
			skip = 1
	
	# Add lifecycle block after vector_bucket_name
	elif tt1 == "vector_bucket_name":
		t1 = t1 + "\n lifecycle {\n   ignore_changes = [force_destroy]\n}\n"
	
	return skip, t1, flag1, flag2


# ============================================================================
# Magic method for backward compatibility with getattr()
# ============================================================================

def __getattr__(name):
	"""
	Dynamically provide default handler for all S3VECTORS resources.
	
	This allows getattr(module, "aws_resource") to work by returning
	the default handler for all resources.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_s3vectors' has no attribute '{name}'")


log.debug(f"S3VECTORS handlers: 1 custom + __getattr__ for remaining resources")
