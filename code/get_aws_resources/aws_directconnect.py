import boto3
import common
import context
import logging
import inspect
from botocore.config import Config

def get_aws_dx_gateway(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        response = []
        
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            for j in response:
                common.write_import(type, j[key], None)
        else:
            response = client.describe_direct_connect_gateways(directConnectGatewayId=id)
            if response[topkey]:
                j = response[topkey][0]
                common.write_import(type, j[key], None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True
