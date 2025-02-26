import common
import boto3
import globals
import os
import sys
import inspect
import json


def get_aws_vpc(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_vpc doing " + type + ' with id ' + str(id) +
            " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    try:    
        if id is None:
            for sn in globals.vpclist.keys():
                common.write_import(type,sn,None)
                common.add_known_dependancy("aws_subnet",sn)
                if not globals.dnet:
                    common.add_known_dependancy("aws_route_table_association",sn)   
                    common.add_dependancy("aws_route_table_association",sn)
                    common.add_dependancy("aws_vpc_ipv4_cidr_block_association",sn)
                    common.add_dependancy("aws_vpc_endpoint", sn)

        elif id.startswith("vpc-"):
            try:
                if globals.vpclist[id]:
                    common.write_import(type, id, None)
                    common.add_known_dependancy("aws_subnet",id)
                    if not globals.dnet:
                        common.add_known_dependancy("aws_route_table_association",id)   
                        common.add_dependancy("aws_route_table_association",id)
                        common.add_dependancy("aws_vpc_ipv4_cidr_block_association",id)
                        common.add_dependancy("aws_vpc_endpoint", id)

                    pkey = type+"."+id
                    globals.rproc[pkey] = True
                else:
                    print("WARNING: vpc not in vpclist" + id)
            except KeyError:
                    print("WARNING: vpc not in vpclist " + id+ " Resource may be referencing a vpc that no longer exists")  
            
        else:
            print("WARNING: get_aws_vpc unexpected id value",str(id))
            return True
                    

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_subnet(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_subnet doing " + type + ' with id ' + str(id) +
            " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    try:    
        if id is None:
            for sn in globals.subnetlist.keys():
               common.write_import(type,sn,None)

        elif id.startswith("subnet-"):
            try:
                if globals.subnetlist[id]:
                    common.write_import(type, id, None)
                    pkey = type+"."+id
                    globals.rproc[pkey] = True
                else:
                    print("WARNING: subnet not in subnetlist" + id)
            except KeyError:
                    print("WARNING: subnet not in subnetlist " + id+ " Resource may be referencing a subnet that no longer exists")  
            
        elif id.startswith("vpc-"):
            for j in globals.subnets:
                if j['VpcId'] == id:
                    #print("Found subnet in vpc " + id + " " + j['SubnetId'])
                    common.write_import(type, j['SubnetId'], None)
        else:
            print("WARNING: get_aws_subnet unexpected id value",str(id))
            return True
                    

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_security_group(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_security_group doing " + type + ' with id ' + str(id) +
            " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    try:    
        if id is None:
            for sn in globals.sglist.keys():
                common.write_import(type,sn,None)
                if not globals.dsgs: 
                    common.add_dependancy("aws_security_group_rule",sn)
                    pkey = type+"."+sn
                    globals.rproc[pkey] = True

        elif id.startswith("sg-"):
            try:
                if globals.sglist[id]:
                    common.write_import(type, id, None)
                    if not globals.dsgs:
                        common.add_dependancy("aws_security_group_rule",id)

                    pkey = type+"."+id
                    globals.rproc[pkey] = True
                else:
                    print("WARNING: sg not in sglist" + id)
            except KeyError:
                    print("WARNING: sg not in sglist " + id+ " Resource may be referencing a security_group that no longer exists")  
            
        else:
            print("WARNING: get_aws_security_group unexpected id value",str(id))
            return True
                    

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_instance(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        session = boto3.Session(region_name=globals.region,profile_name=globals.profile)
        client = session.client(clfn)
        #client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                for k in j['Instances']:
                    if globals.ec2tag is None:
                        if k['State']['Name'] == 'running' or k['State']['Name'] == 'stopped':
                            common.write_import(type,k[key],None) 
                    else:
                        tags=k['Tags']
                        #print(json.dumps(tags, indent=2, default=str))
                        for tag in tags:
                            if tag['Key'] == globals.ec2tagk:
                                if tag['Value'] == globals.ec2tagv:
                                    if k['State']['Name'] == 'running' or k['State']['Name'] == 'stopped':
                                        common.write_import(type, k[key], None)

        else:  
            if id.startswith("i-"):    
                response = client.describe_instances(InstanceIds=[id])
            else:
                response = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': [id]},])
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response['Reservations']:
                
                for k in j['Instances']:
                    #print(json.dumps(k['Tags'],indent=2,default=str))
                    
                    if k['State']['Name'] == 'running' or k['State']['Name'] == 'stopped':
                        common.write_import(type,k[key],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_security_group_rule(type, id, clfn, descfn, topkey, key, filterid):

    if globals.debug:
        print("--> In get_security_group_rule doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.describe_security_group_rules()        
        else:        
            if id.startswith("sg-"):
                response = client.describe_security_group_rules(Filters=[{'Name': 'group-id','Values': [id]},])
                pkey="aws_security_group_rule."+id
                globals.rproc[pkey] = True
            else:  # assume it's security group name
                response = client.describe_security_group_rules(GroupNames=[id]) 
                for j in response[topkey]:
                    gid=j['GroupId']
                    pkey="aws_security_group_rule."+gid
                    globals.rproc[pkey] = True



        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        

        
        for j in response[topkey]:
            protocol="";fromport="";toport="";cidr4="";cidr6="";prefixlistid="";refgrp_sgid="";refgrp_peerst="";refgrp_userid="";refgrp_vpcid="";refgrp_peerid=""
            
            try:
                sgid=j['GroupId']
                if j['IsEgress']:
                    ing="egress"
                else:
                    ing="ingress"
            except KeyError:
                pass
            try:
                protocol=j['IpProtocol']
            except KeyError:
                pass
            try:
                fromport=str(j['FromPort'])
            except KeyError:
                pass
            try:
                toport=str(j['ToPort'])
            except KeyError:
                pass
            try:
                cidr4=j['CidrIpv4']
            except KeyError:
                pass
            try:
                cidr6=j['CidrIpv6']
            except KeyError:
                pass
            try:
                prefixlistid=j['PrefixListId']
            except KeyError:
                pass
            try:   
                refgrp_sgid=j['ReferencedGroupInfo']['GroupId']
            except KeyError:
                pass
            try:
                refgrp_peerst=j['ReferencedGroupInfo']['PeeringStatus']
            except KeyError:
                pass
            try:
                refgrp_userid=j['ReferencedGroupInfo']['UserId']
            except KeyError:
                pass
            try:
                refgrp_vpcid=j['ReferencedGroupInfo']['VpcId']
            except KeyError:
                pass
            try:
                refgrp_peerid=j['ReferencedGroupInfo']['VpcPeeringConnectionId']
            except KeyError:
                pass

            #if "icmp" in protocol:
            #    print(str(j))


            if "icmp" not in protocol:
                if protocol=="-1": protocol="all"
                if fromport=="-1": fromport="0"
                if toport=="-1": toport="0"


            #if ing=="ingress" and sgid=="sg-0b70930caea1aac99": 
                #print(str(j))
            #    print("************1************")
            #    print(sgid+ing+protocol+fromport+toport)
            #    print("************2************")
            #    print(cidr4+cidr6+prefixlistid)
            #    print("************3************")
            #    print(refgrp_sgid+refgrp_peerst+refgrp_userid+refgrp_vpcid+refgrp_peerid)


            impstring=sgid+"_"+ing
            #print("protocol="+protocol)
            if protocol != "": impstring=impstring + "_" + protocol
            if fromport != "": impstring=impstring + "_" + fromport
            if toport != "": impstring= impstring + "_" + toport
            if cidr4 != "": impstring= impstring + "_" + cidr4
            if cidr6 != "": impstring= impstring + "_" + cidr6
            if refgrp_sgid != "": impstring= impstring + "_" + refgrp_sgid
            #else:
            #    if cidr4 != "": impstring= impstring + "_" + cidr4
            #    if cidr6 != "": impstring= impstring + "_" + cidr6
            if prefixlistid !="": impstring= impstring + "_" + prefixlistid

            common.write_import(type,impstring,None) 
            pkey="aws_security_group_rule."+sgid
            globals.rproc[pkey] = True


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True



def get_aws_eip(type, id, clfn, descfn, topkey, key, filterid):

    if globals.debug:
        print("--> In get_aws_eip doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.describe_addresses()        
        else:        
            response = client.describe_addresses(AllocationIds=[id])


        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response[topkey]:
            common.write_import(type,j[key],None) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_eip_association(type, id, clfn, descfn, topkey, key, filterid):

    if globals.debug:
        print("--> In get_aws_eip_assocation doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.describe_addresses()        
        else:        
            response = client.describe_addresses(AllocationIds=[id])


        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response[topkey]:
            try:
                asocid=j['AssociationId']
                common.write_import(type,j['AssociationId'],None) 
            except KeyError:
                return True

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


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
                            if 'SubnetId' in item['Associations'][r]:
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
                            elif 'GatewayId' in item['Associations'][r]:
                                gwid = str(item['Associations'][r]['GatewayId'])
                                theid = gwid+"/"+rtid
                                common.write_import(type, theid, None)
                                pkey = type+"."+gwid
                                globals.rproc[pkey] = True

                        except Exception as e:
                           common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

                     else:
                         pkey="aws_route_table_association"+"."+vpcid
                         if globals.debug: print("Setting " + pkey + "=True")
                         globals.rproc[pkey] = True

            # set subnet true now ? as there's no assoc.
            for ti in globals.rproc.keys():
                if not globals.rproc[ti]:
                    if "aws_route_table_association.subnet" in str(ti):
                        globals.rproc[ti] = True
                        #print("************** Setting " + ti + "=True")
        else:
            print("No response for get_aws_route_table_association")
            if id is not None:
                pkey="aws_route_table_association"+"."+id
                if globals.debug: print("Setting " + pkey + "=True")
                globals.rproc[pkey] = True


                        
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
 

    return True


def get_aws_launch_template(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_launch_template    doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    response = common.call_boto3(type,clfn, descfn, topkey, key, id)
    # print("-9a->"+str(response))
    if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True

    for j in response:
        retid = j['LaunchTemplateId']
        theid = retid
        common.write_import(type, theid, id)

    return True

def get_aws_vpc_ipv4_cidr_block_association(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_vpc_ipv4_cidr_block_association doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        client = boto3.client(clfn)
        response=[]

        if id is None:
            response = client.describe_vpcs()
            
        else:
            response = client.describe_vpcs(VpcIds=[id])
        #response = common.call_boto3(type,clfn, descfn, topkey, key, id)    
  
        if response[topkey] == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response[topkey]:
            cidrb = j['CidrBlockAssociationSet']
            vpcid = j['VpcId']
            vpc_cidr = j['CidrBlock']
            if id==vpcid:
                for k in cidrb:
                    if vpc_cidr == k['CidrBlock']: 
                        pkey = type+"."+vpcid
                        globals.rproc[pkey] = True
                        continue
                    theid=k['AssociationId']
                    specid=vpcid+"__"+theid
                    common.write_import(type, theid, specid)
                    pkey = type+"."+vpcid
                    globals.rproc[pkey] = True
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_subnet_old(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_subnet doing " + type + ' with id ' + str(id) +
            " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

    response = common.call_boto3(type,clfn, descfn, topkey, key, id)
    #print("-9a->"+str(response))
    
    try:
        if response == []: 
            if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
            if id is not None:
                pkey = type+"."+id
                globals.rproc[pkey] = True
            return True
        
        if id is None:
            for j in response: 
                subid=j[key]
                try:
                    if globals.subnetlist[subid]:
                        common.write_import(type, j[key], None) 
                    else:
                            print("WARNING: subnet not in subnetlist" + subid)
                except KeyError:
                    print("WARNING: subnet not in subnetlist " + subid+ " Resource may be referencing a subnet that no longer exists")    
        
        elif "subnet-" in id:
            for j in response:
                subid=j['SubnetId']
                
            if id==subid: 
                try:
                    if globals.subnetlist[subid]:
                        common.write_import(type, j[key], None)
                    else:
                            print("WARNING: subnet not in subnetlist" + subid)
                except KeyError:
                    print("WARNING: subnet not in subnetlist " + subid+ " Resource may be referencing a subnet that no longer exists")


        elif "vpc-" in id:
            for j in response:
                vpcid=j['VpcId']
                if id==vpcid: 
                    common.write_import(type, j[key], None)
                    pkey = type+"."+vpcid
                    globals.rproc[pkey] = True


    
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)


    return True




def get_aws_network_acl(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_network_acl doing " + type + ' with id ' + str(id) +
            " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

## vall boto3 with Filter default=false

    response = []
    client = boto3.client(clfn)
    paginator = client.get_paginator(descfn)
    #print("51a paginator")
    # TODO - just get all onlce and use @@@@ globals
    try:
        if id is not None:
            if "acl-" in id:
                for page in paginator.paginate(Filters=[
                    {
                        'Name': 'association.network-acl-id',
                        'Values': [id]
                    },
                    {
                        'Name': 'default',
                        'Values': ['false']
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
                        'Values': ['false']
                    }
                    ]):
                    response.extend(page[topkey])
            else:
                print("Error in get_aws_route_table_association unexpected id value")
        else:
            for page in paginator.paginate(Filters=[{'Name': 'default', 'Values': ['false']}]):
                response.extend(page[topkey])



################################################################


        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        
        if id is None:
            for j in response: common.write_import(type, j[key], None)     
        
        else:
            for j in response:
                common.write_import(type, j[key], None)
                pkey = type+"."+j[key]
                globals.rproc[pkey] = True

    
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_default_network_acl(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In get_aws_default_network_acl doing " + type + ' with id ' + str(id) +
            " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

## vall boto3 with Filter default=false
    try:
        response = []
        client = boto3.client(clfn)
        paginator = client.get_paginator(descfn)
            # TODO - just get all onlce and use @@@@ globals
        if id is not None:
            if id .startswith("acl-"):
                for page in paginator.paginate(Filters=[
                    {
                        'Name': 'association.network-acl-id',
                        'Values': [id]
                    },
                    {
                        'Name': 'default',
                        'Values': ['true']
                    }
                    ]):
                    response.extend(page[topkey])
            elif id.startswith("vpc-"):
                for page in paginator.paginate(Filters=[
                    {
                        'Name': 'vpc-id',
                        'Values': [id]
                    },
                    {
                        'Name': 'default',
                        'Values': ['true']
                    }
                    ]):
                    response.extend(page[topkey])
            else:
                print("Error in get_aws_route_table_association unexpected id value")
        else:
            for page in paginator.paginate(Filters=[
                    {
                        'Name': 'default',
                        'Values': ['true']
                    }
                    ]):
                    response.extend(page[topkey])    

        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        
        if id is None:
            for j in response: common.write_import(type, j[key], None)     
        
        else:
            for j in response:
                common.write_import(type, j[key], None)
                pkey = type+"."+j[key]
                globals.rproc[pkey] = True

    
    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
       
    return True


def get_aws_key_pair(type, id, clfn, descfn, topkey, key, filterid):

    if globals.debug:
        print("--> In get_aws_key_pair  doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
        
    try:

        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.describe_key_pairs()
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                common.write_import(type,j[key],None) 

        else:            
            response = client.describe_key_pairs(KeyNames=[id])
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                common.write_import(type,j[key],None) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_ebs_encryption_by_default(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        common.write_import(type,"default",None) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_vpc_dhcp_options_association(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        if id is None:
            print("WARNING: No id or invalid id provided for "+type)
        else:
            if "|" in id:
                vpcid=id.split("|")[1]
            elif id.startswith("vpc-"):
                vpcid=id
            else:
                print("WARNING: No id or invalid id provided for "+type)
                return True
            
            print("vpcid="+vpcid)
            common.write_import(type,vpcid,None) 

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_route(type, id, clfn, descfn, topkey, key, filterid):
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
                routes=j['Routes']
                print(str(routes))
                common.write_import(type,j[key],None) 

        else:      
            response = client.describe_route_tables(RouteTableIds=[id])
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        for j in response[topkey]:
            routes=j['Routes']
            print(str(routes))
            common.write_import(type,j[key],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)


    return True


def get_aws_spot_datafeed_subscription(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        common.write_import(type,"spot-datafeed-subscription",None) 



    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

#aws_vpc_endpoint_route_table_association
def get_aws_vpc_endpoint_route_table_association(type, id, clfn, descfn, topkey, key, filterid):
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
                endpid=j[key]
                #print(str(j))
                try:
                    for k in j['RouteTableIds']:
                        theid=endpid+"/"+k
                        common.write_import(type,theid,None) 
                except KeyError:
                    print("No route table ids for endpoint "+endpid)
                    continue
                

        else:      
            response = client.describe_vpc_endpoints(VpcEndpointIds=[id])
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response[topkey]
            endpid=j[key]
            for k in j['RouteTableIds']:
                theid=endpid+"/"+k
                common.write_import(type,theid,None) 
                common.write_import(type,j[key],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_ec2_transit_gateway(type, id, clfn, descfn, topkey, key, filterid):
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
                common.add_known_dependancy("aws_ec2_transit_gateway_vpc_attachment",j[key])
                common.add_known_dependancy("aws_ec2_transit_gateway_peering_attachment", j[key])
                common.add_known_dependancy("aws_ec2_transit_gateway_route_table", j[key])
                common.add_known_dependancy("aws_ec2_transit_gateway_vpn_attachment", j[key])

        else: 
            if id.startswith("tgw-"):     
                response = client.describe_transit_gateways(TransitGatewayIds=[id,],)
                if response[topkey] == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
                for j in response[topkey]:
                    common.write_import(type,j[key],None)
                    common.add_known_dependancy("aws_ec2_transit_gateway_vpc_attachment",j[key])
                    common.add_known_dependancy("aws_ec2_transit_gateway_peering_attachment", j[key])
                    common.add_known_dependancy("aws_ec2_transit_gateway_route_table", j[key])
                    common.add_known_dependancy("aws_ec2_transit_gateway_vpn_attachment", j[key])


            else:
                print("WARNING: "+type+" id must start with tgw-")


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_ec2_transit_gateway_vpc_attachment(type, id, clfn, descfn, topkey, key, filterid):
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
            if id.startswith("tgw-"):     
                response = client.describe_transit_gateway_vpc_attachments(Filters=[{'Name': 'transit-gateway-id','Values': [id]}])
                if response[topkey] == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
                for j in response[topkey]:
                    common.write_import(type,j[key],None)
              
            elif id.startswith("vpc-"):     
                response = client.describe_transit_gateway_vpc_attachments(Filters=[{'Name': 'vpc-id','Values': [id]}])
                if response[topkey] == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
                for j in response[topkey]:
                    common.write_import(type,j[key],None)

            else:
                print("WARNING: "+type+" id must start with tgw- or vpc-")


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_ec2_transit_gateway_peering_attachment(type, id, clfn, descfn, topkey, key, filterid):
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
            if id.startswith("tgw-"):     
                response = client.describe_transit_gateway_peering_attachments(Filters=[{'Name': 'transit-gateway-id','Values': [id]}])
                if response[topkey] == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
                for j in response[topkey]:
                    common.write_import(type,j[key],None)           
            else:
                print("WARNING: "+type+" id must start with tgw- or vpc-")


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_ec2_transit_gateway_route_table(type, id, clfn, descfn, topkey, key, filterid):
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
                common.add_dependancy("aws_ec2_transit_gateway_route",j[key])
 
        else: 
            if id.startswith("tgw-"):     
                response = client.describe_transit_gateway_route_tables(Filters=[{'Name': 'transit-gateway-id','Values': [id]}])
                if response[topkey] == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
                for j in response[topkey]:
                    common.write_import(type,j[key],None)   
                    common.add_dependancy("aws_ec2_transit_gateway_route",j[key])        
            else:
                print("WARNING: "+type+" id must start with tgw- or vpc-")


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_ec2_transit_gateway_route(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            print("WARNING: "+type+" id must pass Transit gateway route table id")
 
        else: 
            if id.startswith("tgw-rtb-"):     
                response = client.search_transit_gateway_routes(TransitGatewayRouteTableId=id,Filters=[{'Name': 'type','Values': ['static']}])
                if response[topkey] == []: 
                    if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                    pkey=type+"."+id
                    globals.rproc[pkey]=True
                    return True
                for j in response[topkey]:
                    pkey=id+"_"+j[key]
                    common.write_import(type,pkey,id)           
            else:
                print("WARNING: "+type+" id must start with tgw-rtb-")


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_vpc_endpoint_service(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            response = client.describe_vpc_endpoint_services(Filters=[{'Name': 'owner','Values': [globals.acc]},],)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response[topkey]:
                common.write_import(type,j[key],None) 

        else:      
            response = client.describe_vpc_endpoint_services(ServiceNames=[id])
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            j=response
            common.write_import(type,j[key],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_ec2_transit_gateway_vpn_attachment(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(Filters=[
                {'Name': 'resource-type','Values': ['vpn']},
                {'Name': 'state','Values': ['available','pending','pendingAcceptance']}
                ]):
                response = response + page[topkey]
            #print(response)
            if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
            for j in response:
                fn="data_"+type+"-"+j[key]+".tf"
                if os.path.exists(fn): os.remove(fn)
                fn="data_"+type+"-"+j[key]+".tfproto"
                theid=type+"_"+j[key]
                tgwid=j['TransitGatewayId']
                vpnid=j['ResourceId']
                with open(fn, "w") as f:
                    f.write('data \"aws_ec2_transit_gateway_vpn_attachment\" \"'+theid+'\" {\n')
                    f.write(' transit_gateway_id = aws_ec2_transit_gateway.'+tgwid+'.id \n')
                    f.write(' vpn_connection_id  = aws_vpn_connection.'+vpnid+'.id \n')
                    f.write('}\n')
                common.add_dependancy("aws_ec2_transit_gateway",tgwid)
                common.add_dependancy("aws_vpn_connection",vpnid)
 
 
        else: 
            if id.startswith("tgw-"):     
                response = client.describe_transit_gateway_attachments(Filters=[
                    {'Name': 'transit-gateway-id','Values': [id]},
                    {'Name': 'resource-type','Values': ['vpn']},
                    {'Name': 'state','Values': ['available','pending','pendingAcceptance']}
                    ])
                if response[topkey] == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
                for j in response[topkey]:
                    fn="data_"+type+"-"+j[key]+".tf"
                    if os.path.exists(fn): os.remove(fn)
                    fn="data_"+type+"-"+j[key]+".tfproto"
                    theid=type+"_"+j[key]
                    tgwid=j['TransitGatewayId']
                    vpnid=j['ResourceId']
                    with open(fn, "w") as f:
                        f.write('data \"aws_ec2_transit_gateway_vpn_attachment\" \"'+theid+'\" {\n')
                        f.write(' transit_gateway_id = aws_ec2_transit_gateway.'+tgwid+'.id \n')
                        f.write(' vpn_connection_id  = aws_vpn_connection.'+vpnid+'.id \n')
                        f.write('}\n')
                common.add_dependancy("aws_ec2_transit_gateway",tgwid)
                common.add_dependancy("aws_vpn_connection",vpnid)
                        
              
            elif id.startswith("vpc-"):     
                response = client.describe_transit_gateway_attachments(Filters=[
                    {'Name': 'vpc-id','Values': [id]},
                    {'Name': 'resource-type','Values': ['vpn']},
                    {'Name': 'state','Values': ['available','pending','pendingAcceptance']}
                    ])
                if response[topkey] == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
                for j in response[topkey]:
                    fn="data_"+type+"-"+j[key]+".tf"
                    if os.path.exists(fn): os.remove(fn)
                    fn="data_"+type+"-"+j[key]+".tfproto"
                    theid=type+"_"+j[key]
                    tgwid=j['TransitGatewayId']
                    vpnid=j['ResourceId']
                    with open(fn, "w") as f:
                        f.write('data \"aws_ec2_transit_gateway_vpn_attachment\" \"'+theid+'\" {\n')
                        f.write(' transit_gateway_id = aws_ec2_transit_gateway.'+tgwid+'.id \n')
                        f.write(' vpn_connection_id  = aws_vpn_connection.'+vpnid+'.id \n')
                        f.write('}\n')
                    common.add_dependancy("aws_ec2_transit_gateway",tgwid)
                    common.add_dependancy("aws_vpn_connection",vpnid)
               

            else:
                print("WARNING: "+type+" id must start with tgw- or vpc-")


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


# get_aws_vpc_endpoint
def get_aws_vpc_endpoint(type, id, clfn, descfn, topkey, key, filterid):
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
            if response == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                return True
            for j in response:
                common.write_import(type, j[key], None)

        elif id.startswith("vpc-"):
            pkey=type+"."+id
            response = client.describe_vpc_endpoints(Filters=[{'Name': 'vpc-id','Values': [id]},])
            if response == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                globals.rproc[pkey]=True
                return True
            for j in response[topkey]:
                common.write_import(type, j[key], None) 
            globals.rproc[pkey]=True

        
        elif id.startswith("vpce-"):
            pkey=type+"."+id
            response = client.describe_vpc_endpoints(VpcEndpointIds=[id])
            if response == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
                globals.rproc[pkey]=True
                return True
            for j in response[topkey]:
                common.write_import(type, j[key], None)
            globals.rproc[pkey]=True

        else:
            print("WARNING: "+type+" id unexpected = "+ str(id))

    except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

    return True

