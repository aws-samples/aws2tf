#!/usr/bin/env python3
import boto3
import signal
import argparse
import s3
import common
import resources
import globals
import kms
import eks
import ec2
import iam

import os
import sys


def call_resource(type, id):
    rr=False
    clfn, descfn, topkey, key, filterid = resources.resource_data(type, id)
    if clfn is None:
        print("error clfn is None with type="+type)
        exit()
    try:
        print("calling generic getresource with type="+type+" id="+str(id)+"   clfn="+clfn +
              " descfn="+str(descfn)+" topkey="+topkey + "  key="+key + "  filterid="+filterid)
        rr=common.getresource(type, id, clfn, descfn, topkey, key, filterid)
    except:
        pass
    if not rr:
        try:
            print("calling specific common.get_"+type+" with type="+type+" id="+str(id)+"   clfn=" +
                    clfn+" descfn="+str(descfn)+" topkey="+topkey + "  key="+key + "  filterid="+filterid)
            # TODO try getfn = getattr(eval(clfn), "get_"+type)
            getfn = getattr(eval(clfn), "get_"+type)            
            getfn(type, id, clfn, descfn, topkey, key, filterid)

        except Exception as e:
                # By this way we can know about the type of error occurring
                print(f"{e=}")
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)

                exit()

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
            file = open('processed.txt', 'r')
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
            print("No processed.txt found")
            pass

    if mg is False:
        print("No merge - removing terraform.tfstate* and aws_*.tf *.out")
        com = "rm -f aws.tf terraform.tfstate* aws_*.tf s3-*.tf tfplan *.out import*.tf imported/* main.tf"
        rout = common.rc(com)

    id = args.id

    if args.bucket is None:
        fb = id
    else:
        fb = args.bucket

    if args.debug is not None:
        globals.debug = True

    com = "rm -f *.txt *.json"
    rout = common.rc(com)

    common.aws_tf(region)

# get the current
    my_session = boto3.setup_default_session(region_name=region)
    globals.acc = boto3.client('sts').get_caller_identity().get('Account')
    print('Using region: '+region + ' account: ' + globals.acc)
    globals.region = region
    globals.regionl = len(region)
    common.aws_tf(region)

    if type == "all":
        type = "net"

    elif type == "aws_vpc" or type == "vpc":
        type = "aws_vpc"
    elif type == "subnet":
        type = "aws_subnet"
    elif type == "config":
        type = "aws_config_config_rule"
    elif type == "eks":
        type = "aws_eks_cluster"
    elif type == "cw" or type == "cloudwatch" or type == "logs":
        type = "aws_cloudwatch_log_group"

################# -- now we are calling ----   ###############################

    if type == "s3":
        com = "rm -f s3-*.tf s3.tf tfplan *s3*.out"
        rout = common.rc(com)
        s3.get_all_s3_buckets(fb, region)

    elif type == "net":
        all_types = resources.resource_types(type)
        for i in all_types:
            # print("calling "+i)
            call_resource(i, id)
    elif type == "kms":
        all_types = resources.resource_types(type)
        for i in all_types:
            print("calling "+i)
            call_resource(i, id)

    elif type == "iam" or type == "lattice":
        all_types = resources.resource_types(type)
        for i in all_types:
            call_resource(i, id)

    # calling by direct terraform type aws_xxxxx
    else:
        call_resource(type,id)

#########################################################################################################################

## Known dependancies section
    
    kdep=False
    for ti in globals.rproc.keys():
        if not globals.rproc[ti]: 
            print("Known Dependancies ----------------------")
            print(str(ti)+":"+str(globals.rproc[ti]))  
            kdep=True

    #if kdep:
    for ti in list(globals.rdep):
            if not globals.rdep[ti]:
                i = ti.split(".")[0]
                id = ti.split(".")[1]
                if id not in str(globals.policyarns):
                    print("KD calling call_resource with type="+i+" id="+str(id))
                    call_resource(i, id)
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
                call_resource(i, id)
        detdep=False
        lc  = lc + 1
# go again plan and split / fix
        com = "rm -f aws_*.tf *.out"
        rout = common.rc(com)
        common.tfplan1()
        common.tfplan2()
        #print("********** keys start ***************")
        #for ti in globals.rproc.keys():
        #    print(str(ti)+":"+str(globals.rproc[ti]))

        #print("********** keys end ***************")  

        for ti in globals.rproc.keys():
            
            if not globals.rproc[ti]:
                detdep=True 

                print(str(ti))

        print("----------- "+str(lc)+" loops completed --------------") 
        
        if lc > 8:
            print("ERROR: Too many loops exiting")
            print("ERROR: still False........")
            for ti in globals.rproc.keys():
                if not globals.rproc[ti]:
                    
                    print(str(ti))

            exit()
            #detdep=True

    common.tfplan3()
    common.wrapup()

#################################

    print("writing processed.txt")
    if mg is True:
        with open("processed.txt", "a") as f:
            for i in globals.rproc.keys():
                print(str(i))
                f.write(i+"\n")

    else:
        
        
        with open("processed.txt", "w") as f:
            for i in globals.rproc.keys():
                print(str(i))
                f.write(i+"\n")

    com = "sort -u processed.txt -o processed.txt"
    rout = common.rc(com)

    if globals.debug is True:
        print("Types -----------------")
        print(globals.types)

        print("Processed ---------------")
        for i in globals.rproc.keys():
            print(i)

    print("Done")

    exit(0)
