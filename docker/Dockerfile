FROM python:3.9-alpine3.20

#update, install curl, git, zip/unzip
RUN apk update \
    && apk add bash \
    && apk add curl zip git unzip iputils libc6-compat

RUN apk add --no-cache aws-cli


#ENV TERRAFORM_VERSION="1.9.3"
#RUN curl https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip > terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
#      unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /bin && \
#      rm -f terraform_${TERRAFORM_VERSION}_linux_amd64.zip

ENV TERRAFORM_VERSION="1.9.5"
RUN curl https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_arm64.zip > terraform_${TERRAFORM_VERSION}_linux_arm64.zip && \
      unzip terraform_${TERRAFORM_VERSION}_linux_arm64.zip -d /bin && \
      rm -f terraform_${TERRAFORM_VERSION}_linux_arm64.zip


RUN adduser -D aws2tf
RUN git clone -b python https://github.com/aws-samples/aws2tf.git /aws2tf
RUN chown -R aws2tf /aws2tf
USER aws2tf
WORKDIR /aws2tf
#install dependencies
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED=1
CMD ["tail", "-f", "/dev/null"]  
