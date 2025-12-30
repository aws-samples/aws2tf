"""
SDB Resource Handlers - Optimized with __getattr__

This file contains SDB resource handlers.
All resources use the default handler via __getattr__.

Auto-generated stub file.
"""

import logging
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# Magic method for backward compatibility with getattr()
# ============================================================================

def __getattr__(name):
	"""
	Dynamically provide default handler for all SDB resources.
	
	This allows getattr(module, "aws_resource") to work by returning
	the default handler for all resources.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_sdb' has no attribute '{name}'")


log.debug(f"SDB handlers: __getattr__ for all resources")
