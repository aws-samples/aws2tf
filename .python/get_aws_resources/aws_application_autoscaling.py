import common
import boto3
import globals
import inspect

def get_aws_appautoscaling_target(type, id, clfn, descfn, topkey, key, filterid):


    if globals.debug:
        print("--> In get_aws_appautoscaling_target  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:

        response = []
        client = boto3.client(clfn)

        if id is None:
            response = client.describe_scalable_targets(ServiceNamespace="ecs")
        
            if response == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            #print(">>>>>>>>>>>>"+str(response))
            for j in response[topkey]:
                #print(str(j))
                sns=j['ServiceNamespace']
                rid=j['ResourceId']
                scd=j['ScalableDimension']
                pkey=sns+"/"+rid
                pkey="aws_appautoscaling_target."+sns+"/"+rid
                tid=sns+"/"+rid+"/"+scd
                common.write_import(type,tid,None)

                globals.rproc[pkey]=True

        else:
            #print("id="+id)
            if "/" in id:
                rrid=id.split("/",1)[1]
            elif "|" in id:
                rrid=id.split("|")[2]
            else:
                print("Invalid id format for "+type+" id="+str(id)+" - returning")
                return True
            #print("rrid="+rrid+ " topkey="+topkey)
            response = client.describe_scalable_targets(ServiceNamespace="ecs",ResourceIds=[rrid])
            #print("----------"+str(response))
            if response[topkey] == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning"); 
                # fix tracking
                globals.rproc[type+"."+id]=True
                return True
            #print("----------here")
            for j in response[topkey]:

                #print(str(j))
                sns=j['ServiceNamespace']
                rid=j['ResourceId']
                scd=j['ScalableDimension']
                pkey="aws_appautoscaling_target."+sns+"/"+rid
                tid=sns+"/"+rid+"/"+scd
                common.write_import(type,tid,None)
                #print("****pkey="+pkey)
                globals.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_appautoscaling_policy(type, id, clfn, descfn, topkey, key, filterid):


    if globals.debug:
        print("--> In get_aws_appautoscaling_policy  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:

        response = []
        client = boto3.client(clfn)

        if id is None:
            response = client.describe_scaling_policies(ServiceNamespace="ecs")
            #print("----------"+str(response))
            if response == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            #print(str(response))
            for j in response[topkey]:
                #print(str(j))
                sns=j['ServiceNamespace']
                rid=j['ResourceId']
                scd=j['ScalableDimension']
                pln=j['PolicyName']
                pkey=sns+"/"+rid
                pkey="aws_appautoscaling_policy."+sns+"/"+rid
                tid=sns+"/"+rid+"/"+scd+"/"+pln
                common.write_import(type,tid,None)

                globals.rproc[pkey]=True

        else:
            print(id)
            if "/" in id:
                rrid=id.split("/",1)[1]
            else: rrid=id
            print(rrid)
            response = client.describe_scaling_policies(ServiceNamespace="ecs",ResourceId=rrid)
            #print(str(response))
            if response[topkey] == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning"); 
                globals.rproc[type+"."+id]=True
                return True
            for j in response[topkey]:

                #print(str(j))
                sns=j['ServiceNamespace']
                rid=j['ResourceId']
                scd=j['ScalableDimension']
                pln=j['PolicyName']
                pkey="aws_appautoscaling_policy."+sns+"/"+rid
                tid=sns+"/"+rid+"/"+scd+"/"+pln
                common.write_import(type,tid,None)
                #print("****pkey="+pkey)
                globals.rproc[pkey]=True  

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True