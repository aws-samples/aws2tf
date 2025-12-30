"""
SSM Resource Handlers - Optimized with __getattr__

This file contains ONLY SSM resources with custom transformation logic.
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
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# SSM Resources with Custom Logic (4 functions)
# ============================================================================

def aws_ssm_document(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="content":
		t1="\n lifecycle {\n   ignore_changes = [content]\n}\n"+t1
	return skip,t1,flag1,flag2



def aws_ssm_maintenance_window(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="schedule_offset" and tt2=="0": 
		t1="lifecycle {\n   ignore_changes = [schedule_offset]\n}\n"
	return skip,t1,flag1,flag2



def aws_ssm_parameter(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1 == "arn": 
		context.ssmparamn=tt2
		skip=1 
	elif tt1 == "value":
		if context.ssmparamn != "":
			client = boto3.client("ssm")
			response = client.get_parameter(Name=context.ssmparamn, WithDecryption=True)
			vs=response["Parameter"]["Value"]
			ml=len(vs.split('\n'))
			if ml > 1:
				vs=vs.replace('\n','').replace('${','$${').replace('\t','')
			if vs.startswith('{"') or vs.startswith('["') :
				t1 = tt1 + " = jsonencode("+vs+")\n"
			else:
				t1 = tt1 + " = \"" + vs + "\"\n"
			context.ssmparamn=""	
	elif tt1 == "insecure_value": 
		t1 ="lifecycle {\n" + "   ignore_changes = [value]\n" +  "}\n"
		
	return skip,t1,flag1,flag2



def aws_ssm_parameters_by_path(t1,tt1,tt2,flag1,flag2):


	skip=0
	client = boto3.client("ssm")
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
	
	All simple SSM resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_ssm' has no attribute '{name}'")


log.debug(f"SSM handlers: 4 custom functions + __getattr__ for 0 simple resources")