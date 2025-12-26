import common
from common import log_warning
import logging
log = logging.getLogger('aws2tf')
import boto3
from botocore.config import Config
import context
import inspect

# aws_msk_cluster arn
def get_aws_msk_cluster(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn,config=config)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            for j in response:
                if j['ClusterType']=='PROVISIONED' and j['State']=="ACTIVE":
                    common.write_import(type,j[key],None) 
                    common.add_dependancy("aws_msk_cluster_policy",j[key])
                    common.add_dependancy("aws_msk_scram_secret_association",j[key])

        else:      
            response = client.describe_cluster_v2(ClusterArn=id)
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            j=response['ClusterInfo']
            if j['ClusterType']=='PROVISIONED' and j['State']=="ACTIVE":
                common.write_import(type, j[key], None)
                common.add_dependancy("aws_msk_cluster_policy", j[key])
                common.add_dependancy("aws_msk_scram_secret_association", j[key])

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

# aws_msk_configuration config arn
def get_aws_msk_configuration(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10, 'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []:
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                common.write_import(type, j[key], None)

        else:
            response = client.describe_configuration(Arn=id)
            if response == []:
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            j=response
            common.write_import(type, j[key], None)

    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True

# aws_msk_cluster_policy cluster arn
def get_aws_msk_cluster_policy(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10, 'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        if id is None:
            log_warning("WARNING: Must pass Cluster arn as parameter")
            return True

        else:
            if id.startswith("arn:"):
                pkey=type+"."+id
                response = client.get_cluster_policy(ClusterArn=id)
                if response == []:
                    if context.debug: 
                        log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                        context.rproc[pkey]=True
                        return True
                j=response
                common.write_import(type, id, None)
                context.rproc[pkey]=True
                
            else:
                log_warning("WARNING: Must pass Cluster arn as parameter")
                return True

    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True


# aws_msk_vpc_connection  vpc cnx arn

# aws_msk_serverless_cluster arn
def get_aws_msk_serverless_cluster(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10, 'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []:
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                if j['ClusterType']=='SERVERLESS'and j['State']=="ACTIVE": 
                    common.write_import(type, j[key], None)

        else:
            if id.startswith("arn:"):
                pkey=type+"."+id
                response = client.describe_cluster_v2(ClusterArn=id)
                if response == []:
                    if context.debug:
                        log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                        context.rproc[pkey]=True
                        return True
                j=response['ClusterInfo']
                if j['ClusterType']=='SERVERLESS' and j['State']=="ACTIVE":
                    common.write_import(type, j[key], None)
                context.rproc[pkey]=True

            else:
                log_warning("WARNING: Must pass Cluster arn as parameter")
                return True


    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True

# aws_msk_replicator   rep arn 

# aws_msk_scram_secret_association id or arn ?
def get_aws_msk_scram_secret_association(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10, 'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        if id is None:
            log_warning("WARNING: Must pass Cluster arn as parameter")
            return True

        else:
            if id.startswith("arn:"):
                pkey=type+"."+id
                response = client.list_scram_secrets(ClusterArn=id)
                if response == []:
                    if context.debug: 
                        log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                        context.rproc[pkey]=True
                        return True
                for j in response['SecretArnList']:
                    theid=id
                    common.write_import(type, id, None)
                context.rproc[pkey]=True
            else:
                log_warning("WARNING: Must pass Cluster arn as parameter")
                return True

    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True

