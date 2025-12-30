"""
RDS Resource Handlers - Optimized with __getattr__

This file contains ONLY RDS resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 4 functions
Optimized: 4 functions + __getattr__
Reduction: 0% less code
"""

import common
import fixtf
import logging
import context
import inspect
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# RDS Resources with Custom Logic (4 functions)
# ============================================================================

def aws_db_instance(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1 == "domain_dns_ips":
		if tt2 == "[]": skip=1
	elif tt1 == "db_name" or tt1 ==  "username":
		if context.repdbin: skip=1
	elif tt1 == "parameter_group_name" and tt2 != "null":
		if "default" not in tt2:
			t1=tt1 + " = aws_db_parameter_group." + tt2 + ".id\n"
			common.add_dependancy("aws_db_parameter_group", tt2)
	elif tt1 == "db_subnet_group_name" and tt2 != "null":
		if "default" not in tt2:
			t1=tt1 + " = aws_db_subnet_group." + tt2 + ".id\n"
			common.add_dependancy("aws_db_subnet_group",tt2)
	elif tt1 == "replicate_source_db" and tt2 != "null":
		if tt2.startswith("arn:"):
			if context.region in tt2:
				tt2=tt2.split(":")[-1]
				t1=tt1 + " = aws_db_instance." + tt2.split(":")[1] + ".arn\n"
				common.add_dependancy("aws_db_instance", tt2.split(":")[1])
		else:
			t1=tt1 + " = aws_db_instance." + tt2 + ".arn\n"
			common.add_dependancy("aws_db_instance", tt2)


	return skip,t1,flag1,flag2



def aws_db_option_group(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="name":
		if tt2.startswith("default:"):
			tt2=tt2.split(":")[1] 
			t1=tt1 + ' = "'+tt2+'"\n'
	return skip,t1,flag1,flag2



def aws_rds_cluster(t1,tt1,tt2,flag1,flag2):


	try:
		skip=0

		if tt1 == "db_cluster_parameter_group_name":
			if not tt2.startswith("default"):
				t1=tt1 + " = aws_rds_cluster_parameter_group." + tt2 + ".id\n"
				common.add_dependancy("aws_rds_cluster_parameter_group",tt2)
		elif tt1 == "db_subnet_group_name":
			if tt2 != "default":
				t1=tt1 + " = aws_db_subnet_group." + tt2 + ".id\n"
				common.add_dependancy("aws_db_subnet_group",tt2)
		elif tt1 == "cluster_members": 
			#t1,skip=fixtf.deref_array(t1,tt1,tt2,"aws_rds_cluster_instance","",skip)
			cc=tt2.count(',')
			if cc == 0:
				inn=tt2.strip('[]').strip("'")
				inn=inn.strip('"')
				#t1=tt1 + " = aws_rds_cluster_instance." + inn + ".id\n"
				common.add_dependancy("aws_rds_cluster_instance",inn)
			if cc > 0:
				log.debug("---cc->>>> %s",  cc)
				for i in range(cc):
					inn=tt2.split(', ')[i].strip('[]').strip("'")
					inn=inn.strip('"')
					log.debug("--inn->>>> %s",  inn)
					#t1=tt1 + " = aws_rds_cluster_instance." + inn + ".id\n"
					common.add_dependancy("aws_rds_cluster_instance", inn)
		# Error: Cycle: aws_rds_cluster.launch-database-qkj2lkbcs7ne-auroras-auroracluster-oxhqkawhlbto, aws_rds_cluster_instance.mdadb

		

	except Exception as e:
		log.error("*** Exception in aws_rds_cluster: " + str(e))
		common.handle_error2(e,"aws_rds_cluster","mdadb")
    
	return skip,t1,flag1,flag2



def aws_rds_cluster_instance(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="performance_insights_retention_period":
		if tt2=="0":
			skip=1
	elif tt1 == "cluster_identifier" and tt2 != "null":
		t1=tt1 + " = aws_rds_cluster." + tt2 + ".id\n"
		common.add_dependancy("aws_rds_cluster", tt2)
	elif tt1 == "db_subnet_group_name" and tt2 != "null":
		if tt2 != "default":
			t1=tt1 + " = aws_db_subnet_group." + tt2 + ".id\n"
			common.add_dependancy("aws_db_subnet_group", tt2)

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
	
	All simple RDS resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_rds' has no attribute '{name}'")


log.debug(f"RDS handlers: 4 custom functions + __getattr__ for 0 simple resources")