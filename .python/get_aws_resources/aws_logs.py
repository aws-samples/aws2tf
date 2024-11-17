import common
import globals
import inspect
import boto3

def get_aws_cloudwatch_log_group(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_cloudwatch_log_group  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        paginator = client.get_paginator(descfn)
        if id is None:
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                logn=j[key]
                common.write_import(type,logn,None) 
                common.add_dependancy("aws_cloudwatch_log_stream", logn) 

        elif "arn:" in id:
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                if j['arn'] == id:
                    logn=j[key]
                    common.write_import(type,logn,None) 
                    common.add_dependancy("aws_cloudwatch_log_stream", logn) 

        else: # assume it's a log name
            for page in paginator.paginate(logGroupNamePattern=id):
                response = response + page[topkey]
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                logn=j[key]
                common.write_import(type,logn,None) 
                common.add_dependancy("aws_cloudwatch_log_stream", logn) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True



def get_aws_cloudwatch_log_stream(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_cloudwatch_log_stream  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        client = boto3.client(clfn)
        if id is not None:    
            response = client.describe_log_streams(logGroupName=id)
            if response[topkey] == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                pkey=type+"."+id
                globals.rproc[pkey]=True
                return True
            for j in response[topkey]:
                sn = j[key]
                lgn=id
                theid=lgn+":"+sn
                common.write_import(type, theid, None)
            pkey=type+"."+id
            globals.rproc[pkey]=True
 
        else:
            print("WARNING: No id provided for get_aws_cloudwatch_log_stream")
            return True
    
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True
