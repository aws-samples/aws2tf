import common

def aws_dms_certificate(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_dms_endpoint(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="endpoint_id":
		t1 = t1 + "\nlifecycle {\n" + "   ignore_changes = [s3_settings,postgres_settings[0].max_file_size]\n" +  "}\n"
	if tt1=="max_file_size" and tt2=="0": 
		t1=tt1+" = 1048576\n"
	
	return skip,t1,flag1,flag2

def aws_dms_event_subscription(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_dms_replication_config(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_dms_replication_instance(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="replication_subnet_group_id" and tt2 != "null":
		t1=tt1 + " = aws_dms_replication_subnet_group." + tt2 + ".id\n"
		common.add_dependancy("aws_dms_replication_subnet_group",tt2)
	return skip,t1,flag1,flag2

def aws_dms_replication_subnet_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_dms_replication_task(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="CloudWatchLogGroup": skip=1
	if tt1=="CloudWatchLogStream": skip=1

	return skip,t1,flag1,flag2

def aws_dms_s3_endpoint(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

