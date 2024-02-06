import fixtf
import common
import globals

def aws_ecs_cluster(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "kms_key_id":
		##tt2=tt2.strip('\"')
		if tt2 != "null": 
			if tt2 == "AWS_OWNED_KMS_KEY":	
				skip=1
			else:
				t1=tt1 + " = aws_kms_key.k-" + tt2 + ".id\n"
				common.add_dependancy("aws_kms_key",tt2)
		else:
			skip=1

	return skip,t1,flag1,flag2

def aws_ecs_account_setting_default(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ecs_capacity_provider(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ecs_cluster_capacity_providers(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ecs_container_definition(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ecs_service(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "security_groups": t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)
	elif tt1 == "subnets":  t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_subnet","subnet-",skip)
	elif tt1 == "cluster":
		##tt2=tt2.strip('\"')
		if "arn:" in tt2: tt2 = tt2.split("/")[-1]
			
		if tt2 != "null": 
			t1=tt1 + " = aws_ecs_cluster." + tt2 + ".id\n"
			common.add_dependancy("aws_ecs_cluster",tt2)
		else:
			skip=1
	elif tt1 == "task_definition":
		##tt2=tt2.strip('\"')
		if "arn:" in tt2: 	
			tt2 = tt2.split("/")[-1]
			t1=tt1 + " = aws_ecs_task_definition." + tt2 + ".arn\n"
			common.add_dependancy("aws_ecs_task_definition",tt2)
		else:
			tdarn="arn:aws:ecs:"+globals.region+":"+globals.acc+":"+"task-definition:"+tt2
			common.add_dependancy("aws_ecs_task_definition",tdarn)


	return skip,t1,flag1,flag2

def aws_ecs_tag(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ecs_task_definition(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "execution_role_arn" or tt1 == "task_role_arn":
		##tt2=tt2.strip('\"')
		if tt2 != "null":
			if ":" in tt2: tt2=tt2.split("/")[-1]
			t1=tt1 + " = aws_iam_role." + tt2 + ".arn\n"
			common.add_dependancy("aws_iam_role",tt2)
	return skip,t1,flag1,flag2

def aws_ecs_task_execution(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ecs_task_set(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

