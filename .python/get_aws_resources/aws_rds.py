import common
import boto3
import globals
import inspect


def get_aws_db_parameter_group(type, id, clfn, descfn, topkey, key, filterid):


    if globals.debug:
        print("--> In get_aws_db_parameter_group  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        ## id filter here
   
        paginator = client.get_paginator(descfn)
        for page in paginator.paginate():
                response = response + page[topkey]
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        #print(str(response))
        for j in response:
            if id is None:
                common.write_import(type,j[key],None) 
            else:
                if "default." not in id: 
                    did="default."+id
                if did==j[key]: 
                    common.write_import(type,j[key],None)
                else:
                    if id==j[key]:
                        common.write_import(type,j[key],None)

   

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_db_option_group(type, id, clfn, descfn, topkey, key, filterid):


    if globals.debug:
        print("--> In get_aws_db_option_group  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        ## id filter here
   
        paginator = client.get_paginator(descfn)
        for page in paginator.paginate():
                response = response + page[topkey]
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        #print(str(response))
        for j in response:
            if id is None:
                if "default:" not in j[key]:
                    common.write_import(type,j[key],None) 
            else:
                if "default:" not in id:  
                    if id==j[key]:
                        common.write_import(type,j[key],None)

   

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


#aws_db_subnet_group

def get_aws_db_subnet_group(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    
    try:
        response = []
        client = boto3.client(clfn)
        ## id filter here
   
        paginator = client.get_paginator(descfn)
        for page in paginator.paginate():
                response = response + page[topkey]
        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        #print(str(response))

        for j in response:
            if id is None:
                if "default" != j[key]:
                    common.write_import(type,j[key],None) 
            else:
                if "default" != id:  
                    if id==j[key]:
                        common.write_import(type,j[key],None)
                else:
                    pkey="aws_db_subnet_group."+id
                    globals.rproc[pkey]=True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

# aws_rds_custom_db_engine_version


def get_aws_rds_custom_db_engine_version(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        paginator = client.get_paginator(descfn)
        if id is None: 
            for page in paginator.paginate():
                response = response + page[topkey]
        else:
            for page in paginator.paginate(Engine=id):
                response = response + page[topkey]

        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response:
            eng=j['Engine']
            engv=j['EngineVersion']
            pkey=eng+":"+engv
            common.write_import(type,pkey,None) 



    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


#aws_db_event_subscription#

def get_aws_db_event_subscription(type, id, clfn, descfn, topkey, key, filterid):
    #if globals.debug:
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
                print(j)
                common.write_import(type,j[key],None) 

        else:      
            response = client.describe_event_subscriptions(SubscriptionName=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                print(j)
                common.write_import(type,j[key],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


# aws_db_instance


def get_aws_db_instance(type, id, clfn, descfn, topkey, key, filterid):
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
                engine=j['Engine']
                if engine=="docdb" or engine.startswith("aurora"): continue
                common.write_import(type, j[key], None)

        else:
            response = client.describe_db_instances(DBInstanceIdentifier=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                print(j)
                engine=j['Engine']
                if engine=="docdb" or engine.startswith("aurora"): continue
                common.write_import(type, j[key], None)

    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True

def get_aws_rds_cluster_instance(type, id, clfn, descfn, topkey, key, filterid):
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
                engine=j['Engine']
                if engine.startswith("aurora"): 
                    common.write_import(type, j[key], None)
                else:
                    continue

        else:
            response = client.describe_db_instances(DBInstanceIdentifier=id)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                print(j)
                engine=j['Engine']
                if engine.startswith("aurora"):
                    common.write_import(type, j[key], None)
                else:
                    continue

    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True