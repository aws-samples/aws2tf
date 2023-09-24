import ec2
import common
import subprocess
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

        #dep call ?
        #com="./aws2tf.py -t aws_vpc -r eu-west-1 -i " + tt2
        #print("running: "+com)
        #rout=common.rc(com)
        #print(str(rout.stdout.decode().rstrip()))
        #subprocess.call(com, shell=True)
        #print("--> plan warning destroy - existing state ?")
        #exit()
        #print("gen complete")
            
       
        #ec2.ec2_resources("aws_vpc",tt2)



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

    if tt1 == "name_prefix" and flag1 is True: skip=1
       
    #            
    return skip,t1,flag1,flag2

def  aws_route_table(t1,tt1,tt2,flag1,flag2):
    skip=0
    print(tt1 + " " + tt2)
    if tt1 == "vpc_id":
        tt2=tt2.strip('\"')
        t1=tt1 + " = aws_vpc." + tt2 + ".id\n"
    if "cidr_block" in tt1:
        tt2=tt2.strip('\"')
        if tt2 == "": t1=tt1 + " = null\n"

    return skip,t1,flag1,flag2

def  aws_internet_gateway(t1,tt1,tt2,flag1,flag2):
    skip=0

    return skip,t1,flag1,flag2

def  aws_nat_gateway(t1,tt1,tt2,flag1,flag2):
    skip=0

    return skip,t1,flag1,flag2 



def  aws_resource(t1,tt1,tt2,flag1,flag2):
    skip=0

    return skip,t1,flag1,flag2 