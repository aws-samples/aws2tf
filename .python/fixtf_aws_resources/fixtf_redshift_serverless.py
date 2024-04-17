import common
import fixtf
import sys
import os
import inspect

def aws_redshiftserverless_namespace(t1,tt1,tt2,flag1,flag2):
    try:
        skip=0


        if tt1 == "default_iam_role_arn":  t1=fixtf.deref_role_arn(t1,tt1,tt2)

        ##elif tt1 == "iam_roles":  t1=fixtf.deref_role_arn_array(t1,tt1,tt2)

    except Exception as e:
        common.handle_error2(e,str(inspect.currentframe().f_code.co_name),id)    
    
    return skip,t1,flag1,flag2 


def aws_redshiftserverless_workgroup(t1,tt1,tt2,flag1,flag2):
    skip=0
    ##if tt1 == "subnet_ids":  t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_subnet","subnet-",skip)
    ##elif tt1 == "security_group_ids": t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)
    if tt1 == "namespace_name": 
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_redshiftserverless_namespace." + tt2 + ".id\n"
        common.add_dependancy("aws_redshiftserverless_namespace",tt2)

    return skip,t1,flag1,flag2



def aws_redshiftserverless_credentials(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_redshiftserverless_endpoint_access(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_redshiftserverless_resource_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_redshiftserverless_snapshot(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_redshiftserverless_usage_limit(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

