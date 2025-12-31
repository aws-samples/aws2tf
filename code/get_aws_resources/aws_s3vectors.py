import common
from common import log_warning
import logging
log = logging.getLogger('aws2tf')
import boto3
from botocore.config import Config
import context
import inspect

def get_aws_s3vectors_vector_bucket(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn,config=config)
        if id is None:
            print("here")
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            for j in response:
                common.write_import(type,j[key],None) 

        else: 
            if id.startswith("arn:"):    
                response = client.get_vector_bucket(vectorBucketArn=id)
            else:
                response = client.get_vector_bucket(vectorBucketName=id)
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            # get_vector_bucket returns vectorBucket (singular), not vectorBuckets
            j=response['vectorBucket']
            common.write_import(type,j[key],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_s3vectors_index(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn,config=config)
        if id is None:
            # First, get all vector buckets
            bucket_paginator = client.get_paginator('list_vector_buckets')
            buckets = []
            for page in bucket_paginator.paginate():
                buckets = buckets + page['vectorBuckets']
            
            # Then list indexes for each bucket
            for bucket in buckets:
                bucket_name = bucket['vectorBucketName']
                try:
                    index_paginator = client.get_paginator(descfn)
                    for page in index_paginator.paginate(vectorBucketName=bucket_name):
                        response = response + page[topkey]
                except Exception as e:
                    if context.debug: log.debug(f"Error listing indexes for bucket {bucket_name}: {e}")
                    continue
            
            if response == []:
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                common.write_import(type,j[key],None)

        else:
            # Get specific index by ARN
            if id.startswith("arn:"):
                response = client.get_index(indexArn=id)
            else:
                # If not ARN, assume it's indexName and we need vectorBucketName
                # This case is tricky - we'd need both indexName and vectorBucketName
                log.warning(f"Index ID must be ARN format, got: {id}")
                return True
            
            if response == []:
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            # get_index returns index (singular), not indexes
            j=response.get('index', response)
            common.write_import(type,j[key],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_s3vectors_vector_bucket_policy(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn,config=config)
        if id is None:
            # First, get all vector buckets
            bucket_paginator = client.get_paginator('list_vector_buckets')
            buckets = []
            for page in bucket_paginator.paginate():
                buckets = buckets + page['vectorBuckets']
            
            # Then get policy for each bucket (if it exists)
            for bucket in buckets:
                bucket_arn = bucket['vectorBucketArn']
                try:
                    policy_response = client.get_vector_bucket_policy(vectorBucketArn=bucket_arn)
                    # Policy exists for this bucket
                    common.write_import(type, bucket_arn, None)
                except client.exceptions.NoSuchVectorBucketPolicy:
                    # No policy for this bucket, skip it
                    if context.debug: log.debug(f"No policy for bucket {bucket_arn}")
                    continue
                except Exception as e:
                    if context.debug: log.debug(f"Error getting policy for bucket {bucket_arn}: {e}")
                    continue

        else:
            # Get specific policy by bucket ARN
            response = client.get_vector_bucket_policy(vectorBucketArn=id)
            # The response contains the policy directly, use the bucket ARN as the import ID
            common.write_import(type, id, None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True
