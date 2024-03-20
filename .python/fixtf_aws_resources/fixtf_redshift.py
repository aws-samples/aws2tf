import common
import fixtf

def aws_redshift_cluster(t1,tt1,tt2,flag1,flag2):
    skip=0
    ##if tt1 == "vpc_security_group_ids": t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)
    ## if tt1 == "iam_roles":    t1=fixtf.deref_role_arn_array(t1,tt1,tt2)
    if tt1 == "cluster_subnet_group_name":
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_redshift_subnet_group." + tt2 + ".id\n"
        common.add_dependancy("aws_redshift_subnet_group",tt2)
    elif tt1 == "cluster_parameter_group_name":
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_redshift_parameter_group." + tt2 + ".id\n"
        common.add_dependancy("aws_redshift_parameter_group",tt2)
    #elif tt1 == "kms_key_id":    t1=fixtf.deref_kms_key(t1,tt1,tt2)
    
    return skip,t1,flag1,flag2 

def aws_redshift_subnet_group(t1,tt1,tt2,flag1,flag2):
    skip=0
    ##if tt1 == "subnet_ids":  t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_subnet","subnet-",skip)
    return skip,t1,flag1,flag2

def aws_redshift_parameter_group(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2




def aws_redshift_authentication_profile(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_redshift_cluster_credentials(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_redshift_cluster_iam_roles(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_redshift_cluster_snapshot(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_redshift_endpoint_access(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_redshift_endpoint_authorization(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_redshift_event_subscription(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_redshift_hsm_client_certificate(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_redshift_hsm_configuration(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_redshift_orderable_cluster(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_redshift_partner(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_redshift_resource_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_redshift_scheduled_action(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_redshift_service_account(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_redshift_snapshot_copy_grant(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_redshift_snapshot_schedule(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_redshift_snapshot_schedule_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_redshift_usage_limit(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

