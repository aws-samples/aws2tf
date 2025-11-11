import common
import context
import boto3
import botocore
import inspect

def get_aws_ecs_cluster(type,id,clfn,descfn,topkey,key,filterid):

    if context.debug:
        print("--> get_aws_ecs_cluster  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        
        response = []
        response=common.call_boto3(type,clfn,descfn,topkey,key,id)
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        
        for j in response: 
            retid=j # no key
            
            cln=retid.split('/')[1]
            common.write_import(type,cln,None) 
            common.add_known_dependancy("aws_ecs_service",cln)
            common.add_known_dependancy("aws_ecs_capacity_provider",cln)
            common.add_known_dependancy("aws_ecs_cluster_capacity_providers",cln)
    

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)


    return True


def get_aws_ecs_service(type,id,clfn,descfn,topkey,key,filterid):

    if context.debug:
        print("--> get_aws_ecs_service  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if "arn:" in id:

            cln=id.split('/')[-2]
            srvn=id.split('/')[-1]
            response = client.describe_services(cluster=cln,services=[srvn])
            response=response['services']
            for j in response: 
                pkey=cln+"/"+srvn   # clustername/servicename
                common.write_import(type,pkey,None) 
                tid="ecs/service/"+pkey
                common.add_dependancy("aws_appautoscaling_target",tid)
                common.add_dependancy("aws_appautoscaling_policy",tid)
                return True


        elif id is None:         
            response = client.list_services()
        else:
            response = client.list_services(cluster=id) 

        response=response[topkey]
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        
        # a list of arns is returned
        
        for j in response: 
            retid=j # no key
            srvn=retid.split('/')[-1]
            cln=retid.split('/')[-2]

            pkey=cln+"/"+srvn   # clustername/servicename
            common.write_import(type,pkey,None) 
            tid="ecs/service/"+pkey

            common.add_dependancy("aws_appautoscaling_target",tid)
            common.add_dependancy("aws_appautoscaling_policy",tid)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_ecs_task_definition(type,id,clfn,descfn,topkey,key,filterid):

    if context.debug:
        print("--> get_aws_ecs_task_definition  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:         
            #print("ERROR: must pass task id as parameter for "+type)
            response = client.list_task_definitions()
            response=response['taskDefinitionArns']
        else:
            tid=id
            if "arn:" in id:
                 tid=id.split(":")[-2]+":"+id.split(":")[-1]
                
            response = client.describe_task_definition(taskDefinition=tid) 
            response=response[topkey]

        
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        #print(str(response))
        if id is None:
            for j in response: 
                pkey=j
                common.write_import(type,pkey,None) 
        else:
            pkey=response['taskDefinitionArn']
            common.write_import(type,pkey,None) 
            context.rproc["aws_ecs_task_definition."+id]=True


    except botocore.exceptions.ClientError as err:
         print("Cannot find Task desciption with decription" + id)
         return True
         
    
    except Exception as e:
        if "Unable to describe task definition" in e:
            print("ERROR: -1->"+e)
            return True
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_ecs_capacity_provider(type,id,clfn,descfn,topkey,key,filterid):

    if context.debug:
        print("--> get_aws_ecs_capacity_provider  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            print("WARNING: must pass cluster id as parameter for "+type)
            return True
        else:
            response = client.describe_capacity_providers()
            response=response[topkey]
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True

            for j in response: 
                pkey=j[key]
                if "FARGATE" not in pkey:    
                    common.write_import(type,pkey,None) 

    
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_ecs_cluster_capacity_providers(type,id,clfn,descfn,topkey,key,filterid):

    if context.debug:
        print("--> get_aws_ecs_cluster_capacity_provider  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            print("WARNING: must pass cluster id as parameter for "+type)
            return True
        else:
            response = client.describe_capacity_providers()
            response=response[topkey]
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True

            common.write_import(type,id,None) 


    
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True
