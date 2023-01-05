#!/bin/bash
echo "Check Buckets"
for i in `terraform state list 2> /dev/null | grep 'aws_s3_bucket\.'`;do 
    rname=$(echo $i | cut -f2 -d'.')
    #echo "rname=$rname"
    f1=`printf "aws_s3_bucket__%s.tf" $rname`
    #echo $f1
    if [[ ! -f $f1 ]];then
        echo "cross check - bucket for $f1 not found"
        cname=$(echo $rname | cut -f2 -d'_')
        ../../scripts/060-get-s3.sh $cname
    fi 
done
echo "Check Bucket Versioning"
for i in `terraform state list 2> /dev/null | grep 'aws_s3_bucket_versioning\.'`;do 
    rname=$(echo $i | cut -f2 -d'.')
    #echo "rname=$rname"
    f1=`printf "aws_s3_bucket_versioning__%s.tf" $rname`
    #echo $f1
    if [[ ! -f $f1 ]];then
        echo "cross check - versioning for $f1 not found"
        cname=$(echo $rname | cut -f2 -d'_')
        ../../scripts/get-s3-versioning.sh $cname
    fi 
done

