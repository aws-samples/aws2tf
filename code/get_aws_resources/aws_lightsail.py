import boto3
import common
import inspect
from botocore.config import Config

def get_aws_lightsail_lb(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all load balancers
            response = client.get_load_balancers()
            for j in response[topkey]:
                common.write_import(type, j[key], None)
        else:
            # Get specific load balancer
            response = client.get_load_balancer(loadBalancerName=id)
            j = response.get('loadBalancer', response)
            common.write_import(type, j[key], None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True

def get_aws_lightsail_lb_stickiness_policy(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all load balancers and check which have stickiness enabled
            response = client.get_load_balancers()
            for lb in response['loadBalancers']:
                config_options = lb.get('configurationOptions', {})
                if config_options.get('SessionStickinessEnabled') == 'true':
                    common.write_import(type, lb['name'], None)
        else:
            # Get specific load balancer and check if stickiness is enabled
            response = client.get_load_balancer(loadBalancerName=id)
            lb = response.get('loadBalancer', response)
            config_options = lb.get('configurationOptions', {})
            if config_options.get('SessionStickinessEnabled') == 'true':
                common.write_import(type, lb['name'], None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True

def get_aws_lightsail_lb_https_redirection_policy(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all load balancers and check which have HTTPS redirection enabled
            response = client.get_load_balancers()
            for lb in response['loadBalancers']:
                if lb.get('httpsRedirectionEnabled', False):
                    common.write_import(type, lb['name'], None)
        else:
            # Get specific load balancer and check if HTTPS redirection is enabled
            response = client.get_load_balancer(loadBalancerName=id)
            lb = response.get('loadBalancer', response)
            if lb.get('httpsRedirectionEnabled', False):
                common.write_import(type, lb['name'], None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True
