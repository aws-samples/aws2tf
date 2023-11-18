#!/usr/bin/env python3
import boto3
import signal
import argparse
import s3
import common
import resources
import globals


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
            getfn = getattr(common, "get_"+type)
            getfn(type, id, clfn, descfn, topkey, key, filterid)
        except Exception as e:
                # By this way we can know about the type of error occurring
                print(f"{e=}")
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
        com = "rm -f terraform.tfstate* aws_*.tf s3-*.tf tfplan *.out import*.tf imported/* main.tf"
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

# -- now we are calling ----

    if type == "s3":
        com = "rm -f s3-*.tf s3.tf tfplan *s3*.out"
        rout = common.rc(com)
        s3.get_all_s3_buckets(fb, region)

    elif type == "net":
        all_types = resources.resource_types(type)
        for i in all_types:
            # print("calling "+i)
            clfn, descfn, topkey, key, filterid = resources.resource_data(
                i, id)
            # print("calling getresource with type="+i+" id="+str(id)+"   clfn="+clfn+" descfn="+str(descfn)+" topkey="+topkey + "  key="+key +"  filterid="+filterid)
            common.getresource(i, id, clfn, descfn, topkey, key, filterid)

        # special case for route tables:
        clfn = "ec2"
        descfn = "describe_route_tables"
        topkey = "RouteTables"
        key = "Associations"
        filterid = key
        if id is not None and "vpc-" in id:
            filterid = ".Associations.0.SubnetId"
        if id is not None and "subnet-" in id:
            filterid = ".Associations.0.SubnetId"
        # call s special: once (if subnet in processed or igw)
        i = "aws_route_table_association"
        common.get_aws_route_table_association(
            i, id, clfn, descfn, topkey, key, filterid)

    elif type == "iam" or type == "lattice":
        all_types = resources.resource_types(type)
        for i in all_types:
            if globals.debug:
                print("calling "+i)
            try:
                clfn, descfn, topkey, key, filterid = resources.resource_data(
                    i, id)
                if globals.debug:
                    print("calling getresource with type="+i+" id="+str(id)+"   clfn="+clfn +
                          " descfn="+str(descfn)+" topkey="+topkey + "  key="+key + "  filterid="+filterid)
                common.getresource(i, id, clfn, descfn, topkey, key, filterid)
            except Exception as e:
                # By this way we can know about the type of error occurring
                print(f"{e=}")
                pass
            try:
                getfn = getattr(common, "get_"+i)
                getfn(i, id, clfn, descfn, topkey, key, filterid)
            except:
                pass

        # clfn="iam"
        # descfn="list_role_policies"
        # topkey="PolicyNames"
        # key="PolicyNames"
        # filterid="RoleName"

        # common.get_aws_iam_role_policy(i,id,clfn,descfn,topkey,key,filterid)

    # calling by direct terraform type aws_xxxxx
    else:
        call_resource(type,id)


    print("Known Dependancies ----------------------")

    # lattice
    for j in globals.rproc.keys():
        if "aws_vpclattice_service_network" in j:

            id = str(j.split(".")[1])
            print(id)
            # ../../scripts/get-vpclattice-auth-policy.sh $cname
            # ../../scripts/get-vpclattice-resource-policy.sh $rarn
            # ../../scripts/get-vpclattice-service-network-service-associations.sh $cname
            # ../../scripts/get-vpclattice-service-network-vpc-association.sh $cname
            # ../../scripts/get-vpclattice-access-log-subscription.sh $cname
            # ../../scripts/get-vpclattice-services.sh $cname

            # for type in ["aws_vpclattice_service"]:
            for type in ["aws_vpclattice_service", "aws_vpclattice_service_network_vpc_association"]:
                print(type)
                clfn, descfn, topkey, key, filterid = resources.resource_data(
                    type, id)
                try:
                    get_fn = getattr(common, "get_"+type)
                    print("calling get_aws_vpclattice_service with type="+type+" id="+str(id)+"   clfn=" +
                          clfn+" descfn="+str(descfn)+" topkey="+topkey + "  key="+key + "  filterid="+filterid)
                    get_fn(type, id, clfn, descfn, topkey, key, filterid)
                except Exception as e:
                    # By this way we can know about the type of error occurring
                    print(f"{e=}")
                    pass

## Known dependancies section
    for ti in globals.rdep.keys():
        if not globals.rdep[ti]:
            i = ti.split(".")[0]
            id = ti.split(".")[1]
            print("KD calling getresource with type="+i+" id="+str(id))
            call_resource(i, id)



# Known dependancies section
# role attachments
# not needed - managed_policy_arns in aws_iam_role handles it
#    i="aws_iam_role_policy_attachment"
#    for j in globals.rproc.keys():
#        if "aws_iam_role" in j:
#            id=str(j.split(".")[1])
#            try:
#                clfn,descfn,topkey,key,filterid=resources.resource_data(i,id)
#                if globals.debug:
#                    print("KD calling common.get_aws_iam_policy_attchment with type="+i+" id="+str(id)+"   clfn="+clfn+" descfn="+str(descfn)+" topkey="+topkey + "  key="+key +"  filterid="+filterid)
#                else:
#                    print(i+"."+id)
#                common.get_aws_iam_policy_attchment(i,id,clfn,descfn,topkey,key,filterid)
#
#            except Exception as e:
#                # By this way we can know about the type of error occurring
#                print(f"{e=}")
#                print("failed")

    for ti in globals.dependancies:
        if "arn:aws:iam::aws:policy" not in ti:
            if str(ti) not in globals.rproc:
                print("KD="+str(ti))
                i = ti.split(".")[0]
                id = ti.split(".")[1]
                if id not in str(globals.policyarns):
                    try:
                        clfn, descfn, topkey, key, filterid = resources.resource_data(
                            i, id)
                        print("DD calling getresource with type="+i+" id="+str(id)+"   clfn="+clfn +
                              " descfn="+str(descfn)+" topkey="+topkey + "  key="+key + "  filterid="+filterid)
                        common.getresource(
                            i, id, clfn, descfn, topkey, key, filterid)
                    except:
                        pass
                    try:
                        getfn = getattr(common, "get_"+i)
                        print("DD calling common.get_"+i+" with type="+i+" id="+str(id)+"   clfn="+clfn +
                              " descfn="+str(descfn)+" topkey="+topkey + "  key="+key + "  filterid="+filterid)

                        getfn(i, id, clfn, descfn, topkey, key, filterid)
                    except Exception as e:
                        # By this way we can know about the type of error occurring
                        print(f"{e=}")
                else:
                    print("DD skip found "+id+" in globals.policyarns")

    common.tfplan1()
    common.tfplan2()

    for i in globals.rproc.keys():
        print(str(i)+ " : "+str(globals.rproc[i]))


    print("Detected Dependancies -----------------------")
    detdep=True
    while detdep:
        for ti in globals.rproc.keys():
            if not globals.rproc[ti]:
                i = ti.split(".")[0]
                id = ti.split(".")[1]
                print("DD calling getresource with type="+i+" id="+str(id))
                call_resource(i, id)
        detdep=False
# go again plan and split / fix
        com = "rm -f aws_*.tf *.out"
        rout = common.rc(com)
        common.tfplan1()
        common.tfplan2()
        for ti in globals.rproc.keys():
            print(str(ti)+":"+str(globals.rproc[ti]))

        for ti in globals.rproc.keys():
            if not globals.rproc[ti]:
                detdep=True


    print("Processed --------------------")

    common.tfplan3()

    common.wrapup()

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

    exit(0)



