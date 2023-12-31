import common
import botocore
import globals
import fixtf2

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
      #print("**********************VPC Lattice listener"+str(theid))
      fixtf2.add_dependancy("aws_vpclattice_listener",theid)

   return True

def get_aws_vpclattice_service_network_vpc_association(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug: 
      print("--> In get_aws_vpclattice_service_network_vpc_association doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   get_aws_vpc_lattice(type,id,clfn,descfn,topkey,key,filterid)
   return True

def get_aws_vpclattice_service_network_service_association(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug: 
      print("--> In get_aws_vpclattice_service_network_vpc_association doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   get_aws_vpc_lattice(type,id,clfn,descfn,topkey,key,filterid)
   return True

def get_aws_vpclattice_access_log_subscription(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug: 
      print("--> In get_aws_vpclattice_service_network_vpc_association doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   get_aws_vpc_lattice(type,id,clfn,descfn,topkey,key,filterid)
   return True

def get_aws_vpclattice_auth_policy(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug: 
      print("--> In get_aws_vpclattice_auth_policy doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   
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
         response = getfn(resourceIdentifier=id)  ## special
         #response=response1[topkey]
   except Exception as e:
      print(f"{e=}")
      print("unexpected error in paginate")
      exit()
      

   if response == []: 
      print("empty response returning") 
      return 
   else:
       print("**********************VPC Lattice auth policy"+str(response))  
   for j in response: 
        #retid=j['id']
        #theid=retid
        ### turn id into an arn ?
        thearn="arn:aws:vpclattice:"+globals.region+":"+globals.acc+":auth-policy/"+id
        # can use the arn - wants to import with id

        common.write_import(type,id,None) 
        #fixtf2.add_dependancy("aws_vpclattice_listener_rule",theid)
        #globals.rproc["aws_vpclattice_listener."+id]=True

   return True
   



def get_aws_vpclattice_listener(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug:  print("--> In get_aws_vpclattice_listener doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   print("--> In get_aws_vpclattice_listener doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)



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
         response1 = getfn(serviceIdentifier=id)  ## special
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
        theid=id+"/"+retid
        common.write_import(type,theid,None) 
        fixtf2.add_dependancy("aws_vpclattice_listener_rule",theid)
        globals.rproc["aws_vpclattice_listener."+id]=True

   return True


# need to deal with id  svc/ruleid - extract ruleid
def get_aws_vpclattice_listener_rule(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug:  print("--> In get_aws_vpclattice_listener doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   print("--> In get_aws_vpclattice_listener doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)



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
         svid=id.split("/")[0]
         rlid=id.split("/")[1]
         print(f"{svid=},{rlid=}")
         getfn = getattr(client, descfn)
         response1 = getfn(serviceIdentifier=svid,listenerIdentifier=rlid)  ## special
         response=response1[topkey]
   except Exception as e:
      print(f"{e=}")
      print("unexpected error in paginate")
      exit()
      
   print("***>>>>"+str(response))
   if response == []: 
      print("empty response returning") 
      return   
   for j in response: 
        retid=j['id']
        theid=svid+"/"+rlid+"/"+retid
        common.write_import(type,theid,None) 
   globals.rproc["aws_vpclattice_listener_rule."+id]=True     

   return True





def get_aws_vpc_lattice(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug: print("--> In generic get_aws_vpclattice doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

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

   return True




