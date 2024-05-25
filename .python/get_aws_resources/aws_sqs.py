import common
import boto3
import globals
import inspect

def get_aws_sqs_queue(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_queues()
            try:
                tempr=response[topkey]
            except:
                print("No queues found "+type+ " id="+str(id)+" returning")
                return True
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                common.write_import(type,j,None) 

        else:      
            response = client.list_queues(QueueNamePrefix=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                if j==id:
                    common.write_import(type,j,None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

