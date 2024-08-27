echo "copy to s3"
set
#reg=$(aws configure get region)
#acc=$(aws sts get-caller-identity --query Account --output text)

#if aws s3 ls "s3://aws2tf-$acc_$reg" 2>&1 | grep -q 'NoSuchBucket'; then
#    aws s3 mb s3://aws2tf-$acc_$reg
#fi


#aws s3 cp /tmp/aws2tf/generated/tf-$acc_$reg s3://aws2tf-$acc_$reg/ --recursive