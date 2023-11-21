import common
import boto3


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
   
   return



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

   if response == []: 
      print("empty response returning") 
      return  
    
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
   
   return

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
   #print("response="+str(response))
   if response == []: 
      print("empty response returning") 
      return   
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
   return
