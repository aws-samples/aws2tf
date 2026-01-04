"""
SAGEMAKER Resource Handlers - Optimized with __getattr__

This file contains ONLY SAGEMAKER resources with custom transformation logic.
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
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# SAGEMAKER Resources with Custom Logic (3 functions)
# ============================================================================

def aws_sagemaker_app(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="domain_id" and tt2!="null":
		t1=tt1+" = aws_sagemaker_domain."+tt2+".id\n"
		common.add_dependancy("aws_sagemaker_domain",tt2)
	return skip,t1,flag1,flag2



def aws_sagemaker_domain(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="tag_propagation" and tt2=="null":	
		t1=tt1 + " = \"DISABLED\"\n"
		t1=t1+"\n lifecycle {\n   ignore_changes = [tag_propagation]\n}\n"
	return skip,t1,flag1,flag2



def aws_sagemaker_user_profile(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="domain_id" and tt2!="null":
		t1=tt1+" = aws_sagemaker_domain."+tt2+".id\n"
		common.add_dependancy("aws_sagemaker_domain",tt2)
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
	
	All simple SAGEMAKER resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_sagemaker' has no attribute '{name}'")


log.debug(f"SAGEMAKER handlers: 3 custom functions + __getattr__ for 0 simple resources")


def aws_sagemaker_flow_definition(t1, tt1, tt2, flag1, flag2):
    skip = 0
    
    # Skip empty task_keywords list (requires at least 1 item)
    if tt1 == "task_keywords" and tt2 == "[]":
        skip = 1
    
    return skip, t1, flag1, flag2


def aws_sagemaker_pipeline(t1,tt1,tt2,flag1,flag2):

	skip=0
	# Add lifecycle block to ignore pipeline_definition changes (JSON formatting differences)
	if tt1=="pipeline_name" and tt2 != "null":
		t1 = t1 + "\n lifecycle {\n   ignore_changes = [pipeline_definition]\n}\n"
	return skip,t1,flag1,flag2
