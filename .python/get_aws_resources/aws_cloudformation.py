import common
import boto3
import globals
import inspect

def get_aws_cloudformation_stack(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(StackStatusFilter=['CREATE_COMPLETE']):
                response = response + page[topkey]
            if response == []: 
                print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                common.write_import(type,j[key],None) 

        else:      
            response = client.describe_stacks(StackName=id)
            if response['Stacks'] == []: 
                print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response['Stacks']:
                #print(j)
                stat=j['StackStatus']
                if stat == "CREATE_COMPLETE":
                    common.write_import(type,j[key],None)
                else:
                    print("Stack "+id+" status is "+stat+" so skipping")

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True