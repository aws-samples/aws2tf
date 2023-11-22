#!/usr/bin/env python3

import common
import boto3
import globals
import os
import sys

def get_aws_route_table_association(type,id,clfn,descfn,topkey,key,filterid):
   try:
      if globals.debug: print("--> In get_aws_route_table_association doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
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
         else:
            print("Error in get_aws_route_table_association unexpected id value")
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
                     if id is not None:
                        if subid == id:
                           theid=subid+"/"+rtid
                           common.write_import(type,theid,None)    
                           pkey=type+"."+subid
                           globals.rproc[pkey]=True 
                     else:
                           theid=subid+"/"+rtid
                           common.write_import(type,theid,None)    
                           pkey=type+"."+subid
                           globals.rproc[pkey]=True 

               except:
                  pass
   except Exception as e:
            print(f"{e=}")
            print("-1->unexpected error in common.call_boto3")
            print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
      
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





