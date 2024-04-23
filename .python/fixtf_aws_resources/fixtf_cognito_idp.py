import common
import fixtf

def aws_cognito_identity_provider(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cognito_managed_user_pool_client(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cognito_resource_server(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cognito_risk_configuration(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cognito_user(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cognito_user_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "user_pool_id" and tt2 != "null":
		t1=tt1+" = aws_cognito_user_pool."+tt2+".id\n"
		common.add_dependancy("aws_cognito_user_pool",tt2)
	return skip,t1,flag1,flag2

def aws_cognito_user_in_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cognito_user_pool(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="email_verification_message" or tt1=="email_verification_subject" or tt1=="sms_authentication_message" or tt1=="sms_verification_message": 
		skip=1
	return skip,t1,flag1,flag2

def aws_cognito_user_pool_client(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="access_token_validity":
		if tt2=="0":
			t1=tt1+" = 1\n" + "\nlifecycle {\n" + "   ignore_changes = [access_token_validity]\n" +  "}\n"

	elif tt1 == "user_pool_id" and tt2 != "null":
		t1=tt1+" = aws_cognito_user_pool."+tt2+".id\n"
		common.add_dependancy("aws_cognito_user_pool",tt2)
	
	elif tt1=="access_token":
		if tt2=="null":
			t1=tt1+" = \"hours\"\n"
	elif tt1=="refresh_token":
		if tt2=="null":
			t1=tt1+" = \"days\"\n"
	
	return skip,t1,flag1,flag2

def aws_cognito_user_pool_domain(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cognito_user_pool_ui_customization(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

