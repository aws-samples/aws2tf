FROM amazonlinux:2023
RUN yum -y install rpm dnf-plugins-core \
 && yum -y update \
 && yum -y install \
      initscripts \
      sudo \
      which \
      hostname \
      unzip \
      git \
      python3 \
      python3-pip \
 && yum clean all
 

RUN git clone -b python https://github.com/aws-samples/aws2tf.git /aws2tf
WORKDIR /aws2tf
RUN pip3 install awscli boto3 requests
ENV PYTHONUNBUFFERED=1
ENV TERRAFORM_VERSION="1.9.3"
RUN curl https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip > terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
  unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /bin && \
  rm -f terraform_${TERRAFORM_VERSION}_linux_amd64.zip
  
ENTRYPOINT ["cat"]