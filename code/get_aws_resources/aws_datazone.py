import common
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect
from io import StringIO
from timed_interrupt import timed_int


# aws_datazone_asset_type
# ASSET_TYPE FORM_TYPE LINEAGE_NODE_TYPE

def get_aws_datazone_asset_type(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        paginator = client.get_paginator(descfn)

        if id is None:
            log.info("WARNING must pass domain id to get_aws_datazone_asset_type")
            return True
        else:

            pkey=type+"."+id
            for ut in ['ASSET_TYPE','FORM_TYPE','LINEAGE_NODE_TYPE']:
                response == []
                try:
                    for page in paginator.paginate(domainIdentifier=id,searchScope=ut,managed=False):
                        response = response + page[topkey]
                except Exception as e:
                    log.info("ERROR: "+str(e))
                    #if "ResourceNotFoundException" in str(e):
                    #    print("Resource not found for "+ut)
                    #    continue
                    #else:
                    #    print("ERROR: "+str(e))
                    #    exit()
 
                if response == []: 
                    if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                    context.rproc[pkey]=True  
                    continue  
                    
                
                for k in response:
                    #print("----------------------------------------------------------")
                    #print("ut="+ut)
                    #print("\nk="+str(k))
                    try:
                        if ut == 'ASSET_TYPE': 
                            j=k['assetTypeItem']
                        elif ut == 'FORM_TYPE': 
                            j=k['formTypeItem']
                        elif ut == 'LINEAGE_NODE_TYPE': 
                            j=k['lineageNodeTypeItem']
                    except KeyError:
                        #print("KeyError: "+str(k))
                        continue
                    theid=id+','+j[key]
                    log.info("SKIPPING: "+str(type)+" "+str(theid)+" due to import issues")
                    #common.write_import(type,theid,None) 
                
            context.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True


# aws_datazone_user_profile
# DATAZONE_SSO_USER, DATAZONE_USER, SSO_USER, DATAZONE_IAM_USER

def get_aws_datazone_user_profile(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    
    try:
        response = []
        client = boto3.client(clfn)
        paginator = client.get_paginator(descfn)

        if id is None:
            log.info("WARNING must pass domain id to get_aws_datazone_user_profile")
            return True
        else:
            pkey=type+"."+id
            for ut in ['SSO_USER','DATAZONE_USER','DATAZONE_SSO_USER','DATAZONE_IAM_USER']:
                #print("ut="+ut)
                response == []
                try:
                    for page in paginator.paginate(domainIdentifier=id,userType=ut):
                        response = response + page[topkey]
                except Exception as e:
                    if "ResourceNotFoundException" in str(e):
                        if context.debug: log.debug("Resource not found for "+ut)
                        continue
                    else:
                        log.info("ERROR: "+str(e))
                        exit()
                #print("response="+str(response))
                if response == []: 
                    if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
                    context.rproc[pkey]=True    
              
                for k in response:
                    if str(k['status'])=="ACTIVATED":
                        if k['type']=="IAM":
                            uarn=k['details']['iam']['arn']
                            theid=uarn+","+id+','+k['type']
                            common.write_import(type,theid,None)
                        else:
                            if context.debug: 
                                log.debug(str(k))
                            j=k[key]
                            theid=j+","+id+','+k['type']
                            common.write_import(type,theid,None) 
                    #print(theid)
                    #common.write_import(type,theid,None) 
                
        context.rproc[pkey]=True


    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True


#####

def get_aws_datazone_domain(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(status='AVAILABLE'):
                response = response + page[topkey]
            if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                dzid=j[key]
                dv=j['domainVersion']
                if dv=="V1":
                    #print(str(j))
                    resp2=client.get_domain(identifier=dzid)
                    dz_common(resp2,dzid,type,client)
                    
        else:      
            response = client.get_domain(identifier=id)
            if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response
            dzid=j[key]
            dv=j['domainVersion']
            if dv=="V1":
                resp2=client.get_domain(identifier=j[key])
                dz_common(resp2,dzid,type,client)


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def dz_common(resp2,dzid,type,client):
    sso=resp2['singleSignOn']['type']
    dst=resp2['status']
    if context.debug: log.debug("DataZone sso="+str(sso)+" dst="+str(dst)," dzid="+dzid)
    common.write_import(type,dzid,None)
    common.add_dependancy("aws_datazone_project", dzid)
    common.add_dependancy("aws_datazone_glossary", dzid)
    common.add_dependancy("aws_datazone_environment_profile", dzid)
    common.add_dependancy("aws_datazone_environment_blueprint_configuration", dzid)

# write data files

    resp3=client.list_environment_blueprints(domainIdentifier=dzid,managed=True)
    for k in resp3['items']:
        bid=k['id']
        bn=k['name']
        pn=k['provider']
        if context.debug: log.debug(str(bid),str(bn),str(pn))
        output = StringIO()
        output.write('data "aws_datazone_environment_blueprint" "' + str(dzid)+"_"+str(bid)+ '" {\n')
        output.write('  domain_id = aws_datazone_domain.' + str(dzid) + '.id\n') ## error undefined
        #output.write('  domain_id = "' + str(dzid) + '"\n')
        output.write('  name = "'+ bn + '"\n')
        output.write('  managed = true\n')
        output.write('}\n')
        fn="imported/data-dz_"+str(dzid)+"_"+str(bid)+".tf"
        try:
            with open(fn, 'w') as f:
               f.write(output.getvalue().strip() + '\n')
        except:
            log.info("ERROR: could not write to file: " + fn)
            log.info("exit 139")
            timed_int.stop()
            exit()

    if sso!="DISABLED":
        common.add_dependancy("aws_datazone_user_profile", dzid)
    else:
        log.info("skipping sso="+str(sso)+" dst="+str(dst)+" dzid="+dzid)
        return True




    return True


def get_aws_datazone_project(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        
        response = []
        client = boto3.client(clfn)

        paginator = client.get_paginator(descfn)
        if id is None:
            log.info("WARNING must pass domain id to get_aws_datazone_project")
            return True
        else:
            for page in paginator.paginate(domainIdentifier=id):
                response = response + page[topkey]
        pkey=type+"."+id
        if response == []: 
            if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
            context.rproc[pkey]=True
            return True
        for j in response:
            theid=id+":"+j[key]
            common.write_import(type,theid,None) 
            common.add_dependancy("aws_datazone_environment", theid)
            
        context.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


# get-project has gloassary terms - each term has glossary id
def get_aws_datazone_glossary(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        
        response = []
        client = boto3.client(clfn)

        paginator = client.get_paginator(descfn)
        if id is None:
            log.info("WARNING must pass domain id to get_aws_datazone_glossary")
            return True
        else:
            for page in paginator.paginate(domainIdentifier=id,searchScope='GLOSSARY'):
                response = response + page[topkey]
        pkey=type+"."+id
        if response == []: 
            if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
            context.rproc[pkey]=True
            return True
        #print(str(response))
        for k in response:
            j=k['glossaryItem']
            theid=id+","+j[key]+","+j['owningProjectId']
            #print(theid)
            common.write_import(type,theid,None) 
            common.add_dependancy("aws_datazone_glossary_term", theid)

        context.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_datazone_glossary_term(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)

        paginator = client.get_paginator(descfn)
        if id is None:
            log.info("WARNING must pass domain id to get_aws_datazone_glossary_term")
            return True
        else:
            #print("Glossary terms id ",id)
            did=id.split(',')[0]
            pid=id.split(',')[2]
            #print("Glossary terms for ",did,pid)
            for page in paginator.paginate(domainIdentifier=did,owningProjectIdentifier=pid,searchScope='GLOSSARY_TERM'):
                response = response + page[topkey]

        pkey=type+"."+id
        if response == []: 
            if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
            context.rproc[pkey]=True    
            return True
        #print(str(response))
        for k in response:
            j=k['glossaryTermItem']
            theid=did+","+j[key]+","+j['glossaryId']
            #print(theid)
            common.write_import(type,theid,theid+"_"+pid) 
        context.rproc[pkey]=True
        
        

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_datazone_form_type(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        
        response = []
        client = boto3.client(clfn)

        paginator = client.get_paginator(descfn)
        if id is None:
            log.info("WARNING must pass domain id to get_aws_datazone_form_type")
            return True
        else:
            for page in paginator.paginate(domainIdentifier=id,managed=False,
                        searchScope='FORM_TYPE',sort={'attribute': 'name','order': 'ASCENDING'}):
                response = response + page[topkey]
        pkey=type+"."+id
        if response == []: 
            if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
            context.rproc[pkey]=True
            return True
        #print(str(response))
        for k in response:

            j=k['formTypeItem']
            theid=id+","+j['name']+","+j['revision']
            #print(theid)
            common.write_import(type,theid,None) 

        context.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True



def get_aws_datazone_environment_blueprint_configuration(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
      
        response = []
        client = boto3.client(clfn)

        paginator = client.get_paginator(descfn)
        if id is None:
            log.info("WARNING must pass domain id to get_aws_datazone_environment_blueprint_configuration")
            return True
        else:
            for page in paginator.paginate(domainIdentifier=id):
                response = response + page[topkey]
        pkey=type+"."+id
        if response == []: 
            if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
            context.rproc[pkey]=True
            return True
        for j in response:
            theid=id+'/'+j[key]
            common.write_import(type,theid,None) 
            
        context.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_datazone_environment_profile(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)

        paginator = client.get_paginator(descfn)
        if id is None:
            log.info("WARNING must pass domain id to get_aws_datazone_environment_profile")
            return True
        else:
            try:
                for page in paginator.paginate(domainIdentifier=id):
                    response = response + page[topkey]
            except Exception as e:
                log.info(str(e))
                log.warning("WARNING: no environment profiles found for domain id "+id)
                context.rproc[type+"."+id]=True
                return True

        pkey=type+"."+id
        if response == []: 
            if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
            context.rproc[pkey]=True
            return True
        for j in response:
            theid=j[key]+","+id
            altid=id+"_"+j[key]
            common.write_import(type,theid,altid) 

        context.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_datazone_environment(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
    
        paginator = client.get_paginator(descfn)
        if id is None:
            log.info("WARNING must pass domain_id:project_id to get_aws_datazone_environment")
            return True
        else:
            dzd=id.split(':')[0]
            pid=id.split(':')[1]
            for page in paginator.paginate(domainIdentifier=dzd,projectIdentifier=pid):
                response = response + page[topkey]
        pkey=type+"."+id
        if response == []: 
            if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
            context.rproc[pkey]=True
            return True
        for j in response:
            theid=dzd+","+j[key]
            common.write_import(type,theid,None) 

        context.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True
