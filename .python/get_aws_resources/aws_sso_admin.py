import common
import boto3
import globals
import inspect

def get_aws_ssoadmin_instances(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:

        with open("data__aws_sso_admin_instances.tf", "w") as f:
            f.write("data \"aws_ssoadmin_instances\" \"sso\" {}\n")
        print("Running terraform refresh")
        com = "terraform refresh -no-color -target=data.aws_ssoadmin_instances.sso > /dev/null"
        rout = common.rc(com) 
        #print(rout.stdout.decode().rstrip())
        #print("Running state show")
        com="terraform state show -no-color data.aws_ssoadmin_instances.sso | grep :instance"
        rout = common.rc(com) 
        ins=rout.stdout.decode().strip().strip('\"').strip(",").replace('"', '')
        print("SSO Instance=",ins)
        globals.ssoinstance=ins
        common.add_known_dependancy("aws_ssoadmin_permission_set",ins)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

#aws_ssoadmin_permission_set

def get_aws_ssoadmin_permission_set(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        if id is None and globals.ssoinstance is None: print("No SSO instance found"); return True
        if id == globals.ssoinstance: id=globals.ssoinstance
        if globals.ssoinstance is not None: id=globals.ssoinstance
        response = []
        client = boto3.client(clfn)    
        response = client.list_permission_sets(InstanceArn=id)
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response['PermissionSets']:
            pkey=j+","+id
            theid=pkey.replace(",", "_")
            common.write_import(type,pkey,theid)
            common.add_dependancy("aws_ssoadmin_managed_policy_attachment", pkey)
            common.add_dependancy("aws_ssoadmin_permission_set_inline_policy", pkey)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_ssoadmin_managed_policy_attachment(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        # id - instid arm /perm arn
        if "," not in id: print("No SSO instance found"); return True

        response = []
        client = boto3.client(clfn)  
        inid=id.split(",")[1]; psarn=id.split(",")[0] 
        print("id="+id)
        response = client.list_managed_policies_in_permission_set(InstanceArn=inid,PermissionSetArn=psarn)
        if response == []: 
            print("Empty response for "+type+ " id="+str(id)+" returning")
            rkey=type+"."+psarn+","+inid
            globals.rproc[rkey] = True
            return True
        for j in response['AttachedManagedPolicies']:
            mparn=j['Arn']
            print("----->>>>>> mparn="+mparn)
            pkey=mparn+","+psarn+","+inid
            theid=pkey.replace(",", "_")
            common.write_import(type,pkey,theid)
        rkey=type+"."+psarn+","+inid
        globals.rproc[rkey] = True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_ssoadmin_permission_set_inline_policy(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        # id - instid arm /perm arn
        if "/" not in id: print("No SSO instance found"); return True

        response = []
        client = boto3.client(clfn)  
        inid=id.split(",")[1]; psarn=id.split(",")[0]  
        response = client.get_inline_policy_for_permission_set(InstanceArn=inid,PermissionSetArn=psarn)
        if response == []: 
            print("Empty response for "+type+ " id="+str(id)+" returning")
            rkey=type+"."+psarn+","+inid
            globals.rproc[rkey] = True
            return True

        j=response['InlinePolicy']
        if j == {}: 
            print("Empty inline policy [1] for "+type+ " id="+str(id)+" returning")
            rkey=type+"."+psarn+","+inid
            globals.rproc[rkey] = True
            return True
        if len(j) < 4: 
            print("Empty inline policy [2] for "+type+ " id="+str(id)+" returning")
            rkey=type+"."+psarn+","+inid
            globals.rproc[rkey] = True
            return True
        pkey=psarn+","+inid

        theid=pkey.replace(",", "_")
        common.write_import(type,pkey,theid)
        rkey=type+"."+psarn+","+inid
        globals.rproc[rkey] = True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True