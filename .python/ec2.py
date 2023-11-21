#!/usr/bin/env python3

import common
import boto3

def get_aws_route_table_association(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug: print("--> In get_aws_route_table_association doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   if type in str(globals.types): 
      print("Found "+type+"in types skipping ...")
      return

  
   response = []
   client = boto3.client(clfn) 
   paginator = client.get_paginator(descfn)
   # TODO - just get all onlce and use @@@@ globals
   if "subnet-" in id:
      for page in paginator.paginate(Filters=[
            {
                  'Name': 'association.subnet-id',
                  'Values': [id]
            },
         ]):
         response.extend(page[topkey])  
   else:
      for page in paginator.paginate():
         response.extend(page[topkey])

   #print("response length="+str(len(response)))
   #print(str(response))
   #print(id)
   if str(response) != "[]": 
      for item in response:
         il=len(item['Associations'])
         #print("Associations length="+str(il))
         for r in range(0,il):
            #print(str(r))
            #print(str(item['Associations'][r]))
            rtid=(str(item['Associations'][r]['RouteTableId']))
            try:
               #print(str(item['Associations'][r]['SubnetId']))
               subid=str(item['Associations'][r]['SubnetId'])
               #print(subid+" in pre-rproc....")
               #print(globals.rproc)
               
               # TODO wrong check ? if don't have subnet should add as dependancy
               if subid in str(globals.rproc):

                  # TODO check if already have the association
                  theid=subid+"/"+rtid
                  common.write_import(type,theid,None)    
                  pkey=type+"."+id
                  globals.rproc[pkey]=True    
            except:
               pass
   return

def get_aws_launch_template(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug: print("--> In get_aws_launch_template    doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   response=common.call_boto3(clfn,descfn,topkey,id)
   #print("-9a->"+str(response))
   if response == []: 
      print("empty response returning") 
      return   
   for j in response: 
            retid=j['LaunchTemplateId']
            theid=retid
            common.write_import(type,theid,id) 

   return





