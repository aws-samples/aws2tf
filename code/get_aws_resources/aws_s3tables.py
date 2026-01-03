import common
from common import log_warning
import logging
log = logging.getLogger('aws2tf')
import boto3
from botocore.config import Config
import context
import inspect

def get_aws_s3tables_table_bucket(type, id, clfn, descfn, topkey, key, filterid):
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
                common.write_import(type,j[key],None) 
                common.add_known_dependancy("aws_s3tables_namespace",j[key])

        else:      
            response = client.get_table_bucket(tableBucketARN=id)
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            j=response
            common.write_import(type,j[key],None)
            common.add_known_dependancy("aws_s3tables_namespace",j[key])

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_s3tables_namespace(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn,config=config)
        if id is None:
            log_warning("WARNING: must pass table bucket ARN as parameter")
            return True

        else:      
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(tableBucketARN=id):
                response = response + page[topkey]
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
                pkey=type+"."+id
                context.rproc[pkey]=True
                return True
            for j in response:
                for k in j[key]:
                    theid=id+";"+k
                    common.write_import(type,theid,None) 
                    common.add_dependancy("aws_s3tables_table", theid)
            pkey=type+"."+id
            context.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_s3tables_table(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn,config=config)
        if id is None:
            log_warning("WARNING: must pass table bucket ARN and namespace as parameters")
            return True

        else:   
            if ";" not in id:
                log_warning("WARNING: must pass table bucket ARN and namespace as parameters")
                return True  
            barn=id.split(";")[0]
            namespace=id.split(";")[1] 
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(tableBucketARN=barn,namespace=namespace):
                response = response + page[topkey]
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
                pkey=type+"."+id
                context.rproc[pkey]=True
                return True
            for j in response:
                theid=id+";"+j[key]
                common.write_import(type,theid,None) 
            pkey=type+"."+id
            context.rproc[pkey]=True
            

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_s3tables_table_bucket_replication(type, id, clfn, descfn, topkey, key, filterid):
    try:
        from botocore.config import Config
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all table buckets first
            paginator = client.get_paginator('list_table_buckets')
            buckets = []
            for page in paginator.paginate():
                buckets = buckets + page['tableBuckets']
            
            # Then try to get replication config for each bucket
            for bucket in buckets:
                bucket_arn = bucket['arn']
                try:
                    response = client.get_table_bucket_replication(tableBucketARN=bucket_arn)
                    # Replication exists for this bucket
                    common.write_import(type, bucket_arn, None)
                except client.exceptions.NotFoundException:
                    # No replication for this bucket
                    if context.debug: log.debug(f"No replication for {bucket_arn}")
                    continue
                except Exception as e:
                    if context.debug: log.debug(f"Error getting replication for {bucket_arn}: {e}")
                    continue
        else:
            # Get specific replication by table bucket ARN
            try:
                response = client.get_table_bucket_replication(tableBucketARN=id)
                common.write_import(type, id, None)
            except client.exceptions.NotFoundException:
                if context.debug: log.debug(f"No replication found for {id}")
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True


def get_aws_s3tables_table_replication(type, id, clfn, descfn, topkey, key, filterid):
    try:
        from botocore.config import Config
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all table buckets first
            paginator = client.get_paginator('list_table_buckets')
            buckets = []
            for page in paginator.paginate():
                buckets = buckets + page['tableBuckets']
            
            # For each bucket, list namespaces
            for bucket in buckets:
                bucket_arn = bucket['arn']
                try:
                    ns_paginator = client.get_paginator('list_namespaces')
                    namespaces = []
                    for page in ns_paginator.paginate(tableBucketARN=bucket_arn):
                        namespaces = namespaces + page['namespaces']
                    
                    # For each namespace, list tables
                    for ns in namespaces:
                        try:
                            table_paginator = client.get_paginator('list_tables')
                            tables = []
                            for page in table_paginator.paginate(tableBucketARN=bucket_arn, namespace=ns['namespace']):
                                tables = tables + page['tables']
                            
                            # For each table, check if replication exists
                            for table in tables:
                                table_arn = table['arn']
                                try:
                                    response = client.get_table_replication(tableArn=table_arn)
                                    # Replication exists for this table
                                    common.write_import(type, table_arn, None)
                                except client.exceptions.NotFoundException:
                                    # No replication for this table
                                    if context.debug: log.debug(f"No replication for {table_arn}")
                                    continue
                                except Exception as e:
                                    if context.debug: log.debug(f"Error getting replication for {table_arn}: {e}")
                                    continue
                        except Exception as e:
                            if context.debug: log.debug(f"Error listing tables in namespace {ns['namespace']}: {e}")
                            continue
                except Exception as e:
                    if context.debug: log.debug(f"Error listing namespaces for {bucket_arn}: {e}")
                    continue
        else:
            # Get specific replication by table ARN
            try:
                response = client.get_table_replication(tableArn=id)
                common.write_import(type, id, None)
            except client.exceptions.NotFoundException:
                if context.debug: log.debug(f"No replication found for {id}")
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True


def get_aws_s3tables_table_policy(type, id, clfn, descfn, topkey, key, filterid):
    try:
        from botocore.config import Config
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all table buckets
            paginator = client.get_paginator('list_table_buckets')
            table_buckets = []
            for page in paginator.paginate():
                table_buckets = table_buckets + page['tableBuckets']
            
            # For each table bucket, list namespaces and tables
            for bucket in table_buckets:
                bucket_arn = bucket['arn']
                try:
                    # List namespaces
                    ns_paginator = client.get_paginator('list_namespaces')
                    namespaces = []
                    for ns_page in ns_paginator.paginate(tableBucketARN=bucket_arn):
                        namespaces = namespaces + ns_page['namespaces']
                    
                    # For each namespace, list tables
                    for namespace in namespaces:
                        ns_name = namespace['namespace'][0] if isinstance(namespace['namespace'], list) else namespace['namespace']
                        try:
                            # List tables
                            table_paginator = client.get_paginator('list_tables')
                            tables = []
                            for table_page in table_paginator.paginate(tableBucketARN=bucket_arn, namespace=ns_name):
                                tables = tables + table_page['tables']
                            
                            # For each table, try to get its policy
                            for table in tables:
                                table_name = table['name']
                                try:
                                    # Try to get the table policy
                                    policy_response = client.get_table_policy(
                                        tableBucketARN=bucket_arn,
                                        namespace=ns_name,
                                        name=table_name
                                    )
                                    # Policy exists for this table
                                    composite_id = f"{bucket_arn};{ns_name};{table_name}"
                                    common.write_import(type, composite_id, None)
                                except client.exceptions.NotFoundException:
                                    # No policy for this table
                                    if context.debug: log.debug(f"No policy for table {table_name}")
                                    continue
                                except Exception as e:
                                    if context.debug: log.debug(f"Error getting policy for table {table_name}: {e}")
                                    continue
                        except Exception as e:
                            if context.debug: log.debug(f"Error listing tables for namespace {ns_name}: {e}")
                            continue
                except Exception as e:
                    if context.debug: log.debug(f"Error listing namespaces for bucket {bucket_arn}: {e}")
                    continue
        else:
            # Specific import - id should be composite: bucket-arn;namespace;table-name
            if ';' in id:
                parts = id.split(';')
                if len(parts) == 3:
                    bucket_arn, namespace, table_name = parts
                    try:
                        # Verify the policy exists
                        policy_response = client.get_table_policy(
                            tableBucketARN=bucket_arn,
                            namespace=namespace,
                            name=table_name
                        )
                        common.write_import(type, id, None)
                    except Exception as e:
                        if context.debug: log.debug(f"Error getting policy for {id}: {e}")
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True
