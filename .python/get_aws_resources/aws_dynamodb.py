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

        else:
            response = client.describe_table(TableName=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response[topkey] # 'Table
            common.write_import(type,j[key],None) # key=TableName


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
            
    return True
