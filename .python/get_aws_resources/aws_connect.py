import common
import boto3
import globals
import inspect


def get_aws_connect_instance(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []:
                print("Empty response for "+type + " id="+str(id)+" returning")
                return True
            for j in response:
                common.write_import(type, j[key], "r-"+j[key])
                common.add_dependancy("aws_connect_instance_storage_config", j[key])
                common.add_dependancy("aws_connect_phone_number", j[key])

        else:
            response = client.describe_instance(InstanceId=id)
            if response == []:
                print("Empty response for "+type + " id="+str(id)+" returning")
                return True
            j = response['Instance']
            common.write_import(type, j[key], "r-"+j[key])
            common.add_dependancy("aws_connect_instance_storage_config", j[key])
            common.add_dependancy("aws_connect_phone_number", j[key])

    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True


def get_aws_connect_instance_storage_config(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []

        if id is None:
            print("Must pass instanceid for "+type)
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
                    print("Empty response for "+type +
                          " id="+str(id)+" returning")
                    return True
                for j in response:
                    if j['AssociationId'] not in associds:
                        theid = id+":"+j['AssociationId']+":"+rt
                        common.write_import(type, theid, "r-"+theid)
                        associds = associds+":"+j['AssociationId']

            associds = ""
            globals.rproc[pkey] = True
    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True


def get_aws_connect_phone_number(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []

        if id is None:
            print("Must pass instanceid for "+type)
            return True

        else:
            client = boto3.client(clfn)
            paginator = client.get_paginator(descfn)
            pkey = type+"."+id

            for page in paginator.paginate(InstanceId=id):
                response = response + page[topkey]
            if response == []:
                print("Empty response for "+type + " id="+str(id)+" returning")
                return True
            for j in response:
                theid = j[key]
                common.write_import(type, theid, "r-"+theid)

            globals.rproc[pkey] = True
    except Exception as e:
        common.handle_error(
            e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True
