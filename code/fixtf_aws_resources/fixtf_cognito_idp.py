"""
COGNITO_IDP Resource Handlers - Optimized with __getattr__

This file contains ONLY COGNITO_IDP resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 3 functions
Optimized: 3 functions + __getattr__
Reduction: 0% less code
"""

import logging
import common
import fixtf
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# COGNITO_IDP Resources with Custom Logic (3 functions)
# ============================================================================

def aws_cognito_user_group(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1 == "user_pool_id" and tt2 != "null":
		t1=tt1+" = aws_cognito_user_pool."+tt2+".id\n"
		common.add_dependancy("aws_cognito_user_pool",tt2)
	return skip,t1,flag1,flag2



def aws_cognito_user_pool(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="email_verification_message" or tt1=="email_verification_subject" or tt1=="sms_authentication_message" or tt1=="sms_verification_message": 
		skip=1
	if tt1=="username_attributes" and tt2=="[]":
		skip=1
	return skip,t1,flag1,flag2



def aws_cognito_user_pool_client(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="access_token_validity":
		if tt2=="0":
			t1=tt1+" = 1\n" + "\nlifecycle {\n" + "   ignore_changes = [access_token_validity]\n" +  "}\n"

	if tt1=="id_token_validity":
		if tt2=="0": skip=1
			#t1=tt1+" = 1\n" + "\nlifecycle {\n" + "   ignore_changes = [id_token_validity]\n" +  "}\n"

	elif tt1 == "user_pool_id" and tt2 != "null":
		t1=tt1+" = aws_cognito_user_pool."+tt2+".id\n"
		common.add_dependancy("aws_cognito_user_pool",tt2)
	
	elif tt1=="access_token":
		if tt2=="null":
			t1=tt1+" = \"hours\"\n"
	elif tt1=="refresh_token":
		if tt2=="null":
			t1=tt1+" = \"days\"\n"
	
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
	
	All simple COGNITO_IDP resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_cognito_idp' has no attribute '{name}'")


log.debug(f"COGNITO_IDP handlers: 3 custom functions + __getattr__ for 0 simple resources")