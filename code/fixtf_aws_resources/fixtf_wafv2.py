"""
WAFV2 Resource Handlers - Optimized with __getattr__

This file contains ONLY WAFV2 resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 1 functions
Optimized: 1 functions + __getattr__
Reduction: 0% less code
"""

import common
import fixtf
import logging
import base64
import boto3
import sys
import os
import context
import inspect
import json
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# WAFV2 Resources with Custom Logic (1 functions)
# ============================================================================

def aws_wafv2_web_acl(t1,tt1,tt2,flag1,flag2):


	skip=0
	if "resource" in t1 and "{" in t1 and "aws_wafv2_web_acl" in t1:
		wid=t1.split('"')[3]
		aclid=wid.split("_")[0].split("w-")[1]
		aclnm=wid.split("_")[1]
		aclsc=wid.split("_")[2]
		context.waf2id=aclid
		context.waf2nm=aclnm
		context.waf2sc=aclsc
		#t1=t1+"\n lifecycle {\n   ignore_changes = [rule]\n}\n"

	if tt1=="rule_json" and tt2=="null":
		# call get_web_acl
		try:
			client=boto3.client("wafv2")
			response = client.get_web_acl(Id=context.waf2id,Name=context.waf2nm,Scope=context.waf2sc)
			rules=response['WebACL']['Rules']
			if rules != []:
				fn='w-'+context.waf2id+'_'+context.waf2nm+'_'+context.waf2sc+'.webacl'
				if os.path.exists(fn):os.remove(fn)
				with open(fn, 'w') as f: json.dump(rules, f, indent=2, default=str)
				t1 = tt1 + ' = file("'+fn+'")\n'
				t1=t1+"\n lifecycle {\n   ignore_changes = [rule_json,rule]\n}\n"
			else:
				log.debug("empty rule %s %s %s", context.waf2nm, context.waf2sc, context.waf2id)
		except Exception as e:
			log.error("Error in get_web_acl %s", e)
			sys.exit(1)


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
	
	All simple WAFV2 resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_wafv2' has no attribute '{name}'")


log.debug(f"WAFV2 handlers: 1 custom functions + __getattr__ for 0 simple resources")