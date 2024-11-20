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

def get_aws_s3_bucket(type, id, clfn, descfn, topkey, key, filterid):
   globals.tracking_message="Stage 3 of 10 getting s3 resources ..."
   get_all_s3_buckets(id,globals.region)
   return True


def check_access(bucket_name,my_region):
   s3= boto3.client("s3",region_name=my_region)
   try:
      objs = s3.list_objects_v2(Bucket=bucket_name,MaxKeys=1)
   except Exception as e:
         exc_type, exc_obj, exc_tb = sys.exc_info()
         exn=str(exc_type.__name__)
         #print(f"{exn=}")
         if exn == "AccessDenied" or exn=="ClientError":
            print("NO ACCESS: to Bucket: "+bucket_name + " - continue")
            globals.bucketlist[bucket_name]=False
            return
         
         print(f"{e=}")
         print("ERROR: -2->unexpected error in get_all_s3_buckets")
         
         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
         print(exc_type, fname, exc_tb.tb_lineno)
         print('continuing on exception to location .......')
         return
   return

def check_location(bucket_name,my_region):
   s3= boto3.client("s3",region_name=my_region)
   type="aws_s3_bucket"
   try:
      location = s3.get_bucket_location(Bucket=bucket_name)
         #
      bl=location['LocationConstraint']
      if bl is None and my_region == 'us-east-1': bl='us-east-1'
      #print ("bucket: " +  bucket_name + " location="+str(bl)+"  my_region="+my_region)
      if bl != my_region:
         print('Skipping bucket '+bucket_name+' in region '+ str(bl)+ " not in configured region "+my_region)  
         pkey=type+"."+bucket_name
         globals.rproc[pkey]=True
         globals.bucketlist[bucket_name]=False
         if bl is None:  
            print('skipping on None location (assume us-east-1) .......')
            pkey=type+"."+bucket_name
            globals.rproc[pkey]=True
            if my_region != "us-east-1": 
               globals.bucketlist[bucket_name]=False
               return
         else:
            #globals.rproc[pkey]=True
            return
      elif bl == 'null':  
         #globals.rproc[pkey]=True
         print('continuing on null location .......')
         return
      else:
         #print("here...."+bucket_name)
         #globals.rproc[pkey]=True
         pkey=type+"."+bucket_name
         globals.rproc[pkey]=True
        
         #print(bl)
         return
   except Exception as e:
         exc_type, exc_obj, exc_tb = sys.exc_info()
         exn=str(exc_type.__name__)
         #print(f"{exn=}")
         if exn == "AccessDenied" or exn=="ClientError":
            print("NO ACCESS: to Bucket: "+bucket_name + " - continue")
            globals.bucketlist[bucket_name]=False
            return
         
         print(f"{e=}")
         print("ERROR: -2->unexpected error in get_all_s3_buckets")
         
         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
         print(exc_type, fname, exc_tb.tb_lineno)
         print('continuing on exception to location .......')
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
  
   s3_fields2 = {
      'aws_s3_bucket_acl': s3.get_bucket_acl
   }
  
   

   buckets = s3a.buckets.all()

   if globals.fast:

      for bucket in s3a.buckets.all():
         if fb is not None and fb not in bucket.name: continue

         globals.bucketlist[bucket.name]=True
      
      
      #print("----------------------")
      
      # check can access
      with ThreadPoolExecutor(max_workers=globals.cores) as executor4:
         futures = [
            executor4.submit(check_access,key,my_region)
            for key in globals.bucketlist.keys()
         ]


      #for k, v in globals.bucketlist.items():
      #   if v is False:
      #      print("false bucket="+k,str(v))
   

      # check location
      with ThreadPoolExecutor(max_workers=globals.cores) as executor5:
         futures = [
            executor5.submit(check_location,key,my_region)
            for key in globals.bucketlist.keys()
         ]


      #for k, v in globals.bucketlist.items():
      #   if v is True:
      #      print("false bucket="+k,str(v))

      for k, v in globals.bucketlist.items():
         if v is True:
            #print("true bucket="+k,str(v))
            bucket_name=k
            if "aws_s3_bucket,"+bucket_name in globals.rproc:
               print("Already processed skipping bucket " + bucket_name)
               continue
            
            common.write_import(type,bucket_name,"b-"+bucket_name)
            common.add_dependancy("aws_s3_access_point",bucket_name)


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

      for buck in buckets: 
      
         bucket_name=buck.name
         
         if "aws_s3_bucket,"+bucket_name in globals.rproc:
            print("Already processed skipping bucket " + bucket_name)
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
               location = s3.get_bucket_location(Bucket=bucket_name)
               #print(str(location))
               bl=location['LocationConstraint']
               if bl is None and my_region == 'us-east-1':
                  bl='us-east-1'
               #print("bl="+bl)
               #print ("bucket: " +  bucket_name + " location="+str(bl)+"  my_region="+my_region)
               if bl != my_region:
                  print('Skipping bucket '+bucket_name+' in region '+ str(bl)+ " not in configured region "+my_region)  
                  pkey=type+"."+bucket_name
                  globals.rproc[pkey]=True
                  if bl is None:  
                     print('skipping on None location (assume us-east-1) .......')
                     pkey=type+"."+bucket_name
                     globals.rproc[pkey]=True
                     if my_region != "us-east-1": continue
                  else:
                     #globals.rproc[pkey]=True
                     continue
               elif bl == 'null':  
                     #globals.rproc[pkey]=True
                     print('continuing on null location .......')
                     continue
               else:
                  #print("skip...."+bucket_name)
                  #globals.rproc[pkey]=True
                  pkey=type+"."+bucket_name
                  globals.rproc[pkey]=True
                  pass
                  #print(bl)
                  
         except Exception as e:
               exc_type, exc_obj, exc_tb = sys.exc_info()
               exn=str(exc_type.__name__)
               #print(f"{exn=}")
               if exn == "AccessDenied" or exn=="ClientError":
                  print("NO ACCESS: to Bucket: "+bucket_name + " - continue")
                  continue
               
               print(f"{e=}")
               print("ERROR: -2->unexpected error in get_all_s3_buckets")
               
               fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
               print(exc_type, fname, exc_tb.tb_lineno)
               print('continuing on exception to location .......')
               continue
         

         #try:
         #    mp="s3://"+buck.name+"/"
         #    objects = list(buck.objects.all(mp))
         #except:
         #    print("failed to access bucket " +bucket_name + " " + bl +" skipping ..")
         #    continue
         #print("write_import for Bucket: "+bucket_name)
         print("Processing Bucket: "+bucket_name + '  ............')
         common.write_import(type,bucket_name,"b-"+bucket_name)
         common.add_dependancy("aws_s3_access_point",bucket_name)
      
         for key in s3_fields2:
            get_s3(s3_fields2, key, bucket_name)

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
