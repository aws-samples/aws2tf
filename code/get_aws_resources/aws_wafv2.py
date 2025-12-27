import common
from common import log_warning
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect
from botocore.config import Config
from botocore.exceptions import ClientError

def get_aws_wafv2_ip_set(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None: # assume scope = cloudfront
            sc="CLOUDFRONT"
            if context.region == "us-east-1":
                response = client.list_ip_sets(Scope=sc)
                if response == []: 
                    if context.debug: log.debug("Empty response for "+type+ " Scope="+str(sc)+" returning")
                    return True
                for j in response[topkey]:
                    idd=j["Id"]
                    nm=j["Name"]
                    sc="CLOUDFRONT"
                    pkey=idd+"/"+nm+"/"+sc
                    common.write_import(type,pkey,"w-"+pkey.replace("/","_")) 
            else:
                log_warning("WARNING:Can only import CLOUDFRONT ip sets from us-east-1 region")
            log.info("INFO: Getting Regional resources")
            sc="REGIONAL"
            response = client.list_ip_sets(Scope=sc)
            #print(str(response))
            if response[topkey] == []:
                if context.debug: 
                    log.debug("Empty response for "+type+ " Scope="+str(sc)+" returning")
                    log.info(str(response))
                return True
            
            #print(str(response))
            for j in response[topkey]:
                idd=j["Id"]
                nm=j["Name"]
                pkey=idd+"/"+nm+"/"+sc
                common.write_import(type, pkey, "w-"+pkey.replace("/", "_"))


        else: 
            if "|" in id:
                nm=id.split("|")[0]
                idd=id.split("|")[1]
                sc=id.split("|")[2]  
            else:
                log.info("Invalid id format for "+type+" id="+str(id)+" - returning")
                return True
            response = client.get_ip_set(Scope=sc,Name=nm,Id=idd)
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            j=response['IPSet']
            pkey=idd+"/"+nm+"/"+sc
            common.write_import(type,pkey,"w-"+pkey.replace("/","_"))

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True



def get_aws_wafv2_web_acl(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None: # assume scope = cloudfront
            sc="CLOUDFRONT"
            if context.region == "us-east-1":
                response = client.list_web_acls(Scope=sc)
                if response == []: 
                    if context.debug: log.debug("Empty response for "+type+ " Scope="+str(sc)+" returning")
                    return True
                for j in response[topkey]:
                    idd=j["Id"]
                    nm=j["Name"]
                    sc="CLOUDFRONT"
                    arn=j['ARN']
                    pkey=idd+"/"+nm+"/"+sc
                    common.write_import(type,pkey,"w-"+pkey.replace("/","_")) 
                    if type not in context.all_extypes:
                        common.add_dependancy("aws_wafv2_web_acl_logging_configuration",arn)
            else:
                log_warning("WARNING:Can only import CLOUDFRONT web ACL's from us-east-1 region")
 
            sc="REGIONAL"
            response = client.list_web_acls(Scope=sc)
            if response[topkey] == []:
                if context.debug: 
                    log.debug("Empty response for "+type+ " Scope="+str(sc)+" returning")
                    log.info(str(response))
                return True
            
            #print(str(response))
            for j in response[topkey]:
                idd=j["Id"]
                nm=j["Name"]
                arn=j['ARN']
                pkey=idd+"/"+nm+"/"+sc
                common.write_import(type, pkey, "w-"+pkey.replace("/", "_"))
                if type not in context.all_extypes:
                    common.add_dependancy("aws_wafv2_web_acl_logging_configuration",arn)
                    common.add_dependancy("aws_wafv2_web_acl_association",arn)

        else: 
            if "|" in id:
                nm=id.split("|")[0]
                idd=id.split("|")[1]
                sc=id.split("|")[2]  
            else:
                log.info("Invalid id format for "+type+" id="+str(id)+" - returning")
                return True
            client = boto3.client(clfn)
            response = client.get_web_acl(Scope=sc,Name=nm,Id=idd)
            if response == []: 
                if context.debug: 
                    log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            j=response['WebACL']
            arn=j['ARN']
            pkey=idd+"/"+nm+"/"+sc
            common.write_import(type,pkey,"w-"+pkey.replace("/","_"))
            if type not in context.all_extypes:
                common.add_dependancy("aws_wafv2_web_acl_logging_configuration",arn)
                common.add_dependancy("aws_wafv2_web_acl_association",arn)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_wafv2_rule_group(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None: # assume scope = cloudfront
            sc="CLOUDFRONT"
            if context.region == "us-east-1":
                response = client.list_rule_groups(Scope=sc)
                if response == []: 
                    if context.debug: 
                        log.debug("Empty response for "+type+ " Scope="+str(sc)+" returning")
                    return True
                for j in response[topkey]:
                    idd=j["Id"]
                    nm=j["Name"]
                    sc="CLOUDFRONT"
                    pkey=idd+"/"+nm+"/"+sc
                    common.write_import(type,pkey,"w-"+pkey.replace("/","_")) 
            else:
                log_warning("WARNING:Can only import CLOUDFRONT web ACL's from us-east-1 region")
 
            sc="REGIONAL"
            response = client.list_rule_groups(Scope=sc)
            if response[topkey] == []:
                if context.debug: 
                    log.debug("Empty response for "+type+ " Scope="+str(sc)+" returning")
                    log.info(str(response))
                return True
            
            #print(str(response))
            for j in response[topkey]:
                idd=j["Id"]
                nm=j["Name"]
                pkey=idd+"/"+nm+"/"+sc
                common.write_import(type, pkey, "w-"+pkey.replace("/", "_"))

        else: 
            if "|" in id:
                nm=id.split("|")[0]
                idd=id.split("|")[1]
                sc=id.split("|")[2]  
            else:
                log.info("Invalid id format for "+type+" id="+str(id)+" - returning")
                return True
            client = boto3.client(clfn)
            response = client.get_rule_group(Scope=sc,Name=nm,Id=idd)
            if response == []: 
                if context.debug: 
                    log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            j=response['RuleGroup']
            pkey=idd+"/"+nm+"/"+sc
            common.write_import(type,pkey,"w-"+pkey.replace("/","_"))

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

# aws_wafv2_web_acl_logging_configuration ARN
def get_aws_wafv2_web_acl_logging_configuration(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn,config=config)
        if id is None:
            log_warning("WARNING: Must pass WebACL arn as parameter")
            return True

        else:   
            try:   
                response = client.get_logging_configuration(ResourceArn=id)
            except ClientError as error:
                if error.response['Error']['Code'] == 'WAFNonexistentItemException':
                    log.info("The WAF resource you're trying to access doesn't exist.")
                    response=[]
            if response == []: 
                    if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
                    pkey=type+"."+id
                    context.rproc[pkey]=True
                    return True
            j=response['LoggingConfiguration']
            common.write_import(type,j[key],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

#aws_wafv2_web_acl_association

# needs scope

def get_aws_wafv2_web_acl_association(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn,config=config)
        if id is None:
            log.warning("Must pass webacl arn as parameter")
            return True

        else: 
            if id.startswith("arn:"):
                #rtypes=['APPLICATION_LOAD_BALANCER','API_GATEWAY','APPSYNC','COGNITO_USER_POOL','APP_RUNNER_SERVICE','VERIFIED_ACCESS_INSTANCE','AMPLIFY']
                rtypes=['APPLICATION_LOAD_BALANCER','API_GATEWAY','COGNITO_USER_POOL','APP_RUNNER_SERVICE']

                for rtype in rtypes:
                    response = client.list_resources_for_web_acl(WebACLArn=id,ResourceType=rtype)
                    if response['ResourceArns'] == []: 
                        if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" continue") 
                        continue
                    for j in response['ResourceArns']:
                        pkey=id+","+j
                        common.write_import(type,pkey,None)
                        if j.startswith("arn:aws:elasticloadbalancing"):
                            common.add_dependancy("aws_lb",j)
                pkey=type+"."+id
                context.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True
