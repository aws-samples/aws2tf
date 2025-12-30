"""
REDSHIFT_SERVERLESS Resource Handlers - Optimized with __getattr__

This file contains ONLY REDSHIFT_SERVERLESS resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 2 functions
Optimized: 2 functions + __getattr__
Reduction: 0% less code
"""

import logging
import common
import fixtf
import sys
import os
import inspect
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# REDSHIFT_SERVERLESS Resources with Custom Logic (2 functions)
# ============================================================================

def aws_redshiftserverless_namespace(t1,tt1,tt2,flag1,flag2):


    try:
        skip=0


        if tt1 == "default_iam_role_arn":  t1=fixtf.deref_role_arn(t1,tt1,tt2)

        ##elif tt1 == "iam_roles":  t1=fixtf.deref_role_arn_array(t1,tt1,tt2)

    except Exception as e:
        common.handle_error2(e,str(inspect.currentframe().f_code.co_name),id)    
    
    return skip,t1,flag1,flag2 




def aws_redshiftserverless_workgroup(t1,tt1,tt2,flag1,flag2):


    skip=0

    if tt1 == "namespace_name": 
        
        t1=tt1 + " = aws_redshiftserverless_namespace." + tt2 + ".id\n"
        common.add_dependancy("aws_redshiftserverless_namespace",tt2)

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
	
	All simple REDSHIFT_SERVERLESS resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_redshift_serverless' has no attribute '{name}'")


log.debug(f"REDSHIFT_SERVERLESS handlers: 2 custom functions + __getattr__ for 0 simple resources")