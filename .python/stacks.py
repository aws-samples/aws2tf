import boto3
import os
import globals
import aws2tf
import s3

def getstack(stack_name,nested,client):
    print("have client for stack "+stack_name)
    try:
        resp = client.describe_stack_resources(StackName=stack_name)
        response=resp['StackResources']
    except Exception as e:
        print(f"{e=}")
        print("-1->unexpected error in getstack")
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        exit()


    for j in response:
      
        type=j['ResourceType']
        stat=j['ResourceStatus']
        
        if type == "AWS::CloudFormation::Stack":
            if stat == "CREATE_COMPLETE":
                print(type+' '+stat)
                stackr=j['PhysicalResourceId']
                print("--> adding"+ stackr +"to nested")
                nested=nested+[stackr]
    
    return nested


def getstackresources(stack_name,client):
    try:
        resp = client.describe_stack_resources(StackName=stack_name)
        response=resp['StackResources']
    except Exception as e:
        print(f"{e=}")
        print("-1->unexpected error in getstack")
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        exit()
    ri=0
    rl=len(response)
    with open('unprocessed.log', 'a') as f:
        for j in response:
      
            type=j['ResourceType']
            pid=j['PhysicalResourceId'].split('/')[-1]
            parn=j['PhysicalResourceId']
            lrid=j['LogicalResourceId']
            stat=j['ResourceStatus']
            ri=ri+1

            if globals.debug:
                print("type="+type)
            
            print("stack "+stack_name+ " importing "+ str(ri) + " of "+ str(rl)+ " type="+type+ " pid="+pid)


            if type == "AWS::CloudFormation::Stack": continue
            elif "AWS::CloudFormation::WaitCondition" in type: f.write("skipping "+type+"\n")
            elif type == "AWS::ApiGateway::Account":        print("Error: **Terraform does not support import of "+ type +" skipped**")
            elif type == "AWS::EC2::Instance":              aws2tf.call_resource("aws_null", pid) 
            elif type == "AWS::EC2::KeyPair":               aws2tf.call_resource("aws_null", pid) 
            elif type == "AWS::EC2::DHCPOptions":           aws2tf.call_resource("aws_null", pid) 
            elif type == "AWS::EC2::EIP":                   aws2tf.call_resource("aws_null", pid) 
            elif type == "AWS::EC2::NatGateway":            aws2tf.call_resource("aws_nat_gateway", pid) 
            elif type == "AWS::EC2::NetworkAcl":            aws2tf.call_resource("aws_null", pid) 
            elif type == "AWS::EC2::NetworkAclEntry":       f.write(type +" fetched as part of NetworkAcl..\n")
            elif type == "AWS::EC2::SubnetNetworkAclAssociation": f.write(type +" fetched as part of NetworkAcl..\n")
            elif type == "AWS::EC2::InternetGateway":       aws2tf.call_resource("aws_internet_gateway", pid) 
            elif type == "AWS::EC2::LaunchTemplate":        aws2tf.call_resource("aws_null", pid) 
            elif type == "AWS::EC2::SecurityGroup":         aws2tf.call_resource("aws_security_group", pid) 
            elif type == "AWS::EC2::SecurityGroupIngress":  f.write(type +" fetched as part of SecurityGroup..\n")
            elif type == "AWS::EC2::VPCEndpoint":           aws2tf.call_resource("aws_null", pid) 
            elif type == "AWS::EC2::VPC":                   aws2tf.call_resource("aws_vpc", pid) 
            elif type == "AWS::EC2::Subnet":                aws2tf.call_resource("aws_subnet", pid) 
            elif type == "AWS::EC2::RouteTable":            aws2tf.call_resource("aws_route_table", pid) 
            elif type == "AWS::EC2::Route":                     f.write(type +" fetched as part of RouteTable...\n")
            elif type == "AWS::EC2::SubnetRouteTableAssociation": f.write(type +" fetched as part of Subnet...\n")
            elif type == "AWS::EC2::VPCGatewayAttachment":      f.write(type +" fetched as part of IGW...\n")
            elif type == "AWS::EC2::VPCEndpointService":        aws2tf.call_resource("aws_null", pid) 
            elif type == "AWS::EC2::FlowLog":                   aws2tf.call_resource("aws_null", pid) 


            elif type == "AWS::EKS::Cluster":                   aws2tf.call_resource("aws_eks_cluster", pid)


            elif type == "AWS::IAM::Role":                      aws2tf.call_resource("aws_iam_role", pid)
            elif type == "AWS::IAM::Policy":                    f.write(type +" fetched as part of Role etc ...\n")


            elif type == "AWS::S3::Bucket":                     s3.get_all_s3_buckets(pid, globals.region)
            elif type == "AWS::S3::BucketPolicy":               f.write(type +" fetched as part of bucket...\n")

            else:
                f.write("--UNPROCESSED-- "+type + " "+ pid +" "+ parn+" \n")

    return

def get_stacks(stack_name):
    client = boto3.client('cloudformation')
    nested=[]
    print("level 1 nesting")
    nested=getstack(stack_name,nested,client)

    print("level 2 nesting")
    for nest in nested:
        if nest != stack_name:
            print(nest)
            getstack(nest,nested)

    if stack_name not in (str(nested)):
        nested=nested+[stack_name]
 

    print("Stacks Found:")
    for nest in nested:
        print(nest)

    for nest in nested:
        print("getting stack resources for " + nest)
        getstackresources(nest,client)
    
    print("stack "+stack_name+" done")

