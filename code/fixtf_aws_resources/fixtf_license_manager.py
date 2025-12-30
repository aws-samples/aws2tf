"""
LICENSE_MANAGER Resource Handlers - Optimized with __getattr__

This file contains ONLY LICENSE_MANAGER resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 0 functions
Optimized: 0 functions + __getattr__
Reduction: 0% less code
"""

import logging
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# Magic method for backward compatibility with getattr()
# ============================================================================

def __getattr__(name):
	"""
	Dynamically provide default handler for resources without custom logic.
	
	This allows getattr(module, "aws_resource") to work even if the
	function doesn't exist, by returning the default handler.
	
	All LICENSE_MANAGER resources automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_license_manager' has no attribute '{name}'")


log.debug(f"LICENSE_MANAGER handlers: __getattr__ for all 0 resources")