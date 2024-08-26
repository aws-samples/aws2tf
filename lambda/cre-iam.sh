aws iam create-role \
  --role-name laws2tf \
  --assume-role-policy-document '{"Version": "2012-10-17","Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}'
aws iam attach-role-policy --role-name laws2tf --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole  
# attach s3 full access policy
aws iam attach-role-policy --role-name laws2tf --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess

