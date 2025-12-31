import boto3
import common
import inspect
from botocore.config import Config

def get_aws_workspacesweb_portal(type, id, clfn, descfn, topkey, key, filterid):
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all portals - not pageable
            response = client.list_portals()
            for j in response[topkey]:
                common.write_import(type, j[key], None)
        else:
            # Get specific portal
            response = client.get_portal(portalArn=id)
            j = response.get('portal', response)
            common.write_import(type, j[key], None)
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True
