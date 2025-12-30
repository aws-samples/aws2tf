import common
from common import log_warning
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect
import sys


def get_aws_connect_instance(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []:
                if context.debug: log.debug("Empty response for "+type + " id="+str(id)+" returning")
                return True
            for j in response:
                common.write_import(type, j[key], "r-"+j[key])
                common.add_dependancy("aws_connect_instance_storage_config", j[key])
                common.add_dependancy("aws_connect_phone_number", j[key])
                common.add_dependancy("aws_connect_hours_of_operation", j[key])
                common.add_dependancy("aws_connect_contact_flow", j[key])
                common.add_dependancy("aws_connect_queue", j[key])
                common.add_dependancy("aws_connect_routing_profile", j[key])
                common.add_dependancy("aws_connect_security_profile", j[key])
                common.add_dependancy("aws_connect_user", j[key])
                common.add_dependancy("aws_connect_vocabulary", j[key])
                common.add_dependancy("aws_connect_bot_association", j[key])
                common.add_dependancy("aws_connect_lambda_function_association", j[key])

        else:
            response = client.describe_instance(InstanceId=id)
            if response == []:
                if context.debug: log.debug("Empty response for "+type + " id="+str(id)+" returning")
                return True
            j = response['Instance']
            common.write_import(type, j[key], "r-"+j[key])
            common.add_dependancy("aws_connect_instance_storage_config", j[key])
            common.add_dependancy("aws_connect_phone_number", j[key])
            common.add_dependancy("aws_connect_hours_of_operation", j[key])
            common.add_dependancy("aws_connect_contact_flow", j[key])
            common.add_dependancy("aws_connect_queue", j[key])
            common.add_dependancy("aws_connect_routing_profile", j[key])
            common.add_dependancy("aws_connect_security_profile", j[key])
            common.add_dependancy("aws_connect_user", j[key])
            common.add_dependancy("aws_connect_vocabulary", j[key])
            common.add_dependancy("aws_connect_bot_association", j[key])
            common.add_dependancy("aws_connect_lambda_function_association", j[key])

    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True


def get_aws_connect_instance_storage_config(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        if id is None:
            log.debug("Must pass instanceid for "+type)
            return True
        else:
            client = boto3.client(clfn)
            paginator = client.get_paginator(descfn)
            associds = ""
            pkey = type+"."+id
            #ResourceType = ['CHAT_TRANSCRIPTS', 'CALL_RECORDINGS', 'SCHEDULED_REPORTS', 'MEDIA_STREAMS', 'CONTACT_TRACE_RECORDS', 'AGENT_EVENTS', 'REAL_TIME_CONTACT_ANALYSIS_SEGMENTS',
            #                'ATTACHMENTS', 'CONTACT_EVALUATIONS', 'SCREEN_RECORDINGS', 'REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS', 'REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS']
            ResourceType = ['CHAT_TRANSCRIPTS', 'CALL_RECORDINGS', 'SCHEDULED_REPORTS', 'CONTACT_TRACE_RECORDS']
            for rt in ResourceType:
                for page in paginator.paginate(InstanceId=id, ResourceType=rt):
                    response = response + page[topkey]
                if response == []:
                    if context.debug: log.debug("Empty response for "+type + " id="+str(id)+" returning")
                    context.rproc[pkey] = True
                    return True
                for j in response:
                    if j['AssociationId'] not in associds:
                        theid = id+":"+j['AssociationId']+":"+rt
                        common.write_import(type, theid, "r-"+theid)
                        associds = associds+":"+j['AssociationId']

            associds = ""
            context.rproc[pkey] = True
    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True


def get_aws_connect_phone_number(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []

        if id is None:
            log.debug("Must pass instanceid for "+type)
            return True

        else:
            client = boto3.client(clfn)
            paginator = client.get_paginator(descfn)
            pkey = type+"."+id

            for page in paginator.paginate(InstanceId=id):
                response = response + page[topkey]
            if response == []:
                if context.debug: log.debug("Empty response for "+type + " id="+str(id)+" returning")
                context.rproc[pkey] = True
                return True
            for j in response:
                theid = j[key]
                common.write_import(type, theid, "r-"+theid)

            context.rproc[pkey] = True
    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True



def get_aws_connect_hours_of_operation(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []

        if id is None:
            log.debug("Must pass instanceid for "+type)
            return True

        else:
            client = boto3.client(clfn)
            paginator = client.get_paginator(descfn)
            pkey = type+"."+id

            for page in paginator.paginate(InstanceId=id):
                response = response + page[topkey]
            if response == []:
                if context.debug: log.debug("Empty response for "+type + " id="+str(id)+" returning")
                context.rproc[pkey] = True
                return True
            for j in response:
                theid = id+":"+j[key]
                common.write_import(type, theid, "r-"+theid)

            context.rproc[pkey] = True
    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True



# aws_connect_contact_flow
def get_aws_connect_contact_flow(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []

        if id is None:
            log.debug("Must pass instanceid for "+type)
            return True

        else:
            client = boto3.client(clfn)
            paginator = client.get_paginator(descfn)
            pkey = type+"."+id
            #ContactFlowTypes=['CONTACT_FLOW','CUSTOMER_QUEUE','CUSTOMER_HOLD','CUSTOMER_WHISPER','AGENT_HOLD','AGENT_WHISPER','OUTBOUND_WHISPER','AGENT_TRANSFER','QUEUE_TRANSFER']
            for page in paginator.paginate(InstanceId=id):
                response = response + page[topkey]
            if response == []:
                if context.debug: log.debug("Empty response for "+type + " id="+str(id)+" returning")
                context.rproc[pkey] = True
                return True
            for j in response:
                theid = id+":"+j[key]
                common.write_import(type, theid, "r-"+theid)

            context.rproc[pkey] = True
    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True


def get_aws_connect_queue(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []

        if id is None:
            log.debug("Must pass instanceid for "+type)
            return True

        else:
            client = boto3.client(clfn)
            paginator = client.get_paginator(descfn)
            pkey = type+"."+id
            for page in paginator.paginate(InstanceId=id,QueueTypes=['STANDARD']):
                response = response + page[topkey]
            if response == []:
                if context.debug: log.debug("Empty response for "+type + " id="+str(id)+" returning")
                context.rproc[pkey] = True
                return True
            for j in response:
                theid = id+":"+j[key]
                #qn=j['Name']
                #if qn != "BasicQueue":
                common.write_import(type, theid, "r-"+theid)

            context.rproc[pkey] = True
    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True

#aws_connect_routing_profile

def get_aws_connect_routing_profile(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []

        if id is None:
            log.debug("Must pass instanceid for "+type)
            return True

        else:
            client = boto3.client(clfn)
            paginator = client.get_paginator(descfn)
            pkey = type+"."+id
            for page in paginator.paginate(InstanceId=id):
                response = response + page[topkey]
            if response == []:
                if context.debug: log.debug("Empty response for "+type + " id="+str(id)+" returning")
                context.rproc[pkey] = True
                return True
            for j in response:
                #resp2=client.describe_routing_profile(InstanceId=id,RoutingProfileId=j[key])
                theid = id+":"+j[key]
                common.write_import(type, theid, "r-"+theid)

            context.rproc[pkey] = True
    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True

#aws_connect_security_profile
def get_aws_connect_security_profile(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []

        if id is None:
            log.debug("Must pass instanceid for "+type)
            return True

        else:
            client = boto3.client(clfn)
            paginator = client.get_paginator(descfn)
            pkey = type+"."+id
            for page in paginator.paginate(InstanceId=id):
                response = response + page[topkey]
            if response == []:
                if context.debug: log.debug("Empty response for "+type + " id="+str(id)+" returning")
                context.rproc[pkey] = True
                return True
            for j in response:
                theid = id+":"+j[key]
                common.write_import(type, theid, "r-"+theid)

            context.rproc[pkey] = True
    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True

#aws_connect_user
def get_aws_connect_user(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []

        if id is None:
            log.debug("Must pass instanceid for "+type)
            return True

        else:
            client = boto3.client(clfn)
            paginator = client.get_paginator(descfn)
            pkey = type+"."+id
            for page in paginator.paginate(InstanceId=id):
                response = response + page[topkey]
            if response == []:
                if context.debug: log.debug("Empty response for "+type + " id="+str(id)+" returning")
                context.rproc[pkey] = True
                return True
            for j in response:
                theid = id+":"+j[key]
                common.write_import(type, theid, "r-"+theid)

            context.rproc[pkey] = True
    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True

# aws_connect_vocabulary
#AccessDeniedException exception for aws_connect.py - returning
# ERROR: Not found aws_connect_vocabulary.4de80d0a-3f95-4475-a7bb-86236b92d13c - check if this resource still exists in AWS. Also check what resource is using it - grep the *.tf files in the generated/tf.* subdirectory

def get_aws_connect_vocabulary(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []

        if id is None:
            log.debug("Must pass instanceid for "+type)
            return True

        else:
            try:
                client = boto3.client(clfn)
                paginator = client.get_paginator(descfn)
                pkey = type+"."+id
                for page in paginator.paginate(InstanceId=id,State='ACTIVE'):
                    response = response + page[topkey]
                if response == []:
                    if context.debug: log.debug("Empty response for "+type + " id="+str(id)+" returning")
                    context.rproc[pkey] = True
                    return True
                for j in response:
                    theid = id+":"+j[key]
                    common.write_import(type, theid, "r-"+theid)

                context.rproc[pkey] = True
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                exn=str(exc_type.__name__)
                if exn == "AccessDeniedException":
                    pkey = type+"."+id
                    context.rproc[pkey] = True
                    return True

    except Exception as e:

        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True




# aws_connect_bot_association

def get_aws_connect_bot_association(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []

        if id is None:
            log.debug("Must pass instanceid for "+type)
            return True

        else:
            client = boto3.client(clfn)
            paginator = client.get_paginator(descfn)
            pkey = type+"."+id
      
            for page in paginator.paginate(InstanceId=id,LexVersion='V1'):
                response = response + page[topkey]
          
            if response == []:
                if context.debug: log.debug("Empty response for "+type + " id="+str(id)+" returning")
                context.rproc[pkey] = True
                return True
            for j in response:
                botn=j['LexBot'][key]
                botr=j['LexBot']['LexRegion']
                theid = id+":"+botn+":"+botr
                common.write_import(type, theid, "r-"+theid)

            context.rproc[pkey] = True
    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True


# aws_connect_contact_flow_module
# aws_connect_lambda_function_association
def get_aws_connect_lambda_function_association(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []

        if id is None:
            log.debug("Must pass instanceid for "+type)
            return True

        else:
            client = boto3.client(clfn)
            paginator = client.get_paginator(descfn)
            pkey = type+"."+id
            for page in paginator.paginate(InstanceId=id):
                response = response + page[topkey]
            if response == []:
                if context.debug: log.debug("Empty response for "+type + " id="+str(id)+" returning")
                context.rproc[pkey] = True
                return True
            
            for j in response:
                if j.startswith("arn:aws:lambda:"):
                    theid = id+","+j
                    common.write_import(type, theid, "r-"+theid)
                    fn=j.split(":")[-1]
                    common.add_dependancy("aws_lambda_function",fn)

            context.rproc[pkey] = True
    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True


# aws_connect_quick_connect
# aws_connect_user_hierarchy_group
# aws_connect_user_hierarchy_structure