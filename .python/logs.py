import common
import globals


def get_aws_cloudwatch_log_group(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_cloudwatch_log_group  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    response = common.call_boto3(clfn, descfn, topkey, id)
    print("-9a->"+str(response))
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
