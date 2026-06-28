import common
from common import log_warning
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect
import botocore
import inspect
import sys
from botocore.config import Config
from botocore.exceptions import ClientError

def get_aws_db_snapshot(type, id, clfn, descfn, topkey, key, filterid):
    # Only MANUAL snapshots are importable as aws_db_snapshot. describe_db_snapshots
    # also returns automated ("rds:" prefix) and AWS Backup ("awsbackup:" prefix)
    # snapshots, which are service-managed and fail import with
    # "Cannot import non-existent remote object".
    if context.debug:
        log.debug("--> In get_aws_db_snapshot doing " + type + ' with id ' + str(id))
    try:
        response = []
        client = boto3.client(clfn)
        paginator = client.get_paginator(descfn)
        for page in paginator.paginate():
            response = response + page[topkey]
        if response == []:
            log.debug("Empty response for "+type+" id="+str(id)+" returning"); return True
        for j in response:
            if j.get('SnapshotType') != 'manual':
                continue
            if id is None or id == j.get(filterid):
                common.write_import(type, j[key], None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True


def get_aws_db_instance_automated_backups_replication(type, id, clfn, descfn, topkey, key, filterid):
    # aws_db_instance_automated_backups_replication manages *cross-region*
    # automated-backup replication. describe_db_instance_automated_backups returns
    # both local backups and replicas, and its read uses the
    # DB_INSTANCE_AUTOMATED_BACKUPS_ARN filter - so the import id must be the
    # automated-backup ARN (...:auto-backup:ab-...), NOT the db instance ARN. A
    # local backup (source region == current region) is part of the db_instance and
    # is not a replication resource, so only emit genuine cross-region replicas.
    if context.debug:
        log.debug("--> In get_aws_db_instance_automated_backups_replication doing " + type + ' with id ' + str(id))
    try:
        response = []
        client = boto3.client(clfn)
        paginator = client.get_paginator(descfn)
        for page in paginator.paginate():
            response = response + page[topkey]
        if response == []:
            log.debug("Empty response for "+type+" id="+str(id)+" returning"); return True
        for j in response:
            bkarn = j.get('DBInstanceAutomatedBackupsArn')
            srcarn = j.get('DBInstanceArn', '') or ''
            src_region = srcarn.split(':')[3] if srcarn.count(':') >= 4 else ''
            if bkarn and src_region and src_region != context.region:
                common.write_import(type, bkarn, None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True


def get_aws_db_parameter_group(type, id, clfn, descfn, topkey, key, filterid):


    if context.debug:
        log.debug("--> In get_aws_db_parameter_group  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        ## id filter here
   
        paginator = client.get_paginator(descfn)
        for page in paginator.paginate():
                response = response + page[topkey]
        if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response:
            if id is None:
                common.write_import(type,j[key],None) 
            else:
                if "default." not in id: 
                    did="default."+id
                if did==j[key]: 
                    common.write_import(type,j[key],None)
                else:
                    if id==j[key]:
                        common.write_import(type,j[key],None)

   

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_db_option_group(type, id, clfn, descfn, topkey, key, filterid):


    if context.debug:
        log.debug("--> In get_aws_db_option_group  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        ## id filter here
   
        paginator = client.get_paginator(descfn)
        for page in paginator.paginate():
                response = response + page[topkey]
        if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response:
            if id is None:
                if "default:" not in j[key]:
                    common.write_import(type,j[key],None) 
            else:
                if "default:" not in id:  
                    if id==j[key]:
                        common.write_import(type,j[key],None)

   

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


#aws_db_subnet_group

def get_aws_db_subnet_group(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    
    try:
        response = []
        client = boto3.client(clfn)
        ## id filter here
   
        paginator = client.get_paginator(descfn)
        for page in paginator.paginate():
                response = response + page[topkey]
        if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True

        for j in response:
            if id is None:
                if "default" != j[key]:
                    common.write_import(type,j[key],None) 
            else:
                if "default" != id:  
                    if id==j[key]:
                        common.write_import(type,j[key],None)
                else:
                    pkey="aws_db_subnet_group."+id
                    context.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

# aws_rds_custom_db_engine_version


def get_aws_rds_custom_db_engine_version(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        paginator = client.get_paginator(descfn)
        if id is None: 
            for page in paginator.paginate():
                response = response + page[topkey]
        else:
            for page in paginator.paginate(Engine=id):
                response = response + page[topkey]

        if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response:
            eng=j['Engine']
            engv=j['EngineVersion']
            pkey=eng+":"+engv
            common.write_import(type,pkey,None) 



    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


#aws_db_event_subscription#

def get_aws_db_event_subscription(type, id, clfn, descfn, topkey, key, filterid):
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

        else:      
            response = client.describe_event_subscriptions(SubscriptionName=id)
            if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                common.write_import(type,j[key],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


# aws_db_instance


def get_aws_db_instance(type, id, clfn, descfn, topkey, key, filterid):
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
                engine=j['Engine']
                if engine=="docdb" or engine.startswith("aurora"): continue
                common.write_import(type, j[key], None)

        else:
            response = client.describe_db_instances(DBInstanceIdentifier=id)
            if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                engine=j['Engine']
                if engine=="docdb" or engine.startswith("aurora"): continue
                common.write_import(type, j[key], None)

    except client.exceptions.InvalidParameterValue as error:
            log_warning("WARNING: InvalidParameterValue for "+type+ " "+str(id)+" returning")
            log.debug(str(error.response['Error']['Code']))
            pkey=type+"."+str(id)
            context.rproc[pkey]=True
            return True
    
    
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True

def get_aws_rds_cluster_instance(type, id, clfn, descfn, topkey, key, filterid):
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
                engine=j['Engine']
                if engine.startswith("aurora"): 
                    common.write_import(type, j[key], None)
                    pkey=type+"."+j[key]
                    context.rproc[pkey]=True
                    
                else:
                    continue
            

        else:
            response = client.describe_db_instances(DBInstanceIdentifier=id)
            if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                engine=j['Engine']
                if engine.startswith("aurora"):
                    common.write_import(type, j[key], None)
                    pkey=type+"."+j[key]
                    context.rproc[pkey]=True
                else:
                    continue

    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True

def get_aws_rds_cluster(type, id, clfn, descfn, topkey, key, filterid):
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
                engine=j['Engine']
                if engine.startswith("aurora"): 
                    common.write_import(type, j[key], None)
                    pkey=type+"."+j[key]
                    context.rproc[pkey]=True
                    
                else:
                    continue
            

        else:
            response = client.describe_db_clusters(DBClusterIdentifier=id)
            if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                engine=j['Engine']
                if engine.startswith("aurora"):
                    common.write_import(type, j[key], None)
                    pkey=type+"."+j[key]
                    context.rproc[pkey]=True
                else:
                    continue

    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True