"""
NETWORKMANAGER Resource Handlers - Optimized with __getattr__

This file contains ONLY NETWORKMANAGER resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 3 functions
Optimized: 3 functions + __getattr__
Reduction: 0% less code
"""

import logging
import common
import context
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# NETWORKMANAGER Resources with Custom Logic (3 functions)
# ============================================================================

def aws_networkmanager_device(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="global_network_id" and tt2 !="null":
		t1=tt1+" = aws_networkmanager_global_network."+tt2+".id\n"
		t1=t1+"\nlifecycle {\n" + "   ignore_changes = [location]\n" +  "}\n"
	return skip,t1,flag1,flag2



def aws_networkmanager_site(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="global_network_id" and tt2 !="null":
		t1=tt1+" = aws_networkmanager_global_network."+tt2+".id\n"
		t1=t1+"\nlifecycle {\n" + "   ignore_changes = [location]\n" +  "}\n"


	return skip,t1,flag1,flag2



def aws_networkmanager_transit_gateway_registration(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="global_network_id" and tt2 !="null":
		t1=tt1+" = aws_networkmanager_global_network."+tt2+".id\n"
	elif tt1=="transit_gateway_arn" and tt2 !="null":
		if tt2.startswith("arn:"):
			tgid=tt2.split("/")[-1]
			if tgid in str(context.tgwlist.keys()):
				t1=tt1+" = aws_ec2_transit_gateway."+tgid+".arn\n"
				common.add_dependancy("aws_ec2_transit_gateway",tgid)
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
	
	All simple NETWORKMANAGER resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_networkmanager' has no attribute '{name}'")


log.debug(f"NETWORKMANAGER handlers: 3 custom functions + __getattr__ for 0 simple resources")