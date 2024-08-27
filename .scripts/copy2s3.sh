echo "Inside copy to s3"
acc=$(echo $1)
reg=$(echo $2)
merge=$(echo $3)
echo $acc $reg $merge
if aws s3 ls "s3://aws2tf-${acc}-${reg}" 2>&1 | grep -q 'NoSuchBucket'; then
    echo "Bucket aws2tf-${acc}-${reg} does not exist. Creating..."
    cmd=$(printf "aws s3 mb s3://aws2tf-%s-%s" $acc $reg)
    echo $cmd
    eval $cmd
    if [ $? -ne 0 ]; then
        echo "Error creating bucket aws2tf-${acc}-${reg}"
        exit 1
    fi
fi
echo "Copying to s3://aws2tf-${acc}-${reg}"
cmd=$(printf "aws s3 cp /tmp/aws2tf/generated/tf-%s-%s s3://aws2tf-%s-%s/ --recursive --exclude " $acc $reg $acc $reg)
echo $cmd
aws s3 cp /tmp/aws2tf/generated/tf-${acc}-${reg} s3://aws2tf-${acc}-${reg}/ --recursive --exclude ".terraform/*" 
echo "Done copying to s3"