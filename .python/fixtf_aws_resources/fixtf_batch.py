def aws_batch_compute_environment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_batch_job_definition(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="deregister_on_new_revision" and tt2=="null":
		t1=tt1+" = true\n" 
		t1=t1+"\n lifecycle {\n   ignore_changes = [deregister_on_new_revision]\n}\n"

	return skip,t1,flag1,flag2

def aws_batch_job_queue(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_batch_scheduling_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

