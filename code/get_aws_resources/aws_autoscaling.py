
import common
import boto3
import context
import inspect

def get_aws_autoscaling_group(type, id, clfn, descfn, topkey, key, filterid):    
    if context.debug:
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
                if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                common.write_import(type,j[key],None) 

        else:
            if id.startswith("arn:aws:autoscaling:"): 
                qid = id.split("/")[-1]
            else:
                qid = id
            pkey=type+"."+id
            if context.debug: print("Looking for "+pkey)
            response = client.describe_auto_scaling_groups(AutoScalingGroupNames=[qid])
            if response == []: 
                if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
                context.rproc[pkey] = True
                return True
            for j in response[topkey]:
                common.write_import(type,j[key],None)
            context.rproc[pkey] = True
            
    except Exception as e:
            common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
            
    return True