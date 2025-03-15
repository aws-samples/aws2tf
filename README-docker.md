## Running aws2tf using a container

**Note: you do not need to clone this repo to run aws2tf using a container - just follow these instructions instead**

### Pre-requisites

* `docker` installed and available - see [here](https://docs.docker.com/engine/install/)


### Make the required sub directories

```bash
mkdir -p aws2tf/generated
cd aws2tf
```

### Create the Dockerfile (tip: use the copy icon, top right)

```bash
cat << 'EOF' > Dockerfile
FROM python:3.12.9-alpine3.21
RUN apk update \
    && apk add curl zip git unzip

# Get Terraform
ARG TF_VERSION=latest
RUN set -eux \
	&& if [ "${TF_VERSION}" = "latest" ]; then \
		VERSION="$( curl -sS https://releases.hashicorp.com/terraform/ \
			| tac | tac \
			| grep -Eo '/terraform/[.0-9]+/\"' \
			| grep -Eo '[.0-9]+' \
			| sort -V \
			| tail -1 )"; \
	else \
		VERSION="$( curl -sS https://releases.hashicorp.com/terraform/ \
			| tac | tac \
			| grep -Eo "/terraform/${TF_VERSION}\.[.0-9]+/\"" \
			| grep -Eo '[.0-9]+' \
			| sort -V \
			| tail -1 )"; \
	fi \
	\
	# Get correct architecture
	&& if [ "$(dpkg --print-architecture | awk -F'-' '{print $NF}' )" = "i386" ]; then\
		ARCH=386; \
	elif [ "$(uname -m)" = "x86_64" ]; then \
		ARCH=amd64; \
	elif [ "$(uname -m)" = "aarch64" ]; then \
		ARCH=arm64; \
	elif [ "$(uname -m)" = "armv7l" ]; then \
		ARCH=arm; \
	fi \
	\
	&& curl --fail -sS -L -O \
		https://releases.hashicorp.com/terraform/${VERSION}/terraform_${VERSION}_linux_${ARCH}.zip \
	&& unzip terraform_${VERSION}_linux_${ARCH}.zip -d /usr/bin \
	&& chmod +x /usr/bin/terraform \
    && rm -f terraform_${VERSION}_linux_${ARCH}.zip

RUN adduser -D aws2tf
RUN git clone -b python https://github.com/aws-samples/aws2tf.git /aws2tf
RUN chown -R aws2tf /aws2tf
USER aws2tf
WORKDIR /aws2tf
#install dependencies
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED=1
# Set the entrypoint
ENTRYPOINT ["python", "aws2tf.py"]
CMD []
EOF
```

### build the container from the newly created Dockerfile.aws2tf

```bash
docker build --no-cache -t aws2tf . 
```

### Create an alias ro run the aws2tf container

```bash
alias aws2tf.py="docker run --security-opt=no-new-privileges --name aws2tf --rm -it -v $(pwd)/generated:/aws2tf/generated -v ~/.aws:/home/aws2tf/.aws:ro aws2tf"
```


### run aws2tf using the alias to the container:

```bash
./aws2tf.py -t vpc
```


