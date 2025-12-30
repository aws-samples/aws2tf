"""
SECRETSMANAGER Resource Handlers - Optimized with __getattr__

This file contains ONLY SECRETSMANAGER resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 3 functions
Optimized: 3 functions + __getattr__
Reduction: 0% less code
"""

import logging
import common
import boto3
import context
import inspect
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# SECRETSMANAGER Resources with Custom Logic (3 functions)
# ============================================================================

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
            context.secvid=vid
        elif tt1 == "secret_id":
            context.secid=tt2
        elif tt1 == "secret_string":
            if "null" in tt2:
                client = boto3.client('secretsmanager')
                response = client.get_secret_value(SecretId=context.secid,VersionId=context.secvid)
                sv=response['SecretString']
                if '""""' in sv:
                    sv=sv.replace('""""', '""')
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



# ============================================================================
# Magic method for backward compatibility with getattr()
# ============================================================================



# ============================================================================
# Magic method for backward compatibility with getattr()
# ============================================================================

def __getattr__(name):
	"""
	Dynamically provide default handler for resources without custom logic.
	
	This allows getattr(module, "aws_resource") to work even if the
	function doesn't exist, by returning the default handler.
	
	All simple SECRETSMANAGER resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_secretsmanager' has no attribute '{name}'")


log.debug(f"SECRETSMANAGER handlers: 3 custom functions + __getattr__ for 0 simple resources")