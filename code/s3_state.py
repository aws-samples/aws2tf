"""S3 operations for state backup in aws2tf."""

import boto3
import os
import json
import context
import logging
from botocore.exceptions import ClientError

log = logging.getLogger('aws2tf')


def create_bucket_if_not_exists(bucket_name):
    s3_client = boto3.client('s3')
    
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        log.info(f"Bucket {bucket_name} already exists.")
    except ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            log.info(f"Bucket {bucket_name} does not exist. Creating now...")
            try:
               s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': context.region})
               log.info(f"Bucket {bucket_name} created successfully.")
            except ClientError as create_error:
               log.error(f"Error creating bucket {bucket_name}: {create_error}")
               return False
        else:
            log.error(f"Error checking bucket {bucket_name}: {e}")
            return False
    
    return True



def upload_directory_to_s3():
   log.info("Uploading to S3...")
   s3_client = boto3.client('s3')
   local_directory="/tmp/aws2tf/generated/tf-"+context.pathadd+context.acc+"-"+context.region
   bucket_name="aws2tf-"+context.acc+"-"+context.region
   s3_prefix=''
   log.info("Calling create_bucket_if_not_exists for %s",  bucket_name)
   bret=create_bucket_if_not_exists(bucket_name)
   if bret:
      log.info("Upload files to s3 %s",  bucket_name)
      for root, dirs, files in os.walk(local_directory):
         if '.terraform' in dirs:  dirs.remove('.terraform')
         if 'tfplan' in files: files.remove('tfplan')
         if '.terraform.lock.hcl' in files: files.remove('.terraform.lock.hcl')
         for filename in files:
               local_path = os.path.join(root, filename)
               
               # Calculate relative path
               relative_path = os.path.relpath(local_path, local_directory)
               s3_path = os.path.join(s3_prefix, relative_path).replace("\\", "/")
               
               try:
                  s3_client.upload_file(local_path, bucket_name, s3_path)
               except ClientError as e:
                  log.error(f"Error uploading {local_path}: {e}")
                  return False
      log.info("Upload to S3 complete.")
   else:
      log.error("Upload to S3 failed - False return from create_bucket_if_not_exists for %s",  bucket_name)
      return False


def empty_and_delete_bucket():
    bucket_name="aws2tf-"+context.acc+"-"+context.region
    s3 = boto3.resource('s3')
    s3_client = boto3.client('s3')
    bucket = s3.Bucket(bucket_name)
    log.info("Emptying and deleting bucket... %s",  bucket_name)
    # Check if the bucket exists
    try:
        s3_client.head_bucket(Bucket=bucket_name)
    except ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            log.info(f"Bucket {bucket_name} does not exist. Nothing to delete.")
            return
        else:
            log.error(f"Error checking bucket {bucket_name}: {e}")
            return

    # Empty the bucket
    try:
        bucket.objects.all().delete()
        log.info(f"Bucket {bucket_name} emptied successfully.")
    except ClientError as e:
        log.error(f"Error emptying bucket {bucket_name}: {e}")
        return

    # Delete the bucket
    try:
        bucket.delete()
        log.info(f"Bucket {bucket_name} deleted successfully.")
    except ClientError as e:
        log.error(f"Error deleting bucket {bucket_name}: {e}")
        return

    log.info(f"Bucket {bucket_name} has been emptied and deleted.")


def download_from_s3():
    log.info("Restore S3")
    s3_client = boto3.client('s3')
    local_directory="/tmp/aws2tf/generated/tf-"+context.pathadd+context.acc+"-"+context.region
    bucket_name="aws2tf-"+context.acc+"-"+context.region
    s3_prefix=''
    # Check if the bucket exists
    try:
        s3_client.head_bucket(Bucket=bucket_name)
    except ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            log.error(f"Bucket {bucket_name} does not exist. Cannot download.")
            return
        else:
            log.error(f"Error checking bucket {bucket_name}: {e}")
            return

    # Create the local directory if it doesn't exist
    os.makedirs(local_directory, exist_ok=True)

    # List objects in the bucket with the specified prefix
    paginator = s3_client.get_paginator('list_objects_v2')
    for page in paginator.paginate(Bucket=bucket_name, Prefix=s3_prefix):
        if 'Contents' not in page:
            continue

        for obj in page['Contents']:
            # Skip the .terraform directory
            if '.terraform' in obj['Key']:
                continue

            # Get the relative path of the file
            relative_path = os.path.relpath(obj['Key'], s3_prefix)
            local_file_path = os.path.join(local_directory, relative_path)

            # Create the directory structure if it doesn't exist
            os.makedirs(os.path.dirname(local_file_path), exist_ok=True)

            # Download the file
            try:
                s3_client.download_file(bucket_name, obj['Key'], local_file_path)
            except ClientError as e:
                log.error(f"Error downloading {obj['Key']}: {e}")

    log.info(f"Download from {bucket_name}/{s3_prefix} to {local_directory} completed.")
