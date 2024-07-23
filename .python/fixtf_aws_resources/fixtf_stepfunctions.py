def aws_sfn_activity(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sfn_alias(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_sfn_state_machine(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="definition":
				t1="\n lifecycle {\n   ignore_changes = [definition]\n}\n" + t1
	return skip,t1,flag1,flag2

def aws_sfn_state_machine_versions(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

