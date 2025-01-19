import fixtf
import common
import globals

def aws_ecs_cluster(t1,tt1,tt2,flag1,flag2):
	skip=0

	if tt1 == "namespace":
		if "arn:" in tt2: t1=fixtf.globals_replace(t1,tt1,tt2)
			


	return skip,t1,flag1,flag2

def aws_ecs_account_setting_default(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ecs_capacity_provider(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="auto_scaling_group_arn" and tt2.startswith("arn:aws:autoscaling:"):
		common.add_dependancy("aws_autoscaling_group", tt2)
	return skip,t1,flag1,flag2

def aws_ecs_cluster_capacity_providers(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="cluster_name":
		t1=tt1+" = aws_ecs_cluster."+tt2+".name\n"
		common.add_dependancy("aws_ecs_cluster", tt2)
	return skip,t1,flag1,flag2

def aws_ecs_container_definition(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ecs_service(t1,tt1,tt2,flag1,flag2):
	skip=0
	##if tt1 == "security_groups": t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)
	##if tt1 == "subnets":  t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_subnet","subnet-",skip)
	if tt1 == "cluster":
		
		if "arn:" in tt2: tt2 = tt2.split("/")[-1]
			
		if tt2 != "null": 
			t1=tt1 + " = aws_ecs_cluster." + tt2 + ".id\n"
			common.add_dependancy("aws_ecs_cluster",tt2)
		else:
			skip=1
	elif tt1 == "task_definition":
		#print("--->>>>"+tt2)
		
		if "arn:" in tt2: 	
			tt2 = tt2.split("/")[-1]
			t1=tt1 + " = aws_ecs_task_definition." + tt2 + ".arn\n"
			common.add_dependancy("aws_ecs_task_definition",tt2)
		else:
			tdarn="arn:aws:ecs:"+globals.region+":"+globals.acc+":"+"task-definition:"+tt2
			#print("--->>>>"+tt2,tdarn)
			#tdn=tdarn.replace("/","_").replace(".","_").replace(":","_")
			#t1=tt1+" = aws_ecs_task_definition."+tdn+".id\n"
			common.add_dependancy("aws_ecs_task_definition",tdarn)

	return skip,t1,flag1,flag2

def aws_ecs_tag(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ecs_task_definition(t1,tt1,tt2,flag1,flag2):
	skip=0
	
	if tt1=="awslogs-group" and tt2 !="null":
		# fixup cw log name
		lgn=tt2.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_")
		t1=tt1 + " = aws_cloudwatch_log_group." + lgn + ".id\n"
		common.add_dependancy("aws_cloudwatch_log_group", tt2) 
	return skip,t1,flag1,flag2

def aws_ecs_task_execution(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_ecs_task_set(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

