"""
CHIME_SDK_MEDIA_PIPELINES Resource Handlers - Optimized with __getattr__

This file contains ONLY CHIME_SDK_MEDIA_PIPELINES resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 0 functions
Optimized: 0 functions + __getattr__
Reduction: 0% less code
"""

import logging
import common
import fixtf
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
	
	All CHIME_SDK_MEDIA_PIPELINES resources automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_chime_sdk_media_pipelines' has no attribute '{name}'")


log.debug(f"CHIME_SDK_MEDIA_PIPELINES handlers: __getattr__ for all 0 resources")