import common
import boto3
import globals
import os
import sys
import inspect


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
            else:
                print("Warning: Must pass domain id / user profile name for "+type)

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
                return True
            for j in response:
                if j[key] != "default":
                    common.write_import(type, j[key], None)

        else:
            response = client.list_apps(DomainId=id)
            if response == []:
                print("Empty response for "+type + " id="+str(id)+" returning")
                return True
            j = response
            if j[key] != "default":
                common.write_import(type, j[key], None)

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
