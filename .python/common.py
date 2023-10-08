import json
import sys
import subprocess
import fixtf
import os
#import aws2tf

def tfplan(type):
   print("tf plan")
   rf=str(type) + "_resources.out"
   com="terraform plan -generate-config-out="+ rf + " -out tfplan -json | jq . > plan1.json"
   print(com)
   rout=rc(com)

   file="plan1.json"
   f2=open(file, "r")
   plan2=False

   while True:
      line = f2.readline()
      if not line:
         break
      #print(line)
      if '@level": "error"' in line:
         #print("Error" + line)
         try:
               mess=f2.readline()
               i=mess.split('(')[2].split(')')[0]
               print("Removing "+i+" files - plan errors see plan1.json")
               com="rm -f s3-*"+ i + "*_import.tf aws_s3_*__b-"+ i +".tf"
               rout=rc(com)
               plan2=True
         except:
               print("Error - no error message")
               continue

   print("Plan 1 complete")
   if plan2:
      
      print("Plan 2 ... ")
      # redo plan
      com="rm -f aws_s3_bucket_resources.out aws_s3*.tf"
      print(com)
      rout=rc(com)
      com="terraform plan -generate-config-out="+ rf + " -out tfplan"
      print(com)
      rout=rc(com)
      el=len(rout.stderr.decode().rstrip())
      if el!=0: 
            print(rout.stderr.decode().rstrip())
            print("--> plan errors exiting  ?")
            exit()
      if "0 to destroy" not in str(rout.stdout.decode().rstrip()):
            print(str(rout.stdout.decode().rstrip()))
            print("--> plan warning destroy - existing state ?")
            exit()
      print("Plan 2 complete")
   
   if os.path.isfile("tfplan"):
         print("calling fixtf "+ type)
         fixtf.fixtf(type)
   else:
         print("could not find expected tfplan file - exiting")
         exit()
         


def wrapup():
   #print("wrap up")
   print("Format")
   com="terraform fmt -no-color"
   rout=rc(com) 
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

def start_state(sf):
   #print("start state")
       #echo $tsf
   sf.write('{\n')
   sf.write('  "version": 4,\n')
   sf.write('  "resources\": [ \n')

def end_state(sf):
   #print("end state")
   sf.write('  ]\n')
   sf.write('}\n')

def res_head(sf,ttft,rname):
   #print("res head")
   sf.write('    {\n')
   sf.write('      "mode": "managed",\n')
   sf.write('      "type": "'+ ttft + '",\n')
   sf.write('      "name": "' + rname + '",\n')
   sf.write('      "provider": "provider[\\"registry.terraform.io/hashicorp/aws\\"]",\n')
   sf.write('      "instances": [ \n')
   sf.write('        {\n')
   sf.write('          "attributes": {\n') 

def res_tail(sf):
   #print("res tail")
   sf.write('          }\n')
   sf.write('        }\n')
   sf.write('      ]\n')
   sf.write('    },\n')


def check_python_version():
  version = sys.version_info
  major = version.major
  minor = version.minor
  if major < 3 or (major == 3 and minor < 7):
    print("This program requires Python 3.7 or later.")
    sys.exit(1)

def is_pool_running(pool):
    """Check if a multiprocessing pool is running."""

    if pool is None:
        return False
    return True


def finish_state(statefile):
   #print("finishing state file")
   with open(statefile, 'r') as fp:
        for count, line in enumerate(fp):
            pass
   #print('Total Lines', count + 1)
   if count <= 5 :
      print("empty state exiting")
      exit()


   el=count-2
   #print('toedit=' + str(el))
   fp.close()

   with open(statefile, 'r') as file:
      data = file.readlines()
   data[el] = '    }\n'

   with open(statefile, 'w') as file:
      file.writelines( data )
      file.close()

   f = open(statefile, 'r')
   data = json.load(f)
   f.close()
   
   #print("skipping refesh etc ...")

   #return

   com="terraform refresh -no-color -lock=false -state " + statefile
   #print(com)
   rout=rc(com)
   #print(rout)

   for i in data['resources']:

      ttft=i['type']
      rname=i['name']
      com="terraform state show -no-color -state " + statefile + " " + ttft + "." + rname + " > " + ttft + "-" + rname + "-1.txt"
      #print("show for " +ttft + " " + rname)
#      print(com)
      rout=rc(com)
#      print(rout)
      # state move

      com="terraform state mv -state " + statefile + " -state-out=terraform.tfstate -lock=true " + ttft + "." + rname + " " + ttft + "." + rname
      #com="terraform state mv -state " + statefile + " -state-out=terraform.tfstate -lock=true " + ttft +  " " + ttft 

      print("move for " +ttft + " " + rname)
#      print(com)
      rout=rc(com)
#      print(rout) 


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
