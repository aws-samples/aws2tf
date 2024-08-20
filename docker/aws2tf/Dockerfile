FROM python:3-alpine

RUN apk add --update git bash curl unzip zip openssl make
RUN pip install awscli boto3 requests
RUN git clone -b python https://github.com/aws-samples/aws2tf.git /aws2tf
WORKDIR /aws2tf
ENV TERRAFORM_VERSION="1.9.3"
RUN curl https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip > terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
  unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /bin && \
  rm -f terraform_${TERRAFORM_VERSION}_linux_amd64.zip
  
ENTRYPOINT ["cat"]