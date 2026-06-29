"""
IAM Resource Handlers - Optimized with __getattr__

This file contains ONLY IAM resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 8 functions
Optimized: 8 functions + __getattr__
Reduction: 0% less code
"""

import logging
import common
import fixtf
import context
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# IAM Resources with Custom Logic (8 functions)
# ============================================================================

def aws_iam_access_key(t1,tt1,tt2,flag1,flag2):


    skip=0
    if tt1 == "user":
        pkey="aws_iam_access_key."+tt2
        context.rproc[pkey]=True
        t1=tt1+" = aws_iam_user."+tt2+".id\n"
    return skip,t1,flag1,flag2



def aws_iam_group_membership(t1,tt1,tt2,flag1,flag2):


    skip=0
    if tt1=="user" and tt2 !="null":
        t1=tt1+" = aws_iam_user."+tt2+".id\n"
        common.add_dependancy("aws_iam_user", tt2)
		
    return skip,t1,flag1,flag2



def aws_iam_group_policy(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="group" and tt2 !="null":
		t1=tt1+" = aws_iam_group."+tt2+".id\n"
	return skip,t1,flag1,flag2



def aws_iam_openid_connect_provider(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="url":
		t1=tt1+" = \"https://"+tt2+"\"\n"
	return skip,t1,flag1,flag2



def aws_iam_policy(t1,tt1,tt2,flag1,flag2):


    skip=0
    if tt1 == "name":
        
        if len(tt2) > 0: flag1=True
    if tt1 == "name_prefix" and flag1 is True: skip=1
    if tt1 == "policy": t1=fixtf.globals_replace(t1,tt1,tt2)
  
    return skip,t1,flag1,flag2


def aws_iam_role(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "name":
		if len(tt2) > 0: 
			flag1=True
			flag2=tt2
	elif tt1 == "name_prefix" and flag1 is True: skip=1
	elif tt1 == "policy": t1=fixtf.globals_replace(t1,tt1,tt2)
	elif tt1 == "assume_role_policy": t1=fixtf.globals_replace(t1,tt1,tt2)
	elif tt1 == "permissions_boundary" and tt2 != "null":
		if "arn:aws:iam::aws:policy" not in tt2:
			pn=tt2.split("/")[-1]
			common.add_dependancy("aws_iam_policy",tt2)
			t1=tt1+" = aws_iam_policy."+pn+".arn\n"
	elif tt1 == "managed_policy_arns":   
		if tt2 == "[]": 
			skip=1
		elif ":"+context.acc+":" in tt2:
			fs=""
			ends=",data.aws_caller_identity.current.account_id"
			tt2=tt2.replace("[","").replace("]","")
			cc=tt2.count(",")
			pt1=tt1+" = ["
			for j in range(0,cc+1):
				ps=tt2.split(",")[j]
				if ":"+context.acc+":" in ps:
					a1=ps.find(":"+context.acc+":")
					ps=ps[:a1]+":%s:"+ps[a1+14:]
					ps = 'format('+ps+ends+')'
				pt1=pt1+ps+","
			pt1=pt1+"]\n"
			t1=pt1.replace(",]","]")
			context.roles=context.roles+[flag2]
		else:
			pass
	return skip,t1,flag1,flag2


def aws_iam_role_policy(t1,tt1,tt2,flag1,flag2):


    skip=0
    if tt1 == "name_prefix" and flag1 is True: skip=1
    
    #if tt1 == "name_prefix":  skip=1
    if tt1 == "name":
        if len(tt2) > 0: 
            flag1=True
            flag2=tt2


  
    return skip,t1,flag1,flag2



def aws_iam_role_policy_attachment(t1,tt1,tt2,flag1,flag2):


    skip=0

    if tt1 == "policy_arn": t1=fixtf.globals_replace(t1,tt1,tt2)


    return skip,t1,flag1,flag2



def aws_iam_user_group_membership(t1,tt1,tt2,flag1,flag2):


    skip=0
    if tt1 == "user":
        t1=tt1+" = aws_iam_user."+tt2+".id\n"
        common.add_dependancy("aws_iam_user", tt2)
    elif tt1 == "groups":
        t1,skip = fixtf.deref_array(t1, tt1, tt2, "aws_iam_group", "", skip)

    elif tt1 == "groups":
        t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_iam_group","",skip)
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
	
	All simple IAM resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_iam' has no attribute '{name}'")


log.debug(f"IAM handlers: 8 custom functions + __getattr__ for 0 simple resources")