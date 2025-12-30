"""
DOCDB Resource Handlers - Optimized with __getattr__

This file contains ONLY DOCDB resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 2 functions
Optimized: 2 functions + __getattr__
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
# DOCDB Resources with Custom Logic (2 functions)
# ============================================================================

def aws_docdb_cluster(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1 == "cluster_members": t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_docdb_cluster_instance","*",skip)

	elif tt1 == "db_subnet_group_name":
			if tt2 != "default":
				t1=tt1 + " = aws_docdb_subnet_group." + tt2 + ".id\n"
				common.add_dependancy("aws_docdb_subnet_group",tt2)

	elif tt1 == "engine":
		t1=tt1+' = "docdb"\n'
		t1=t1+"\n lifecycle {\n   ignore_changes = [engine,cluster_members]\n}\n"
	return skip,t1,flag1,flag2



def aws_docdb_cluster_instance(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1 == "engine":
		t1=tt1+' = "docdb"\n'
		t1=t1+"\n lifecycle {\n   ignore_changes = [engine]\n}\n"
	## can't do this - will cycle
	#if tt1 == "cluster_identifier":
#		t1=tt1 + " = aws_docdb_cluster." + tt2 + ".id\n"
#		common.add_dependancy("aws_docdb_cluster",tt2)
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
	
	All simple DOCDB resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_docdb' has no attribute '{name}'")


log.debug(f"DOCDB handlers: 2 custom functions + __getattr__ for 0 simple resources")