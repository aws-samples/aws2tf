#!/usr/bin/env python3
import logging
log = logging.getLogger('aws2tf')
import boto3
import common
import context
import os
import sys
import inspect
from get_aws_resources import aws_s3control
import concurrent.futures
from typing import List, Dict
import io
from concurrent.futures import ThreadPoolExecutor
from botocore.exceptions import NoCredentialsError, ClientError
from tqdm import tqdm


def extract_bucket_name_from_arn(id_or_arn):
    """
    Extract bucket name from either a bucket name or bucket ARN.
    
    Args:
        id_or_arn: Either a bucket name or ARN (arn:aws:s3:::bucket-name)
    
    Returns:
        The bucket name
    """
    if id_or_arn is None:
        return None
    
    # If it's an ARN, extract the bucket name
    if id_or_arn.startswith('arn:'):
        # S3 ARN format: arn:aws:s3:::bucket-name or arn:aws:s3:::bucket-name/*
        parts = id_or_arn.split(':')
        if len(parts) >= 6:
            # The bucket name is after the 5th colon
            bucket_part = parts[5]
            # Remove any path components (e.g., bucket-name/path -> bucket-name)
            bucket_name = bucket_part.split('/')[0]
            if context.debug:
                log.debug(f"Extracted bucket name '{bucket_name}' from ARN '{id_or_arn}'")
            return bucket_name
        else:
            if context.debug:
                log.debug(f"Invalid S3 ARN format: {id_or_arn}, using as-is")
            return id_or_arn
    
    # Not an ARN, return as-is (it's already a bucket name)
    return id_or_arn


def get_aws_s3_bucket(type, id, clfn, descfn, topkey, key, filterid):
   # Extract bucket name from ARN if needed
   bucket_name = extract_bucket_name_from_arn(id)
   
   context.tracking_message="Stage 3 of 10 getting s3 resources ..."
   #log.info(f"Getting s3 resources id=%s",id)
   get_all_s3_buckets(bucket_name,context.region)
   return True


def get_aws_s3_bucket_cors_configuration(type, id, clfn, descfn, topkey, key, filterid):
   """Route CORS configuration requests to main S3 bucket handler"""
   return get_aws_s3_bucket(type, id, clfn, descfn, topkey, key, filterid)


def get_aws_s3_bucket_server_side_encryption_configuration(type, id, clfn, descfn, topkey, key, filterid):
   """Route server-side encryption configuration requests to main S3 bucket handler"""
   return get_aws_s3_bucket(type, id, clfn, descfn, topkey, key, filterid)


def get_aws_s3_directory_bucket(type, id, clfn, descfn, topkey, key, filterid):
   """Get S3 Express directory buckets"""
   try:
      from botocore.config import Config
      config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
      client = boto3.client(clfn, config=config)
      
      # Extract bucket name from ARN if needed
      bucket_name = extract_bucket_name_from_arn(id)
      
      if bucket_name is None:
         # List all directory buckets
         response = client.list_directory_buckets()
         for j in response[topkey]:
            common.write_import(type, j[key], None)
      else:
         # Get specific directory bucket
         response = client.list_directory_buckets()
         for j in response[topkey]:
            if bucket_name in j[key]:
               common.write_import(type, j[key], None)
               break
   except Exception as e:
      common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
   
   return True


def check_access(bucket_name,my_region):
   
   try:
      #session = boto3.Session(region_name=my_region,profile_name=context.profile)
      #s3 = session.client('s3')
      s3 = boto3.client('s3')
      ####### problematic call
      objs = s3.list_objects_v2(Bucket=bucket_name,MaxKeys=1)

   
   except NoCredentialsError as e:
        log.info(f"CREDENTIAL ERROR: Unable to locate credentials for SSO session")
        log.info("Please ensure you have an active SSO session (run 'aws sso login')")
        log.info(f"Error details: {e}")
        context.bucketlist[bucket_name] = False
        return False

   except ClientError as e:
      error_code = e.response['Error']['Code']
      if error_code == 'AccessDenied':
            log.info(f"NO ACCESS (1): to Bucket: {bucket_name} - continue")
            context.bucketlist[bucket_name] = False
            context.s3list[bucket_name] = False
            pkey="aws_s3_bucket."+bucket_name
            context.rproc[pkey]=True
            return False
        
      elif error_code == 'ExpiredToken':
            log.info(f"TOKEN EXPIRED: Your AWS session token has expired")
            log.info("Please renew your session (run 'aws sso login')")
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            exn=str(exc_type.__name__)
            log.info((f"{fname=} {exc_tb.tb_lineno=} \n"))
            context.bucketlist[bucket_name] = False
            return False
      else:
            log.info(f"AWS Error: {error_code} - {e}")
            context.bucketlist[bucket_name] = False
            return False

   except Exception as e:
         exc_type, exc_obj, exc_tb = sys.exc_info()
         exn=str(exc_type.__name__)
         if exn == "AccessDenied" or exn=="ClientError":
            log.info("NO ACCESS (2): to Bucket: "+bucket_name + " - continue")
            context.bucketlist[bucket_name]=False
            return
         
         log.info(f"{e=}")
         log.info("ERROR: -2->unexpected error in get_all_s3_buckets")
         
         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
         log.info("%s %s %s", exc_type, fname, exc_tb.tb_lineno)
         log.info('continuing on exception .......')
         return
   return


def get_all_s3_buckets(fb,my_region):
   type="aws_s3_bucket"
   if fb is not None:
      if fb =="" or fb =="null":
         log.info("bucket name is empty or null")
         pkey=type+"."+fb
         context.rproc[pkey]=True
         return True
      
      if fb not in str(context.s3list.keys()):
            log.info("Bucket %s not in s3list %s",  fb)
            pkey=type+"."+fb
            context.rproc[pkey]=True
            return True
   
   if context.debug: log.debug("my_region="+my_region)
   """Gets all the AWS S3 buckets and saves them to a file."""
   boto3.setup_default_session(region_name=my_region)
   s3a = boto3.resource("s3",region_name=my_region) 
   s3 = boto3.client("s3",region_name=my_region)
   s3_fields = {
      'aws_s3_bucket_accelerate_configuration': s3.get_bucket_accelerate_configuration,
      # 'aws_s3_bucket_acl': s3.get_bucket_acl,   should not use
      'aws_s3_bucket_analytics': s3.get_bucket_analytics_configuration,
      'aws_s3_bucket_cors_configuration': s3.get_bucket_cors,
      'aws_s3_bucket_intelligent_tiering_configuration': s3.get_bucket_intelligent_tiering_configuration,
      'aws_s3_bucket_inventory': s3.get_bucket_inventory_configuration,
      'aws_s3_bucket_lifecycle_configuration': s3.get_bucket_lifecycle_configuration,  ##   ?
      'aws_s3_bucket_logging': s3.get_bucket_logging,
      'aws_s3_bucket_metric': s3.get_bucket_metrics_configuration,
      'aws_s3_bucket_notification': s3.get_bucket_notification,
      #  no terraform resource ': s3.get_bucket_notification_configuration,
      'aws_s3_bucket_object_lock_configuration': s3.get_object_lock_configuration,
      'aws_s3_bucket_ownership_controls': s3.get_bucket_ownership_controls,
      'aws_s3_bucket_policy': s3.get_bucket_policy,
      #  no terraform resource ': s3.get_bucket_policy_status,
      'aws_s3_bucket_replication_configuration': s3.get_bucket_replication,
      'aws_s3_bucket_request_payment_configuration': s3.get_bucket_request_payment,
      'aws_s3_bucket_server_side_encryption_configuration': s3.get_bucket_encryption,
      #: no terraform resource s3.get_bucket_tagging,
      'aws_s3_bucket_versioning': s3.get_bucket_versioning,
      'aws_s3_bucket_website_configuration': s3.get_bucket_website
   }
  
   if not context.debug:
      for bn in context.s3list.keys():
         #log.info("Checking bucket "+bn+" fb= "+str(fb))
      #for bucket in s3a.buckets.all():
         #if fb is not None and fb not in bucket.name: continue
         if fb is not None and fb not in bn: 
            #log.info("skipping bucket "+bn)
            continue

         #context.bucketlist[bucket.name]=True
         context.bucketlist[bn]=True
      
      # check can access
      log.debug(f"Checking access to {len(context.bucketlist)} S3 buckets...")
      with ThreadPoolExecutor(max_workers=context.cores) as executor4:
         futures = [
            executor4.submit(check_access,key,my_region)
            for key in context.bucketlist.keys()
         ]
         # Show progress
         for future in tqdm(concurrent.futures.as_completed(futures),
                           total=len(futures),
                           desc="Checking bucket access",
                           unit="bucket", leave=False):
            future.result()


      # Process accessible buckets
      accessible_buckets = [k for k, v in context.bucketlist.items() if v is True]
      log.debug(f"Processing {len(accessible_buckets)} accessible S3 buckets...")
      
      for bucket_name in tqdm(accessible_buckets,
                             desc="Processing S3 buckets",
                             unit="bucket", leave=False):
         
         if "aws_s3_bucket."+bucket_name in str(context.rproc):
            if context.rproc["aws_s3_bucket."+bucket_name] is True:
               if context.debug:
                  log.debug("Already processed skipping bucket " + bucket_name + " (MT)")
               continue
            
         if context.debug:
            log.debug("Processing Bucket (MT): "+bucket_name + ' ...')
         common.write_import(type,bucket_name,"b-"+bucket_name)
         common.add_dependancy("aws_s3_access_point",bucket_name)
         pkey=type+"."+bucket_name
         context.rproc[pkey]=True


      context.tracking_message="Stage 3 of 10 getting s3 bucket properties resources ..."
      log.debug(f"Getting S3 bucket properties for {len(accessible_buckets)} buckets...")
      
      for bucket_name in tqdm(accessible_buckets,
                             desc="Getting bucket properties",
                             unit="bucket", leave=False):
         ### thread thread ?
         with ThreadPoolExecutor(max_workers=context.cores) as executor3:
                  futures = [
                     executor3.submit(get_s3,s3_fields,key,bucket_name)
                     for key in s3_fields
                  ]   
      
      return True


#### debug not multi-threaded

   else:

      #for buck in buckets: 
      for bucket_name in context.s3list.keys():   
      
         #bucket_name=buck.name
         if "aws_s3_bucket,"+bucket_name in context.rproc:
            log.debug("Already processed skipping bucket " + bucket_name+ " (ST)")
            sys.exit(1)
            continue
         # jump if bucket name does not match
         if fb is not None:
               if fb not in bucket_name:
                  continue
         try:
               objs = s3.list_objects_v2(Bucket=bucket_name,MaxKeys=1)
                  
         except Exception as e:
               exc_type, exc_obj, exc_tb = sys.exc_info()
               exn=str(exc_type.__name__)
               if exn == "AccessDenied" or exn=="ClientError":
                  log.info("NO ACCESS (3): to Bucket: "+bucket_name + " - continue")
                  continue
               
               log.info(f"{e=}")
               log.info("ERROR: -2->unexpected error in get_all_s3_buckets")
               
               fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
               log.info("%s %s %s", exc_type, fname, exc_tb.tb_lineno)
               log.info('continuing on exception to location .......')
               continue

         if "aws_s3_bucket."+bucket_name in str(context.rproc):
               if context.rproc["aws_s3_bucket."+bucket_name] is True:
                  log.debug("Already processed skipping bucket " + bucket_name + " (MT)")
                  continue

         log.info("Processing Bucket (ST): "+bucket_name + ' ...')
         common.write_import(type,bucket_name,"b-"+bucket_name)
         common.add_dependancy("aws_s3_access_point",bucket_name)
         pkey=type+"."+bucket_name
         context.rproc[pkey]=True
      
         for key in s3_fields:
            get_s3(s3_fields, key, bucket_name)

   return True
      
     
         
####################################################

def get_s3(s3_fields,type,bucket_name):
   try:
      if context.debug: 
         log.debug("get_s3 type=" + type)
      response=s3_fields[type](Bucket=bucket_name)
      if type=="aws_s3_bucket_replication_configuration": 
         try:
            barn=str(response['ReplicationConfiguration']['Rules'][0]['Destination']['Bucket'])
            repbuck=barn.split(":")[-1]
            common.add_known_dependancy("aws_s3_bucket",repbuck)
         except:
             response=response
      rl=len(response)
      if rl > 1 :  common.write_import(type,bucket_name,"b-"+bucket_name)


   except:
      if context.debug: log.debug("No " + type + " config for bucket " + bucket_name)
      pass



def get_s3_access_control(type, id, clfn, descfn, topkey, key, filterid):
   ret=aws_s3control.get_aws_s3_access_point(type, id, clfn, descfn, topkey, key, filterid)
   return ret
