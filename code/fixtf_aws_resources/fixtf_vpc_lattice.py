import common
import fixtf
import base64
import boto3
import sys
import os
import globals
import inspect

def aws_vpclattice_auth_policy(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "resource_identifier":
        
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
        
        t1=tt1 + " = aws_vpc." + tt2 + ".id\n"
        common.add_dependancy("aws_vpc",tt2)

    elif tt1 == "service_network_identifier":
        
        t1=tt1 + " = aws_vpclattice_service_network." + tt2 + ".id\n"
        common.add_dependancy("aws_vpclattice_service_network",tt2)
    
    return skip,t1,flag1,flag2


def aws_vpclattice_service_network_service_association(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "target_group_identifier":
        
        t1=tt1 + " = aws_vpclattice_target_group." + tt2 + ".id\n"
        #common.add_dependancy("aws_vpclattice_target_group",tt2)
    elif tt1 == "service_identifier":
        
        flag2=tt2
        t1=tt1 + " = aws_vpclattice_service." + tt2 + ".id\n"
    elif tt1 == "service_network_identifier":
        
        t1=tt1 + " = aws_vpclattice_service_network." + tt2 + ".id\n"
        #common.add_dependancy("aws_vpclattice_service_network",tt2)

    return skip,t1,flag1,flag2

def aws_vpclattice_listener(t1,tt1,tt2,flag1,flag2):
    skip=0

    if tt1 == "service_arn": t1=fixtf.globals_replace(t1,tt1,tt2)
    elif tt1 == "target_group_identifier":
        
        t1=tt1 + " = aws_vpclattice_target_group." + tt2 + ".id\n"
        common.add_dependancy("aws_vpclattice_target_group",tt2)
    elif tt1 == "service_identifier":
        
        flag2=tt2
        t1=tt1 + " = aws_vpclattice_service." + tt2 + ".id\n"


    return skip,t1,flag1,flag2

def aws_vpclattice_listener_rule(t1,tt1,tt2,flag1,flag2):
    skip=0
    try:
        if tt1 == "target_group_identifier":
            
            t1=tt1 + " = aws_vpclattice_target_group." + tt2 + ".id\n"
            common.add_dependancy("aws_vpclattice_target_group",tt2)
        elif tt1=="priority":
            if tt2=="99999": 
                tt2="100"
                t1=tt1 + " = " + tt2 + "\n"
                t1=t1+"\nlifecycle {\n" + "   ignore_changes = [priority]\n" +  "}\n"
                
        
        elif tt1 == "service_identifier":
            
            flag2=tt2
            t1=tt1 + " = aws_vpclattice_service." + tt2 + ".id\n"
        elif tt1 == "listener_identifier":
            
            if flag2 is not False:
                #print("flag2="+flag2)
                rh=flag2.split('__')[1]
                svc=rh.split('_listener-')[0]
                ln=flag2.split('_listener-')[1]
                ln2=ln.split('_rule-')[0]
                tt2=svc+"_listener-"+ln2
                #print("---->>>> tt2="+tt2)
                t1=tt1 + " = aws_vpclattice_listener." + tt2 + ".listener_id\n"
    except Exception as e:
        common.handle_error2(e,str(inspect.currentframe().f_code.co_name),id)

    return skip,t1,flag1,flag2

def aws_vpclattice_target_group(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "vpc_identifier":
        
        if tt2 != "null":
            t1=tt1 + " = aws_vpc." + tt2 + ".id\n"
            common.add_dependancy("aws_vpc",tt2)
    if tt1 == "port":
        if tt2 == "0": skip=1
    return skip,t1,flag1,flag2

def aws_vpclattice_target_group_attachment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpclattice_resource_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpclattice_resource_configuration(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpclattice_service_network_resource_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_vpclattice_resource_gateway(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2


