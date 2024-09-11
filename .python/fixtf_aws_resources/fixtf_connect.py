import common

def aws_connect_bot_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_connect_contact_flow(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_connect_contact_flow_module(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_connect_hours_of_operation(t1,tt1,tt2,flag1,flag2):
	skip=0
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
	return skip,t1,flag1,flag2

def aws_connect_quick_connect(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_connect_routing_profile(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_connect_security_profile(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_connect_user(t1,tt1,tt2,flag1,flag2):
	skip=0
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

