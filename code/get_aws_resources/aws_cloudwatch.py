#!/usr/bin/env python3
"""
Get functions for AWS CloudWatch resources
"""

import boto3
import common
import inspect
from botocore.config import Config

def get_aws_cloudwatch_composite_alarm(type, id, clfn, descfn, topkey, key, filterid):
    """
    Get composite alarms using describe_alarms with AlarmTypes filter
    """
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all composite alarms
            paginator = client.get_paginator(descfn)
            response = []
            for page in paginator.paginate(AlarmTypes=['CompositeAlarm']):
                response = response + page[topkey]
            for j in response:
                common.write_import(type, j[key], None)
        else:
            # Get specific composite alarm
            response = client.describe_alarms(AlarmNames=[id], AlarmTypes=['CompositeAlarm'])
            if response[topkey]:
                j = response[topkey][0]
                common.write_import(type, j[key], None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True

def get_aws_cloudwatch_contributor_managed_insight_rule(type, id, clfn, descfn, topkey, key, filterid):
    """
    Get contributor managed insight rules using describe_insight_rules
    """
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all insight rules - not pageable
            response = client.describe_insight_rules()
            for j in response[topkey]:
                # Only import managed rules (those with ManagedRule field set to True)
                if j.get('ManagedRule', False):
                    common.write_import(type, j[key], None)
        else:
            # Get specific insight rule
            response = client.describe_insight_rules()
            for j in response[topkey]:
                if j[key] == id and j.get('ManagedRule', False):
                    common.write_import(type, j[key], None)
                    break
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True
