#!/usr/bin/env python3

import boto3
import signal
import argparse
import glob
import os
import sys


sys.path.insert(0, './.python')
from get_aws_resources import aws_s3
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



if __name__ == '__main__':

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
    argParser.add_argument("-v", "--validate", help="validate and exit", action='store_true')
    argParser.add_argument("-a", "--apionly", help="boto3 api only (for debugging)", action='store_true')
    argParser.add_argument("-b3", "--boto3error", help="exit on boto3 api error (for debugging)", action='store_true')
    args = argParser.parse_args()
    type=""
    # print("args=%s" % args)
    
    # print("args.bucket=%s" % args.bucket)
    # print("args.type=%s" % args.type)
    # print("args.id=%s" % args.id)
    mg=args.merge

    if args.list: extra_help()
    if args.debug: globals.debug = True
    if args.validate: globals.validate = True

    if args.type is None or args.type=="":
        print("type is required eg:  -t aws_vpc")
        print("setting to all")
        args.type = "all"
    else:
        type = args.type

    if args.region is None:
        com = "aws configure get region"
        rout = common.rc(com)
        el = len(rout.stderr.decode().rstrip())
        if el != 0:
            print(
                "region is required eg:  -r eu-west-1  [using eu-west-1 as default]")
            region = "eu-west-1"
        else:
            region = rout.stdout.decode().rstrip()
            print("region set from aws cli as "+region)
    else:
        region = args.region

    globals.region = region
    globals.regionl = len(region)

    print("args.merge="+str(args.merge))
 
    if args.merge:
        print("Merging "+str(mg))
        try:
            file = open('pyprocessed.txt', 'r')
            while True:
                line = file.readline()
                if not line:
                    break
                line = line.strip()

                globals.rproc[line] = True
            print("Pre Processed:")
            for i in globals.rproc.keys():
                print(i)

        except:
            print("No pyprocessed.txt found")
            pass


    # get the current env and set directory

    my_session = boto3.setup_default_session(region_name=region)
    globals.acc = boto3.client('sts').get_caller_identity().get('Account')
    print('Using region: '+region + ' account: ' + globals.acc+"\n")
    globals.region = region
    globals.regionl = len(region)
    
    globals.path1="generated/tf-"+globals.acc+"_"+region
    globals.path2=globals.path1+"/imported"
    com = "mkdir -p "+globals.path2
    rout = common.rc(com)
    globals.cwd=os.getcwd()
    os.chdir(globals.path1) 

    common.aws_tf(region)


    if mg is False:
        print("No merge - removing terraform.tfstate* and aws_*.tf *.out")
        com = "rm -f aws.tf terraform.tfstate* aws_*.tf s3-*.tf aws_*.zip tfplan *.out *.log aws_*.sh stacks.sh import*.tf imported/* main.tf plan1* plan2* *.txt *.json *.err"
        rout = common.rc(com)
        com = "mkdir -p imported notimported"
        rout = common.rc(com)

    id = args.id
    
    if type == "" or type is None: type = "all"
    print("---<><>"+ str(type),str(id))
        

################# -- now we are calling ----   ###############################

    all_types = resources.resource_types(type)
    try:
        lall=len(all_types)
    except:
        lall=0
    #print("all_types="+str(all_types))

    if all_types is None:
        print("No resources found")
        exit()

    if type == "stack":
        if id is None:
            print("Must pass a stack name as a parameter   -i <stack name>")
            exit()
        else:
            stacks.get_stacks(id)

    elif type.startswith("aws_"):
        if type in aws_dict.aws_resources:
            common.call_resource(type, id)

    elif all_types != None and lall > 1:
        print("len all_types="+str(len(all_types)))
        ic=0
        istart=1
        it=len(all_types)
        for i in all_types:
            ic=ic+1
            if ic > it: break 
            if ic < istart: continue
                
            print(str(ic)+" of "+str(it) +"\t"+i)
            common.call_resource(i, id)
            
    else:
        if all_types is not None:
            for type in all_types:
                if type in aws_dict.aws_resources:
                    common.call_resource(type,id)
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

    if args.apionly:   exit(0)

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

        x=glob.glob("import__aws_*.tf")
        #print(str(x))
        #td=""
        for fil in x:
            tf=fil.split('__',1)[1]
            #td=td+" "+tf
##########################
##########################
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


        #if lc > 16:
        #    print("ERROR: Too many loops exiting")
        #    for ti in globals.rproc.keys():
        #        if not globals.rproc[ti]:  
        #            print("ERROR: Not found "+str(ti)+" - check if this resource still exists in AWS")
        #    exit()

    common.tfplan3()
    if globals.validate is False: common.wrapup()

##########################################################################
####### Finish up
#########################################################################

    print("writing pyprocessed.txt")
    
    with open("pyprocessed.txt", "a") as f:
        for i in globals.rproc.keys():
            if globals.debug: print(str(i))
            f.write(i+"\n")
    com = "sort -u pyprocessed.txt -o pyprocessed.txt"
    rout = common.rc(com)

    if globals.debug is True:
        print("Types -----------------")
        print(globals.types)

        print("Processed ---------------")
        for i in globals.rproc.keys():
            print(i)

    print("\nTerraform files & state in sub-directory: "+ globals.path1+"\n")

    exit(0)





