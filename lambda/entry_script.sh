#!/bin/sh
echo "working dir"
pwd
mkdir -p /tmp/aws2tf/generated
cp -r * /tmp/aws2tf
cd /tmp/aws2tf
ls -l
set | grep AWS
echo "Starting lambda handler"
if [ -z "${AWS_LAMBDA_RUNTIME_API}" ]; then
    exec ~/.aws-lambda-rie/aws-lambda-rie python3 -m awslambdaric $@
else
    exec python3 -m awslambdaric $@
fi
