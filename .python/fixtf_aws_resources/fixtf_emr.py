import common
import fixtf
import base64
import boto3
import sys
import os
import globals
import inspect


def aws_emr_block_public_access_configuration(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_emr_cluster(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="kdc_admin_password":
		if tt2.startswith("null"):
			t1=tt1+" = \"CHANGE_ME\"\n"
	elif tt1=="applications":
		t1=t1+"\n lifecycle {\n   ignore_changes = [kerberos_attributes[0].kdc_admin_password]\n}\n"
		globals.emrsubnetid=False
	elif tt1=="subnet_id":
		if "subnet" in tt2: globals.emrsubnetid=True
	elif tt1=="subnet_ids":
		if globals.emrsubnetid: skip=1
	elif tt1=="security_configuration" and tt2!="null":
		t1=tt1+" = aws_emr_security_configuration."+tt2+".name\n"
		common.add_dependancy("aws_emr_security_configuration", tt2)

		
	return skip,t1,flag1,flag2

def aws_emr_instance_fleet(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_emr_instance_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_emr_managed_scaling_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_emr_release_labels(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_emr_security_configuration(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="configuration":
		t1=t1+"\n lifecycle {\n   ignore_changes = [configuration]\n}\n"
	return skip,t1,flag1,flag2

def aws_emr_studio(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_emr_studio_session_mapping(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_emr_supported_instance_types(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

