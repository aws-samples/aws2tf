import common
import boto3
import globals
import inspect


def get_aws_sns_topic_policy(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:

        response = []
        client = boto3.client(clfn)
        if id is None:
            print("WARNING: Must pass TopicARN as parameter")
            return True

        else:
             
            response = client.get_topic_attributes(TopicArn=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            common.write_import(type,id,None)


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)



    return True

def get_aws_sns_topic_subscription(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            print("WARNING: Must pass TopicARN as parameter")
            return True

        else:
            toparn=id.rsplit(":",1)[0]
            response = client.list_subscriptions_by_topic(TopicArn=toparn)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                if id == j[key]:
                    common.write_import(type,j[key],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True