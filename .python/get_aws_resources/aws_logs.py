import common
import globals
import inspect


def get_aws_cloudwatch_log_group(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_cloudwatch_log_group  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    response = common.call_boto3(type,clfn, descfn, topkey, key, id)
    #print("-9a->"+str(response))
    try:
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True

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
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

