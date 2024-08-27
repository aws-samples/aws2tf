reg=$(aws configure get region)
acc=$(aws sts get-caller-identity --query Account --output text)
aws lambda create-function \
  --function-name laws2tf \
  --package-type Image \
  --architectures arm64 \
  --code ImageUri=$acc.dkr.ecr.$reg.amazonaws.com/laws2tf:latest \
  --role arn:aws:iam::$acc:role/laws2tf \
  --timeout 300 \
  --memory-size 2048 \
  --ephemeral-storage Size=8192 \
  --output text