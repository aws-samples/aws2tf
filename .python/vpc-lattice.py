import common
import botocore

def get_aws_vpclattice_service(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug:  print("--> In get_aws_vpclattice_service doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

   client = common.boto3.client(clfn) 
   if globals.debug: print("--client")
   response=[]
   
   if globals.debug: print("Paginator")

   try:
      paginator = client.get_paginator(descfn)
      for page in paginator.paginate():
         response.extend(page[topkey])
   except botocore.exceptions.OperationNotPageableError as err:
         #print(f"{err=}")
         getfn = getattr(client, descfn)
         response1 = getfn()
         response=response1[topkey]
   except Exception as e:
      print(f"{e=}")
      print("unexpected error in paginate")
      exit()
      

   if response == []: 
      print("empty response returning") 
      return   
   for j in response: 
        retid=j['id']
        theid=retid
        common.write_import(type,theid,None) 

   return

def get_aws_vpclattice_service_network_vpc_association(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug: print("--> In get_aws_vpclattice_service_network_vpc_association doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

   client = common.boto3.client(clfn) 
   if globals.debug: print("--client")
   response=[]
   
   if globals.debug: print("Paginator")

   try:
      paginator = client.get_paginator(descfn)
      for page in paginator.paginate():
         response.extend(page[topkey])
   except botocore.exceptions.OperationNotPageableError as err:
        #print(f"{err=}")
        getfn = getattr(client, descfn)
        response1 = getfn(serviceNetworkIdentifier=id)  ## special
        response=response1[topkey]
   except Exception as e:
      print(f"{e=}")
      print("unexpected error in paginate")
      exit()
      

   if response == []: 
      print("empty response returning") 
      return   
   for j in response: 
            retid=j['id']
            theid=retid
            common.write_import(type,theid,None) 

   return