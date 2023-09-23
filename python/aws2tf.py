#!/usr/bin/env python3
import boto3
import multiprocessing
import signal
import argparse
import s3
import ec2
import os
import common

if __name__ == '__main__':
    common.check_python_version()
    #print("cwd=%s" % os.getcwd())
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-b", "--bucket", help="bucket name or matching sting")
    argParser.add_argument("-t", "--type", help="resource type aws_s3, ec2 aws_vpc etc")
    argParser.add_argument("-r", "--region", help="region")
    argParser.add_argument("-i", "--id", help="resource id")
    args = argParser.parse_args()
    #print("args=%s" % args)

    #print("args.bucket=%s" % args.bucket)
    #print("args.type=%s" % args.type)
    #print("args.id=%s" % args.id)
    if args.type is None:
        print("type is required eg:  -t aws_vpc")
        exit()

    if args.region is None:
        print("region is required eg:  -r eu-west-1")
        exit()

    com="rm -f data/*.txt data/*.json"
    rout=common.rc(com)


    fb=args.bucket  
    id=args.id
    #print("id="+str(id))

    type=args.type
    region=args.region


    signal.signal(signal.SIGINT, common.ctrl_c_handler)

# get the current
    my_session = boto3.setup_default_session(region_name=region) 
 
    #print('Boto Region = '+ my_region + " region passed ="+region)
   
    #cpus=multiprocessing.cpu_count()
    #print("cpus="+str(cpus))


    print("calling ec2.ec2_resources ...")
    ec2.ec2_resources(type,id)
    
    common.wrapup()
    print("Python done - exiting")
    exit(0)

