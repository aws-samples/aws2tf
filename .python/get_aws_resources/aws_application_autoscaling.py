import common
import boto3
import globals
import os
import sys

def get_aws_appautoscaling_target(type, id, clfn, descfn, topkey, key, filterid):


    #if globals.debug:
    print("--> In get_aws_appautoscaling_target  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:

        response = []
        client = boto3.client(clfn)

        if id is None:
            response = client.describe_scalable_targets(ServiceNamespace="ecs")
        
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            print(str(response))
            for j in response[topkey]:
                print(str(j))
                sns=j['ServiceNamespace']
                rid=j['ResourceId']
                scd=j['ScalableDimension']
                pkey=sns+"/"+rid
                pkey="aws_appautoscaling_target."+sns+"/"+rid
                tid=sns+"/"+rid+"/"+scd
                common.write_import(type,tid,None)

                globals.rproc[pkey]=True

        else:
            print(id)
            rrid=id.split("/",1)[1]
            print(rrid)
            response = client.describe_scalable_targets(ServiceNamespace="ecs",ResourceIds=[rrid])
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:

                print(str(j))
                sns=j['ServiceNamespace']
                rid=j['ResourceId']
                scd=j['ScalableDimension']
                pkey="aws_appautoscaling_target."+sns+"/"+rid
                tid=sns+"/"+rid+"/"+scd
                common.write_import(type,tid,None)
                print("****pkey="+pkey)
                globals.rproc[pkey]=True

    except Exception as e:
            print(f"{e=}")
            print("ERROR: -2->unexpected error in get_aws_appautoscaling_target")
            print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            exit()

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
        
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
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
            #print(id)
            rrid=id.split("/",1)[1]
            #print(rrid)
            response = client.describe_scaling_policies(ServiceNamespace="ecs",ResourceId=rrid)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
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
            print(f"{e=}")
            print("ERROR: -2->unexpected error in get_aws_appautoscaling_policy")
            print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            exit()

    return True