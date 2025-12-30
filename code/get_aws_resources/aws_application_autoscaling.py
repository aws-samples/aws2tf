import common
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect

def get_aws_appautoscaling_target(type, id, clfn, descfn, topkey, key, filterid):


    if context.debug:
        log.debug("--> In get_aws_appautoscaling_target  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:

        response = []
        client = boto3.client(clfn)

        if id is None:
            response = client.describe_scalable_targets(ServiceNamespace="ecs")
        
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
    
            for j in response[topkey]:
     
                sns=j['ServiceNamespace']
                rid=j['ResourceId']
                scd=j['ScalableDimension']
                pkey=sns+"/"+rid
                pkey="aws_appautoscaling_target."+sns+"/"+rid
                tid=sns+"/"+rid+"/"+scd
                common.write_import(type,tid,None)

                context.rproc[pkey]=True

        else:
       
            if "/" in id:
                rrid=id.split("/",1)[1]
            elif "|" in id:
                rrid=id.split("|")[2]
            else:
                log.info("Invalid id format for "+type+" id="+str(id)+" - returning")
                return True
 
            response = client.describe_scalable_targets(ServiceNamespace="ecs",ResourceIds=[rrid])

            if response[topkey] == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                # fix tracking
                context.rproc[type+"."+id]=True
                return True

            for j in response[topkey]:


                sns=j['ServiceNamespace']
                rid=j['ResourceId']
                scd=j['ScalableDimension']
                pkey="aws_appautoscaling_target."+sns+"/"+rid
                tid=sns+"/"+rid+"/"+scd
                common.write_import(type,tid,None)
     
                context.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_appautoscaling_policy(type, id, clfn, descfn, topkey, key, filterid):


    if context.debug:
        log.debug("--> In get_aws_appautoscaling_policy  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:

        response = []
        client = boto3.client(clfn)

        if id is None:
            response = client.describe_scaling_policies(ServiceNamespace="ecs")

            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True

            for j in response[topkey]:

                sns=j['ServiceNamespace']
                rid=j['ResourceId']
                scd=j['ScalableDimension']
                pln=j['PolicyName']
                pkey=sns+"/"+rid
                pkey="aws_appautoscaling_policy."+sns+"/"+rid
                tid=sns+"/"+rid+"/"+scd+"/"+pln
                common.write_import(type,tid,None)

                context.rproc[pkey]=True

        else:

            if "/" in id:
                rrid=id.split("/",1)[1]
            else: rrid=id

            response = client.describe_scaling_policies(ServiceNamespace="ecs",ResourceId=rrid)
      
            if response[topkey] == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                context.rproc[type+"."+id]=True
                return True
            for j in response[topkey]:

 
                sns=j['ServiceNamespace']
                rid=j['ResourceId']
                scd=j['ScalableDimension']
                pln=j['PolicyName']
                pkey="aws_appautoscaling_policy."+sns+"/"+rid
                tid=sns+"/"+rid+"/"+scd+"/"+pln
                common.write_import(type,tid,None)
         
                context.rproc[pkey]=True  

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True