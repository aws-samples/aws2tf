import common
import boto3
import globals
import inspect

def get_aws_dynamodb_table(type, id, clfn, descfn, topkey, key, filterid):

    if globals.debug:
        print("--> In get_aws_dynamodb_table  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:

        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_tables()
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response['TableNames']:
                common.write_import(type,j,None) 
                common.add_dependancy("aws_dynamodb_kinesis_streaming_destination",j)

        else:
            response = client.describe_table(TableName=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response[topkey] # 'Table
            common.write_import(type,j[key],None) # key=TableName
            common.add_dependancy("aws_dynamodb_kinesis_streaming_destination",j[key])



    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
            
    return True

# aws_dynamodb_kinesis_streaming_destination
def get_aws_dynamodb_kinesis_streaming_destination(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            print("WARNING: Must pass table name as paramter for",type); 
            return True

        else:      
            pkey=type+"."+id
            response = client.describe_kinesis_streaming_destination(TableName=id)
            print(response[topkey])
            if response[topkey] == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
                globals.rproc[pkey]=True
                return True
            for j in response[topkey]:
                tkey=id+","+j[key]
                common.write_import(type,tkey,None)
            globals.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


