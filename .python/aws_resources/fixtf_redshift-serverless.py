def aws_redshiftserverless_namespace(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "kms_key_id":
        tt2=tt2.strip('\"')
        if tt2 != "null": 
            if tt2 == "AWS_OWNED_KMS_KEY":
                skip=1
            else:
                t1=tt1 + " = aws_kms_key.k-" + tt2 + ".id\n"
                add_dependancy("aws_kms_key",tt2)
        else:
            skip=1

    elif tt1 == "default_iam_role_arn": 
        t1=deref_role_arn(t1,tt1,tt2)

    elif tt1 == "iam_roles":    
        t1=deref_role_arn_array(t1,tt1,tt2)

    return skip,t1,flag1,flag2 

def aws_redshiftserverless_workgroup(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "subnet_ids":  t1,skip = deref_array(t1,tt1,tt2,"aws_subnet","subnet-",skip)
    elif tt1 == "security_group_ids": t1,skip = deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)
    elif tt1 == "namespace_name": 
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_redshiftserverless_namespace." + tt2 + ".id\n"
        add_dependancy("aws_redshiftserverless_namespace",tt2)

    return skip,t1,flag1,flag2



def aws_redshiftserverless_credentials(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_redshiftserverless_endpoint_access(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_redshiftserverless_resource_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_redshiftserverless_snapshot(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_redshiftserverless_usage_limit(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

