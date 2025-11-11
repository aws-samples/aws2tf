import common
import boto3
import context
import inspect

def get_aws_guardduty_detector(type, id, clfn, descfn, topkey, key, filterid):
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
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            #print(str(response))
            for j in response:
                common.write_import(type,j,"d-"+j) 

        else:      
            response = client.get_detector(DetectorId=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            common.write_import(type,id,"d-"+id)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True