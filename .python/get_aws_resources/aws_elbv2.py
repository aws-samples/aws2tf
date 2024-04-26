import common
import globals
import boto3
import botocore
import inspect

def get_aws_lb(type,id,clfn,descfn,topkey,key,filterid):

    if globals.debug:
        print("--> get_describe_rules  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        client = boto3.client(clfn)
        response = []
        if id is None:
            response = client.describe_load_balancers() 
        elif "arn:" in id:
            response = client.describe_load_balancers(LoadBalancerArns=[id])
        else:
            response = client.describe_load_balancers(Names=[id])
        
        response=response[topkey]
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        
        for j in response: 
            retid=j[key] # key is LoadBalancerArn
            common.write_import(type,retid,None) 
            common.add_dependancy("aws_lb_listener",retid)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_lb_listener(type,id,clfn,descfn,topkey,key,filterid):

    if globals.debug:
        print("--> get_aws_lb_listener  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        client = boto3.client(clfn)
        response = []
        if id is None:
            response = client.describe_listeners() 
        elif ":listener/" in id and id is not None:
                response = client.describe_listeners(ListenerArns=[id])
        elif ":loadbalancer/" in id and id is not None:
                response = client.describe_listeners(LoadBalancerArn=id)
   
        response=response[topkey]
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        
        for j in response: 
            retid=j[key] # ListenerARN
            common.write_import(type,retid,None) 
            common.add_dependancy("aws_lb_listener_rule",retid)
            pkey="aws_lb_listener."+id
            globals.rproc[pkey]=True


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_lb_listener_rule(type,id,clfn,descfn,topkey,key,filterid):

    if globals.debug:
        print("--> get_describe_rules  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        client = boto3.client(clfn)
        response = []
        if id is None:
            response = client.describe_rules() 
        if ":listener-rule/" in id:
            response = client.describe_rules(RuleArns=[id])
        if ":listener/" in id:
            response = client.describe_rules(ListenerArn=id)
        
        response=response[topkey]
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        
        for j in response: 
            retid=j[key] # key is RuleArn
            # is it default ?
            isdef=j['IsDefault']
            if isdef==False:
                common.write_import(type,retid,None) 
                pkey="aws_lb_listener_rule."+id
                globals.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

