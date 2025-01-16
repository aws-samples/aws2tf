def aws_neptune_cluster(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="engine":
		t1 = tt1 + " = \"neptune\"\n"
		t1 = t1  + "\n lifecycle {\n   ignore_changes = [engine,serverless_v2_scaling_configuration[0].min_capacity]\n}\n"
	if tt1=="min_capacity" and tt2=="0.5": 
		t1 = tt1 + " = \"1.0\"\n"
	return skip,t1,flag1,flag2

def aws_neptune_cluster_endpoint(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_neptune_cluster_instance(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_neptune_cluster_parameter_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="name":
		if tt2.startswith("default."):
			tt2=tt2.split(".")[1]
			t1 = tt1 + " = \""+tt2+"\"\n"
			t1 =t1  +"\n lifecycle {\n   ignore_changes = [name]\n}\n"
	return skip,t1,flag1,flag2

def aws_neptune_cluster_snapshot(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_neptune_engine_version(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_neptune_event_subscription(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_neptune_global_cluster(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_neptune_orderable_db_instance(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_neptune_parameter_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="name":
		if tt2.startswith("default."):
			tt2=tt2.split(".")[1]
			t1 = tt1 + " = \""+tt2+"\"\n"
			t1 =t1  +"\n lifecycle {\n   ignore_changes = [name]\n}\n"
	return skip,t1,flag1,flag2

def aws_neptune_subnet_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

