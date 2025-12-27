import common
from common import log_warning
import logging
log = logging.getLogger('aws2tf')
import boto3
import context
import inspect
from botocore.config import Config

# as list_clusters is awkward
def get_aws_eks_cluster(type,id,clfn,descfn,topkey,key,filterid):
   if context.debug:
      log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
 
 
   response = []
   config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
   client = boto3.client(clfn,config=config)
   if id is None:
      paginator = client.get_paginator(descfn)
      for page in paginator.paginate():
         response = response + page[topkey]
      if response == []: 
         #if context.debug: 
         log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
         return True
      
      for j in response: 
         retid=j # no key
         theid=retid
         common.write_import(type,theid,None) 
         # add fargate known dependancy for cluster name
         common.add_known_dependancy("aws_eks_fargate_profile",theid)
         common.add_known_dependancy("aws_eks_node_group",theid) 
         common.add_known_dependancy("aws_eks_identity_provider_config",theid)
         common.add_known_dependancy("aws_eks_addon",theid)
         #common.add_known_dependancy("aws_eks_pod_identity_association", theid)
         common.add_known_dependancy("aws_eks_access_entry", theid)
 
   else:      
      response = client.describe_cluster(name=id)
      if response == []: 
         #if context.debug: 
         log.debug("Empty response for "+type+ " id="+str(id)+" returning") 
         return True
      
      theid=id
      common.write_import(type,theid,None) 
         # add fargate known dependancy for cluster name
      common.add_known_dependancy("aws_eks_fargate_profile",theid)
      common.add_known_dependancy("aws_eks_node_group",theid) 
      common.add_known_dependancy("aws_eks_identity_provider_config",theid)
      common.add_known_dependancy("aws_eks_addon",theid)
      #common.add_known_dependancy("aws_eks_pod_identity_association", theid)
      common.add_known_dependancy("aws_eks_access_entry", theid)




   return True

def get_aws_eks_fargate_profile(type,id,clfn,descfn,topkey,key,filterid):
   if context.debug:
      log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   
   try:
      if id is None:
         log.info("No id passed in get_aws_eks_fargate_profile returning")  
         return True
      
      
      
      response=common.call_boto3(type,clfn,descfn,topkey,key,id)
      if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True

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
   if context.debug:
      log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

   try:
      if id is None:
            log.info("No id passed in get_aws_eks_node_group returning")  
            return True
      
      
      response=common.call_boto3(type,clfn,descfn,topkey,key,id)
      if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
   
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
   if context.debug:
      log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
      
   try:
       
      if id is None:
            log.info("No id passed in get_aws_eks_addon returning")  
            return True
      
      
      response=common.call_boto3(type,clfn,descfn,topkey,key,id)

      if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True

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
   if context.debug:
      log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   try:   
      if id is None:
            log.info("No id passed in aws_eks_identity_provider_config returning")  
            return True
      
      response=common.call_boto3(type,clfn,descfn,topkey,key,id)
      if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
      
      for j in response: 
         log.info(j)  
         
         retid=j['name'] # no key
         # need to ocerwrite theid
         theid=id+":"+retid
         rn=id+"__"+retid
         common.write_import(type,theid,rn) 

   except Exception as e:
      common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

   return True

def get_aws_eks_pod_identity_association(type,id,clfn,descfn,topkey,key,filterid):
   if context.debug:
      log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

   try:
      if id is None:
         log.info("No id passed in get_aws_eks_pod_identity_association returning")  
         return True
       
      response = []
      client = boto3.client(clfn)
    
          
      response = client.list_pod_identity_associations(clusterName=id)


      if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
      for j in response[topkey]:
            retid=j['associationId']
            theid=id+","+retid
            rn=id+"__"+retid
            common.write_import(type,theid,rn) 


   except Exception as e:
      common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

   return True
   
      
def get_aws_eks_access_entry(type,id,clfn,descfn,topkey,key,filterid):
   if context.debug:
      log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

   try:
      response = []
        
      if id is None:
         log.info("No id passed in get_aws_eks_access_entry returning")  
         return True      
 
                 
      client = boto3.client(clfn)  
      response = client.list_access_entries(clusterName=id)
   
      if response == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
      for j in response[topkey]:
            ## need to get the type
            retid=j
            theid=id+":"+retid
            pkey=id+","+retid
            if "aws-service-role" in j:
               log.info("INFO: aws-service-role in get_aws_eks_access_entry returning")
               context.rproc[pkey]=True
               continue

            resp2=client.describe_access_entry(clusterName=id,principalArn=j)
            if resp2 == []: log.debug("Empty response for "+type+ " id="+str(id)+" returning"); return True
            if resp2['accessEntry']['type'] == 'STANDARD':
               common.write_import(type,theid,None) 
               common.add_dependancy("aws_eks_access_policy_association",pkey)


   except Exception as e:
      common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

   return True
  

def get_aws_eks_access_policy_association(type,id,clfn,descfn,topkey,key,filterid):
   if context.debug:
      log.debug("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

   try:
      response = []
        
      if id is None:
         log.info("No id passed in get_aws_eks_access_policy_association returning")  
         return True      
 
      if "," not in id:
         log.warning("Must pass cluster-name,principa_arn to get_aws_eks_access_policy_association returning")  
         return True
      
      if "arn:" not in id:
         log.warning("Must pass cluster-name,principa_arn to get_aws_eks_access_policy_association returning")  
         return True
      
      cln=id.split(',')[0]
      parn=id.split(',')[1]
      pkey=type+"."+id
      if "aws-service-role" in parn: 
         log.info("INFO: aws-service-role in get_aws_eks_access_policy_association returning")
         context.rproc[pkey]=True
         return True           
      client = boto3.client(clfn)  
      response = client.list_associated_access_policies(clusterName=cln,principalArn=parn)
      
      
      if response[topkey] == []: 
         if context.debug: log.debug("Empty response for "+type+ " id="+str(id)+" returning")
         context.rproc[pkey]=True
         return True
      
      for j in response[topkey]:
            retid=j[key]
            theid=cln+"#"+parn+"#"+retid
            
            common.write_import(type,theid,None) 
            
      context.rproc[pkey]=True

   except Exception as e:
      common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
  
   return True