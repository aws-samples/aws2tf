def aws_config_aggregate_authorization(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_config_config_rule(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_config_configuration_aggregator(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_config_configuration_recorder(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_config_configuration_recorder_status(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_config_conformance_pack(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_config_delivery_channel(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="s3_bucket_name":
		#print("---t1->>>>", t1)
		#print("---tt2->>>>", tt2)
		t1=tt1+" = \""+tt2+"\"\n"
			
	return skip,t1,flag1,flag2

def aws_config_organization_conformance_pack(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_config_organization_custom_policy_rule(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_config_organization_custom_rule(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_config_organization_managed_rule(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_config_remediation_configuration(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

