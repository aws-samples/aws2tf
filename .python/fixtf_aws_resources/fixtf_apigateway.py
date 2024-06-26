import fixtf
import common
import globals


def aws_api_gateway_account(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_api_gateway_api_key(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_api_gateway_authorizer(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_api_gateway_base_path_mapping(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_api_gateway_client_certificate(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_api_gateway_deployment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_api_gateway_documentation_part(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_api_gateway_documentation_version(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_api_gateway_domain_name(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_api_gateway_gateway_response(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_api_gateway_integration(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_api_gateway_integration_response(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_api_gateway_method(t1,tt1,tt2,flag1,flag2):
	skip=0
	if t1.startswith("resource"):
		globals.apigwrestapiid=t1.split("r-")[1].split("_")[0]
	if tt1=="resource_id" and tt2 != "null":
		t1=tt1 + " = aws_api_gateway_resource.r-" + str(globals.apigwrestapiid)+"_" + tt2 + ".id\n"
	if tt1=="authorizer_id" and tt2 != "null":
		t1=tt1 + " = aws_api_gateway_authorizer.r-" + str(globals.apigwrestapiid)+"_" + tt2 + ".id\n"
	return skip,t1,flag1,flag2

def aws_api_gateway_method_response(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_api_gateway_method_settings(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_api_gateway_model(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_api_gateway_request_validator(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_api_gateway_resource(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_api_gateway_rest_api(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "vpc_endpoint_ids":
		if tt2=="[]": skip=1
	return skip,t1,flag1,flag2

def aws_api_gateway_rest_api_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_api_gateway_stage(t1,tt1,tt2,flag1,flag2):
	skip=0
	if t1.startswith("resource"):
		globals.apigwrestapiid=t1.split("r-")[1].split("_")[0]
	if tt1=="deployment_id" and tt2 != "null":
		t1=tt1 + " = aws_api_gateway_deployment.r-" + str(globals.apigwrestapiid)+"_" + tt2 + ".id\n"
	return skip,t1,flag1,flag2

def aws_api_gateway_usage_plan(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_api_gateway_usage_plan_key(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_api_gateway_vpc_link(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

