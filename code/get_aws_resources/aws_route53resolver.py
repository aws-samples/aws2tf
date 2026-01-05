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


def get_aws_route53_resolver_firewall_rule(type, id, clfn, descfn, topkey, key, filterid):
    try:
        from botocore.config import Config
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        
        if id is None:
            # List all firewall rule groups, then list rules for each
            paginator = client.get_paginator('list_firewall_rule_groups')
            rule_groups = []
            for page in paginator.paginate():
                rule_groups = rule_groups + page['FirewallRuleGroups']
            
            for rule_group in rule_groups:
                rule_group_id = rule_group['Id']
                try:
                    # List rules for this rule group
                    rules_paginator = client.get_paginator('list_firewall_rules')
                    for rules_page in rules_paginator.paginate(FirewallRuleGroupId=rule_group_id):
                        for rule in rules_page['FirewallRules']:
                            # Build composite ID: rule_group_id:domain_list_id or rule_group_id:threat_protection_id
                            if 'FirewallDomainListId' in rule:
                                composite_id = f"{rule_group_id}:{rule['FirewallDomainListId']}"
                                common.write_import(type, composite_id, None)
                            elif 'FirewallThreatProtectionId' in rule:
                                composite_id = f"{rule_group_id}:{rule['FirewallThreatProtectionId']}"
                                common.write_import(type, composite_id, None)
                except Exception as e:
                    if context.debug: log.debug(f"Error listing rules for group {rule_group_id}: {e}")
                    continue
        else:
            # Specific import - id should be composite: rule_group_id:domain_list_id
            if ':' in id:
                rule_group_id, resource_id = id.split(':', 1)
                # Verify the rule exists
                try:
                    rules_paginator = client.get_paginator('list_firewall_rules')
                    for rules_page in rules_paginator.paginate(FirewallRuleGroupId=rule_group_id):
                        for rule in rules_page['FirewallRules']:
                            if ('FirewallDomainListId' in rule and rule['FirewallDomainListId'] == resource_id) or \
                               ('FirewallThreatProtectionId' in rule and rule['FirewallThreatProtectionId'] == resource_id):
                                common.write_import(type, id, None)
                                break
                except Exception as e:
                    if context.debug: log.debug(f"Error getting rule {id}: {e}")
            elif id.startswith('rslvr-frg-'):
                # If just rule group ID provided, get all rules for that group
                try:
                    rules_paginator = client.get_paginator('list_firewall_rules')
                    for rules_page in rules_paginator.paginate(FirewallRuleGroupId=id):
                        for rule in rules_page['FirewallRules']:
                            if 'FirewallDomainListId' in rule:
                                composite_id = f"{id}:{rule['FirewallDomainListId']}"
                                common.write_import(type, composite_id, None)
                            elif 'FirewallThreatProtectionId' in rule:
                                composite_id = f"{id}:{rule['FirewallThreatProtectionId']}"
                                common.write_import(type, composite_id, None)
                except Exception as e:
                    if context.debug: log.debug(f"Error listing rules for group {id}: {e}")
    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)
    return True
