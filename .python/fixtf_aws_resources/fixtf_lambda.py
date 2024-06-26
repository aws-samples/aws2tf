import common
import fixtf
import os
import globals

def aws_lambda_function(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "role":
        tt2=tt2.split("/")[-1]
        if "." in tt2:
            rn=tt2.replace(".","_")
            t1=tt1 + " = aws_iam_role." + rn + ".arn\n"
        else:
            t1=tt1 + " = aws_iam_role." + tt2 + ".arn\n"
        common.add_dependancy("aws_iam_role",tt2)
        pkey="aws_iam_role"+"."+tt2
        print("pkey="+pkey)
        #globals.rproc[pkey]=True
    elif tt1 == "filename":
             
        if os.path.isfile(flag2+".zip"):
            t1=tt1 + " = \""+flag2+".zip\"\n lifecycle {\n   ignore_changes = [filename,publish,source_code_hash]\n}\n"
        elif tt2 == "null": skip=1
    elif tt1 == "image_uri":
        
        if tt2 == "null": skip=1
    elif tt1 == "source_code_hash":
        
        if os.path.isfile(flag2+".zip"):
            t1=tt1 + " = filebase64sha256(\""+flag2+".zip"+"\")\n"
        elif tt2 == "null": skip=1

    elif tt1 == "s3_bucket":
        
        if tt2 == "null": skip=1

    ##elif tt1 == "subnet_ids":  t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_subnet","subnet-",skip)
    ##elif tt1 == "security_group_ids": t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)

        #t1=tt1 + " = aws_vpc_config." + tt2 + ".arn\n"
        #common.add_dependancy("aws_vpc_config",tt2)
    return skip,t1,flag1,flag2

def aws_lambda_alias(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_lambda_permission(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_lambda_function_event_invoke_configs(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_lambda_event_source_mapping(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_lambda_code_signing_config(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_lambda_function_url(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_lambda_functions(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_lambda_invocation(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_lambda_provisioned_concurrency_config(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_lambda_layer_version(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_lambda_layer_version_permission(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

