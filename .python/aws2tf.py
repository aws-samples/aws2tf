#!/usr/bin/env python3
import boto3
import signal
import argparse
import aws_s3
import common
import resources
import globals
import glob
import stacks
import os
import sys


if __name__ == '__main__':

    common.check_python_version()
    # print("cwd=%s" % os.getcwd())
    signal.signal(signal.SIGINT, common.ctrl_c_handler)
    argParser = argparse.ArgumentParser()
    argParser.add_argument(
        "-b", "--bucket", help="bucket name or matching sting")
    argParser.add_argument(
        "-t", "--type", help="resource type aws_s3, ec2 aws_vpc etc")
    argParser.add_argument("-r", "--region", help="region")
    argParser.add_argument("-i", "--id", help="resource id")
    argParser.add_argument("-m", "--merge", help="merge [False]|True")
    argParser.add_argument("-d", "--debug", help="debug [False]|True")
    argParser.add_argument("-v", "--validate", help="validate [False]|True")
    args = argParser.parse_args()
    # print("args=%s" % args)

    # print("args.bucket=%s" % args.bucket)
    # print("args.type=%s" % args.type)
    # print("args.id=%s" % args.id)

    if args.validate is not None:
        globals.validate = True
    

    if args.type is None:
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

    mg = False
    if args.merge is not None:
        mg = True
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

    if mg is False:
        print("No merge - removing terraform.tfstate* and aws_*.tf *.out")
        com = "rm -f aws.tf terraform.tfstate* aws_*.tf s3-*.tf aws_*.zip tfplan *.out *.log import*.tf imported/* main.tf"
        rout = common.rc(com)

    id = args.id

    if args.bucket is None:
        fb = id
    else:
        fb = args.bucket

    if args.debug is not None:
        globals.debug = True

    if mg is False:
        com = "rm -f *.txt *.json"
        rout = common.rc(com)

    common.aws_tf(region)

# get the current
    my_session = boto3.setup_default_session(region_name=region)
    globals.acc = boto3.client('sts').get_caller_identity().get('Account')
    print('Using region: '+region + ' account: ' + globals.acc+"\n")
    globals.region = region
    globals.regionl = len(region)
    common.aws_tf(region)

    if type == "all": type = "test"
    elif type == "aws_vpc" or type == "vpc": type = "aws_vpc"
    elif type == "subnet": type = "aws_subnet"
    elif type == "config": type = "aws_config_config_rule"
    elif type == "ec2": type = "aws_instance"
    elif type == "eks": type = "aws_eks_cluster"
    elif type == "lambda": type="aws_lambda_function"
    elif type == "cw" or type == "cloudwatch" or type == "logs": type = "aws_cloudwatch_log_group"
        

################# -- now we are calling ----   ###############################

    if type == "s3":
        com = "rm -f s3-*.tf s3.tf tfplan *s3*.out"
        rout = common.rc(com)
        aws_s3.get_all_s3_buckets(fb, region)

    elif type == "net" or type == "kms" or type == "iam" or type == "lattice" or type == "test":
        all_types = resources.resource_types(type)
        for i in all_types:
            common.call_resource(i, id)

    elif type == "stack":
        if id is None:
            print("Must pass a stack name as a parameter   -i <stack name>")
            exit()
        else:
            stacks.get_stacks(id)


    # calling by direct terraform type aws_xxxxx
    else:
        common.call_resource(type,id)

#########################################################################################################################

## Known dependancies section
    
    kdep=False
    for ti in globals.rdep.keys():
        if not globals.rdep[ti]: 
            print("Known Dependancies ----------------------")
            print(str(ti)+":"+str(globals.rdep[ti]))  
            kdep=True

    #if kdep:
    for ti in list(globals.rdep):
            if not globals.rdep[ti]:
                i = ti.split(".")[0]
                id = ti.split(".")[1]
                if id not in str(globals.policyarns):
                    print("KD calling common.call_resource with type="+i+" id="+str(id))
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
            print(str(ti)+":"+str(globals.rproc[ti]))  
            detdep=True
            
 
    if not detdep:
        print("No Detected Dependancies") 

    lc=0
    while detdep:
        for ti in list(globals.rproc):
            if not globals.rproc[ti]:
                i = ti.split(".")[0]
                id = ti.split(".")[1]
                if globals.debug: print("DD calling getresource with type="+i+" id="+str(id))
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
            com = "rm -f "+tf
            rout = common.rc(com)
        #print(str(td))
        #com = "rm -f "+td
        #rout = common.rc(com)
         
        common.tfplan1()
        common.tfplan2()
        #print("********** keys start ***************")
        #for ti in globals.rproc.keys():
        #    print(str(ti)+":"+str(globals.rproc[ti]))

        #print("********** keys end ***************")  

        for ti in globals.rproc.keys():
            if not globals.rproc[ti]:
                detdep=True 
                print(str(ti)+" is False")

        print("----------- Completed "+str(lc)+" dependancy check loops --------------") 
        
        if lc > 9:
            print("ERROR: Too many loops exiting")
            for ti in globals.rproc.keys():
                if not globals.rproc[ti]:  
                    print("ERROR: Not found "+str(ti)+" - check if this resource still exists in AWS")

            exit()
            #detdep=True

    common.tfplan3()
    if globals.validate is False:
        common.wrapup()

#################################

    print("writing pyprocessed.txt")
    if mg is True:
        with open("pyprocessed.txt", "a") as f:
            for i in globals.rproc.keys():
                if globals.debug: print(str(i))
                f.write(i+"\n")
    else:
        with open("pyprocessed.txt", "w") as f:
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

    print("Done")

    exit(0)
