import boto3
import sys
import subprocess
import os
import globals
import glob
import botocore
import fixtf
from datetime import datetime
import resources
from get_aws_resources import aws_athena
from get_aws_resources import aws_application_autoscaling
from get_aws_resources import aws_kms
from get_aws_resources import aws_ec2
from get_aws_resources import aws_ecs
from get_aws_resources import aws_eks
from get_aws_resources import aws_elbv2
from get_aws_resources import aws_iam
from get_aws_resources import aws_vpc_lattice
from get_aws_resources import aws_logs
from get_aws_resources import aws_config
from get_aws_resources import aws_lambda
from get_aws_resources import aws_redshift
from get_aws_resources import aws_secretsmanager
from get_aws_resources import aws_kinesis
from get_aws_resources import aws_glue
from get_aws_resources import aws_rds
from get_aws_resources import aws_apigateway
from fixtf_aws_resources import needid_dict


def call_resource(type, id):
    
   if type=="aws_null":
      with open('stack-null.log', 'a') as f3:
         f3.write("-->> called aws_null for: "+id+"\n")
      return
   

   with open('processed-resources.log', 'a') as f4:
      f4.write(str(type)+ " : " +str(id)+"\n")
      
    ## don't get it if we alreay have it
    # if globals.rproc
   if globals.debug: print("---->>>>> "+type+"   "+str(id))
   if id is not None:
      ti=type+"."+id
      try:
         if globals.rproc[ti]: 
            print("Already processed " + ti)
            return
      except:
         pass
   else:
      if type in needid_dict.aws_needid:
         print("WARNING: " +  type + " cannot have null id must pass parameter "+needid_dict.aws_needid[type]['param'])
         exit(0)

   rr=False
   sr=False
   clfn, descfn, topkey, key, filterid = resources.resource_data(type, id)
   if key == "NOIMPORT":
      print("WARNING: Terraform cannot import type: " + type)
      return

   
   
   if clfn is None:
        print("ERROR: clfn is None with type="+type)
        exit()
## Try specific    
    
   try:
            if globals.debug:
               print("calling specific common.get_"+type+" with type="+type+" id="+str(id)+"   clfn=" +
                    clfn+" descfn="+str(descfn)+" topkey="+topkey + "  key="+key + "  filterid="+filterid)
            
            if clfn=="vpc-lattice":  getfn = getattr(eval("aws_vpc_lattice"), "get_"+type) 
            elif clfn=="redshift-serverless":  getfn = getattr(eval("aws_redshift"), "get_"+type) 
               #aws_redshift.get_aws_redshiftserverless_namespace(type, id, clfn, descfn, topkey, key, filterid)

            else:   
               #print("-1aa- clfn:"+clfn+" type:"+type)
               mclfn=clfn.replace("-","_")
               getfn = getattr(eval("aws_"+mclfn), "get_"+type) 
               #print("-1ab- clfn:"+clfn+" type:"+type)

            sr=getfn(type, id, clfn, descfn, topkey, key, filterid)

   except AttributeError as e:
      if globals.debug: 
         print("AttributeError: name 'getfn' - no aws_"+clfn+".py file ?")
         print(f"{e=}")
         exc_type, exc_obj, exc_tb = sys.exc_info()
         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
         print(exc_type, fname, exc_tb.tb_lineno)
      pass

   except SyntaxError:
      if globals.debug: print("SyntaxError: name 'getfn' - no aws_"+clfn+".py file ?")
      pass

   except NameError:
      if globals.debug: print("WARNING: NameError: name 'getfn' - no aws_"+clfn+".py file ?")
      pass

   except Exception as e:      
                # By this way we can know about the type of error occurring
                print(f"{e=}")
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)   
                exit() 
    
   
   if not sr:
      try:
         if globals.debug:
               print("calling generic getresource with type="+type+" id="+str(id)+"   clfn="+clfn +
               " descfn="+str(descfn)+" topkey="+topkey + "  key="+key + "  filterid="+filterid)
         rr=getresource(type, id, clfn, descfn, topkey, key, filterid)
      except Exception as e:
         print(f"{e=}")
                  
         exc_type, exc_obj, exc_tb = sys.exc_info()
         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
         print(exc_type, fname, exc_tb.tb_lineno)  
         if rr is False:
            print("--->> Could not get resource "+type+" id="+id)
            pass
   

def tfplan1():
   print("Terraform Plan Loop ... ")
   rf="resources.out"
   #com="terraform plan -generate-config-out="+ rf + " -out tfplan -json > plan2.json"


   if not glob.glob("import*.tf"):
      print("No import*.tf files found for this resource, exiting ....")
      exit()

   com="rm -f "+rf
   rout=rc(com)

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
                     print("ERROR: Removing "+i+" import files - plan errors see plan1.json")
                     globals.badlist=globals.badlist+[i]
                     com="rm -f import__*"+i+"*.tf"
                     print(com)
                     rout=rc(com)
                  elif "Error: Cannot import non-existent remote object" in mess:
                     print("ERROR: Cannot import non-existent remote object - see plan1.json")
                     i=mess.split('(')[1].split(')')[0].split('/')[-1]
                     print("ERROR: Removing "+i+" import files - plan errors see plan1.json")
                     globals.badlist=globals.badlist+[i]
                     com="mv import__*"+i+"*.tf import__*"+i+"*.tf.error"
                     print(com)
                     rout=rc(com)
                     exit()

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
               dt=datetime.now().isoformat(timespec='seconds') 
               com="cp plan1.json plan1.json."+dt
               print(com)
               rout=rc(com)
               #continue
               exit()

   #print("Plan 1 complete -- resources.out generated")

   if not os.path.isfile("resources.out"):
         print("could not find expected resources.out file after Plan 1 - exiting")
         dt=datetime.now().isoformat(timespec='seconds') 
         com="cp plan1.json plan1.json."+dt
         print(com)
         rout=rc(com)
         exit()  
   return

def tfplan2():
   #print("fix tf files.....") 
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
         fixtf.fixtf(type,tf)
   com="terraform fmt"
   rout=rc(com)


def tfplan3():
   print("Validate and Test Plan  ... ")
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
      if globals.validate: return


   if globals.plan2:
      
      print("Penultimate Terraform Plan ... ")
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
         print("-->> plan will change resources! - unexpected")
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
   print("Final Terraform Validation")
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
   
   print("Terraform Import")
   #print(str(rout.stdout.decode().rstrip()))
   # do the import via apply
   print("terraform import via apply of tfplan....")
   com="terraform apply -no-color tfplan"
   rout=rc(com)
   zerod=False
   zeroc=False
   print(str(rout.stdout.decode().rstrip()))
   print("Final Plan Check .....")
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
# check boto3 version 
   if boto3.__version__ < '1.34.64':
      print("This program requires boto3 1.34.64 or later.")
      print("Try: pip install boto3==1.34.64")
      sys.exit(1)


def aws_tf(region):
   if not os.path.isfile("aws.tf"):
      with open("aws.tf", 'w') as f3: 
         f3.write('terraform {\n')
         f3.write('  required_version = "> 1.5.4"\n')
         f3.write('  required_providers {\n')
         f3.write('    aws = {\n')
         f3.write('      source  = "hashicorp/aws"\n')
         f3.write('      version = "5.41.0"\n')
         f3.write('    }\n')
         f3.write('  }\n')
         f3.write('}\n')
         f3.write('provider "aws" {\n')
         f3.write('  region                   = "' + region +'"\n')
         f3.write('  shared_credentials_files = ["~/.aws/credentials"]\n')
         #f3.write('  profile                  = var.profile\n')
         f3.write('}\n')
      with open("data-aws.tf", 'w') as f3:
         f3.write('data "aws_region" "current" {}\n')
         f3.write('data "aws_caller_identity" "current" {}\n')
         f3.write('data "aws_availability_zones" "az" {\n')
         f3.write('state = "available"\n')
         f3.write('}\n')
   if not os.path.isdir(".terraform/providers/registry.terraform.io/hashicorp/aws"): 
      com = "terraform init"
      rout = rc(com) 
      print(rout.stdout.decode().rstrip())
   else:
      print("skipping terraform init")
        
                

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
   try:
      if tfid is None:
         tfid=theid.replace("/","__").replace(".","__").replace(":","__")
      fn="import__"+type+"__"+tfid+".tf"
      #if globals.acc in fn:
      #   fn=fn.replace(globals.acc, "__")
      if globals.debug: print(fn)
      #print(fn)
      
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

   except Exception as e:      
                # By this way we can know about the type of error occurring
                print(f"{e=}")
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)   
                exit()

   return

#########################################################################################################################

def getresource(type,id,clfn,descfn,topkey,key,filterid):
   #for j in globals.specials:
   #   if type == j: 
   #      print(type + " in specials list returning ..")
   #      return False
   if globals.debug: print("-1-> In getresource doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

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
      response=call_boto3(type,clfn,descfn,topkey,id)   
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
                  special_deps(type,theid)
               
               
               #
               # id has something
               #
               else:  
                  #if globals.debug: print("-gr31-"+"filterid="+str(filterid)+" id="+str(id))
                  if "." not in filterid:
                     #print("***item=" + str(item))
                     try:
                        if id == str(item[filterid]):
                           #if globals.debug: print("-gr31 item-"+str(item))
                           theid=item[key]
                           special_deps(type,theid)
                           write_import(type,theid,None)
                     except:
                        if globals.mopup.get(type) is not None:
                           if id.startswith(globals.mopup[type]):
                              write_import(type,id,None)
                              return True

                        else:
                           with open('missed-getresource.log', 'a') as f4:
                              f4.write("Could have done write_import "+type+" id="+id+" filterid="+filterid+"/n")
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
   if ttft == "aws_security_group": 
      add_known_dependancy("aws_security_group_rule",taddr) 
      add_dependancy("aws_security_group_rule",taddr) 
   if ttft == "aws_subnet": 
      add_known_dependancy("aws_route_table_association",taddr) 
      add_dependancy("aws_route_table_association",taddr)  
   elif ttft == "aws_vpc": 
      add_known_dependancy("aws_route_table_association",taddr)  
      add_known_dependancy("aws_subnet",taddr)  
      add_dependancy("aws_route_table_association",taddr)
      add_dependancy("aws_vpc_ipv4_cidr_block_association",taddr)

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

def add_dependancy(type,id):
    # check if we alredy have it
    pkey=type+"."+id
    if pkey not in globals.rproc:
        print("add_dependancy: " + pkey)
        globals.rproc[pkey]=False
    return


## TODO - always get all / paginate all - save in globals - filter on id in get_aws_ ??
## but in smaller use cases may be better to make filtered boto3 calls ?
## this call doesn't take the key

## can't pass filterid - not possible to use for page in paginator.paginate(filterid=id)
# TODO ? won't accept filter id as string param1 in paginate(param1,id) ??
# hench working around using descfn - not ideal

def call_boto3(type,clfn,descfn,topkey,id): 
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
               #print(">> id="+str(id))
               if id is not None:
                  if id.startswith("lt-"):
                     #print("--->>> id="+str(id))
                     for page in paginator.paginate(LaunchTemplateIds=[id]): response.extend(page[topkey])
                  else:
                     #print("-->> id="+str(id))
                     for page in paginator.paginate(LaunchTemplateNames=[id]): response.extend(page[topkey])
               else:
                  for page in paginator.paginate(): response.extend(page[topkey])

            elif descfn == "describe_instances":
               print("call_boto3 clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
               if id is not None:
                  if "i-" in id:
                     for page in paginator.paginate(InstanceIds=[id]): response.extend(page[topkey][0]['Instances'])
               else:
                  for page in paginator.paginate(): response.extend(page[topkey][0]['Instances'])
                  sav_boto3_rep(descfn,response)
               
               #print(str(response))

            elif descfn == "list_fargate_profiles" or descfn == "list_nodegroups" or descfn == "list_identity_provider_configs" or descfn == "list_addons":
               #print("--1a "+str(id))
               for page in paginator.paginate(clusterName=id): response.extend(page[topkey])
            
            elif clfn=="kms" and descfn=="list_aliases" and id is not None:
               if id.startswith("k-"): id=id[2:]
               #print("-- call boto3 --"+str(id))
               for page in paginator.paginate(KeyId=id): response.extend(page[topkey])
               return response
            
            elif clfn=="lambda" and descfn=="list_aliases" and id is not None:
               for page in paginator.paginate(FunctionName=id): response.extend(page[topkey])
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

         except botocore.exceptions.ParamValidationError as err:
            print(f"{err=}"+","+type+","+clfn)
            print("ParamValidationError 1 in common.call_boto3: type="+type+" clfn="+clfn)
            return []
            

         except botocore.exceptions.OperationNotPageableError as err:
               print(f"{err=}")
               #print("calling non paginated fn "+str(descfn))
               try:
                  getfn = getattr(client, descfn)
                  response1 = getfn()
                  response=response1[topkey]
               except botocore.exceptions.ParamValidationError as err:
                  print(f"{err=}"+","+type+","+clfn)
                  #print("ParamValidationError 2 in common.call_boto3: type="+type+" clfn="+clfn)
                  return []
               

         except Exception as e:
            print(f"{e=}")
            print("-1->unexpected error in common.call_boto3")
            print("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            with open('boto3-error.plog', 'a') as f:
               f.write("type="+type+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id)+"\n")
               f.write(f"{e=}\n")
               f.write("-----------------------------------------------------------------------------\n")
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
         #print("Global response ")
         return response
      
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
   if str(descfn)=="describe_subnets" and globals.aws_subnet_resp==[]: globals.aws_subnet_resp=response  
   elif str(descfn)=="describe_vpcs" and globals.aws_vpc_resp==[]: globals.aws_vpc_resp=response  
   elif str(descfn)=="describe_route_tables" and globals.aws_route_table_resp==[]: globals.aws_route_table_resp=response  
   elif str(descfn)=="list_aliases" and globals.aws_kms_alias_resp==[]: globals.aws_kms_alias_resp=response  
   elif str(descfn)=="list_roles" and globals.aws_iam_role_resp==[]: globals.aws_iam_role_resp=response  
   elif str(descfn)=="describe_instances" and globals.aws_instance_resp==[]: globals.aws_instance_resp=response  
   return 

def get_boto3_resp(descfn):
   response=[]
   if str(descfn)=="describe_subnets" and globals.aws_subnet_resp != []: response=globals.aws_subnet_resp
   elif str(descfn)=="describe_vpcs" and globals.aws_vpc_resp != []: response=globals.aws_vpc_resp
   elif str(descfn)=="describe_route_tables" and globals.aws_route_table_resp != []: response=globals.aws_route_table_resp 
   elif str(descfn)=="list_aliases" and globals.aws_kms_alias_resp != []: response=globals.aws_kms_alias_resp 
   elif str(descfn)=="list_roles" and globals.aws_iam_role_resp != []: response=globals.aws_iam_role_resp
   elif str(descfn)=="describe_instances" and globals.aws_instance_resp != []: response=globals.aws_instance_resp
   return response

