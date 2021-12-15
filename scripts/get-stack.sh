#!/bin/bash
if [ "$1" == "" ]; then echo "must specify a stack name" && exit; fi
nested=() 
echo "#!/bin/bash" > commands.sh

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
            #echo $type $pid
            case $type in
                AWS::ECR::Repository) echo "echo 'Stack $1 Importing $i of $count ..'" >> commands.sh && echo "../../scripts/get-ecr.sh $pid"  >> commands.sh ;;
                AWS::EC2::SecurityGroup) echo "echo 'Stack $1 Importing $i of $count ..'" >> commands.sh && echo "../../scripts/110-get-security-group.sh $pid"  >> commands.sh ;;
                AWS::EC2::SecurityGroupIngress) ;; # fetched as part of Security Group
                AWS::EC2::VPCEndpoint) echo "echo 'Stack $1 Importing $i of $count ..'" >> commands.sh && echo "../../scripts/161-get-vpce.sh $pid" >> commands.sh ;;
                AWS::EC2::VPC) echo "echo 'Stack $1 Importing $i of $count ..'" >> commands.sh && echo "../../scripts/100-get-vpc.sh $pid" >> commands.sh ;;
                AWS::EC2::Subnet) echo "echo 'Stack $1 Importing $i of $count ..'" >> commands.sh && echo "../../scripts/105-get-subnet.sh $pid" >> commands.sh ;;
                AWS::EC2::RouteTable) echo "echo 'Stack $1 Importing $i of $count ..'" >> commands.sh && echo "../../scripts/140-get-route-table.sh $pid" >> commands.sh ;;
                AWS::EC2::SubnetRouteTableAssociation) echo "../../scripts/141-get-route-table-associations.sh $pid" >> commands.sh ;;
                AWS::S3::Bucket) echo "echo 'Stack $1 Importing $i of $count ..'" >> commands.sh && echo "../../scripts/060-get-s3.sh $pid" >> commands.sh ;;
                AWS::Lambda::Function) echo "echo 'Stack $1 Importing $i of $count ..'" >> commands.sh && echo "../../scripts/700-get-lambda-function.sh $pid"  >> commands.sh ;;
                AWS::Lambda::Permission) ;; # fetched as part of function
                AWS::SSM::Parameter) echo "echo 'Stack $1 Importing $i of $count ..'" >> commands.sh && echo "../../scripts/445-get-ssm-params.sh $pid" >> commands.sh ;;
                AWS::KMS::Key) echo "echo 'Stack $1 Importing $i of $count ..'" >> commands.sh && echo "../../scripts/080-get-kms-key.sh $pid" >> commands.sh ;;
                AWS::IAM::Role) echo "echo 'Stack $1 Importing $i of $count ..'" >> commands.sh && echo "../../scripts/050-get-iam-roles.sh $pid" >> commands.sh ;;
                AWS::Events::Rule) echo "../../scripts/713-get-eb-rule.sh $pid" >> commands.sh;;
                AWS::KMS::Alias) ;; # feteched as part of key
                AWS::CodeArtifact::Domain)  echo "echo 'Stack $1 Importing $i of $count ..'" >> commands.sh && echo "../../scripts/627-get-code-artifact-domain.sh $pid"  >> commands.sh ;;
                AWS::CodeArtifact::Repository) echo "echo 'Stack $1 Importing $i of $count ..'" >> commands.sh && echo "../../scripts/627-get-code-artifact-repository.sh $pid"  >> commands.sh ;;
                AWS::CloudFormation::Stack) ;;
                *) echo "--UNPROCESSED-- $type $pid" ;;
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

echo "commands.sh"
cat commands.sh

