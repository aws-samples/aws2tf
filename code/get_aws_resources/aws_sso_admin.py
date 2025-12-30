import common
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect

def get_aws_ssoadmin_instances(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:

        with open("data__aws_sso_admin_instances.tf", "w") as f:
            f.write("data \"aws_ssoadmin_instances\" \"sso\" {}\n")
        log.debug("Running terraform refresh")
        com = "terraform refresh -no-color -target=data.aws_ssoadmin_instances.sso > /dev/null"
        rout = common.rc(com) 
        com="terraform state show -no-color data.aws_ssoadmin_instances.sso | grep :instance"
        rout = common.rc(com) 
        ins=rout.stdout.decode().strip().strip('\"').strip(",").replace('"', '')
        log.debug("SSO Instance=%s", ins)
        context.ssoinstance=ins
        common.add_known_dependancy("aws_ssoadmin_permission_set",ins)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

#aws_ssoadmin_permission_set

def get_aws_ssoadmin_permission_set(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        if id is None and context.ssoinstance is None: 
            log.debug("No SSO instance found")
            return True
        if id =="":
            log.debug("No SSO instance found")
            return True
        if id == context.ssoinstance: id=context.ssoinstance
        if context.ssoinstance is not None: id=context.ssoinstance
        response = []
        client = boto3.client(clfn)    
        response = client.list_permission_sets(InstanceArn=id)
        if response == []: 
            if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
            return True
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
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        # id - instid arm /perm arn
        if id is None: log.debug("No SSO instance found"); return True
        if "," not in id: log.debug("No SSO instance found"); return True

        response = []
        client = boto3.client(clfn)  
        inid=id.split(",")[1]; psarn=id.split(",")[0] 
        response = client.list_managed_policies_in_permission_set(InstanceArn=inid,PermissionSetArn=psarn)
        if response == []: 
            if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
            rkey=type+"."+psarn+","+inid
            context.rproc[rkey] = True
            return True
        for j in response['AttachedManagedPolicies']:
            mparn=j['Arn']
            pkey=mparn+","+psarn+","+inid
            theid=pkey.replace(",", "_")
            common.write_import(type,pkey,theid)
        rkey=type+"."+psarn+","+inid
        context.rproc[rkey] = True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_ssoadmin_permission_set_inline_policy(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        # id - instid arm /perm arn
        if id is None: 
            log.debug("No SSO instance found")
            return True
        if "/" not in id: 
            log.debug("No SSO instance found") 
            return True

        response = []
        client = boto3.client(clfn)  
        inid=id.split(",")[1]; psarn=id.split(",")[0]  
        response = client.get_inline_policy_for_permission_set(InstanceArn=inid,PermissionSetArn=psarn)
        if response == []: 
            if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
            rkey=type+"."+psarn+","+inid
            context.rproc[rkey] = True
            return True

        j=response['InlinePolicy']
        if j == {}: 
            log.info("Empty inline policy [1] for "+type+ " id="+str(id)+" returning")
            rkey=type+"."+psarn+","+inid
            context.rproc[rkey] = True
            return True
        if len(j) < 4: 
            log.info("Empty inline policy [2] for "+type+ " id="+str(id)+" returning")
            rkey=type+"."+psarn+","+inid
            context.rproc[rkey] = True
            return True
        pkey=psarn+","+inid

        theid=pkey.replace(",", "_")
        common.write_import(type,pkey,theid)
        rkey=type+"."+psarn+","+inid
        context.rproc[rkey] = True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True