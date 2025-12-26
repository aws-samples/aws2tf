import common
import fixtf
import logging
log = logging.getLogger('aws2tf')
import base64
import boto3
import sys
import os
import context
import inspect
import json

def aws_proxy_protocol_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_wafv2_ip_set(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_wafv2_regex_pattern_set(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_wafv2_rule_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_wafv2_web_acl(t1,tt1,tt2,flag1,flag2):
	skip=0
	if "resource" in t1 and "{" in t1 and "aws_wafv2_web_acl" in t1:
		wid=t1.split('"')[3]
		aclid=wid.split("_")[0].split("w-")[1]
		aclnm=wid.split("_")[1]
		aclsc=wid.split("_")[2]
		#print("web acl:",aclid,aclnm,aclsc)
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
				log.warning("empty rule %s %s %s", context.waf2nm, context.waf2sc, context.waf2id)
		except Exception as e:
			log.error("Error in get_web_acl %s", e)
			os._exit(1)


	return skip,t1,flag1,flag2

def aws_wafv2_web_acl_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_wafv2_web_acl_logging_configuration(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

