import common
import fixtf
import base64
import boto3
import globals
import botocore
import inspect

# as list_clusters is awkward
def get_aws_eks_cluster(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug:
      print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   response=common.call_boto3(type,clfn,descfn,topkey,key,id)
   if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
  
   for j in response: 
        retid=j # no key
        theid=retid
        common.write_import(type,theid,None) 
        # add fargate known dependancy for cluster name
        common.add_known_dependancy("aws_eks_fargate_profile",theid)
        common.add_known_dependancy("aws_eks_node_group",theid) 
        common.add_known_dependancy("aws_eks_identity_provider_config",theid)
        common.add_known_dependancy("aws_eks_addon",theid)
        common.add_known_dependancy("aws_eks_pod_identity_association", theid)
        common.add_known_dependancy("aws_eks_access_entry", theid)

   return True

def get_aws_eks_fargate_profile(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug:
      print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   
   try:
      if id is None:
            print("No id passed in get_aws_eks_fargate_profile returning")  
            return True
      
      
      
      response=common.call_boto3(type,clfn,descfn,topkey,key,id)
      if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True

      for j in response: 
         retid=j # no key
         # need to ocerwrite theid
         theid=id+":"+retid
         rn=id+"__"+retid
         common.write_import(type,theid,rn) 

   except Exception as e:
      common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

   return True

def get_aws_eks_node_group(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug:
      print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

   try:
      if id is None:
            print("No id passed in get_aws_eks_node_group returning")  
            return True
      
      
      response=common.call_boto3(type,clfn,descfn,topkey,key,id)
      if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
   
      for j in response: 
         retid=j # no key
         # need to ocerwrite theid
         theid=id+":"+retid
         rn=id+"__"+retid
         common.write_import(type,theid,rn) 

   except Exception as e:
      common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

   return True

def get_aws_eks_addon(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug:
      print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
      
   try:
       
      if id is None:
            print("No id passed in get_aws_eks_addon returning")  
            return True
      
      
      response=common.call_boto3(type,clfn,descfn,topkey,key,id)

      if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True

      for j in response:
         retid=j # no key
         # need to ocerwrite theid
         theid=id+":"+retid
         rn=id+"__"+retid
         common.write_import(type,theid,rn) 

   except Exception as e:
      common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

   return True



def get_aws_eks_identity_provider_config(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug:
      print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   try:   
      if id is None:
            print("No id passed in aws_eks_identity_provider_config returning")  
            return True
      
      response=common.call_boto3(type,clfn,descfn,topkey,key,id)
      if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
      
      for j in response: 
         print(j)  
         
         retid=j['name'] # no key
         # need to ocerwrite theid
         theid=id+":"+retid
         rn=id+"__"+retid
         common.write_import(type,theid,rn) 

   except Exception as e:
      common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

   return True

def get_aws_eks_pod_identity_association(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug:
      print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

   try:
      if id is None:
         print("No id passed in get_aws_eks_pod_identity_association returning")  
         return True
       
      response = []
      client = boto3.client(clfn)
    
          
      response = client.list_pod_identity_associations(clusterName=id)


      if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        #print(str(response))
      for j in response[topkey]:
            retid=j['associationId']
            theid=id+","+retid
            rn=id+"__"+retid
            common.write_import(type,theid,rn) 


   except Exception as e:
      common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

   return True
   
      
def get_aws_eks_access_entry(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug:
      print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

   try:
      response = []
        
      if id is None:
         print("No id passed in get_aws_eks_access_entry returning")  
         return True      
 
                 
      client = boto3.client(clfn)  
      response = client.list_access_entries(clusterName=id)
   
      if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        #print(str(response))
      for j in response[topkey]:
            retid=j
            theid=id+":"+retid
            common.write_import(type,theid,None) 
            pkey=id+","+retid
            common.add_dependancy("aws_eks_access_policy_association",pkey)


   except Exception as e:
      common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

   return True
  

def get_aws_eks_access_policy_association(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug:
      print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

   try:
      response = []
        
      if id is None:
         print("No id passed in get_aws_eks_access_policy_association returning")  
         return True      
 
      if "," not in id:
         print("Must pass cluster-name,principa_arn to get_aws_eks_access_policy_association returning")  
         return True
      
      if "arn:" not in id:
         print("Must pass cluster-name,principa_arn to get_aws_eks_access_policy_association returning")  
         return True
      
      cln=id.split(',')[0]
      parn=id.split(',')[1]
                 
      client = boto3.client(clfn)  
      response = client.list_associated_access_policies(clusterName=cln,principalArn=parn)
      pkey=type+"."+id
      
      if response[topkey] == []: 
         print("Empty response for "+type+ " id="+str(id)+" returning")
         globals.rproc[pkey]=True
         return True
      
      for j in response[topkey]:
            retid=j[key]
            theid=cln+"#"+parn+"#"+retid
            
            common.write_import(type,theid,None) 
            
      globals.rproc[pkey]=True

   except Exception as e:
      common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
  
   return True