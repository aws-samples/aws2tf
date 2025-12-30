---
inclusion: always
---
<!------------------------------------------------------------------------------------
   Add rules to this file or a short description and have Kiro refine them for you.
   
   Learn about inclusion modes: https://kiro.dev/docs/steering/#inclusion-modes
-------------------------------------------------------------------------------------> 

# new resource testing

if you need to test a resource here is the procedure with an example for "aws_vpc"

- see if it exists as an entry in fixtf_aws_resource/aws_not_implemented.py if it does comment that line.
- make sure aws_vpc exists in fixtf_aws_resource/aws_dict.py - stop if it does not exists
- in code/.automation create a new sub directory called test_aws_vpc
- in test_aws_vpc create the terraform files for a working example of aws_vpc - you can use your own research or scan the .automation/terraform-provider-aws/website/docs/r/vpc.html.markdown file for example code, you may have to create other resource types to support a working example
- run "terraform validate" to check the terraform code you created in test_aws_vpc,if the validate fails try and correct the code and rerun terraform validate
- run "terraform plan" to also check the terraform code you created in test_aws_vpc,if the plan fails try and correct the code and rerun terraform plan
- run "terraform apply -auto-approve" to deploy the code and check it deployed ok
- now run a specific type test for the new resource with a command ./aws2tf.py -t aws_vpc
- check it completes ok of not try to correct the error, stop after two attempts aand get input from the user
- also test a specific get of the new resource using a resource specific id eg: ./aws2tf.py -t aws_vpc -i vpc-09d8b4321d497f01b this id will be different for each resource type, you can get a good idea by looking for the import section of the markdown file vpc.html.markdown

it looks like this:

import {
  to = aws_vpc.test_vpc
  id = "vpc-a01106c2"
}

you see the id = "vpc-a01106c2"  - so it's looking for a vpc-* type of id for aws_vpc and so we use ./aws2tf.py -t aws_vpc -i vpc-09d8b4321d497f01b for the specific test - where vpc-09d8b4321d497f01b is the id of the vpc that is actually created - you should see this in the terraform apply output or by using terraform state show commands in the test_aws_vpc directory.

- if the two ./aws2tf.py tests succeed you should run "terraform destroy -auto-approve" in the  test_aws_vpc sub directory

- document the test results and action you took in a file called test-results.md in the test_aws_vpc directory

- if the test fails document the problems in test_aws_vpc/test-failed.md and if required uncomment the aws_vpc entry in fixtf_aws_resource/aws_not_implemented.py so it remains inactive.

- do not loop/iterate extensively when you have a problem - make 2 or 3 attempts to fix a problem then fail the test and document in test-failed.md - remember to run "terraform destroy -auto-approve"







