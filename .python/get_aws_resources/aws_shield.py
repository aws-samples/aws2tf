import common
import boto3
import globals
import inspect

def get_aws_shield_protection_group(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            try:
                response = client.list_protection_groups()
            except Exception as e:
                print("No shield protection groups")
                return True
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                common.write_import(type,j[key],None) 

        else:      
            response = client.describe_protection_groups(ProtectionGroupId=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response['ProtectionGroup']
      
            common.write_import(type,j[key],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True