import common
from common import log_warning
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
            if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                if j[key] != "default":
                    common.write_import(type,j[key],None) 
                    common.add_dependancy("aws_cloudwatch_event_rule",j[key])
                else:
                    common.add_dependancy("aws_cloudwatch_event_rule","default")

        else:   
            if id != "default":   
                response = client.describe_event_bus(Name=id)
                if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
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
            log_warning("WARNING: Muse pass event_bus_name as a parameter returning")
            return True
        else:  
                if id == "default":
                    response = client.list_rules(EventBusName=id)
                    if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
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
                        log_warning("WARNING: "+str(e)+" for "+type+ " id="+str(id)+" returning")
                        log.debug("ADVICE: Check if: "+type+ " id="+str(id)+" actually exists ?")
                        log.debug("ADVICE: Check what other resources may be referring to this resource if it doesn't exist")
                        pkey="aws_cloudwatch_event_rule."+id
                        context.rproc[pkey] = True
                        return True
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
            log_warning("WARNING: Must pass event_bus_name/rule-name as a parameter returning")
            return True

        else:   
            if "/" in id:    
                rn=id.split("/")[1]; 
                ebn=id.split("/")[0]
                if not ebn.startswith("aws."):
                    response = client.list_targets_by_rule(EventBusName=ebn,Rule=rn)
                    
                    if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
                    for j in response[topkey]:
                    #event_bus_name/rule-name/target-id
                        pkey=id+"/"+j[key]
                        common.write_import(type,pkey,None)
                pkey="aws_cloudwatch_event_target."+id
                context.rproc[pkey] = True
            else:
                log_warning("WARNING: Must pass event_bus_name/rule-name as a parameter returning")

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True
    


def get_aws_cloudwatch_event_bus_policy(type, id, clfn, descfn, topkey, key, filterid):
    """
    Get event bus policies by iterating through event buses and checking for policies
    """
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        client = boto3.client(clfn)
        
        if id is None:
            # List all event buses and check for policies
            response = client.list_event_buses()
            if response == []: 
                log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            
            for bus in response['EventBuses']:
                bus_name = bus['Name']
                try:
                    # Try to get the policy for this event bus
                    bus_details = client.describe_event_bus(Name=bus_name)
                    if 'Policy' in bus_details and bus_details['Policy']:
                        # Policy exists for this bus
                        common.write_import(type, bus_name, None)
                except Exception as e:
                    if context.debug:
                        log.debug(f"No policy for event bus {bus_name}: {e}")
                    continue
        else:
            # Get specific event bus policy
            response = client.describe_event_bus(Name=id)
            if 'Policy' in response and response['Policy']:
                common.write_import(type, id, None)
            else:
                log_warning(f"No policy found for event bus {id}")

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_cloudwatch_event_permission(type, id, clfn, descfn, topkey, key, filterid):
    """
    Get event permissions with composite ID support (event-bus-name/statement-id)
    Permissions are stored as statements in the event bus policy
    """
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        import json
        client = boto3.client(clfn)
        
        if id is None:
            # List all event buses and extract permissions from their policies
            response = client.list_event_buses()
            if response == []: 
                log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            
            for bus in response['EventBuses']:
                bus_name = bus['Name']
                try:
                    # Get the policy for this event bus
                    bus_details = client.describe_event_bus(Name=bus_name)
                    if 'Policy' in bus_details and bus_details['Policy']:
                        # Parse the policy JSON to extract statement IDs
                        policy = json.loads(bus_details['Policy'])
                        if 'Statement' in policy:
                            for statement in policy['Statement']:
                                if 'Sid' in statement:
                                    statement_id = statement['Sid']
                                    # Build composite ID: event-bus-name/statement-id
                                    composite_id = bus_name + '/' + statement_id
                                    common.write_import(type, composite_id, None)
                except Exception as e:
                    if context.debug:
                        log.debug(f"Error processing event bus {bus_name}: {e}")
                    continue
        else:
            # Handle composite ID in specific import
            if '/' in id:
                bus_name, statement_id = id.split('/', 1)
                try:
                    # Verify the permission exists
                    bus_details = client.describe_event_bus(Name=bus_name)
                    if 'Policy' in bus_details and bus_details['Policy']:
                        policy = json.loads(bus_details['Policy'])
                        if 'Statement' in policy:
                            for statement in policy['Statement']:
                                if statement.get('Sid') == statement_id:
                                    common.write_import(type, id, None)
                                    break
                except Exception as e:
                    if context.debug:
                        log.debug(f"Error getting permission {id}: {e}")
            else:
                log_warning(f"Invalid ID format for {type}: expected event-bus-name/statement-id, got {id}")

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True
