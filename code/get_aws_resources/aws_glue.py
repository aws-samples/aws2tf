import common
from common import log_warning
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
            if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
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
            log_warning("WARNING: ID can not be None - must pass catalog:database or catalog:database:tablename" )
            return True
        cc=id.count(':')
        if cc==0:
                    log_warning("WARNING: ID - must pass catalog:database or catalog:database:tablename" )
                    return True
        if cc == 1:
                    catalogn=id.split(':')[0]
                    databasen=id.split(':')[1]
                    
        if cc == 2:
                    catalogn=id.split(':')[0]
                    databasen=id.split(':')[1]
                    tabnam=id.split(':')[2]
                    
        
        tkey="aws_glue_catalog_table"+"."+catalogn+":"+databasen
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
            if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response['TriggerNames']:
                pkey=j
                common.write_import(type,pkey,None) 

        else:          
            response = client.get_trigger(Name=id)
            if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
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
        if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
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
            if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                common.write_import(type,j[key],None) 

        else:      
            response = client.get_security_configuration(Name=id)
            if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
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
            if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                crn=j[key]
                dbn=j['DatabaseName']
                common.write_import(type,crn,None) 
                common.add_dependancy("aws_glue_catalog_database",dbn)

        else:          
            response = client.get_crawler(Name=id)
            if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
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
            if response['DevEndpointNames'] == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
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
            if response['DataCatalogEncryptionSettings'] == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
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
            if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                pkey=context.acc+":"+j[key]
                theid="c-"+pkey.replace(":","_")
                common.write_import(type, pkey, theid)
        else:
            response = client.get_connection(Name=id)
            if response['Connection'] == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
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
            if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True

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
            response = client.get_classifier(Name=id)
            if response['Classifier'] == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
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
            log.debug("ID can not be None")
        
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
                log_warning("WARNING: Invalid aws_glue_partition id passed must pass catalogid:database:tablename got: " + id +"c="+str(cc))
                context.rproc[tkey]=True
                return True

            try:
                response = client.get_partitions(CatalogId=catalogn,DatabaseName=databasen,TableName=tabnam)
            except Exception as e:
                log.info(e)
                context.rproc[tkey]=True

            if response == []: 
                log.debug("*-** Empty response for "+type+ " id="+str(id))
                log.debug("tkey="+tkey+" returning")
                context.rproc[tkey]=True
                return True
            
            for j in response[topkey]:
                vals=""
                for k in j[key]: vals=vals+k+"#"
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
            if response[topkey] == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                common.write_import(type,j[key],None) 

        else:      
            response = client.list_data_quality_rulesets()
            if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
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
            if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                log.debug(j)
                common.write_import(type, j, None)

        else:
            response = client.get_workflow(Name=id)
            if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response['Workflow']
            common.write_import(type, j[key], None)

    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True


# aws_glue_partition_index
def get_aws_glue_partition_index(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        client = boto3.client(clfn)
        
        if id is None:
            # First get all databases
            db_paginator = client.get_paginator('get_databases')
            databases = []
            for page in db_paginator.paginate():
                databases = databases + page['DatabaseList']
            
            # Then for each database, get all tables
            for db in databases:
                db_name = db['Name']
                try:
                    table_response = client.get_tables(DatabaseName=db_name)
                    tables = table_response.get('TableList', [])
                    
                    # For each table, get partition indexes
                    for table in tables:
                        table_name = table['Name']
                        try:
                            index_response = client.get_partition_indexes(
                                DatabaseName=db_name,
                                TableName=table_name
                            )
                            indexes = index_response.get(topkey, [])
                            
                            # Build composite ID: catalog_id:database_name:table_name:index_name
                            for idx in indexes:
                                composite_id = f"{context.acc}:{db_name}:{table_name}:{idx[key]}"
                                common.write_import(type, composite_id, None)
                        except Exception as e:
                            if context.debug: log.debug(f"Error getting indexes for table {table_name}: {e}")
                            continue
                except Exception as e:
                    if context.debug: log.debug(f"Error getting tables for database {db_name}: {e}")
                    continue
        else:
            # Handle composite ID: catalog_id:database_name:table_name:index_name
            if id.count(':') == 3:
                catalog_id, db_name, table_name, index_name = id.split(':', 3)
                try:
                    response = client.get_partition_indexes(
                        DatabaseName=db_name,
                        TableName=table_name
                    )
                    indexes = response.get(topkey, [])
                    for idx in indexes:
                        if idx[key] == index_name:
                            common.write_import(type, id, None)
                            break
                except Exception as e:
                    if context.debug: log.debug(f"Error getting specific index: {e}")
            else:
                if context.debug: log.debug("Must pass catalog_id:database_name:table_name:index_name for "+type)

    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True


# aws_glue_resource_policy - Regional singleton
def get_aws_glue_resource_policy(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        client = boto3.client(clfn)
        
        # This is a regional singleton - import ID is the region
        if id is None:
            # Use the current region
            region = context.region
        else:
            region = id
        
        try:
            # Try to get the resource policy
            response = client.get_resource_policy()
            # Policy exists, write import using region as ID
            common.write_import(type, region, None)
        except client.exceptions.EntityNotFoundException:
            # No policy exists for this region
            if context.debug: log.debug(f"No resource policy found for region {region}")
        except Exception as e:
            if context.debug: log.debug(f"Error getting resource policy: {e}")

    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True


# aws_glue_user_defined_function
def get_aws_glue_user_defined_function(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        client = boto3.client(clfn)
        
        if id is None:
            # First get all databases
            db_paginator = client.get_paginator('get_databases')
            databases = []
            for page in db_paginator.paginate():
                databases = databases + page['DatabaseList']
            
            # Then for each database, get all user defined functions
            for db in databases:
                db_name = db['Name']
                try:
                    # Pattern is required - use ".*" to match all functions
                    response = client.get_user_defined_functions(
                        DatabaseName=db_name,
                        Pattern='.*'
                    )
                    functions = response.get(topkey, [])
                    
                    # Build composite ID: catalog_id:database_name:function_name
                    for func in functions:
                        composite_id = f"{context.acc}:{db_name}:{func[key]}"
                        common.write_import(type, composite_id, None)
                except Exception as e:
                    if context.debug: log.debug(f"Error getting functions for database {db_name}: {e}")
                    continue
        else:
            # Handle composite ID: catalog_id:database_name:function_name
            if id.count(':') == 2:
                catalog_id, db_name, function_name = id.split(':', 2)
                try:
                    response = client.get_user_defined_functions(
                        DatabaseName=db_name,
                        Pattern='.*'
                    )
                    functions = response.get(topkey, [])
                    for func in functions:
                        if func[key] == function_name:
                            common.write_import(type, id, None)
                            break
                except Exception as e:
                    if context.debug: log.debug(f"Error getting specific function: {e}")
            else:
                if context.debug: log.debug("Must pass catalog_id:database_name:function_name for "+type)

    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True
