"""
NETWORKFLOWMONITOR Resource Handlers - Optimized with __getattr__

This file contains NETWORKFLOWMONITOR resource handlers.
All resources use the default handler via __getattr__.

Auto-generated stub file.
"""

import logging
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


# ============================================================================
# Magic method for backward compatibility with getattr()
# ============================================================================

def __getattr__(name):
	"""
	Dynamically provide default handler for all NETWORKFLOWMONITOR resources.
	
	This allows getattr(module, "aws_resource") to work by returning
	the default handler for all resources.
	"""
	if name.startswith("aws_"):
		return BaseResourceHandler.default_handler
	raise AttributeError(f"module 'fixtf_networkflowmonitor' has no attribute '{name}'")


log.debug(f"NETWORKFLOWMONITOR handlers: __getattr__ for all resources")


def aws_networkflowmonitor_monitor(t1, tt1, tt2, flag1, flag2):
    import common
    import context
    import boto3
    from botocore.config import Config
    skip = 0
    
    # Extract monitor name from resource declaration
    if t1.startswith("resource"):
        parts = t1.split('"')
        if len(parts) >= 4:
            monitor_name = parts[3]
            context.networkflowmonitor_monitor_name = monitor_name
    
    # Handle scope_arn - need to look it up from the monitor
    if tt1 == "scope_arn":
        if hasattr(context, 'networkflowmonitor_monitor_name'):
            try:
                config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
                client = boto3.client('networkflowmonitor', region_name=context.region)
                response = client.get_monitor(monitorName=context.networkflowmonitor_monitor_name)
                scope_arn = response.get('scopeArn', '')
                if scope_arn and '/' in scope_arn:
                    scope_id = scope_arn.split('/')[-1]
                    t1 = tt1 + " = aws_networkflowmonitor_scope.r-" + scope_id + ".scope_arn\n"
                    common.add_dependancy("aws_networkflowmonitor_scope", scope_id)
                else:
                    # Fallback if we can't parse
                    t1 = tt1 + " = \"" + scope_arn + "\"\n"
            except Exception as e:
                if context.debug: log.debug(f"Error getting monitor details: {e}")
                # Skip if we can't get it
                skip = 1
    
    return skip, t1, flag1, flag2
