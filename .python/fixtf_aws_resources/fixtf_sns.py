def aws_sns_platform_application(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sns_sms_preferences(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sns_topic(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "signature_version":
		if tt2 == "0": skip=1 
	return skip,t1,flag1,flag2

def aws_sns_topic_data_protection_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sns_topic_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sns_topic_subscription(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

