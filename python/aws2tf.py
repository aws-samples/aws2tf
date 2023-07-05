import boto3
import json
import multiprocessing
import sys
import signal
import os
import subprocess
import aws2tf



def rc(cmd):
    out = subprocess.run(cmd, shell=True, capture_output=True)
    ol=len(out.stdout.decode('utf-8').rstrip())    
    el=len(out.stderr.decode().rstrip())
    if el!=0:
         errm=out.stderr.decode().rstrip()
         print(errm)

    # could be > /dev/null
    #if ol==0:
    #    print("No return from command " + str(cmd) + " exit ...")
    
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
   print("finishing state file")
   with open(statefile, 'r') as fp:
        for count, line in enumerate(fp):
            pass
   print('Total Lines', count + 1)
   if count <= 5 :
      print("empty state exiting")
      exit()


   el=count-2
   print('toedit=' + str(el))
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
   
   com="cd data && terraform refresh -no-color -lock=false"
   rout=rc(com)
   #print(rout)

   for i in data['resources']:
      #print(json.dumps(i, indent=4, default=str)) 
      ttft=i['type']
      rname=i['name']
      com="terraform state show -no-color -state " + statefile + " " + ttft + "." + rname + " > data/" + ttft + "-" + rname + "-1.txt"
      print(ttft + " " + rname)
      rout=rc(com)
      #print(rout) 
