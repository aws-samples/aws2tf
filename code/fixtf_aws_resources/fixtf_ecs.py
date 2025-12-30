"""
ECS Resource Handlers - Optimized with __getattr__

This file contains ONLY ECS resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 5 functions
Optimized: 5 functions + __getattr__
Reduction: 0% less code
"""

import logging
import fixtf
import common
import context
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# ECS Resources with Custom Logic (5 functions)
# ============================================================================

def aws_ecs_cluster(t1,tt1,tt2,flag1,flag2):


	skip=0

	if tt1 == "namespace":
		if "arn:" in tt2: t1=fixtf.globals_replace(t1,tt1,tt2)
			
	return skip,t1,flag1,flag2



def aws_ecs_capacity_provider(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="auto_scaling_group_arn" and tt2.startswith("arn:aws:autoscaling:"):
		common.add_dependancy("aws_autoscaling_group", tt2)
	return skip,t1,flag1,flag2



def aws_ecs_cluster_capacity_providers(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="cluster_name":
		t1=tt1+" = aws_ecs_cluster."+tt2+".name\n"
		common.add_dependancy("aws_ecs_cluster", tt2)
	return skip,t1,flag1,flag2



def aws_ecs_service(t1,tt1,tt2,flag1,flag2):


	skip=0

	if tt1 == "cluster":
		
		if "arn:" in tt2: tt2 = tt2.split("/")[-1]
			
		if tt2 != "null": 
			t1=tt1 + " = aws_ecs_cluster." + tt2 + ".id\n"
			common.add_dependancy("aws_ecs_cluster",tt2)
		else:
			skip=1
	elif tt1 == "task_definition":
		
		if "arn:" in tt2: 	
			tt2 = tt2.split("/")[-1]
			t1=tt1 + " = aws_ecs_task_definition." + tt2 + ".arn\n"
			common.add_dependancy("aws_ecs_task_definition",tt2)
		else:
			tdarn="arn:aws:ecs:"+context.region+":"+context.acc+":"+"task-definition:"+tt2
			#tdn=tdarn.replace("/","_").replace(".","_").replace(":","_")
			#t1=tt1+" = aws_ecs_task_definition."+tdn+".id\n"
			common.add_dependancy("aws_ecs_task_definition",tdarn)

	return skip,t1,flag1,flag2



def aws_ecs_task_definition(t1,tt1,tt2,flag1,flag2):


	skip=0
	
	if tt1=="awslogs-group" and tt2 !="null":
		# fixup cw log name
		lgn=tt2.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_")
		t1=tt1 + " = aws_cloudwatch_log_group." + lgn + ".id\n"
		common.add_dependancy("aws_cloudwatch_log_group", tt2) 
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
	
	All simple ECS resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_ecs' has no attribute '{name}'")


log.debug(f"ECS handlers: 5 custom functions + __getattr__ for 0 simple resources")