#!/usr/bin/env python3
import boto3
import multiprocessing
import signal
import argparse
import s3
import ec2
import os
import common
import resources
import cw
import fixtf

if __name__ == '__main__':
    global processed
    common.check_python_version()
    #print("cwd=%s" % os.getcwd())
    signal.signal(signal.SIGINT, common.ctrl_c_handler)
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-b", "--bucket", help="bucket name or matching sting")
    argParser.add_argument("-t", "--type", help="resource type aws_s3, ec2 aws_vpc etc")
    argParser.add_argument("-r", "--region", help="region")
    argParser.add_argument("-i", "--id", help="resource id")
    argParser.add_argument("-m", "--merge", help="merge [False]|True")
    args = argParser.parse_args()
    #print("args=%s" % args)
    processed = []
    dependancies = []
    
    #print("args.bucket=%s" % args.bucket)
    #print("args.type=%s" % args.type)
    #print("args.id=%s" % args.id)
    if args.type is None:
        print("type is required eg:  -t aws_vpc")
        print("setting to all")
        args.type="all"
    else:
        type=args.type

    if args.region is None:
        print("region is required eg:  -r eu-west-1  [using eu-west-1 as default]")
        region="eu-west-1"
    else:
        region=args.region   

    mg=False
    if args.merge is not None:
        mg=args.merge

    if mg is False:
        print("No merge - removing terraform.tfstate* and aws_*.tf")
        com="rm -f terraform.tfstate* aws_*.tf"
        rout=common.rc(com)

    id=args.id
    if args.bucket is None:
        fb=id
    else:
        fb=args.bucket  


    com="rm -f *.txt *.json"
    rout=common.rc(com)


    common.aws_tf(region)

# get the current
    my_session = boto3.setup_default_session(region_name=region) 
 
    print('region passed ='+region)
   
    #cpus=multiprocessing.cpu_count()
    #print("cpus="+str(cpus))

    if type=="net":
        net_types=resources.resource_types(type)
        for i in net_types:
            #print("calling "+i)
            ec2.ec2_resources(i,None)


    elif type=="s3":
        com="rm -f s3-*.tf s3.tf tfplan *s3*.out"
        rout=common.rc(com)
        s3.get_all_s3_buckets(fb,region)

    elif type=="cw":
        cw.cwlogs(type,id,"logGroups","logGroupName","logGroupNamePrefix")

    else:
        print("calling ec2.ec2_resources with type="+type+" id="+str(id))
        ec2.ec2_resources(type,id)

    
    common.wrapup()
    print(processed)
    print("Done - exiting")
    exit(0)

