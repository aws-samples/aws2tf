def aws_cloud9_environment_ec2(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="instance_type" and tt2=="null": skip=1
	if tt1=="image_id" and tt2=="null": skip=1
	return skip,t1,flag1,flag2

def aws_cloud9_environment_membership(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

