import common
import boto3
import globals
import sys
import os

##
## hmm inline policies are in the aws_iam_role  anyway !
##
def get_aws_iam_role_policy(type,id,clfn,descfn,topkey,key,filterid):
   print("--> In get_aws_iam_role_policy doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   
   client = boto3.client(clfn) 
   response=[]
   rn=id
   if id is None:
      for j in globals.rproc.keys():
         if "aws_iam_role" in j:
            response=[]
            dotc=j.count('.')
            rn=j.split(".")[1]
            if dotc > 1: rn=rn +"." + j.split(".")[2]         
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(RoleName=rn):   # special
               response.extend(page[topkey])
            if response == []: 
               continue
            #print("--RoleName="+rn+" response="+str(response))
            for j in response: 
               if j not in str(globals.policies):
                  print("adding "+j+" to policies for role " + rn)
                  globals.policies = globals.policies + [j]
                  theid=rn+":"+j
                  common.write_import(type,theid,None)


   else:
      response=[]
      paginator = client.get_paginator(descfn)
      for page in paginator.paginate(RoleName=rn):
         response.extend(page[topkey])
      print("RoleName="+rn+" response="+str(response))

      for j in response: 
         if j not in str(globals.policies):
            print("adding "+j+" to policies for role " + rn)
            globals.policies = globals.policies + [j]
            theid=rn+":"+j
            common.write_import(type,theid,None) 
   
   return True



##
## special due to scope local
##
def get_aws_iam_policy(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug: print("--> In get_aws_iam_policy doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

   client = boto3.client(clfn) 
   if globals.debug: print("client")
   response=[]
   if "arn:" in id:
      print("hi")
      response1 = client.get_policy(PolicyArn=id)
      #print(str(response1))
      response=response1['Policy']

   else:
      paginator = client.get_paginator(descfn)
      if globals.debug: print("Paginator")

      try:
         for page in paginator.paginate(Scope='Local'):  # special
            response.extend(page[topkey])
      except Exception as e:
         print(f"{e=}")

   if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
 
    
   if id is None:
      for j in response: 
            #print("j="+str(j))
            theid=j[key]
            retid=j["Arn"]
            try:
               ln=retid.rfind("/")
               pn=retid[ln+1:]
            except Exception as e:
               print("pn error")
               print(f"{e=}")

            print("policy name="+str(pn))      
            if retid == id:
               if theid not in str(globals.policies):
                  #print("---adding "+theid+" to policies")
                  globals.policies = globals.policies + [theid]
                  globals.policyarns = globals.policyarns + [retid]
                  common.write_import(type,retid,pn)

   else:
         j=response
         #print("j="+str(j))
         theid=j[key]
         retid=j["Arn"]
         try:
            ln=retid.rfind("/")
            pn=retid[ln+1:]
         except Exception as e:
               print("pn error")
               print(f"{e=}")

         print("policy name="+str(pn))
            #print("response="+str(retid)+" id="+str(id))
         
         if theid not in str(globals.policies):
                  #print("-- adding "+theid+" to policies")
                  globals.policies = globals.policies + [theid]
                  globals.policyarns = globals.policyarns + [retid]
                  common.write_import(type,retid,pn)  
   
   return True

##
## special due to mandator role name,
##
def get_aws_iam_policy_attchment(type,id,clfn,descfn,topkey,key,filterid):
   #print("--> In get_aws_iam_policy_attachment doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   if id is None:
      print("Id must be set to the RoleName")
      return
   client = boto3.client(clfn) 
   response=[]
   paginator = client.get_paginator(descfn)
   try:
      for page in paginator.paginate(RoleName=id):    ## special
      #for page in paginator.paginate():
         response.extend(page[topkey])
   except Exception as e:
      print(f"{e=}")

   if response == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True
   
   for j in response: 
            retid=j['PolicyArn']
            theid=id+"/"+retid
            ln=retid.rfind("/")
            pn=retid[ln+1:]
            rn=id+"__"+pn
            # - no as using policy arns (minus account id etc)
            if "arn:aws:iam::aws:policy" not in theid:
               common.add_known_dependancy("aws_iam_policy",retid)
               globals.dependancies=globals.dependancies + ["aws_iam_policy."+retid]
            #print("adding "+theid+" attachment")
            common.write_import(type,theid,rn) 
   return True



def get_aws_iam_instance_profile(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug:
       print("--> In get_aws_iam_instance_profile  doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   
   client = boto3.client(clfn) 
   response=[]

   try:
      response1 = client.get_instance_profile(InstanceProfileName=id)
      j=response1[topkey]
      if j == []: print("Empty response for "+type+ " id="+str(id)+" returning"); return True

      #print("get_instance_profile response="+str(j))
 
      theid=j[key]
      common.write_import(type,theid,None) 
      
   except Exception as e:
        print(f"{e=}")
        print("ERROR: -2->unexpected error in aws_iam_instance_profile")
        print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        exit()



   return True

