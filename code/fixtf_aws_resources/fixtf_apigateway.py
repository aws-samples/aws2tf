"""
APIGATEWAY Resource Handlers - Optimized with __getattr__

This file contains ONLY APIGATEWAY resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 6 functions
Optimized: 6 functions + __getattr__
Reduction: 0% less code
"""

import logging
import fixtf
import common
import context
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# APIGATEWAY Resources with Custom Logic (3 functions)
# ============================================================================

def aws_api_gateway_method(t1,tt1,tt2,flag1,flag2):


	skip=0
	if t1.startswith("resource"):
		context.apigwrestapiid=t1.split("r-")[1].split("_")[0]
	if tt1=="resource_id" and tt2 != "null":
		t1=tt1 + " = aws_api_gateway_resource.r-" + str(context.apigwrestapiid)+"_" + tt2 + ".id\n"
		common.add_dependancy("aws_api_gateway_resource", str(context.apigwrestapiid)+"_"+tt2)
	if tt1=="authorizer_id" and tt2 != "null":
		t1=tt1 + " = aws_api_gateway_authorizer.r-" + str(context.apigwrestapiid)+"_" + tt2 + ".id\n"
		common.add_dependancy("aws_api_gateway_authorizer", str(context.apigwrestapiid)+"_"+tt2)
	return skip,t1,flag1,flag2


def aws_api_gateway_documentation_part(t1,tt1,tt2,flag1,flag2):

	skip=0
	if t1.startswith("resource"):
		context.apigwrestapiid=t1.split("r-")[1].split("_")[0]
	if tt1=="rest_api_id" and tt2 != "null":
		t1=tt1 + " = aws_api_gateway_rest_api.r-" + str(context.apigwrestapiid) + ".id\n"
		common.add_dependancy("aws_api_gateway_rest_api", str(context.apigwrestapiid))
	return skip,t1,flag1,flag2


def aws_api_gateway_model(t1,tt1,tt2,flag1,flag2):

	skip=0
	if t1.startswith("resource"):
		context.apigwrestapiid=t1.split("r-")[1].split("_")[0]
	if tt1=="rest_api_id" and tt2 != "null":
		t1=tt1 + " = aws_api_gateway_rest_api.r-" + str(context.apigwrestapiid) + ".id\n"
		common.add_dependancy("aws_api_gateway_rest_api", str(context.apigwrestapiid))
	return skip,t1,flag1,flag2


def aws_api_gateway_request_validator(t1,tt1,tt2,flag1,flag2):

	skip=0
	if t1.startswith("resource"):
		context.apigwrestapiid=t1.split("r-")[1].split("_")[0]
	if tt1=="rest_api_id" and tt2 != "null":
		t1=tt1 + " = aws_api_gateway_rest_api.r-" + str(context.apigwrestapiid) + ".id\n"
		common.add_dependancy("aws_api_gateway_rest_api", str(context.apigwrestapiid))
	return skip,t1,flag1,flag2



def aws_api_gateway_rest_api(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1 == "vpc_endpoint_ids":
		if tt2=="[]": skip=1
	return skip,t1,flag1,flag2



def aws_api_gateway_stage(t1,tt1,tt2,flag1,flag2):


	skip=0
	if t1.startswith("resource"):
		context.apigwrestapiid=t1.split("r-")[1].split("_")[0]
	if tt1=="deployment_id" and tt2 != "null":
		t1=tt1 + " = aws_api_gateway_deployment.r-" + str(context.apigwrestapiid)+"_" + tt2 + ".id\n"
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
	
	All simple APIGATEWAY resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_apigateway' has no attribute '{name}'")


log.debug(f"APIGATEWAY handlers: 3 custom functions + __getattr__ for 0 simple resources")


def aws_api_gateway_documentation_version(t1,tt1,tt2,flag1,flag2):

	skip=0
	if t1.startswith("resource"):
		context.apigwrestapiid=t1.split("r-")[1].split("_")[0]
	if tt1=="rest_api_id" and tt2 != "null":
		t1=tt1 + " = aws_api_gateway_rest_api.r-" + str(context.apigwrestapiid) + ".id\n"
		common.add_dependancy("aws_api_gateway_rest_api", str(context.apigwrestapiid))
	return skip,t1,flag1,flag2


def aws_api_gateway_gateway_response(t1,tt1,tt2,flag1,flag2):

	skip=0
	if t1.startswith("resource"):
		context.apigwrestapiid=t1.split("r-")[1].split("_")[0]
	if tt1=="rest_api_id" and tt2 != "null":
		t1=tt1 + " = aws_api_gateway_rest_api.r-" + str(context.apigwrestapiid) + ".id\n"
		common.add_dependancy("aws_api_gateway_rest_api", str(context.apigwrestapiid))
	return skip,t1,flag1,flag2


def aws_api_gateway_rest_api_policy(t1,tt1,tt2,flag1,flag2):

	skip=0
	if t1.startswith("resource"):
		# Extract REST API ID from resource name (no "r-" prefix for policy resources)
		parts = t1.split('"')
		if len(parts) >= 4:
			context.apigwrestapiid = parts[3]
	if tt1=="rest_api_id" and tt2 != "null":
		t1=tt1 + " = aws_api_gateway_rest_api.r-" + str(context.apigwrestapiid) + ".id\n"
		# Add lifecycle block to ignore JSON key ordering changes
		t1 = t1 + "\n lifecycle {\n   ignore_changes = [policy]\n}\n"
		common.add_dependancy("aws_api_gateway_rest_api", str(context.apigwrestapiid))
	return skip,t1,flag1,flag2


def aws_api_gateway_usage_plan_key(t1,tt1,tt2,flag1,flag2):

	skip=0
	if t1.startswith("resource"):
		# Extract usage plan ID and key ID from resource name
		# Format: r-usagePlanId_keyId
		name_parts = t1.split('"')[3]  # Get resource name
		if '_' in name_parts:
			parts = name_parts.split('_', 1)
			context.usageplanid = parts[0].replace('r-', '')
			if len(parts) > 1:
				context.apikeyid = parts[1]
	if tt1=="usage_plan_id" and tt2 != "null":
		t1=tt1 + " = aws_api_gateway_usage_plan.r-" + str(context.usageplanid) + ".id\n"
		common.add_dependancy("aws_api_gateway_usage_plan", str(context.usageplanid))
	if tt1=="key_id" and tt2 != "null":
		# API key resources don't use "r-" prefix
		t1=tt1 + " = aws_api_gateway_api_key." + str(context.apikeyid) + ".id\n"
		common.add_dependancy("aws_api_gateway_api_key", str(context.apikeyid))
	return skip,t1,flag1,flag2
