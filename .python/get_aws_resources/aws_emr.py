import common
import boto3
import globals
import inspect
import sys


def get_aws_emr_cluster(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []:
                if globals.debug: print("Empty response for "+type + " id="+str(id)+" returning")
                return True
            for j in response:
                if "TERMINATED" not in j['Status']['State']:
                    # print(str(j))
                    common.write_import(type, j[key], None)
                    common.add_dependancy("aws_emr_instance_group", j[key])
                    common.add_dependancy("aws_emr_instance_fleet", j[key])
                    common.add_dependancy(
                        "aws_emr_managed_scaling_policy", j[key])
                    common.add_dependancy(
                        "aws_emr_block_public_access_configuration", "current")

        else:
            response = client.describe_cluster(ClusterId=id)
            if response == []:
                if globals.debug: print("Empty response for "+type + " id="+str(id)+" returning")
                return True
            j = response['Cluster']
            # print(str(j))
            if "TERMINATED" not in j['Status']['State']:
                common.write_import(type, j[key], None)
                common.add_dependancy("aws_emr_instance_group", j[key])
                common.add_dependancy("aws_emr_instance_fleet", j[key])
                common.add_dependancy("aws_emr_managed_scaling_policy", j[key])
                common.add_dependancy(
                    "aws_emr_block_public_access_configuration", "current")

    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True

# aws_emr_security_configuration


def get_aws_emr_security_configuration(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []:
                if globals.debug: print("Empty response for "+type + " id="+str(id)+" returning")
                return True
            for j in response:
                common.write_import(type, j[key], None)

        else:
            response = client.describe_security_configuration(Name=id)
            if response == []:
                if globals.debug: print("Empty response for "+type + " id="+str(id)+" returning")
                return True
            j = response
            # print(str(j))
            common.write_import(type, j[key], None)

    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True


# aws_emr_instance_group
def get_aws_emr_instance_group(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            print("WARNING: Muse pass cluster is as parameter returning")
            return True
        else:
            try:
                response = client.list_instance_groups(ClusterId=id)
                if response == []:
                    if globals.debug: print("Empty response for "+type +
                          " id="+str(id)+" returning")
                    pkey = type+"."+id
                    globals.rproc[pkey] = True
                    return True
                for j in response['InstanceGroups']:
                    pkey = id+"/"+j[key]
                    # print(str(j))
                    common.write_import(type, pkey, None)
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                exn = str(exc_type.__name__)
                if exn == "InvalidRequestException":
                    if globals.debug: print("Empty response for "+type +
                          " id="+str(id)+" returning")
                    pkey = type+"."+id
                    globals.rproc[pkey] = True
                    return True

            pkey = type+"."+id
            globals.rproc[pkey] = True

    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True



# aws_emr_instance_group
def get_aws_emr_instance_fleet(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            print("WARNING: Muse pass cluster is as parameter returning")
            return True
        else:
            try:
                response = client.list_instance_fleets(ClusterId=id)
                if response == []:
                    if globals.debug: print("Empty response for "+type +
                          " id="+str(id)+" returning")
                    pkey = type+"."+id
                    globals.rproc[pkey] = True
                    return True
                for j in response['InstanceFleets']:
                    pkey = id+"/"+j[key]
                    # print(str(j))
                    common.write_import(type, pkey, None)
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                exn = str(exc_type.__name__)
                if exn == "InvalidRequestException":
                    if globals.debug: print("Empty response for "+type +
                          " id="+str(id)+" returning")
                    pkey = type+"."+id
                    globals.rproc[pkey] = True
                    return True

            pkey = type+"."+id
            globals.rproc[pkey] = True

    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True




# aws_emr_managed_scaling_policy


def get_aws_emr_managed_scaling_policy(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        
        client = boto3.client(clfn)
        if id is None:
            print("WARNING: Must pass cluster is as parameter returning")
            return True

        else:
            pkey = type+"."+id
            response = client.get_managed_scaling_policy(ClusterId=id)
            try:
                j = response['ManagedScalingPolicy']
            except KeyError as e:
                if globals.debug: print("Empty response for "+type + " id="+str(id)+" returning")
                globals.rproc[pkey] = True
                return True
            common.write_import(type, id, None)
            globals.rproc[pkey] = True

    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True


def get_aws_emr_block_public_access_configuration(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        id = "current"
        pkey = type+"."+id

        response = []
        client = boto3.client(clfn)
        response = client.get_block_public_access_configuration()
        try:
                j = response['BlockPublicAccessConfiguration']
        except KeyError as e:
                if globals.debug: print("Empty response for "+type + " id="+str(id)+" returning")
                globals.rproc[pkey] = True
                return True
        common.write_import(type, id, None)
        globals.rproc[pkey] = True

    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey,id)

    return True
