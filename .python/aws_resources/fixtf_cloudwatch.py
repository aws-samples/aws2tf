import common
import fixtf

def aws_cloudwatch_event_rule(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_cloudwatch_log_group(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "name":
        tt2=tt2.strip('\"')
        if len(tt2) > 0: flag1=True

    #CIRCULAR reference problems:
    #if tt1 == "security_groups": t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)
  
    if tt1 == "name_prefix" and flag1 is True: skip=1

    if tt1 == "kms_key_id":
        tt2=tt2.strip('\"')
        if tt2 != "null": 
            t1=tt1 + " = aws_kms_key.k-" + tt2 + ".id\n"
            common.add_dependancy("aws_kms_key",tt2)
        else:
            skip=1

    return skip,t1,flag1,flag2 

def aws_cloudwatch_composite_alarm(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudwatch_dashboard(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudwatch_event_api_destination(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudwatch_event_archive(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudwatch_event_bus(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudwatch_event_bus_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudwatch_event_connection(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudwatch_event_endpoint(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudwatch_event_permission(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudwatch_event_source(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudwatch_event_target(t1,tt1,tt2,flag1,flag2):
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

