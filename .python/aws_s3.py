#!/usr/bin/env python3
import boto3
import common
import globals

def get_all_s3_buckets(fb,my_region):
   print("bucket name="+str(fb))
   type="aws_s3_bucket"
   
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


     #print("Bucket: "+bucket_name + '  ------------------------------')

     try:
         #print('location')
         location = s3.get_bucket_location(Bucket=bucket_name)
         
         bl=location['LocationConstraint']
         #print ("bucket: " +  bucket_name + " location="+bl)
         if bl != my_region:
            #print('continuing on non default location '+ bl)
            continue
         if bl is None:  
               #print('continuing on None location .......')
               continue
         elif bl == 'null':  
               #print('continuing on null location .......')
               continue
         else:
            pass
            #print(bl)
            
     except Exception as e:
         print(f"{e=}")
         print('continuing on exception to location .......')
         continue
     

     #try:
     #    mp="s3://"+buck.name+"/"
     #    objects = list(buck.objects.all(mp))
     #except:
     #    print("failed to access bucket " +bucket_name + " " + bl +" skipping ..")
     #    continue
     print("Bucket: "+bucket_name)

     common.write_import(type,bucket_name,"b-"+bucket_name)

     for key in s3_fields:
            #print("outside get_s3 type=" + key)
         get_s3(s3_fields,key,bucket_name)

   return True
      
     
         
####################################################

def get_s3(s3_fields,type,bucket_name):
   try:
      #print("in get_s3 type=" + type)
      response=s3_fields[type](Bucket=bucket_name)
      rl=len(response)
      if rl > 1 :

         common.write_import(type,bucket_name,"b-"+bucket_name)

   except:
      if globals.debug: print("No " + type + " config for bucket " + bucket_name)
      pass
