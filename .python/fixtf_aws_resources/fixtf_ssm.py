import common
import fixtf
import base64
import boto3
import sys
import os
import globals

def aws_ssm_activation(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ssm_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ssm_default_patch_baseline(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ssm_document(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ssm_instances(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ssm_maintenance_window(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ssm_maintenance_window_target(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ssm_maintenance_window_task(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ssm_maintenance_windows(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ssm_parameter(t1,tt1,tt2,flag1,flag2):
	skip=0
	print(str(tt1) + " " + str(tt2))
	if tt1 == "arn": globals.ssmparamn=tt2 
	elif tt1 == "value":
		if globals.ssmparamn != "":
			client = boto3.client("ssm")
			response = client.get_parameter(Name=globals.ssmparamn, WithDecryption=True)
			vs=response["Parameter"]["Value"]
			if vs.startswith('{"'):
				t1 = tt1 + " = jsonencode("+vs+")\n"
			else:
				t1 = tt1 + " = \"" + vs + "\"\n"
			globals.ssmparamn=""
	elif tt1 == "insecure_value": 
		t1 ="lifecycle {\n" + "   ignore_changes = [value]\n" +  "}\n"
		
	return skip,t1,flag1,flag2

def aws_ssm_parameters_by_path(t1,tt1,tt2,flag1,flag2):
	skip=0
	client = boto3.client("ssm")
	return skip,t1,flag1,flag2

def aws_ssm_patch_baseline(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ssm_patch_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ssm_resource_data_sync(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ssm_service_setting(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

