import common
import boto3
import globals
import inspect

def get_aws_s3_access_point(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        my_region=globals.region
        if globals.sso:
            session = boto3.Session(region_name=my_region,profile_name=globals.profile)
            client = session.client(clfn)
        else:
            client = boto3.client(clfn)

        if id is None:
            try:
                response = client.list_access_points(AccountId=globals.acc)
            except Exception as e:
                print("Access Point 1 ClientError "+str(e))
                return True
        
            for j in response[topkey]:
                pkey=globals.acc+":"+j[key]
                common.write_import(type,pkey,None) 

        else:      
            try:
                response = client.list_access_points(AccountId=globals.acc,Bucket=id)
            except Exception as e:    
                print("Access Point 2 ClientError "+str(e))
                pkey=type+"."+id
                globals.rproc[pkey]=True
                return True
            if response == []: 
                print("Empty response for "+type+ " id="+str(id)+" returning")
                pkey=type+"."+id
                globals.rproc[pkey]=True
                return True
            for j in response[topkey]:
                pkey=globals.acc+":"+j[key]
                common.write_import(type,pkey,None)
            pkey=type+"."+id
            globals.rproc[pkey]=True
             

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True