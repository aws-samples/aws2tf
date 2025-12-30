"""
EMR Resource Handlers - Optimized with __getattr__

This file contains ONLY EMR resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 4 functions
Optimized: 4 functions + __getattr__
Reduction: 0% less code
"""

import logging
import common
import fixtf
import base64
import boto3
import sys
import os
import context
import inspect
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# EMR Resources with Custom Logic (4 functions)
# ============================================================================

def aws_emr_cluster(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="kdc_admin_password":
		if tt2.startswith("null"):
			t1=tt1+" = \"CHANGE_ME\"\n"
	elif tt1=="applications":
		t1=t1+"\n lifecycle {\n   ignore_changes = [kerberos_attributes[0].kdc_admin_password]\n}\n"
		context.emrsubnetid=False
	elif tt1=="subnet_id":
		if "subnet" in tt2: context.emrsubnetid=True
	elif tt1=="subnet_ids":
		if context.emrsubnetid: skip=1
	elif tt1=="security_configuration" and tt2!="null":
		t1=tt1+" = aws_emr_security_configuration."+tt2+".name\n"
		common.add_dependancy("aws_emr_security_configuration", tt2)

		
	return skip,t1,flag1,flag2



def aws_emr_instance_fleet(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="cluster_id" and tt2 !="null":
		t1=tt1+" = aws_emr_cluster."+tt2+".id\n"
		common.add_dependancy("aws_emr_cluster", tt2)
	return skip,t1,flag1,flag2



def aws_emr_instance_group(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="cluster_id" and tt2 !="null":
		t1=tt1+" = aws_emr_cluster."+tt2+".id\n"
		common.add_dependancy("aws_emr_cluster", tt2)

	return skip,t1,flag1,flag2



def aws_emr_security_configuration(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="name":
		t1=t1+"\n lifecycle {\n   ignore_changes = [configuration]\n}\n"
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
	
	All simple EMR resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_emr' has no attribute '{name}'")


log.debug(f"EMR handlers: 4 custom functions + __getattr__ for 0 simple resources")