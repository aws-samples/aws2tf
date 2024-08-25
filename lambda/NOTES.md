lambda_runtime_api_addr = os.environ["AWS_LAMBDA_RUNTIME_API"]


See:

https://dev.to/jason_yuen_5481b9088043d7/comment/1cnpi

RUN curl -Lo /usr/local/bin/aws-lambda-rie \
    https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie && \
    chmod +x /usr/local/bin/aws-lambda-rie

COPY entry_script.sh ${FUNCTION_DIR}

# Install dependencies
RUN pip install \
    --target ${FUNCTION_DIR} \
    awslambdaric

# Copy function code
COPY src/* ${FUNCTION_DIR}

ENTRYPOINT [ "sh", "entry_script.sh" ]
CMD [ "app.handler" ]




entry_script.sh

#!/bin/sh

if [ -z "${AWS_LAMBDA_RUNTIME_API}" ]; then
    exec /usr/local/bin/aws-lambda-rie /usr/local/bin/python -m awslambdaric $@
else
    exec /usr/local/bin/python -m awslambdaric $@
fi





aws ecr create-repository --repository-name hello-world --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE

aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account>.dkr.ecr.<region>.amazonaws.com

docker tag hello-world:latest <account>.dkr.ecr.<region>.amazonaws.com/hello-world:latest
docker push <account>.dkr.ecr.<region>.amazonaws.com/hello-world:latest

aws lambda create-function \
  --function-name hello-world \
  --package-type Image \
  --code ImageUri=111122223333.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest \
  --role arn:aws:iam::111122223333:role/lambda-ex


aws lambda invoke --function-name hello-world response.json

