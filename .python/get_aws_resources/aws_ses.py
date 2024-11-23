import common
import boto3
import globals
import inspect

def get_aws_ses_active_receipt_rule_set(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)

        response=client.describe_active_receipt_rule_set()
        try:
                if response[topkey] == []: 
                    print("Empty response for "+type+ " id="+str(id)+" returning")
                    return True
        except Exception as e:
                print("No ses rule sets returning "+type)
                return True
            
        for j in response[topkey]:
            common.write_import(type,j[key],None) 



    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True