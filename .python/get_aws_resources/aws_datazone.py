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
                #common.add_dependancy("aws_datazone_project", j[key])

        else:      
            response = client.get_domain(identifier=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response
            common.write_import(type,j[key],None)
            # provider crashes on import
            #common.add_dependancy("aws_datazone_project", j[key])

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

        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response:
            print(j)
            common.write_import(type,j[key],None) 
            pkey=type+"."+id
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
            print("WARNING must pass domain id to get_aws_datazone_project")
            return True
        else:
            for page in paginator.paginate(domainIdentifier=id):
                response = response + page[topkey]

        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response:
            projid=j[key]
            proj=client.get_project(domainIdentifier=id,identifier=projid)
            for glossterm in proj['glossaryTerms']:
                print(glossterm)
                gt = client.get_glossary_term(domainIdentifier='string',identifier='string')
                glossid=gt['glossaryId']
                theid=id+","+glossid+","+projid
                common.write_import(type,theid,None) 
        pkey=type+"."+id
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
            print("WARNING must pass domain id to get_aws_datazone_project")
            return True
        else:
            for page in paginator.paginate(domainIdentifier=id):
                response = response + page[topkey]

        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response:
            theid=id+'/'+j[key]
            common.write_import(type,theid,None) 
            pkey=type+"."+id
            globals.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

