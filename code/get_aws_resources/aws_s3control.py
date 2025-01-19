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
        client = boto3.client(clfn)
        if id is None:
            response = client.list_access_points(AccountId=globals.acc)
        
            for j in response[topkey]:
                pkey=globals.acc+":"+j[key]
                common.write_import(type,pkey,None) 

        else:      
            response = client.list_access_points(AccountId=globals.acc,Bucket=id)
            if response == []: 
                print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response[topkey]:
                pkey=globals.acc+":"+j[key]
                common.write_import(type,pkey,None)
            pkey=type+"."+id
            globals.rproc[pkey]=True
             

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True