import common
import fixtf


def aws_cloudwatch_log_group(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "name":
        
        if len(tt2) > 0: flag1=True

    #CIRCULAR reference problems:
    ##if tt1 == "security_groups": t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)
  
    if tt1 == "name_prefix" and flag1 is True: skip=1

    return skip,t1,flag1,flag2 

def aws_cloudwatch_composite_alarm(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudwatch_dashboard(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2



def aws_cloudwatch_log_data_protection_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudwatch_log_destination(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudwatch_log_destination_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudwatch_log_metric_filter(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudwatch_log_resource_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudwatch_log_stream(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudwatch_log_subscription_filter(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudwatch_metric_alarm(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudwatch_metric_stream(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudwatch_query_definition(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

