#!/bin/sh
echo "entry 009"
#echo "working dir"
#pwd
cd /tmp
cp -r /aws2tf .
mkdir -p /tmp/aws2tf/generated
cd /tmp/aws2tf
df -m /tmp
echo $@
#set
# make buck etc
#echo "Starting lambda handler"
if [ -z "${AWS_LAMBDA_RUNTIME_API}" ]; then
    exec ~/.aws-lambda-rie/aws-lambda-rie python3 -m awslambdaric $@
else
    exec python3 -m awslambdaric $@
fi
