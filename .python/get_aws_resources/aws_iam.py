import common
import boto3
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
               if k not in str(globals.policies):
                  print("adding "+k+" to policies for role " + rn)
                  globals.policies = globals.policies + [k]
                  theid=rn+":"+k
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
   if id is None:
   
      paginator = client.get_paginator(descfn)
      if globals.debug: print("Paginator")

      try:
         for page in paginator.paginate(Scope='Local'):  # special
            response.extend(page[topkey])
      except Exception as e:
         print(f"{e=}")
   
   elif "arn:" in id:
      #print("hi")
      response1 = client.get_policy(PolicyArn=id)
      #print(str(response1))
      response=response1['Policy']

   if response == []: 
      if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
      return True
 
    
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

            if globals.debug: print("policy name="+str(pn))      
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

         if globals.debug: print("policy name="+str(pn))
            #print("response="+str(retid)+" id="+str(id))
         
         if theid not in str(globals.policies):
                  #print("-- adding "+theid+" to policies")
                  globals.policies = globals.policies + [theid]
                  globals.policyarns = globals.policyarns + [retid]
                  common.write_import(type,retid,pn)  
   
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

def get_aws_iam_role_policy(type, id, clfn, descfn, topkey, key, filterid):
   if globals.debug:
      print("--> In get_aws_iam_role_policy  doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   try:
      if id is None:
         print("Id is None for "+type+ " returning")
         return True
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
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate():
                response = response + page[topkey]
            if response == []: 
               if globals.debug: print("Empty response for "+type+ " id="+str(id)+" returning")
               return True
            for j in response:
                rn=j[key]  ## RoleName
                rna=rn.replace(".","_")
                common.write_import(type,j[key],rna)
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
   
   for j in response: 
            retid=j['PolicyArn']
            theid=id+"/"+retid
            ln=retid.rfind("/")
            pn=retid[ln+1:]
            rn=id+"__"+pn
            # - no as using policy arns (minus account id etc)
            if "arn:aws:iam::aws:policy" not in theid:
               common.add_dependancy("aws_iam_policy",retid)
               
            #print("adding "+theid+" attachment")
            common.write_import(type,theid,rn) 
   pkey="aws_iam_role_policy_attachment."+id
   globals.rproc[pkey]=True
   return True




##
## special due to mandator role name,
##
def get_aws_iam_policy_attchment(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug:
      print("--> In get_aws_iam_policy_attachment doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

   print("Use alternatives to"+type+" not implemented")
   return
   