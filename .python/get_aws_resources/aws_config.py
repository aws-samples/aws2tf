import common
import globals
import os
import sys
import inspect

# "$AWS configservice describe-config-rules  --config-rule-names $1"
def get_aws_config_config_rule(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_config_config_rule  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = common.call_boto3(type,clfn, descfn, topkey, key, id)
        #print("-9a->"+str(response))
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True

        if id is None:
            for j in response:
                retid = j[key]
                theid = retid
                common.write_import(type, theid, id)
        else:
            for j in response:
                retid = j[key]
                if id == retid:
                    theid = retid
                    common.write_import(type, theid, id)
                    

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True
