import boto3
import sys
import subprocess
import fixtf
import os
import globals
import glob
#import aws2tf

# global variables initailsed in commomn:



def tfplan(type):
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
                  com="rm -f s3-*"+ i + "s3-*_import.tf aws_s3_*__b-"+ i +".tf main.tf"
                  rout=rc(com)
                  plan2=True
               except:
                  if globals.debug is True:
                     print(mess.strip())
                  plan2=True
         except:
               print("Error - no error message, check plan1.json")
               #continue
               exit()

   print("Plan 1 complete -- resources.out generated")

   if not os.path.isfile("resources.out"):
         print("could not find expected resources.out file after Plan 1 - exiting")
         exit()

   print("split resources.out")
   splitf("resources.out")
   
   for type in globals.types:
      x=glob.glob(type+"__*.out")
      for fil in x:
         tf=fil.split('.')[0]
         print("tf="+tf)
         fixtf.fixtf(type,tf)
   
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





   if plan2:
      
      print("Plan 2 ... ")
      # redo plan
      com="rm -f resources.out tfplan"
      print(com)
      rout=rc(com)
      com="terraform plan -generate-config-out="+ rf + " -out tfplan -json > plan2.json"
      print(com)
      rout=rc(com)
      zerod=False
      with open('plan2.json', 'r') as f:
         for line in f.readlines():
            #print(line)
            if '0 to destroy' in line:
              zerod=True
            if '@level":"error"' in line:
              if globals.debug is True:
                 print("Error" + line)
              print("-->> Plan 2 errors exiting - check plan2.json - or run terraform plan")
              exit()

      if not zerod:
         print("-->> plan will destroy - unexpected, is there existing state ?")
         print("-->> look at plan2.json - or run terraform plan")
         exit()

      print("Plan 2 complete")
   
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
      com="mv *_import.tf imported"
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

   f3.close()



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

#
#  boto3.client("logs")
# aws_logs_log_group id  "logs"  "describe_log_groups"


# if type == "aws_vpc_endpoint": return "ec2","describe_vpc_endpoints","VpcEndpoints","VpcEndpointId","vpc-id"

def getresource(type,id,clfn,descfn,topkey,key,filterid):
    globals.types=globals.types+[type]
    client = boto3.client(clfn)   
    dfn = getattr(client, descfn)
    print("--> In getresource doing "+ type + ' with id ' + str(id))
    if id is None:
      response=dfn() 
    else:   
      if filterid == "logGroupNamePattern":
         print("calling with filter logGroupNamePattern="+id)
         response=dfn(logGroupNamePattern=id)
      elif filterid == "ConfigRuleNames":
         print("calling with filter ConfigRuleNames="+id)
         response=dfn(ConfigRuleNames=[id])
      ## standard call --filter
      else:
         print("calling with filter id="+filterid + " and id=" + id)
         response=dfn(Filters=[{'Name': filterid, 'Values': [id]}])
       
    #print("response="+str(response[botokey]))
    if str(response[topkey]) != "[]":
      fn=type+"_import.tf"
      with open(fn, "w") as f:
            for item in response[topkey]:
                theid=item[key]
                tfid=theid.replace("/","_")
                f.write('import {\n')
                f.write('  to = ' +type + '.' + tfid + '\n')
                f.write('  id = "'+ theid + '"\n')
                f.write('}\n')
                globals.processed=globals.processed+[type+","+theid]
  
    #tfplan(type)

