
import common
import fixtf

def aws_vpclattice_auth_policy(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "resource_identifier":
        ##tt2=tt2.strip('\"')
        if "svc-" in tt2:
            t1=tt1 + " = aws_vpclattice_service." + tt2 + ".arn\n"
            common.add_dependancy("aws_vpclattice_service",tt2)
        if "sn-" in tt2:
            t1=tt1 + " = aws_vpclattice_service_network." + tt2 + ".arn\n"
            common.add_dependancy("aws_vpclattice_service_network",tt2)
    return skip,t1,flag1,flag2

def aws_vpclattice_service_network(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2 


def aws_vpclattice_service(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_vpclattice_service_network_vpc_association(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "vpc_identifier":
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_vpc." + tt2 + ".id\n"
        common.add_dependancy("aws_vpc",tt2)

    elif tt1 == "service_network_identifier":
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_vpclattice_service_network." + tt2 + ".id\n"
        common.add_dependancy("aws_vpclattice_service_network",tt2)
    
    elif tt1 == "security_group_ids": 
        t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)
    return skip,t1,flag1,flag2


def aws_vpclattice_service_network_service_association(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "target_group_identifier":
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_vpclattice_target_group." + tt2 + ".id\n"
        #common.add_dependancy("aws_vpclattice_target_group",tt2)
    elif tt1 == "service_identifier":
        ##tt2=tt2.strip('\"')
        flag2=tt2
        t1=tt1 + " = aws_vpclattice_service." + tt2 + ".id\n"
    elif tt1 == "service_network_identifier":
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_vpclattice_service_network." + tt2 + ".id\n"
        #common.add_dependancy("aws_vpclattice_service_network",tt2)

    return skip,t1,flag1,flag2

def aws_vpclattice_listener(t1,tt1,tt2,flag1,flag2):
    skip=0

    if tt1 == "service_arn": t1=fixtf.globals_replace(t1,tt1,tt2)
    elif tt1 == "target_group_identifier":
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_vpclattice_target_group." + tt2 + ".id\n"
        common.add_dependancy("aws_vpclattice_target_group",tt2)
    elif tt1 == "service_identifier":
        ##tt2=tt2.strip('\"')
        flag2=tt2
        t1=tt1 + " = aws_vpclattice_service." + tt2 + ".id\n"


    return skip,t1,flag1,flag2

def aws_vpclattice_listener_rule(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "target_group_identifier":
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_vpclattice_target_group." + tt2 + ".id\n"
        common.add_dependancy("aws_vpclattice_target_group",tt2)
    elif tt1 == "service_identifier":
        ##tt2=tt2.strip('\"')
        flag2=tt2
        t1=tt1 + " = aws_vpclattice_service." + tt2 + ".id\n"
    elif tt1 == "listener_identifier":
        ##tt2=tt2.strip('\"')
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
        ##tt2=tt2.strip('\"')
        if tt2 != "null":
            t1=tt1 + " = aws_vpc." + tt2 + ".id\n"
            common.add_dependancy("aws_vpc",tt2)
    if tt1 == "port":
        if tt2 == "0": skip=1
    return skip,t1,flag1,flag2

def aws_vpclattice_target_group_attachment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

