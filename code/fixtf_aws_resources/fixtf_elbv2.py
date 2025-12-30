"""
ELBV2 Resource Handlers - Optimized with __getattr__

This file contains ONLY ELBV2 resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 3 functions
Optimized: 3 functions + __getattr__
Reduction: 0% less code
"""

import logging
import context
import common
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# ELBV2 Resources with Custom Logic (3 functions)
# ============================================================================

def aws_lb_listener(t1,tt1,tt2,flag1,flag2):


	skip=0

	if "load_balancer_arn" == tt1:
		tt2=tt2.replace("/","_").replace(".","_").replace(":","_")
		t1 = tt1 + " = aws_lb."+tt2+".arn\n"
		t1=t1+"\n lifecycle {\n   ignore_changes = [default_action[0].forward[0]]\n}\n"

	if "order" == tt1:
		if tt2 == "0": skip=1
	elif "duration" == tt1:
		if tt2 == "0": t1=tt1+" = 1\n"	
		#if tt2 == "0": skip=1

	return skip,t1,flag1,flag2




def aws_lb_listener_rule(t1,tt1,tt2,flag1,flag2):


	skip=0
	if "listener_arn" == tt1:
		tt2=tt2.replace("/","_").replace(".","_").replace(":","_")
		t1 = tt1 + " = aws_lb_listener."+tt2+".arn\n"
		t1=t1+ "\nlifecycle {\n" + "   ignore_changes = [action[0].target_group_arn,action[0].forward[0].stickiness[0].duration]\n" +  "}\n"
	elif "order" == tt1:
		if tt2 == "0": skip=1
	elif "duration" == tt1:
		#if tt2 == "0": skip=1
		if tt2 == "0":	t1=tt1+" = 1\n"


	return skip,t1,flag1,flag2



def aws_lb_target_group(t1,tt1,tt2,flag1,flag2):


	skip=0
	if "on_deregistration" in tt1:
		if tt2 == "null": t1=tt1+" = \"no_rebalance\"\n"
	if "on_unhealthy" in tt1:
		if tt2 == "null": 
			t1=tt1+" = \"no_rebalance\"\n" #+\n lifecycle {\n   ignore_changes = [on_deregistration,on_unhealthy,enable_unhealthy_connection_termination]\n}\n"

	if "enable_unhealthy_connection_termination" in tt1:
		if tt2 == "null": t1=tt1+" = true\n"

	if "target_control_port" in tt1:
		if tt2 == "0": skip=1 

	if "name" == tt1:
		t1=t1+"\n lifecycle {\n   ignore_changes = [target_failover[0].on_deregistration,target_failover[0].on_unhealthy,target_health_state[0].enable_unhealthy_connection_termination]\n}\n"


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
	
	All simple ELBV2 resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_elbv2' has no attribute '{name}'")


log.debug(f"ELBV2 handlers: 3 custom functions + __getattr__ for 0 simple resources")