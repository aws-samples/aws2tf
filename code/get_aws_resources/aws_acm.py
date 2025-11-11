import common
import boto3
import context
import inspect

def get_aws_acm_certificate(type, id, clfn, descfn, topkey, key, filterid):
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
            if response == []: 
                if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            for j in response:
                if j['Status']=="ISSUED":
                    common.write_import(type,j[key],None) 
                else:
                    print("Skipping ACM Certificate "+str(j[key])+" as status is "+str(j['Status']))

        elif id.startswith("arn:"):      
            response = client.describe_certificate(CertificateArn=id)
            if response == []: 
                if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            j=response['Certificate']
            if j['Status']=="ISSUED":
                common.write_import(type,id,None)

        else:
            print("Unhandled id type for "+type+" id="+str(id))            

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True