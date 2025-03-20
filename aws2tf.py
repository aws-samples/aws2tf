#!/usr/bin/env python3

import boto3
import signal
import argparse
import glob
import os
import sys
import shutil
import datetime
import concurrent.futures
from typing import List, Dict
import io
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, './code')
#from get_aws_resources import aws_s3
import common
import resources
import globals
import timed_interrupt

import stacks
from fixtf_aws_resources import aws_dict
from build_lists import build_lists, build_secondary_lists



def extra_help():
    print("\nExtra help\n")
    print("Type codes supported - ./aws2tf.py -t [type code]:\n")
    with open('code/resources.py', 'r') as f:
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
    print("exit 001")
    timed_interrupt.timed_int.stop()
    exit()


def process_file_operations(files: List[str], output_file: str) -> None:
    """Efficiently process multiple files into a single output file."""
    with open(output_file, 'w') as outfile:
        timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        outfile.write(f"# Generated by aws2tf on: {timestamp}\n\n")
        
        # Use a buffer to reduce I/O operations
        buffer = io.StringIO()
        for tf_file in sorted(files):
            if globals.debug:
                buffer.write(f"# Source: {tf_file}\n")
            with open(tf_file, 'r') as infile:
                buffer.write(infile.read())
            buffer.write('\n\n')
        
        outfile.write(buffer.getvalue())  


def apl_threaded(rn):
    client = boto3.client('iam') 
    response=[]
    
    try:
        response=client.list_attached_role_policies(RoleName=rn)
    except Exception as e:  
        print(f"{e=}")
    #print(str(response)+"\n")
    if response['AttachedPolicies'] == []: 
        globals.attached_role_policies_list[rn]=False
    #else:
    #    globals.attached_role_policies_list[rn]=response['AttachedPolicies']


def dd_threaded(ti):
    if not globals.rproc[ti]:
        i = ti.split(".")[0]
        id = ti.split(".", 1)[1]
        if globals.debug: print("DD calling getresource with type="+i+" id="+str(id))
        globals.tracking_message="Stage 5 of 10, Processing Dependancy, "+str(i)+" "+str(id)
        common.call_resource(i, id)

    return


def kd_threaded(ti):
    if not globals.rdep[ti]:
        i = ti.split(".")[0]
        id = ti.split(".")[1]
        if globals.debug: print("type="+i+" id="+str(id))
        common.call_resource(i, id)
    return


#if __name__ == '__main__':

def main():

    now = datetime.datetime.now()
    print("aws2tf started at %s" % now)
    starttime=now
   

    #print("cwd="+str(sys.argv),str(len(sys.argv)))
    if len(sys.argv) > 1:
        if sys.argv[1]=="-h": timed_interrupt.timed_int.stop() 

    argParser = argparse.ArgumentParser()
    argParser.add_argument("-l", "--list",help="List extra help information" , action='store_true')
    argParser.add_argument("-t", "--type", help="resource type aws_s3, ec2 aws_vpc etc")
    argParser.add_argument("-i", "--id", help="resource id")
    argParser.add_argument("-r", "--region", help="region")
    argParser.add_argument("-p", "--profile", help="profile")
    argParser.add_argument("-m", "--merge", help="merge", action='store_true')
    argParser.add_argument("-d", "--debug", help="debug", action='store_true')
    argParser.add_argument("-s", "--singlefile", help="only a single file main.tf is produced", action='store_true')
    argParser.add_argument("-f", "--fast", help="fast multi-threaded mode", action='store_true')
    argParser.add_argument("-v", "--validate", help="validate and exit", action='store_true')
    argParser.add_argument("-a", "--accept", help="expected plan changes accepted", action='store_true')
    argParser.add_argument("-e", "--exclude", help="resource types to exclude")
    argParser.add_argument("-ec2tag", "--ec2tag", help="ec2 key:value pair to import")
    argParser.add_argument("-dnet", "--datanet", help="write data statements for aws_vpc, aws_subnet",action='store_true')
    argParser.add_argument("-dsgs", "--datasgs", help="write data statements for aws_security_groups",action='store_true')
    argParser.add_argument("-dkms", "--datakms", help="write data statements for aws_kms_key",action='store_true')
    argParser.add_argument("-dkey", "--datakey", help="write data statements for aws_key_pair",action='store_true')
    argParser.add_argument("-b3", "--boto3error", help="exit on boto3 api error (for debugging)", action='store_true')
    argParser.add_argument("-la", "--serverless", help="Lambda mode - when running in a Lambda container", action='store_true')
    argParser.add_argument("-tv", "--tv", help="Specify version of Terraform AWS provider default = "+globals.tfver)
    args = argParser.parse_args()
    type=""

    common.check_python_version()
    # print("cwd=%s" % os.getcwd())
    signal.signal(signal.SIGINT, common.ctrl_c_handler)

    path = shutil.which("terraform") 

    if path is None:
        print("no executable found for command 'terraform'")
        print("exit 002")
        timed_interrupt.timed_int.stop()
        exit()

    # check terraform version
    
    com = "terraform version"
    rout = common.rc(com)
    tvr=rout.stdout.decode().rstrip()
    if "." not in tvr:
        print("Unexpected Terraform version "+str(tvr))
        timed_interrupt.timed_int.stop()
        os._exit(1)                                      
    tv=str(rout.stdout.decode().rstrip()).split("rm v")[-1].split("\n")[0]
    tvmaj=int(tv.split(".")[0])
    tvmin=int(tv.split(".")[1])
    
    if tvmaj < 1:
        print("Terraform version is too old - please upgrade to v1.9.5 or later "+str(tv))
        timed_interrupt.timed_int.stop()
        os._exit(1) 
    if tvmaj==1 and tvmin<8:                                      
        print("Terraform version is too old - please upgrade to v1.9.5 or later "+str(tv))
        timed_interrupt.timed_int.stop()
        os._exit(1)
    print("Terraform version",tv)

    globals.expected=args.accept

    # print("args=%s" % args)
    
    # print("args.bucket=%s" % args.bucket)
    # print("args.type=%s" % args.type)
    # print("args.id=%s" % args.id)
    globals.merge=args.merge

    if args.list: extra_help()
    if args.fast: globals.fast = True
    if args.debug: 
        globals.debug = True
        globals.fast = False

    if args.profile: 
        globals.profile = args.profile

    if args.tv:
        globals.tfver=args.tv

    if args.ec2tag:
        isinv=True
        if args.ec2tag!="" and ":" in args.ec2tag:
            isinv=False             
            #args.ec2tag = args.ec2tag[1:-1]
            globals.ec2tag=args.ec2tag
            globals.ec2tagk=globals.ec2tag.split(":")[0]
            globals.ec2tagv=globals.ec2tag.split(":")[1]
        else:
            isinv=True
        
        if isinv:
            #if len(globals.ec2tagk) < 1 or len(globals.ec2tagv) < 1:
            print("ec2tag must be in format (with quotes) \"key:value\"")
            print("exit 005")
            timed_interrupt.timed_int.stop()
            exit()


    if args.validate: 
        globals.validate = True

    if args.datanet:  globals.dnet = True
    if args.datasgs:  globals.dsgs = True
    if args.datakms:  globals.dkms = True
    if args.datakey:  globals.dkey = True

    if args.type is None or args.type=="":
        if args.serverless:
            print("type is required eg:  -t aws_vpc  when in serverless mode, exiting ....")
            print("exit 003")
            timed_interrupt.timed_int.stop()
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
                        print("exit 004")
                        timed_interrupt.timed_int.stop()
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
        if args.profile is None:
            boto3.setup_default_session(region_name=region)
        else:
            boto3.setup_default_session(region_name=region,profile_name=globals.profile)
    except Exception as e: 
        print("AWS Authorization Error: "+str(e))
      
    if globals.debug: print("getting account")
    try:
        globals.acc = boto3.client('sts').get_caller_identity().get('Account')
        print("account="+globals.acc)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        exn=str(exc_type.__name__)
        
        if "ExpiredToken" in str(e):
            print("STS Authorization Error: ExpiredToken, exiting .....")
            
        elif "EndpointConnectionError" in exn:
            print("Failed to connect to AWS - check network connectivity, exiting .....")
            
        else:
            print(str(e))
            print(str(exn))
        timed_interrupt.timed_int.stop()
        exit()
    print('Using region: '+region + ' account: ' + globals.acc+ " profile: "+globals.profile+"\n")
####  restore form S3 if merging & serverless

####    

    globals.region = region
    globals.regionl = len(region)
    if args.serverless:     
        globals.serverless=True
        globals.path1="/tmp/aws2tf/generated/tf-"+globals.acc+"-"+region
        globals.path2=globals.path1+"/imported"
        globals.path3=globals.path1+"/notimported"
    else:
        globals.serverless=False
        globals.path1="generated/tf-"+globals.acc+"-"+region
        globals.path2=globals.path1+"/imported"
        globals.path3=globals.path1+"/notimported"

    if globals.serverless:
        if args.merge: common.download_from_s3()
        else: common.empty_and_delete_bucket()


    if globals.merge is False:
        com = "rm -rf "+globals.path1
        rout = common.rc(com)
        if globals.serverless: common.empty_and_delete_bucket()


    com = "mkdir -p "+globals.path2
    rout = common.rc(com)

    com = "mkdir -p "+globals.path3
    rout = common.rc(com)

    globals.cwd=os.getcwd()
    os.chdir(globals.path1) 
    globals.tracking_message="Stage 1 of 10, Terraform Initialise ..."
    common.aws_tf(region,args)

    # check we have it
    foundtf=False
    for root, dirs, files in os.walk(globals.cwd+"/"+globals.path1):
        if '.terraform' in dirs:
            print("PASSED: Terraform Initialise OK")
            foundtf=True
            break

    if not foundtf:
        print("Terraform Initialise may have failed...")
        timed_interrupt.timed_int.stop()
        exit()


    if args.merge:
        print("Merging "+str(globals.merge))
        #print("Merging capability disabled for now - exiting")
        #exit()
        try:
            with open('pyprocessed.txt', 'r') as file:
                # Your file operations here
                content = file.readlines()
                # Process content as needed


            for line in content:
                globals.rproc[line] = True
                
            if globals.debug:
                print("Pre Processed:")
                for i in globals.rproc.keys():   print(i)

                com = "rm -f main.tf"
                rout = common.rc(com) 
                com = "cp imported/*.tf ."
                rout = common.rc(com) 

        except FileNotFoundError:
            print("Could not find pyprocessed.txt")
        except IOError as e:
            print(f"IO error occurred: {str(e)}")   

    id = args.id


#### setup
    st1 = datetime.datetime.now()
    print("build lists started at %s" % now)
    build_lists()
    now = datetime.datetime.now()
    print("build lists finished at %s" % now)
    print("build lists took %s" % (now - st1))
    #print(str(globals.attached_role_policies_list))
    #for k,v in globals.attached_role_policies_list.items():
    #    print(k,v)
    
    if type == "" or type is None: type = "all"
    
    print("---<><> "+ str(type),"Id="+str(id)," exclude="+str(globals.all_extypes))  

################# -- now we are calling ----   ###############################
    globals.tracking_message="Stage 3 of 10 getting resources ..."


    if "," in type:
        if "stack" in type:
            print("Cannot mix stack with other types")
            print("exit 006")
            timed_interrupt.timed_int.stop()
            exit()

        if id is not None:
            print("Cannot pass id with multiple types")
            print("exit 007")
            timed_interrupt.timed_int.stop()
            exit()

        #if globals.serverless:
        #    print("Cannot pass multiple types when running on serverless")
        #    exit()

        types = type.split(",")
        all_types = []
        for type1 in types: 
            if type1.startswith("aws_"): all_types = all_types + resources.resource_types(type1)

        for type2 in all_types:
            if type2 in aws_dict.aws_resources:   
                if type2 in globals.all_extypes:
                    print("Excluding", type2) 
                    continue                 
                common.call_resource(type2, id)
            else:
                print("Resource",type2," not found in aws_dict")
        
    else:
        if type=="all" and id is not None:
            print("Cannot pass an id (-i) with all types")
            print("exit 007")
            timed_interrupt.timed_int.stop()
            exit()
        all_types = resources.resource_types(type)

        try:
            lall=len(all_types)
        except:
            lall=0

        if all_types is None: print("No resources found all_types=None")
        print("all_types="+str(all_types))

        if type == "stack":
            
            if id is None:
                print("Must pass a stack name as a parameter   -i <stack name>")
                print("exit 008")
                timed_interrupt.timed_int.stop()
                exit()
            else:
                globals.tracking_message="Stage 3 of 10 getting stack " +id+" resources ..."
                globals.expected=True
                stacks.get_stacks(id)
        
        elif type.startswith("aws_"):
            if type in aws_dict.aws_resources:
                if type in globals.all_extypes:
                    print("Excluding type", type) 
                else:    
                    common.call_resource(type, id)
            else:
                print("Resource",type," not found in aws_dict")

        
################
        
        elif all_types is not None and lall > 1:
            #all_types=all_types[:10]
            print("len all_types="+str(len(all_types))) # testing only
            #print("all_types="+str(all_types))
            if "aws_iam" in str(all_types) and id is None:
                print("INFO: Building secondary lists",id)
                build_secondary_lists(id)

            
            globals.esttime=len(all_types)/4
            #id="foobar" # testing only
            #print("------------------1-------------------------------------------")
            ic=0
            istart=0
            it=len(all_types)

            globals.expected=True
            
            if globals.fast:
                globals.tracking_message="Stage 3 of 10 getting "+str(it)+" resources multi-threaded"
                with ThreadPoolExecutor(max_workers=globals.cores) as executor:
                    futures = [
                        executor.submit(common.call_resource, i, id)
                        for i in all_types
                    ]
                    #return [f.result() for f in futures]     
            else:
                for i in all_types:
                    ic=ic+1
                    if ic > it: break 
                    if ic < istart: continue
                    
                    if globals.debug: print(str(ic)+" of "+str(it) +"\t"+i)
                    globals.tracking_message="Stage 3 of 10, "+ str(ic)+" of "+str(it) +" resource types \t currently getting "+i
                    common.call_resource(i, id)
                                
        else:
            if all_types is not None:
                for type in all_types:
                    if type in aws_dict.aws_resources:
                        common.call_resource(type,id)
                    else:
                        print("Resource",type," not found in aws_dict")
            else:
                print("No resources found")
                globals.tracking_message="Stage 3 of 10 no resources found exiting ..."
                print("exit 009")
                timed_interrupt.timed_int.stop()
                exit()

#########################################################################################################################
## Known dependancies section
 #########################################################################################################################   

    globals.tracking_message="Stage 4 of 10, Known Dependancies"
    print("Known Dependancies - Multi Threaded")
    if globals.fast:
        globals.tracking_message="Stage 4 of 10, Known Dependancies - Multi Threaded "+str(globals.cores)
        with ThreadPoolExecutor(max_workers=globals.cores) as executor12:
            futures2 = [
                executor12.submit(kd_threaded(ti))
                for ti in list(globals.rdep)
            ]     

    else:
        for ti in list(globals.rdep):
            if not globals.rdep[ti]:
                i = ti.split(".")[0]
                id = ti.split(".")[1]
                if globals.debug: print("type="+i+" id="+str(id))
                common.call_resource(i, id)
    #else:
    #    print("No Known Dependancies")
    globals.tracking_message="Stage 4 of 10, Known Dependancies: terraform plan"
    common.tfplan1()
    globals.tracking_message="Stage 4 of 10, Known Dependancies: moving files"
    common.tfplan2()
    
    
    # Detected deps
    
    if ":" in globals.rproc:
        print(": in rproc exiting")
        print("exit 010")
        timed_interrupt.timed_int.stop()
        exit()
    now = datetime.datetime.now()
    x=glob.glob("import__aws_*.tf")
    globals.esttime=len(x)/4
    if not globals.fast: print("\naws2tf Detected Dependancies started at %s\n" % now)
    globals.tracking_message="Stage 5 of 10, Detected Dependancies: starting"
    detdep=False
    for ti in globals.rproc.keys():
        if not globals.rproc[ti]: 
            #print(str(ti)+":"+str(globals.rproc[ti]))  
            if globals.debug: print(str(ti)) 
            detdep=True
            
    if not detdep: print("No Detected Dependancies") 

    lc=0
    olddetdepstr=""
    detdepstr=""

    while detdep:
        
## mutlithread ?  
        if globals.fast:  
            globals.tracking_message="Stage 5 of 10, Detected Dependancies: Multi Threaded "+str(globals.cores)
            with ThreadPoolExecutor(max_workers=globals.cores) as executor2:
                futures2 = [
                    executor2.submit(dd_threaded(ti))
                    for ti in list(globals.rproc)
                ]

        else:
            for ti in list(globals.rproc):
                if not globals.rproc[ti]:
                    i = ti.split(".")[0]
                    id = ti.split(".", 1)[1]
                    if globals.debug: print("DD calling getresource with type="+i+" id="+str(id))
                    #print("----- DD ----  calling getresource with type="+i+" id="+str(id))
                    common.call_resource(i, id)   
        
        detdep=False
        lc  = lc + 1

# go again plan and split / fix
        if not globals.fast: print("Terraform Plan - Dependancies Detection Loop "+str(lc)+".....")
        globals.tracking_message="Stage 6 of 10, Dependancies Detection: Loop "+str(lc)
        x=glob.glob("import__aws_*.tf")
        globals.esttime=len(x)/4
        #print(str(x))
        #td=""
        for fil in x:
            tf=fil.split('__',1)[1]
            #td=td+" "+tf

            com = "mv "+tf +" imported/"+tf
            rout = common.rc(com)

        globals.tracking_message="Stage 6 of 10, Dependancies Detection: Loop "+str(lc)+" terraform plan"
        common.tfplan1()
        globals.tracking_message="Stage 6 of 10, Dependancies Detection: Loop "+str(lc)+" moving files"
        common.tfplan2()
 
        detdepstr=""
        for ti in globals.rproc.keys():
            if not globals.rproc[ti]:
                detdep=True 
                #print(str(ti)+" is False")
                detdepstr=detdepstr+str(ti)+" "

        if not globals.fast: print("\n----------- Completed "+str(lc)+" dependancy check loops --------------") 
        globals.tracking_message="Stage 6 of 10, Completed "+str(lc)+" dependancy check loops"
        if olddetdepstr == detdepstr and detdepstr != "":
            globals.tracking_message="No change/progress in dependancies exiting..."
            print("\nERROR: No change/progress in dependancies exiting... \n")
            for ti in globals.rproc.keys():
                if not globals.rproc[ti]:
                    print("ERROR: Not found "+str(ti)+" - check if this resource still exists in AWS. Also check what resource is using it - grep the *.tf files in the generated/tf.* subdirectory")
                    globals.tracking_message="No change/progress in dependancies exiting..."
            print("exit 011")
            timed_interrupt.timed_int.stop()
            exit()

        olddetdepstr=detdepstr

    common.tfplan3()
    if globals.validate is False: 
        now = datetime.datetime.now()
        print("aws2tf wrap up started at %s" % now)
        common.wrapup()
    else: 
        print("\nValidation only - no files written")
        print("exit 012")
        timed_interrupt.timed_int.stop()
        exit()

##########################################################################
####### Finish up
#########################################################################
    globals.tracking_message="Stage 10 of 10, Completed"

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
        globals.esttime=len(x)/4
        awsf=len(x)
        if awsf < 256:
            globals.tracking_message="Running trivy security check"
            print("\nRunning trivy security check .....")
            common.trivy_check()

        else:
            print("\nSkipping security check - too many files.")
            print("Use trivy manually if required")
    else:
        print("trivy not installed, skipping security check")

    if globals.serverless: common.upload_directory_to_s3()

    x = glob.glob("*.err")
    awsf=len(x)
    if awsf > 0:
        print("\nErrors found - see *.err files, and please report via github issue")   


    if args.singlefile:
        print("Single file mode .....")
        #globals.tracking_message="Single file mode - merging"
        tf_files = glob.glob("aws_*__*.tf")
        if not tf_files:
            print("No aws_*.tf files found")
        else:
            process_file_operations(tf_files, 'main.tf')
        print(f"Successfully merged {len(tf_files)} files into main.tf")
        com = "mv aws_*__*.tf imported"
        rout = common.rc(com)
    
    globals.tracking_message="aws2tf, Completed"
    now = datetime.datetime.now()
    print("aws2tf started at  %s" % starttime)
    #print("aws2tf finished at %s" % now)
    # print execution time
    print("aws2tf execution time h:mm:ss :"+ str(now - starttime))
    print("\nTerraform files & state in sub-directory: "+ globals.path1)
    timed_interrupt.timed_int.stop()

    exit(0)


if __name__ == '__main__':
    main()
