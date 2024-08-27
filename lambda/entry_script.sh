#!/bin/sh
echo "working dir"
mkdir -p /tmp/aws2tf/generated
cp -r * /tmp/aws2tf
set | grep AWS
echo "Starting lambda handler"
if [ -z "${AWS_LAMBDA_RUNTIME_API}" ]; then
    exec ~/.aws-lambda-rie/aws-lambda-rie python3 -m awslambdaric $@
else
    exec python3 -m awslambdaric $@
fi
