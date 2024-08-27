echo "Inside copy to s3"
echo $1 $2 $3
acc=$(echo $1)
reg=$(echo $2)
merge=$(echo $3)
if aws s3 ls "s3://aws2tf-$acc_$reg" 2>&1 | grep -q 'NoSuchBucket'; then
    echo "Bucket aws2tf-$acc_$reg does not exist. Creating..."
    aws s3 mb s3://aws2tf-$acc_$reg
fi
echo "Copying to s3://aws2tf-$acc_$reg"
aws s3 cp /tmp/aws2tf/generated/tf-$acc_$reg s3://aws2tf-$acc_$reg/ --recursive
echo "Done copying to s3"