#!/bin/bash
echo "Check Buckets"
for i in `terraform state list 2> /dev/null | grep 'aws_s3_bucket\.'`;do 
rname=$(echo $i | cut -f2 -d'.')
#echo "rname=$rname"
f1=`printf "aws_s3_bucket__%s.tf" $rname`
#echo $f1
if [[ ! -f $f1 ]];then
    echo "cross check - bucket for $f1 not found"
    ../../scripts/060-get-s3.sh $rname
fi 
done


