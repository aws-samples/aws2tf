def aws_amplify_app(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_amplify_backend_environment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_amplify_branch(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="app_id" and tt2 != "null":
		t1 = tt1+" = aws_amplify_app."+tt2+".id\n"
	return skip,t1,flag1,flag2

def aws_amplify_domain_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_amplify_webhook(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

