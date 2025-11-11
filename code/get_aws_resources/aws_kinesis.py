import common
import boto3
import context
import inspect


def get_aws_kinesis_stream(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        print("--> In get_aws_kinesis_stream  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:

        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                common.write_import(type,j[key],None) 

        else:   
            response = client.describe_stream(StreamName=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response['StreamDescription']
            common.write_import(type,j[key],None)


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True