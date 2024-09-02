import boto3
from botocore.exceptions import ClientError
import sys
import traceback
import subprocess
import os
import re
from io import StringIO
from contextlib import suppress
import shutil
import json
import globals
import glob
import botocore
import fixtf
import inspect
from datetime import datetime
import resources

#####################

from get_aws_resources import aws_acm
from get_aws_resources import aws_amplify
from get_aws_resources import aws_athena
from get_aws_resources import aws_autoscaling
from get_aws_resources import aws_apigateway
from get_aws_resources import aws_apigatewayv2
from get_aws_resources import aws_appmesh
from get_aws_resources import aws_application_autoscaling
from get_aws_resources import aws_appstream
from get_aws_resources import aws_batch
from get_aws_resources import aws_backup
from get_aws_resources import aws_bedrock
from get_aws_resources import aws_bedrock_agent
from get_aws_resources import aws_cleanrooms
from get_aws_resources import aws_cloud9
from get_aws_resources import aws_cloudformation
from get_aws_resources import aws_cloudfront
from get_aws_resources import aws_cloudtrail
from get_aws_resources import aws_codebuild
from get_aws_resources import aws_codecommit
from get_aws_resources import aws_codeartifact
from get_aws_resources import aws_codeguruprofiler
from get_aws_resources import aws_codestar_notifications
from get_aws_resources import aws_cognito_identity
from get_aws_resources import aws_cognito_idp
from get_aws_resources import aws_config
from get_aws_resources import aws_customer_profiles
from get_aws_resources import aws_datazone
from get_aws_resources import aws_dms
from get_aws_resources import aws_docdb
from get_aws_resources import aws_ds
from get_aws_resources import aws_dynamodb
from get_aws_resources import aws_kms
from get_aws_resources import aws_ec2
from get_aws_resources import aws_ecs
from get_aws_resources import aws_efs
from get_aws_resources import aws_ecr_public
from get_aws_resources import aws_ecr
from get_aws_resources import aws_eks
from get_aws_resources import aws_elbv2
from get_aws_resources import aws_emr
from get_aws_resources import aws_events
from get_aws_resources import aws_firehose
from get_aws_resources import aws_glue
from get_aws_resources import aws_guardduty
from get_aws_resources import aws_iam
from get_aws_resources import aws_kendra
from get_aws_resources import aws_kinesis
from get_aws_resources import aws_logs
from get_aws_resources import aws_lakeformation
from get_aws_resources import aws_lambda
from get_aws_resources import aws_neptune
from get_aws_resources import aws_organizations
from get_aws_resources import aws_ram
from get_aws_resources import aws_rds
from get_aws_resources import aws_redshift
from get_aws_resources import aws_redshift_serverless
from get_aws_resources import aws_resource_explorer_2
from get_aws_resources import aws_route53
from get_aws_resources import aws_s3
from get_aws_resources import aws_s3control
from get_aws_resources import aws_sagemaker
from get_aws_resources import aws_schemas
from get_aws_resources import aws_scheduler
from get_aws_resources import aws_securityhub
from get_aws_resources import aws_secretsmanager
from get_aws_resources import aws_servicecatalog
from get_aws_resources import aws_servicediscovery
from get_aws_resources import aws_shield
from get_aws_resources import aws_ses
from get_aws_resources import aws_sns
from get_aws_resources import aws_sqs
from get_aws_resources import aws_ssm
from get_aws_resources import aws_sso_admin
from get_aws_resources import aws_vpc_lattice
from get_aws_resources import aws_wafv2
from get_aws_resources import aws_xray

from fixtf_aws_resources import needid_dict
from fixtf_aws_resources import aws_no_import
from fixtf_aws_resources import aws_not_implemented


def call_resource(type, id):
   #print("---- in call_resources >>>>> "+type+"   "+str(id))
   #if type in globals.all_extypes: 
   #   print("Type:",type," excluded, skipping ...")
   #   return
   
   
   if type in aws_no_import.noimport:
      print("WARNING: Terraform cannot import type: " + type)
      if id is not None:
         with open('not-imported.log', 'a') as f2:
            f2.write(type + " : " + str(id) + "\n")
         globals.rproc[type+"."+id] = True
      return

   if type in aws_not_implemented.notimplemented:
      print("Not supported by aws2tf currently: " + type +
            " please submit github issue to request support")
      return

   elif type == "aws_null":
      with open('stack-null.err', 'a') as f3:
         f3.write("-->> called aws_null for: "+id+"\n")
      return

   with open('processed-resources.log', 'a') as f4:
      f4.write(str(type) + " : " + str(id)+"\n")

    # don't get it if we alreay have it
    # if globals.rproc
   if globals.debug: print("---->>>>> "+type+"   "+str(id))
   if id is not None:
      ti = type+"."+id
      try:
         if globals.rproc[ti]:
            print("Already processed " + ti)
            return
      except:
         pass
   else:
      if type in needid_dict.aws_needid:
         print("WARNING: " + type + " cannot have null id must pass parameter " +
               needid_dict.aws_needid[type]['param'])
         # TODO api only
         return

   rr = False
   sr = False
   clfn, descfn, topkey, key, filterid = resources.resource_data(type, id)
   if key == "NOIMPORT":
      print("WARNING: Terraform cannot import type: " + type)
      return

   if clfn is None:
        print("ERROR: clfn is None with type="+type)
        exit()
# Try specific

   try:
            if globals.debug:
               print("calling specific common.get_"+type+" with type="+type+" id="+str(id)+"   clfn=" +
                    clfn+" descfn="+str(descfn)+" topkey="+topkey + "  key="+key + "  filterid="+filterid)

            if clfn == "vpc-lattice":  getfn = getattr(eval("aws_vpc_lattice"), "get_"+type)
            elif clfn == "redshift-serverless":  getfn = getattr(eval("aws_redshift_serverless"), "get_"+type)
            elif clfn == "s3":  getfn = getattr(eval("aws_s3"), "get_"+type)

            else:
               # print("-1aa- clfn:"+clfn+" type:"+type)
               mclfn = clfn.replace("-", "_")

               # print("-1ab- mclfn:"+mclfn+" type:"+type)
               getfn = getattr(eval("aws_"+mclfn), "get_"+type)
               # print("-1ac- clfn:"+clfn+" type:"+type)

            sr = getfn(type, id, clfn, descfn, topkey, key, filterid)

   except AttributeError as e:
      if globals.debug:
         print("AttributeError: name 'getfn' - no aws_"+clfn+".py file ?")
         print(f"{e=}")
         exc_type, exc_obj, exc_tb = sys.exc_info()
         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
         print(exc_type, fname, exc_tb.tb_lineno)
      pass

   except SyntaxError:
      if globals.debug: print(
          "SyntaxError: name 'getfn' - no aws_"+clfn+".py file ?")
      pass

   except NameError as e:
      if globals.debug:
         print("WARNING: NameError: name 'getfn' - no aws_"+clfn+".py file ?")
         print(f"{e=}")
         exc_type, exc_obj, exc_tb = sys.exc_info()
         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
         print(exc_type, fname, exc_tb.tb_lineno)

      pass

   except Exception as e:
      handle_error(e, str(inspect.currentframe().f_code.co_name),
                   clfn, descfn, topkey, id)

   if not sr:
      try:
         if globals.debug:
               print("calling generic getresource with type="+type+" id="+str(id)+"   clfn="+clfn +
               " descfn="+str(descfn)+" topkey="+topkey + "  key="+key + "  filterid="+filterid)
         rr = getresource(type, id, clfn, descfn, topkey, key, filterid)
      except Exception as e:
         print(f"{e=}")

         exc_type, exc_obj, exc_tb = sys.exc_info()
         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
         print(exc_type, fname, exc_tb.tb_lineno)
         if rr is False:
            print("--->> Could not get resource "+type+" id="+str(id))
            pass


def tfplan1():
   print("Terraform Plan - Dependancies Detection Loop ...")
   rf = "resources.out"
   # com="terraform plan -generate-config-out="+ rf + " -out tfplan -json > plan2.json"

   if not glob.glob("import*.tf"):
      print("No import*.tf files found for this resource, exiting ....")
      exit()

   com = "cp imported/provider.tf provider.tf"
   rout = rc(com)

   com = "mv aws_*.tf imported"
   rout = rc(com)



   com = "terraform plan -generate-config-out=" + \
       rf + " -out tfplan -json > plan1.json"
   print(com)
   rout = rc(com)
      
   file = "plan1.json"
   f2 = open(file, "r")
   plan2 = True

   while True:
      line = f2.readline()
      if not line:
         break
      # print(line)
      if '@level": "error"' in line:
         if globals.debug is True:
            print("Error" + line)
         try:
               mess = f2.readline()
               try:
                  if "VPC Lattice" in mess and "404" in mess:
                     print("ERROR: VPC Lattice 404 error - see plan1.json")
                     i = mess.split('(')[1].split(')')[0].split('/')[-1]
                     if i != "":
                        print("ERROR: Removing "+i +
                              " import files - plan errors see plan1.json [p1]")
                        globals.badlist = globals.badlist+[i]
                        shutil.move("import__*"+i+"*.tf",
                                    "notimported/import__*"+i+"*.tf")

                  elif "Error: Cannot import non-existent remote object" in mess:
                     print(
                         "ERROR: Cannot import non-existent remote object - see plan1.json")
                     i = mess.split('(')[1].split(')')[0].split('/')[-1]
                     if i != "":
                        print("ERROR: Removing "+i +
                              " import files - plan errors see plan1.json [p2]")
                        globals.badlist = globals.badlist+[i]
                        shutil.move("import__*"+i+"*.tf",
                                    "notimported/import__*"+i+"*.tf")

               except:
                  pass

               try:
                  i = mess.split('(')[2].split(')')[0]
                  if i != "":
                     print("ERROR: Removing "+i +
                           " files - plan errors see plan1.json [p3]")
                     globals.badlist = globals.badlist+[i]
                     shutil.move("import__*"+i+"*.tf",
                                 "notimported/import__*"+i+"*.tf")
                     shutil.move("aws_*"+i+"*.tf",
                                 "notimported/aws_*"+i+"*.tf")

               except:
                  if globals.debug is True:
                     print(mess.strip())
                  globals.plan2 = True

         except:
               print("Error - no error message, check plan1.json")
               dt = datetime.now().isoformat(timespec='seconds')
               com = "cp plan1.json plan1.json."+dt
               print(com)
               rout = rc(com)
               # continue
               exit()

   # print("Plan 1 complete -- resources.out generated")

   if not os.path.isfile("resources.out"):
         print("could not find expected resources.out file after Plan 1 - exiting")
         dt = datetime.now().isoformat(timespec='seconds')
         com = "cp plan1.json plan1.json."+dt
         print(com)
         rout = rc(com)

         # exit()
   return


def tfplan2():
   # print("fix tf files.....")
   if not os.path.isfile("resources.out"):
         print("could not find expected resources.out file in tfplan2 - exiting")
         # exit()
         return

   # print("split resources.out")
   splitf("resources.out")  # generated *.out files
   # zap the badlist
   for i in globals.badlist:
      # com="rm -f aws_*"+i+"*.out"+" aws_*"+i+"*.tf"
      print("ERROR: Removing "+i+" files - plan errors see plan1.json [p4]")

      # print(com)
      # rout=rc(com)
      try:
         shutil.move("aws_*"+i+"*.tf", "notimported/aws_*"+i+"*.tf")
         shutil.move("aws_*"+i+"*.out", "notimported/aws_*"+i+"*.out")
      except FileNotFoundError as e:
         print(f"{e=}")
         pass
      # sed to remove references


   # copy all imported/aws_*.tf to here ?
   com = "cp imported/aws_*.tf ."
   rout = rc(com)

   x = glob.glob("aws_*__*.out")
   for fil in x:
         type = fil.split('__')[0]
         tf = fil.split('.')[0]
         fixtf.fixtf(type, tf)

   com = "mv aws_*.out imported"
   rout = rc(com)


   com = "terraform fmt"
   rout = rc(com)


def tfplan3():

   #### move tfproto files
   x=glob.glob("data*.tfproto")
   for fil in x:
      tf=fil.split('.tfproto',1)[0]
      com = "mv "+fil +" "+ tf+".tf"
      print(com)
      rout = rc(com)


   print("\nValidate and Test Plan  ... ")
   if globals.merge:
      com = "cp imported/aws_*.tf ."
      rout = rc(com)
   if not glob.glob("aws_*.tf"):
      print("No aws_*.tf files found for this resource, exiting ....")
      exit()

   rf = "resources.out"
   com = "cp imported/provider.tf provider.tf"
   rout = rc(com)

   com = "terraform validate -no-color"
   rout = rc(com)
   el = len(rout.stderr.decode().rstrip())
   if el != 0:
      errm = rout.stderr.decode().rstrip()
      print(errm)
      com = "terraform validate -no-color -json > validate2.json"
      rout = rc(com)

   if "Success! The configuration is valid" not in str(rout.stdout.decode().rstrip()):
      print(str(rout.stdout.decode().rstrip()))
      print("Validation after fix failed - exiting")
      exit()

   else:
      print("Valid Configuration.")
      if globals.validate:
         print("Validate Only..")
         return
   zeroi=0    

################################################################################
   x = glob.glob("aws_*__*.tf")
   awsf=len(x)
   y = glob.glob("import__*.tf")
   impf=len(y)

   if awsf != impf:
      if globals.workaround=="":
         print("ERROR: "+str(awsf)+ "x aws_*.tf and " + str(impf) +"x import__*.tf file counts do not match")
         #print("\nLikely import error [1] - do the following and report errors in github issue:")
         #print("cd "+globals.path1)
         #print("terraform plan -generate-config-out=resources.out")
         fix_imports()
         #exit()
      else:
         print("INFO: "+str(awsf)+ "x aws_*.tf and " + str(impf) +"x import__*.tf file counts do not match")
         print("INFO: Continuing due to workaround "+globals.workaround)
   else:
      print("PASSED: aws_*.tf and import__*.tf file counts match =",awsf)


################################################################################

   #if globals.merge:
   globals.plan2=True

   if globals.plan2:

      print("Penultimate Terraform Plan ... ")

      # redo plan
      com = "rm -f resources.out tfplan"
      #print(com)
      rout = rc(com)
      
      com = "terraform plan -generate-config-out=" + \
          rf + " -out tfplan -json > plan2.json"
      print(com)
      rout = rc(com)
      zerod = False
      zeroc = False
      zeroa = False
      zeroi = -1
      planList = []
      planDict = {}
      changeList = []
      with open('plan2.json') as f:
         for jsonObj in f:
            planDict = json.loads(jsonObj)
            planList.append(planDict)
      for pe in planList:
         if pe['type'] == "change_summary":  
            zeroi=pe['changes']['import']
            zeroa=pe['changes']['add']
            zeroc=pe['changes']['change']
            zerod=pe['changes']['remove']

      print("Plan:",zeroi, "to import,",zeroa,"to add,",zeroc,"to change,",zerod,"to destroy")

      with open('plan2.json', 'r') as f:
         for line in f.readlines():
            if '@level":"error"' in line:
              if "Error: Conflicting configuration arguments" in line and "aws_security_group_rule." in line:
                 print(
                     "WARNING: Conflicting configuration arguments in aws_security_group_rule")
              else:
                  if globals.debug is True:
                     print("Error" + line)

                  print("-->> Plan 2 errors exiting - check plan2.json - or run terraform plan")
                  exit()

      if zerod != 0:
         print("-->> plan will destroy resources! - unexpected, is there existing state ?")
         print("-->> look at plan2.json - or run terraform plan")
         exit()

      if zeroc != 0:
         # decide if to ignore ot not
         planList = []
         planDict = {}
         changeList = []
         allowedchange = False
         nchanges = 0
         nallowedchanges = 0
         with open('plan2.json') as f:
            for jsonObj in f:
               planDict = json.loads(jsonObj)
               planList.append(planDict)
         for pe in planList:
            if pe['type'] == "planned_change" and pe['change']['action'] == "update":
               nchanges = nchanges+1
               ctype = pe['change']['resource']['resource_type']
               if ctype == "aws_lb_listener" or ctype == "aws_cognito_user_pool_client" \
                  or ctype=="aws_bedrockagent_agent" or ctype=="aws_bedrockagent_agent_action_group":
                  
                  changeList.append(pe['change']['resource']['addr'])
                  print("Planned changes found in Terraform Plan for type: " +
                        str(pe['change']['resource']['resource_type']))
                  allowedchange = True
                  nallowedchanges = nallowedchanges+1
               else:
                  print("Unexpected plan changes found in Terraform Plan for resource: " +
                        str(pe['change']['resource']['addr']))
         if nchanges == nallowedchanges:
            print("\n-->> plan will change " + str(nchanges) +
                  " resources! - these are expected changes only (should be non-consequential)")
            ci = 1

            print(
                "-->> Check the planned changes in these resources listed below by running: terraform plan\n")

            for i in changeList:
               print(str(ci)+": "+str(i))
               ci = ci+1
            print("\n")

            if globals.expected is False:
               print("You can check the changes by running 'terraform plan' in ",globals.path1+"\n")
               print("Then rerun the same ./aws2tf.py command and add the '-a' flag to accept these plan changes and continue to import")
               exit()

            if globals.debug is True:
               print("\n-->> Then if happy with the output changes for the above resources, run this command to complete aws2tf-py tasks:")
               print("terraform apply -no-color tfplan")
               exit()
         else:
            print("-->> plan will change resources! - unexpected")
            print("-->> look at plan2.json - or run terraform plan")
            exit()

      if zeroa !=0:
         print("-->> plan will add resources! - unexpected")
         print("-->> look at plan2.json - or run terraform plan")
         exit()

      print("Plan complete")
      ## if merging get .out files from imported ?

   ### validations checks
   # import__ == aws_*.tf - and import number
   #   
   if not globals.merge:
      if zeroi == awsf:
         print("PASSED: import count = file counts =",str(zeroi))
      else:
         print("INFO: import count "+str(zeroi) +" != file counts "+ str(awsf))
         if globals.workaround=="":
            print("\nLikely import error [2] - do the following and report errors in github issue")
            print("cd "+globals.path1)
            print("terraform plan -generate-config-out=resources.out")
            exit()
         else:
            print("INFO: Continuing due to workaround "+globals.workaround)
         
   if globals.merge:
         print("Merge check")
         if zeroi==0:
            print("Nothing to merge exiting ...")
            exit()
         # get imported
         x = glob.glob("imported/import__*.tf")
         preimpf=len(x)
         toimp=impf-preimpf
         com = "terraform state list | grep ^aws_ | wc -l"
         rout = rc(com)
         stc=int(rout.stdout.decode().rstrip())
         print("Existing import file =",str(preimpf))
         print("Existing state count =",str(stc))
         print("Expected import =",str(toimp))
         if preimpf != stc:
            print("Miss-matched previous imports",str(preimpf),"and state file resources",str(stc) ,"exiting")
            exit() 
         if toimp != zeroi:
            print("Unexpected import number exiting")
            exit() 
         else:
            print("PASSED: importing expected number of resources")    

   if not os.path.isfile("tfplan"):
      print("Plan - could not find expected tfplan file - exiting")
      exit()

   #if globals.merge:
   #   exit()
   #   print("merge - exit after plan2")

def wrapup():

   print("Final Terraform Validation")
   com = "terraform validate -no-color"
   rout = rc(com)
   el = len(rout.stderr.decode().rstrip())
   if el != 0:
      errm = rout.stderr.decode().rstrip()
      print(errm)
   if "Success! The configuration is valid" not in str(rout.stdout.decode().rstrip()):
      print(str(rout.stdout.decode().rstrip()))
      exit()
   else:
      print("PASSED: Valid Configuration.")

   if globals.merge:
      print("Pre apply merge check")
      if not os.path.isfile("plan2.json"):
         print("ERROR: Could not find plan2.json, unexpected on merge - exiting ....")
         exit()
      
   print("Terraform import via apply of tfplan....")
   com = "terraform apply -no-color tfplan"
   rout = rc(com)
   zerod = False
   zeroc = False
   if "Error" in str(rout.stderr.decode().rstrip()):
      print("ERROR: problem in apply ... further checks ....")
      errs=str(rout.stderr.decode().rstrip())
      ## Plan check
      print("\nPost Error Import Plan Check .....")
      com = "terraform plan -no-color"
      rout = rc(com)
      if "No changes. Your infrastructure matches the configuration" not in str(rout.stdout.decode().rstrip()):
         print(errs)
         print("ERROR: unexpected final plan stuff - exiting")
         print(str(rout.stdout.decode().rstrip()))
         print(str(rout.stderr.decode().rstrip()))
         exit()
      else:
         print("PASSED: No changes in plan")
         com = "mv import__*.tf *.out *.json imported"
         rout = rc(com)
         com = "cp aws_*.tf imported"
         rout = rc(com)
         return
   #print(str(rout.stdout.decode().rstrip()))
   print("\nPost Import Plan Check .....")
   com = "terraform plan -no-color"
   rout = rc(com)
   if "No changes. Your infrastructure matches the configuration" not in str(rout.stdout.decode().rstrip()):
      print("ERROR: unexpected final plan failure")
      print(str(rout.stdout.decode().rstrip()))
      print(str(rout.stderr.decode().rstrip()))
      exit()
   else:
      print("PASSED: No changes in plan")
      com = "mv import__*.tf *.out *.json imported"
      rout = rc(com)
      com = "cp aws_*.tf imported"
      rout = rc(com)

######################################################################

def rc(cmd):
    out = subprocess.run(cmd, shell=True, capture_output=True)
    ol = len(out.stdout.decode('utf-8').rstrip())
    el = len(out.stderr.decode().rstrip())
    if el != 0:
         errm = out.stderr.decode().rstrip()
         # print(errm)
         # exit(1)

    # print(out.stdout.decode().rstrip())
    return out


def fix_imports():
   x = glob.glob("aws_*__*.tf")
   awsf=len(x)
   y = glob.glob("import__*.tf")
   impf=len(y)
   print("\nFix Import Intervention")
   print("aws_*.tf files =", str(awsf))
   print("import__*.tf files =", str(impf))
   if impf > awsf:
      for fil2 in y:  # all import files  
         impok=False
         for fil in x: # all aws_ files
            
            tf=fil.split('.tf',1)[0]
            iseg=fil2.replace("import__","").replace(".tf", "")
            if tf == iseg:
                  #print("Match:",iseg,tf)
                  impok=True
                  break
         
         ## out of for loop
         #print("impok =", str(impok))
         if impok is False:
            com = "mv "+fil2+" "+fil2.replace(".tf",".err")
            print(fil2.replace(".tf",".err"))
            rc(com)
           

def ctrl_c_handler(signum, frame):
  print("Ctrl-C pressed.")
  exit()


def check_python_version():
   version = sys.version_info
   major = version.major
   minor = version.minor
   if major < 3 or (major == 3 and minor < 8):
      print("This program requires Python 3.8 or later.")
      sys.exit(1)
# check boto3 version
   if boto3.__version__ < '1.34.93':
      bv = str(boto3.__version__)
      vs = bv.split(".")
      v1 = int(vs[0])*100000+int(vs[1])*1000+int(vs[2])
      if v1 < 134093:
         print("boto3 version:"+bv)
         print("This program requires boto3 1.34.93 or later.")
         print("Try: pip install boto3==1.34.93")
         sys.exit(1)


def aws_tf(region):
   # os.chdir(globals.path1)
   #if not os.path.isfile("aws.tf"):
   if globals.serverless:
      with open("provider.tf", 'w') as f3:
            f3.write('terraform {\n')
            f3.write('  required_version = "> 1.7.4"\n')
            f3.write('  required_providers {\n')
            f3.write('    aws = {\n')
            f3.write('      source  = "hashicorp/aws"\n')
            # f3.write('      version = "5.48.0"\n')
            f3.write('      version = "5.65.0"\n')
            f3.write('    }\n')
            f3.write('  }\n')
            f3.write('}\n')
            f3.write('provider "aws" {\n')
            f3.write('  region                   = "' + region + '"\n')
            f3.write('}\n')
   else:
      with open("provider.tf", 'w') as f3:
            f3.write('terraform {\n')
            f3.write('  required_version = "> 1.7.4"\n')
            f3.write('  required_providers {\n')
            f3.write('    aws = {\n')
            f3.write('      source  = "hashicorp/aws"\n')
            # f3.write('      version = "5.48.0"\n')
            f3.write('      version = "5.65.0"\n')
            f3.write('    }\n')
            f3.write('  }\n')
            f3.write('}\n')
            f3.write('provider "aws" {\n')
            f3.write('  region                   = "' + region + '"\n')
            f3.write('  shared_credentials_files = ["~/.aws/credentials"]\n')
            # f3.write('  profile                  = var.profile\n')
            f3.write('}\n')
   com = "cp provider.tf imported/provider.tf"
   rout = rc(com)
   if not os.path.isfile("data-aws.tf"):   
      with open("data-aws.tf", 'w') as f3:
         f3.write('data "aws_region" "current" {}\n')
         f3.write('data "aws_caller_identity" "current" {}\n')
         f3.write('data "aws_availability_zones" "az" {\n')
         f3.write('state = "available"\n')
         f3.write('}\n')
   if not globals.merge:
      print("terraform init")
      com = "terraform init -no-color -upgrade"
      rout = rc(com)
      print(rout.stdout.decode().rstrip())
   else:
      print("skipping terraform init")


# split resources.out
def splitf_old(file):
   lhs = 0
   rhs = 0
   if os.path.isfile(file):
      print("split file:" + file)
      with open(file, "r") as f:
         Lines = f.readlines()
      for tt1 in Lines:
         # print(tt1)
         if "{" in tt1: lhs = lhs+1
         if "}" in tt1: rhs = rhs+1
         if lhs > 1:
               if lhs == rhs:
                  try:
                     f2.write(tt1+"\n")
                     f2.close()
                     lhs = 0
                     rhs = 0
                     continue
                  except:
                     pass

         if tt1.startswith("resource"):
               # print("resource: " + tt1)
               ttft = tt1.split('"')[1]
               taddr = tt1.split('"')[3]
               # if globals.acc in taddr:
               #   a1=taddr.find(globals.acc)
               #   taddr=taddr[:a1]+taddr[a1+12:]
               #   #print("taddr="+taddr)

               f2 = open(ttft+"__"+taddr+".out", "w")
               f2.write(tt1)

         elif tt1.startswith("#"):
               continue
         elif tt1 == "" or tt1 == "\n":
               continue
         else:
               try:
                  f2.write(tt1)
               except:
                  print("tried to write to closed file: >" + tt1 + "<")
   else:
      print("could not find expected resources.out file")

   # moves resources.out to imported
   f2.close()
   shutil.move(file, "imported/"+file)


#################################

def splitf(input_file):
   # Compile regex patterns for better performance
   resource_pattern = re.compile(r'resource "(\w+)" "(.+?)"')
   comment_pattern = re.compile(r'^\s*#')
   print("split file: " + input_file)
   # Read the entire file content at once
   with open(input_file, 'r') as f:
        content = f.read()
   
    # Use a more efficient splitting method
   resource_blocks = re.split(r'(?=\nresource ")', '\n' + content)

   for block in resource_blocks[1:]:  # Skip the first (empty) block
        match = resource_pattern.search(block)
        if match:
            resource_type = match.group(1)
            resource_name = match.group(2)

            # Create filename
            filename = f"{resource_type}__{resource_name.replace('/', '__')}.out"

            # Use StringIO for efficient string operations
            output = StringIO()

            for line in block.split('\n'):
                if not comment_pattern.match(line):
                    output.write(line + '\n')

            # Write the filtered resource block to a new file
            with open(filename, 'w') as f:
                f.write(output.getvalue().strip() + '\n')

            # print(f"Created file: {filename}")
   shutil.move(input_file,"imported/"+input_file)


################################



# if type == "aws_vpc_endpoint": return "ec2","describe_vpc_endpoints","VpcEndpoints","VpcEndpointId","vpc-id"

#generally pass 3rd param as None - unless overriding
def write_import(type,theid,tfid):
   try:
      ## todo -  if theid starts with a number or is an od (but what if its hexdecimal  ?)

      if tfid is None:
            tfid=theid.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_")
      else:
            tfid=tfid.replace("/", "_").replace(".", "_").replace(":", "_").replace("|", "_").replace("$", "_").replace(",","_").replace("&","_").replace("#","_")
         
         #catch tfid starts with number
      if tfid[:1].isdigit(): tfid="r-"+tfid

      if "!" in theid:
         fn="notimported/import__"+type+"__"+tfid+".tf"
         print("ERROR: Not importing "+type+" "+theid)
         print("ERROR: Invalid character ! in name")
      else:
         fn="import__"+type+"__"+tfid+".tf"

      fn=fn.replace(globals.acc,"012345678912")

      if globals.debug: print(fn)
         #print(fn)
         
         # check if file exists:
         #
      if os.path.isfile(fn):
            if globals.debug: print("File exists: " + fn)
            pkey=type+"."+tfid
            globals.rproc[pkey]=True
            return
         #print("theid=",theid,"  tfid=",tfid)

      output = StringIO()
      output.write('import {\n')
      output.write('  to = ' +type + '.' + tfid + '\n')
      output.write('  id = "'+ theid + '"\n')
      output.write('}\n')

               # Write the filtered resource block to a new file
      with open(fn, 'w') as f:
         f.write(output.getvalue().strip() + '\n')

      pkey=type+"."+tfid
      globals.rproc[pkey]=True
      pkey=type+"."+theid
      globals.rproc[pkey]=True


   except Exception as e:  
      handle_error2(e,str(inspect.currentframe().f_code.co_name),id)    

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
      response=call_boto3(type,clfn,descfn,topkey,key,id)   
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
                        if globals.debug:  print("Skipping service role " + str(item[key])) 
                        continue
                  except:
                     pass

                  try:
                     theid=item[key]
                  except TypeError:
                     print("ERROR: getresource TypeError: "+str(response)+" key="+key+" type="+type,descfn)
                     with open('boto3-error.err', 'a') as f:
                        f.write("ERROR: getresource TypeError: type="+type+" key="+key+" descfn="+descfn+"\n"+str(response)+"\n")
                     continue
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
                  if globals.debug: 
                     print("-gr31-"+"filterid="+str(filterid)+" id="+str(id)+"  key="+key)
                     print(str(item))
                  if "." not in filterid:
                     #print("***item=" + str(item))
                     try:
                        if id == str(item[filterid]):
                           #if globals.debug: print("-gr31 item-"+str(item))
                           theid=item[key]
                           special_deps(type,theid)
                           write_import(type,theid,None)
                        elif filterid != key:
                           if globals.debug:
                              print("id="+id+" filterid="+filterid)
                              print("item="+str(item))
                           theid=item[filterid]
                           write_import(type,theid,None)
                     except Exception as e:
                        print(f"{e=}")
                        if globals.mopup.get(type) is not None:
                           if id.startswith(globals.mopup[type]):
                              write_import(type,id,None)
                              return True

                        else:
                           with open('missed-getresource.log', 'a') as f4:
                              f4.write("Could have done write_import "+type+" id="+id+" filterid="+filterid+"/n")
                           return False
                  else:
                     ### There IS a dot in the filterid so we need to dig deeper
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
            print("No "+type+" "+id+" found - empty response") 
            pkey=type+"."+id  
            globals.rproc[pkey]=True      
         else:
            print("No "+type+" found - empty response")
         return True
   
   except Exception as e:
      handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

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



def add_known_dependancy(type,id):
    # check if we alredy have it
    pkey=type+"."+id
    if pkey not in globals.rdep:
        print("add_known_dependancy: " + pkey)
        globals.rdep[pkey]=False
    return

def add_dependancy(type,id):
    # check if we alredy have it
   if id is None: 
      print("WARNING: add_dependancy: id is None")
      return
   try:
   #   if type=="aws_kms_alias" and id=="k-817bb810-7154-4d9b-b582-7dbb62e77876":
   #      raise Exception("aws_kms_alias")
      if type=="aws_glue_catalog_database":
         if ":" not in id: id=globals.acc+":"+id
      pkey=type+"."+id
      if pkey not in globals.rproc:
         print("add_dependancy: " + pkey)
         globals.rproc[pkey]=False
   except Exception as e:
      handle_error(e, str(inspect.currentframe().f_code.co_name), type, id)
   return


## TODO - always get all / paginate all - save in globals - filter on id in get_aws_ ??
## but in smaller use cases may be better to make filtered boto3 calls ?
## this call doesn't take the key

## can't pass filterid - not possible to use for page in paginator.paginate(filterid=id)
# TODO ? won't accept filter id as string param1 in paginate(param1,id) ??
# hench working around using descfn - not ideal

def call_boto3(type,clfn,descfn,topkey,key,id): 
   try:
      if globals.debug: 
         print("call_boto3 clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
      if globals.debug: print("pre-response")
      # get any pre-saved response
      response=get_boto3_resp(descfn)  # sets response to [] if nothing saved
      
      if response == []:
         client = boto3.client(clfn) 
         if globals.debug: print("client")
         try:
            paginator = client.get_paginator(descfn)
            if globals.debug: print("paginator")
    
            if "apigatewayv2" in str(type):
               for page in paginator.paginate(ApiId=id): 
                  response.extend(page[topkey]) 
               pkey=type+"."+id
               globals.rproc[pkey]=True
               #if response != []:
               #   print(str(response))
               

            elif descfn == "describe_launch_templates":
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
               #print("call_boto3 clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
               if id is not None:
                  if "i-" in id:
                     for page in paginator.paginate(InstanceIds=[id]): response.extend(page[topkey][0]['Instances'])
               else:
                  for page in paginator.paginate(): 
                     if len(page[topkey])==0:
                        continue
                     response.extend(page[topkey][0]['Instances'])
                  sav_boto3_rep(descfn,response)
               
               #print(str(response))

            elif descfn == "describe_pod_identity_association" or descfn == "list_fargate_profiles" or descfn == "list_nodegroups" or descfn == "list_identity_provider_configs" or descfn == "list_addons":
               #print("--1a "+str(id))
               for page in paginator.paginate(clusterName=id): response.extend(page[topkey])
            
            
            elif descfn == "list_access_keys" and id is not None:
               for page in paginator.paginate(UserName=id): response.extend(page[topkey])
                    
            
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
               if globals.debug: print("--1b")
               # main get all call - usually a list- describe- or get- 
               for page in paginator.paginate(): 
                  response.extend(page[topkey])
               sav_boto3_rep(descfn,response)

               if id is not None:
                  fresp=response
                  if globals.debug:print("--2")
                  response=[]
                  if globals.debug: print(str(fresp))
                  # get by id - useually a describe- or get-
                  for i in fresp:
                     if globals.debug: 
                        try:
                           print(i[key],id)
                        except TypeError:
                           print(i,id)
                     try:
                        if id in i[key]:
                           response=[i]
                           break
                     except TypeError:
                        if id in i:
                           response=[i]
                           break
                  #print("--3")
                  # get by filter - useually a list- describe- or get-   
               # save a full paginate as we don't want to do it many times
               

         except botocore.exceptions.ParamValidationError as e:

            print("ParamValidationError 1 in common.call_boto3: type="+type+" clfn="+clfn)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"{e=} [pv1] ", fname, exc_tb.tb_lineno)
            with open('boto3-error.err', 'a') as f:
                     f.write("type="+type+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id)+"\n")
                     f.write(f"{e=} [pv1] \n")
                     f.write(f"{fname=} {exc_tb.tb_lineno=} [e2] \n")
                     f.write("-----------------------------------------------------------------------------\n")
            return []
            

         except botocore.exceptions.OperationNotPageableError as err:
               if globals.debug:
                  print(f"{err=}")
                  print("calling non paginated fn "+str(descfn)+" id="+str(id))
               try:
                  getfn = getattr(client, descfn)                     
                  response1 = getfn()
                  response1=response1[topkey]
                  if globals.debug: print("Non-pag response1="+str(response1))
                  if id is None:
                     if globals.debug: print("id None")
                     response=response1
                     if globals.debug: print("Non-pag response no ID ="+str(response))
                  else: #try a match
                     for j in response1:
                        if id==j[key]:
                           response=[j]
                           if globals.debug: print("Non-pag response with ID ="+str(response))
                           

               except botocore.exceptions.ParamValidationError as e:

                  print("ParamValidationError 2 in common.call_boto3: type="+type+" clfn="+clfn)
                  exc_type, exc_obj, exc_tb = sys.exc_info()
                  fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                  print(f"{e=} [pv2] ", fname, exc_tb.tb_lineno)    
                                    
                  with open('boto3-error.err', 'a') as f:
                     f.write("type="+type+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id)+"\n")
                     f.write(f"{e=} [pv2] \n")
                     f.write(f"{fname=} {exc_tb.tb_lineno=} [e2] \n")
                     f.write("-----------------------------------------------------------------------------\n")
                  return []
               

         except Exception as e:
            handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

         #print("--2a")  
         rl=len(response)
         #print("--2b" + str(rl)) 
         if rl==0:
            if globals.debug: print("** zero response length for "+ descfn + " in call_boto3 returning .. []")
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
      handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

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


def handle_error(e,frame,clfn,descfn,topkey,id):
   
   exc_type, exc_obj, exc_tb = sys.exc_info()
   exn=str(exc_type.__name__)
   fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
   #print("exn="+exn)
   if exn == "EndpointConnectionError":
      print("No endpoint in this region for "+fname+" - returning")
      return
   elif exn=="ClientError":
      #print("ClientError exception for "+fname+" - returning")
      if "does not exist" in str(e):
         print(id+" does not exist" )
         return
      print("Exception message :"+str(e))
      return
   elif exn=="ForbiddenException":
      print("Call Forbidden exception for "+fname+" - returning")
      return
   elif exn == "ParamValidationError" or exn=="ValidationException" or exn=="InvalidRequestException" or exn =="InvalidParameterValueException" or exn=="InvalidParameterException":
      print(str(exc_obj)+" for "+frame+" id="+str(id)+" - returning")
      return
   elif exn == "BadRequestException" and clfn=="guardduty":
      print(str(exc_obj)+" for "+frame+" id="+str(id)+" - returning")
      return  
   
   elif exn=="AccessDeniedException":
      pkey=frame.split("get_")[1]
      print("AccessDeniedException exception for "+fname+" - returning")
      return


   elif "NotFoundException" in exn:
      if frame.startswith("get_"):
         print("NOT FOUND: "+frame.split("get_")[1]+" "+str(id)+" check if it exists and what references it - returning")
         pkey=frame.split("get_")[1]+"."+str(id)
         if "aws_glue_catalog_database" in pkey:
            pkey=frame.split("get_")[1]+"."+globals.acc+":"+id
         globals.rproc[pkey]=True
      else:
         print("NOT FOUND: "+frame+" "+id+" check if it exists - returning")
      return    

   elif exn=="ResourceNotFoundException" or exn=="EntityNotFoundException" or exn=="NoSuchEntityException" or exn=="NotFoundException" or exn=="LoadBalancerNotFoundException" or exn=="NamespaceNotFound" or exn=="NoSuchHostedZone":
      if frame.startswith("get_"):
         print("RESOURCE NOT FOUND: "+frame.split("get_")[1]+" "+str(id)+" check if it exists and what references it - returning")
         pkey=frame.split("get_")[1]+"."+str(id)
         globals.rproc[pkey]=True
      else:
         print("RESOURCE NOT FOUND: "+frame+" "+str(id)+" check if it exists - returning")
      return    
   
   elif exn == "KeyError":
      if "kms" in str(exc_obj):
         print("KeyError cannot find key for " +fname+" id="+str(id)+" - returning")
         return
      
      if clfn=="sqs":
         print("KeyError cannot find queue url for " +fname+" id="+str(id)+" - returning")
         return
      
   elif exn == "InvalidDocument":
      if clfn=="ssm":
         print("KeyError cannot find ssm document for " +fname+" id="+str(id)+" - returning")
         return

   elif exn == "AWSOrganizationsNotInUseException" or exn =="OrganizationAccessDeniedException":
      print("NO ORG: "+frame+" this account doesn't appear to be in an AWS Organisation (or you don't have org permissions) - returning")
      return

   elif "NoSuch" in exn and clfn=="cloudfront":
      print(str(exc_obj)+" for "+frame+" id="+str(id)+" - returning")
      return



   print("\nERROR: in "+frame+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
   try:   
      print(f"{e=} [e1]")
      print(fname, exc_tb.tb_lineno)
   except:
      print("except err")
      pass
   with open('boto3-error.err', 'a') as f:
      f.write("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id)+"\n")
      f.write(f"{e=} [e1] \n")
      f.write(f"{fname=} {exc_tb.tb_lineno=} [e1] \n")
      f.write("-----------------------------------------------------------------------------\n")

   exit()

def handle_error2(e,frame,id):
   print("\nERROR: in "+frame)
   print("id="+str(id))
   exc_type, exc_obj, exc_tb = sys.exc_info()
   fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
   exn=str(exc_type.__name__)
   if exn == "EndpointConnectionError":
      print("No endpoint in this region - returning")
      return
   print(f"{e=} [e2] ", fname, exc_tb.tb_lineno)
   with open('boto3-error.err', 'a') as f:
      f.write("id="+str(id)+"\n")
      f.write(f"{e=} [e2] ")
      f.write(f"{fname=} {exc_tb.tb_lineno=} [e2] \n")
      f.write("-----------------------------------------------------------------------------\n")
   exit()



def create_bucket_if_not_exists(bucket_name):
    s3_client = boto3.client('s3')
    
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        print(f"Bucket {bucket_name} already exists.")
    except ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            print(f"Bucket {bucket_name} does not exist. Creating now...")
            try:
               s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': globals.region})
               print(f"Bucket {bucket_name} created successfully.")
            except ClientError as create_error:
               print(f"Error creating bucket {bucket_name}: {create_error}")
               return False
        else:
            print(f"Error checking bucket {bucket_name}: {e}")
            return False
    
    return True



def upload_directory_to_s3():
   print("Uploading to S3...")
   s3_client = boto3.client('s3')
   local_directory="/tmp/aws2tf/generated/tf-"+globals.acc+"-"+globals.region
   bucket_name="aws2tf-"+globals.acc+"-"+globals.region
   s3_prefix=''
   print("Calling create_bucket_if_not_exists for",bucket_name)
   bret=create_bucket_if_not_exists(bucket_name)
   if bret:
      print("Upload files to s3",bucket_name)
      for root, dirs, files in os.walk(local_directory):
         if '.terraform' in dirs:  dirs.remove('.terraform')
         if 'tfplan' in files: files.remove('tfplan')
         if '.terraform.lock.hcl' in files: files.remove('.terraform.lock.hcl')
         for filename in files:
               local_path = os.path.join(root, filename)
               
               # Calculate relative path
               relative_path = os.path.relpath(local_path, local_directory)
               s3_path = os.path.join(s3_prefix, relative_path).replace("\\", "/")
               
               try:
                  #print(f"Uploading {local_path} to {bucket_name}/{s3_path}")
                  s3_client.upload_file(local_path, bucket_name, s3_path)
               except ClientError as e:
                  print(f"Error uploading {local_path}: {e}")
                  return False
      print("Upload to S3 complete.")
   else:
      print("Upload to S3 failed - False return from create_bucket_if_not_exists for", bucket_name)
      return False

def empty_and_delete_bucket():
    bucket_name="aws2tf-"+globals.acc+"-"+globals.region
    s3 = boto3.resource('s3')
    s3_client = boto3.client('s3')
    bucket = s3.Bucket(bucket_name)
    print("Emptying and deleting bucket...",bucket_name)
    # Check if the bucket exists
    try:
        s3_client.head_bucket(Bucket=bucket_name)
    except ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            print(f"Bucket {bucket_name} does not exist. Nothing to delete.")
            return
        else:
            print(f"Error checking bucket {bucket_name}: {e}")
            return

    # Empty the bucket
    try:
        bucket.objects.all().delete()
        print(f"Bucket {bucket_name} emptied successfully.")
    except ClientError as e:
        print(f"Error emptying bucket {bucket_name}: {e}")
        return

    # Delete the bucket
    try:
        bucket.delete()
        print(f"Bucket {bucket_name} deleted successfully.")
    except ClientError as e:
        print(f"Error deleting bucket {bucket_name}: {e}")
        return

    print(f"Bucket {bucket_name} has been emptied and deleted.")


def download_from_s3():
    print("Restore S3")
    s3_client = boto3.client('s3')
    local_directory="/tmp/aws2tf/generated/tf-"+globals.acc+"-"+globals.region
    bucket_name="aws2tf-"+globals.acc+"-"+globals.region
    s3_prefix=''
    # Check if the bucket exists
    try:
        s3_client.head_bucket(Bucket=bucket_name)
    except ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            print(f"Bucket {bucket_name} does not exist. Cannot download.")
            return
        else:
            print(f"Error checking bucket {bucket_name}: {e}")
            return

    # Create the local directory if it doesn't exist
    os.makedirs(local_directory, exist_ok=True)

    # List objects in the bucket with the specified prefix
    paginator = s3_client.get_paginator('list_objects_v2')
    for page in paginator.paginate(Bucket=bucket_name, Prefix=s3_prefix):
        if 'Contents' not in page:
            continue

        for obj in page['Contents']:
            # Skip the .terraform directory
            if '.terraform' in obj['Key']:
                continue

            # Get the relative path of the file
            relative_path = os.path.relpath(obj['Key'], s3_prefix)
            local_file_path = os.path.join(local_directory, relative_path)

            # Create the directory structure if it doesn't exist
            os.makedirs(os.path.dirname(local_file_path), exist_ok=True)

            # Download the file
            try:
                #print(f"Downloading {obj['Key']} to {local_file_path}")
                s3_client.download_file(bucket_name, obj['Key'], local_file_path)
            except ClientError as e:
                print(f"Error downloading {obj['Key']}: {e}")

    print(f"Download from {bucket_name}/{s3_prefix} to {local_directory} completed.")

def trivy_check():
    # Get current directory and extract the last two parts
    mydir = os.getcwd()
    mydir = '/'.join(mydir.split('/')[-2:])

    # Check if jq is installed
    if shutil.which('jq') is None:
        print("jq is not installed. skipping security report")
        return

    # Check if trivy is installed
    if shutil.which('trivy') is None:
        print("trivy is not installed. skipping security report")
        return

    # Get trivy version
    try:
        trivy_version = subprocess.check_output(['trivy', 'version'], universal_newlines=True)
        ver = int(''.join(filter(str.isdigit, trivy_version.split('\n')[0].split(':')[1].strip())))
    except subprocess.CalledProcessError:
        print("Error getting trivy version")
        return

    if ver < 480:
        print("Please upgrade trivy to version v0.48.0 or higher")
        return

    print("Generating trivy security report ....")
    
    with open('security-report.txt', 'w') as report:
        report.write("trivy security report\n")
        
        for severity in ['CRITICAL', 'HIGH']:
            report.write(f"{severity}:\n")
            try:
                output = subprocess.check_output(['trivy', 'fs', '--scanners', 'misconfig', '.', '-s', severity, '--format', 'json', '-q'], universal_newlines=True)
                results = json.loads(output)
                for result in results.get('Results', []):
                    misconfigurations = result.get('Misconfigurations', [])
                    if misconfigurations:
                        for misconfig in misconfigurations:
                            resource = misconfig.get('CauseMetadata', {}).get('Resource', '')
                            description = misconfig.get('Description', '')
                            references = misconfig.get('References', [])
                            report.write(json.dumps([resource, description, references]) + '\n')
            except subprocess.CalledProcessError:
                print(f"Error running trivy for {severity} severity")

    print(f"Trivy security report: {mydir}/security-report.txt")
