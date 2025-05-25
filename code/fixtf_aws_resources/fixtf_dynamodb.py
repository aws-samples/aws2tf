def aws_dynamodb_contributor_insights(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_dynamodb_global_table(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_dynamodb_kinesis_streaming_destination(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="table_name" and tt2!="null":
		t1 =tt1+" = aws_dynamodb_table."+tt2+".name\n"
	return skip,t1,flag1,flag2

def aws_dynamodb_table(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="recovery_period_in_days" and tt2=="0":
		skip=1
	return skip,t1,flag1,flag2

def aws_dynamodb_table_item(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_dynamodb_table_replica(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_dynamodb_tag(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

