def aws_pipes_pipe(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="maximum_record_age_in_seconds" or tt1=="parallelization_factor":
		if tt2=="0": skip=1
	if tt1=="description":
		t1=t1+"\n lifecycle {\n   ignore_changes = [description]\n}\n"

	return skip,t1,flag1,flag2

