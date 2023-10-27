import boto3
import sys
import subprocess
import fixtf
import os
import globals
import glob


def tfplan():
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

   print("fix tf files.....") 
   
   
# change this so don't reply on type - get it from file name

   x=glob.glob("aws_*_import.tf")
   for fil in x:
         tf=fil.split('_import')[0]
         #print("tf="+tf)
         globals.types=globals.types+[tf]
        
   x=glob.glob("aws_*__*.out")
   for fil in x:
         type=fil.split('__')[0]
         tf=fil.split('.')[0]
         #print("type="+type+" tf="+tf)
         globals.types=globals.types+[type]             
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
      if globals.validate: exit()


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
      com="mv *_import.tf *.out *.json imported"
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


# if type == "aws_vpc_endpoint": return "ec2","describe_vpc_endpoints","VpcEndpoints","VpcEndpointId","vpc-id"

def write_import(type,theid):
   tfid=theid.replace("/","__").replace(".","__").replace(":","__")
   fn=type+"_"+tfid+"_import.tf"
   with open(fn, "a") as f:
      f.write('import {\n')
      f.write('  to = ' +type + '.' + tfid + '\n')
      f.write('  id = "'+ theid + '"\n')
      f.write('}\n')
   globals.processed=globals.processed+[type+"."+theid]  
   return



def getresource(type,id,clfn,descfn,topkey,key,filterid):
   for j in globals.specials:
      if type == j: 
         print(type + " in specials list returning ..")
         return
   print("--> In getresource doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

   if type in str(globals.types): 
      print("Found "+type+"in types skipping ...")
      return
   fn=type+"_import.tf"
   
   if id is not None:
      pt=type+"."+id
      fn=type+"_"+id+"_import.tf"
      if pt in str(globals.processed):
         print("Found "+pt+"in processed skipping ...") 
         return 
   
   
   response = []
   client = boto3.client(clfn) 
   paginator = client.get_paginator(descfn)
   for page in paginator.paginate():
      response.extend(page[topkey])
   print("response length="+str(len(response)))
   #for item in response:
   #   print(item)
   #   print("--------------------------------------")

   print("filterid="+filterid)

   if str(response) != "[]":
         for item in response:
            if id is None or filterid=="": # do it all
               #print(str(item))
               try:
                  if "aws-service-role" in str(item["Path"]): 
                     print("Skipping service role" + str(item[key])) 
                     continue
               except:
                  pass
               
               theid=item[key]
               pt=type+"."+theid
               if pt not in str(globals.processed):
                  write_import(type,theid)
               else:
                  print("Found "+pt+"in processed skipping ...") 
                  continue
            else:
               if "." not in filterid:
                  #print("item=" + str(item) + " id=" + id + " filterid=" + filterid)
                  if id == str(item[filterid]):
                     #print(str(item))
                     theid=item[key]
                     write_import(type,theid)
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
                           write_import(type,theid)
                     except:
                        print("-------- error on processing")
                        print(str(item))
                        print("filterid="+filterid)
                        print("----------------------------")
                        pass
                  
  
    #tfplan(type)

def special_deps(ttft,taddr):
   #print("In special deps"+ttft+"  "+taddr)
   if ttft == "aws_subnet": 
      #print("In special deps")
      globals.dependancies=globals.dependancies + ["aws_route_table_association."+taddr]
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
   print("--> In getresource doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+"filterid="+filterid)
   if type in str(globals.types): 
      print("Found "+type+"in types skipping ...")
      return
   fn=type+"_import.tf"
   
   if id is not None:
      pt=type+"."+id
      fn=type+"_"+id+"_import.tf"
      if pt in str(globals.processed):
         print("Found "+pt+"in processed skipping ...") 
         return 
   
   
   response = []
   client = boto3.client(clfn) 
   paginator = client.get_paginator(descfn)
   for page in paginator.paginate():
      response.extend(page[topkey])
   print("response length="+str(len(response)))
   if str(response) != "[]": 
      with open(fn, "a") as f:
         for item in response:
            il=len(item['Associations'])
            for r in range(0,il):
               #print(str(r))
               #print(str(item['Associations'][r]))
               rtid=(str(item['Associations'][r]['RouteTableId']))
               try:
                  #print(str(item['Associations'][r]['SubnetId']))
                  subid=str(item['Associations'][r]['SubnetId'])
                  if subid in str(globals.processed):
                     #print(subid+"in processed...."+fn)
                     theid=subid+"/"+rtid
                     write_import(type,theid)        
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
      for j in globals.processed:
         if "aws_iam_role" in j:
            response=[]
            dotc=j.count('.')
            rn=j.split(".")[1]
            if dotc > 1: rn=rn +"." + j.split(".")[2]         
            paginator = client.get_paginator(descfn)
            for page in paginator.paginate(RoleName=rn):
               response.extend(page[topkey])
            if response == []: 
               continue
            #print("--RoleName="+rn+" response="+str(response))
            for j in response: 
               if j not in str(globals.policies):
                  print("adding "+j+" to policies for role " + rn)
                  globals.policies = globals.policies + [j]
                  theid=rn+":"+j
                  write_import(type,theid)


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
            write_import(type,theid) 
   
   return



##
## special due to scope local
##
def get_aws_iam_policy(type,id,clfn,descfn,topkey,key,filterid):
   print("--> In get_aws_iam_policy doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)
   
   client = boto3.client(clfn) 
   response=[]
   paginator = client.get_paginator(descfn)
   for page in paginator.paginate(Scope='Local'):
      response.extend(page[topkey])
   #print("response="+str(response))
   if response == []: 
      print("empty response returning") 
      return   
   for j in response: 
            theid=j[key]
            retid=j["Arn"]
            if id is None:
               if theid not in str(globals.policies):
                  print("adding "+theid+" to policies")
                  globals.policies = globals.policies + [theid]
                  write_import(type,retid) 
            else:
               if retid == id:
                  if theid not in str(globals.policies):
                     print("adding "+theid+" to policies")
                     globals.policies = globals.policies + [theid]
                     write_import(type,retid)
   return



