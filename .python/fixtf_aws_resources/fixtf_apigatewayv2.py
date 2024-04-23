import common
import fixtf
import base64
import boto3
import sys
import os
import globals
import inspect


def aws_apigatewayv2_api(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_apigatewayv2_api_mapping(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_apigatewayv2_authorizer(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_apigatewayv2_deployment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_apigatewayv2_domain_name(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_apigatewayv2_integration(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_apigatewayv2_integration_response(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_apigatewayv2_model(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_apigatewayv2_route(t1,tt1,tt2,flag1,flag2):
	skip=0
	try:
		if tt1 == "authorizer_id" and tt2 != "null":
			t1=tt1+" = aws_apigatewayv2_authorizer."+globals.api_id+"_"+tt2+".id\n"
			
	except Exception as e:
		common.handle_error2(e,str(inspect.currentframe().f_code.co_name),id)
	return skip,t1,flag1,flag2

def aws_apigatewayv2_route_response(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_apigatewayv2_stage(t1,tt1,tt2,flag1,flag2):
	skip=0
	try:
		### FIX THIS
		if tt1 == "deployment_id" and tt2 != "null":
			t1=tt1+" = aws_apigatewayv2_deployment."+globals.api_id+"_"+tt2+".id\n"
	except Exception as e:
		common.handle_error2(e,str(inspect.currentframe().f_code.co_name),id)
	return skip,t1,flag1,flag2

def aws_apigatewayv2_vpc_link(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

