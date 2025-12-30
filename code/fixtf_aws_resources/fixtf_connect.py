"""
CONNECT Resource Handlers - Optimized with __getattr__

This file contains ONLY CONNECT resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 8 functions
Optimized: 8 functions + __getattr__
Reduction: 0% less code
"""

import logging
import common
import context
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# CONNECT Resources with Custom Logic (8 functions)
# ============================================================================

def aws_connect_contact_flow(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="instance_id":
		t1=tt1+" = aws_connect_instance.r-"+tt2+".id\n"
		common.add_dependancy("aws_connect_instance",tt2)
	return skip,t1,flag1,flag2



def aws_connect_hours_of_operation(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="instance_id":
		t1=tt1+" = aws_connect_instance.r-"+tt2+".id\n"
		context.connectinid=tt2
		common.add_dependancy("aws_connect_instance",tt2)
	return skip,t1,flag1,flag2



def aws_connect_instance_storage_config(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="instance_id":
		t1=tt1+" = aws_connect_instance.r-"+tt2+".id\n"
		common.add_dependancy("aws_connect_instance",tt2)

	return skip,t1,flag1,flag2



def aws_connect_phone_number(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="target_arn" and tt2.startswith("arn:aws:connect:"):
		cid=tt2.split("/")[1]
		t1=tt1+" = aws_connect_instance.r-"+cid+".arn\n"
	return skip,t1,flag1,flag2



def aws_connect_queue(t1,tt1,tt2,flag1,flag2):


	skip=0
	if "resource" in t1 and "{" in t1 and "aws_connect_queue" in t1:
		inid=t1.split('"r-')[1].split("_")[0]
		context.connectinid=inid


	if tt1=="instance_id":
		t1=tt1+" = aws_connect_instance.r-"+tt2+".id\n"
		context.connectinid=tt2
		common.add_dependancy("aws_connect_instance",tt2)
	elif tt1=="hours_of_operation_id":
		t1=tt1+" = aws_connect_hours_of_operation.r-"+context.connectinid+"_"+tt2+".hours_of_operation_id\n"
	return skip,t1,flag1,flag2



def aws_connect_routing_profile(t1,tt1,tt2,flag1,flag2):


	skip=0
	if "resource" in t1 and "{" in t1 and "aws_connect_routing_profile" in t1:
		inid=t1.split('"r-')[1].split("_")[0]
		context.connectinid=inid
	elif tt1=="name":
		t1=t1+"\n lifecycle {\n   ignore_changes = [media_concurrencies]\n}\n"
	elif tt1=="concurrency" and tt2=="0": 
		t1=tt1+" = 1\n"
	elif tt1=="instance_id":
		t1=tt1+" = aws_connect_instance.r-"+tt2+".id\n"
		context.connectinid=tt2
		common.add_dependancy("aws_connect_instance",tt2)
	elif tt1=="queue_id" or tt1=="default_outbound_queue_id":
		t1=tt1+" = aws_connect_queue.r-"+context.connectinid+"_"+tt2+".queue_id\n"
	return skip,t1,flag1,flag2



def aws_connect_security_profile(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="instance_id":
		t1=tt1+" = aws_connect_instance.r-"+tt2+".id\n"
		common.add_dependancy("aws_connect_instance",tt2)	
	return skip,t1,flag1,flag2



def aws_connect_user(t1,tt1,tt2,flag1,flag2):


	skip=0
	if "resource" in t1 and "{" in t1 and "aws_connect_user" in t1:
		inid=t1.split('"r-')[1].split("_")[0]
		context.connectinid=inid
	if tt1=="instance_id":
		t1=tt1+" = aws_connect_instance.r-"+tt2+".id\n"
		common.add_dependancy("aws_connect_instance",tt2)
		context.connectinid=tt2
	elif tt1=="routing_profile_id":
		t1=tt1+" = aws_connect_routing_profile.r-"+context.connectinid+"_"+tt2+".routing_profile_id\n"
	elif tt1=="security_profile_ids":
		if "," not in tt2:
			secid=tt2.lstrip('[').rstrip(']').strip('"')
			t1=tt1+" = [aws_connect_security_profile.r-"+context.connectinid+"_"+secid+".security_profile_id]\n"
			
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
	
	All simple CONNECT resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_connect' has no attribute '{name}'")


log.debug(f"CONNECT handlers: 8 custom functions + __getattr__ for 0 simple resources")