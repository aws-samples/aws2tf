import common
import fixtf
import os
import context
import boto3
from botocore.exceptions import ClientError

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
        #context.rproc[pkey]=True
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

    ###### layers code
    elif tt1 == "layers" and tt2!="[]":
        if tt2 != "null" and "arn:" in tt2:
            cc=tt2.count(',')
            tt2=tt2.lstrip('[').rstrip(']')
        else:
             print("WARNING: layers is not an array", tt2)
             return skip,t1,flag1,flag2
        #if context.debug: 
        builds=""
        if cc > 0:
            for i in range(cc+1):
                subn=tt2.split(',')[i]
                subn=subn.strip(" ").lstrip('"').rstrip('"').strip(" ")
                if context.acc in subn:
                    tarn=subn.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_")
                    common.add_dependancy("aws_lambda_layer_version",subn)
                    builds=builds+"aws_lambda_layer_version."+tarn+".arn,"
                else:
                    builds=builds+"\""+subn+"\", "
            
            if builds.endswith(','):
                builds=builds.rstrip(',')
            t1 = tt1+" = ["+builds+"]\n"
                
        elif cc == 0:
            if context.acc in tt2:  
                tt2=tt2.lstrip('"').rstrip('"')
                larn=tt2.split(":")[:-1]
                myarn=""
                for ta in larn:
                    myarn=myarn+ta+":"
                
                myarn=myarn.rstrip(":")
                tarn=tt2.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_")
                # test we can get at it before sub
                
                t1 = tt1+" = [aws_lambda_layer_version."+tarn+ ".arn]\n"
                common.add_dependancy("aws_lambda_layer_version",tt2)

    return skip,t1,flag1,flag2

def aws_lambda_alias(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_lambda_permission(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1=="function_name" and tt2 != "null":
         t1 = tt1 + " = aws_lambda_function." + tt2 + ".function_name\n"
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
    if tt1 == "filename":    
        if os.path.isfile(flag2+".zip"):
            t1=tt1 + " = \""+flag2+".zip\"\n lifecycle {\n   ignore_changes = [filename,source_code_hash]\n}\n"
        
        elif tt2 == "null": skip=1
    
    return skip,t1,flag1,flag2

def aws_lambda_layer_version_permission(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_lambda_function_event_invoke_config(t1, tt1, tt2, flag1, flag2):
    skip=0
    if tt1=="maximum_event_age_in_seconds" and tt2=="0": skip=1
    elif tt1=="function_name" and tt2 != "null":
        if tt2.startswith("arn:"):
            fname=tt2.split(":")[-1]
            t1 = tt1 + " = aws_lambda_function." + fname + ".arn\n"
        else:
            t1 = tt1 + " = aws_lambda_function." + tt2 + ".function_name\n"
    return skip,t1,flag1,flag2