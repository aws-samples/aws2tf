import common
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import os
import sys
import inspect

def get_aws_organizations_organization(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.describe_organization()

            if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j = response[topkey]
  
            common.write_import(type,j[key],None) 
            response2=[]
            try:
                response2=client.list_roots()

                if response2 == []: log.info("Empty response2 for list_roots id="+str(id)+" returning"); return True
                for j in response2['Roots']:
                    #common.add_known_dependancy("aws_organizations_policy", j[key])
                    common.add_known_dependancy("aws_organizations_organizational_unit", j['Id'])
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
            #fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                exn=str(exc_type.__name__)
                if exn == "AccessDeniedException":
                    log.info("Can't list_roots - no access or not a master account......")              
                    return True
                #else:
                #    print(f"{e=} [org1]")
                #    return True


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_organizations_organizational_unit(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            log.info("WARNING must pass parent org id as paremter returning ....")
            return True
        #try:
        response = client.list_organizational_units_for_parent(ParentId=id)
        #except Exception as e:
        #    print("No Org unit found returning True......")
        #    return True
        if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
        
        for j in response[topkey]:
            common.write_import(type, j[key], None)


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_organizations_policy(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        scpskip=True
        client = boto3.client(clfn)
        try:
            response = client.list_policies(Filter='SERVICE_CONTROL_POLICY')
        except Exception as e:
            log.info("No SCP Policies found ......")
            scpskip=False
            
        if scpskip:
            log.info("SCPs")
            if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                if "AWS" not in j[key]:
                    common.write_import(type,j[key],None) 
                    common.add_known_dependancy("aws_organizations_policy_attachment", j[key])

        response = []
        tagskip=True

        try:
            response = client.list_policies(Filter='TAG_POLICY')
        except Exception as e:
            log.info("No TAG Policies found ......")
            tagskip=False
        if tagskip:
            if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                #if "AWS" not in j[key]:
                    common.write_import(type,j[key],None) 
                    common.add_known_dependancy("aws_organizations_policy_attachment", j[key])

        response = []
        backskip=True

        try:
            response = client.list_policies(Filter='BACKUP_POLICY')
        except Exception as e:
            log.info("No Backup Policies found ......")
            backskip=False

        if backskip:    
            if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                #if "AWS" not in j[key]:
                    common.write_import(type,j[key],None)
                    common.add_known_dependancy("aws_organizations_policy_attachment", j[key])


        response = []
        aiskip=True

        try:
            response = client.list_policies(Filter='AISERVICES_OPT_OUT_POLICY')
        except Exception as e:
            log.info("No AI Policies found ......")
            aislip=False
        if aiskip:
            if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                #if "AWS" not in j[key]:
                    common.write_import(type,j[key],None)
                    common.add_known_dependancy("aws_organizations_policy_attachment", j[key])
        
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_organizations_account(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        try:
            response = client.list_accounts()
        except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
            #fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                exn=str(exc_type.__name__)
                if exn == "AccessDeniedException":
                    log.info("Can't list_accounts - no access or not a master account......")              
                    return True
                #else:
                #    print(f"{e=} [org1]")
                #    return True

        if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response[topkey]:
            common.write_import(type, j[key], None)   

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_organizations_resource_policy(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        try:
            response = client.describe_resource_policy()
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            #fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            exn=str(exc_type.__name__)
            if exn == "ResourcePolicyNotFoundException":
                log.info("No Resource Policies found - returning True ....")
                return True
            elif exn == "AccessDeniedException":
                    log.info("Can't describe_resource_policy - no access or not a master account......")              
                    return True
            #else:
            #    print(f"{e=} [org1]")
            #    print("No Org Resource Policy found returning True......")
            #    return True
        #print("RESPONSE2")
        #print(str(response))
        if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response[topkey]:
            common.write_import(type, j[key], None) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

#aws_organizations_policy_attachment
def get_aws_organizations_policy_attachment(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id.startswith("p-"):
            #print("--------->>>>>>>>>>ID="+id)
            try:
                response = client.list_targets_for_policy(PolicyId=id)
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                #fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                exn=str(exc_type.__name__)
                if exn == "ResourcePolicyNotFoundException":
                    log.info("No Resource Policy found - returning True ....")
                    return True
                elif exn == "AccessDeniedException":
                        log.info("Can't describe_resource_policy - no access or not a master account......")              
                        return True
                #else:
                #    print(f"{e=} [org1]")
                #    print("No Org Resource Policy found returning True......")

                #    return True
            #print("aws_organizations_policy_attachment response: "+str(response))
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                pkey=type+"."+id
                context.rproc[pkey]=True
                return True
            
            if id=="p-pj4vhztq":
                    log.info("J=",response)
            for j in response[topkey]:
                #print("J="+str(j))
                tid=j['TargetId']
                pkey=tid+":"+id

                common.write_import(type, pkey, id)            

        else:
            log.info("Must pass a policy id as a parmeter - returning True")


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True