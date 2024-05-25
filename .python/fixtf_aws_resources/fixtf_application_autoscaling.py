import fixtf
import common

def aws_appautoscaling_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_appautoscaling_scheduled_action(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_appautoscaling_target(t1,tt1,tt2,flag1,flag2):
	skip=0
	#if tt1 == "role_arn": 
#		if ":role/aws-service-role" in tt2:
#			t1=fixtf.globals_replace(t1,tt1,tt2)
#		else:
#			if tt2 != "null":
#				if ":" in tt2: tt2=tt2.split("/")[-1]
#				t1=tt1 + " = aws_iam_role." + tt2 + ".arn\n"
#				common.add_dependancy("aws_iam_role",tt2)
	return skip,t1,flag1,flag2

