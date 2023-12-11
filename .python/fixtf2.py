import globals

def  aws_vpc(t1,tt1,tt2,skipipv6,flag2):
    skip = 0

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


def aws_vpc_ipv4_cidr_block_association(t1,tt1,tt2,skipipv6,flag2):
    skip = 0         
    if tt1 == "vpc_id":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_vpc." + tt2 + ".id\n"
        add_dependancy("aws_vpc",tt2)
    return skip,t1,skipipv6,flag2

    
def aws_subnet(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "vpc_id":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_vpc." + tt2 + ".id\n"
        add_dependancy("aws_vpc",tt2)
        

    if tt1 == "enable_lni_at_device_index":
        if tt2 == "0": skip=1
    if tt1 == "availability_zone_id": skip=1
    #
    if tt1 == "map_customer_owned_ip_on_launch":
        if tt2 == "false": skip=1

    return skip,t1,flag1,flag2


def  aws_security_group(t1,tt1,tt2,flag1,flag2):
    skip = 0
    if tt1 == "vpc_id":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_vpc." + tt2 + ".id\n"
        add_dependancy("aws_vpc",tt2)

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

    if tt1 == "vpc_id":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_vpc." + tt2 + ".id\n"
        add_dependancy("aws_vpc",tt2)

    elif "cidr_block" in tt1:
        tt2=tt2.strip('\"')
        if tt2 == "": t1=tt1 + " = null\n"

    elif "nat_gateway_id" in tt1:
        tt2=tt2.strip('\"')
        if tt2 != "":
            t1=tt1 + " = aws_nat_gateway." + tt2 + ".id\n"
            add_dependancy("aws_nat_gateway",tt2)

    elif tt1 == "gateway_id":
        tt2=tt2.strip('\"')
        if tt2 != "":
            t1=tt1 + " = aws_internet_gateway." + tt2 + ".id\n"
            add_dependancy("aws_internet_gateway",tt2)

    return skip,t1,flag1,flag2

def  aws_internet_gateway(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "vpc_id":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_vpc." + tt2 + ".id\n"
        add_dependancy("aws_vpc",tt2)

    return skip,t1,flag1,flag2

def  aws_nat_gateway(t1,tt1,tt2,flag1,flag2):
    skip=0
    if "secondary_private_ip_address_count" in tt1:
        tt2=tt2.strip('\"')
        if tt2 == "0": skip=1
    if tt1 == "subnet_id":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_subnet." + tt2 + ".id\n"
        add_dependancy("aws_subnet",tt2)

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


def aws_s3_bucket_acl(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_s3_bucket_analytics(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_s3_bucket_cors_configuration(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_s3_bucket_intelligent_tiering_configuration(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_s3_bucket_versioning(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_s3_bucket_website_configuration(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_s3_bucket_lifecycle_configuration(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_s3_bucket_logging(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_s3_bucket_metric(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_s3_bucket_request_payment_configuration(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_s3_bucket_accelerate_configuration(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_s3_bucket_server_side_encryption_configuration(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_s3_bucket_ownership_controls(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_s3_bucket_policy(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "policy": t1=globals_replace(t1,tt1,tt2)
    return skip,t1,flag1,flag2


def aws_vpc_endpoint(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "vpc_id":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_vpc." + tt2 + ".id\n"
        add_dependancy("aws_vpc",tt2)

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
        add_dependancy("aws_subnet",tt2)
    if tt1 == "route_table_id":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_route_table." + tt2 + ".id\n"
        add_dependancy("aws_route_table",tt2)
    if tt1 == "gateway_id":
        tt2=tt2.strip('\"')
        if tt2 == "null": skip=1
    
    return skip,t1,flag1,flag2


def aws_cloudwatch_log_group(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "name":
        tt2=tt2.strip('\"')
        if len(tt2) > 0: flag1=True

    #CIRCULAR reference problems:
    #if tt1 == "security_groups": t1,skip = deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)
  
    if tt1 == "name_prefix" and flag1 is True: skip=1

    if tt1 == "kms_key_id":
        tt2=tt2.strip('\"')
        if tt2 != "null": 
            t1=tt1 + " = aws_kms_key.k-" + tt2 + ".id\n"
            add_dependancy("aws_kms_key",tt2)
        else:
            skip=1

    return skip,t1,flag1,flag2 

def aws_config_config_rule(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2


## iam

def  aws_iam_role(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "name":
        tt2=tt2.strip('\"')
        if len(tt2) > 0: 
            flag1=True
            flag2=tt2
    if tt1 == "name_prefix" and flag1 is True: skip=1
    if tt1 == "policy": t1=globals_replace(t1,tt1,tt2)
    if tt1 == "assume_role_policy": t1=globals_replace(t1,tt1,tt2)
    if tt1 == "managed_policy_arns":   
        if tt2 == "[]": 
            skip=1
        elif ":"+globals.acc+":" in tt2:
            fs=""
            ends=",data.aws_caller_identity.current.account_id"
            tt2=tt2.replace("[","").replace("]","")
            cc=tt2.count(",")
            #print(str(tt2)+"cc="+str(cc))
            pt1=tt1+" = ["
            for j in range(0,cc+1):
                #print("-- tt2 "+str(j)+" split ="+tt2.split(",")[j])
                #print("-- tt2 "+j+" split ="+tt2.split(",")[j])
                ps=tt2.split(",")[j]
                if ":"+globals.acc+":" in ps:
                    #print("ps1="+ps)
                    a1=ps.find(":"+globals.acc+":")
                    #print("a1="+str(a1))
                    ps=ps[:a1]+":%s:"+ps[a1+14:]
                    #print("ps2="+ps)
                    ps = 'format('+ps+ends+')'
                    #print("ps3="+ps)         
                pt1=pt1+ps+","
            pt1=pt1+"]\n"
            t1=pt1.replace(",]","]")
            globals.roles=globals.roles+[flag2]
        else:
            pass
    #    else:
    #        t1=globals_replace(t1,tt1,tt2)
    return skip,t1,flag1,flag2

def aws_iam_role_policy(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "role_name":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_iam_role." + tt2 + ".id\n"
        add_dependancy("aws_iam_role",tt2)
  
    return skip,t1,flag1,flag2

def aws_iam_policy(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "name":
        tt2=tt2.strip('\"')
        if len(tt2) > 0: flag1=True
    if tt1 == "name_prefix" and flag1 is True: skip=1
    if tt1 == "policy": t1=globals_replace(t1,tt1,tt2)
  
    return skip,t1,flag1,flag2


def aws_iam_role_policy_attachment(t1,tt1,tt2,flag1,flag2):
    #print("fixit2.aws_iam_role_policy_attachment")
    skip=0
    if tt1 == "role":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_iam_role." + tt2 + ".id\n"
        add_dependancy("aws_iam_role",tt2)
    # skip as using policy arns minus account number etc..
    #if tt1 == "policy_arn": 
    #    tt2=tt2.strip('\"')
    #    tt2=str(tt2).split("/")[-1]
    #    t1=tt1 + " = aws_iam_policy." + str(tt2) + ".arn\n"
    if tt1 == "policy_arn": t1=globals_replace(t1,tt1,tt2)

    return skip,t1,flag1,flag2


### VPC Lattice  -----------------------

def aws_vpclattice_service_network(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2 


def aws_vpclattice_service(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_vpclattice_service_network_vpc_association(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "vpc_identifier":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_vpc." + tt2 + ".id\n"
        add_dependancy("aws_vpc",tt2)

    elif tt1 == "service_network_identifier":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_vpclattice_service_network." + tt2 + ".id\n"
        add_dependancy("aws_vpclattice_service_network",tt2)
    
    elif tt1 == "security_group_ids": 
        t1,skip = deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)
    return skip,t1,flag1,flag2


def aws_vpclattice_service_network_service_association(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "target_group_identifier":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_vpclattice_target_group." + tt2 + ".id\n"
        #add_dependancy("aws_vpclattice_target_group",tt2)
    elif tt1 == "service_identifier":
        tt2=tt2.strip('\"')
        flag2=tt2
        t1=tt1 + " = aws_vpclattice_service." + tt2 + ".id\n"
    elif tt1 == "service_network_identifier":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_vpclattice_service_network." + tt2 + ".id\n"
        #add_dependancy("aws_vpclattice_service_network",tt2)

    return skip,t1,flag1,flag2

def aws_vpclattice_listener(t1,tt1,tt2,flag1,flag2):
    skip=0

    if tt1 == "service_arn": t1=globals_replace(t1,tt1,tt2)
    elif tt1 == "target_group_identifier":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_vpclattice_target_group." + tt2 + ".id\n"
        add_dependancy("aws_vpclattice_target_group",tt2)
    elif tt1 == "service_identifier":
        tt2=tt2.strip('\"')
        flag2=tt2
        t1=tt1 + " = aws_vpclattice_service." + tt2 + ".id\n"


    return skip,t1,flag1,flag2

def aws_vpclattice_listener_rule(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "target_group_identifier":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_vpclattice_target_group." + tt2 + ".id\n"
        add_dependancy("aws_vpclattice_target_group",tt2)
    elif tt1 == "service_identifier":
        tt2=tt2.strip('\"')
        flag2=tt2
        t1=tt1 + " = aws_vpclattice_service." + tt2 + ".id\n"
    elif tt1 == "listener_identifier":
        tt2=tt2.strip('\"')
        if flag2 is not False:
            print("flag2="+flag2)
            svc=flag2.split('__')[1]
            ln=flag2.split('__')[2]
            tt2=svc+"__"+ln
            print("tt2="+tt2)
            t1=tt1 + " = aws_vpclattice_listener." + tt2 + ".listener_id\n"

    return skip,t1,flag1,flag2

def aws_vpclattice_target_group(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "vpc_identifier":
        tt2=tt2.strip('\"')
        if tt2 != "null":
            t1=tt1 + " = aws_vpc." + tt2 + ".id\n"
            add_dependancy("aws_vpc",tt2)
    if tt1 == "port":
        if tt2 == "0": skip=1
    return skip,t1,flag1,flag2


def aws_launch_template(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "security_group_names":
        tt2=tt2.strip('\"')
        if tt2 == "[]": 
            skip=1
    elif tt1 == "vpc_security_group_ids": t1,skip = deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)

    return skip,t1,flag1,flag2


### EKS -----------

def aws_eks_cluster(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "subnet_ids":  t1,skip = deref_array(t1,tt1,tt2,"aws_subnet","subnet-",skip)
    elif tt1 == "security_group_ids": t1,skip = deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)
    elif tt1 == "role_name":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_iam_role." + tt2 + ".id\n"
        add_dependancy("aws_iam_role",tt2)
    elif tt1 == "role_arn":
        tt2=tt2.strip('\"')
        if ":" in tt2: tt2=tt2.split("/")[-1]
        t1=tt1 + " = aws_iam_role." + tt2 + ".arn\n"
        add_dependancy("aws_iam_role",tt2)
    elif tt1 == "key_arn":
        tt2=tt2.strip('\"')
        if ":" in tt2: tt2="k-"+tt2.split("/")[-1]
        t1=tt1 + " = aws_kms_key." + tt2 + ".arn\n"
        add_dependancy("aws_kms_key",tt2)
    
    return skip,t1,flag1,flag2


def aws_eks_fargate_profile(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "subnet_ids":  t1,skip = deref_array(t1,tt1,tt2,"aws_subnet","subnet-",skip)
    elif tt1 == "pod_execution_role_arn":
        tt2=tt2.strip('\"')
        if ":" in tt2: tt2=tt2.split("/")[-1]
        t1=tt1 + " = aws_iam_role." + tt2 + ".arn\n"
        add_dependancy("aws_iam_role",tt2)
    elif tt1 == "cluster_name":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_eks_cluster." + tt2 + ".id\n"
        add_dependancy("aws_eks_cluster",tt2)
    
    return skip,t1,flag1,flag2

def aws_eks_node_group(t1,tt1,tt2,flag1,flag2):
    skip=0
    if "launch_template {" in t1: 
        #print("******* flag1 true launch_template")
        flag1=True
    if "max_unavailable_percentage" in tt1:
        tt2=tt2.strip('\"')
        #print(tt1+" "+tt2)
        if tt2 == "0": skip=1
    elif tt1 == "cluster_name":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_eks_cluster." + tt2 + ".id\n"
        add_dependancy("aws_eks_cluster",tt2)
    elif tt1 == "subnet_ids":  t1,skip = deref_array(t1,tt1,tt2,"aws_subnet","subnet-",skip)
    elif tt1 == "node_role_arn":
        tt2=tt2.strip('\"')
        if ":" in tt2: tt2=tt2.split("/")[-1]
        t1=tt1 + " = aws_iam_role." + tt2 + ".arn\n"
        add_dependancy("aws_iam_role",tt2)
    elif tt1 == "name":
        if flag1 is True: 
            tt2=tt2.strip('\"')
            #print("----********"+tt2)
            t1=tt1 + " = aws_launch_template." + tt2 + ".name\n"
            add_dependancy("aws_launch_template",tt2)
            flag1=False
    
    return skip,t1,flag1,flag2


def aws_eks_addon(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2 


def aws_kms_key(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "policy": t1=globals_replace(t1,tt1,tt2)
    #if tt1 == "key_id":
    #    add_dependancy("aws_kms_alias","k-"+theid)
    return skip,t1,flag1,flag2 

def aws_kms_alias(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "policy": t1=globals_replace(t1,tt1,tt2)
    if tt1 == "target_key_id":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_kms_key.k-" + tt2 + ".id\n"

    return skip,t1,flag1,flag2 


def aws_resource(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2 

def globals_replace(t1,tt1,tt2):
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
    if tt1 == "managed_policy_arns":
        tt2=tt2.replace('[','')
        tt2=tt2.replace(']','')
        tt2=tt2.replace('"','')
        t1 = tt1+' = [format("'+tt2+'"'+ends+')]\n'
    return t1


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
            add_dependancy(ttft,subn)

            
    if cc == 0 and prefix in tt2: 
        subs=subs + ttft + "." + tt2 + ".id,"
        add_dependancy(ttft,tt2)
             
    t1=tt1 + " = [" + subs + "]\n"
    t1=t1.replace(',]',']')
    return t1,skip



def add_dependancy(type,id):
    # check if we alredy have it
    pkey=type+"."+id
    if pkey not in globals.rproc:
        print("add_dependancy: " + pkey)
        globals.rproc[pkey]=False
    return


