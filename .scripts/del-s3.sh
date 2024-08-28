echo "Inside delete s3"
acc=$(echo $1)
reg=$(echo $2)
merge=$(echo $3)
echo $acc $reg $merge
if [[ $merge == "merge" ]];then
    echo "Merging so don't delete bucket, exiting....."
    exit 1
fi

if aws s3 ls "s3://aws2tf-${acc}-${reg}" 2>&1 | grep -q 'NoSuchBucket'; then
    echo "Bucket aws2tf-${acc}-${reg} does not exist. exiting..."
    exit 1
fi

echo "Emptying bucket aws2tf-${acc}-${reg}"
aws s3 rm s3://aws2tf-${acc}-${reg} --recursive
if [[ $? -eq 0 ]];then
    echo "Bucket aws2tf-${acc}-${reg} emptied"
fi
echo "Deleting bucket aws2tf-${acc}-${reg}"
aws s3 rb s3://aws2tf-${acc}-${reg} --force
if [[ $? -eq 0 ]];then
    echo "Bucket aws2tf-${acc}-${reg} deleted"
fi

 
echo "Done delete s3"