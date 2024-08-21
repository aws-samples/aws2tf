mkdir -p aws2tf/generated
cd aws2tf
cat << 'EOF' > Dockerfile.aws2tf
FROM python:3.9-alpine3.20
RUN apk update \
    && apk add bash \
    && apk add curl zip git unzip iputils \
    && apk add --no-cache aws-cli

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
#ENTRYPOINT ["./aws2tf.py"] 
CMD ["./aws2tf.py"] 
EOF
docker build -f Dockerfile.aws2tf --no-cache -t aws2tf . 
alias aws2tf.py="docker run  --name aws2tf --rm -it -v $(pwd)/generated:/aws2tf/generated -v ~/.aws:/home/aws2tf/.aws aws2tf ./aws2tf.py"
echo "run with:"
echo "aws2tf.py -t vpc"



