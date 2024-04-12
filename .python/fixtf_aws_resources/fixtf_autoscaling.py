import globals
import common
import fixtf
import base64
import boto3
import sys
import os


def aws_autoscaling_attachment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_autoscaling_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="name":
		t1=t1+"\n lifecycle {\n   ignore_changes = [force_delete,force_delete_warm_pool,ignore_failed_scaling_activities,wait_for_capacity_timeout]\n}\n"
	elif tt1 == "load_balancers" and tt2 == "[]": skip=1
	elif tt1 == "target_group_arns": skip=1
	elif tt1 == "availability_zones":
		if len(tt2) > 4: globals.asg_azs=True
	elif tt1 == "vpc_zone_identifier":
		if globals.asg_azs: skip=1

	elif tt1 == "force_delete" or tt1=="force_delete_warm_pool" or tt1=="ignore_failed_scaling_activities":
		if tt2=="null":
			t1 = tt1 +" = false\n"
   			

	elif tt1=="wait_for_capacity_timeout":
		if tt2=="null":
			t1 = tt1 +" = \"10m\"\n"
	

	return skip,t1,flag1,flag2

def aws_autoscaling_group_tag(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_autoscaling_lifecycle_hook(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_autoscaling_notification(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_autoscaling_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_autoscaling_schedule(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_autoscaling_traffic_source_attachment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2


def aws_launch_configuration(t1,tt1,tt2,flag1,flag2):
	skip=0

	if tt1 == "id":
			flag2=tt2

	elif tt1 == "iam_instance_profile":
		if tt2 != "null":
			t1 = tt1 + " = aws_iam_instance_profile."+tt2+".id\n"
			common.add_dependancy("aws_iam_instance_profile",tt2)

	elif tt1 == "key_name": 
		if tt2 != "null":
			t1=tt1 + " = aws_key_pair." + tt2 + ".id\n"
			common.add_dependancy("aws_key_pair",tt2)

	elif tt1 == "user_data_base64": skip=1
	elif tt1 == "user_data":
		#inid=flag2.split("__")[1]
		client = boto3.client("autoscaling")
		print(str(flag2))
		inid=flag2.split("__")[1]
		resp = client.describe_launch_configurations(LaunchConfigurationNames=[inid])
		if len(resp['LaunchConfigurations']) >1:
			print("WARNING Got >1 launch configuations in fixtf_autoscaling aws_launch_configuration")
		try:
			ud=resp['LaunchConfigurations'][0]['UserData']
			ud2=base64.b64decode(ud).decode('utf-8')

			with open(flag2+'.sh', 'w') as f:
				f.write(str(ud2))
			t1="user_data_base64 = filebase64sha256(\""+flag2+".sh\")\n lifecycle {\n      create_before_destroy = true\n     ignore_changes = [user_data,user_data_base64]\n}\n"
		except KeyError:
			pass

		except Exception as e:
			print(f"{e=}")
			print("ERROR: -1-> fixtf-autoscaling aws_launch_configuration")
			exc_type, exc_obj, exc_tb = sys.exc_info()
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			print(exc_type, fname, exc_tb.tb_lineno)
			exit()


	return skip,t1,flag1,flag2


