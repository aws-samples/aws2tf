import common
import boto3
import globals
import os
import sys


def get_aws_redshiftserverless_namespace(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_redshiftserverless_namespace  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    # Directly get id
    
    try:
        if id is not None:
            common.write_import(type,id,None) 
        else:
            response = []
            client = boto3.client(clfn)
            response1 = client.list_namespaces()
            response=response1['namespaces']
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                common.write_import(type,j[key],None) 

        

    except Exception as e:
            print(f"{e=}")
            print("ERROR: -2->unexpected error in get_aws_redshiftserverless_namespace")
            print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            exit()

    return True


def get_aws_redshiftserverless_workgroup(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In _aws_redshiftserverless_workgroup  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    # Directly get id
    try:
        if id is not None:
            common.write_import(type,id,None) 
        else:
            response = []
            client = boto3.client(clfn)
            response1 = client.list_workgroups()
            response=response1['workgroups']
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True

            for j in response:
                common.write_import(type,j[key],None)



    except Exception as e:
            print(f"{e=}")
            print("ERROR: -2->unexpected error in get_aws_vpc_ipv4_cidr_block_association")
            print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            exit()

    return True


def get_aws_redshift_parameter_group(type, id, clfn, descfn, topkey, key, filterid):


    if globals.debug:
        print("--> In get_aws_redshift_parameter_group  doing " + type + ' with id ' + str(id) +
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
                if "default." not in j[key]: 
                    common.write_import(type,j[key],None) 
                else:
                     print("Default param skipping "+j[key])
            else:
                if "default." not in id: 
                    if id==j[key]: common.write_import(type,j[key],None)
                else:
                    print("Default param skipping "+j[key])
   

    except Exception as e:
            print(f"{e=}")
            print("ERROR: -2->unexpected error in get_aws_redshift_parameter_group")
            print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            exit()

    return True



