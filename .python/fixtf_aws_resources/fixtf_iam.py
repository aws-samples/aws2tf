import common
import fixtf
import globals


def aws_iam_access_key(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "user":
        pkey="aws_iam_access_key."+tt2
        globals.rproc[pkey]=True
        t1=tt1+" = aws_iam_user."+tt2+".id\n"
    return skip,t1,flag1,flag2

def aws_iam_access_keys(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_iam_account_alias(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_iam_account_password_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_iam_group(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1 == "name":
		#print("get users in group "+tt2)
		common.add_dependancy("aws_iam_user_group_membership",tt2)
		common.add_dependancy("aws_iam_group_policy",tt2)
	return skip,t1,flag1,flag2

def aws_iam_group_membership(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1=="user" and tt2 !="null":
        t1=tt1+" = aws_iam_user."+tt2+".id\n"
        common.add_dependancy("aws_iam_user", tt2)
		
    return skip,t1,flag1,flag2

def aws_iam_group_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="group" and tt2 !="null":
		t1=tt1+" = aws_iam_group."+tt2+".id\n"
	return skip,t1,flag1,flag2

def aws_iam_group_policy_attachment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_iam_instance_profile(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_iam_openid_connect_provider(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="url":
		t1=tt1+" = \"https://"+tt2+"\"\n"
	return skip,t1,flag1,flag2

def aws_iam_policy(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "name":
        
        if len(tt2) > 0: flag1=True
    if tt1 == "name_prefix" and flag1 is True: skip=1
    if tt1 == "policy": t1=fixtf.globals_replace(t1,tt1,tt2)
  
    return skip,t1,flag1,flag2

def aws_iam_policy_attachment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_iam_policy_document(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_iam_principal_policy_simulation(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def  aws_iam_role(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "name":
        
        if len(tt2) > 0: 
            flag1=True
            flag2=tt2
    if tt1 == "name_prefix" and flag1 is True: skip=1
    if tt1 == "policy": t1=fixtf.globals_replace(t1,tt1,tt2)
    if tt1 == "assume_role_policy": t1=fixtf.globals_replace(t1,tt1,tt2)
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
    #        t1=fixtf.globals_replace(t1,tt1,tt2)
    return skip,t1,flag1,flag2

def aws_iam_role_policy(t1,tt1,tt2,flag1,flag2):
    skip=0
    #if tt1 == "role_name":
    #    t1=tt1 + " = aws_iam_role." + tt2 + ".id\n"
    #    common.add_dependancy("aws_iam_role",tt2)
  
    return skip,t1,flag1,flag2

def aws_iam_role_policy_attachment(t1,tt1,tt2,flag1,flag2):
    #print("fixit2.aws_iam_role_policy_attachment")
    skip=0
    #if tt1 == "role":
    #    
    #    t1=tt1 + " = aws_iam_role." + tt2 + ".id\n"
    #    common.add_dependancy("aws_iam_role",tt2)
    # skip as using policy arns minus account number etc..
    #if tt1 == "policy_arn": 
    #    
    #    tt2=str(tt2).split("/")[-1]
    #    t1=tt1 + " = aws_iam_policy." + str(tt2) + ".arn\n"
    if tt1 == "policy_arn": t1=fixtf.globals_replace(t1,tt1,tt2)

    return skip,t1,flag1,flag2

def aws_iam_saml_provider(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_iam_security_token_service_preferences(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_iam_server_certificate(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_iam_service_linked_role(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_iam_service_specific_credential(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_iam_session_context(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_iam_signing_certificate(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_iam_user_group_membership(t1,tt1,tt2,flag1,flag2):
    skip=0
    #print(t1)
    if tt1 == "user":
        t1=tt1+" = aws_iam_user."+tt2+".id\n"
        common.add_dependancy("aws_iam_user", tt2)
    elif tt1 == "groups":
        t1,skip = fixtf.deref_array(t1, tt1, tt2, "aws_iam_group", "", skip)

    elif tt1 == "groups":
        t1,skip = fixtf.deref_array(t1,tt1,tt2,"aws_iam_group","",skip)
    return skip,t1,flag1,flag2

def aws_iam_user_login_profile(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_iam_user_policy(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_iam_user_policy_attachment(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_iam_user_ssh_key(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_iam_user(t1,tt1,tt2,flag1,flag2):
    skip=0
    if tt1 == "name":
        #common.add_dependancy("aws_iam_access_key",tt2)
        common.add_dependancy("aws_iam_user_policy",tt2)
		
    return skip,t1,flag1,flag2

def aws_iam_users(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

def aws_iam_virtual_mfa_device(t1,tt1,tt2,flag1,flag2):
	skip=0
	return skip,t1,flag1,flag2

