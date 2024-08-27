#!/bin/sh
echo "entry 008"
#echo "working dir"
#pwd
cd /tmp
cp -r /aws2tf .
mkdir -p /tmp/aws2tf/generated
cd /tmp/aws2tf
df -m /tmp
#echo "files in /tmp/aws2tf"
#ls -al
#set | grep AWS
#echo "Starting lambda handler"
if [ -z "${AWS_LAMBDA_RUNTIME_API}" ]; then
    exec ~/.aws-lambda-rie/aws-lambda-rie python3 -m awslambdaric $@
else
    exec python3 -m awslambdaric $@
fi
