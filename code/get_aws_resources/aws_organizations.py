import common
from common import log_warning
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

            if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j = response[topkey]

            # describe_organization works from any member account, but terraform reads this
            # resource with list_roots/list_accounts - importing it without those fails the plan
            response2=[]
            try:
                response2=client.list_roots()
                client.list_accounts()
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
            #fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                exn=str(exc_type.__name__)
                if exn == "AccessDeniedException":
                    log.info("Can't read organization - no access or not a master account......")
                    return True
                #else:
                #    print(f"{e=} [org1]")
                #    return True

            common.write_import(type,j[key],None)

            if response2 == []: log.info("Empty response2 for list_roots id="+str(id)+" returning"); return True
            for j in response2['Roots']:
                #common.add_known_dependancy("aws_organizations_policy", j[key])
                common.add_known_dependancy("aws_organizations_organizational_unit", j['Id'])


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
            log_warning("WARNING must pass parent org id as paremter returning ....")
            return True

        # Use paginator to handle >20 child OUs
        paginator = client.get_paginator('list_organizational_units_for_parent')
        for page in paginator.paginate(ParentId=id):
            for j in page[topkey]:
                common.write_import(type, j[key], None)
                # Recurse into child OUs to discover nested OUs
                get_aws_organizations_organizational_unit(type, j[key], clfn, descfn, topkey, key, filterid)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_organizations_policy(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        client = boto3.client(clfn)

        policy_types = [
            ('SERVICE_CONTROL_POLICY', 'SCP'),
            ('TAG_POLICY', 'TAG'),
            ('BACKUP_POLICY', 'Backup'),
            ('AISERVICES_OPT_OUT_POLICY', 'AI'),
        ]

        for policy_filter, label in policy_types:
            try:
                paginator = client.get_paginator('list_policies')
                for page in paginator.paginate(Filter=policy_filter):
                    for j in page[topkey]:
                        # Skip AWS-managed SCPs (e.g. p-FullAWSAccess)
                        if policy_filter == 'SERVICE_CONTROL_POLICY' and "AWS" in j[key]:
                            continue
                        common.write_import(type, j[key], None)
                        common.add_known_dependancy("aws_organizations_policy_attachment", j[key])
            except Exception as e:
                log.info("No %s Policies found ......", label)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_organizations_account(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        client = boto3.client(clfn)
        try:
            paginator = client.get_paginator('list_accounts')
            for page in paginator.paginate():
                for j in page[topkey]:
                    common.write_import(type, j[key], None)
        except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                exn=str(exc_type.__name__)
                if exn == "AccessDeniedException":
                    log.info("Can't list_accounts - no access or not a management account......")
                    return True
                else:
                    raise

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
                log.debug("No Resource Policies found - returning True ....")
                return True
            elif exn == "AccessDeniedException":
                    log.info("Can't describe_resource_policy - no access or not a master account......")              
                    return True
            #else:
            #    print(f"{e=} [org1]")
            #    print("No Org Resource Policy found returning True......")
            #    return True
        if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
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
        client = boto3.client(clfn)
        if id.startswith("p-"):
            try:
                # Use paginator to handle policies attached to many targets (>20)
                paginator = client.get_paginator('list_targets_for_policy')
                found = False
                for page in paginator.paginate(PolicyId=id):
                    for j in page[topkey]:
                        found = True
                        tid=j['TargetId']
                        pkey=tid+":"+id
                        # Pass None as tfid so resource names auto-derive from pkey,
                        # producing unique names per target (avoids overwrites)
                        common.write_import(type, pkey, None)

                if not found:
                    if context.debug: log.debug("No targets for policy "+str(id)+" returning")
                    pkey=type+"."+id
                    context.rproc[pkey]=True

            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                exn=str(exc_type.__name__)
                if exn == "ResourcePolicyNotFoundException":
                    log.debug("No Resource Policy found - returning True ....")
                    return True
                elif exn == "AccessDeniedException":
                    log.info("Can't list_targets_for_policy - no access or not a management account......")
                    return True
                else:
                    raise

        else:
            log.debug("Must pass a policy id as a parameter - returning True")


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True