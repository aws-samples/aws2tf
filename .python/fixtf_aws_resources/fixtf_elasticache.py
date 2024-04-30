def aws_elasticache_cluster(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_elasticache_global_replication_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_elasticache_parameter_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_elasticache_replication_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_elasticache_subnet_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_elasticache_user(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "engine" and tt2=="redis":
		t1=tt1+' = "REDIS"\n'
		t1=t1+"\n lifecycle {\n   ignore_changes = [engine,authentication_mode[0].type]\n}\n"
	if tt1 == "type" and tt2=="no-password":
		tt2="no-password-required"
		t1=tt1+' = "'+tt2+'"\n'


	return skip,t1,flag1,flag2

def aws_elasticache_user_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_elasticache_user_group_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

