echo "Inside restore to s3"
acc=$(echo $1)
reg=$(echo $2)
merge=$(echo $3)
echo $acc $reg $merge
if [[ $merge == "nomerge"]];then
    echo "Not merging, exiting ..."
    exit 1
fi
if aws s3 ls "s3://aws2tf-${acc}-${reg}" 2>&1 | grep -q 'NoSuchBucket'; then
    echo "Bucket aws2tf-${acc}-${reg} does not exist. exiting..."
    exit 1
fi
echo "Copying to /tmp from s3://aws2tf-${acc}-${reg}"
aws s3 cp /tmp/aws2tf/generated/tf-${acc}-${reg} s3://aws2tf-${acc}-${reg}/ --recursive --exclude ".terraform/*" 
echo "Done copying to s3"