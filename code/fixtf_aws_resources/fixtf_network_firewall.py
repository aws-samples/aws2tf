"""
NETWORK_FIREWALL Resource Handlers - Optimized with __getattr__

This file contains ONLY NETWORK_FIREWALL resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 3 functions
Optimized: 3 functions + __getattr__
Reduction: 0% less code
"""

import logging
import common
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# NETWORK_FIREWALL Resources with Custom Logic (3 functions)
# ============================================================================

def aws_networkfirewall_firewall(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="firewall_policy_arn":
		if tt2!="null" and tt2.startswith("arn:"):
			tarn=tt2.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_")
			t1=tt1 + " = aws_networkfirewall_firewall_policy." + tarn + ".arn\n"
			common.add_dependancy("aws_networkfirewall_firewall_policy", tt2)
	return skip,t1,flag1,flag2



def aws_networkfirewall_firewall_policy(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="priority" and tt2=="0": skip=1
	elif tt1=="resource_arn" and tt2!="null" and tt2.startswith("arn:"):
		tarn=tt2.replace("/", "_").replace(".", "_").replace(":", "_").replace("|", "_").replace("$", "_").replace(", ", "_").replace("&", "_").replace("#", "_").replace("[", "_").replace("]", "_").replace("=", "_").replace("!", "_").replace(";", "_")
		t1=tt1 + " = aws_networkfirewall_rule_group." + tarn + ".arn\n"
		common.add_dependancy("aws_networkfirewall_rule_group", tt2)
	return skip,t1,flag1,flag2



def aws_networkfirewall_logging_configuration(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="firewall_arn" and tt2!="null" and tt2.startswith("arn:"):
		tarn=tt2.replace("/", "_").replace(".", "_").replace(":", "_").replace("|", "_").replace("$", "_").replace(", ", "_").replace("&", "_").replace("#", "_").replace("[", "_").replace("]", "_").replace("=", "_").replace("!", "_").replace(";", "_")
		t1=tt1 + " = aws_networkfirewall_firewall." + tarn + ".arn\n"
		common.add_dependancy("aws_networkfirewall_firewall", tt2)

	elif tt1==" tls_inspection_configuration_arn" and tt2!="null" and tt2.startswith("arn:"):
		tarn=tt2.replace("/", "_").replace(".", "_").replace(":", "_").replace("|", "_").replace("$", "_").replace(", ", "_").replace("&", "_").replace("#", "_").replace("[", "_").replace("]", "_").replace("=", "_").replace("!", "_").replace(";", "_")
		t1=tt1 + " = aws_networkfirewall_tls_inspection_configuration." + tarn + ".arn\n"
		common.add_dependancy("aws_networkfirewall_tls_inspection_configuration", tt2)
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
	
	All simple NETWORK_FIREWALL resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_network_firewall' has no attribute '{name}'")


log.debug(f"NETWORK_FIREWALL handlers: 3 custom functions + __getattr__ for 0 simple resources")