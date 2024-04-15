import common
import fixtf
import base64
import boto3
import sys
import os
import globals
import inspect

def aws_common(type,t1,tt1,tt2,flag1,flag2):
    skip=0
    try:
        if tt1 == "security_groups" or tt1 == "security_group_ids" or tt1 == "vpc_security_group_ids":
        # avoid circular references
            if type != "aws_security_group": 
                if type != "aws_cloudwatch_log_group":
                    #print("--->>  aws_common: type=",type,"tt1=",tt1,"tt2=",tt2)
                    t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)
                    #print("--returned deref array ->>  aws_common: t1="+t1+" skip="+str(skip))
                    return skip,t1,flag1,flag2


        elif tt1 == "subnets" or tt1 == "subnet_ids": t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_subnet","subnet-",skip)
        elif tt1 == "route_table_ids": t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_route_table","rtb-",skip)
        #elif tt1 == "cluster_members": fixtf.deref_array(t1,tt1,tt2,type,"*",skip)
        elif tt1 == "iam_roles": t1=fixtf.deref_role_arn_array(t1,tt1,tt2)
        elif tt1 == "vpc_id":
            if tt2 != "null":
                t1=tt1 + " = aws_vpc." + tt2 + ".id\n"
                common.add_dependancy("aws_vpc", tt2)

        elif tt1 == "subnet_id":
            if tt2 != "null":
                t1=tt1 + " = aws_subnet." + tt2 + ".id\n"
                print("----->>>>>>"+tt2)
                common.add_dependancy("aws_subnet", tt2)

        
        
        elif tt1 == "kms_key_id":
            if type != "aws_docdb_cluster":
                if tt2 != "null": 
                    if tt2 == "AWS_OWNED_KMS_KEY":	
                        skip=1
                    else:
                        if "arn:" in tt2: tt2=tt2.split("/")[-1]	
                        t1=tt1 + " = aws_kms_key.k-" + tt2 + ".id\n"
                        common.add_dependancy("aws_kms_key",tt2)
                else:
                    skip=1

        elif tt1 == "role_arn" or tt1=="service_linked_role_arn" or tt1 == "execution_role_arn" or tt1 == "task_role_arn": 
            t1=fixtf.deref_role_arn(t1,tt1,tt2)

        elif tt1 == "role" or tt1=="iam_role" or tt1=="role_name":
            if tt2 !="null" and "arn:" not in tt2:  
                t1=tt1 + " = aws_iam_role." + tt2 + ".id\n"
                common.add_dependancy("aws_iam_role",tt2)

        elif tt1=="target_group_arn" and tt2 != "null":
            tgarn=tt2
            tt2=tt2.replace("/","_").replace(".","_").replace(":","_")
            t1 = tt1 + " = aws_lb_target_group."+tt2+".arn\n"
            common.add_dependancy("aws_lb_target_group",tgarn)


    except Exception as e:
        common.handle_error2(e,str(inspect.currentframe()),id)

    
    return skip,t1,flag1,flag2