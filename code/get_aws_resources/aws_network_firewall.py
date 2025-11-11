import common
import boto3
from botocore.config import Config
import context
import inspect

def get_aws_networkfirewall_firewall(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn,config=config)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: 
                if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            for j in response:
                common.write_import(type,j[key],None) 
                common.write_import("aws_networkfirewall_logging_configuration",j[key],None) 

        else: 
            if id.startswith("arn:"):
                response = client.describe_firewall(FirewallArn=id)
            else:      
                response = client.describe_firewall(FirewallName=id)
            if response == []: 
                if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            #print(str(response))
            j=response['Firewall']
            common.write_import(type,j[key],None)
            common.write_import("aws_networkfirewall_logging_configuration",j[key],None) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_networkfirewall_firewall_policy(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn,config=config)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: 
                if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            for j in response:
                common.write_import(type,j[key],None) 

        else: 
            if id.startswith("arn:"):
                response = client.describe_firewall_policy(FirewallPolicyArn=id)
            else:      
                response = client.describe_firewall_policy(FirewallPolicyName=id)
            if response == []: 
                if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            #print(str(response))
            j=response['FirewallPolicyResponse']
            common.write_import(type,j['FirewallPolicyArn'],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_networkfirewall_rule_group(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn,config=config)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(Type='STATELESS'):
                response = response + page[topkey]
            if response == []: 
                if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
            else:    
                for j in response:
                    common.write_import(type,j[key],None) 

            for page in paginator.paginate(Type='STATEFUL'):
                response = response + page[topkey]
            if response == []: 
                if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            for j in response:
                common.write_import(type,j[key],None) 

        else: 
            if id.startswith("arn:"):
                if ":stateless-rulegroup/" in id:
                    response = client.describe_rule_group(RuleGroupArn=id,AnalyzeRuleGroup=False,Type='STATELESS')
            else:      
                print("INFO: must pass arn for rule group")
            if response == []: 
                if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
            else:
                j=response['RuleGroupResponse']
                common.write_import(type, j['RuleGroupArn'], None)
            if id.startswith("arn:"):
                if ":stateful-rulegroup/" in id:
                    response = client.describe_rule_group(RuleGroupArn=id,AnalyzeRuleGroup=False,Type='STATEFUL')
            else:      
                print("INFO: must pass arn for rule group")
            if response == []: 
                if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
            else:
                j=response['RuleGroupResponse']
                common.write_import(type, j['RuleGroupArn'], None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


# aws_networkfirewall_tls_inspection_configuration
def get_aws_networkfirewall_tls_inspection_configuration(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10, 'mode': 'standard'})
        client = boto3.client(clfn, config=config)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []:
                if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                common.write_import(type, j[key], None)

        else:
            if id.startswith("arn:"):
                response = client.describe_tls_inspection_configuration(TlsInspectionConfigurationArn=id)
            else:
                response = client.describe_tls_inspection_configuration(TlsInspectionConfigurationName=id)
            if response == []:
                if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            #print(str(response))
            j=response['TlsInspectionConfigurationResponse']
            common.write_import(type, j['TlsInspectionConfigurationArn'], None)

    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True
