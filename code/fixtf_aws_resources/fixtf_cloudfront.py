"""
CLOUDFRONT Resource Handlers - Optimized with __getattr__

This file contains ONLY CLOUDFRONT resources with custom transformation logic.
All other resources automatically use the default handler via __getattr__.

Original: 2 functions
Optimized: 2 functions + __getattr__
Reduction: 0% less code
"""

import logging
import boto3
from botocore.config import Config
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')

# Cache for policy type checks to avoid repeated API calls
_cache_policy_types = {}


# ============================================================================
# CLOUDFRONT Resources with Custom Logic (2 functions)
# ============================================================================

def aws_cloudfront_distribution(t1,tt1,tt2,flag1,flag2):
	skip=0
	if tt1=="cache_policy_id" and tt2 != "null":
		# Check if this is an AWS-managed or custom cache policy
		if _is_custom_cache_policy(tt2):
			# Custom policy - dereference it
			t1=tt1+" = aws_cloudfront_cache_policy.o-"+tt2+".id\n"
		# else: AWS-managed policy - keep literal value
	return skip,t1,flag1,flag2


def _is_custom_cache_policy(policy_id):
	"""
	Check if a CloudFront cache policy is custom (not AWS-managed).
	Uses caching to avoid repeated API calls.
	
	Returns True if custom, False if AWS-managed or on error.
	"""
	# Check cache first
	if policy_id in _cache_policy_types:
		return _cache_policy_types[policy_id]
	
	try:
		config = Config(retries={'max_attempts': 3, 'mode': 'standard'})
		client = boto3.client('cloudfront', config=config)
		
		# Get the cache policy details
		response = client.get_cache_policy(Id=policy_id)
		policy_name = response['CachePolicy']['CachePolicyConfig']['Name']
		
		# AWS-managed policies have names starting with "Managed-"
		is_custom = not policy_name.startswith('Managed-')
		
		# Cache the result
		_cache_policy_types[policy_id] = is_custom
		
		if is_custom:
			log.debug(f"Cache policy {policy_id} is custom, will dereference")
		else:
			log.debug(f"Cache policy {policy_id} is AWS-managed ({policy_name}), using literal")
		
		return is_custom
		
	except Exception as e:
		# On any error, assume AWS-managed (safer to use literal)
		log.debug(f"Error checking cache policy {policy_id}: {e}, assuming AWS-managed")
		_cache_policy_types[policy_id] = False
		return False



def aws_cloudfront_function(t1,tt1,tt2,flag1,flag2):


	skip=0
	if tt1=="publish" and tt2=="null": 
		#t1=t1+"\n lifecycle {\n   ignore_changes = [publish]\n}\n"
		t1=tt1+" = true\n" 
		t1=t1+"\n lifecycle {\n   ignore_changes = [publish]\n}\n"
	return skip,t1,flag1,flag2



# ============================================================================
# Magic method for backward compatibility with getattr()
# ============================================================================



# ============================================================================
# Magic method for backward compatibility with getattr()
# ============================================================================

def __getattr__(name):
	"""
	Dynamically provide default handler for resources without custom logic.
	
	This allows getattr(module, "aws_resource") to work even if the
	function doesn't exist, by returning the default handler.
	
	All simple CLOUDFRONT resources (0 resources) automatically use this.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_cloudfront' has no attribute '{name}'")


log.debug(f"CLOUDFRONT handlers: 2 custom functions + __getattr__ for 0 simple resources")