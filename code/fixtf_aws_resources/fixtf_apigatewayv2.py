"""
APIGATEWAYV2 Resource Handlers - Optimized with __getattr__

This file contains ONLY APIGATEWAYV2 resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 3 functions
Optimized: 3 functions + __getattr__
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
# APIGATEWAYV2 Resources with Custom Logic (3 functions)
# ============================================================================

def aws_apigatewayv2_integration(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="payload_format_version":
		if "1" in tt2:
			t1=tt1+" = \"1.0\"\n"
		elif "2" in tt2:
			t1=tt1+" = \"2.0\"\n"
	return skip,t1,flag1,flag2



def aws_apigatewayv2_route(t1,tt1,tt2,flag1,flag2):


	skip=0
	try:
		if tt1 == "authorizer_id" and tt2 != "null":
			t1=tt1+" = aws_apigatewayv2_authorizer."+context.api_id+"_"+tt2+".id\n"
			
	except Exception as e:
		common.handle_error2(e,str(inspect.currentframe().f_code.co_name),id)
	return skip,t1,flag1,flag2



def aws_apigatewayv2_stage(t1,tt1,tt2,flag1,flag2):


	skip=0
	try:
		### FIX THIS
		if tt1 == "deployment_id" and tt2 != "null":
			t1=tt1+" = aws_apigatewayv2_deployment."+context.api_id+"_"+tt2+".id\n"
	except Exception as e:
		common.handle_error2(e,str(inspect.currentframe().f_code.co_name),id)
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
	
	All simple APIGATEWAYV2 resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_apigatewayv2' has no attribute '{name}'")


log.debug(f"APIGATEWAYV2 handlers: 3 custom functions + __getattr__ for 0 simple resources")