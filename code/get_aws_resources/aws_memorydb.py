#!/usr/bin/env python3
import logging
log = logging.getLogger('aws2tf')
import boto3
import common
import context
import inspect
from botocore.config import Config


def get_aws_memorydb_subnet_group(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            paginator = client.get_paginator(descfn)
            response = []
            for page in paginator.paginate():
                response.extend(page[topkey])
            for j in response:
                common.write_import(type, j[key], None)
        else:
            response = client.describe_subnet_groups(SubnetGroupName=id)
            if response[topkey]:
                common.write_import(type, id, None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True


def get_aws_memorydb_parameter_group(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            paginator = client.get_paginator(descfn)
            response = []
            for page in paginator.paginate():
                response.extend(page[topkey])
            for j in response:
                common.write_import(type, j[key], None)
        else:
            response = client.describe_parameter_groups(ParameterGroupName=id)
            if response[topkey]:
                common.write_import(type, id, None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True


def get_aws_memorydb_user(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            paginator = client.get_paginator(descfn)
            response = []
            for page in paginator.paginate():
                response.extend(page[topkey])
            for j in response:
                common.write_import(type, j[key], None)
        else:
            response = client.describe_users(UserName=id)
            if response[topkey]:
                common.write_import(type, id, None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True


def get_aws_memorydb_acl(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            paginator = client.get_paginator(descfn)
            response = []
            for page in paginator.paginate():
                response.extend(page[topkey])
            for j in response:
                common.write_import(type, j[key], None)
        else:
            response = client.describe_acls(ACLName=id)
            if response[topkey]:
                common.write_import(type, id, None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True


def get_aws_memorydb_cluster(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            paginator = client.get_paginator(descfn)
            response = []
            for page in paginator.paginate():
                response.extend(page[topkey])
            for j in response:
                common.write_import(type, j[key], None)
        else:
            response = client.describe_clusters(ClusterName=id)
            if response[topkey]:
                common.write_import(type, id, None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True


def get_aws_memorydb_snapshot(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            paginator = client.get_paginator(descfn)
            response = []
            for page in paginator.paginate():
                response.extend(page[topkey])
            for j in response:
                common.write_import(type, j[key], None)
        else:
            response = client.describe_snapshots(SnapshotName=id)
            if response[topkey]:
                common.write_import(type, id, None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True


def get_aws_memorydb_multi_region_cluster(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            paginator = client.get_paginator(descfn)
            response = []
            for page in paginator.paginate():
                response.extend(page[topkey])
            for j in response:
                common.write_import(type, j[key], None)
        else:
            response = client.describe_multi_region_clusters(MultiRegionClusterName=id)
            if response[topkey]:
                common.write_import(type, id, None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True
