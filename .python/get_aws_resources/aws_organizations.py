import common
import boto3
import globals
import os
import sys
import inspect

def get_aws_organizations_organization(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.describe_organization()

            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j = response[topkey]
  
            common.write_import(type,j[key],None) 
            response2=[]
            try:
                response2=client.list_roots()

                if response2 == []: print("Empty response2 for list_roots id="+str(id)+" returning"); return True
                for j in response2['Roots']:
                    #common.add_known_dependancy("aws_organizations_policy", j[key])
                    common.add_known_dependancy("aws_organizations_organizational_unit", j['Id'])
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
            #fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                exn=str(exc_type.__name__)
                if exn == "AccessDeniedException":
                    print("Can't list_roots - no access or not a master account......")              
                    return True
                else:
                    print(f"{e=} [org1]")
                    return True


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_organizations_organizational_unit(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            print("WARNING must pass parent org id as paremter returning ....")
            return True
        #try:
        response = client.list_organizational_units_for_parent(ParentId=id)
        #except Exception as e:
        #    print("No Org unit found returning True......")
        #    return True
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        
        for j in response[topkey]:
            common.write_import(type, j[key], None)


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_organizations_policy(type, id, clfn, descfn, topkey, key, filterid):
    #if globals.debug:
    print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        try:
            response = client.list_policies(Filter='SERVICE_CONTROL_POLICY')
        except Exception as e:
            print("No Policy found returning True......")
            return True
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response[topkey]:
            if "AWS" not in j[key]:
                common.write_import(type,j[key],None) 

        try:
            response = client.list_policies(Filter='TAG_POLICY')
        except Exception as e:
            print("No Policy found returning True......")
            return True
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response[topkey]:
            #if "AWS" not in j[key]:
                common.write_import(type,j[key],None) 

        try:
            response = client.list_policies(Filter='BACKUP_POLICY')
        except Exception as e:
            print("No Policy found returning True......")
            return True
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response[topkey]:
            #if "AWS" not in j[key]:
                common.write_import(type,j[key],None)

        try:
            response = client.list_policies(Filter='AISERVICES_OPT_OUT_POLICY')
        except Exception as e:
            print("No Policy found returning True......")
            return True
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response[topkey]:
            #if "AWS" not in j[key]:
                common.write_import(type,j[key],None)
        



    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_organizations_account(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
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
                    print("Can't list_accounts - no access or not a master account......")              
                    return True
                else:
                    print(f"{e=} [org1]")
                    return True

        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response[topkey]:
            common.write_import(type, j[key], None) 


        

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_organizations_resource_policy(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
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
                print("No Resource Policy found - returning True ....")
                return True
            elif exn == "AccessDeniedException":
                    print("Can't describe_resource_policy - no access or not a master account......")              
                    return True
            else:
                print(f"{e=} [org1]")
                print("No Org Resource Policy found returning True......")
                return True
        print("RESPONSE2")
        print(str(response))
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response[topkey]:
            common.write_import(type, j[key], None) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True