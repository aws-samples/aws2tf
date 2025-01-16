import common
import boto3
import globals
import inspect

def get_aws_batch_scheduling_policy(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
      
        response = client.list_scheduling_policies()
        if response == []: 
            print("Empty response for "+type+ " id="+str(id)+" returning")
            return True
        for j in response['schedulingPolicies']:
            #print(str(j['arn']))
            common.write_import(type,j['arn'],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_batch_job_definition(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
      
        response = client.describe_job_definitions()
        if response == []: 
            print("Empty response for "+type+ " id="+str(id)+" returning")
            return True
        for j in response[topkey]:
            if j['status']!="INACTIVE":
                common.write_import(type,j[key],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True