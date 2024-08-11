import common
import boto3
import globals
import inspect

def aws_secretsmanager_random_password(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_secretsmanager_secret_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_secretsmanager_secret_rotation(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1=="rotate_immediately" and tt2=="null":
        t1=tt1+" = true\n" + " lifecycle {\n   ignore_changes = [rotate_immediately]\n}\n"
    return skip,t1,flag1,flag2

def aws_secretsmanager_secret_version(t1,tt1,tt2,flag1,flag2):
    skip=0
    ## need to get binary and string values
    try:
        if t1.startswith("resource"):
            vid=t1.split("_")[-1]
            vid=vid.replace("\"","").replace("{","").replace(" ","").replace("\n","")
            globals.secvid=vid
        elif tt1 == "secret_id":
            globals.secid=tt2
        elif tt1 == "secret_string":
            if "null" in tt2:
                client = boto3.client('secretsmanager')
                response = client.get_secret_value(SecretId=globals.secid,VersionId=globals.secvid)
                sv=response['SecretString']
                t1 = tt1 + " = jsonencode("+sv+")\n"
        if tt1 == "secret_binary": 
            t1="\n lifecycle {\n   ignore_changes = [secret_binary,secret_string]\n}\n"

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
    
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

