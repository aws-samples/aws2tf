import common
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect

def get_aws_kinesis_firehose_delivery_stream(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_delivery_streams()
            if response[topkey] == []: 
                log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                # have the name - not must get the arn
                response = client.describe_delivery_stream(DeliveryStreamName=j)
                k=response['DeliveryStreamDescription']
                common.write_import(type,k[key],None) 
                pkey=type+"."+j
                context.rproc[pkey]=True

        else:      
            response = client.describe_delivery_stream(DeliveryStreamName=id)
            if response == []: 
                log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                pkey=type+"."+id
                context.rproc[pkey]=True
                return True
            j=response['DeliveryStreamDescription']
            common.write_import(type,j[key],None)
            pkey=type+"."+id
            context.rproc[pkey]=True
            

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True