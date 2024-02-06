def aws_autoscaling_attachment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_autoscaling_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "load_balancers" and tt2 == "[]": skip=1
	elif tt1 == "target_group_arns": skip=1
	return skip,t1,flag1,flag2

def aws_autoscaling_group_tag(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_autoscaling_lifecycle_hook(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_autoscaling_notification(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_autoscaling_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_autoscaling_schedule(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_autoscaling_traffic_source_attachment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

