import common
def aws_workspaces_connection_alias(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_workspaces_directory(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_workspaces_ip_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_workspaces_workspace(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="directory_id":
		common.add_dependancy("aws_workspaces_directory",tt2)
		common.add_dependancy("aws_directory_service_directory",tt2)
	return skip,t1,flag1,flag2

