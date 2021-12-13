# aws2tf

**Work in progress - please report any issues you find.**

This utility 'AWS to Terraform' (aws2tf)
reads an AWS Account and generates all the required terraform configuration files (.tf) from each of the composite AWS resources

It also imports the terraform state using a

"terraform import ...." command

And finally runs a

"terraform plan ."  command

There should hopefully be no subsequent additions or deletions reported by the terraform plan command as all the appropriate terraform configuration files will have have automatically been created.

## Requirements & Prerequisites
+ The tool is written for the bash shell script & Python3 and has been tested on macOS 11.6.
+ AWS cli (v2) **version 2.3.4 or higher** needs to be installed and you need a login with at least "Read" privileges.
+ terraform **version v1.0.6** or higher needs to be installed.
+ jq **version 1.6 or higher**


## Quickstart guide to using the tool

Running the tool in your local shell (bash) required these steps:
1. Unzip or clone this git repo into an empty directory
2. login to the AWS cli  (aws configure)
3. run the tool


## Usage Guide

### The First Run
To generate the terraform files for an account and stop after a "terraform validate":
```
./aws2tf.sh -v yes
```

or if your interested in a type or group for example: Transit Gateway resources:
```
./aws2tf.sh -v yes -t tgw
```

```
terraform validate
Success! The configuration is valid.
```


Or there may be some kind of error as trying to test everyone's AWS combinations in advance isn't possible.

**If you happen to find one of these errors please open an issue here and paste in the error and it will get fixed.**

Once the validation is ok you can use the tool in anger to not only generate the terraform files (-v yes) but also import the resources and perform a terraform plan (see below)

---

<br>

To generate the terraform files for an entire AWS account, import the resources and perform a terraform plan:
```
./aws2tf.sh 
```


To include AWS account Policies and Roles:
```
./aws2tf.sh -p yes
```

To generate the terraform files for an EKS cluster named "mycluster"
```
./aws2tf.sh -t eks -i mycluster
```

To add App Mesh resources

```
./aws2tf.sh -t appmesh -c yes
```


To get a selection of resources use the -t option 
The currently supported types are:

* appmesh - App Mesh resources `-t appmesh`
* code - Code* resources `-t code`
* eb - EventBridge resources `-t eb`
* ecs - An ECS cluster and it's related resources `-t ecs -i Cluster-Name`
* eks - An EKS cluster and it's related resources `-t eks -i Cluster-Name`
* iam - All IAM related users, groups, policies & roles `-t iam`
* kms - KMS keys and aliases `-t kms`
* lf - Lake Formation resources `-t lf`
* lambda - Lambda resources `-t lambda`
* params - SSM parameters `-t params`
* org - AWS Organizations `-t org`
* rds - RDS database resources `-t rds`
* secrets - Secrets Manager secrets `-t secrets`
* sagemaker - SageMaker resources `-t sagemaker`
* spot - spot requests `-t spot`
* tgw - Transit Gateway resources `-t tgw -i transit-gateway-id`
* vpc - A VPC and it's related resources `-t vpc -i VPC-id`
  

To get all the VPC related resources in a particular VPC
```
./aws2tf.sh -t vpc -i vpc-xxxxxxxxx
```
To use a specific region and profile
```
./aws2tf.sh -t vpc -i vpc-xxxxxxxxx -r eu-west-1 -p default
```

#### Using the cumulative mode

If for example you want to get several VPCs you can use the cumulative mode:

To get all the VPC related resources in a particular VPC
```
./aws2tf.sh -t vpc -i vpc-aaaaaaaaa 
./aws2tf.sh -t vpc -i vpc-bbbbbbbbb -c yes
./aws2tf.sh -t vpc -i vpc-ccccccccc -c yes
```


<br>

Be patient - lots of output is given as aws2tf:

+ Loops through each provider 
+ Creates the requited *.tf configuration files in the "generated" directory
+ Performs the necessary 'terraform import' commands
+ And finally runs a 'terraform plan'

----

## Supported Resource Types

The following terraform resource types are supported by this tool at this time:

### App Mesh
* aws_appmesh_mesh
* aws_appmesh_route
* aws_appmesh_virtual_service
* aws_appmesh_virtual_node
* aws_appmesh_virtual_route
* aws_appmesh_virtual_gateway
* aws_appmesh_gateway_route

### Athena
* aws_athena_named_query
  
### Autoscaling
* aws_autoscaling_group

### Cloud9
* aws_cloud9_environment_ec2

### CloudFront
* aws_cloudfront_distribution

### CloudTrail
* aws_cloudtrail

### CloudWatch
* aws_cloudwatch_log_group

### CodeBuild
* aws_codebuild_project

### CodePipeline
* aws_codepipeline

### Config
* aws_config_configuration_recorder
* aws_config_delivery_channel
* aws_config_configuration_recorder_status
* aws_config_rule

### Database Migration Service (DMS)
* aws_dms_replication_instance
* aws_dms_endpoint
* aws_dms_replication_task

### Directory Services
* aws_directory_service_directory


### EC2
* aws_ec2_client_vpn_endpoint
* aws_ec2_client_vpn_network_association
* aws_ec2_transit_gateway
* aws_ec2_transit_gateway_route_table
* aws_ec2_transit_gateway_vpc_attachment
* aws_eip
* aws_instance
* aws_launch_template
* aws_spot_fleet_request

### ECR
* aws_ecr_repository

### ECS
* aws_ecs_capacity_provider (tbd)
* aws_ecs_cluster
* aws_ecs_service
* aws_ecs_task_definition

### EKS
* aws_eks_cluster
* aws_eks_fargate_profile
* aws_eks_node_group

### Elastic Load Balancing v2 (ALB/NLB)
* aws_lb
* aws_lb_listener
* aws_lb_target_group

### EMR (work in progress not de-referenced fully)

* aws_emr_cluster
* aws_emr_instance_group
* aws_emr_security_configuration

### Glue (needs updating)
* aws_glue_job
* aws_glue_crawler

### IAM
* aws_iam_instance_profile
* aws_iam_policy
* aws_iam_role
* aws_iam_role_policy
* aws_iam_role_policy_attachment

### KMS
* aws_kms_key
* aws_kms_alias

### Lambda
* aws_lambda_function
* aws_lambda_alias

### Organizations

* aws_organizations_account
* aws_organizations_organization
* aws_organizations_organizational_unit
* aws_organizations_policy

### Resource Groups
* aws_resource_group

### RDS
* aws_db_instance

### Route 53
* aws_route53_zone

### S3
* aws_s3_access_point
* aws_s3_bucket
* aws_s3_bucket_policy

### SageMaker
* aws_sagemaker_domain
* aws_sagemaker_user_profile
* aws_sagemaker_app

### Secrets Manager
* aws_secretsmanager_secret
* aws_secretsmanager_secret_version

### Service Discovery
* aws_service_discovery_service
* aws_service_discovery_private_dns_namespace

### SSM
* aws_ssm_association
* aws_ssm_document
* aws_ssm_parameter

### VPC
* aws_customer_gateway
* aws_internet_gateway
* aws_nat_gateway
* aws_network_interface
* aws_network_interface_attachment
* aws_route_table
* aws_route_table_association
* aws_subnet
* aws_security_group
* aws_security_group_rule
* aws_vpc
* aws_vpc_ipv4_cidr_block_association
* aws_vpc_endpoint
* aws_vpc_endpoint_service
* aws_vpc_dhcp_options
* aws_vpc_peering_connection
* aws_vpn_connection


## Planned Additions

+ Other terraform providers as terraform supports.

----

## Known problems

### Speed

It can take a lot of time to loop around everything in large accounts, in particular the importing of the resources.

### KMS:

Can fail if your login doesn't have access to KMS

### S3 Buckets

Can fail if you don't have access to the KMS key used for encryption.






