import common
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect



def get_aws_sns_topic(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:

        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_topics()
            if response == []: 
                log.info("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response[topkey]:  
                common.write_import(type, j[key], None)
                common.add_dependancy("aws_sns_topic_policy",j[key])
                common.add_dependancy("aws_sns_topic_subscription", j[key])
        else:
            response = client.get_topic_attributes(TopicArn=id)
            if response == []: 
                log.info("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            common.write_import(type,id,None)
            common.add_dependancy("aws_sns_topic_policy",id)
            common.add_dependancy("aws_sns_topic_subscription",id)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
    return True


def get_aws_sns_topic_policy(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            log.warning("WARNING: Must pass TopicARN as parameter")
            return True

        else:
            response = client.get_topic_attributes(TopicArn=id)
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                pkey="aws_sns_topic_policy."+id
                context.rproc[pkey]=True
                return True
            common.write_import(type,id,None)
            pkey="aws_sns_topic_policy."+id
            context.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
    return True

def get_aws_sns_topic_subscription(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            log.warning("WARNING: Must pass TopicARN as parameter")
            return True

        else:
   
            if id.startswith("arn:aws:sns:"):
                response = client.list_subscriptions_by_topic(TopicArn=id)
                if response == []: 
                    if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                    return True
                for j in response[topkey]:
            
                    if j[key].startswith("arn:"):
                        common.write_import(type,j[key],None)
                    elif j[key]=="PendingConfirmation":
                        log.warning("WARNING: Skipping subscription as status = "+j[key])
                pkey="aws_sns_topic_subscription."+id
                context.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True