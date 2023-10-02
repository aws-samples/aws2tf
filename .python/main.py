#!/usr/bin/env python3
import boto3
import multiprocessing
import signal
import argparse
import aws2tf
import s3
import ec2
import os

if __name__ == '__main__':
    aws2tf.check_python_version()
    #print("cwd=%s" % os.getcwd())
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-b", "--bucket", help="bucket name or matching sting")
    argParser.add_argument("-t", "--type", help="resource type s3, ec2 vpc etc")
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
    rout=aws2tf.rc(com)


    fb=args.bucket  
    id=args.id
    #print("id="+str(id))

    type=args.type
    region=args.region

    statefile='data/'+type+'-terraform.tfstate'

    signal.signal(signal.SIGINT, aws2tf.ctrl_c_handler)

# get the current
    my_session = boto3.setup_default_session(region_name=region) 
 
    #print('Boto Region = '+ my_region + " region passed ="+region)
   
    #cpus=multiprocessing.cpu_count()
    #print("cpus="+str(cpus))


    with open(statefile, "w") as sf:
        aws2tf.start_state(sf)

##############################
### fetch rsources  
# ############################# 
#    
        #s3.get_all_s3_buckets(sf,fb)
        ec2.ec2_resources(sf,type,id)

        aws2tf.end_state(sf)
   

    sf.close()

    aws2tf.finish_state(statefile)
       

    print("Python done")
    exit(0)