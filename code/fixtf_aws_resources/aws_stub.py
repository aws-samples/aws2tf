import common
import fixtf
import logging
import context
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')



def __getattr__(name):
	"""
	Dynamically provide default handler for resources without custom logic.
	
	This allows getattr(module, 'aws_stub') to work even if aws_stub function
	doesn't exist, by returning the default handler.
	
	All simple api resources (xx resources) automatically use this:.
	"""
	if name.startswith('aws_'):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_api' has no attribute '{name}'")


log.debug(f"api handlers: 0 custom functions + __getattr__ for xx simple resources")
