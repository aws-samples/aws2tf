import common

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
	if tt1=="topic_arn":
		#tn=tt2.replace(":","_")
		#t1=tt1 + " = aws_sns_topic." + tn + ".arn\n"
		t1=t1+"\n lifecycle {\n   ignore_changes = [confirmation_timeout_in_minutes,endpoint_auto_confirms]\n}\n"
		common.add_dependancy("aws_sns_topic",tt2)


	return skip,t1,flag1,flag2

