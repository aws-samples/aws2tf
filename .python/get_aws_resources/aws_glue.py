import common
import boto3
import globals
import os
import sys

def get_aws_glue_catalog_database(type, id, clfn, descfn, topkey, key, filterid):

    if globals.debug:
        print("--> In get_aws_glue_catalog_database  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                pkey=globals.acc+":"+j[key]
                tfid="d-"+pkey.replace(":","__")
                common.write_import(type,pkey,tfid) 

        else:          
            response = client.get_database(Name=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response['Database']
            pkey=globals.acc+":"+j[key]
            tfid="d-"+pkey.replace(":","__")
            common.write_import(type,pkey,tfid)
            common.add_dependancy("aws_glue_catalog_table",pkey)

    except Exception as e:
            print(f"{e=}")
            print("ERROR: -2->unexpected error in get_aws_glue_catalog_database")
            print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            exit()

    return True

## ID must pass catalog/database   or catalog/database/table
def get_aws_glue_catalog_table(type, id, clfn, descfn, topkey, key, filterid):

    # need to fetch catalogid and database from id


    if globals.debug:
        print("--> In get_aws_glue_catalog_table  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        cc=id.count('/')
        if cc == 1:
             catalogn=id.split('/')[0]
             databasen=id.split('/')[1]
        if cc == 2:
             tabnam=id.split('/')[2]

        
        if id is None:
            print("ID cannot be None")
 
        else:     
            ## Do not have table name


            ## Do have table name
            if cc == 1:
                response = client.get_tables(CatalogId=catalogn,DatabaseName=databasen)
            if cc == 2:
                response = client.get_tables(CatalogId=catalogn,DatabaseName=databasen,Expression=tabnam)

            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
            #Terraform import id = "123456789012:MyDatabase:MyTable"
                pkey=catalogn+":"+databasen+":"+j[key]
                tfid="d-"+pkey.replace(":","__")
                common.write_import(type,pkey,tfid)

    except Exception as e:
            print(f"{e=}")
            print("ERROR: -2->unexpected error in get_aws_glue_catalog_database")
            print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            exit()

    return True