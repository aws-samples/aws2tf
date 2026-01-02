import common
from common import log_warning
import logging
log = logging.getLogger('aws2tf')
import context
import inspect
import boto3

def get_aws_cloudwatch_log_group(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In get_aws_cloudwatch_log_group  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        paginator = client.get_paginator(descfn)
        if id is None:
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                logn=j[key]
                common.write_import(type,logn,None) 
                common.add_dependancy("aws_cloudwatch_log_stream", logn) 

        elif "arn:" in id:
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                if j['arn'] == id:
                    logn=j[key]
                    common.write_import(type,logn,None) 
                    common.add_dependancy("aws_cloudwatch_log_stream", logn) 

        else: # assume it's a log name
            for page in paginator.paginate(logGroupNamePattern=id):
                response = response + page[topkey]
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                logn=j[key]
                common.write_import(type,logn,None) 
                common.add_dependancy("aws_cloudwatch_log_stream", logn) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True



def get_aws_cloudwatch_log_stream(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In get_aws_cloudwatch_log_stream  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        client = boto3.client(clfn)
        if id is not None:    
            response = client.describe_log_streams(logGroupName=id)
            if response[topkey] == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                pkey=type+"."+id
                context.rproc[pkey]=True
                return True
            for j in response[topkey]:
                sn = j[key]
                lgn=id
                theid=lgn+":"+sn
                common.write_import(type, theid, None)
            pkey=type+"."+id
            context.rproc[pkey]=True
 
        else:
            log_warning("WARNING: No id provided for get_aws_cloudwatch_log_stream")
            return True
    
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_cloudwatch_log_data_protection_policy(type, id, clfn, descfn, topkey, key, filterid):
    """
    Get log data protection policies by iterating through log groups and checking for policies
    """
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        client = boto3.client(clfn)
        
        if id is None:
            # List all log groups and check for data protection policies
            paginator = client.get_paginator('describe_log_groups')
            for page in paginator.paginate():
                for log_group in page['logGroups']:
                    log_group_name = log_group['logGroupName']
                    try:
                        # Try to get the data protection policy for this log group
                        response = client.get_data_protection_policy(logGroupIdentifier=log_group_name)
                        if 'policyDocument' in response and response['policyDocument']:
                            # Policy exists for this log group
                            common.write_import(type, log_group_name, None)
                    except client.exceptions.ResourceNotFoundException:
                        # No policy for this log group
                        if context.debug:
                            log.debug(f"No data protection policy for log group {log_group_name}")
                        continue
                    except Exception as e:
                        if context.debug:
                            log.debug(f"Error getting policy for log group {log_group_name}: {e}")
                        continue
        else:
            # Get specific log group's data protection policy
            try:
                response = client.get_data_protection_policy(logGroupIdentifier=id)
                if 'policyDocument' in response and response['policyDocument']:
                    common.write_import(type, id, None)
                else:
                    log_warning(f"No data protection policy found for log group {id}")
            except client.exceptions.ResourceNotFoundException:
                log_warning(f"No data protection policy found for log group {id}")

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_cloudwatch_log_destination_policy(type, id, clfn, descfn, topkey, key, filterid):
    """
    Get log destination policies by iterating through destinations and checking for policies
    """
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        client = boto3.client(clfn)
        
        if id is None:
            # List all destinations and check for policies
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                for destination in page[topkey]:
                    # Check if destination has an access policy
                    if 'accessPolicy' in destination and destination['accessPolicy']:
                        destination_name = destination[key]
                        common.write_import(type, destination_name, None)
        else:
            # Get specific destination's policy
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(DestinationNamePrefix=id):
                for destination in page[topkey]:
                    if destination[key] == id:
                        if 'accessPolicy' in destination and destination['accessPolicy']:
                            common.write_import(type, id, None)
                        else:
                            log_warning(f"No access policy found for destination {id}")
                        break

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True
