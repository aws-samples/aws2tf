"""
KENDRA Resource Handlers - Optimized with __getattr__

This file contains ONLY KENDRA resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 5 functions
Optimized: 5 functions + __getattr__
Reduction: 0% less code
"""

import logging
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# KENDRA Resources with Custom Logic (5 functions)
# ============================================================================

def aws_kendra_data_source(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="index_id": t1 = tt1 + " = aws_kendra_index.k-" + tt2+ ".id\n"
	return skip,t1,flag1,flag2



def aws_kendra_experience(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="index_id": t1 = tt1 + " = aws_kendra_index.k-" + tt2+ ".id\n"
	elif tt1=="data_source_ids" and tt2=="[]": skip=1
	elif tt1=="faq_ids" and tt2=="[]": skip=1

	return skip,t1,flag1,flag2



def aws_kendra_faq(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="index_id": t1 = tt1 + " = aws_kendra_index.k-" + tt2+ ".id\n"
	return skip,t1,flag1,flag2



def aws_kendra_query_suggestions_block_list(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="index_id": t1 = tt1 + " = aws_kendra_index.k-" + tt2+ ".id\n"
	return skip,t1,flag1,flag2



def aws_kendra_thesaurus(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="index_id": t1 = tt1 + " = aws_kendra_index.k-" + tt2+ ".id\n"
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
	
	All simple KENDRA resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_kendra' has no attribute '{name}'")


log.debug(f"KENDRA handlers: 5 custom functions + __getattr__ for 0 simple resources")