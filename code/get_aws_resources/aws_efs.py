import common
from common import log_warning
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect
import sys,os


def get_aws_efs_file_system(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                common.write_import(type,j[key],None)  
                common.add_known_dependancy("aws_efs_mount_target",j[key]) 
                common.add_known_dependancy("aws_efs_access_point", j[key])
                common.add_known_dependancy("aws_efs_file_system_policy", j[key])
                common.add_known_dependancy("aws_efs_backup_policy", j[key])
                common.add_known_dependancy("aws_efs_replication_configuration", j[key])
                #common.add_known_dependancy("aws_efs_lifecycle_configuration", j[key])

        else: 
            if id.startswith("fs-"):     
                response = client.describe_file_systems(FileSystemId=id)
                if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
                for j in response[topkey]:
                    common.write_import(type,j[key],None)
                    common.add_known_dependancy("aws_efs_mount_target",j[key])
                    common.add_known_dependancy("aws_efs_access_point", j[key])
                    #common.add_known_dependancy("aws_efs_file_system_policy", j[key])
                    #common.add_known_dependancy("aws_efs_backup_policy", j[key])
                    common.add_known_dependancy("aws_efs_replication_configuration", j[key])
                    #common.add_known_dependancy("aws_efs_lifecycle_configuration", j[key])


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_efs_mount_target(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None: 

            log_warning("WARNING: Must pass parameter for get_aws_efs_mount_target"); return True
        else: 
            if id.startswith("fs-"):     
                response = client.describe_mount_targets(FileSystemId=id)
                if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
                for j in response[topkey]:
                    common.write_import(type,j[key],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_efs_access_point(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None: 

            log_warning("WARNING: Must pass parameter for get_aws_efs_mount_target"); return True
        else: 
            if id.startswith("fs-"):     
                response = client.describe_access_points(FileSystemId=id)
                if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
                for j in response[topkey]:
                    common.write_import(type,j[key],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_efs_replication_configuration(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None: 

            log_warning("WARNING: Must pass parameter for get_aws_efs_replication_configuration"); return True
        else: 
            if id.startswith("fs-"):   
                try:  
                    response = client.describe_replication_configurations(FileSystemId=id)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exn=str(exc_type.__name__)
                    if exn == "ReplicationNotFound":
                        if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                        return True
                if response == []: 
                    log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                    return True
                
                common.write_import(type,id,None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_efs_file_system_policy(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None: 
            log_warning("WARNING: Must pass parameter for get_aws_efs_file_system_policy"); return True
        else: 
            if id.startswith("fs-"):   
                try:  
                    response = client.describe_file_system_policy(FileSystemId=id)
                #except PolicyNotFound:
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exn=str(exc_type.__name__)
                    if exn == "PolicyNotFound":
                        if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                        return True
                if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
                
                common.write_import(type,id,None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_efs_backup_policy(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None: 
            log_warning("WARNING: Must pass parameter for get_aws_efs_replication_configuration"); return True
        else: 
            if id.startswith("fs-"):     
                try:
                    response = client.describe_backup_policy(FileSystemId=id)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    exn=str(exc_type.__name__)
                    if exn == "PolicyNotFound":
                        if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                        return True
                if response == []: 
                    log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                    return True
                
                common.write_import(type,id,None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_efs_lifecycle_configuration(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None: 
            log_warning("WARNING: Must pass parameter for get_aws_efs_replication_configuration"); return True
        else: 
            if id.startswith("fs-"):     
                response = client.describe_lifecycle_configuration(FileSystemId=id)
                if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
                
                common.write_import(type,id,None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True