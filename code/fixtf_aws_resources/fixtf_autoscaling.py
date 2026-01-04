"""
AUTOSCALING Resource Handlers - Optimized with __getattr__

This file contains ONLY AUTOSCALING resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 2 functions
Optimized: 2 functions + __getattr__
Reduction: 0% less code
"""

import context
import common
import logging
import fixtf
import base64
import boto3
import inspect
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# AUTOSCALING Resources with Custom Logic (2 functions)
# ============================================================================

def aws_autoscaling_group(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="capacity_rebalance":
		t1=t1+"\n lifecycle {\n   ignore_changes = [force_delete,force_delete_warm_pool,ignore_failed_scaling_activities,wait_for_capacity_timeout]\n}\n"
	elif tt1 == "load_balancers" and tt2 == "[]": skip=1
	elif tt1 == "target_group_arns": skip=1
	elif tt1 == "availability_zones":
		if len(tt2) > 4: context.asg_azs=True
	elif tt1 == "vpc_zone_identifier":
		if context.asg_azs: skip=1

	elif tt1 == "force_delete" or tt1=="force_delete_warm_pool" or tt1=="ignore_failed_scaling_activities":
		if tt2=="null":
			t1 = tt1 +" = false\n"
   			

	elif tt1=="wait_for_capacity_timeout":
		if tt2=="null":
			t1 = tt1 +" = \"10m\"\n"

	elif tt1=="launch_configuration":
		if tt2!="null":
			t1 = tt1 +" = aws_launch_configuration."+tt2+".id\n"
			common.add_dependancy("aws_launch_configuration",tt2)

	elif tt1=="launch_template_id":
		if tt2!="null":
			if context.ltlist[id]:
				t1 = tt1 +" = aws_launch_template."+tt2+".id\n"
				common.add_dependancy("aws_launch_template",tt2)
	elif tt1=="id":
		if tt2.startswith("lt-"):
			if context.ltlist[id]:
				t1 = tt1 +" = aws_launch_template."+tt2+".id\n"
				common.add_dependancy("aws_launch_template",tt2)
				flag1=True

	elif tt1=="name":
		if flag1:
			skip=1
			flag1=False

	elif tt1=="on_demand_max_price_percentage_over_lowest_price" and tt2=="0": skip=1
	elif tt1=="spot_max_price_percentage_over_lowest_price" and tt2=="0": skip=1

	return skip,t1,flag1,flag2



def aws_launch_configuration(t1,tt1,tt2,flag1,flag2):


	skip=0

	if tt1 == "id":
			flag2=tt2

	elif tt1 == "iam_instance_profile":
		if tt2 != "null":
			t1 = tt1 + " = aws_iam_instance_profile."+tt2+".id\n"
			common.add_dependancy("aws_iam_instance_profile",tt2)

	elif tt1 == "key_name": 
		if tt2 != "null":
			if not context.dkey:
				tfil=tt2.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_")
				t1=tt1 + " = aws_key_pair." + tfil + ".id\n"
				common.add_dependancy("aws_key_pair",tt2)
			else:
				tfil=tt2.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_")
				t1=tt1 + " = data.aws_key_pair." + tfil + ".key_name\n"
				common.add_dependancy("aws_key_pair",tt2)

	elif tt1 == "user_data_base64": skip=1
	elif tt1 == "user_data":
		#inid=flag2.split("__")[1]
		client = boto3.client("autoscaling")
		log.debug(str(flag2))
		inid=flag2.split("__")[1]
		resp = client.describe_launch_configurations(LaunchConfigurationNames=[inid])
		if len(resp['LaunchConfigurations']) >1:
			log.warning("WARNING Got >1 launch configuations in fixtf_autoscaling aws_launch_configuration")
		try:
			ud=resp['LaunchConfigurations'][0]['UserData']
			ud2=base64.b64decode(ud).decode('utf-8')

			with open(flag2+'.sh', 'w') as f:
				f.write(str(ud2))
			t1="user_data_base64 = filebase64sha256(\""+flag2+".sh\")\n lifecycle {\n      create_before_destroy = true\n     ignore_changes = [user_data,user_data_base64]\n}\n"
		except KeyError:
			pass

		except Exception as e:
			common.handle_error2(e,str(inspect.currentframe().f_code.co_name),id)


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
	
	All simple AUTOSCALING resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_autoscaling' has no attribute '{name}'")


log.debug(f"AUTOSCALING handlers: 2 custom functions + __getattr__ for 0 simple resources")