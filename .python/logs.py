import common
import globals

def get_aws_cloudwatch_log_group(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_config_config_rule  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    response = common.call_boto3(clfn, descfn, topkey, id)
    # print("-9a->"+str(response))
    if response == []:
        print("empty response returning")
        return
    for j in response:

        retid = j[key]
        theid = retid
        common.write_import(type, theid, id)