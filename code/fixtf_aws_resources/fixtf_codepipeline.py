def aws_codepipeline(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="timeout_in_minutes" and tt2=="0": skip=1
	return skip,t1,flag1,flag2

def aws_codepipeline_custom_action_type(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_codepipeline_webhook(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

