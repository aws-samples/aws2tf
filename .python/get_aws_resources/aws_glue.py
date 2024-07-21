import common
import boto3
import globals
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
                pkey2="aws_glue_catalog_table."+pkey
                globals.rproc[pkey2]=True

        else: 
            if ":" in id:   id =id.split(":")[1]    
            response = client.get_database(Name=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response['Database']
            pkey=globals.acc+":"+j[key]
            tfid="d-"+pkey.replace(":","__")
            common.write_import(type,pkey,tfid)
            #print("KD add aws_glue_catalog_table "+pkey)
            common.add_dependancy("aws_glue_catalog_table",pkey)
            pkey2="aws_glue_catalog_table."+pkey
            globals.rproc[pkey2]=True

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

def get_aws_glue_job(type, id, clfn, descfn, topkey, key, filterid):

    if globals.debug:
        print("--> In get_aws_glue_job  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        
        response = client.list_jobs()
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response['JobNames']:
            pkey=j
            if id is None:
                common.write_import(type,pkey,None) 
            else:
                if id==j:
                    common.write_import(type,pkey,None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)


    return True

def get_aws_glue_security_configuration(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
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
                common.write_import(type,j[key],None) 

        else:      
            response = client.get_security_configuration(Name=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response['SecurityConfiguration']
            common.write_import(type,j[key],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_glue_crawler(type, id, clfn, descfn, topkey, key, filterid):

    if globals.debug:
        print("--> In get_aws_glue_crawler doing " + type + ' with id ' + str(id) +
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
                crn=j[key]
                dbn=j['DatabaseName']
                common.write_import(type,crn,None) 
                common.add_dependancy("aws_glue_catalog_database",dbn)

        else:          
            response = client.get_crawler(Name=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response['Crawler']
            crn=j[key]
            dbn=j['DatabaseName']
            common.write_import(type,crn,None)
            common.add_dependancy("aws_glue_catalog_database",dbn)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

# aws_glue_dev_endpoint

def get_aws_glue_dev_endpoint(type, id, clfn, descfn, topkey, key, filterid):

    if globals.debug:
        print("--> In get_aws_glue_dev_endpoint doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)   
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_dev_endpoints()
            if response['DevEndpointNames'] == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response['DevEndpointNames']:
                epn=j
                if id is None:
                    common.write_import(type,epn,None) 
                elif epn==id:
                    common.write_import(type, epn, None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

# aws_glue_data_catalog_encryption_settings

def get_aws_glue_data_catalog_encryption_settings(type, id, clfn, descfn, topkey, key, filterid):

    if globals.debug:
        print("--> In get_aws_glue_dev_endpoint doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)   
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.get_data_catalog_encryption_settings()
            if response['DataCatalogEncryptionSettings'] == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            if id is None:
                common.write_import(type,globals.acc,"c-"+globals.acc) 
            else:
                common.write_import(type,id,"c-"+id)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

# aws_glue_connection
def get_aws_glue_connection(type, id, clfn, descfn, topkey, key, filterid):

    if globals.debug:
        print("--> In get_aws_glue_connection doing " + type + ' with id ' + str(id) +
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
                theid="c-"+pkey.replace(":","_")
                common.write_import(type, pkey, theid)
        else:
            response = client.get_connection(Name=id)
            if response['Connection'] == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response['Connection'][key]
            pkey=globals.acc+":"+j
            theid="c-"+pkey.replace(":","_")
            common.write_import(type, pkey, theid)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_glue_classifier(type, id, clfn, descfn, topkey, key, filterid):

    if globals.debug:
        print("--> In get_aws_glue_connection doing " + type + ' with id ' + str(id) +
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
                print(str(j))
                try:
                    pkey=j['CsvClassifier'][key]
                    common.write_import(type, pkey, None)
                except Exception as e:
                    print(e)
                    print(str(j))
                #pkey=globals.acc+":"+j[key]
                #theid="c-"+pkey.replace(":","_")
                #common.write_import(type, pkey, theid)
        else:
            print("ID is "+str(id))
            response = client.get_classifier(Name=id)
            if response['Classifier'] == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response['Classifier']
            try:
                pkey=j['CsvClassifier'][key]
                common.write_import(type, pkey, None)
            except Exception as e:
                print("e=",e)
                print(str(j))
            try:
                pkey=j['JsonClassifier'][key]
                common.write_import(type, pkey, None)
            except Exception as e:
                print(e)
                print(str(j))

            #theid="c-"+pkey.replace(":","_")
            #common.write_import(type, pkey, theid)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True