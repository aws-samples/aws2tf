def aws_secretsmanager_random_password(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_secretsmanager_secret_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_secretsmanager_secret_rotation(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_secretsmanager_secret_version(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_secretsmanager_secret(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "recovery_window_in_days":
        
        if tt2 == "null": 
            t1 = tt1 + "= 30\n lifecycle {\n   ignore_changes = [recovery_window_in_days,force_overwrite_replica_secret]\n}\n"

    elif tt1 == "force_overwrite_replica_secret":
        
        if tt2 == "null": 
            t1 = tt1 + "= false\n"


    return skip,t1,flag1,flag2

