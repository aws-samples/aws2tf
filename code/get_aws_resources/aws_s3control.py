import common
import boto3
import context
import inspect

def get_aws_s3_access_point(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        my_region=context.region
        if context.sso:
            session = boto3.Session(region_name=my_region,profile_name=context.profile)
            client = session.client(clfn)
        else:
            client = boto3.client(clfn)

        if id is None:
            try:
                response = client.list_access_points(AccountId=context.acc)
            except Exception as e:
                print("Access Point 1 ClientError "+str(e))
                return True
        
            for j in response[topkey]:
                pkey=context.acc+":"+j[key]
                common.write_import(type,pkey,None) 

        else:      
            try:
                response = client.list_access_points(AccountId=context.acc,Bucket=id)
            except Exception as e:    
                print("Access Point 2 ClientError "+str(e))
                print("INFO: If using endpoints - check the endpoint policy returning")
                pkey=type+"."+id
                context.rproc[pkey]=True
                return True
            if response == []: 
                print("Empty response for "+type+ " id="+str(id)+" returning")
                pkey=type+"."+id
                context.rproc[pkey]=True
                return True
            for j in response[topkey]:
                pkey=context.acc+":"+j[key]
                common.write_import(type,pkey,None)
            pkey=type+"."+id
            context.rproc[pkey]=True
             

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True