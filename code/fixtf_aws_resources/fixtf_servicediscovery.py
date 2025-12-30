"""
SERVICEDISCOVERY Resource Handlers - Optimized with __getattr__

This file contains ONLY SERVICEDISCOVERY resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 1 functions
Optimized: 1 functions + __getattr__
Reduction: 0% less code
"""

import logging
import common
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# SERVICEDISCOVERY Resources with Custom Logic (1 functions)
# ============================================================================

def aws_service_discovery_service(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="type" and tt2=="DNS_HTTP": skip=1
	elif tt1=="namespace_id":
		if tt2.startswith("ns-"):
			t1=tt1+" = aws_service_discovery_private_dns_namespace."+tt2+".id\n"
			common.add_dependancy("aws_service_discovery_private_dns_namespace",tt2)
		
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
	
	All simple SERVICEDISCOVERY resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_servicediscovery' has no attribute '{name}'")


log.debug(f"SERVICEDISCOVERY handlers: 1 custom functions + __getattr__ for 0 simple resources")