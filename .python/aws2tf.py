#!/usr/bin/env python3
import boto3
import signal
import argparse
import s3
import common
import resources
import globals

if __name__ == '__main__':
   
    globals.processed=[]
    common.check_python_version()
    #print("cwd=%s" % os.getcwd())
    signal.signal(signal.SIGINT, common.ctrl_c_handler)
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-b", "--bucket", help="bucket name or matching sting")
    argParser.add_argument("-t", "--type", help="resource type aws_s3, ec2 aws_vpc etc")
    argParser.add_argument("-r", "--region", help="region")
    argParser.add_argument("-i", "--id", help="resource id")
    argParser.add_argument("-m", "--merge", help="merge [False]|True")
    argParser.add_argument("-d", "--debug", help="debug [False]|True")
    args = argParser.parse_args()
    #print("args=%s" % args)

    
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
        mg=True
        print("Merging "+str(mg))
        file = open('processed.txt', 'r')
        while True:
            line = file.readline()
            if not line:
                break
            line=line.strip()
            globals.processed=globals.processed+[line]
        print("Pre Processed:")
        for i in globals.processed:
            print(i)

    if mg is False:
        print("No merge - removing terraform.tfstate* and aws_*.tf")
        com="rm -f terraform.tfstate* aws_*.tf s3-*.tf tfplan *.out *import.tf imported/*.tf main.tf"
        rout=common.rc(com)


    id=args.id

    if args.bucket is None:
        fb=id
    else:
        fb=args.bucket  

  
    if args.debug is not None:
        globals.debug=True
 

    com="rm -f *.txt *.json"
    rout=common.rc(com)

    common.aws_tf(region)

# get the current
    my_session = boto3.setup_default_session(region_name=region) 
 
    print('Using region: '+region)
   
    if type=="all": type="net"
 
    elif type=="aws_vpc" or type=="vpc": type="aws_vpc"     
    elif type=="config": type="aws_config_config_rule"
    elif type=="cw" or type=="cloudwatch" or type=="logs": type="aws_cloudwatch_log_group"

### -- now er are calling ----

    if type=="s3":
        com="rm -f s3-*.tf s3.tf tfplan *s3*.out"
        rout=common.rc(com)
        s3.get_all_s3_buckets(fb,region)  
        
    elif type=="net":
        net_types=resources.resource_types(type)
        for i in net_types:
            print("calling "+i)
            clfn,descfn,topkey,key,filterid=resources.resource_data(i,id)
            print("calling getresource with type="+i+" id="+str(id)+"   clfn="+clfn+" descfn="+str(descfn)+" topkey="+topkey + "  key="+key +"  filterid="+filterid)
            common.getresource(i,id,clfn,descfn,topkey,key,filterid)
            

    else:        
        clfn,descfn,topkey,key,filterid=resources.resource_data(type,id)
        if clfn is not None:
            print("calling getresource with type="+type+" id="+str(id)+" -- clfn="+clfn + " descfn="+descfn+  "topkey="+topkey + "key="+key +"filterid="+filterid)
            common.getresource(type,id,clfn,descfn,topkey,key,filterid)
        else:
            print("Error on calling resources with type="+type+" id="+str(id) + "  exiting...")
            exit()

    # loop through globals.type and call tfplan(type)

    common.tfplan(type)
 
    common.wrapup()
   
    if mg is True:
        with open("processed.txt","a") as f:
            for i in globals.processed:
                f.write(i+"\n")
                if globals.debug is True:
                    print("Processed:")
                    print(i)
    else:
        with open("processed.txt","w") as f:
            for i in globals.processed:
                f.write(i+"\n")
                if globals.debug is True:
                    print("Processed:")
                    print(i)

    com="sort -u processed.txt -o processed.txt"
    rout=common.rc(com)

    if globals.debug is True:
        print(globals.types)

    exit(0)

