#!/usr/bin/env python3
import boto3
import common
import globals
import os
import sys
import inspect
from get_aws_resources import aws_s3control
import concurrent.futures
from typing import List, Dict
import io
from concurrent.futures import ThreadPoolExecutor
from botocore.exceptions import NoCredentialsError, ClientError


def get_aws_s3_bucket(type, id, clfn, descfn, topkey, key, filterid):
   globals.tracking_message="Stage 3 of 10 getting s3 resources ..."
   get_all_s3_buckets(id,globals.region)
   return True


def check_access(bucket_name,my_region):
   
   try:
      #session = boto3.Session(region_name=my_region,profile_name=globals.profile)
      #s3 = session.client('s3')
      s3 = boto3.client('s3')
      ####### problematic call
      objs = s3.list_objects_v2(Bucket=bucket_name,MaxKeys=1)

   
   except NoCredentialsError as e:
        print(f"CREDENTIAL ERROR: Unable to locate credentials for SSO session")
        print("Please ensure you have an active SSO session (run 'aws sso login')")
        print(f"Error details: {e}")
        globals.bucketlist[bucket_name] = False
        return False

   except ClientError as e:
      error_code = e.response['Error']['Code']
      if error_code == 'AccessDenied':
            print(f"NO ACCESS (1): to Bucket: {bucket_name} - continue")
            globals.bucketlist[bucket_name] = False
            globals.s3list[bucket_name] = False
            pkey="aws_s3_bucket."+bucket_name
            globals.rproc[pkey]=True
            return False
        
      elif error_code == 'ExpiredToken':
            print(f"TOKEN EXPIRED: Your AWS session token has expired")
            print("Please renew your session (run 'aws sso login')")
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            exn=str(exc_type.__name__)
            print((f"{fname=} {exc_tb.tb_lineno=} \n"))
            globals.bucketlist[bucket_name] = False
            return False
      else:
            print(f"AWS Error: {error_code} - {e}")
            globals.bucketlist[bucket_name] = False
            return False

   except Exception as e:
         exc_type, exc_obj, exc_tb = sys.exc_info()
         exn=str(exc_type.__name__)
         #print(f"{exn=}")
         if exn == "AccessDenied" or exn=="ClientError":
            print("NO ACCESS (2): to Bucket: "+bucket_name + " - continue")
            globals.bucketlist[bucket_name]=False
            return
         
         print(f"{e=}")
         print("ERROR: -2->unexpected error in get_all_s3_buckets")
         
         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
         print(exc_type, fname, exc_tb.tb_lineno)
         print('continuing on exception .......')
         return
   return


def get_all_s3_buckets(fb,my_region):
   #print("bucket name="+str(fb))
   type="aws_s3_bucket"
   if fb =="" or fb =="null":
      print("bucket name is empty or null")
      pkey=type+"."+fb
      globals.rproc[pkey]=True
      return True
   
   if globals.debug: print("my_region="+my_region)
   #print("processed=" + str(globals.rproc))
   """Gets all the AWS S3 buckets and saves them to a file."""
   boto3.setup_default_session(region_name=my_region)
   s3a = boto3.resource("s3",region_name=my_region) 
   s3 = boto3.client("s3",region_name=my_region)
   s3_fields = {
      'aws_s3_bucket_accelerate_configuration': s3.get_bucket_accelerate_configuration,
      'aws_s3_bucket_acl': s3.get_bucket_acl, 
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
  


   if not globals.debug:

      for bn in globals.s3list.keys():
      #for bucket in s3a.buckets.all():
         #if fb is not None and fb not in bucket.name: continue
         if fb is not None and fb not in bn: continue

         #globals.bucketlist[bucket.name]=True
         globals.bucketlist[bn]=True
      
      
      #print("----------------------")
      
      # check can access
      with ThreadPoolExecutor(max_workers=globals.cores) as executor4:
         futures = [
            executor4.submit(check_access,key,my_region)
            for key in globals.bucketlist.keys()
         ]


      for k, v in globals.bucketlist.items():
         if v is True:
            #print("true bucket="+k,str(v))
            bucket_name=k
            
            if "aws_s3_bucket."+bucket_name in str(globals.rproc):
               if globals.rproc["aws_s3_bucket."+bucket_name] is True:
                  print("Already processed skipping bucket " + bucket_name + " (MT)")
                  continue
               
            print("Processing Bucket (MT): "+bucket_name + ' ...')
            common.write_import(type,bucket_name,"b-"+bucket_name)
            common.add_dependancy("aws_s3_access_point",bucket_name)
            pkey=type+"."+bucket_name
            globals.rproc[pkey]=True


      globals.tracking_message="Stage 3 of 10 getting s3 bucket properties resources ..."
      for k, v in globals.bucketlist.items():
         if v is True:
            #print("true bucket="+k,str(v))
            bucket_name=k
            ### thread thread ?
            with ThreadPoolExecutor(max_workers=globals.cores) as executor3:
                     futures = [
                        executor3.submit(get_s3,s3_fields,key,bucket_name)
                        for key in s3_fields
                     ]   
      
      return True


#### debug not multi-threaded

   else:

      #for buck in buckets: 
      for bucket_name in globals.s3list.keys():   
      
         #bucket_name=buck.name
         if "aws_s3_bucket,"+bucket_name in globals.rproc:
            print("Already processed skipping bucket " + bucket_name+ " (ST)")
            os._exit(1)
            continue
         # jump if bucket name does not match
         if fb is not None:
               #print("fb="+fb+" bucket_name="+bucket_name)
               if fb not in bucket_name:
                  #print("skipping bucket " + bucket_name)
                  continue
         try:
               #print('location') - no error if no access for getting location
               objs = s3.list_objects_v2(Bucket=bucket_name,MaxKeys=1)
                  
         except Exception as e:
               exc_type, exc_obj, exc_tb = sys.exc_info()
               exn=str(exc_type.__name__)
               #print(f"{exn=}")
               if exn == "AccessDenied" or exn=="ClientError":
                  print("NO ACCESS (3): to Bucket: "+bucket_name + " - continue")
                  continue
               
               print(f"{e=}")
               print("ERROR: -2->unexpected error in get_all_s3_buckets")
               
               fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
               print(exc_type, fname, exc_tb.tb_lineno)
               print('continuing on exception to location .......')
               continue

         if "aws_s3_bucket."+bucket_name in str(globals.rproc):
               if globals.rproc["aws_s3_bucket."+bucket_name] is True:
                  print("Already processed skipping bucket " + bucket_name + " (MT)")
                  continue

         print("Processing Bucket (ST): "+bucket_name + ' ...')
         common.write_import(type,bucket_name,"b-"+bucket_name)
         common.add_dependancy("aws_s3_access_point",bucket_name)
         pkey=type+"."+bucket_name
         globals.rproc[pkey]=True
      
         for key in s3_fields:
            get_s3(s3_fields, key, bucket_name)

   return True
      
     
         
####################################################

def get_s3(s3_fields,type,bucket_name):
   try:
      if globals.debug: print("get_s3 type=" + type)
      response=s3_fields[type](Bucket=bucket_name)
      
      rl=len(response)
      if rl > 1 :  common.write_import(type,bucket_name,"b-"+bucket_name)


   except:
      if globals.debug: print("No " + type + " config for bucket " + bucket_name)
      pass



def get_s3_access_control(type, id, clfn, descfn, topkey, key, filterid):
   ret=aws_s3control.get_aws_s3_access_point(type, id, clfn, descfn, topkey, key, filterid)
   return ret
