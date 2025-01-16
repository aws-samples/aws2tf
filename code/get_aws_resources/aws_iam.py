import common
import boto3
from botocore.config import Config
import globals
import inspect


def get_aws_iam_role_policy(type,id,clfn,descfn,topkey,key,filterid):
   print("--> In get_aws_iam_role_policy doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   
   client = boto3.client(clfn) 
   response=[]
   rn=id
   if id is None:
      #for j in globals.rproc.keys():
      for j in list(globals.rproc):
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
            for k in response: 
               print("adding "+k+" to policies for role " + rn)
               theid=rn+":"+k
               common.write_import(type,theid,None)


   else:
      response=[]
      paginator = client.get_paginator(descfn)
      for page in paginator.paginate(RoleName=rn):
         response.extend(page[topkey])
      print("RoleName="+rn+" response="+str(response))

      for j in response: 
         print("adding "+j+" to policies for role " + rn)
         theid=rn+":"+j
         common.write_import(type,theid,None) 
   
   return True



##
## special due to scope local
##
def get_aws_iam_policy(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug: print("--> In get_aws_iam_policy doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   
   try:
   
      response=[]
      client = boto3.client(clfn) 
      if globals.debug: print("client")

      if id is None:
         for parn in globals.policylist.keys():
            try:
               ln=parn.rfind("/")
               pn=parn[ln+1:]
            except Exception as e:
                  print("pn error")
                  print(f"{e=}")
            if globals.debug: print("policy name="+str(pn))
            common.write_import(type,parn,pn)
            pkey=type+"."+parn
            globals.rproc[pkey]=True
         return True


# looking for a specific policy arn
      elif "arn:" in id:
         ln=id.rfind("/")
         pn=id[ln+1:]
         response1 = client.get_policy(PolicyArn=id)
         #print(str(response1))
         response=response1['Policy']

      else:
         print("WARNING: must pass arn to get_aws_iam_policy")
         if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
         return True

#######

      if response == []: 
         if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
         pkey=type+"."+id
         globals.rproc[pkey]=True
         return True
### we have a response
      else:
            j=response
            #print("j="+str(j))
            theid=j[key]
            retid=j["Arn"]
            pkey=type+"."+retid

            ln=retid.rfind("/")
            pn=retid[ln+1:]

            if globals.debug: print("policy name="+str(pn))
               #print("response="+str(retid)+" id="+str(id))
            common.write_import(type,retid,pn)  
            pkey=type+"."+retid
            globals.rproc[pkey]=True

   except Exception as e:
        common.handle_error(e, str(inspect.currentframe().f_code.co_name), clfn, descfn, topkey, id)

   return True





def get_aws_iam_instance_profile(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug:
       print("--> In get_aws_iam_instance_profile  doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   
   client = boto3.client(clfn) 
   response=[]

   try:
      response1 = client.get_instance_profile(InstanceProfileName=id)
      j=response1[topkey]
      if j == []: 
         if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
         return True

      #print("get_instance_profile response="+str(j))
 
      theid=j[key]
      common.write_import(type,theid,None) 
      
   except Exception as e:
      common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

   return True

def get_aws_iam_user_group_membership(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug:
       print("--> In get_aws_iam_user_group_membership  doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   
   client = boto3.client(clfn) 
   response=[]

   try:
      grpn=id
      response1 = client.get_group(GroupName=id)
      response=response1[topkey]

      if response == []: 
         if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
         pkey="aws_iam_user_group_membership."+grpn
         globals.rproc[pkey]=True
         return True
      for j in response:
         userid=j[key]
         grpn=id
         theid=userid+"/"+grpn
         common.write_import(type,theid,None) 
         pkey="aws_iam_user_group_membership."+grpn
         globals.rproc[pkey]=True

      
   except Exception as e:
      common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)
                          

   return True


def get_aws_iam_user_policy(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug:
      print("--> In get_aws_iam_user_policy  doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   
   client = boto3.client(clfn) 
   response=[]

   try:
      response1 = client.list_user_policies(UserName=id)
      #print("response1="+str(response1))
      response=response1['PolicyNames']
      if response == []: 
         if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
         pkey="aws_iam_user_policy."+id
         globals.rproc[pkey]=True
         return True
      for j in response:
         polname=j
         theid=id+":"+polname
         common.write_import(type,theid,None) 
         pkey="aws_iam_user_policy."+id
         globals.rproc[pkey]=True

      
   except Exception as e:
      common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)


   return True

def get_aws_iam_group_policy(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug:
      print("--> In get_aws_iam_group_policy  doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   
   client = boto3.client(clfn) 
   response=[]

   try:

      if id is None:
         print("Id must be set to the GroupName")
         return True

      response1 = client.list_group_policies(GroupName=id)
      #print("response1="+str(response1))
      response=response1['PolicyNames']
      if response == []: 
         if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
         pkey="aws_iam_group_policy."+id
         globals.rproc[pkey]=True
         return True
      #print("response="+str(response))
      for j in response:
         polname=j
         theid=id+":"+polname
         common.write_import(type,theid,None) 
         pkey="aws_iam_group_policy."+id
         globals.rproc[pkey]=True

      
   except Exception as e:
      common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)


   return True



def get_aws_iam_service_linked_role(type, id, clfn, descfn, topkey, key, filterid):
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
                if ":role/aws-service-role" in j[key]:
                  common.write_import(type,j[key],None) 

        else:   
              
            response = client.get_role(RoleName=id)
            if response == []: 
               if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
               return True
            j=response
            if ":role/aws-service-role" in j[key]:
               common.write_import(type,j[key],None)

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True

def get_aws_iam_role(type,id,clfn,descfn,topkey,key,filterid):

    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

        
    try:
        client = boto3.client(clfn)
        response = []
        if id is None:

            for rn in globals.rolelist.keys():
               rna=rn.replace(".","_")
               common.write_import(type,rn,rna)
               common.add_dependancy("aws_iam_role_policy_attachment",rn)
               common.add_dependancy("aws_iam_role_policy",rn)

        else:   
            if "/aws-service-role/" in id: return True    
            response = client.get_role(RoleName=id)
            if response == []: 
               if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
               return True
            j=response['Role']
            rn=j[key]
            rna=rn.replace(".","_")
            common.write_import(type,j[key],rna)
            common.add_dependancy("aws_iam_role_policy_attachment",rn)
            common.add_dependancy("aws_iam_role_policy",rn)


    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


##
## special due to mandator role name,
##
def get_aws_iam_role_policy_attachment(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug:
      print("--> In get_aws_iam_role_policy_attachment doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   if id is None:
      print("Id must be set to the RoleName")
      return
   

   #print(len(globals.attached_role_policies_list))
   if len(globals.attached_role_policies_list) == 0:
      client = boto3.client(clfn) 
      response=[]
      paginator = client.get_paginator(descfn)
      try:
         for page in paginator.paginate(RoleName=id):    ## special
         #for page in paginator.paginate():
            response.extend(page[topkey])
      except Exception as e:
         print(f"{e=}")

      if response == []: 
         if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
         pkey="aws_iam_role_policy_attachment."+id
         globals.rproc[pkey]=True
         return True
      ## multi thread ?
      for j in response: 
               retid=j['PolicyArn']
               theid=id+"/"+retid
               ln=retid.rfind("/")
               pn=retid[ln+1:]
               rn=id+"__"+pn
               # - no as using policy arns (minus account id etc)
               #if "andyt1" in retid:
               #   print("********** iarp  id="+str(id)+" theid="+str(theid)+" rn="+rn)
               if "arn:aws:iam::aws:policy" not in theid:
                  common.add_dependancy("aws_iam_policy",retid)
                  
               common.write_import(type,theid,rn) 

   else:
      if globals.attached_role_policies_list[id] is not False:
         for j in globals.attached_role_policies_list[id]:
            #print("********** irap: "+str(j))
            retid=j['PolicyArn']
            theid=id+"/"+retid
            #ln=retid.rfind("/")
            #pn=retid[ln+1:]
            pn=j['PolicyName']
            rn=id+"__"+pn
            # - no as using policy arns (minus account id etc)
            #if "andyt1" in retid:
            #print("********** irap id="+str(id)+" theid="+str(theid)+"retid="+str(retid)+" rn="+rn)
            if "arn:aws:iam::aws:policy" not in theid:
               common.add_dependancy("aws_iam_policy", retid)

            common.write_import(type, theid, rn)
      else:
         pkey="aws_iam_role_policy_attachment."+id
         #print("irap False skipping "+str(id))
            
   
   ####
   pkey="aws_iam_role_policy_attachment."+id
   globals.rproc[pkey]=True
   
   return True


def get_aws_iam_role_policy(type, id, clfn, descfn, topkey, key, filterid):
   if globals.debug:
      print("--> In get_aws_iam_role_policy  doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   try:
      if id is None:
         print("Id is None for "+type+ " returning")
         return True

      #print(len(globals.role_policies_list))
      if len(globals.role_policies_list) == 0:

         client = boto3.client(clfn)
         response=[]

         response1 = client.list_role_policies(RoleName=id)
         #print("response1="+str(response1))
         response=response1['PolicyNames']
         if response == []:
            if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
            pkey="aws_iam_role_policy."+id
            globals.rproc[pkey]=True
            return True
         #print("response="+str(response))
         for j in response:
            polname=j
            theid=id+":"+polname
            common.write_import(type, theid, None)
            pkey="aws_iam_role_policy."+id
            globals.rproc[pkey]=True

      else:
         if globals.role_policies_list[id] is not False:
            for j in globals.role_policies_list[id]:
               #print("********** irp "+str(j))
               polname=j
               theid=id+":"+polname
               #print("*********  irp adding "+str(theid))
               common.write_import(type, theid, None)
               pkey="aws_iam_role_policy."+id
               globals.rproc[pkey]=True
         else:
            #print("*********  irp False skipping "+str(id))
            pkey="aws_iam_role_policy."+id
            globals.rproc[pkey]=True

   except Exception as e:
      common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)


   return True





##
## special due to mandator role name,
##
def get_aws_iam_policy_attchment(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug:
      print("--> In get_aws_iam_policy_attachment doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

   print("Use alternatives to"+type+" not implemented")
   return


#aws_iam_group_policy_attachment
def get_aws_iam_group_policy_attachment(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug:
      print("--> In get_aws_iam_group_policy_attachment doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   if id is None:
      print("Id must be set to the GroupName")
      return True
   

   #print(len(globals.attached_role_policies_list))

   client = boto3.client(clfn) 
   response=[]
   paginator = client.get_paginator(descfn)
   try:
         for page in paginator.paginate(GroupName=id):    ## special
         #for page in paginator.paginate():
            response.extend(page[topkey])
   except Exception as e:
         print(f"{e=}")

   if response == []: 
         if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
         pkey="aws_iam_group_policy_attachment."+id
         globals.rproc[pkey]=True
         return True
      ## multi thread ?
   for j in response: 
               retid=j['PolicyArn']
               theid=id+"/"+retid
               ln=retid.rfind("/")
               pn=retid[ln+1:]
               rn=id+"__"+pn

               if "arn:aws:iam::aws:policy" not in theid:
                  common.add_dependancy("aws_iam_policy",retid)
                  
               common.write_import(type,theid,rn) 

   
   ####
   pkey="aws_iam_group_policy_attachment."+id
   globals.rproc[pkey]=True
   
   return True

def get_aws_iam_group(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn,config=config)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            for j in response:
               common.write_import(type,j[key],None) 
               common.add_dependancy("aws_iam_user_group_membership",j[key])
               common.add_dependancy("aws_iam_group_policy",j[key])
               common.add_dependancy("aws_iam_group_policy_attachment",j[key])

        else:      
            response = client.get_group(GroupName=id)
            if response == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            j=response['Group']
            common.write_import(type,j[key],None)
            common.add_dependancy("aws_iam_user_group_membership",j[key])
            common.add_dependancy("aws_iam_group_policy",j[key])
            common.add_dependancy("aws_iam_group_policy_attachment",j[key])

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True


def get_aws_iam_user(type, id, clfn, descfn, topkey, key, filterid):
    if globals.debug:
        print("--> In "+str(inspect.currentframe().f_code.co_name)+" doing " + type + ' with id ' + str(id) +
              " clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
    try:
        response = []
        config = Config(retries = {'max_attempts': 10,'mode': 'standard'})
        client = boto3.client(clfn,config=config)
        if id is None:
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            for j in response:
               common.write_import(type,j[key],None) 
               common.add_dependancy("aws_iam_user_policy_attachment",j[key])
               common.add_dependancy("aws_iam_user_policy",j[key])
               #list_groups_for_user
               gresponse = client.list_groups_for_user(UserName=j[key])
               for k in gresponse['Groups']:
                common.add_dependancy("aws_iam_user_group_membership", k['GroupName'])

        else:      
            response = client.get_user(UserName=id)
            if response == []: 
                if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning") 
                return True
            j=response['User']
            common.write_import(type,j[key],None)
            common.add_dependancy("aws_iam_user_policy_attachment",j[key])
            common.add_dependancy("aws_iam_user_policy",j[key])
            #list_groups_for_user
            gresponse = client.list_groups_for_user(UserName=j[key])
            for k in gresponse['Groups']:
                common.add_dependancy("aws_iam_user_group_membership", k['GroupName'])

    except Exception as e:
        common.handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

    return True
   

   #aws_iam_group_policy_attachment
def get_aws_iam_user_policy_attachment(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug:
      print("--> In get_aws_iam_user_policy_attachment doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   if id is None:
      print("Id must be set to the UserName")
      return True

   client = boto3.client(clfn) 
   response=[]
   paginator = client.get_paginator(descfn)
   try:
         for page in paginator.paginate(UserName=id):    ## special
         #for page in paginator.paginate():
            response.extend(page[topkey])
   except Exception as e:
         print(f"{e=}")

   if response == []: 
         if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
         pkey="aws_iam_user_policy_attachment."+id
         globals.rproc[pkey]=True
         return True
      ## multi thread ?
   for j in response: 
               retid=j['PolicyArn']
               theid=id+"/"+retid
               ln=retid.rfind("/")
               pn=retid[ln+1:]
               rn=id+"__"+pn

               if "arn:aws:iam::aws:policy" not in theid:
                  common.add_dependancy("aws_iam_policy",retid)
                  
               common.write_import(type,theid,rn) 

   pkey="aws_iam_user_policy_attachment."+id
   globals.rproc[pkey]=True
   
   return True