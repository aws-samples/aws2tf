import common
import fixtf
import globals
import inspect

def aws_db_parameter_group(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_db_subnet_group(t1,tt1,tt2,flag1,flag2):
    skip=0
    ##if tt1 == "subnet_ids":  t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_subnet","subnet-",skip)
    return skip,t1,flag1,flag2

def aws_db_instance(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "domain_dns_ips":
       if tt2 == "[]": skip=1

    elif tt1 == "db_name" or tt1 ==  "username":
       if globals.repdbin: skip=1

    elif tt1 == "parameter_group_name":
        if "default" not in tt2:
            t1=tt1 + " = aws_db_parameter_group." + tt2 + ".id\n"

    return skip,t1,flag1,flag2

def aws_db_event_subscription(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2



def aws_db_cluster_snapshot(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_db_event_categories(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2


def aws_db_instance_automated_backups_replication(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_db_instance_role_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_db_option_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_db_proxy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_db_proxy_default_target_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_db_proxy_endpoint(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_db_proxy_target(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_db_snapshot(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_db_snapshot_copy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2



def aws_rds_cluster(t1,tt1,tt2,flag1,flag2):
	try:
		skip=0
		##if tt1 == "vpc_security_group_ids": t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)
		## if tt1 == "iam_roles":  t1=fixtf.deref_role_arn_array(t1,tt1,tt2)
		if tt1 == "db_cluster_parameter_group_name":
			t1=tt1 + " = aws_rds_cluster_parameter_group." + tt2 + ".id\n"
			common.add_dependancy("aws_rds_cluster_parameter_group",tt2)
		elif tt1 == "db_subnet_group_name":
			t1=tt1 + " = aws_db_subnet_group." + tt2 + ".id\n"
			common.add_dependancy("aws_db_subnet_group",tt2)
		#elif tt1 == "kms_key_id": t1=fixtf.deref_kms_key(t1,tt1,tt2)
		elif tt1 == "cluster_members": 
			t1,skip=fixtf.deref_array(t1,tt1,tt2,"aws_rds_cluster_instance","",skip)
			#common.add_dependancy("aws_rds_cluster_instance",tt2)

	except Exception as e:
		print("*** Exception in aws_rds_cluster: " + str(e))
		common.handle_error2(e,"aws_rds_cluster","mdadb")
    
	return skip,t1,flag1,flag2

def aws_rds_cluster_parameter_group(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_rds_cluster_instance(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="performance_insights_retention_period":
		if tt2=="0":
			skip=1
	return skip,t1,flag1,flag2


def aws_rds_certificate(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_rds_cluster_activity_stream(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_rds_cluster_endpoint(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_rds_cluster_role_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_rds_clusters(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_rds_custom_db_engine_version(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_rds_engine_version(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_rds_export_task(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_rds_global_cluster(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_rds_orderable_db_instance(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_rds_reserved_instance(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_rds_reserved_instance_offering(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

