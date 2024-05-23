def aws_cloudformation_stack(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudformation_stack_set(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="call_as":
		t1=t1+"\n lifecycle {\n   ignore_changes = [call_as,permission_model]\n}\n"
	return skip,t1,flag1,flag2

def aws_cloudformation_stack_set_instance(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudformation_type(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

