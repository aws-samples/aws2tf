import common
import fixtf

def aws_eks_addon(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "cluster_name":
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_eks_cluster." + tt2 + ".id\n"
        common.add_dependancy("aws_eks_cluster",tt2)
    elif tt1 == "service_account_role_arn":
        ##tt2=tt2.strip('\"')
        if ":role/" in tt2:
            tt2=tt2.split("/")[-1]
            t1=tt1 + " = aws_iam_role." + tt2 + ".arn\n"
            common.add_dependancy("aws_iam_role",tt2)

    return skip,t1,flag1,flag2 

def aws_eks_addon_version(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_eks_cluster_auth(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_eks_pod_identity_association(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_eks_cluster(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "subnet_ids":  t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_subnet","subnet-",skip)
    elif tt1 == "security_group_ids": t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)
    elif tt1 == "role_name":
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_iam_role." + tt2 + ".id\n"
        common.add_dependancy("aws_iam_role",tt2)
    elif tt1 == "role_arn":
        ##tt2=tt2.strip('\"')
        if ":" in tt2: tt2=tt2.split("/")[-1]
        t1=tt1 + " = aws_iam_role." + tt2 + ".arn\n"
        common.add_dependancy("aws_iam_role",tt2)
    elif tt1 == "key_arn":
        ##tt2=tt2.strip('\"')
        if ":" in tt2: tt2="k-"+tt2.split("/")[-1]
        t1=tt1 + " = aws_kms_key." + tt2 + ".arn\n"
        common.add_dependancy("aws_kms_key",tt2)
    
    return skip,t1,flag1,flag2


def aws_eks_fargate_profile(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "subnet_ids":  t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_subnet","subnet-",skip)
    elif tt1 == "pod_execution_role_arn":
        ##tt2=tt2.strip('\"')
        if ":" in tt2: tt2=tt2.split("/")[-1]
        t1=tt1 + " = aws_iam_role." + tt2 + ".arn\n"
        common.add_dependancy("aws_iam_role",tt2)

    
    return skip,t1,flag1,flag2

def aws_eks_node_group(t1,tt1,tt2,flag1,flag2):
    skip=0
    if "launch_template {" in t1: 
        #print("******* flag1 true launch_template")
        flag1=True


    if "max_unavailable_percentage" in tt1:
        ##tt2=tt2.strip('\"')
        #print(tt1+" "+tt2)
        if tt2 == "0": skip=1

    elif "max_unavailable" in tt1:
        ##tt2=tt2.strip('\"')
        #print(tt1+" "+tt2)
        if tt2 == "0": skip=1

    elif "node_group_name_prefix" in tt1: skip=1
    elif tt1 == "cluster_name":
        ##tt2=tt2.strip('\"')
        t1=tt1 + " = aws_eks_cluster." + tt2 + ".id\n"
        common.add_dependancy("aws_eks_cluster",tt2)
    elif tt1 == "subnet_ids":  t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_subnet","subnet-",skip)
    elif tt1 == "node_role_arn":
        ##tt2=tt2.strip('\"')
        if ":" in tt2: tt2=tt2.split("/")[-1]
        t1=tt1 + " = aws_iam_role." + tt2 + ".arn\n"
        common.add_dependancy("aws_iam_role",tt2)
    elif tt1 == "name":
        if flag1 is True: 
            ##tt2=tt2.strip('\"')
            #print("----********"+tt2)
            t1=tt1 + " = aws_launch_template." + tt2 + ".name\n"
            common.add_dependancy("aws_launch_template",tt2)
            flag1=False
    
    return skip,t1,flag1,flag2




