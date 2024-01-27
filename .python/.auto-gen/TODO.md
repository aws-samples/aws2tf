#aws_default_subnet - fix default only
#aws_default_vpc - fix default only

aws_default_route_table


aws_lambda_function

aws_iam_role andy.test.role


aws_kms_alias - too many loops


add_dependancy: aws_vpc_ipv4_cidr_block_association.vpc-0d18b88f8596b92c3
Terraform Plan Loop ... 
terraform plan -generate-config-out=resources.out -out tfplan -json | jq . > plan1.json
split file:resources.out
e=KeyError('Value')
<class 'KeyError'> fixtf.py 265
-- no fixtf for aws_instance__i-011a4b38e318edfbd calling generic fixtf2.aws_resource
WARNING: No fixtf for aws_instance__i-011a4b38e318edfbd call