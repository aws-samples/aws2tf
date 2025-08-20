import globals

def aws_elasticache_cluster(t1,tt1,tt2,flag1,flag2):
	skip=0



	
	if tt1 == "replication_group_id" and tt2 != "null":
		ot1=tt1+' = aws_elasticache_replication_group.'+'_'+tt2+'.id\n'
		

	elif tt1 == "engine" and globals.elastirep: skip=1
	elif tt1 == "az_mode" and globals.elastirep: skip=1
	elif tt1 == "engine_version" and globals.elastirep: skip=1
	elif tt1 == "maintenance_window" and globals.elastirep: skip=1
	elif tt1 == "node_type" and globals.elastirep: skip=1
	elif tt1 == "node_type" and globals.elastirep: skip=1
	elif tt1 == "num_cache_nodes" and globals.elastirep: skip=1

	elif tt1 == "parameter_group_name" and globals.elastirep: skip=1
	elif tt1 == "port" and globals.elastirep: skip=1
	elif tt1 == "snapshot_retention_limit" and globals.elastirep: skip=1
	elif tt1 == "snapshot_window" and globals.elastirep: skip=1
	elif tt1 == "subnet_group_name" and globals.elastirep: skip=1
	elif tt1 == "security_group_ids" and globals.elastirep: skip=1

	return skip,t1,flag1,flag2

def aws_elasticache_serverless_cache(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_elasticache_global_replication_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "num_node_groups" and tt2 == "0": skip=1
	return skip,t1,flag1,flag2

def aws_elasticache_parameter_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_elasticache_replication_group(t1,tt1,tt2,flag1,flag2):
	skip=0

	if tt1 == "global_replication_group_id" and tt2 != "null":
		ot1=tt1+' = aws_elasticache_global_replication_group.'+'_'+tt2+'.id\n'
		globals.elastigrep=True
	elif tt1 == "num_node_groups" and globals.elastigrep: skip=1
	elif tt1 == "parameter_group_name" and globals.elastigrep: skip=1
	elif tt1 == "engine" and globals.elastigrep: skip=1
	elif tt1 == "engine_version" and globals.elastigrep: skip=1
	elif tt1 == "node_type" and globals.elastigrep: skip=1
	elif tt1 == "security_group_names" and globals.elastigrep: skip=1
	elif tt1 == "security_group_ids" and globals.elastigrep: skip=1
	elif tt1 == "transit_encryption_enabled" and globals.elastigrep: skip=1
	elif tt1 == "at_rest_encryption_enabled" and globals.elastigrep: skip=1
	elif tt1 == "replicas_per_node_group" and tt2=="0": skip=1
	elif tt1 == "auth_token_update_strategy" and tt2=="null": 
		t1 = tt1+' = "ROTATE"\n'
		t1=t1+"\n lifecycle {\n   ignore_changes = [auth_token_update_strategy]\n}\n"


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

