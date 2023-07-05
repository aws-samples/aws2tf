#!/usr/bin/env python3
import boto3
import json
import aws2tf


def s3_state(sf,ttft,bucket_name):
   rname="b_"+bucket_name
   aws2tf.res_head(sf,ttft,rname)
   sf.write('            "bucket": "' + bucket_name +'",\n')
   sf.write('            "id": "' + bucket_name +'"\n')
   aws2tf.res_tail(sf)

def get_s3(sf,f,s3_fields,type,bucket_name):
   try:
      #print("in get_s3 type=" + type)
      response=s3_fields[type](Bucket=bucket_name)
      rl=len(response)
      if rl > 1 :
         #print("resp done " + type + " rl=" + str(rl))
         s3_state(sf,type,bucket_name)
         #print("state done " + type)
         f.write('"' + type + '": ' + json.dumps(response, indent=4, default=str) + "\n")
         #if 'logging' in type:
         #   print(json.dumps(response, indent=4, default=str))
         

   except:
      #print("No " + type + " config for bucket " + bucket_name)
      pass


def get_all_s3_buckets(sf,fb):
  """Gets all the AWS S3 buckets and saves them to a file."""
  s3a = boto3.resource("s3")
  s3 = boto3.client("s3")
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
     if fb is not None:
         if fb not in bucket_name:
            continue

     fn="data/s3-"+str(bucket_name)+".json"
     with open(fn, "w") as f:
   
      print("Bucket: "+bucket_name + '  ----------------------------------------------------------------')

      try:
         #print('location')
         location = s3.get_bucket_location(Bucket=bucket_name)
         
         bl=location['LocationConstraint']
         if bl != my_region:
            print('continuing on non default location '+ bl)
            continue
         if bl is None:  
               print('continuing on None location .......')
               continue
         elif bl == 'null':  
               print('continuing on null location .......')
               continue
         else:
            pass
            #print(bl)
            
      except:
         print('continuing on exception to location .......')
         continue

      f.write("{\n")
      f.write('"name": "' + bucket_name + '",\n')


      s3_state(sf,"aws_s3_bucket",bucket_name)


      for key in s3_fields:
         #print("outside get_s3 type=" + key)
         get_s3(sf,f,s3_fields,key,bucket_name)
      
      f.write("}\n")
      f.close()

####################################################


