import common,fixtf
import base64
import boto3
import sys,os
import globals
import inspect

# returns True if key is one we want - ie not AWS managed
def check_key(keyid):
	keyclient=boto3.client('kms')
	try:
		kresp=keyclient.describe_key(KeyId=keyid)
		kstatus=kresp['KeyMetadata']['KeyState']
		kman=kresp['KeyMetadata']['KeyManager']
		#print(str(kresp))
		if kstatus == "Enabled" or kstatus == "Disabled":
			if kman == "AWS":
				print("key is managed by AWS")
				return False
			return True
		else:
			print("WARNING: key is not valid or is managed by AWS")
			print(str(kresp))
			return False
	except Exception as e:
		print("WARNING: can't access key",keyid)
		#print(f"{e=} [k1]")
		#exc_type, exc_obj, exc_tb = sys.exc_info()
	return False

def aws_common(type,t1,tt1,tt2,flag1,flag2):
    skip=0
    #if globals.debug: print("aws_common t1=",t1)
    try:
        if tt1=="api_id" and "apigatewayv2" in type:
            t1=tt1 + " = aws_apigatewayv2_api." + tt2 + ".id\n"
            globals.api_id=tt2
            common.add_dependancy("aws_apigatewayv2_api", tt2)
        if tt1=="bucket" or tt1=="s3_bucket_name":
            if type != "aws_s3_bucket":
                if "." not in tt2:
                    if tt2 != "":
                        t1=tt1 + " = aws_s3_bucket.b-" + tt2 + ".bucket\n"
                        common.add_dependancy("aws_s3_bucket", tt2)
                        return skip,t1,flag1,flag2
                    
        elif tt1 == "rest_api_id" and "aws_api_gateway_" in type:
            if tt2 != "null":
                t1=tt1 + " = aws_api_gateway_rest_api.r-" + tt2 + ".id\n"
                #common.add_dependancy("aws_api_gateway_rest_api", tt2)
                globals.apigwrestapiid=tt2

        elif tt1 == "security_groups" or tt1 == "security_group_ids" or tt1 == "vpc_security_group_ids":
        # avoid circular references
            if type != "aws_security_group": 
                if type != "aws_cloudwatch_log_group":
                    #print("--->>  aws_common: type=",type,"tt1=",tt1,"tt2=",tt2)
                    t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_security_group","sg-",skip)
                    #print("--returned deref array ->>  aws_common: t1="+t1+" skip="+str(skip))
                    return skip,t1,flag1,flag2

        elif tt1 == "subnets" or tt1 == "subnet_ids": t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_subnet","subnet-",skip)
        elif tt1 == "route_table_ids": t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_route_table","rtb-",skip)
        
        elif tt1 == "iam_roles": t1=fixtf.deref_role_arn_array(t1,tt1,tt2)
        elif tt1 == "vpc_id":
            if tt2 != "null":
                if globals.vpclist[tt2]:
                    t1=tt1 + " = aws_vpc." + tt2 + ".id\n"
                    common.add_dependancy("aws_vpc", tt2)
                else:
                    print("WARNING: vpc_id not found in vpclist",tt2)

        elif tt1 == "subnet_id":
            if tt2 != "null":
                if globals.subnetlist[tt2]:
                    t1=tt1 + " = aws_subnet." + tt2 + ".id\n"
                    common.add_dependancy("aws_subnet", tt2)
                else:
                    print("WARNING: subnet_id not found in subnetlist", tt2)

        elif tt1 == "file_system_id":
            if tt2 != "null":
                t1=tt1 + " = aws_efs_file_system." + tt2 + ".id\n"
                common.add_dependancy("aws_efs_file_system", tt2)

        elif tt1 == "kms_key_arn":
            if tt2 != "null":     
                if "arn:" in tt2: 
                    tt2=tt2.split("/")[-1]
                    if check_key(tt2):	
                        t1=tt1 + " = aws_kms_key.k-" + tt2 + ".arn\n"
                        common.add_dependancy("aws_kms_key",tt2)
            else:
                skip=1
        
        elif tt1 == "kms_key_id" or tt1=="kms_master_key_id" or tt1=="target_key_id":
            if type != "aws_docdb_cluster":
                if tt2 != "null": 
                    skip=1
                    if tt2 == "AWS_OWNED_KMS_KEY":	
                        skip=1
                    else:
                        if "arn:" in tt2:   
                            tt2=tt2.split("/")[-1]	
                            if check_key(tt2):
                                t1=tt1 + " = aws_kms_key.k-" + tt2 + ".arn\n"
                                common.add_dependancy("aws_kms_key",tt2) 
                                skip=0             
                        else:
                            tt2=tt2.split("/")[-1]
                            if check_key(tt2):
                                t1=tt1 + " = aws_kms_key.k-" + tt2 + ".id\n"
                                common.add_dependancy("aws_kms_key", tt2)
                                skip=0                   
                else:
                    skip=1

        elif tt1 == "instance_profile_name":
            if tt2 != "null":
                t1=tt1 + " = aws_iam_instance_profile." + tt2 + ".id\n"
                common.add_dependancy("aws_iam_instance_profile", tt2)
            else:
                skip=1

        elif tt1 == "key_pair":
            if tt2 != "null":
                t1=tt1 + " = aws_key_pair." + tt2 + ".id\n"
                common.add_dependancy("aws_key_pair", tt2)
            else:
                skip=1

        elif tt1 == "role_arn" or tt1=="service_linked_role_arn" or tt1 == "execution_role_arn" \
            or tt1 == "task_role_arn" or tt1 == "iam_service_role_arn" or tt1 == "execution_role" \
                or tt1=="source_arn" or tt1 == "cloudwatch_role_arn" or tt1=="service_linked_role_arn" \
                    or tt1=="service_role": 
            t1=fixtf.deref_role_arn(t1,tt1,tt2)

        elif tt1 == "role" or tt1=="iam_role" or tt1=="role_name":
            if tt2 !="null" and "arn:" not in tt2: 
                if "/" not in tt2: 
                    if globals.rolelist[tt2]:
                        rn=tt2.replace(".","_")
                        t1=tt1 + " = aws_iam_role." + rn + ".id\n"
                        common.add_dependancy("aws_iam_role",tt2)
                    else:
                        print("WARNING: role not found in rolelist", tt2)

        elif tt1=="target_group_arn" and tt2 != "null":
            tgarn=tt2
            tt2=tt2.replace("/","_").replace(".","_").replace(":","_")
            t1 = tt1 + " = aws_lb_target_group."+tt2+".arn\n"
            common.add_dependancy("aws_lb_target_group",tgarn)


        ### RHS processing
        ### causes a hang loop
        #if tt2.startswith("s3://"): t1=fixtf.rhs_replace(t1,tt1,tt2)
        ## replace region and account number on RHS
        elif tt2==globals.acc: t1=tt1 + ' = format("%s",data.aws_caller_identity.current.account_id)\n'
        elif tt2==globals.region: t1=tt1 + ' = format("%s",data.aws_region.current.name)\n'
        ## fix zones
        elif tt2==globals.region+"a":  t1=tt1 + ' = format("%sa",data.aws_region.current.name)\n'
        elif tt2==globals.region+"b":  t1=tt1 + ' = format("%sb",data.aws_region.current.name)\n'
        elif tt2==globals.region+"c":  t1=tt1 + ' = format("%sc",data.aws_region.current.name)\n'
        elif tt2==globals.region+"d":  t1=tt1 + ' = format("%sd",data.aws_region.current.name)\n'
        elif tt2==globals.region+"e":  t1=tt1 + ' = format("%se",data.aws_region.current.name)\n'
        elif tt2==globals.region+"f":  t1=tt1 + ' = format("%sf",data.aws_region.current.name)\n'

        if globals.debug: print("aws_common tt2="+tt2)
        ## Use a straight if here ?
        ## tt2 is arn - call globals_replace ?
        if tt2.startswith("arn:"): 
            t1=fixtf.globals_replace(t1, tt1, tt2)
        #if tt2.startswith('["arn:'): 
        #    t1=fixtf.globals_replace(t1, tt1, tt2)

    except Exception as e:
        common.handle_error2(e,str(inspect.currentframe()),id)

    
    return skip,t1,flag1,flag2