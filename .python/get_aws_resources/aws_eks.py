import common
import fixtf
import base64
import boto3
import globals
import botocore
import inspect

# as list_clusters is awkward
def get_aws_eks_cluster(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug: print("--> In get_aws_eks_cluster doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
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

   return True

def get_aws_eks_fargate_profile(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug: print("--> In get_aws_eks_fargate_profile  doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   response=common.call_boto3(type,clfn,descfn,topkey,key,id)
   if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True

   for j in response: 
      retid=j # no key
      # need to ocerwrite theid
      theid=id+":"+retid
      rn=id+"__"+retid
      #print("rn="+rn)
      #print("theid="+theid)
      common.write_import(type,theid,rn) 

   return True

def get_aws_eks_node_group(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug: print("--> In get_aws_eks_fargate_profile  doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   response=common.call_boto3(type,clfn,descfn,topkey,key,id)
   if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
 
   for j in response: 
      retid=j # no key
      # need to ocerwrite theid
      theid=id+":"+retid
      rn=id+"__"+retid
      print("rn="+rn)
      print("theid="+theid)
      common.write_import(type,theid,rn) 

   return True

def get_aws_eks_addon(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug: print("--> In get_aws_eks_addon  doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   response=common.call_boto3(type,clfn,descfn,topkey,key,id)

   if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True

   for j in response:
      print("**********************EKS Addon"+str(j)) 
      retid=j # no key
      # need to ocerwrite theid
      theid=id+":"+retid
      rn=id+"__"+retid
      print("rn="+rn)
      print("theid="+theid)
      common.write_import(type,theid,rn) 

   return True



def get_aws_eks_identity_provider_config(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug: print("--> In get_aws_eks_identity_provider_config  doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   response=common.call_boto3(type,clfn,descfn,topkey,key,id)
   if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
   
   for j in response: 
      print(j)  
      
      retid=j['name'] # no key
      # need to ocerwrite theid
      theid=id+":"+retid
      rn=id+"__"+retid
      print("rn="+rn)
      print("theid="+theid)
      common.write_import(type,theid,rn) 

   return True

def get_aws_eks_pod_identity_association(type,id,clfn,descfn,topkey,key,filterid):
   #if globals.debug: 
   print("--> In get_aws_eks_identity_provider_config  doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

   try:
        response = []
        client = boto3.client(clfn)
        if id is None:
            print("No id passed in get_aws_eks_pod_identity_association returning")        
        else:        
            response = client.list_pod_identity_associations(clusterName=id)


        if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
        print(str(response))
        for j in response[topkey]:
            retid=j['associationId']
            theid=id+":"+retid
            rn=id+"__"+retid
            print("rn="+rn)
            print("theid="+theid)
            common.write_import(type,theid,rn) 


   except botocore.errorfactory.ResourceNotFoundException as err:
      print(f"{err=}"+","+type+","+clfn)
      return []

   except Exception as e:
      common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
   
      

  

