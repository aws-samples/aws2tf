import common
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect

def get_aws_cloudwatch_event_bus(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_event_buses()
            if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                if j[key] != "default":
                    common.write_import(type,j[key],None) 
                    common.add_dependancy("aws_cloudwatch_event_rule",j[key])
                else:
                    common.add_dependancy("aws_cloudwatch_event_rule","default")

        else:   
            if id != "default":   
                response = client.describe_event_bus(Name=id)
                if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
                j=response
                common.write_import(type,j[key],None)
                common.add_dependancy("aws_cloudwatch_event_rule",j[key])
            else:
                common.add_dependancy("aws_cloudwatch_event_rule", "default")

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_cloudwatch_event_rule(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        #event_bus_name
        if id is None:
            log.warning("WARNING: Muse pass event_bus_name as a parameter returning")
            return True
        else:  
                if id == "default":
                    response = client.list_rules(EventBusName=id)
                    if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
                    for j in response[topkey]:
                #event_bus_name/rule-name
                        pkey=id+"/"+j[key]
                        common.write_import(type,pkey,None)
                        common.add_dependancy("aws_cloudwatch_event_target", pkey)
                    pkey="aws_cloudwatch_event_rule."+id
                    context.rproc[pkey] = True
                else:
                    try:
                        response = client.describe_rule(Name=id)
                    except Exception as e:
                        log.warning("WARNING: "+str(e)+" for "+type+ " id="+str(id)+" returning")
                        log.info("ADVICE: Check if: "+type+ " id="+str(id)+" actually exists ?")
                        log.info("ADVICE: Check what other resources may be referring to this resource if it doesn't exist")
                        pkey="aws_cloudwatch_event_rule."+id
                        context.rproc[pkey] = True
                        return True
                    #print(str(response))
                    j=response
                #event_bus_name/rule-name
                    pkey=j['EventBusName']+"/"+j[key]
                    common.write_import(type,pkey,None)
                    common.add_dependancy("aws_cloudwatch_event_target", pkey)
                    pkey="aws_cloudwatch_event_rule."+id
                    context.rproc[pkey] = True



    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_cloudwatch_event_target(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        #event_bus_name/rule-name/target-id
        if id is None:
            log.warning("WARNING: Must pass event_bus_name/rule-name as a parameter returning")
            return True

        else:   
            if "/" in id:    
                rn=id.split("/")[1]; 
                ebn=id.split("/")[0]
                if not ebn.startswith("aws."):
                    response = client.list_targets_by_rule(EventBusName=ebn,Rule=rn)
                    
                    if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
                    for j in response[topkey]:
                    #event_bus_name/rule-name/target-id
                        pkey=id+"/"+j[key]
                        common.write_import(type,pkey,None)
                pkey="aws_cloudwatch_event_target."+id
                context.rproc[pkey] = True
            else:
                log.warning("WARNING: Must pass event_bus_name/rule-name as a parameter returning")

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True
    
