"""
S3TABLES Resource Handlers - Optimized with __getattr__

This file contains ONLY S3TABLES resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 2 functions
Optimized: 2 functions + __getattr__
Reduction: 0% less code
"""

import logging
import common
import context
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# S3TABLES Resources with Custom Logic (2 functions)
# ============================================================================

def aws_s3tables_table(t1,tt1,tt2,flag1,flag2):


    skip=0
    #if tt1=="namespace" and tt2 !="null":
    #    t1=tt1+" = aws_s3tables_namespace."+tt2+".id\n"
    if tt1=="table_bucket_arn" and tt2 !="null":
        barn=tt2.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_")
        t1=tt1+" = aws_s3tables_table_bucket."+barn+".arn\n"
 
    
    return skip,t1,flag1,flag2



def aws_s3tables_namespace(t1,tt1,tt2,flag1,flag2):


    skip=0
    if tt1=="table_bucket_arn" and tt2 !="null":
        barn=tt2.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_")
        t1=tt1+" = aws_s3tables_table_bucket."+barn+".arn\n"
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
	
	All simple S3TABLES resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_s3tables' has no attribute '{name}'")


log.debug(f"S3TABLES handlers: 2 custom functions + __getattr__ for 0 simple resources")


def aws_s3tables_table_policy(t1, tt1, tt2, flag1, flag2):
    skip = 0
    
    # Add lifecycle block to ignore resource_policy (JSON normalization issues)
    if tt1 == "table_bucket_arn" and tt2 != "null":
        t1 = t1 + "\n lifecycle {\n   ignore_changes = [resource_policy]\n}\n"
    
    return skip, t1, flag1, flag2
