import common
import boto3
import globals
import os
import sys
import inspect

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
                common.add_dependancy("aws_glue_catalog_table",pkey)

        else:          
            response = client.get_database(Name=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response['Database']
            pkey=globals.acc+":"+j[key]
            tfid="d-"+pkey.replace(":","__")
            common.write_import(type,pkey,tfid)
            print("Add dep aws_glue_catalog_table "+pkey)
            common.add_dependancy("aws_glue_catalog_table",pkey)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

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


        
        if id is None:
            print("ID cannot be None")
 
        else:     
            ## Do not have table name
            cc=id.count(':')
            if cc == 1:
                catalogn=id.split(':')[0]
                databasen=id.split(':')[1]
            if cc == 2:
                tabnam=id.split(':')[2]

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
            
            # set dependency false
            tkey="aws_glue_catalog_table"+"."+catalogn+":"+databasen
            #print("Setting True "+tkey)
            globals.rproc[tkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_glue_trigger(type, id, clfn, descfn, topkey, key, filterid):

    if globals.debug:
        print("--> In get_aws_glue_trigger  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_triggers()
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response['TriggerNames']:
                pkey=j
                common.write_import(type,pkey,None) 

        else:          
            response = client.get_trigger(Name=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response['Trigger']
            pkey=j[key]
            common.write_import(type,pkey,None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)


    return True