import globals

def  aws_vpc(t1,tt1,tt2,skipipv6,flag2):
    skip = 0
    #print(t1)
    #print(tt1)
    #print(tt2)

    if tt1 == "assign_generated_ipv6_cidr_block":
        if tt2 in "true": skipipv6=True
    if tt1 == "ipv6_cidr_block":
        if skipipv6: skip = 1
    if tt1 == "ipv6_ipam_pool_id":
        if skipipv6: skip = 1
    if tt1 == "ipv6_netmask_length":
        if tt2 == "0":
            skip=1
        
    #            
    return skip,t1,skipipv6,flag2

    
def aws_subnet(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "vpc_id":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_vpc." + tt2 + ".id\n"

    if tt1 == "enable_lni_at_device_index":
        if tt2 == "0": skip=1
    if tt1 == "availability_zone_id": skip=1
    #
    if tt1 == "map_customer_owned_ip_on_launch":
        if tt2 == "false": skip=1

    return skip,t1,flag1,flag2


def  aws_security_group(t1,tt1,tt2,flag1,flag2):
    skip = 0
    #print(t1)
    #print(tt1)
    #print(tt2)

    if tt1 == "vpc_id":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_vpc." + tt2 + ".id\n"
    if tt1 == "name":
        tt2=tt2.strip('\"')
        if len(tt2) > 0: flag1=True

    #CIRCULAR reference problems:
    #if tt1 == "security_groups": t1,skip = deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)

    if tt1 == "name_prefix" and flag1 is True: skip=1
       
    #            
    return skip,t1,flag1,flag2

def  aws_route_table(t1,tt1,tt2,flag1,flag2):
    skip=0
    #print(tt1 + " " + tt2)
    if tt1 == "vpc_id":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_vpc." + tt2 + ".id\n"
    if "cidr_block" in tt1:
        tt2=tt2.strip('\"')
        if tt2 == "": t1=tt1 + " = null\n"

    return skip,t1,flag1,flag2

def  aws_internet_gateway(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "vpc_id":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_vpc." + tt2 + ".id\n"

    return skip,t1,flag1,flag2

def  aws_nat_gateway(t1,tt1,tt2,flag1,flag2):
    skip=0
    if "secondary_private_ip_address_count" in tt1:
        tt2=tt2.strip('\"')
        if tt2 == "0": skip=1
    if tt1 == "subnet_id":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_subnet." + tt2 + ".id\n"

    return skip,t1,flag1,flag2 


def  aws_network_acl(t1,tt1,tt2,flag1,flag2):
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
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_s3_bucket.b-" + tt2 + ".bucket\n"
        flag2=False
    


    return skip,t1,flag1,flag2


def aws_vpc_endpoint(t1,tt1,tt2,flag1,flag2):
    skip=0
    #print("tt1="+tt1)
    if tt1 == "vpc_id":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_vpc." + tt2 + ".id\n"

    if tt1 == "subnet_ids":  t1,skip = deref_array(t1,tt1,tt2,"aws_subnet","subnet-",skip)
    if tt1 == "security_group_ids": t1,skip = deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)

    return skip,t1,flag1,flag2


def aws_vpc_dhcp_options(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2


def aws_route_table_association(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "subnet_id":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_subnet." + tt2 + ".id\n"
    if tt1 == "route_table_id":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_route_table." + tt2 + ".id\n"
    
    return skip,t1,flag1,flag2


def deref_array(t1,tt1,tt2,ttft,prefix,skip):
    tt2=tt2.replace('"','').replace(' ','').replace('[','').replace(']','')
    cc=tt2.count(',')
    subs=""
    #if globals.debug: 
    #print("-->> " + tt1 + ": "  + tt2 + " count=" + str(cc))
    if cc > 0:
        for i in range(cc+1):
            subn=tt2.split(',')[i]
            subs=subs + ttft + "." + subn + ".id,"
            
    if cc == 0 and prefix in tt2: subs=subs + ttft + "." + tt2 + ".id,"
             
    t1=tt1 + " = [" + subs + "]\n"
    t1=t1.replace(',]',']')
    return t1,skip

def aws_cloudwatch_log_group(t1,tt1,tt2,flag1,flag2):
    skip=0

    return skip,t1,flag1,flag2 


def aws_config_config_rule(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2


## iam

def  aws_iam_role(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "name":
        tt2=tt2.strip('\"')
        if len(tt2) > 0: flag1=True
    if tt1 == "name_prefix" and flag1 is True: skip=1
    return skip,t1,flag1,flag2

def aws_iam_role_policy(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "subnet_id":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_iam_role." + tt2 + ".id\n"
  
    return skip,t1,flag1,flag2

def aws_iam_policy(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "name":
        tt2=tt2.strip('\"')
        if len(tt2) > 0: flag1=True
    if tt1 == "name_prefix" and flag1 is True: skip=1
    if tt1 == "policy":
        #print("policy " + globals.acc + " "+ tt2)
        ends=""
        while ":"+globals.acc+":" in tt2:
            #print("--> 5")
            r1=tt2.find(":"+globals.region+":")
            a1=tt2.find(":"+globals.acc+":")
            #print("--> r1="+ str(r1) + " ")
            #print("--> a1="+ str(a1) + " ")
            if r1>0 and r1 < a1:
                    #print("--> 6a")
                    ends=ends+",data.aws_region.current.name"
                    tt2=tt2[:r1]+":%s:"+tt2[r1+globals.regionl+2:]

            a1=tt2.find(":"+globals.acc+":")
            tt2=tt2[:a1]+":%s:"+tt2[a1+14:]
            ends=ends+",data.aws_caller_identity.current.account_id"
         
            t1 = tt1+" = format("+tt2+ends+")\n"
  
    return skip,t1,flag1,flag2


# -----------------------
def  aws_resource(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2 
