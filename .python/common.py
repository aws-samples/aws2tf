import boto3
import sys
import subprocess
import fixtf
import os
import globals
import glob
import botocore
import fixtf2


def tfplan1():
   print("Plan 1 ... ")
   rf="resources.out"
   com="terraform plan -generate-config-out="+ rf + " -json | jq . > plan1.json"
   print(com)
   rout=rc(com)
   
   file="plan1.json"
   f2=open(file, "r")
   plan2=True

   while True:
      line = f2.readline()
      if not line:
         break
      #print(line)
      if '@level": "error"' in line:
         if globals.debug is True:
            print("Error" + line)
         try:
               mess=f2.readline()
               try:
                  i=mess.split('(')[2].split(')')[0]
                  print("Removing "+i+" files - plan errors see plan1.json")
                  com="rm -f s3-*"+ i + "import__*s3-*.tf aws_s3_*__b-"+ i +".tf main.tf"
                  rout=rc(com)
                  globals.plan2=True
               except:
                  if globals.debug is True:
                     print(mess.strip())
                  globals.plan2=True
         except:
               print("Error - no error message, check plan1.json")
               #continue
               exit()

   #print("Plan 1 complete -- resources.out generated")

   if not os.path.isfile("resources.out"):
         print("could not find expected resources.out file after Plan 1 - exiting")
         exit()  
   return

def tfplan2():
   print("Plan 2 ... ")
   if not os.path.isfile("resources.out"):
         print("could not find expected resources.out file after Plan 1 - exiting")
         exit()

   #print("split resources.out")
   splitf("resources.out")

   print("fix tf files.....") 
        
   x=glob.glob("aws_*__*.out")
   for fil in x:
         type=fil.split('__')[0]
         tf=fil.split('.')[0]
         #print("type="+type+" tf="+tf)
         #if type not in globals.types:
         #   globals.types=globals.types+[type]             
         fixtf.fixtf(type,tf)


def tfplan3():
   print("Plan 3 ... ")
   rf="resources.out"
   ## Derived dependancies here:
   # move files
   # DD's
   # and plan
   # and vaidate
         
   com="terraform fmt"
   rout=rc(com)
 
   com="terraform validate -no-color"
   rout=rc(com)
   el=len(rout.stderr.decode().rstrip())
   if el!=0:
      errm=rout.stderr.decode().rstrip()
      print(errm)
   if "Success! The configuration is valid" not in str(rout.stdout.decode().rstrip()):
      print(str(rout.stdout.decode().rstrip()))
      print("Validation after fix failed - exiting")
      exit()


   else: 
      print("Valid Configuration.")
      if globals.validate: exit()


   if globals.plan2:
      
      print("Plan 4 ... ")
      # redo plan
      com="rm -f resources.out tfplan"
      print(com)
      rout=rc(com)
      com="terraform plan -generate-config-out="+ rf + " -out tfplan -json > plan2.json"
      print(com)
      rout=rc(com)
      zerod=False
      zeroc=False
      with open('plan2.json', 'r') as f:
         for line in f.readlines():
            #print(line)
            if '0 to destroy' in line:
              zerod=True
            if '0 to change' in line:
              zeroc=True
            if '@level":"error"' in line:
              if globals.debug is True:
                 print("Error" + line)
              print("-->> Plan 2 errors exiting - check plan2.json - or run terraform plan")
              exit()

      if not zerod:
         print("-->> plan will destroy - unexpected, is there existing state ?")
         print("-->> look at plan2.json - or run terraform plan")
         exit()

      if not zeroc:
         print("-->> plan will change resources - unexpected, is there existing state ?")
         print("-->> look at plan2.json - or run terraform plan")
         exit()

      print("Plan 4 complete")
   
   if not os.path.isfile("tfplan"):
         print("could not find expected tfplan file - exiting")
         exit()
         


def wrapup():
   #print("split main.tf")
   #splitf("main.tf")
   print("Validate json")
   com="terraform validate -no-color -json > validate.json"
   rout=rc(com)
   print("Validate")
   com="terraform validate -no-color"
   rout=rc(com)
   el=len(rout.stderr.decode().rstrip())
   if el!=0:
      errm=rout.stderr.decode().rstrip()
      print(errm)
   if "Success! The configuration is valid" not in str(rout.stdout.decode().rstrip()):
      print(str(rout.stdout.decode().rstrip()))
   else: 
      print("Valid Configuration.")
   

   #print(str(rout.stdout.decode().rstrip()))
   # do the import via apply
   print("terraform import via apply of tfplan....")
   com="terraform apply -no-color tfplan"
   rout=rc(com)
   print(str(rout.stdout.decode().rstrip()))
   print("Final Plan check .....")
   com="terraform plan -no-color"
   rout=rc(com)
   if "No changes. Your infrastructure matches the configuration" not in str(rout.stdout.decode().rstrip()):
      print(str(rout.stdout.decode().rstrip()))
   else: 
      print("No changes in plan")
      com="mv import__*.tf *.out *.json imported"
      rout=rc(com)




def rc(cmd):
    out = subprocess.run(cmd, shell=True, capture_output=True)
    ol=len(out.stdout.decode('utf-8').rstrip())    
    el=len(out.stderr.decode().rstrip())
    if el!=0:
         errm=out.stderr.decode().rstrip()
         #print(errm)
         #exit(1)

    # could be > /dev/null
    #if ol==0:
    #    print("No return from command " + str(cmd))
    
    #print(out.stdout.decode().rstrip())
    return out

def ctrl_c_handler(signum, frame):
  print("Ctrl-C pressed.")
  exit()


def check_python_version():
  version = sys.version_info
  major = version.major
  minor = version.minor
  if major < 3 or (major == 3 and minor < 7):
    print("This program requires Python 3.7 or later.")
    sys.exit(1)



def aws_tf(region):
   if not os.path.isfile("aws.tf"):
      with open("aws.tf", 'w') as f3: 
         f3.write('terraform {\n')
         f3.write('  required_version = "> 1.5.6"\n')
         f3.write('  required_providers {\n')
         f3.write('    aws = {\n')
         f3.write('      source  = "hashicorp/aws"\n')
         f3.write('      version = "> 5.16"\n')
         f3.write('    }\n')
         f3.write('  }\n')
         f3.write('}\n')
         f3.write('provider "aws" {\n')
         f3.write('  region                   = "' + region +'"\n')
         f3.write('  shared_credentials_files = ["~/.aws/credentials"]\n')
         #f3.write('  profile                  = var.profile\n')
         f3.write('}\n')
         f3.write('data "aws_region" "current" {}\n')
         f3.write('data "aws_caller_identity" "current" {}\n')
         f3.write('data "aws_availability_zones" "az" {\n')
         f3.write('state = "available"\n')
         f3.write('}\n')


# split resources.out
def splitf(file):
   lhs=0
   rhs=0
   if os.path.isfile(file):
      print("split file:"+ file)
      with open(file, "r") as f:
         Lines = f.readlines()
      for tt1 in Lines:
         #print(tt1)
         if "{" in tt1: lhs=lhs+1
         if "}" in tt1: rhs=rhs+1
         if lhs > 1:
               if lhs == rhs:
                  try:
                     f2.write(tt1+"\n")
                     f2.close()
                     lhs=0
                     rhs=0
                     continue
                  except:
                     pass

         if tt1.startswith("resource"):
               #print("resource: " + tt1)
               ttft=tt1.split('"')[1]
               taddr=tt1.split('"')[3]
               if globals.acc in taddr:
                  a1=taddr.find(globals.acc)
                  taddr=taddr[:a1]+taddr[a1+12:]
                  #print("taddr="+taddr)
      
               f2=open(ttft+"__"+taddr+".out","w")
               f2.write(tt1)

         elif tt1.startswith("#"):
               continue
         elif tt1=="" or tt1=="\n":
               continue
         else:
               try:
                  f2.write(tt1)
               except:
                  print("tried to write to closed file: >"+ tt1 + "<")
   else:
      print("could not find expected main.tf file")
      
        
   com="mv "+file +" imported/" +file
   rout=rc(com)  
   #com="terraform fmt"
   #rout=rc(com) 


# if type == "aws_vpc_endpoint": return "ec2","describe_vpc_endpoints","VpcEndpoints","VpcEndpointId","vpc-id"

#generally pass 3rd param as None - unless overriding
def write_import(type,theid,tfid):
   if tfid is None:
      tfid=theid.replace("/","__").replace(".","__").replace(":","__")
   fn="import__"+type+"__"+tfid+".tf"
   
   # check if file exists:
   #
   if os.path.isfile(fn):
      if globals.debug: print("File exists: " + fn)
      pkey=type+"."+tfid
      globals.rproc[pkey]=True
      return
   
   with open(fn, "a") as f:
      f.write('import {\n')
      f.write('  to = ' +type + '.' + tfid + '\n')
      f.write('  id = "'+ theid + '"\n')
      f.write('}\n')

   pkey=type+"."+tfid
   globals.rproc[pkey]=True

   return

#########################################################################################################################

def getresource(type,id,clfn,descfn,topkey,key,filterid):
   for j in globals.specials:
      if type == j: 
         print(type + " in specials list returning ..")
         return False
   if "aws_launch" in type: print("-1-> In getresource doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

   if type in str(globals.types): 
      print("Found "+type+"in types skipping ...")
      return True
   #print("--4 >")
   try:
      if id is not None:
         pt=type+"."+id
         if pt in globals.rproc:
            if globals.rproc[pt] is True:
               print("Found "+pt+" in processed skipping ...") 
               return True
      response=call_boto3(clfn,descfn,topkey,id)   
      #print("-->"+str(response))
      if str(response) != "[]":
            for item in response:
               #print("-"+str(item))
               #print("-gr01-")
               if id is None or filterid=="": # do it all
                  #print("-gr21-")
                  if globals.debug: print("--"+str(item))
                  try:
                     if "aws-service-role" in str(item["Path"]): 
                        print("Skipping service role " + str(item[key])) 
                        continue
                  except:
                     pass

                  
                  theid=item[key]
                  pt=type+"."+theid
                  if pt not in globals.rproc:
                     write_import(type,theid,None)
                  else:
                     if globals.rproc[pt] is True:
                        print("Found "+pt+" in processed skipping ...") 
                        continue
               else:
                  #print("-gr31-"+"filterid="+str(filterid)+" id="+str(id))
                  if "." not in filterid:
                     #print("***item=" + str(item))
                     try:
                        if id == str(item[filterid]):
                           #print("--"+str(item))
                           theid=item[key]
                           special_deps(type,theid)
                           write_import(type,theid,None)
                     except:
                        print("Could have done write_import "+type+" "+id)
                        return False
                  else:
                     ### There's a dot in the filterid so we need to dig deeper
                     print(str(item))
                     print("id="+id+" filterid="+filterid)
                     filt1=filterid.split('.')[1]
                     filt2=filterid.split('.')[3]
                     print("filt1="+filt1+" filt2="+filt2)
                     dotc=len(item[filt1])
                     print("dotc="+str(dotc))

                     for j in range(0,dotc):
                        #print(str(item[filt1][j]))
                        try:
                           val=str(item[filt1][j][filt2])
                           print("val="+val + " id=" + id)
                           if id == val:
                              theid=item[key]
                              if dotc>1: theid=id+"/"+item[key]
                              write_import(type,theid,None)
                        except:
                           print("-------- error on processing")
                           print(str(item))
                           print("filterid="+filterid)
                           print("----------------------------")
                           pass
      else:
         if id is not None:
            print("No "+type+" "+id+" found -empty response")         
         else:
            print("No "+type+" found -empty response")
         return True
   
   except Exception as e:
      print(f"{e=}")
      print("unexpected error in common.getresource")
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      exit()
        

   return True               
  
    #tfplan(type)

def special_deps(ttft,taddr):
   #print("In special deps"+ttft+"  "+taddr)
   if ttft == "aws_subnet": 
      add_known_dependancy("aws_route_table_association",taddr) 
      fixtf2.add_dependancy("aws_route_table_association",taddr)  
   elif ttft == "aws_vpc": 
      add_known_dependancy("aws_route_table_association",taddr)   
      fixtf2.add_dependancy("aws_route_table_association",taddr)
   elif ttft == "aws_vpclattice_service_network":
      add_known_dependancy("aws_vpclattice_service",taddr) 
      add_known_dependancy("aws_vpclattice_service_network_vpc_association",taddr) 
      # ../../scripts/get-vpclattice-auth-policy.sh $cname
      # ../../scripts/get-vpclattice-resource-policy.sh $rarn
      # ../../scripts/get-vpclattice-service-network-service-associations.sh $cname
      # ../../scripts/get-vpclattice-access-log-subscription.sh $cname

   return  


def get_test(type,id,clfn,descfn,topkey,key,filterid):
   print("in get_test")
   print("--> In get_test doing "+ type + ' with id ' + str(id))   
   return

#def get_aws_vpc_dhcp_options(type,id,clfn,descfn,topkey,key,filterid):
#   print("in get_aws_vpc_dhcp_options")
#   print("--> In get_test doing "+ type + ' with id ' + str(id))   
#   return

def get_aws_route_table_association(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug: print("--> In get_aws_route_table_association doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   if type in str(globals.types): 
      print("Found "+type+"in types skipping ...")
      return

  
   response = []
   client = boto3.client(clfn) 
   paginator = client.get_paginator(descfn)
   if "subnet-" in id:
      for page in paginator.paginate(Filters=[
            {
                  'Name': 'association.subnet-id',
                  'Values': [id]
            },
         ]):
         response.extend(page[topkey])  
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
               if subid in str(globals.rproc):
                  #print(subid+" in processed....")
                  theid=subid+"/"+rtid
                  write_import(type,theid,None)    
                  pkey=type+"."+id
                  globals.rproc[pkey]=True    
            except:
               pass
   return


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
                  write_import(type,theid,None)


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
            write_import(type,theid,None) 
   
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
                  write_import(type,retid,pn)
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
                  write_import(type,retid,pn)  
   
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
               add_known_dependancy("aws_iam_policy",retid)
               globals.dependancies=globals.dependancies + ["aws_iam_policy."+retid]
            #print("adding "+theid+" attachment")
            write_import(type,theid,rn) 
   return

def get_aws_vpclattice_service(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug:  print("--> In get_aws_vpclattice_service doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

   client = boto3.client(clfn) 
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
            write_import(type,theid,None) 

   return

def get_aws_vpclattice_service_network_vpc_association(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug: print("--> In get_aws_vpclattice_service_network_vpc_association doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

   client = boto3.client(clfn) 
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
            write_import(type,theid,None) 

   return

# as list_clusters is awkward
def get_aws_eks_cluster(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug: print("--> In get_aws_eks_cluster doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   response=call_boto3(clfn,descfn,topkey,id)

   if response == []: 
      print("empty response returning") 
      return   
   for j in response: 
      retid=j # no key
      theid=retid
      write_import(type,theid,None) 
      # add fargate known dependancy for cluster name
      add_known_dependancy("aws_eks_fargate_profile",theid)
      add_known_dependancy("aws_eks_node_group",theid) 
    

   return

def get_aws_eks_fargate_profile(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug: print("--> In get_aws_eks_fargate_profile  doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   response=call_boto3(clfn,descfn,topkey,id)

   if response == []: 
      print("empty response returning") 
      return   
   for j in response: 
      retid=j # no key
      # need to ocerwrite theid
      theid=id+":"+retid
      rn=id+"__"+retid
      print("rn="+rn)
      print("theid="+theid)
      write_import(type,theid,rn) 

   return

def get_aws_eks_node_group(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug: print("--> In get_aws_eks_fargate_profile  doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   response=call_boto3(clfn,descfn,topkey,id)

   if response == []: 
      print("empty response returning") 
      return   
   for j in response: 
      retid=j # no key
      # need to ocerwrite theid
      theid=id+":"+retid
      rn=id+"__"+retid
      print("rn="+rn)
      print("theid="+theid)
      write_import(type,theid,rn) 

   return


def get_aws_launch_template(type,id,clfn,descfn,topkey,key,filterid):
   if globals.debug: print("--> In get_aws_launch_template    doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   response=call_boto3(clfn,descfn,topkey,id)
   #print("-9a->"+str(response))
   if response == []: 
      print("empty response returning") 
      return   
   for j in response: 
            retid=j['LaunchTemplateId']
            theid=retid
            write_import(type,theid,id) 

   return






def add_known_dependancy(type,id):
    # check if we alredy have it
    pkey=type+"."+id
    if pkey not in globals.rdep:
        print("add_known_dependancy: " + pkey)
        globals.rdep[pkey]=False
    return


def call_boto3(clfn,descfn,topkey,id):
   
   try:
      if globals.debug: print("calling boto3")
      if globals.debug: print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
      if globals.debug: print("pre-response")
      response = []
      client = boto3.client(clfn) 
      if globals.debug: print("client")

      try:
         paginator = client.get_paginator(descfn)
         if globals.debug: print("paginator")

         if descfn == "describe_launch_templates":
            #print("*******  describe_launch_templates  ********" )
            if id is not None:
               if "lt-" in id:
                  for page in paginator.paginate(LaunchTemplateIds=[id]): response.extend(page[topkey])
               else:
                  #print("--->> id="+str(id))
                  for page in paginator.paginate(LaunchTemplateNames=[id]): response.extend(page[topkey])
            else:
               for page in paginator.paginate(): response.extend(page[topkey])

         if descfn == "list_fargate_profiles" or descfn == "list_nodegroups" :
            #print("--1a "+str(id))
            for page in paginator.paginate(clusterName=id): response.extend(page[topkey])
         else:
            #print("--1b")
            for page in paginator.paginate(): 
               response.extend(page[topkey])

      except botocore.exceptions.OperationNotPageableError as err:
            print(f"{err=}")
            print("calling non paginated fn "+str(descfn))
            getfn = getattr(client, descfn)
            response1 = getfn()
            response=response1[topkey]

      except Exception as e:
         print(f"{e=}")
         print("-1->unexpected error in common.call_boto3")
         print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
         exc_type, exc_obj, exc_tb = sys.exc_info()
         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
         print(exc_type, fname, exc_tb.tb_lineno)
         exit()

      #print("--2a")  
      rl=len(response)
      #print("--2b" + str(rl)) 
      if rl==0:
         print("** zero response length for "+ descfn + " returning .. []")
         return []

      if globals.debug:
         print("response length="+str(len(response)))
         
         for item in response:
            print(item)
            print("--------------------------------------")
   except Exception as e:
         print(f"{e=}")
         print("-2->unexpected error in common.call_boto3")
         print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
         exc_type, exc_obj, exc_tb = sys.exc_info()
         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
         print(exc_type, fname, exc_tb.tb_lineno)
         exit()

   return response