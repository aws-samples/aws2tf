import common
import fixtf
import base64
import boto3
import sys
import os
import globals


def aws_docdb_cluster(t1,tt1,tt2,flag1,flag2):
	skip=0
	##if tt1 == "vpc_security_group_ids": t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)
	if tt1 == "cluster_members": t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_docdb_cluster_instance","*",skip)

	if tt1 == "db_subnet_group_name":
			t1=tt1 + " = aws_docdb_subnet_group." + tt2 + ".id\n"
			common.add_dependancy("aws_docdb_subnet_group",tt2)

	elif tt1 == "kms_key_id":
		if tt2 != "null": 
			if tt2 == "AWS_OWNED_KMS_KEY":	skip=1
			#
			else:
				if "arn:" in tt2: tt2=tt2.split("/")[-1]	
				t1=tt1 + " = aws_kms_key.k-" + tt2 + ".arn\n"
				
				common.add_dependancy("aws_kms_key","k-"+tt2)
		else:
			skip=1

	return skip,t1,flag1,flag2

def aws_docdb_cluster_instance(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_docdb_cluster_parameter_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_docdb_cluster_snapshot(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_docdb_event_subscription(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_docdb_global_cluster(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_docdb_subnet_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	## if tt1 == "subnet_ids": t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_subnet","sg-",skip)
	return skip,t1,flag1,flag2

