import common
import fixtf

def aws_kms_key(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "policy": t1=fixtf.globals_replace(t1,tt1,tt2)
    #if tt1 == "key_id":
    #    common.add_dependancy("aws_kms_alias","k-"+theid)
    return skip,t1,flag1,flag2 

def aws_kms_alias(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "policy": t1=fixtf.globals_replace(t1,tt1,tt2)
    if tt1 == "target_key_id":
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_kms_key.k-" + tt2 + ".id\n"
        common.add_dependancy("aws_kms_key","k-"+tt2)
	
    return skip,t1,flag1,flag2 


def aws_kms_ciphertext(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_kms_custom_key_store(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_kms_external_key(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_kms_grant(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_kms_key_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_kms_public_key(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_kms_replica_external_key(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_kms_replica_key(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_kms_secret(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_kms_secrets(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

