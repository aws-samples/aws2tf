#!/usr/bin/env python3
"""
Handler for AWS CloudWatch resources
"""

import context

def aws_cloudwatch_metric_alarm(t1, tt1, tt2, flag1, flag2):
    """Handler for aws_cloudwatch_metric_alarm resource"""
    skip = 0
    # datapoints_to_alarm must be >= 1; AWS returns 0 when it was never set.
    # Drop the line so the provider uses its default.
    if tt1 == "datapoints_to_alarm" and tt2 == "0":
        skip = 1
    # empty dimensions map conflicts with metric_query - drop it
    elif tt1 == "dimensions" and tt2 == "{}":
        skip = 1
    # period/threshold-style scalars are 0 when metric_query is used; period=0
    # both is invalid and conflicts with metric_query - drop it
    elif tt1 == "period" and tt2 == "0":
        skip = 1
    return skip, t1, flag1, flag2

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
