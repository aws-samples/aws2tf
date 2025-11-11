import common
import boto3
import context
import inspect

def get_aws_kendra_index(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.list_indices()
            if response[topkey] == []: 
                if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response[topkey]:
                common.write_import(type,j[key],"k-"+j[key]) 
                common.add_dependancy("aws_kendra_data_source",j[key])
                common.add_dependancy("aws_kendra_experience",j[key])

        else:      
            response = client.describe_index(Id=id)
            if response == []: 
                if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            j=response
            common.write_import(type,j[key],"k-"+j[key])
            common.add_dependancy("aws_kendra_data_source",j[key])
            common.add_dependancy("aws_kendra_experience",j[key])

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_kendra_data_source(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            print("Warning: No id for "+type)
        else:      
            response = client.list_data_sources(IndexId=id)
            if response[topkey] == []: 
                if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                pkey=type+"."+id
                context.rproc[pkey]=True
                return True
            for j in response[topkey]:
                theid=j[key]+"/"+id
                altk="k-"+theid
                common.write_import(type,theid,"k-"+j[key])
            pkey=type+"."+id
            context.rproc[pkey]=True


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_kendra_experience(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            print("Warning: No id for "+type)
        else:      
            response = client.list_experiences(IndexId=id)
            if response[topkey] == []: 
                if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                pkey=type+"."+id
                context.rproc[pkey]=True
                return True
            for j in response[topkey]:
                theid=j[key]+"/"+id
                altk="k-"+theid
                common.write_import(type,theid,"k-"+j[key])
            pkey=type+"."+id
            context.rproc[pkey]=True


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_kendra_faq(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            print("Warning: No id for "+type)
        else:      
            response = client.list_faqs(IndexId=id)
            if response[topkey] == []: 
                if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                pkey=type+"."+id
                context.rproc[pkey]=True
                return True
            for j in response[topkey]:
                theid=j[key]+"/"+id
                altk="k-"+theid
                common.write_import(type,theid,"k-"+j[key])
            pkey=type+"."+id
            context.rproc[pkey]=True


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_kendra_thesaurus(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            print("Warning: No id for "+type)
        else:      
            response = client.list_thesauri(IndexId=id)
            if response[topkey] == []: 
                if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                pkey=type+"."+id
                context.rproc[pkey]=True
                return True
            for j in response[topkey]:
                theid=j[key]+"/"+id
                altk="k-"+theid
                common.write_import(type,theid,"k-"+j[key])
            pkey=type+"."+id
            context.rproc[pkey]=True


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_kendra_query_suggestions_block_list(type, id, clfn, descfn, topkey, key, filterid):
    if context.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            print("Warning: No id for "+type)
        else:      
            response = client.list_query_suggestions_block_lists(IndexId=id)
            if response[topkey] == []: 
                if context.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                pkey=type+"."+id
                context.rproc[pkey]=True 
                return True
            for j in response[topkey]:
                theid=j[key]+"/"+id
                altk="k-"+theid
                common.write_import(type,theid,"k-"+j[key])
            pkey=type+"."+id
            context.rproc[pkey]=True


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True