"""
APPMESH Resource Handlers - Optimized with __getattr__

This file contains ONLY APPMESH resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 6 functions
Optimized: 6 functions + __getattr__
Reduction: 0% less code
"""

import logging
import common
import context
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# APPMESH Resources with Custom Logic (6 functions)
# ============================================================================

def aws_appmesh_mesh(t1,tt1,tt2,flag1,flag2):


	skip=0
	# deps aws_appmesh_virtual_service, aws_appmesh_virtual_router, aws_appmesh_virtual_node, aws_appmesh_virtual_gateway
	if tt1=="name" and tt2 != "null":
		common.add_dependancy("aws_appmesh_virtual_service",tt2)
		common.add_dependancy("aws_appmesh_virtual_router",tt2)
		common.add_dependancy("aws_appmesh_virtual_node",tt2)
		common.add_dependancy("aws_appmesh_virtual_gateway",tt2)

	
	return skip,t1,flag1,flag2



def aws_appmesh_virtual_gateway(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="mesh_name" and tt2 != "null": 
		t1=tt1+" = aws_appmesh_mesh."+tt2+".id\n"
	#elif tt1=="name" and tt2 != "null": 
	#	common.add_dependancy(aws_appmesh_gateway_route,tt2)

	
	return skip,t1,flag1,flag2



def aws_appmesh_gateway_route(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="port":
		if tt2=="0": skip=1
	return skip,t1,flag1,flag2



def aws_appmesh_virtual_node(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="mesh_name" and tt2 != "null": 
		t1=tt1+" = aws_appmesh_mesh."+tt2+".id\n"
	return skip,t1,flag1,flag2



def aws_appmesh_virtual_router(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="mesh_name" and tt2 != "null": 
		t1=tt1+" = aws_appmesh_mesh."+tt2+".id\n"
	return skip,t1,flag1,flag2



def aws_appmesh_virtual_service(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="mesh_name" and tt2 != "null": 
		t1=tt1+" = aws_appmesh_mesh."+tt2+".id\n"
		context.meshname=tt2
	if tt1=="virtual_node_name" and tt2 != "null": 
		t1=tt1+" = aws_appmesh_virtual_node."+context.meshname+"_"+tt2+".name\n"

	if tt1=="virtual_router_name" and tt2 != "null": 
		t1=tt1+" = aws_appmesh_virtual_router."+context.meshname+"_"+tt2+".name\n"
	
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
	
	All simple APPMESH resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_appmesh' has no attribute '{name}'")


log.debug(f"APPMESH handlers: 6 custom functions + __getattr__ for 0 simple resources")