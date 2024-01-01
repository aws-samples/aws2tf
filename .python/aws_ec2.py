#!/usr/bin/env python3

import common
import boto3
import globals
import os
import sys


def get_aws_route_table_association(type, id, clfn, descfn, topkey, key, filterid):
    #print("--> In get_aws_route_table_association doing " + type + ' with id ' + str(id) +
    #              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        if globals.debug:
            print("--> In get_aws_route_table_association doing " + type + ' with id ' + str(id) +
                  " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        if type in str(globals.types):
            print("Found "+type+"in types skipping ...")
            return

        response = []
        client = boto3.client(clfn)
        paginator = client.get_paginator(descfn)
        # TODO - just get all onlce and use @@@@ globals
        if id is not None:
            if "subnet-" in id:
                for page in paginator.paginate(Filters=[
                    {
                        'Name': 'association.subnet-id',
                        'Values': [id]
                    },
                ]):
                    response.extend(page[topkey])
            elif "vpc-" in id:
                for page in paginator.paginate(Filters=[
                    {
                        'Name': 'vpc-id',
                        'Values': [id]
                    },
                ]):
                    response.extend(page[topkey])
            else:
                print("Error in get_aws_route_table_association unexpected id value")
        else:
            for page in paginator.paginate():
                response.extend(page[topkey])

        #print("@@ response length="+str(len(response)))
        #print(str(response))
        #print("-aa-"+id)
        if str(response) != "[]":
            #print ("-bb-")
            for item in response:
                #print(str(item))
                il = len(item['Associations'])
                #print("Associations length="+str(il))
                for r in range(0, il):
                    # print(str(r))
                    # print(str(item['Associations'][r]))
                     rtid = (str(item['Associations'][r]['RouteTableId']))
                     vpcid = str(item['VpcId'])
                     
                        # print(str(item['Associations'][r]['SubnetId']))
                     ismain=item['Associations'][r]['Main']
                     #print("in pre-rproc.... ismain="+str(ismain)+" vpcid="+str(vpcid))

                     if not ismain:
                        #print("Trying .......")
                        try:
                           subid = str(item['Associations'][r]['SubnetId'])
                            
                           #print("in pre-rproc.... subid="+str(subid)+" ismain="+str(ismain)+" vpcid="+str(vpcid))

                           # TODO wrong check ? if don't have subnet should add as dependancy
                           # if subid in str(globals.rproc):

                           # TODO check if already have the association
                           #print("--10a--- id="+str(id)+" subid="+subid+" rtid="+rtid)
                           if id is not None and "subnet-" in id:
                              if subid == id:
                                 theid = subid+"/"+rtid
                                 common.write_import(type, theid, None)
                                 pkey = type+"."+subid
                                 globals.rproc[pkey] = True
                           else:
                              theid = subid+"/"+rtid
                              common.write_import(type, theid, None)
                              pkey = type+"."+subid
                              globals.rproc[pkey] = True

                        except Exception as e:
                           print(f"{e=}")
                           print("ERROR: -1-> get_aws_route_table_association")
                           print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
                           print(str(item['Associations'][r]))
                           print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                           exc_type, exc_obj, exc_tb = sys.exc_info()
                           fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                           print(exc_type, fname, exc_tb.tb_lineno)
                           exit()
                     else:
                         pkey="aws_route_table_association"+"."+vpcid
                         print("Setting " + pkey + "=True")
                         globals.rproc[pkey] = True

            # set subnet true now ? as there's no assoc.
            for ti in globals.rproc.keys():
                if not globals.rproc[ti]:
                    if "aws_route_table_association.subnet" in str(ti):
                        globals.rproc[ti] = True
                        #print("************** Setting " + ti + "=True")
        else:
            print("No response for get_aws_route_table_association")
            pkey="aws_route_table_association"+"."+id
            print("Setting " + pkey + "=True")
            globals.rproc[pkey] = True


                        
    except Exception as e:
        print(f"{e=}")
        print("ERROR: -2->unexpected error in get_aws_route_table_association")
        print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        exit()

    return True


def get_aws_launch_template(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_launch_template    doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    response = common.call_boto3(clfn, descfn, topkey, id)
    # print("-9a->"+str(response))
    if response == []:
        print("empty response returning")
        return
    for j in response:
        retid = j['LaunchTemplateId']
        theid = retid
        common.write_import(type, theid, id)

    return True

def get_aws_vpc_ipv4_cidr_block_association(type, id, clfn, descfn, topkey, key, filterid):
    #if globals.debug:
    #print("--> In get_aws_vpc_ipv4_cidr_block_association doing " + type + ' with id ' + str(id) +
    #          " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    response = common.call_boto3(clfn, descfn, topkey, id)
    #print("-9a->"+str(response))
    try:
        if response == []:
            print("empty response returning")
            return
        for j in response:
            cidrb = j['CidrBlockAssociationSet']
            vpcid = j['VpcId']
            if id==vpcid:
                retid=cidrb[0]['AssociationId']
                theid = retid
                common.write_import(type, theid, None)
                pkey = type+"."+vpcid
                globals.rproc[pkey] = True
    except Exception as e:
        print(f"{e=}")
        print("ERROR: -2->unexpected error in get_aws_vpc_ipv4_cidr_block_association")
        print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        exit()

    return True


def get_aws_subnet(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_subnet doing " + type + ' with id ' + str(id) +
            " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    response = common.call_boto3(clfn, descfn, topkey, id)
    #print("-9a->"+str(response))
    
    try:
        if response == []:
            print("empty response returning")
            return
        
        if id is None:
            for j in response: common.write_import(type, j[key], None)     
        
        elif "subnet-" in id:
            for j in response:
                subid=j['SubnetId']
                if id==subid: common.write_import(type, j[key], None)


        elif "vpc-" in id:
            for j in response:
                vpcid=j['VpcId']
                if id==vpcid: 
                    common.write_import(type, j[key], None)
                    pkey = type+"."+vpcid
                    globals.rproc[pkey] = True


    
    except Exception as e:
        print(f"{e=}")
        print("ERROR: -2->unexpected error in get_aws_vpc_ipv4_cidr_block_association")
        print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        exit()

    return True



def get_aws_network_acl(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_subnet doing " + type + ' with id ' + str(id) +
            " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

## vall boto3 with Filter default=false

        response = []
        client = boto3.client(clfn)
        paginator = client.get_paginator(descfn)
        # TODO - just get all onlce and use @@@@ globals
        if id is not None:
            if "acl-" in id:
                for page in paginator.paginate(Filters=[
                    {
                        'Name': 'association.network-acl-id',
                        'Values': [id]
                    },
                    {
                        'Name': 'default',
                        'Values': False
                    }
                    ]):
                    response.extend(page[topkey])
            elif "vpc-" in id:
                for page in paginator.paginate(Filters=[
                    {
                        'Name': 'vpc-id',
                        'Values': [id]
                    },
                    {
                        'Name': 'default',
                        'Values': False
                    }
                    ]):
                    response.extend(page[topkey])
            else:
                print("Error in get_aws_route_table_association unexpected id value")
        else:
            for page in paginator.paginate(Filters=[
                    {
                        'Name': 'default',
                        'Values': False
                    }
                    ]):
                    response.extend(page[topkey])



################################################################


    
    try:
        if response == []:
            print("empty response returning")
            return
        
        if id is None:
            for j in response: common.write_import(type, j[key], None)     
        
        else:
            for j in response:
                common.write_import(type, j[key], None)
                pkey = type+"."+j[key]
                globals.rproc[pkey] = True

    
    except Exception as e:
        print(f"{e=}")
        print("ERROR: -2->unexpected error in get_aws_vpc_ipv4_cidr_block_association")
        print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        exit()

    return True


def get_aws_default_network_acl(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_subnet doing " + type + ' with id ' + str(id) +
            " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

## vall boto3 with Filter default=false

        response = []
        client = boto3.client(clfn)
        paginator = client.get_paginator(descfn)
        # TODO - just get all onlce and use @@@@ globals
        if id is not None:
            if "acl-" in id:
                for page in paginator.paginate(Filters=[
                    {
                        'Name': 'association.network-acl-id',
                        'Values': [id]
                    },
                    {
                        'Name': 'default',
                        'Values': False
                    }
                    ]):
                    response.extend(page[topkey])
            elif "vpc-" in id:
                for page in paginator.paginate(Filters=[
                    {
                        'Name': 'vpc-id',
                        'Values': [id]
                    },
                    {
                        'Name': 'default',
                        'Values': False
                    }
                    ]):
                    response.extend(page[topkey])
            else:
                print("Error in get_aws_route_table_association unexpected id value")
        else:
            for page in paginator.paginate(Filters=[
                    {
                        'Name': 'default',
                        'Values': False
                    }
                    ]):
                    response.extend(page[topkey])



################################################################


    
    try:
        if response == []:
            print("empty response returning")
            return
        
        if id is None:
            for j in response: common.write_import(type, j[key], None)     
        
        else:
            for j in response:
                common.write_import(type, j[key], None)
                pkey = type+"."+j[key]
                globals.rproc[pkey] = True

    
    except Exception as e:
        print(f"{e=}")
        print("ERROR: -2->unexpected error in get_aws_vpc_ipv4_cidr_block_association")
        print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        exit()

    return True