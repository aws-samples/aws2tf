import common
import boto3
import globals
import os
import sys

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
            print(f"{e=}")
            print("ERROR: -2->unexpected error in get_aws_dynamodb_table")
            print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            exit()

    return True
