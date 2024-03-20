import common
import fixtf
import base64
import boto3
import sys
import os
import globals

def aws_common(type,t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "security_groups" or tt1 == "security_group_ids" or tt1 == "vpc_security_group_ids":
	# avoid circular references
        if type != "aws_security_group" and type != "aws_cloudwatch_log_group":
            t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)
    elif tt1 == "subnets" or tt1 == "subnet_ids": t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_subnet","subnet-",skip)
    elif tt1 == "route_table_ids": t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_route_table","rtb-",skip)
    #elif tt1 == "cluster_members": fixtf.deref_array(t1,tt1,tt2,type,"*",skip)
    elif tt1 == "iam_roles": t1=fixtf.deref_role_arn_array(t1,tt1,tt2)
    
    elif tt1 == "kms_key_id":
        if type != "aws_docdb_cluster":
            if tt2 != "null": 
                if tt2 == "AWS_OWNED_KMS_KEY":	
                    skip=1
                else:
                    if "arn:" in tt2: tt2=tt2.split("/")[-1]	
                    t1=tt1 + " = aws_kms_key.k-" + tt2 + ".id\n"
                    common.add_dependancy("aws_kms_key","k-"+tt2)
            else:
                skip=1

		
    return skip,t1,flag1,flag2