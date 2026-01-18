---
inclusion: always
---
<!------------------------------------------------------------------------------------
   Add rules to this file or a short description and have Kiro refine them for you.
   
   Learn about inclusion modes: https://kiro.dev/docs/steering/#inclusion-modes
-------------------------------------------------------------------------------------> 


To define a new resource type you must follow these steps:

- The new resource must be named aws_"type" eg. aws_vpc  or aws_subnet, these need to correspond to the terraform resource documented here: https://registry.terraform.io/providers/hashicorp/aws/latest/docs
- next you need to figure out is this resource already listed in code/aws_dict.py

- you need to figure out which boto3 api allows you to list the resource or describe it by looking in 

list the terraform resource name
list the boto3 api client - so for example vpc and subnet use client.ec2 - so the answer is ec2
list the boto3 api that allows you to list all the resources so for vpc it is describe_vpcs