import common
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect

def get_aws_codebuild_project(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        paginator = client.get_paginator(descfn)
        for page in paginator.paginate():
            response = response + page[topkey]
        if response == []: 
            log.debug("Empty response for "+type+ " id="+str(id)+" returning")
            return True
        
        for j in response:
            log.debug(str(j))
            if id is None: 
                common.write_import(type,j,None) 
            elif j==id:
                common.write_import(type,j,None) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_codebuild_report_group(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        paginator = client.get_paginator(descfn)
        for page in paginator.paginate():
            response = response + page[topkey]
        if response == []: 
            log.debug("Empty response for "+type+ " id="+str(id)+" returning")
            return True
        
        for j in response:
            log.debug(str(j))
            if id is None: 
                common.write_import(type,j,None) 
            elif j==id:
                common.write_import(type,j,None) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_codebuild_resource_policy(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        client = boto3.client(clfn)
        
        if id is None:
            # First get all report groups
            report_groups = []
            paginator = client.get_paginator('list_report_groups')
            for page in paginator.paginate():
                report_groups = report_groups + page['reportGroups']
            
            # Then try to get policy for each report group
            for report_group_arn in report_groups:
                try:
                    response = client.get_resource_policy(resourceArn=report_group_arn)
                    # Policy exists for this report group
                    common.write_import(type, report_group_arn, None)
                except client.exceptions.ResourceNotFoundException:
                    # No policy for this report group, skip it
                    if context.debug: log.debug(f"No policy for {report_group_arn}")
                    continue
                except Exception as e:
                    if context.debug: log.debug(f"Error getting policy for {report_group_arn}: {e}")
                    continue
        else:
            # Get specific policy by resource ARN
            try:
                response = client.get_resource_policy(resourceArn=id)
                # Use the resource ARN as the import ID
                common.write_import(type, id, None)
            except client.exceptions.ResourceNotFoundException:
                log.debug(f"NOT FOUND: {type} {id}")

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True
