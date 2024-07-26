import common
import boto3
import globals
import os
import sys
import inspect


def get_aws_sagemaker_domain(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_sagemaker_domain  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            # calls list_secrets
            response = client.list_domains()
            if response[topkey] == []:
                print("Empty response for "+type + " id="+str(id)+" returning")
                return True
            for j in response[topkey]:
                did = j['DomainId']
                common.write_import(type, did, None)
                common.add_dependancy("aws_sagemaker_user_profile", did)
                common.add_dependancy("aws_sagemaker_app", did)
        else:
            if id.startswith("d-"):
                j = client.describe_domain(DomainId=id)
                did = j['DomainId']
                common.write_import(type, did, None)
                common.add_dependancy("aws_sagemaker_user_profile", did)
                common.add_dependancy("aws_sagemaker_app", did)

    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True


def get_aws_sagemaker_notebook_instance(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_sagemaker_notebook_instance  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            # calls list_secrets
            paginator = client.get_paginator('list_notebook_instances')
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []:
                print("Empty response for "+type + " id="+str(id)+" returning")
                return True
            for j in response:
                common.write_import(type, j[key], None)

        else:
            response = client.describe_notebook_instance(
                NotebookInstanceName=id)
            if response == []:
                print("Empty response for "+type + " id="+str(id)+" returning")
                return True
            j = response
            common.write_import(type, j[key], None)

    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True


def get_aws_sagemaker_user_profile(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_sagemaker_notebook_instance  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            # calls list_secrets
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []:
                print("Empty response for "+type + " id="+str(id)+" returning")
                return True
            for j in response:
                k = client.describe_user_profile(
                    DomainId=j['DomainId'], UserProfileName=j['UserProfileName'])
                common.write_import(type, k['UserProfileArn'], None)

        elif id.startswith("d-"):
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(DomainIdEquals=id):
                response = response + page[topkey]
            if response == []:
                print("Empty response for "+type + " id="+str(id)+" returning")
                return True
            for j in response:
                k = client.describe_user_profile(
                    DomainId=j['DomainId'], UserProfileName=j['UserProfileName'])
                common.write_import(type, k['UserProfileArn'], None)
            pkey = "aws_sagemaker_user_profile."+id
            globals.rproc[pkey] = True

        else:
            if "/" in id:
                id0 = id.split("/")[0]
                id1 = id.split("/")[1]
                response = client.describe_user_profile(
                    DomainId=id0, UserProfileName=id1)
                if response == []:
                    print("Empty response for "+type +
                          " id="+str(id)+" returning")
                    return True
                j = response
                common.write_import(type, j['UserProfileArn'], None)
                pkey = "aws_sagemaker_user_profile."+id0
                globals.rproc[pkey] = True

    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True


def get_aws_sagemaker_app(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_sagemaker_notebook_instance  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            # calls list_secrets
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []:
                print("Empty response for "+type + " id="+str(id)+" returning")
                pkey="aws_sagemaker_app."+did
                return True
        elif id.startswith("d-"):
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(DomainIdEquals=id):
                response = response + page[topkey]
            if response == []:
                print("Empty response for "+type + " id="+str(id)+" returning")
                pkey="aws_sagemaker_app."+id
                globals.rproc[pkey]=True
                return True


        else:
            print("WARNING: must pass doamin id as parameter")
            return True

        for j in response:

            did = j['DomainId']
            appt = j['AppType']
            appn = j['AppName']
            print("did=",did,"appn=",appn)
            if appn == "default":
                pkey="aws_sagemaker_app."+did
                globals.rproc[pkey]=True
                continue
            upn = None
            spn = None
            try:
                upn = j['UserProfileName']
            except KeyError:
                upn = None

            try:
                spn = j['SpaceName']
            except KeyError:
                spn = None
            if spn is None:
                response = client.describe_app(
                    DomainId=did, AppType=appt, AppName=appn, UserProfileName=upn)
            if upn is None:
                response = client.describe_app(
                    DomainId=did, AppType=appt, AppName=appn, SpaceName=spn)
            k = response['AppArn']
            common.write_import(type, k, None)
            pkey="aws_sagemaker_app."+did
            globals.rproc[pkey]=True

        

    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True


def get_aws_sagemaker_project(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_sagemaker_project  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            # calls list_secrets
            response = client.list_projects()
            if response[topkey] == []:
                print("Empty response for "+type + " id="+str(id)+" returning")
                return True
            for j in response[topkey]:
                if j['ProjectStatus'] == "CreateCompleted":
                    common.write_import(type, j[key], None)

        else:
            response = client.describe_project(ProjectName=id)
            if response == []:
                print("Empty response for "+type + " id="+str(id)+" returning")
                return True
            j = response
            if j['ProjectStatus'] == "CreateCompleted":
                common.write_import(type, j[key], None)

    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True


def get_aws_sagemaker_space(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_sagemaker_project  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            # calls list_secrets
            response = client.list_spaces()
        else:
            if id.startswith("d-"):
                response = client.list_domains(DomainIdEquals=id)
            else:
                response = client.list_spaces(SpaceNameContains=id)
        if response[topkey] == []:
            print("Empty response for "+type + " id="+str(id)+" returning")
            return True
        for j in response[topkey]:
            spn = j['SpaceName']
            did = j['DomainId']
            response2 = client.describe_space(DomainId=did, SpaceName=spn)
            sparn = response2['SpaceArn']
            if sparn == "":
                print("Empty response for "+type + " id="+str(id)+" returning")
                return True
            common.write_import(type, sparn, None)

    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True



def get_aws_sagemaker_image(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_sagemaker_image_version  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []:
                print("Empty response for "+type + " id="+str(id)+" returning")
                pkey="aws_sagemaker_image."+id
                return True
            for j in response:
                common.write_import(type, j[key], None)# calls list_secrets
                common.add_dependancy("aws_sagemaker_image_version",j[key])
            
        else:
            response = client.describe_image(ImageName=id)
            if response == []:
                print("Empty response for "+type + " id="+str(id)+" returning")
                pkey="aws_sagemaker_image_version."+id
                common.write_import(type, id, None)
                globals.rproc[pkey]=True
            j=response[key]
            common.write_import(type, j, None)# calls list_secrets
            common.add_dependancy("aws_sagemaker_image_version",j)


    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True







def get_aws_sagemaker_image_version(type, id, clfn, descfn, topkey, key, filterid):
    #if globals.debug:
    print("--> In get_aws_sagemaker_image_version  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            # calls list_secrets
            print("WARNING: Must pass image id as parameter")
        else:
            response = client.list_image_versions(ImageName=id)
            if response == []:
                print("Empty response for "+type + " id="+str(id)+" returning")
                return True
            pkey="aws_sagemaker_image_version."+id
            common.write_import(type, id, None)
            print("************",pkey)
            globals.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True
