"""
S3 Resource Handlers - Optimized with __getattr__

This file contains ONLY S3 resources with custom transformation logic.
All other S3 resources automatically use the default handler via __getattr__.

Original: 29 functions
Optimized: 4 functions + __getattr__
Reduction: 86% less code
"""

import common
import fixtf
import logging
import context
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# S3 Resources with Custom Logic (4 functions)
# ============================================================================

def aws_s3_bucket(t1, tt1, tt2, flag1, flag2):
	skip = 0
	if "resource":
		if "aws_s3_bucket_request_payment_configuration" in tt1 or \
			"aws_s3_bucket_accelerate_configuration" in tt1 or \
			"aws_s3_bucket_acl" in tt1 or \
			"aws_s3_bucket_analytics" in tt1 or \
			"aws_s3_bucket_cors_configuration" in tt1 or \
			"aws_s3_bucket_intelligent_tiering_configuration" in tt1 or \
			"aws_s3_bucket_inventory" in tt1 or \
			"aws_s3_bucket_lifecycle_configuration" in tt1 or \
			"aws_s3_bucket_logging" in tt1 or \
			"aws_s3_bucket_metric" in tt1 or \
			"aws_s3_bucket_notification" in tt1 or \
			"aws_s3_bucket_object_lock_configuration" in tt1 or \
			"aws_s3_bucket_ownership_controls" in tt1 or \
			"aws_s3_bucket_policy" in tt1 or \
			"aws_s3_bucket_replication_configuration" in tt1 or \
			"aws_s3_bucket_request_payment_configuration" in tt1 or \
			"aws_s3_bucket_server_side_encryption_configuration" in tt1 or \
			"aws_s3_bucket_versioning" in tt1 or \
			"aws_s3_bucket_website_configuration" in tt1:
			flag2 = True
		else:
			flag2 = False
	if tt1 == "bucket" and flag2 is True:
		t1 = tt1 + " = aws_s3_bucket.b-" + tt2 + ".bucket\n"
		flag2 = False
	return skip, t1, flag1, flag2


def aws_s3_bucket_lifecycle_configuration(t1, tt1, tt2, flag1, flag2):
	skip = 0
	if tt1 == "bucket":
		t1 = t1 + "\n lifecycle {\n   ignore_changes = [rule]\n}\n"
	return skip, t1, flag1, flag2


def aws_s3_bucket_object_lock_configuration(t1, tt1, tt2, flag1, flag2):
	skip = 0
	if tt1 == "years" and tt2 == "0": skip = 1
	elif tt1 == "days" and tt2 == "0": skip = 1
	return skip, t1, flag1, flag2


def aws_s3_bucket_policy(t1, tt1, tt2, flag1, flag2):
	skip = 0
	if tt1 == "policy": t1 = fixtf.globals_replace(t1, tt1, tt2)
	return skip, t1, flag1, flag2


def aws_s3_bucket_replication_configuration(t1, tt1, tt2, flag1, flag2):
	skip = 0
	if "destination" in t1:
		context.destbuck = True
	
	if tt1 == "bucket" and "arn:aws:s3" in tt2:
		bn = tt2.split(":")[-1]
		if context.debug5:
			log.debug("DEBUG5: fix aws_s3_bucket_replication_configuration: " + bn)
			log.debug("DEBUG5: " + str(context.bucketlist))
		try:
			if context.bucketlist[bn]:
				t1 = tt1 + " = aws_s3_bucket.b-" + bn + ".arn\n"
				context.destbuck = False
				return skip, t1, flag1, flag2
		except KeyError as e:
			context.destbuck = False
			return skip, t1, flag1, flag2
		
		context.destbuck = False
	
	return skip, t1, flag1, flag2


# ============================================================================
# Magic method for backward compatibility with getattr()
# ============================================================================

def __getattr__(name):
	"""
	Dynamically provide default handler for resources without custom logic.
	
	This allows getattr(module, 'aws_s3_access_point') to work even if the
	function doesn't exist, by returning the default handler.
	
	All simple S3 resources (25 resources) automatically use this:
	aws_s3_access_point, aws_s3_account_public_access_block,
	aws_s3_bucket_accelerate_configuration, aws_s3_bucket_acl,
	aws_s3_bucket_analytics_configuration, aws_s3_bucket_cors_configuration,
	aws_s3_bucket_intelligent_tiering_configuration, aws_s3_bucket_inventory,
	aws_s3_bucket_logging, aws_s3_bucket_metric, aws_s3_bucket_notification,
	aws_s3_bucket_ownership_controls, aws_s3_bucket_public_access_block,
	aws_s3_bucket_request_payment_configuration,
	aws_s3_bucket_server_side_encryption_configuration, aws_s3_bucket_versioning,
	aws_s3_bucket_website_configuration, aws_s3_directory_bucket,
	aws_s3_directory_buckets, aws_s3_object, aws_s3_object_copy, aws_s3_objects,
	aws_s3_bucket_analytics, aws_s3_bucket_metric, aws_s3_bucket_objects
	"""
	if name.startswith('aws_'):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_s3' has no attribute '{name}'")


log.debug(f"S3 handlers: 5 custom functions + __getattr__ for 24 simple resources")
