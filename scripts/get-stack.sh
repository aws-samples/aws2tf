#!/bin/bash
if [ "$1" == "" ]; then echo "must specify a stack name" && exit; fi
nested=() 
echo "#!/bin/bash" > commands.sh
echo "Stack resources not yet implemented ...." > unprocessed.txt


getstack () {

stackr=$(aws cloudformation describe-stack-resources --stack-name $1 --query StackResources)
#echo $stackr | jq .
count=`echo $stackr | jq ". | length"`
#echo $count
if [ "$count" -gt "0" ]; then
    count=`expr $count - 1`
        for i in `seq 0 $count`; do
            type=$(echo "$stackr" | jq  -r ".[(${i})].ResourceType")
            stat=$(echo "$stackr" | jq  -r ".[(${i})].ResourceStatus")
            
            if [[ "$type" == "AWS::CloudFormation::Stack" ]];then
                if [[ "$stat" == "CREATE_COMPLETE" ]];then 
                    as=$(echo "$stackr" | jq  -r ".[(${i})].PhysicalResourceId" | cut -f2 -d'/')
                    nested+=$(printf "\"%s\" " $as)    
                fi        
            fi
        done   
fi
}

getstackresources () {
stackr=$(aws cloudformation describe-stack-resources --stack-name $1 --query StackResources)
#echo $stackr | jq .
count=`echo $stackr | jq ". | length"`
echo "Getting $count resources for stack $1"
if [ "$count" -gt "0" ]; then
    count=`expr $count - 1`
        for i in `seq 0 $count`; do
            type=$(echo "$stackr" | jq  -r ".[(${i})].ResourceType")
            pid=$(echo "$stackr" | jq  -r ".[(${i})].PhysicalResourceId" | cut -f2 -d'/')
            parn=$(echo "$stackr" | jq  -r ".[(${i})].PhysicalResourceId" | tr -d '"')
            echo "--> $type $pid $parn"
            echo "echo 'Stack $1 Importing $i of $count ..'"
            case $type in
                AWS::CodeArtifact::Domain)  echo "../../scripts/627-get-code-artifact-domain.sh $pid"  >> commands.sh ;;
                AWS::CodeArtifact::Repository)  echo "../../scripts/627-get-code-artifact-repository.sh $pid"  >> commands.sh ;;
                
                AWS::Cognito::IdentityPool) echo "../../scripts/770-get-cognito-identity-pools.sh $pid"  >> commands.sh ;;
                AWS::Cognito::IdentityPoolRoleAttachment) echo "echo '# $type $pid fetched as part of Identity pool..' " >> commands.sh ;;
                AWS::Cognito::UserPool) echo "../../scripts/775-get-cognito-user-pools.sh $pid"  >> commands.sh ;;
                AWS::Cognito::UserPoolClient) echo "echo '# $type $pid fetched as part of User & Identity pool..' " >> commands.sh ;;
                      
                AWS::EC2::EIP)  echo "../../scripts/get-eip.sh $pid"  >> commands.sh ;;
                AWS::EC2::NatGateway)  echo "../../scripts/130-get-natgw.sh $pid"  >> commands.sh ;;
                AWS::EC2::InternetGateway)  echo "../../scripts/120-get-igw.sh $pid"  >> commands.sh ;;
                AWS::EC2::LaunchTemplate)  echo "../../scripts/eks-launch_template.sh $pid"  >> commands.sh ;;
                AWS::EC2::SecurityGroup)  echo "../../scripts/110-get-security-group.sh $pid"  >> commands.sh ;;
                AWS::EC2::SecurityGroupIngress) echo "echo '# $type $pid fetched as part of SecurityGroup..'" >> commands.sh ;; # fetched as part of Security Group
                AWS::EC2::VPCEndpoint)  echo "../../scripts/161-get-vpce.sh $pid" >> commands.sh ;;
                AWS::EC2::VPC) echo "../../scripts/100-get-vpc.sh $pid" >> commands.sh ;;
                AWS::EC2::Subnet) echo "../../scripts/105-get-subnet.sh $pid" >> commands.sh ;;
                AWS::EC2::RouteTable)  echo "../../scripts/140-get-route-table.sh $pid" >> commands.sh ;;
                AWS::EC2::SubnetRouteTableAssociation) echo "../../scripts/141-get-route-table-associations.sh $pid" >> commands.sh ;;
                
                AWS::ECR::Repository)  echo "../../scripts/get-ecr.sh $pid"  >> commands.sh ;;

                AWS::ECS::Service)  echo "../../scripts/get-ecs-service.sh $parn" >> commands.sh ;;
                AWS::ECS::TaskDefinition)  echo "../../scripts/351-get-ecs-task.sh $pid" >> commands.sh ;;
                
                AWS::EKS::Cluster) echo "../../scripts/300-get-eks-cluster.sh $pid" >> commands.sh ;;
                AWS::EKS::Nodegroup) echo "# $type $pid Should be fetched via the EKS Cluster Resource" >> commands.sh ;;
                
                AWS::ElasticLoadBalancingV2::ListenerRule)  echo "../../scripts/elbv2_listener-rules.sh $parn" >> commands.sh ;;
                AWS::ElasticLoadBalancingV2::TargetGroup) echo "../../scripts/elbv2_target-groups.sh $parn" >> commands.sh ;;

                AWS::Events::EventBus)  echo "../../scripts/712-get-eb-bus.sh $pid" >> commands.sh;;
                AWS::Events::Rule)  echo "../../scripts/713-get-eb-rule.sh \"$pid\"" >> commands.sh;;

                AWS::IAM::Role)  echo "../../scripts/050-get-iam-roles.sh $pid" >> commands.sh ;;
                AWS::IAM::ManagedPolicy) echo "../../scripts/get-iam-policies.sh $parn" >> commands.sh ;;
                AWS::IAM::Policy)  echo "../../scripts/get-iam-policies.sh $parn" >> commands.sh ;;

                AWS::KMS::Key)  echo "../../scripts/080-get-kms-key.sh $pid" >> commands.sh ;;                
                AWS::KMS::Alias) echo "echo '#  $type $pid  fetched as part of function..'" >> commands.sh ;;  # fetched as part of function 
                
                AWS::Lambda::Function)  echo "../../scripts/700-get-lambda-function.sh $pid"  >> commands.sh ;;
                AWS::Lambda::Permission) echo "echo '# $type $pid fetched as part of function..'" >> commands.sh ;; # fetched as part of function
                AWS::Lambda::EventInvokeConfig) echo "echo '# $type $pid fetched as part of function..'" >> commands.sh ;; # fetched as part of function
                
                AWS::Logs::LogGroup)  echo "../../scripts/070-get-cw-log-grp.sh /$parn" >> commands.sh ;;
                
                AWS::S3::Bucket)  echo "../../scripts/060-get-s3.sh $pid" >> commands.sh ;;
                AWS::SNS::Topic)  echo "../../scripts/730-get-sns-topic.sh $parn" >> commands.sh ;;
                AWS::SQS::Queue)  echo "../../scripts/720-get-sqs-queue.sh $parn" >> commands.sh ;;
                
                AWS::SSM::Parameter)  echo "../../scripts/445-get-ssm-params.sh $pid" >> commands.sh ;;
                
                AWS::SecretsManager::Secret)  echo "../../scripts/450-get-secrets.sh $parn"  >> commands.sh ;;                
                AWS::ServiceDiscovery::Service)  echo "../../scripts/get-sd-service.sh $pid"  >> commands.sh ;;

                AWS::CloudFormation::WaitCondition*) echo "skipping $type" ;;
                AWS::CloudFormation::Stack) ;;

                *) echo "--UNPROCESSED-- $type $pid $parn" >> unprocessed.txt ;;
esac
        done   
fi
    
}



echo "level 1 nesting"
getstack $1

echo "level 2 nesting"
for nest in ${nested[@]}; do
    nest=`echo $nest | jq -r .`
    getstack $nest
done
nested+=$(printf "\"%s\" " $1)
echo "Stacks Found:"
for nest in ${nested[@]}; do
    nest=`echo $nest | jq -r .`
    echo "$nest"

done

for nest in ${nested[@]}; do
    nest=`echo $nest | jq -r .`
    getstackresources $nest
done

#echo "commands.sh"
#cat commands.sh
cat unprocessed.txt

