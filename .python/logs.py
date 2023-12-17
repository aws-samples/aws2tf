import common
import globals
import os
import sys


def get_aws_cloudwatch_log_group(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_cloudwatch_log_group  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    response = common.call_boto3(clfn, descfn, topkey, id)
    print("-9a->"+str(response))
    try:
        if response == []:
            print("empty response returning")
            return
        if id is not None:
            if "arn:" in id:
                for j in response:
                    tarn = j['arn']
                    if tarn == id:
                        retid = j[key]
                        theid = retid
                        common.write_import(type, theid, id)
            else:
                for j in response:
                    tnam = j['logGroupName']
                    if tnam == id:
                        retid = j[key]
                        theid = retid
                        common.write_import(type, theid, id)
        else:
            for j in response:
                retid = j[key]
                theid = retid
                common.write_import(type, theid, id)
    
    except Exception as e:
        print(f"{e=}")
        print("unexpected error in common.getresource")
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        exit()

