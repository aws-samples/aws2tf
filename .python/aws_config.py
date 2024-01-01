import common
import globals
import os
import sys

# "$AWS configservice describe-config-rules  --config-rule-names $1"
def get_aws_config_config_rule(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_config_config_rule  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = common.call_boto3(clfn, descfn, topkey, id)
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
        print(f"{e=}")
        print("unexpected error in common.getresource")
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        exit()

    return True
