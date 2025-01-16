def aws_appstream_directory_config(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_appstream_fleet(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="desired_sessions" and tt2=="0": skip=1
	if tt1=="desired_instancess" and tt2=="0": skip=1

	return skip,t1,flag1,flag2

def aws_appstream_fleet_stack_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_appstream_image_builder(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_appstream_stack(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="embed_host_domains" and tt2=="[]": skip=1
	return skip,t1,flag1,flag2

def aws_appstream_user(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="send_email_notification" and tt2=="null":
		t1=tt1+" = true\n"
		t1=t1+"\nlifecycle {\n" + "   ignore_changes = [send_email_notification]\n" +  "}\n"
		
	return skip,t1,flag1,flag2

def aws_appstream_user_stack_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

