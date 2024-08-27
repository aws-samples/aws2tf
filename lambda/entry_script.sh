#!/bin/sh
echo "entry 001"
echo "working dir"
pwd
mkdir -p /tmp/aws2tf/generated
cd /tmp/aws2tf
cp -r /aws2tf/* .
pwd
echo "files in /tmp/aws2tf"
set | grep AWS

#echo "Starting lambda handler"
#if [ -z "${AWS_LAMBDA_RUNTIME_API}" ]; then
#    exec ~/.aws-lambda-rie/aws-lambda-rie python3 -m awslambdaric $@
#else
#    exec python3 -m awslambdaric $@
#fi
