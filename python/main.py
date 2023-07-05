#!/usr/bin/env python3
import boto3
import multiprocessing
import signal
import argparse
import aws2tf
import s3
import ec2

if __name__ == '__main__':
    aws2tf.check_python_version()
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-b", "--bucket", help="bucket name or matching sting")
    argParser.add_argument("-t", "--type", help="resource type s3, ec2 vpc etc")
    args = argParser.parse_args()
    print("args=%s" % args)

    print("args.bucket=%s" % args.bucket)
    print("args.type=%s" % args.type)

    com="rm -f data/*.txt data/*.json"
    rout=aws2tf.rc(com)

    fb=args.bucket

    statefile='data/terraform.tfstate'

    signal.signal(signal.SIGINT, aws2tf.ctrl_c_handler)

# get the current region
    my_session = boto3.session.Session()
    my_region = my_session.region_name

    print(my_region)
   
    cpus=multiprocessing.cpu_count()
    print("cpus="+str(cpus))


    with open(statefile, "w") as sf:
        aws2tf.start_state(sf)

##############################
### fetch rsources  
# ############################# 
#    
        #s3.get_all_s3_buckets(sf,fb)
        ec2.ec2_resources(sf)

        aws2tf.end_state(sf)
   

    sf.close()

    aws2tf.finish_state(statefile)
       

    print("Done")
    exit()