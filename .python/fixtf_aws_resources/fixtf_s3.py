import common
import fixtf

def aws_s3_access_point(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_s3_account_public_access_block(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2


def  aws_s3_bucket(t1,tt1,tt2,flag1,flag2):
    skip=0
    if "resource":
        if  "aws_s3_bucket_request_payment_configuration" in tt1 or \
            "aws_s3_bucket_accelerate_configuration" in tt1 or \
            "aws_s3_bucket_acl" in tt1 or \
            "aws_s3_bucket_analytics" in tt1 or \
            "aws_s3_bucket_cors_configuration" in tt1 or \
            "aws_s3_bucket_intelligent_tiering_configuration" in tt1 or \
            "aws_s3_bucket_inventory" in tt1 or \
            "aws_s3_bucket_lifecycle_configuration" in tt1 or \
            "aws_s3_bucket_logging" in tt1  or \
            "aws_s3_bucket_metric" in tt1 or \
            "aws_s3_bucket_notification" in tt1 or \
            "aws_s3_bucket_object_lock_configuration" in tt1 or \
            "aws_s3_bucket_ownership_controls" in tt1 or \
            "aws_s3_bucket_policy" in tt1 or \
            "aws_s3_bucket_replication_configuration" in tt1 or \
            "aws_s3_bucket_request_payment_configuration" in tt1 or \
            "aws_s3_bucket_replication_configuration" in tt1 or \
            "aws_s3_bucket_server_side_encryption_configuration" in tt1 or \
            "aws_s3_bucket_versioning" in tt1 or \
            "aws_s3_bucket_website_configuration"in tt1 :
            flag2=True
        else:
            flag2=False
    if tt1 == "bucket" and flag2 is True:
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_s3_bucket.b-" + tt2 + ".bucket\n"
        flag2=False

    return skip,t1,flag1,flag2

def aws_s3_bucket_accelerate_configuration(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "bucket" and flag2 is True:
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_s3_bucket.b-" + tt2 + ".bucket\n"
    return skip,t1,flag1,flag2

def aws_s3_bucket_acl(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "bucket" and flag2 is True:
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_s3_bucket.b-" + tt2 + ".bucket\n"
    return skip,t1,flag1,flag2

def aws_s3_bucket_analytics(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "bucket" and flag2 is True:
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_s3_bucket.b-" + tt2 + ".bucket\n"
    return skip,t1,flag1,flag2

def aws_s3_bucket_analytics_configuration(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2


def aws_s3_bucket_cors_configuration(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "bucket" and flag2 is True:
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_s3_bucket.b-" + tt2 + ".bucket\n"
    return skip,t1,flag1,flag2

def aws_s3_bucket_intelligent_tiering_configuration(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "bucket" and flag2 is True:
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_s3_bucket.b-" + tt2 + ".bucket\n"
    return skip,t1,flag1,flag2

def aws_s3_bucket_inventory(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_s3_bucket_lifecycle_configuration(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "bucket" and flag2 is True:
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_s3_bucket.b-" + tt2 + ".bucket\n"
    return skip,t1,flag1,flag2

def aws_s3_bucket_logging(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "bucket" and flag2 is True:
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_s3_bucket.b-" + tt2 + ".bucket\n"
    return skip,t1,flag1,flag2

def aws_s3_bucket_metric(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "bucket" and flag2 is True:
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_s3_bucket.b-" + tt2 + ".bucket\n"
    return skip,t1,flag1,flag2

def aws_s3_bucket_notification(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_s3_bucket_object(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_s3_bucket_object_lock_configuration(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_s3_bucket_objects(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_s3_bucket_ownership_controls(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "bucket" and flag2 is True:
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_s3_bucket.b-" + tt2 + ".bucket\n"
    return skip,t1,flag1,flag2

def aws_s3_bucket_policy(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "bucket" and flag2 is True:
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_s3_bucket.b-" + tt2 + ".bucket\n"
    elif tt1 == "policy": t1=fixtf.globals_replace(t1,tt1,tt2)
    return skip,t1,flag1,flag2


def aws_s3_bucket_public_access_block(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_s3_bucket_replication_configuration(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_s3_bucket_request_payment_configuration(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "bucket" and flag2 is True:
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_s3_bucket.b-" + tt2 + ".bucket\n"
    return skip,t1,flag1,flag2

def aws_s3_bucket_server_side_encryption_configuration(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "bucket" and flag2 is True:
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_s3_bucket.b-" + tt2 + ".bucket\n"
    return skip,t1,flag1,flag2

def aws_s3_bucket_versioning(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "bucket" and flag2 is True:
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_s3_bucket.b-" + tt2 + ".bucket\n"
    return skip,t1,flag1,flag2

def aws_s3_bucket_website_configuration(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "bucket" and flag2 is True:
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_s3_bucket.b-" + tt2 + ".bucket\n"
    return skip,t1,flag1,flag2

def aws_s3_directory_bucket(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_s3_directory_buckets(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_s3_object(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_s3_object_copy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_s3_objects(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

