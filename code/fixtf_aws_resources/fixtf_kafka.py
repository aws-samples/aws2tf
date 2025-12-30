"""
KAFKA Resource Handlers - Optimized with __getattr__

This file contains ONLY KAFKA resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 2 functions
Optimized: 2 functions + __getattr__
Reduction: 0% less code
"""

import logging
import common
import context
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# KAFKA Resources with Custom Logic (2 functions)
# ============================================================================

def aws_msk_cluster(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="log_group" and tt2!="null":
		lgn=tt2.replace("/", "_").replace(".", "_").replace(":", "_").replace("|", "_").replace("$", "_").replace(", ", "_").replace("&", "_").replace("#", "_").replace("[", "_").replace("]", "_").replace("=", "_").replace("!", "_").replace(";", "_")
		t1=tt1+" = aws_cloudwatch_log_group."+lgn+".name\n"
		common.add_dependancy("aws_cloudwatch_log_group",tt2)
	elif tt1=="delivery_stream" and tt2!="null":
		karn="arn:aws:firehose:"+context.region+":"+context.acc+":deliverystream/"+tt2
		tarn=karn.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_")
		t1=tt1+" = aws_kinesis_firehose_delivery_stream."+tarn+".name\n"
		common.add_dependancy("aws_kinesis_firehose_delivery_stream",tt2)
	elif tt1=="arn" and tt2.startswith("arn:aws:kafka") and ":configuration:" in tt2:
		tarn=tt2.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_")
		t1=tt1+" = aws_msk_configuration."+tarn+".arn\n"
		# pass the arn
		common.add_dependancy("aws_msk_configuration", tt2)
	elif tt1=="volume_throughput" and tt2=="0": skip=1
	elif tt1=="cluster_name":
		t1=t1+ "\nlifecycle {\n" + "   ignore_changes = [configuration_info]\n" +  "}\n"

	#elif tt1=="arn" and tt2!="null":
	#	t1=tt1+" = aws_msk_configuration."+tarn+".arn\n"



		
	return skip,t1,flag1,flag2



def aws_msk_scram_secret_association(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="cluster_arn":
		tarn=tt2.replace("/", "_").replace(".", "_").replace(":", "_").replace("|", "_").replace("$", "_").replace(", ", "_").replace("&", "_").replace("#", "_").replace("[", "_").replace("]", "_").replace("=", "_").replace("!", "_").replace(";", "_")
		t1=tt1+" = aws_msk_cluster."+tarn+".arn\n"
		#common.add_dependancy("aws_msk_cluster", tt2)
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
	
	All simple KAFKA resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_kafka' has no attribute '{name}'")


log.debug(f"KAFKA handlers: 2 custom functions + __getattr__ for 0 simple resources")