import common
import boto3
import globals
import inspect

def get_aws_codeguruprofiler_profiling_group(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_profiling_groups(includeDescription=False)
            response=response[topkey]
            #print(str(response))
            if response == []: 
                print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                common.write_import(type,j,None) 

        else:      
            response = client.describe_profiling_group(profilingGroupName=id)
            if response == []: 
                print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            j=response
            common.write_import(type,j['profilingGroup']['name'],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True