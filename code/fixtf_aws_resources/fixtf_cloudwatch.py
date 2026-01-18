#!/usr/bin/env python3
"""
Handler for AWS CloudWatch resources
"""

import context

def aws_cloudwatch_composite_alarm(t1, tt1, tt2, flag1, flag2):
    """Handler for aws_cloudwatch_composite_alarm resource"""
    skip = 0
    return skip, t1, flag1, flag2

def aws_cloudwatch_dashboard(t1, tt1, tt2, flag1, flag2):
    """Handler for aws_cloudwatch_dashboard resource"""
    skip = 0
    return skip, t1, flag1, flag2

def aws_cloudwatch_contributor_insight_rule(t1, tt1, tt2, flag1, flag2):
    """Handler for aws_cloudwatch_contributor_insight_rule resource"""
    skip = 0
    
    # Handle null rule_definition - it's a required field
    if tt1 == "rule_definition" and tt2 == "null":
        # Skip this line - rule_definition cannot be null
        skip = 1
    
    return skip, t1, flag1, flag2

def aws_cloudwatch_contributor_managed_insight_rule(t1, tt1, tt2, flag1, flag2):
    """Handler for aws_cloudwatch_contributor_managed_insight_rule resource"""
    skip = 0
    return skip, t1, flag1, flag2

def aws_cloudwatch_event_connection(t1, tt1, tt2, flag1, flag2):
    """Handler for aws_cloudwatch_event_connection resource"""
    skip = 0
    
    # Replace sensitive null value with placeholder - it's write-only
    if "value = null # sensitive" in t1:
        t1 = t1.replace("value = null # sensitive", 'value = "PLACEHOLDER_VALUE_CHANGE_ME" # sensitive - original value not returned by API')
    
    return skip, t1, flag1, flag2
