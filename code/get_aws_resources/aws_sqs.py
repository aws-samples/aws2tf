import common
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect

def get_aws_sqs_queue(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_queues()
            try:
                tempr=response[topkey]
            except:
                log.info("No queues found "+type+ " id="+str(id)+" returning")
                return True
            if response == []: 
                log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response[topkey]:
                common.write_import(type,j,None) 
                common.add_dependancy("aws_sqs_queue_policy",j)
                common.add_dependancy("aws_sqs_queue_redrive_allow_policy", j)
                common.add_dependancy("aws_sqs_queue_redrive_policy", j)

        else:      
            response = client.list_queues()
            if response == []: 
                log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            if "://" not in id:
                # assume it s a queue name and get url:
                try:
                    if context.debug: log.debug("Getting URL for queue %s", id)
                    response2 = client.get_queue_url(QueueName=id)
                    id=response2['QueueUrl']
                except Exception as e:
                    if "NonExistentQueue" in str(e):
                        log.info("Unable to find queue: %s", id)
                    return True


            if "://" in id:
                for j in response[topkey]:
                    if j==id:
                        common.write_import(type,j,None)
                        common.add_dependancy("aws_sqs_queue_policy",j)
                        common.add_dependancy("aws_sqs_queue_redrive_allow_policy", j)
                        common.add_dependancy("aws_sqs_queue_redrive_policy", j)


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_sqs_queue_policy(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            log.info("Must pass queue url as parameter")
            return True
        else:   
            pkey="aws_sqs_queue_policy."+id
            response = client.get_queue_attributes(QueueUrl=id,AttributeNames=['Policy'])
            try:
                tempr=response[topkey]
            except KeyError as e:
                #print(f"{e=}")
                log.info("No policy found for "+type+ " id="+str(id)+" returning")
                
                context.rproc[pkey]=True
                return True
            if response == []: 
                log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            common.write_import(type,id,None)
            context.rproc[pkey]=True


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_sqs_queue_redrive_allow_policy(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            log.info("Must pass queue url as parameter")
            return True
        else:      
            response = client.get_queue_attributes(QueueUrl=id,AttributeNames=['RedriveAllowPolicy'])
            pkey="aws_sqs_queue_redrive_allow_policy."+id
            try:
                tempr=response[topkey]
            except KeyError as e:
                #print(f"{e=}")
                log.info("No redrive allow policy found for "+type+ " id="+str(id)+" returning")
                
                context.rproc[pkey]=True
                return True
            if response == []: 
                log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
 
            common.write_import(type,id,None)
            context.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_sqs_queue_redrive_policy(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            log.info("Must pass queue url as parameter")
            return True
        else: 
            pkey="aws_sqs_queue_redrive_policy."+id     
            response = client.get_queue_attributes(QueueUrl=id,AttributeNames=['RedrivePolicy'])
            try:
                tempr=response[topkey]
            except KeyError as e:
                #print(f"{e=}")
                log.info("No redrive policy found for "+type+ " id="+str(id)+" returning")
                
                context.rproc[pkey]=True
                return True
            if response == []: 
                log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                return True
 
            common.write_import(type,id,None)
            context.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True