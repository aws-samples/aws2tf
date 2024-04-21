def aws_codebuild_project(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="concurrent_build_limit" and tt2 != "null":
		if tt2=="0": skip=1
	return skip,t1,flag1,flag2

def aws_codebuild_report_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_codebuild_resource_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_codebuild_source_credential(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_codebuild_webhook(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

