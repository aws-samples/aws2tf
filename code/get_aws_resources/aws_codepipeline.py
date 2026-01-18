import common
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect
from botocore.config import Config

def get_aws_codepipeline_custom_action_type(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all custom action types
            response = client.list_action_types(actionOwnerFilter='Custom')
            action_types = response.get(topkey, [])
            
            for action in action_types:
                # Build composite ID: Category/Provider/Version
                action_id = action['id']
                composite_id = f"{action_id['category']}/{action_id['provider']}/{action_id['version']}"
                common.write_import(type, composite_id, None)
        else:
            # Handle specific import by composite ID
            # ID format: Category/Provider/Version or Category:Provider:Version
            if '/' in id:
                parts = id.split('/')
            elif ':' in id:
                parts = id.split(':')
            else:
                log.debug(f"Invalid ID format: {id}")
                return True
                
            if len(parts) == 3:
                category, provider, version = parts
                # Verify the action type exists
                response = client.list_action_types(actionOwnerFilter='Custom')
                action_types = response.get(topkey, [])
                
                for action in action_types:
                    action_id = action['id']
                    if (action_id['category'] == category and 
                        action_id['provider'] == provider and 
                        action_id['version'] == version):
                        composite_id = f"{category}/{provider}/{version}"
                        common.write_import(type, composite_id, None)
                        break

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True



def get_aws_codepipeline_webhook(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all webhooks
            response = client.list_webhooks()
            webhooks = response.get(topkey, [])
            
            for webhook in webhooks:
                # Use the webhook ARN as the import ID
                webhook_arn = webhook['arn']
                common.write_import(type, webhook_arn, None)
        else:
            # Get specific webhook by ARN
            response = client.list_webhooks()
            webhooks = response.get(topkey, [])
            
            for webhook in webhooks:
                if webhook['arn'] == id:
                    common.write_import(type, id, None)
                    break

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True
