#!/usr/bin/env python3

import boto3
import signal
import argparse
import glob
import os
import sys
import shutil
import datetime
import json


sys.path.insert(0, './.python')
#from get_aws_resources import aws_s3
import common
import resources
import globals

import stacks
from fixtf_aws_resources import aws_dict


def extra_help():
    print("\nExtra help\n")
    print("Type codes supported - ./aws2tf.py -t [type code]:\n")
    with open('.python/resources.py', 'r') as f:
        for line in f.readlines():
            line3=""
            if "#" in line:  line3=line.split("#")[1].strip()
            line=line.strip().split(":")[0]
            if "type ==" in line and "aws_" not in line:
                line=line.split("==")[-1].strip().strip("'").strip('"')
                if line3 != "": 
                    if len(line) < 3:
                        print("./aws2tf.py  -t "+line+"     \t\t\t"+str(line3))
                    elif len(line) > 10:
                        print("./aws2tf.py  -t "+line+"     \t"+str(line3))
                    else:
                        print("./aws2tf.py  -t "+line+"     \t\t"+str(line3))
                else:
                    print("./aws2tf.py  -t "+line)
    print("\nOr instead of the above type codes use the terraform type eg:\n\n./aws2tf.py -t aws_vpc\n")
    print("\nTo get a deployed stack set:\n\n./aws2tf.py -t stack -i stackname\n")               
    exit()


def build_lists():
  
    print("Building core resource lists ...")
    ## vpcs
    client = boto3.client('ec2')
    response=[]
    paginator = client.get_paginator('describe_vpcs')
    for page in paginator.paginate(): response = response + page['Vpcs']
    for j in response: globals.vpclist[j['VpcId']]=True
    response=[]
    paginator = client.get_paginator('describe_security_groups')
    for page in paginator.paginate(): response = response + page['SecurityGroups']
    for j in response: globals.sglist[j['GroupId']]=True
    response=[]
    paginator = client.get_paginator('describe_subnets')
    for page in paginator.paginate(): response = response + page['Subnets']
    for j in response: globals.subnetlist[j['SubnetId']]=True
    response=[]
    paginator = client.get_paginator('describe_transit_gateways')
    for page in paginator.paginate(): response = response + page['TransitGateways']
    for j in response: globals.tgwlist[j['TransitGatewayId']]=True

    ## roles
    client = boto3.client('iam')
    response=[]
    paginator = client.get_paginator('list_roles')
    for page in paginator.paginate(): response = response + page['Roles']
    with open('imported/roles.json', 'w') as f: json.dump(response, f, indent=2,default=str)

    for j in response: globals.rolelist[j['RoleName']]=True
    response=[]
    #if globals.debug: print(str(globals.vpclist))



#if __name__ == '__main__':

def main():
    now = datetime.datetime.now()
    print("aws2tf started at %s" % now)
    common.check_python_version()
    # print("cwd=%s" % os.getcwd())
    signal.signal(signal.SIGINT, common.ctrl_c_handler)

    argParser = argparse.ArgumentParser()
    argParser.add_argument("-l", "--list",help="List extra help information" , action='store_true')
    argParser.add_argument("-t", "--type", help="resource type aws_s3, ec2 aws_vpc etc")
    argParser.add_argument("-i", "--id", help="resource id")
    argParser.add_argument("-r", "--region", help="region")
    argParser.add_argument("-m", "--merge", help="merge", action='store_true')
    argParser.add_argument("-d", "--debug", help="debug", action='store_true')
    argParser.add_argument("-s", "--singlefile", help="singlefile", action='store_true')
    argParser.add_argument("-v", "--validate", help="validate and exit", action='store_true')
    argParser.add_argument("-a", "--accept", help="expected plan changes accepted", action='store_true')
    argParser.add_argument("-e", "--exclude", help="resource types to exclude")
    argParser.add_argument("-b3", "--boto3error", help="exit on boto3 api error (for debugging)", action='store_true')
    argParser.add_argument("-la", "--serverless", help="Lambda mode - when running in a Lambda container", action='store_true')
    args = argParser.parse_args()
    type=""

    path = shutil.which("terraform") 

    if path is None:
        print("no executable found for command 'terraform'")
        exit()

    globals.expected=args.accept

    # print("args=%s" % args)
    
    # print("args.bucket=%s" % args.bucket)
    # print("args.type=%s" % args.type)
    # print("args.id=%s" % args.id)
    globals.merge=args.merge

    if args.list: extra_help()
    if args.debug: globals.debug = True
    if args.validate: globals.validate = True

    if args.type is None or args.type=="":
        if args.serverless:
            print("type is required eg:  -t aws_vpc  when in serverless mode, exiting ....")
            exit()
        print("type is required eg:  -t aws_vpc")
        print("setting to all")
        args.type = "all"
    else:
        type = args.type

    #print("args.exclude="+str(args.exclude))

 # build exclusion list 

    if args.exclude is not None: 
        extypes=args.exclude
        if "," in extypes:
                extypes = extypes.split(",")
        else:
                extypes = [extypes]
        globals.all_extypes=[]
        for i in extypes: 
            globals.all_extypes = globals.all_extypes + resources.resource_types(i)
    else:
        globals.all_extypes=[]

    if args.region is None:
        com = "aws configure get region"
        rout = common.rc(com)
        el = len(rout.stderr.decode().rstrip())
        if el != 0:
            print("region is required eg:  -r eu-west-1  [using eu-west-1 as default]")
            region = "eu-west-1"
        else:
            region = rout.stdout.decode().rstrip()
            if len(region) == 0:
                region=os.getenv("AWS_REGION")
                if region is None:
                    region=os.getenv("AWS_DEFAULT_REGION")
                    if region is None:
                        print("region is required - set in AWS cli or pass with -r")
                        exit()
            print("region set from aws cli / environment variables as "+region)
    else:
        region = args.region

    globals.region = region
    globals.regionl = len(region)
    #os.environ["AWS"] = "aws --region "+region+" "
 
    # get the current env and set directory
    if globals.debug: print("setting session region="+region)
    try:
        my_session = boto3.setup_default_session(region_name=region)
    except Exception as e: 
        print("AWS Authorization Error: "+str(e))
    if globals.debug: print("getting account")
    try:
        globals.acc = boto3.client('sts').get_caller_identity().get('Account')
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        exn=str(exc_type.__name__)
        if "ExpiredToken" in str(e):
            print("STS Authorization Error: ExpiredToken, exiting .....")
        exit()
    print('Using region: '+region + ' account: ' + globals.acc+"\n")
####  restore form S3 if merging & serverless

    globals.region = region
    globals.regionl = len(region)
    if args.serverless:     
        globals.serverless=True
        globals.path1="/tmp/aws2tf/generated/tf-"+globals.acc+"-"+region
        globals.path2=globals.path1+"/imported"
    else:
        globals.serverless=False
        globals.path1="generated/tf-"+globals.acc+"-"+region
        globals.path2=globals.path1+"/imported"

    if globals.serverless:
        if args.merge: common.download_from_s3()
        else: common.empty_and_delete_bucket()


    if globals.merge is False:
        com = "rm -rf "+globals.path1
        rout = common.rc(com)
        if globals.serverless: common.empty_and_delete_bucket()




    com = "mkdir -p "+globals.path2
    rout = common.rc(com)
    globals.cwd=os.getcwd()
    os.chdir(globals.path1) 

    common.aws_tf(region)

    if args.merge:
        print("Merging "+str(globals.merge))
        #print("Merging capability disabled for now - exiting")
        #exit()
        try:
            file = open('pyprocessed.txt', 'r')
            while True:
                line = file.readline()
                if not line:
                    break
                line = line.strip()

                globals.rproc[line] = True
            if globals.debug:
                print("Pre Processed:")
                for i in globals.rproc.keys():
                    print(i)

            com = "rm -f main.tf"
            rout = common.rc(com) 
            com = "cp imported/*.tf ."
            rout = common.rc(com) 

        except:
            print("No pyprocessed.txt found")
            pass



    id = args.id


#### setup

    build_lists()
    
    if type == "" or type is None: type = "all"
    
    print("---<><> "+ str(type),"Id="+str(id)," exclude="+str(globals.all_extypes))  

################# -- now we are calling ----   ###############################

    if "," in type:
        if "stack" in type:
            print("Cannot mix stack with other types")
            exit()

        if id is not None:
            print("Cannot pass id with multiple types")
            exit()

        #if globals.serverless:
        #    print("Cannot pass multiple types when running on serverless")
        #    exit()

        types = type.split(",")
        all_types = []
        for type1 in types: all_types = all_types + resources.resource_types(type1)

        for type2 in all_types:
            if type2 in aws_dict.aws_resources:   
                if type2 in globals.all_extypes:
                    print("Excluding", type2) 
                    continue                 
                common.call_resource(type2, id)
            else:
                print("Resource",type2," not found in aws_dict")
        
    else:
        all_types = resources.resource_types(type)

        try:
            lall=len(all_types)
        except:
            lall=0

        if all_types is None: print("No resources found all_types=None")

        if type == "stack":
            if id is None:
                print("Must pass a stack name as a parameter   -i <stack name>")
                exit()
            else:
                globals.expected=True
                stacks.get_stacks(id)
        
        elif type.startswith("aws_"):
            if type in aws_dict.aws_resources:
                if type in globals.all_extypes:
                    print("Excluding", type) 
                else:    
                    common.call_resource(type, id)
            else:
                print("Resource",type," not found in aws_dict")

        elif all_types != None and lall > 1:
            #print("len all_types="+str(len(all_types))) # testing only
            #id="foobar" # testing only
            ic=0
            istart=0
            it=len(all_types)
            globals.expected=True
            for i in all_types:
                ic=ic+1
                if ic > it: break 
                if ic < istart: continue
                    
                print(str(ic)+" of "+str(it) +"\t"+i)
                if i in globals.all_extypes:
                    print("Excluding", i) 
                    continue
                common.call_resource(i, id)
                
        else:
            if all_types is not None:
                for type in all_types:
                    if type in aws_dict.aws_resources:
                        if type in globals.all_extypes:
                            print("Excluding", type) 
                            continue 
                        common.call_resource(type,id)
                    else:
                        print("Resource",type," not found in aws_dict")
            else:
                print("No resources found")
                exit()

#########################################################################################################################

## Known dependancies section
    
    for ti in list(globals.rdep):
            if not globals.rdep[ti]:
                i = ti.split(".")[0]
                id = ti.split(".")[1]
                if id not in str(globals.policyarns):
                    if globals.debug: print("type="+i+" id="+str(id))
                    common.call_resource(i, id)
    #else:
    #    print("No Known Dependancies")

    common.tfplan1()
    common.tfplan2()
    
    if ":" in globals.rproc:
        print(": in rproc exiting")
        exit()

    print("Detected Dependancies -----------------------") 
    detdep=False
    for ti in globals.rproc.keys():
        if not globals.rproc[ti]: 
            #print(str(ti)+":"+str(globals.rproc[ti]))  
            print(str(ti)) 
            detdep=True
            
 
    if not detdep:
        print("No Detected Dependancies") 


    lc=0
    olddetdepstr=""
    detdepstr=""
    while detdep:
        for ti in list(globals.rproc):
            if not globals.rproc[ti]:
                i = ti.split(".")[0]
                id = ti.split(".",1)[1]
                if globals.debug: print("DD calling getresource with type="+i+" id="+str(id))
                #print("----- DD ----  calling getresource with type="+i+" id="+str(id))
                common.call_resource(i, id)
        detdep=False
        lc  = lc + 1

# go again plan and split / fix
        print("Terraform Plan - Dependancies Detection Loop "+str(lc)+".....")

        x=glob.glob("import__aws_*.tf")
        #print(str(x))
        #td=""
        for fil in x:
            tf=fil.split('__',1)[1]
            #td=td+" "+tf

            com = "mv "+tf +" imported/"+tf
            rout = common.rc(com)

         
        common.tfplan1()
        common.tfplan2()
 
        detdepstr=""
        for ti in globals.rproc.keys():
            if not globals.rproc[ti]:
                detdep=True 
                print(str(ti)+" is False")
                detdepstr=detdepstr+str(ti)+" "

        print("----------- Completed "+str(lc)+" dependancy check loops --------------") 
        if olddetdepstr == detdepstr and detdepstr != "":
            print("\nERROR: No change/progress in dependancies exiting... \n")
            for ti in globals.rproc.keys():
                if not globals.rproc[ti]:
                    print("ERROR: Not found "+str(ti)+" - check if this resource still exists in AWS. Also check what resource is using it - grep the *.tf files in the generated/tf.* subdirectory")
            exit()

        olddetdepstr=detdepstr

    common.tfplan3()
    if globals.validate is False: 
        now = datetime.datetime.now()
        print("aws2tf wrap up started at %s" % now)
        common.wrapup()
    else: 
        print("\nValidation only - no files written")
        exit()

##########################################################################
####### Finish up
#########################################################################
    

    with open("pyprocessed.txt", "a") as f:
        for i in globals.rproc.keys():
            if globals.debug: print(str(i))
            f.write(i+"\n")
    com = "sort -u pyprocessed.txt -o pyprocessed.txt"
    rout = common.rc(com)
    
#### Trivy - if installed
# 
#       
    path = shutil.which("trivy") 
    if path is not None:
        x = glob.glob("aws_*__*.tf")
        awsf=len(x)
        if awsf < 256:
            print("\nRunning trivy security check .....")
            common.trivy_check()

        else:
            print("\nSkipping security check - too many files.")
            print("Use trivy manually if required")
    else:
        print("trivy not installed, skipping security check")

    print("Terraform files & state in sub-directory: "+ globals.path1)

    if globals.serverless: common.upload_directory_to_s3()

    x = glob.glob("*.err")
    awsf=len(x)
    if awsf > 0:
        print("\nErrors found - see *.err files, and please report via github issue")   

    if args.singlefile:
        print("Single file mode .....")
        tf_files = glob.glob("aws_*__*.tf")
        if not tf_files:
            print("No aws_*.tf files found")
        else:
            with open('main.tf', 'w') as outfile:
                for tf_file in sorted(tf_files):
                    if globals.debug: outfile.write(f"# Source: {tf_file}\n")
                    with open(tf_file, 'r') as infile:
                        outfile.write(infile.read())
                    outfile.write('\n\n')
                    #com = "mv "+tf_file +" imported/"+tf_file
                    #rout = common.rc(com)
        print(f"Successfully merged {len(tf_files)} files into main.tf")
        com = "mv aws_*__*.tf imported"
        rout = common.rc(com)

    now = datetime.datetime.now()
    print("aws2tf finished at %s" % now)
    exit(0)


if __name__ == '__main__':
    main()
