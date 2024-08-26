reg=$(aws configure get region)
acc=$(aws sts get-caller-identity --query Account --output text)
aws ecr get-login-password | docker login --username AWS --password-stdin $acc.dkr.ecr.$reg.amazonaws.com
aws ecr create-repository --repository-name laws2tf --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE
docker tag laws2tf:latest $acc.dkr.ecr.$reg.amazonaws.com/laws2tf:latest
docker push $acc.dkr.ecr.$reg.amazonaws.com/laws2tf:latest
