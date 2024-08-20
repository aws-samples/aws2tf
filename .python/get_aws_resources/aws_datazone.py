import common
import boto3
import globals
import inspect

def get_aws_datazone_domain(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(status='AVAILABLE'):
                response = response + page[topkey]
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                common.write_import(type,j[key],None) 
                # provider crashes on import
                common.add_dependancy("aws_datazone_project", j[key])
                common.add_dependancy("aws_datazone_glossary", j[key])
                common.add_dependancy("aws_datazone_glossary_term", j[key])
                common.add_dependancy("aws_datazone_environment_profile", j[key])

        else:      
            response = client.get_domain(identifier=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response
            common.write_import(type,j[key],None)
            # provider crashes on import
            common.add_dependancy("aws_datazone_project", j[key])
            common.add_dependancy("aws_datazone_glossary", j[key])
            common.add_dependancy("aws_datazone_glossary_term", j[key])
            common.add_dependancy("aws_datazone_environment_profile", j[key])

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_datazone_project(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        
        response = []
        client = boto3.client(clfn)

        paginator = client.get_paginator(descfn)
        if id is None:
            print("WARNING must pass domain id to get_aws_datazone_project")
            return True
        else:
            for page in paginator.paginate(domainIdentifier=id):
                response = response + page[topkey]
        pkey=type+"."+id
        if response == []: 
            print("Empty response for "+type+ " id="+str(id)+" returning") 
            globals.rproc[pkey]=True
            return True
        for j in response:
            theid=id+":"+j[key]
            common.write_import(type,theid,None) 
            
        globals.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


# get-project has gloassary terms - each term has glossary id
def get_aws_datazone_glossary(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        
        response = []
        client = boto3.client(clfn)

        paginator = client.get_paginator(descfn)
        if id is None:
            print("WARNING must pass domain id to get_aws_datazone_glossary")
            return True
        else:
            for page in paginator.paginate(domainIdentifier=id,searchScope='GLOSSARY'):
                response = response + page[topkey]
        pkey=type+"."+id
        if response == []: 
            print("Empty response for "+type+ " id="+str(id)+" returning")
            globals.rproc[pkey]=True
            return True
        #print(str(response))
        for k in response:
            j=k['glossaryItem']
            theid=id+","+j[key]+","+j['owningProjectId']
            print(theid)
            common.write_import(type,theid,None) 

        globals.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_datazone_glossary_term(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)

        paginator = client.get_paginator(descfn)
        if id is None:
            print("WARNING must pass domain id to get_aws_datazone_glossary_term")
            return True
        else:
            for page in paginator.paginate(domainIdentifier=id,searchScope='GLOSSARY_TERM'):
                response = response + page[topkey]

        pkey=type+"."+id
        if response == []: 
            print("Empty response for "+type+ " id="+str(id)+" returning")
            globals.rproc[pkey]=True    
            return True
        #print(str(response))
        for k in response:
            j=k['glossaryTermItem']
            theid=id+","+j[key]+","+j['glossaryId']
            print(theid)
            common.write_import(type,theid,None) 
        globals.rproc[pkey]=True
        
        

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_datazone_form_type(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        
        response = []
        client = boto3.client(clfn)

        paginator = client.get_paginator(descfn)
        if id is None:
            print("WARNING must pass domain id to get_aws_datazone_form_type")
            return True
        else:
            for page in paginator.paginate(domainIdentifier=id,managed=False,
                        searchScope='FORM_TYPE',sort={'attribute': 'name','order': 'ASCENDING'}):
                response = response + page[topkey]
        pkey=type+"."+id
        if response == []: 
            print("Empty response for "+type+ " id="+str(id)+" returning")
            globals.rproc[pkey]=True
            return True
        print(str(response))
        for k in response:

            j=k['formTypeItem']
            theid=id+","+j['name']+","+j['revision']
            print(theid)
            common.write_import(type,theid,None) 

        globals.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True



def get_aws_datazone_environment_blueprint_configuration(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
      
        response = []
        client = boto3.client(clfn)

        paginator = client.get_paginator(descfn)
        if id is None:
            print("WARNING must pass domain id to get_aws_datazone_environment_blueprint_configuration")
            return True
        else:
            for page in paginator.paginate(domainIdentifier=id):
                response = response + page[topkey]
        pkey=type+"."+id
        if response == []: 
            print("Empty response for "+type+ " id="+str(id)+" returning")
            globals.rproc[pkey]=True
            return True
        for j in response:
            theid=id+'/'+j[key]
            common.write_import(type,theid,None) 
            
        globals.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_datazone_environment_profile(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)

        paginator = client.get_paginator(descfn)
        if id is None:
            print("WARNING must pass domain id to get_aws_datazone_environment_profile")
            return True
        else:
            for page in paginator.paginate(domainIdentifier=id):
                response = response + page[topkey]
        pkey=type+"."+id
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response:
            theid=j[key]+","+id
            common.write_import(type,theid,None) 

        globals.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

