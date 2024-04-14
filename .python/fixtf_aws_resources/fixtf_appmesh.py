import common
import globals



def aws_appmesh_mesh(t1,tt1,tt2,flag1,flag2):
	skip=0
	# deps aws_appmesh_virtual_service, aws_appmesh_virtual_router, aws_appmesh_virtual_node, aws_appmesh_virtual_gateway
	if tt1=="name" and tt2 != "null":
		common.add_dependancy("aws_appmesh_virtual_service",tt2)
		common.add_dependancy("aws_appmesh_virtual_router",tt2)
		common.add_dependancy("aws_appmesh_virtual_node",tt2)
		common.add_dependancy("aws_appmesh_virtual_gateway",tt2)

	
	return skip,t1,flag1,flag2

def aws_appmesh_route(t1,tt1,tt2,flag1,flag2):
	skip=0
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
		globals.meshname=tt2
	if tt1=="virtual_node_name" and tt2 != "null": 
		t1=tt1+" = aws_appmesh_virtual_node."+globals.meshname+"_"+tt2+".name\n"

	if tt1=="virtual_router_name" and tt2 != "null": 
		t1=tt1+" = aws_appmesh_virtual_router."+globals.meshname+"_"+tt2+".name\n"
	
	return skip,t1,flag1,flag2

