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