import boto3
import common
import inspect
from botocore.config import Config
import context

def get_aws_devopsguru_event_sources_config(type, id, clfn, descfn, topkey, key, filterid):
    """
    Regional singleton resource - uses region as ID
    """
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # For regional singleton, verify the resource exists before writing import
            try:
                response = client.describe_event_sources_config()
                if response:
                    region = client.meta.region_name
                    common.write_import(type, region, None)
            except client.exceptions.ResourceNotFoundException:
                # Resource doesn't exist in this region - skip it
                if context.debug: 
                    print(f"DevOps Guru event sources config not found in region {client.meta.region_name}")
            except Exception as e:
                if context.debug: 
                    print(f"Error checking event sources config: {e}")
        else:
            # Verify the resource exists in the specified region
            try:
                response = client.describe_event_sources_config()
                if response:
                    common.write_import(type, id, None)
            except client.exceptions.ResourceNotFoundException:
                # Resource doesn't exist - skip it
                if context.debug: 
                    print(f"DevOps Guru event sources config not found for id {id}")
            except Exception as e:
                if context.debug: 
                    print(f"Error getting event sources config: {e}")
    
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    
    return True


def get_aws_devopsguru_notification_channel(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all notification channels
            paginator = client.get_paginator(descfn)
            response = []
            for page in paginator.paginate():
                response = response + page[topkey]
            for j in response:
                common.write_import(type, j[key], None)
        else:
            # Get specific notification channel by listing and filtering
            # Note: There's no describe_notification_channel API method
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                for j in page[topkey]:
                    if j[key] == id:
                        common.write_import(type, j[key], None)
                        return True
    
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    
    return True


def get_aws_devopsguru_resource_collection(type, id, clfn, descfn, topkey, key, filterid):
    """
    Resource collection - uses ResourceCollectionType as ID
    """
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all resource collection types (AWS_CLOUD_FORMATION, AWS_SERVICE, AWS_TAGS)
            # Try each type and see which ones exist with actual resources
            collection_types = ['AWS_CLOUD_FORMATION', 'AWS_SERVICE', 'AWS_TAGS']
            for collection_type in collection_types:
                try:
                    response = client.get_resource_collection(ResourceCollectionType=collection_type)
                    if response and 'ResourceCollection' in response:
                        # Check if the collection actually has resources configured
                        resource_collection = response['ResourceCollection']
                        has_resources = False
                        
                        # Check CloudFormation stacks
                        if 'CloudFormation' in resource_collection:
                            cf = resource_collection['CloudFormation']
                            if cf.get('StackNames') or cf.get('StackFilters'):
                                has_resources = True
                        
                        # Check AWS Services
                        if 'Service' in resource_collection:
                            service = resource_collection['Service']
                            if service.get('ServiceNames'):
                                has_resources = True
                        
                        # Check Tags
                        if 'Tags' in resource_collection:
                            tags = resource_collection['Tags']
                            if tags:
                                has_resources = True
                        
                        # Only import if there are actual resources configured
                        if has_resources:
                            common.write_import(type, collection_type, None)
                except Exception as e:
                    if context.debug:
                        print(f"No resource collection for type {collection_type}: {e}")
                    continue
        else:
            # Get specific resource collection
            try:
                response = client.get_resource_collection(ResourceCollectionType=id)
                if response and 'ResourceCollection' in response:
                    # Verify it has actual resources configured
                    resource_collection = response['ResourceCollection']
                    has_resources = False
                    
                    if 'CloudFormation' in resource_collection:
                        cf = resource_collection['CloudFormation']
                        if cf.get('StackNames') or cf.get('StackFilters'):
                            has_resources = True
                    
                    if 'Service' in resource_collection:
                        service = resource_collection['Service']
                        if service.get('ServiceNames'):
                            has_resources = True
                    
                    if 'Tags' in resource_collection:
                        tags = resource_collection['Tags']
                        if tags:
                            has_resources = True
                    
                    if has_resources:
                        common.write_import(type, id, None)
            except Exception as e:
                if context.debug:
                    print(f"Error getting resource collection {id}: {e}")
    
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    
    return True


def get_aws_devopsguru_service_integration(type, id, clfn, descfn, topkey, key, filterid):
    """
    Regional singleton resource - uses region as ID
    """
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # For regional singleton, verify the resource exists before writing import
            try:
                response = client.describe_service_integration()
                if response:
                    region = client.meta.region_name
                    common.write_import(type, region, None)
            except client.exceptions.ResourceNotFoundException:
                # Resource doesn't exist in this region - skip it
                if context.debug:
                    print(f"DevOps Guru service integration not found in region {client.meta.region_name}")
            except Exception as e:
                if context.debug:
                    print(f"Error checking service integration: {e}")
        else:
            # Verify the resource exists in the specified region
            try:
                response = client.describe_service_integration()
                if response:
                    common.write_import(type, id, None)
            except client.exceptions.ResourceNotFoundException:
                # Resource doesn't exist - skip it
                if context.debug:
                    print(f"DevOps Guru service integration not found for id {id}")
            except Exception as e:
                if context.debug:
                    print(f"Error getting service integration: {e}")
    
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    
    return True
