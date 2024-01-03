import boto3
import os
import sys
import globals
import common
import aws_s3
import botocore


def get_stacks(stack_name):
    client = boto3.client('cloudformation')
    nested=[]
    print("Level 1 stack nesting")
    nested=getstack(stack_name,nested,client)

    if nested is not None:
        print("Level 2 stack nesting")
        for nest in nested:
            if nest != stack_name:
                print(nest)
                getstack(nest,nested,client)

        print("-------------------------------------------")

        for nest in nested:
            print("Getting stack resources for " + nest)
            getstackresources(nest,client)
        
        print("Stack "+stack_name+" done")



def getstack(stack_name,nested,client):
    try:
        resp = client.describe_stack_resources(StackName=stack_name)
        response=resp['StackResources']
    
    except botocore.exceptions.ClientError as err:
        print("ValidationError error in getstack")
        print("Stack "+stack_name+" may not exist in region "+globals.region)
        return
    
    
    except Exception as e:
        print(f"{e=}")
        print("-1->unexpected error in getstack")
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return


    for j in response:
        type=j['ResourceType']
        stat=j['ResourceStatus']
        stacki=j['StackId']
        if stacki not in (str(nested)):
            nested=nested+[stacki]
            #print("--> adding "+ stacki +" to nested")
        
        if type == "AWS::CloudFormation::Stack":
            if stat == "CREATE_COMPLETE":
                #print(type+' '+stat)
                stackr=j['PhysicalResourceId']
                if stackr not in (str(nested)):
                    nested=nested+[stackr]
                    #print("--> adding "+ stackr +" to nested")
   
    
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
    with open('stack-unprocessed.log', 'a') as f:
        for j in response:
            f3=open('stack-fetched.log', 'a')
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

            elif type == "AWS::ApiGateway::Account": f3.write("Error: **Terraform does not support import of $type skipped**\n") 
            elif type == "AWS::ApiGateway::RestApi": common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::ApiGateway::Resource": f3.write(type+" "+pid+"  as part of RestApi..' ") 

            elif type == "AWS::ApplicationAutoScaling::ScalableTarget": f3.write(type+" "+pid+"  as part of parent recources ' ") 
            elif type == "AWS::ApplicationAutoScaling::ScalingPolicy": f3.write(type+" "+pid+"  as part of parent recources ' ") 

            elif type == "AWS::AppMesh::Mesh":  common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::AppMesh::VirtualGateway": f3.write(type+" "+pid+"  as part of parent mesh ' ") 
            elif type == "AWS::AppMesh::VirtualNode": f3.write(type+" "+pid+"  as part of parent mesh ' ") 
            elif type == "AWS::AppMesh::VirtualRouter": f3.write(type+" "+pid+"  as part of parent mesh ' ") 
            elif type == "AWS::AppMesh::VirtualService": f3.write(type+" "+pid+"  as part of parent mesh ' ") 

            elif type == "AWS::Athena::NamedQuery":  common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::Athena::WorkGroup":  common.call_resource("aws_null", type+" "+pid) 

            elif type == "AWS::AutoScaling::AutoScalingGroup":  common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::AutoScaling::LaunchConfiguration":  common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::AutoScaling::LifecycleHook": f3.write(type+" "+pid+" as part of AutoScalingGroup..\n") 

            elif type == "AWS::CDK::Metadata": f3.write(type+" "+pid+" skipped only relevant to CDK .. \n") 

            elif type == "AWS::Cloud9::EnvironmentEC2":  common.call_resource("aws_null", type+" "+pid) 

            elif type == "AWS::CloudWatch::Alarm": common.call_resource("aws_null", type+" "+parn) 

            elif type == "AWS::ApiGateway::Account":        print("Error: **Terraform does not support import of "+ type +" skipped**")
            elif type == "AWS::EC2::Instance":              common.call_resource("aws_instance", pid) 
            elif type == "AWS::EC2::KeyPair":               common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::EC2::DHCPOptions":           common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::EC2::EIP":                   common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::EC2::NatGateway":            common.call_resource("aws_nat_gateway", pid) 
            elif type == "AWS::EC2::NetworkAcl":            common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::EC2::NetworkAclEntry":       f3.write(type +" fetched as part of NetworkAcl..\n")
            elif type == "AWS::EC2::SubnetNetworkAclAssociation": f.write(type +" fetched as part of NetworkAcl..\n")
            elif type == "AWS::EC2::InternetGateway":       common.call_resource("aws_internet_gateway", pid) 
            elif type == "AWS::EC2::LaunchTemplate":        common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::EC2::SecurityGroup":         common.call_resource("aws_security_group", pid) 
            elif type == "AWS::EC2::SecurityGroupIngress":  f3.write(type +" fetched as part of SecurityGroup..\n")
            elif type == "AWS::EC2::VPCEndpoint":           common.call_resource("aws_vpc_endpoint", pid) 
            elif type == "AWS::EC2::VPC":                   print("****>"+pid);common.call_resource("aws_vpc", pid) 
            elif type == "AWS::EC2::Subnet":                common.call_resource("aws_subnet", pid) 
            elif type == "AWS::EC2::RouteTable":            common.call_resource("aws_route_table", pid) 
            elif type == "AWS::EC2::Route":                     f3.write(type +" fetched as part of RouteTable...\n")
            elif type == "AWS::EC2::SubnetRouteTableAssociation": f3.write(type +" fetched as part of Subnet...\n")
            elif type == "AWS::EC2::VPCGatewayAttachment":      f3.write(type +" fetched as part of IGW...\n")
            elif type == "AWS::EC2::VPCEndpointService":        common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::EC2::FlowLog":                   common.call_resource("aws_null", type+" "+pid) 

            elif type == "AWS::ECR::Repository": common.call_resource("aws_null", type+" "+pid) 

            elif type == "AWS::ECS::Cluster":  common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::ECS::Service":  common.call_resource("aws_null", type+" "+parn) 
            elif type == "AWS::ECS::TaskDefinition":  common.call_resource("aws_null", type+" "+pid) 

            elif type == "AWS::EFS::FileSystem":  common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::EFS::MountTarget": f3.write(type+" "+pid+" attached as part of EFS::FileSystem ..") 
            elif type == "AWS::EFS::AccessPoint": f3.write(type+" "+pid+" attached as part of EFS::FileSystem ..'") 

            elif type == "AWS::EKS::Cluster":  common.call_resource("aws_eks_cluster", pid) 
            elif type == "AWS::EKS::Nodegroup": f3.write(type+" "+pid+"  Should be fetched via the EKS Cluster Resource") 

            elif type == "AWS::ElasticLoadBalancingV2::LoadBalancer":  common.call_resource("aws_null", type+" "+parn) 
            elif type == "AWS::ElasticLoadBalancingV2::Listener":  common.call_resource("aws_null", type+" "+parn) 
            elif type == "AWS::ElasticLoadBalancingV2::ListenerRule":  common.call_resource("aws_null", type+" "+parn) 
            elif type == "AWS::ElasticLoadBalancingV2::TargetGroup":  common.call_resource("aws_null", type+" "+parn) 

            elif type == "AWS::EMR::Cluster":  common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::EMR::SecurityConfiguration": common.call_resource("aws_null", type+" "+pid) 

            elif type == "AWS::Events::EventBus": common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::Events::Rule": common.call_resource("aws_cloudwatch_event_rule", pid)

            elif type == "AWS::Glue::Connection": common.call_resource("aws_null", type+" "+pid)
            elif type == "AWS::Glue::Crawler": common.call_resource("aws_glue_crawler", pid)
            elif type == "AWS::Glue::Database": common.call_resource("aws_glue_catalog_database", pid)
            elif type == "AWS::Glue::Job": common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::Glue::Table": f3.write(type+" "+pid+" Should be fetched via Glue Database Resource\n") 
            elif type == "AWS::Glue::Partition": f3.write(type+" "+pid+" Should be fetched via Glue Table Resource") 
            elif type == "AWS::IAM::Role":                      common.call_resource("aws_iam_role", type+" "+pid)

            elif type == "AWS::IAM::ManagedPolicy":  common.call_resource("aws_null", type+" "+parn) 
            elif type == "AWS::IAM::InstanceProfile":  common.call_resource("aws_iam_instance_profile", pid) 
            elif type == "AWS::IAM::User":  common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::IAM::AccessKey": common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::IAM::ServiceLinkedRole":  common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::IAM::Group":  common.call_resource("aws_null", type+" "+pid) 
            #elif type == "AWS::IAM::Policy)  echo "../../scripts/get-iam-policies.sh $parn" >> commands.sh ;;
            elif type == "AWS::IAM::Policy": f3.write(type+" "+pid+" Should be fetched via Roles etc\n") 

            elif type == "AWS::KinesisFirehose::DeliveryStream":  common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::Kinesis::Stream":  common.call_resource("aws_kinesis_stream", pid)
   
            elif type == "AWS::KMS::Key":  common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::KMS::Alias": f3.write(type+" "+pid+"  fetched as part of function..'")  # fetched as part of function

            elif type == "AWS::LakeFormation::DataLakeSettings":  common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::LakeFormation::Resource": common.call_resource("aws_null", type+" "+pid) 
            # pid pard can be json structures for this one
            elif type == "AWS::LakeFormation::Permissions":  common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::LakeFormation::PrincipalPermissions":  common.call_resource("aws_null", lrid) 

            elif type == "AWS::Lambda::Function":  common.call_resource("aws_lambda_function", pid) 
            elif type == "AWS::Lambda::LayerVersion":  common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::Lambda::Permission": f3.write(type+" "+pid+"  as part of function..")          # fetched as part of function
            elif type == "AWS::Lambda::EventInvokeConfig": f3.write(type+" "+pid+"  as part of function..")   # fetched as part of function
            elif type == "AWS::Lambda::EventSourceMapping": f3.write(type+" "+pid+"  as part of function..")  # fetched as part of function

            elif type == "AWS::Logs::LogGroup": common.call_resource("aws_cloudwatch_log_group", parn) 

            elif type == "AWS::RedshiftServerless::Namespace": common.call_resource("aws_redshiftserverless_namespace", pid)
            elif type == "AWS::RedshiftServerless::Workgroup": common.call_resource("aws_redshiftserverless_workgroup", pid)

            elif type == "AWS::Redshift::Cluster":  common.call_resource("aws_redshift_cluster", pid) 
            elif type == "AWS::Redshift::ClusterParameterGroup":  common.call_resource("aws_redshift_parameter_group", pid)
            elif type == "AWS::Redshift::ClusterSubnetGroup":  common.call_resource("aws_redshift_subnet_group", pid) 

            elif type == "AWS::RDS::DBCluster": common.call_resource("aws_rds_cluster", pid)
            elif type == "AWS::RDS::DBClusterParameterGroup": common.call_resource("aws_rds_cluster_parameter_group", pid)
            elif type == "AWS::RDS::DBInstance": common.call_resource("aws_db_instance", pid)   
            elif type == "AWS::RDS::DBParameterGroup":  common.call_resource("aws_db_parameter_group", pid) 
            elif type == "AWS::RDS::DBSubnetGroup": common.call_resource("aws_db_subnet_group", pid) 
            elif type == "AWS::RDS::EventSubscription":  common.call_resource("aws_db_event_subscription", pid) 


            elif type == "AWS::ServiceCatalog::PortfolioPrincipalAssociation": 
                tarn=parn.split('|')[0]
                common.call_resource("aws_null", tarn)
                

            elif type == "AWS::S3::Bucket":                     aws_s3.get_all_s3_buckets(pid, globals.region)
            elif type == "AWS::S3::BucketPolicy":               f3.write(type +" fetched as part of bucket...\n")

            elif type == "AWS::SageMaker::AppImageConfig":  common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::SageMaker::Domain":  common.call_resource("aws_null", type+" "+parn) 
            elif type == "AWS::SageMaker::Image":  common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::SageMaker::ImageVersion": f3.write(type+" "+pid+"  as part of SageMaker Image..'")  # fetched as part of function
            elif type == "AWS::SageMaker::NotebookInstance":  common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::SageMaker::UserProfile": common.call_resource("aws_null", pid)

            elif type == "AWS::SNS::Subscription":  common.call_resource("aws_null", type+" "+parn) 
            elif type == "AWS::SNS::Topic":  common.call_resource("aws_null", type+" "+parn) 
            elif type == "AWS::SNS::TopicPolicy":  common.call_resource("aws_null", type+" "+parn) 
            elif type == "AWS::SQS::Queue":  common.call_resource("aws_null", type+" "+parn) 
            elif type == "AWS::SQS::QueuePolicy": f3.write(type+" "+pid+"  as part of SQS Queue ..\n") 

            elif type == "AWS::SSM::Parameter":  common.call_resource("aws_null", type+" "+pid) 
            elif type == "AWS::ServiceDiscovery::PrivateDnsNamespace": f3.write(type+" "+pid+"  as part srv discovery ? ..\n") 
            elif type == "AWS::StepFunctions::StateMachine":  common.call_resource("aws_null", type+" "+pid) 
            #elif type == "AWS::SecretsManager::SecretTargetAttachment ;;
            elif type == "AWS::SecretsManager::Secret": common.call_resource("aws_secretsmanager_secret", parn) 
            elif type == "AWS::ServiceDiscovery::Service": common.call_resource("aws_null", type+" "+pid) 
 

            else:
                f.write("--UNPROCESSED-- "+type + " "+ pid +" "+ parn+" \n")

    f3.close()
    return



