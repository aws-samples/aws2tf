import common
import fixtf
import base64
import boto3
import sys
import os
import context


def aws_sagemaker_app(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="domain_id" and tt2!="null":
		t1=tt1+" = aws_sagemaker_domain."+tt2+".id\n"
		common.add_dependancy("aws_sagemaker_domain",tt2)
	return skip,t1,flag1,flag2

def aws_sagemaker_app_image_config(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sagemaker_code_repository(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sagemaker_data_quality_job_definition(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sagemaker_device(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sagemaker_device_fleet(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sagemaker_domain(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="tag_propagation" and tt2=="null":	
		t1=tt1 + " = \"DISABLED\"\n"
		t1=t1+"\n lifecycle {\n   ignore_changes = [tag_propagation]\n}\n"
	return skip,t1,flag1,flag2

def aws_sagemaker_endpoint(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sagemaker_endpoint_configuration(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sagemaker_feature_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sagemaker_flow_definition(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sagemaker_human_task_ui(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sagemaker_image(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sagemaker_image_version(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sagemaker_model(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sagemaker_model_package_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sagemaker_model_package_group_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sagemaker_monitoring_schedule(t1,tt1,tt2,flag1,flag2):
	skip=0
	
	return skip,t1,flag1,flag2

def aws_sagemaker_notebook_instance(t1,tt1,tt2,flag1,flag2):
	skip=0
	#if tt1 == "security_groups": 
	#	print("********",str(tt2))
		#t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)

	return skip,t1,flag1,flag2

def aws_sagemaker_notebook_instance_lifecycle_configuration(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sagemaker_pipeline(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sagemaker_prebuilt_ecr_image(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sagemaker_project(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sagemaker_servicecatalog_portfolio_status(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sagemaker_space(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sagemaker_studio_lifecycle_config(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sagemaker_user_profile(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="domain_id" and tt2!="null":
		t1=tt1+" = aws_sagemaker_domain."+tt2+".id\n"
		common.add_dependancy("aws_sagemaker_domain",tt2)
	return skip,t1,flag1,flag2

def aws_sagemaker_workforce(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sagemaker_workteam(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

