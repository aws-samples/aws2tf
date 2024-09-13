import common
import globals

def aws_connect_bot_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_connect_contact_flow(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="instance_id":
		t1=tt1+" = aws_connect_instance.r-"+tt2+".id\n"
		common.add_dependancy("aws_connect_instance",tt2)
	return skip,t1,flag1,flag2

def aws_connect_contact_flow_module(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_connect_hours_of_operation(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="instance_id":
		t1=tt1+" = aws_connect_instance.r-"+tt2+".id\n"
		globals.connectinid=tt2
		common.add_dependancy("aws_connect_instance",tt2)
	return skip,t1,flag1,flag2

def aws_connect_instance(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_connect_instance_storage_config(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="instance_id":
		t1=tt1+" = aws_connect_instance.r-"+tt2+".id\n"
		common.add_dependancy("aws_connect_instance",tt2)

	return skip,t1,flag1,flag2

def aws_connect_lambda_function_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_connect_phone_number(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="target_arn" and tt2.startswith("arn:aws:connect:"):
		cid=tt2.split("/")[1]
		t1=tt1+" = aws_connect_instance.r-"+cid+".arn\n"
	return skip,t1,flag1,flag2

def aws_connect_queue(t1,tt1,tt2,flag1,flag2):
	skip=0
	if "resource" in t1 and "{" in t1 and "aws_connect_queue" in t1:
		inid=t1.split('"r-')[1].split("_")[0]
		globals.connectinid=inid


	if tt1=="instance_id":
		t1=tt1+" = aws_connect_instance.r-"+tt2+".id\n"
		globals.connectinid=tt2
		common.add_dependancy("aws_connect_instance",tt2)
	elif tt1=="hours_of_operation_id":
		t1=tt1+" = aws_connect_hours_of_operation.r-"+globals.connectinid+"_"+tt2+".hours_of_operation_id\n"
	return skip,t1,flag1,flag2

def aws_connect_quick_connect(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_connect_routing_profile(t1,tt1,tt2,flag1,flag2):
	skip=0
	if "resource" in t1 and "{" in t1 and "aws_connect_routing_profile" in t1:
		inid=t1.split('"r-')[1].split("_")[0]
		globals.connectinid=inid
	elif tt1=="name":
		t1=t1+"\n lifecycle {\n   ignore_changes = [media_concurrencies]\n}\n"
	elif tt1=="concurrency" and tt2=="0": 
		t1=tt1+" = 1\n"
	elif tt1=="instance_id":
		t1=tt1+" = aws_connect_instance.r-"+tt2+".id\n"
		globals.connectinid=tt2
		common.add_dependancy("aws_connect_instance",tt2)
	elif tt1=="queue_id" or tt1=="default_outbound_queue_id":
		t1=tt1+" = aws_connect_queue.r-"+globals.connectinid+"_"+tt2+".queue_id\n"
	return skip,t1,flag1,flag2

def aws_connect_security_profile(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="instance_id":
		t1=tt1+" = aws_connect_instance.r-"+tt2+".id\n"
		common.add_dependancy("aws_connect_instance",tt2)	
	return skip,t1,flag1,flag2

def aws_connect_user(t1,tt1,tt2,flag1,flag2):
	skip=0
	if "resource" in t1 and "{" in t1 and "aws_connect_user" in t1:
		inid=t1.split('"r-')[1].split("_")[0]
		globals.connectinid=inid
	if tt1=="instance_id":
		t1=tt1+" = aws_connect_instance.r-"+tt2+".id\n"
		common.add_dependancy("aws_connect_instance",tt2)
		globals.connectinid=tt2
	elif tt1=="routing_profile_id":
		t1=tt1+" = aws_connect_routing_profile.r-"+globals.connectinid+"_"+tt2+".routing_profile_id\n"
	elif tt1=="security_profile_ids":
		if "," not in tt2:
			secid=tt2.lstrip('[').rstrip(']').strip('"')
			t1=tt1+" = [aws_connect_security_profile.r-"+globals.connectinid+"_"+secid+".security_profile_id]\n"
			
	return skip,t1,flag1,flag2

def aws_connect_user_hierarchy_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_connect_user_hierarchy_structure(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_connect_vocabulary(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

