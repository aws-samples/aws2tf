import common
import fixtf
import base64
import boto3
import sys
import os
import context

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
	if tt1=="content":
		t1="\n lifecycle {\n   ignore_changes = [content]\n}\n"+t1
	return skip,t1,flag1,flag2

def aws_ssm_instances(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ssm_maintenance_window(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="schedule_offset" and tt2=="0": 
		t1="lifecycle {\n   ignore_changes = [schedule_offset]\n}\n"
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
	if tt1 == "arn": 
		context.ssmparamn=tt2
		skip=1 
	elif tt1 == "value":
		if context.ssmparamn != "":
			client = boto3.client("ssm")
			response = client.get_parameter(Name=context.ssmparamn, WithDecryption=True)
			vs=response["Parameter"]["Value"]
			ml=len(vs.split('\n'))
			if ml > 1:
				vs=vs.replace('\n','').replace('${','$${').replace('\t','')
			if vs.startswith('{"') or vs.startswith('["') :
				t1 = tt1 + " = jsonencode("+vs+")\n"
			else:
				t1 = tt1 + " = \"" + vs + "\"\n"
			context.ssmparamn=""	
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

