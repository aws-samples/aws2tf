import boto3
import sys
import subprocess
import os
import globals
import glob
import botocore
import fixtf2


def tfplan1():
   print("Plan 1 ... ")
   rf="resources.out"
   #com="terraform plan -generate-config-out="+ rf + " -out tfplan -json > plan2.json"


   if not glob.glob("import*.tf"):
      print("No import*.tf files found for this resource, exiting ....")
      exit()


   com="terraform plan -generate-config-out="+ rf + " -out tfplan -json | jq . > plan1.json"
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
                  if "VPC Lattice" in mess and "404" in mess:
                     print("ERROR: VPC Lattice 404 error - see plan1.json")
                     i=mess.split('(')[1].split(')')[0].split('/')[-1]
                     print("ERROR: Removing "+i+" files - plan errors see plan1.json")
                     globals.badlist=globals.badlist+[i]
                     com="rm -f import__*"+i+"*.tf"
                     print(com)
                     rout=rc(com)



               except:
                  pass

               try:
                  i=mess.split('(')[2].split(')')[0]
                  print("ERROR: Removing "+i+" files - plan errors see plan1.json")
                  globals.badlist=globals.badlist+[i]
                  com="rm -f import__*"+i+"*.tf aws_*"+ i +"*.tf"
                  print(com)
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
   print("fix tf files.....") 
   if not os.path.isfile("resources.out"):
         print("could not find expected resources.out file after Plan 1 - exiting")
         exit()

   #print("split resources.out")
   splitf("resources.out")
   #zap the badlist
   for i in globals.badlist:
      com="rm -f aws_*"+i+"*.out"+" aws_*"+i+"*.tf"
      print("ERROR: Removing "+i+" files - plan errors see plan1.json")
      print(com)
      rout=rc(com)


        
   x=glob.glob("aws_*__*.out")
   for fil in x:
         type=fil.split('__')[0]
         tf=fil.split('.')[0]
         #print("type="+type+" tf="+tf)
         #if type not in globals.types:
         #   globals.types=globals.types+[type]             
         fixtf(type,tf)
   com="terraform fmt"
   rout=rc(com)


def tfplan3():
   print("tfplan3  ... ")
   if not glob.glob("aws_*.tf"):
      print("No aws_*.tf files found for this resource, exiting ....")
      exit()

   rf="resources.out"
         
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
      zeroa=False
      with open('plan2.json', 'r') as f:
         for line in f.readlines():
            #print(line)
            if '0 to destroy' in line:
              zerod=True
            if '0 to change' in line:
              zeroc=True
            if '0 to add' in line:
              zeroa=True

            if '@level":"error"' in line:
              if globals.debug is True:
                 print("Error" + line)
              print("-->> Plan 2 errors exiting - check plan2.json - or run terraform plan")
              exit()

      if not zerod:
         print("-->> plan will destroy resources! - unexpected, is there existing state ?")
         print("-->> look at plan2.json - or run terraform plan")
         exit()

      if not zeroc:
         print("-->> plan will change resources! - unexpected, is there existing state ?")
         print("-->> look at plan2.json - or run terraform plan")
         exit()

      if not zeroa:
         print("-->> plan will add resources! - unexpected")
         print("-->> look at plan2.json - or run terraform plan")
         exit()

      print("Plan 4 complete")
   
   if not os.path.isfile("tfplan"):
         print("Plan 4 - could not find expected tfplan file - exiting")
         exit()
         


def wrapup():
   #print("split main.tf")
   #splitf("main.tf")
   #print("Validate json")
   #com="terraform validate -no-color -json > validate.json"
   #rout=rc(com)
   print("Validate")
   com="terraform validate -no-color"
   rout=rc(com)
   el=len(rout.stderr.decode().rstrip())
   if el!=0:
      errm=rout.stderr.decode().rstrip()
      print(errm)
   if "Success! The configuration is valid" not in str(rout.stdout.decode().rstrip()):
      print(str(rout.stdout.decode().rstrip()))
      exit()
   else: 
      print("PASS: Valid Configuration.")
   

   #print(str(rout.stdout.decode().rstrip()))
   # do the import via apply
   print("terraform import via apply of tfplan....")
   com="terraform apply -no-color tfplan"
   rout=rc(com)
   zerod=False
   zeroc=False
   print(str(rout.stdout.decode().rstrip()))
   print("Final Plan check .....")
   com="terraform plan -no-color"
   rout=rc(com)
   if "No changes. Your infrastructure matches the configuration" not in str(rout.stdout.decode().rstrip()):
      print(str(rout.stdout.decode().rstrip()))
   else: 
      print("PASS: No changes in plan")
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
         f3.write('      version = "5.30.0"\n')
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



def fixtf(ttft,tf):
  
    rf=tf+".out"
    tf2=tf+".tf"
    if globals.debug:
        print(ttft+" fixtf "+tf+".out") 
   
    try:
        f1 = open(rf, 'r')
    except:
        print("no "+rf)
        return
    Lines = f1.readlines()
    #print("getfn for fixtf2."+ttft+" "+tf2)
    with open(tf2, "a") as f2:
        skip=0
        flag1=False
        flag2=tf
        f2.write("##START,"+ttft+"\n")
        for t1 in Lines:
            tt1=t1.split("=")[0].strip()
            try:
                tt2=t1.split("=")[1].strip()
            except:
                tt2=""

             
            try:              
                getfn = getattr(fixtf2, ttft)
            except Exception as e:
                print(f"{e=}")
                print("** no fixtf2 for "+ttft+" calling generic fixtf2.aws_resource")
                #print("t1="+t1) 
                getfn = getattr(fixtf2, "aws_resource")
          
            try:
                #print("calling fixtf2."+ttft+" "+tf2)
                skip,t1,flag1,flag2=getfn(t1,tt1,tt2,flag1,flag2)
            except Exception as e:
                print(f"{e=}")
                print("-- no fixtf2 for "+ttft+" calling generic fixtf2.aws_resource")
                #print("t1="+t1) 
                skip,t1,flag1,flag2=fixtf2.aws_resource(t1,tt1,tt2,flag1,flag2)



            if skip == 0:
                f2.write(t1)
                

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
               #if globals.acc in taddr:
               #   a1=taddr.find(globals.acc)
               #   taddr=taddr[:a1]+taddr[a1+12:]
               #   #print("taddr="+taddr)
      
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
   if type=="aws_kms_alias":
      print(pkey+" setting True")
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
                  print("-gr21-")
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
                  special_deps(type,theid)
               else:  
                  if globals.debug: print("-gr31-"+"filterid="+str(filterid)+" id="+str(id))
                  if "." not in filterid:
                     #print("***item=" + str(item))
                     try:
                        if id == str(item[filterid]):
                           #print("--"+str(item))
                           theid=item[key]
                           special_deps(type,theid)
                           write_import(type,theid,None)
                     except:
                        print("Could have done write_import "+type+" id="+id+" filterid="+filterid)
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
      fixtf2.add_dependancy("aws_vpc_ipv4_cidr_block_association",taddr)
   elif ttft == "aws_vpclattice_service_network":
      add_known_dependancy("aws_vpclattice_service",taddr) 
      add_known_dependancy("aws_vpclattice_service_network_vpc_association",taddr) 
      add_known_dependancy("aws_vpclattice_service_network_service_association",taddr)

      #add_known_dependancy("aws_vpclattice_auth_policy",taddr) get-auth-policy (resource-identifier)
      #add_known_dependancy("aws_vpclattice_resource_policy",taddr)
      # add_known_dependancy("aws_vpclattice_access_log_subscription",taddr) (resource-identifier)
      ## target group

      ## listener


   return  


def get_test(type,id,clfn,descfn,topkey,key,filterid):
   print("in get_test")
   print("--> In get_test doing "+ type + ' with id ' + str(id))   
   return

#def get_aws_vpc_dhcp_options(type,id,clfn,descfn,topkey,key,filterid):
#   print("in get_aws_vpc_dhcp_options")
#   print("--> In get_test doing "+ type + ' with id ' + str(id))   
#   return


def add_known_dependancy(type,id):
    # check if we alredy have it
    pkey=type+"."+id
    if pkey not in globals.rdep:
        print("add_known_dependancy: " + pkey)
        globals.rdep[pkey]=False
    return



## TODO - always get all / paginate all - save in globals - filter on id in get_aws_ ??
## but in smaller use cases may be better to make filtered boto3 calls ?
## this call doesn't take the key

## can't pass filterid - not possible to use for page in paginator.paginate(filterid=id)
# TODO ? won't accept filter id as string param1 in paginate(param1,id) ??
# hench working around using descfn - not ideal



def call_boto3(clfn,descfn,topkey,id):
   
   try:
      if globals.debug: print("call_boto3 clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
      if globals.debug: print("pre-response")
      response=get_boto3_resp(descfn)  # sets response to [] if nothing saved
      if response == []:
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

            elif descfn == "list_fargate_profiles" or descfn == "list_nodegroups" or descfn == "list_identity_provider_configs" or descfn == "list_addons":
               #print("--1a "+str(id))
               for page in paginator.paginate(clusterName=id): response.extend(page[topkey])
            
            elif clfn=="kms" and descfn=="list_aliases" and id is not None:
               if id.startswith("k-"): id=id[2:]
               #print("-- call boto3 --"+str(id))
               for page in paginator.paginate(KeyId=id): response.extend(page[topkey])
               return response
            
            elif clfn=="describe_config_rules" and id is not None:
               for page in paginator.paginate(ConfigRuleNames=id): response.extend(page[topkey])
               return response
            
            elif clfn=="describe_log_groups" and id is not None:
               if "arn:" in id:  
                  ## arn filtering done in get_aws_cloudwatch_log_group()
                  for page in paginator.paginate(): response.extend(page[topkey])
                  return response
               else:
                  for page in paginator.paginate(logGroupNamePattern=id): response.extend(page[topkey])
                  return response            
               
            
            else:
               #print("--1b")
               for page in paginator.paginate(): 
                  response.extend(page[topkey])
               # save a full paginate as we don't want to do it many times
               sav_boto3_rep(descfn,response)

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
            print("** zero response length for "+ descfn + " in call_boto3 returning .. []")
            return []

         if globals.debug:
            print("response length="+str(len(response)))
            
            for item in response:
               print(item)
               print("--------------------------------------")
   
      else:
         print("got global response ")
      
   except Exception as e:
      print(f"{e=}")
      print("-2->unexpected error in common.call_boto3")
      print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      exit()

   return response

def sav_boto3_rep(descfn,response):
   if str(descfn)=="describe_subnets" and globals.aws_subnet_resp==[]:
      globals.aws_subnet_resp=response  
      #print("@@@@ saved global response "+str(descfn))
   #
   if str(descfn)=="describe_vpcs" and globals.aws_vpc_resp==[]:
      globals.aws_vpc_resp=response  

   #
   elif str(descfn)=="describe_route_tables" and globals.aws_route_table_resp==[]:
      globals.aws_route_table_resp=response  
      #print("@@@@ saved global response "+str(descfn))
   elif str(descfn)=="list_aliases" and globals.aws_kms_alias==[]:
      globals.aws_kms_alias=response  
      #print("@@@@ saved global response "+str(descfn))

   return 


def get_boto3_resp(descfn):
   response=[]
   if str(descfn)=="describe_subnets" and globals.aws_subnet_resp != []:
      response=globals.aws_subnet_resp
   
   elif str(descfn)=="describe_vpcs" and globals.aws_vpc_resp != []:
      response=globals.aws_vpc_resp
   
   elif str(descfn)=="describe_route_tables" and globals.aws_route_table_resp != []:
      response=globals.aws_route_table_resp
      #print("@@@@ retreived global response "+str(descfn))  

   elif str(descfn)=="list_aliases" and globals.aws_kms_alias != []:
      response=globals.aws_kms_alias
      #print("@@@@ retreived global response "+str(descfn))  
   return response