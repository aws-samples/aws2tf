#!/usr/bin/env python3
"""
Get functions for AWS CloudWatch resources
"""

import logging
log = logging.getLogger('aws2tf')
import boto3
import common
import context
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

def get_aws_cloudwatch_contributor_insight_rule(type, id, clfn, descfn, topkey, key, filterid):
    """
    Get contributor insight rules (non-managed, user-created rules)
    """
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all insight rules - not pageable
            response = client.describe_insight_rules()
            for j in response[topkey]:
                # Only import non-managed rules (user-created)
                if not j.get('ManagedRule', False):
                    common.write_import(type, j[key], None)
        else:
            # Get specific insight rule - API doesn't support filtering by name
            # Extract rule name from ARN if needed
            rule_name = id
            if id.startswith('arn:'):
                # Extract name from ARN: arn:aws:cloudwatch:region:account:insight-rule/name
                rule_name = id.split('/')[-1]
            
            response = client.describe_insight_rules()
            for j in response[topkey]:
                if j[key] == rule_name and not j.get('ManagedRule', False):
                    common.write_import(type, j[key], None)
                    break
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


def get_aws_cloudwatch_contributor_managed_insight_rule(type, id, clfn, descfn, topkey, key, filterid):
    """
    Get contributor managed insight rules
    These are AWS-managed rules that can be enabled on specific resources
    """
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        # List all insight rules (not pageable, no filtering by name)
        response = client.describe_insight_rules()
        
        # Filter for managed rules
        for rule in response['InsightRules']:
            if rule.get('ManagedRule', False):
                rule_name = rule['Name']
                if id is None or id in rule_name:
                    common.write_import(type, rule_name, None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_cloudwatch_query_definition(type, id, clfn, descfn, topkey, key, filterid):
    """
    Get CloudWatch Logs query definitions
    """
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all query definitions
            response = client.describe_query_definitions()
            for j in response[topkey]:
                common.write_import(type, j[key], None)
        else:
            # Get specific query definition
            response = client.describe_query_definitions(queryDefinitionIds=[id])
            if response[topkey]:
                j = response[topkey][0]
                common.write_import(type, j[key], None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True
