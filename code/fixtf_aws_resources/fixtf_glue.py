"""
GLUE Resource Handlers - Optimized with __getattr__

This file contains ONLY GLUE resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 5 functions
Optimized: 5 functions + __getattr__
Reduction: 0% less code
"""

import context 
import common
import logging
import fixtf
import base64
import boto3
import sys
import os
import inspect
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# GLUE Resources with Custom Logic (5 functions)
# ============================================================================

def aws_glue_crawler(t1,tt1,tt2,flag1,flag2):


	skip=0
	
	try:
		if tt1 == "database_name" and tt2 != "null":
			if tt2 in str(context.gluedbs):
				t1 = tt1 + " = aws_glue_catalog_database.d-"+context.acc+"__"+tt2+".name\n"
			#common.add_dependancy("aws_glue_catalog_database",tt2)

		elif tt1 == "sample_size":
			if tt2 == "0": skip=1
		elif tt1 == "security_configuration" and tt2 != "null":
			t1 = tt1 + " = aws_glue_security_configuration."+tt2+".id\n"
			common.add_dependancy("aws_glue_security_configuration",tt2)
	except Exception as e:
		log.error(e)
		log.error("fixtf_glue.py aws_glue_crawler Exception= %s",  str(e))
		log.error("fixtf_glue.py t1= %s",  t1)
	
	return skip,t1,flag1,flag2



def aws_glue_catalog_table(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1 == "database_name" and tt2 != "null":
		t1 = tt1 + " = aws_glue_catalog_database.d-"+context.acc+"__"+tt2+".name\n"
		common.add_dependancy("aws_glue_catalog_database",tt2)
	return skip,t1,flag1,flag2



def aws_glue_connection(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="connection_properties":
		t1=t1+"\n lifecycle {\n   ignore_changes = [connection_properties]\n}\n"
	return skip,t1,flag1,flag2



def aws_glue_job(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1 == "max_capacity" and tt2 != "null":
		context.gulejobmaxcap=True
	if tt1 == "number_of_workers":
		if context.gulejobmaxcap: skip=1
	if tt1 == "worker_type":
		if context.gulejobmaxcap: skip=1
	if tt1 == "description":
		t1=t1+"\n lifecycle {\n   ignore_changes = [glue_version,number_of_workers,worker_type,role_arn]\n}\n"
	if tt1 == "security_configuration" and tt2 != "null":
		t1 = tt1 + " = aws_glue_security_configuration."+tt2+".id\n"
		common.add_dependancy("aws_glue_security_configuration", tt2)
	if "--output_s3_bucket_name" in tt1:
		t1=tt1 + " = aws_s3_bucket.b-" + tt2 + ".bucket\n"
		common.add_dependancy("aws_s3_bucket",tt2)
	if tt1=="script_location" and tt2.endswith(".py"):
		com="aws s3 cp "+tt2+" ."
		log.debug("executing: "+com)
		log.debug("aws_glue_job t1= %s", t1)
		rout = common.rc(com) 
	
	return skip,t1,flag1,flag2



def aws_glue_trigger(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1 == "timeout": 
		if tt2 == "0": skip=1
	
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
	
	All simple GLUE resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_glue' has no attribute '{name}'")


log.debug(f"GLUE handlers: 5 custom functions + __getattr__ for 0 simple resources")