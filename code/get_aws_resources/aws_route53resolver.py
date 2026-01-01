import boto3
import common
import inspect
from botocore.config import Config
import context

def get_aws_route53_resolver_dnssec_config(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all DNSSEC configs
            response = []
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            
            # Filter for only ENABLED configs
            for j in response:
                if j.get('ValidationStatus') == 'ENABLED':
                    common.write_import(type, j[key], None)
        else:
            # For specific import, the id could be either the DNSSEC config ID or VPC ID
            # Try to get by VPC ID first (if id starts with 'vpc-')
            # Otherwise, list all and find the matching DNSSEC config ID
            if id.startswith('vpc-'):
                # ID is a VPC ID
                response = client.get_resolver_dnssec_config(ResourceId=id)
                j = response.get('ResolverDnssecConfig', response)
                if j.get('ValidationStatus') == 'ENABLED':
                    common.write_import(type, j[key], None)
            else:
                # ID is a DNSSEC config ID - need to list all and find it
                response = []
                paginator = client.get_paginator(descfn)
                for page in paginator.paginate():
                    response = response + page[topkey]
                
                for j in response:
                    if j.get(key) == id and j.get('ValidationStatus') == 'ENABLED':
                        common.write_import(type, j[key], None)
                        break
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True
