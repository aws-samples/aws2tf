import common
import logging
log = logging.getLogger('aws2tf')
import context
import inspect

# "$AWS configservice describe-config-rules  --config-rule-names $1"
def get_aws_config_config_rule(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In get_aws_config_config_rule  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = common.call_boto3(type,clfn, descfn, topkey, key, id)
        #print("-9a->"+str(response))
        if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True

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


def get_aws_config_aggregate_authorization(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In get_aws_config_config_rule  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = common.call_boto3(type,clfn, descfn, topkey, key, id)
        if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True

        if id is None:
                theid=context.acc+":"+context.region
                common.write_import(type, theid, id)

                    

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True