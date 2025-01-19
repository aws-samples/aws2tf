def aws_scheduler_schedule(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="maximum_window_in_minutes" and tt2=="0": skip=1
	return skip,t1,flag1,flag2

def aws_scheduler_schedule_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

