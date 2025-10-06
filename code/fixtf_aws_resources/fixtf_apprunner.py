import globals
def aws_apprunner_auto_scaling_configuration_version(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_apprunner_connection(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_apprunner_custom_domain_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_apprunner_default_auto_scaling_configuration_version(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_apprunner_observability_configuration(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_apprunner_service(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="auto_scaling_configuration_arn":
		if "autoscalingconfiguration/DefaultConfiguration/1" in tt2: skip=1
	if tt1=="image_identifier":
		print(tt2)
		if tt2.startswith(globals.acc) and globals.region in tt2:
			backend=tt2.split("/")[-1]
			t1=tt1 + " = format(\"%s.dkr.ecr.%s.amazonaws.com/%s\",data.aws_caller_identity.current.account_id,data.aws_region.current.region,\""+backend+"\")\n"
			
	return skip,t1,flag1,flag2

def aws_apprunner_vpc_connector(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_apprunner_vpc_ingress_connection(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

