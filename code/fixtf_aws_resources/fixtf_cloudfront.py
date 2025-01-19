def aws_cloudfront_cache_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudfront_continuous_deployment_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudfront_distribution(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="cache_policy_id" and tt2 != "null":
		t1=tt1+" = aws_cloudfront_cache_policy.o-"+tt2+".id\n"
	return skip,t1,flag1,flag2

def aws_cloudfront_field_level_encryption_config(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudfront_field_level_encryption_profile(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudfront_function(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="publish" and tt2=="null": 
		#t1=t1+"\n lifecycle {\n   ignore_changes = [publish]\n}\n"
		t1=tt1+" = true\n" 
		t1=t1+"\n lifecycle {\n   ignore_changes = [publish]\n}\n"
	return skip,t1,flag1,flag2

def aws_cloudfront_key_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudfront_monitoring_subscription(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudfront_origin_access_control(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudfront_origin_access_identities(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudfront_origin_access_identity(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudfront_origin_request_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudfront_public_key(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudfront_realtime_log_config(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_cloudfront_response_headers_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

