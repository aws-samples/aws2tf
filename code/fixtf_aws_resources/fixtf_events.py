def aws_cloudwatch_event_rule(t1,tt1,tt2,flag1,flag2):
	skip=0
	if "name_prefix" in tt1: skip=1

	return skip,t1,flag1,flag2

def aws_cloudwatch_event_api_destination(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudwatch_event_archive(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudwatch_event_bus(t1,tt1,tt2,flag1,flag2):
	skip=0
	
	return skip,t1,flag1,flag2

def aws_cloudwatch_event_bus_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudwatch_event_connection(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudwatch_event_endpoint(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudwatch_event_permission(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudwatch_event_source(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudwatch_event_target(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "arn":
		t1=t1+"\nlifecycle {\n" + "   ignore_changes = [input_transformer]\n" +  "}\n"
	return skip,t1,flag1,flag2