"""
ATHENA Resource Handlers - Optimized with __getattr__

This file contains ONLY ATHENA resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 1 functions
Optimized: 1 functions + __getattr__
Reduction: 0% less code
"""

import common
import context
import logging
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# ATHENA Resources with Custom Logic (1 functions)
# ============================================================================

def aws_athena_named_query(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1 == "database" and tt2 != "null":
		if "-" not in tt2:
			t1 = tt1 + " = aws_athena_database." + tt2 + ".name\n"
			common.add_dependancy("aws_athena_database", tt2)
		else:
			common.log_warning("WARNING: aws_athena_named_query database name has a dash in it %s",  tt2)
	elif tt1 == "workgroup" and tt2 != "null":
		t1 = tt1 + " = aws_athena_workgroup." + tt2 + ".name\n"
		common.add_dependancy("aws_athena_workgroup", tt2)
		

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
	
	All simple ATHENA resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_athena' has no attribute '{name}'")


log.debug(f"ATHENA handlers: 1 custom functions + __getattr__ for 0 simple resources")