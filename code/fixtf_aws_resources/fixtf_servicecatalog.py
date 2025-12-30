"""
SERVICECATALOG Resource Handlers - Optimized with __getattr__

This file contains ONLY SERVICECATALOG resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 5 functions
Optimized: 5 functions + __getattr__
Reduction: 0% less code
"""

import logging
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# SERVICECATALOG Resources with Custom Logic (5 functions)
# ============================================================================

def aws_servicecatalog_constraint(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="portfolio_id" and tt2.startswith("port-"):
		t1=tt1+" = aws_servicecatalog_portfolio."+tt2+".id\n"
	if tt1=="product_id" and tt2.startswith("prod-"):
		t1=tt1+" = aws_servicecatalog_product."+tt2+".id\n"	
	return skip,t1,flag1,flag2



def aws_servicecatalog_principal_portfolio_association(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="portfolio_id" and tt2.startswith("port-"):
		t1=tt1+" = aws_servicecatalog_portfolio."+tt2+".id\n"
	return skip,t1,flag1,flag2



def aws_servicecatalog_product(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="accept_language" and tt2=="null": 
		t1 = tt1 + " = \"en\"\n"
		t1=t1+"\n lifecycle {\n   ignore_changes = [accept_language]\n}\n"
	return skip,t1,flag1,flag2



def aws_servicecatalog_product_portfolio_association(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="portfolio_id" and tt2.startswith("port-"):
		t1=tt1+" = aws_servicecatalog_portfolio."+tt2+".id\n"
	if tt1=="product_id" and tt2.startswith("prod-"):
		t1=tt1+" = aws_servicecatalog_product."+tt2+".id\n"
	return skip,t1,flag1,flag2



def aws_servicecatalog_service_action(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="accept_language" and tt2=="null": 
		t1 = tt1 + " = \"en\"\n"
		t1=t1+"\n lifecycle {\n   ignore_changes = [accept_language]\n}\n"
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
	
	All simple SERVICECATALOG resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_servicecatalog' has no attribute '{name}'")


log.debug(f"SERVICECATALOG handlers: 5 custom functions + __getattr__ for 0 simple resources")