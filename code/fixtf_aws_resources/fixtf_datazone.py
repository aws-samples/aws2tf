"""
DATAZONE Resource Handlers - Optimized with __getattr__

This file contains ONLY DATAZONE resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 7 functions
Optimized: 7 functions + __getattr__
Reduction: 0% less code
"""

import logging
import common
import context
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# DATAZONE Resources with Custom Logic (7 functions)
# ============================================================================

def aws_datazone_project(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="domain_identifier" and tt2!="null":
		t1=tt1+" = aws_datazone_domain."+tt2+".id\n"
		context.dzd=tt2
		common.add_dependancy("aws_datazone_domain",tt2)
	return skip,t1,flag1,flag2



def aws_datazone_glossary(t1,tt1,tt2,flag1,flag2):


	skip=0
	## workaround
	## 
	if tt1=="domain_identifier" and tt2!="null":
		context.dzd=tt2
		t1=tt1+" = aws_datazone_domain."+tt2+".id\n"
		common.add_dependancy("aws_datazone_domain",tt2)
	elif tt1=="owning_project_identifier" and tt2!="null":
		t1=tt1+" = aws_datazone_project."+context.dzd+"_"+tt2+".id\n"
	elif tt1=="description" and tt2!="null":
		t1=tt1+" = \"changeme\"\n"
		t1=t1+"\n lifecycle {\n   ignore_changes = [description]\n}\n"
	return skip,t1,flag1,flag2



def aws_datazone_glossary_term(t1,tt1,tt2,flag1,flag2):


	skip=0
	if "resource" in t1 and "{" in t1 and "aws_datazone_glossary_term" in t1:
		did="dzd_"+t1.split("dzd_")[1].split("_")[0]

		gid=t1.split("dzd_")[1].split("_")[2]
		
		pid=t1.split("dzd_")[1].split("_")[3].split('"')[0]
		context.dzd=did
		context.dzgid=gid
		context.dzpid=pid


	if tt1=="domain_identifier" and tt2!="null":
		context.dzd=tt2
		t1=tt1+" = aws_datazone_domain."+tt2+".id\n"
	elif tt1=="glossary_identifier" and tt2!="null":
		t1=tt1+" = aws_datazone_glossary."+context.dzd+"_"+context.dzgid+"_"+context.dzpid+".id\n"
	elif tt1=="is_a" and tt2!="null":
		if "," not in tt2:
			tid=tt2.split('"')[1]
			t1=tt1+" = [aws_datazone_glossary_term."+context.dzd+"_"+tid+"_"+context.dzgid+"_"+context.dzpid+".id]\n"
	#	common.add_dependancy("aws_datazone_glossary", tt2)
	# Will cause Terraform Error: cycle issues
	#elif tt1=="classifies" and tt2!="null":
	#	if "," not in tt2:
#			tid=tt2.split('"')[1]
#			t1=tt1+" = [aws_datazone_glossary_term."+context.dzd+"_"+tid+"_"+context.dzgid+"_"+context.dzpid+".id]\n"
	#	common.add_dependancy("aws_datazone_glossary", tt2)
	return skip,t1,flag1,flag2



def aws_datazone_environment_blueprint_configuration(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="domain_id" and tt2!="null":
		context.dzd=tt2
		t1=tt1+" = aws_datazone_domain."+tt2+".id\n"
		common.add_dependancy("aws_datazone_domain",tt2)

	return skip,t1,flag1,flag2



def aws_datazone_environment_profile(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="domain_identifier" and tt2!="null":
		context.dzd=tt2
		t1=tt1+" = aws_datazone_domain."+tt2+".id\n"
		common.add_dependancy("aws_datazone_domain",tt2)


	elif tt1=="project_identifier" and tt2!="null":
		t1=tt1+" = aws_datazone_project."+context.dzd+"_"+tt2+".id\n"
		#common.add_dependancy("aws_datazone_project",tt2)
	#elif tt1=="environment_blueprint_identifier":	
	#	t1=tt1+" = aws_datazone_environment_blueprint_configuration."+context.dzd+"_"+tt2+".environment_blueprint_id\n"


	return skip,t1,flag1,flag2



def aws_datazone_environment(t1,tt1,tt2,flag1,flag2):


	skip=0
	
	if "resource" in t1 and "{" in t1 and "aws_datazone_environment" in t1:
		did="dzd_"+t1.split("dzd_")[1].split("_")[0]
		context.dzd=did
	if tt1=="domain_identifier" and tt2!="null":
		t1=tt1+" = aws_datazone_domain."+tt2+".id\n"
		context.dzd=tt2
		common.add_dependancy("aws_datazone_domain",tt2)

	elif tt1=="profile_identifier" and tt2!="null":
		t1=tt1+" = aws_datazone_environment_profile."+context.dzd+"_"+tt2+".id\n"
		#common.add_dependancy("aws_datazone_project",tt2)

	elif tt1=="project_identifier" and tt2!="null":
		t1=tt1+" = aws_datazone_project."+context.dzd+"_"+tt2+".id\n"
		#common.add_dependancy("aws_datazone_project",tt2)
	#elif tt1=="blueprint_identifier":
	#	t1=tt1+" = aws_datazone_environment_blueprint_configuration."+context.dzd+"_"+tt2+".environment_blueprint_id\n"

	return skip,t1,flag1,flag2



def aws_datazone_user_profile(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="domain_identifier" and tt2!="null":
		t1=tt1+" = aws_datazone_domain."+tt2+".id\n"
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
	
	All simple DATAZONE resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_datazone' has no attribute '{name}'")


log.debug(f"DATAZONE handlers: 7 custom functions + __getattr__ for 0 simple resources")