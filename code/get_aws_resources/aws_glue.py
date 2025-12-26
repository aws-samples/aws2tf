import common
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect
import sys

def get_aws_glue_catalog_database(type, id, clfn, descfn, topkey, key, filterid):

    if context.debug:
        log.debug("--> Inn get_aws_glue_catalog_database  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                pkey=context.acc+":"+j[key]
                tfid="d-"+pkey.replace(":","__")
                common.write_import(type,pkey,tfid) 
                common.add_dependancy("aws_glue_catalog_table",pkey)
                context.gluedbs[j[key]]=True

                #pkey2="aws_glue_catalog_table."+pkey
                #context.rproc[pkey2]=True

        else: 
            if ":" in id:   id =id.split(":")[1]   
            response = client.get_database(Name=id)
            if response == []: 
                if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                gkey="aws_glue_catalog_table."+pkey
                context.rproc[gkey]=True
                return True
            j=response['Database']
            pkey=context.acc+":"+j[key]
            tfid="d-"+pkey.replace(":","__")
            common.write_import(type,pkey,tfid)
            context.gluedbs[j[key]]=True
            #print("KD add aws_glue_catalog_table "+pkey)
            common.add_dependancy("aws_glue_catalog_table",pkey)
            gkey="aws_glue_catalog_table."+pkey
            context.rproc[gkey]=True


    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        exn=str(exc_type.__name__)
        if exn=="AccessDeniedException" and "Insufficient Lake Formation permission" in str(e):
            log.info("AccessDeniedException - Insufficient Lake Formation permission for %s %s", type, id)
            if id is not None:
                if ":" in id:   id =id.split(":")[1]
                pkey=context.acc+":"+id
                gkey="aws_glue_catalog_database."+pkey
                
                context.rproc[gkey]=True
        else:
            common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

## ID must pass catalog/database   or catalog/database/table
def get_aws_glue_catalog_table(type, id, clfn, descfn, topkey, key, filterid):

    if context.debug:
        log.debug("--> In get_aws_glue_catalog_table  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    
    try:
        context.workaround=type
        if id is None:
            log.warning("WARNING: ID can not be None - must pass catalog:database or catalog:database:tablename" )
            return True
        cc=id.count(':')
        if cc==0:
                    log.warning("WARNING: ID - must pass catalog:database or catalog:database:tablename" )
                    return True
        if cc == 1:
                    catalogn=id.split(':')[0]
                    databasen=id.split(':')[1]
                    
        if cc == 2:
                    catalogn=id.split(':')[0]
                    databasen=id.split(':')[1]
                    tabnam=id.split(':')[2]
                    
        
        tkey="aws_glue_catalog_table"+"."+catalogn+":"+databasen
        #print(catalogn, databasen, tabnam,cc)
        response = []
        client = boto3.client(clfn)
  
        if cc == 1:
                response = client.get_tables(CatalogId=catalogn,DatabaseName=databasen)
        if cc == 2:
                response = client.get_tables(CatalogId=catalogn,DatabaseName=databasen,Expression=tabnam)
 
        if response[topkey] == []: 
            if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
            tkey="aws_glue_catalog_table"+"."+catalogn+":"+databasen
            context.rproc[tkey]=True
            return True
        for j in response[topkey]:
            #Terraform import id = "123456789012:MyDatabase:MyTable"
                pkey=catalogn+":"+databasen+":"+j[key]
                tfid="d-"+pkey.replace(":","__")
                common.write_import(type,pkey,tfid)
                #common.add_dependancy("aws_glue_partition",pkey)
            
            # set dependency false
        tkey="aws_glue_catalog_table"+"."+catalogn+":"+databasen
        context.rproc[tkey]=True

    except boto3.exceptions.botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'AccessDeniedException':
            log.info(f"AccessDeniedException for aws_glue.py - returning. Resource: {id}")
            tkey="aws_glue_catalog_table"+"."+catalogn+":"+databasen
            context.rproc[tkey]=True
            return True
        else:
            common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)


    
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_glue_trigger(type, id, clfn, descfn, topkey, key, filterid):

    if context.debug:
        log.debug("--> In get_aws_glue_trigger  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_triggers()
            if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response['TriggerNames']:
                pkey=j
                common.write_import(type,pkey,None) 

        else:          
            response = client.get_trigger(Name=id)
            if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response['Trigger']
            pkey=j[key]
            common.write_import(type,pkey,None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)


    return True

def get_aws_glue_job(type, id, clfn, descfn, topkey, key, filterid):

    if context.debug:
        log.debug("--> In get_aws_glue_job  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        
        response = client.list_jobs()
        if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
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
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                common.write_import(type,j[key],None) 

        else:      
            response = client.get_security_configuration(Name=id)
            if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response['SecurityConfiguration']
            common.write_import(type,j[key],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_glue_crawler(type, id, clfn, descfn, topkey, key, filterid):

    if context.debug:
        log.debug("--> In get_aws_glue_crawler doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                crn=j[key]
                dbn=j['DatabaseName']
                common.write_import(type,crn,None) 
                common.add_dependancy("aws_glue_catalog_database",dbn)

        else:          
            response = client.get_crawler(Name=id)
            if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
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

    if context.debug:
        log.debug("--> In get_aws_glue_dev_endpoint doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)   
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_dev_endpoints()
            if response['DevEndpointNames'] == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
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

    if context.debug:
        log.debug("--> In get_aws_glue_dev_endpoint doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)   
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.get_data_catalog_encryption_settings()
            if response['DataCatalogEncryptionSettings'] == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
            if id is None:
                common.write_import(type,context.acc,"c-"+context.acc) 
            else:
                common.write_import(type,id,"c-"+id)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

# aws_glue_connection
def get_aws_glue_connection(type, id, clfn, descfn, topkey, key, filterid):

    if context.debug:
        log.debug("--> In get_aws_glue_connection doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)   
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                pkey=context.acc+":"+j[key]
                theid="c-"+pkey.replace(":","_")
                common.write_import(type, pkey, theid)
        else:
            response = client.get_connection(Name=id)
            if response['Connection'] == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response['Connection'][key]
            pkey=context.acc+":"+j
            theid="c-"+pkey.replace(":","_")
            common.write_import(type, pkey, theid)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_glue_classifier(type, id, clfn, descfn, topkey, key, filterid):

    if context.debug:
        log.debug("--> In get_aws_glue_connection doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)   
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True

            try:
                pkey=j['CsvClassifier'][key]
                common.write_import(type, pkey, None)
            except Exception as e:
                pass
            try:
                pkey=j['JsonClassifier'][key]
                common.write_import(type, pkey, None)
            except Exception as e:
                pass
            try:
                pkey=j['GrokClassifier'][key]
                common.write_import(type, pkey, None)
            except Exception as e:
                pass
            try:
                pkey=j['XMLClassifier'][key]
                common.write_import(type, pkey, None)
            except Exception as e:
                pass
        else:
            #print("ID is "+str(id))
            response = client.get_classifier(Name=id)
            if response['Classifier'] == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response['Classifier']
            try:
                pkey=j['CsvClassifier'][key]
                common.write_import(type, pkey, None)
            except Exception as e:
                pass
            try:
                pkey=j['JsonClassifier'][key]
                common.write_import(type, pkey, None)
            except Exception as e:
                pass
            try:
                pkey=j['GrokClassifier'][key]
                common.write_import(type, pkey, None)
            except Exception as e:
                pass
            try:
                pkey=j['XMLClassifier'][key]
                common.write_import(type, pkey, None)
            except Exception as e:
                pass


            #theid="c-"+pkey.replace(":","_")
            #common.write_import(type, pkey, theid)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_glue_partition(type, id, clfn, descfn, topkey, key, filterid):

    # need to fetch catalogid and database from id
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            log.info("ID can not be None")
        
        else:  
            id=id.strip()  
            ## Do not have table name
            tkey="aws_glue_partition"+"."+id
            cc=id.count(":")
            
            if cc == 2:
                catalogn=id.split(':')[0]
                databasen=id.split(':')[1]
                tabnam=id.split(':')[2]
            else:
                log.warning("WARNING: Invalid aws_glue_partition id passed must pass catalogid:database:tablename got: " + id +"c="+str(cc))
                context.rproc[tkey]=True
                return True

            try:
                response = client.get_partitions(CatalogId=catalogn,DatabaseName=databasen,TableName=tabnam)
            except Exception as e:
                log.info(e)
                context.rproc[tkey]=True

            if response == []: 
                log.info("*-** Empty response for "+type+ " id="+str(id))
                log.info("tkey="+tkey+" returning")
                context.rproc[tkey]=True
                return True
            
            for j in response[topkey]:
                vals=""
                for k in j[key]: vals=vals+k+"#"
                #print("vals="+vals)
                vals=vals.rstrip("#")
                pkey=id+":"+vals
                tfid="p-"+pkey.replace(":","__").replace("#","_")
                common.write_import(type,pkey,tfid)
            
            # set dependency false
            tkey="aws_glue_partition"+"."+id
            context.rproc[tkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_glue_data_quality_ruleset(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_data_quality_rulesets()
            if response[topkey] == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                common.write_import(type,j[key],None) 

        else:      
            response = client.list_data_quality_rulesets()
            if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                common.write_import(type,j[key],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

# aws_glue_workflow
def get_aws_glue_workflow(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                log.info(j)
                common.write_import(type, j, None)

        else:
            response = client.get_workflow(Name=id)
            if response == []: log.info("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response['Workflow']
            common.write_import(type, j[key], None)

    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True
