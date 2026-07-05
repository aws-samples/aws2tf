cd /Users/awsandy/odp/aws/sw/my-aws-samples/aws2tf-kiro1/aws2tf
echo "copying aws2tf"
cp *.py /Users/awsandy/odp/aws/sw/my-aws-samples/aws2tfv6
cp r*.txt /Users/awsandy/odp/aws/sw/my-aws-samples/aws2tfv6 || true
cp *.md /Users/awsandy/odp/aws/sw/my-aws-samples/aws2tfv6 || true
echo "copying aws2tf/code"
cd /Users/awsandy/odp/aws/sw/my-aws-samples/aws2tf-kiro1/aws2tf/code
cp *.py /Users/awsandy/odp/aws/sw/my-aws-samples/aws2tfv6/code
echo "copying aws2tf/code/fixtf_aws_resources"
cd /Users/awsandy/odp/aws/sw/my-aws-samples/aws2tf-kiro1/aws2tf/code/fixtf_aws_resources
cp *.py /Users/awsandy/odp/aws/sw/my-aws-samples/aws2tfv6/code/fixtf_aws_resources
cp *.md /Users/awsandy/odp/aws/sw/my-aws-samples/aws2tfv6/code/fixtf_aws_resources || true
echo "copying aws2tf/code/get_aws_resources"
cd /Users/awsandy/odp/aws/sw/my-aws-samples/aws2tf-kiro1/aws2tf/code/get_aws_resources
cp *.py /Users/awsandy/odp/aws/sw/my-aws-samples/aws2tfv6/code/get_aws_resources
cp *.md /Users/awsandy/odp/aws/sw/my-aws-samples/aws2tfv6/code/get_aws_resources || true
echo "copying aws2tf/documentation"
cd /Users/awsandy/odp/aws/sw/my-aws-samples/aws2tf-kiro1/aws2tf/documentation
cp -r * /Users/awsandy/odp/aws/sw/my-aws-samples/aws2tfv6/documentation
echo "copying aws2tf/.kiro/steering"
cd /Users/awsandy/odp/aws/sw/my-aws-samples/aws2tf-kiro1/aws2tf/.kiro/steering
cp *.md /Users/awsandy/odp/aws/sw/my-aws-samples/aws2tfv6/.kiro/steering || true
cd /Users/awsandy/odp/aws/sw/my-aws-samples/aws2tf-kiro1/aws2tf
