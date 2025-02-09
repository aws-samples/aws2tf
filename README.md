
<img src="https://github.com/aws-samples/aws2tf/blob/python/.logos/aws2tf.png" width="300" alt="aws2tf" class="center">



----

## Description

aws2tf.py will import into Terraform existing AWS infrastructure, and produce the corresponding Terraform HCL files. 

`aws2tf.py` will also attempt to:

* De-reference hardcoded values into their Terraform addresses.
* Find dependent resources and import them.
* Where possible, remove region and account references and replace with Terraform data values.


Finally aws2tf runs a `terraform plan` command and there should hopefully be no subsequent additions or deletions reported by the terraform plan command as all the appropriate terraform configuration files will have automatically been created.

## Requirements & Prerequisites

+ MacOS or Linux 
+ Python3 (v3.8+)
+ boto3 1.36.13 or later (pip3 install -r requirements.txt).
+ AWS cli (v2) **version 2.22.33 or higher** needs to be installed and you need a login with at least "Read" privileges.
+ Terraform **version v1.8.5** or higher needs to be installed. (recommend you avoid early point releases eg. 1.9.0/1.9.1)
+ jq **version 1.6 or higher**

## Optional but recommended

+ pyenv - to help manage Python versions and environments (https://github.com/pyenv/pyenv)
+ tfenv - - to help manage multiple Terraform versions (https://github.com/tfutils/tfenv)
+ trivy **version 0.48.0 or later**  (https://aquasecurity.github.io/trivy/v0.54/)


(*This tool is currently developed/tested using Python 3.9.16 on macOS 15.1.1*)

----

## Quickstart guide to using the tool

Running the tool in your local shell (bash) required these steps:
1. Unzip or clone this git repo into an empty directory.
2. login to the AWS cli  (aws configure).
3. run the tool - see usage guide below.

-----

## Usage Guide

### Help options

To see the command line help use:

```bash
./aws2tf.py -h
```

or for more extensive help:

```bash
./aws2tf.py -l
```

### The First Run

To generate the terraform files for all the VPC's in your account/region:

```bash
./aws2tf.py -t vpc
```

or for a specific VPC:

```bash
./aws2tf.py -t aws_vpc -i vpc-xxxxxxxxxx
```

You can also instead of using predefined types use the direct Terraform resource names:

```bash
./aws2tf.py -t aws_sagemaker_domain
```

You can also combine type requests by using a comma delimited list:

```bash
./aws2tf.py -t vpc,efs,aws_sagemaker_domain
```

By default aws2tf genrates a separate aws_xxxx.tf file for every resource it finds, if you would prefer to have them all merged into a single file (main.tf)
use the -s option:

```bash
./aws2tf.py -t vpc -s
```

### Adding (merging) resources:

Now you can add whatever resources you want by using the -m (merge) flag:

To add all ECS resources:

```bash
./aws2tf.py -t ecs -m
```

You can see all the supported types (-t [type]) by using -l (long help) option: `./aws2tf.py -l`

You can also import just a specific resource by passing it's AWS resource name, in this example all the existing resources and the newly merged resources will be put into a single (main.tf) file as the -s option is included:

```bash
./aws2tf.py -t eks -i my-cluster-name -m -s
```

or for a specific domain:

```bash
./aws2tf.py -t aws_sagemaker_domain -i d-xxxxxxxxx -m 
```

Add a specific S3 bucket:

```bash
./aws2tf -t aws_s3_bucket -i my_bucket_name -m
```


### Importing from a deployed stack

Often Organisations (and AWS blogs/workshops) deploy resources for use using a stack.

aws2tf can convert these to terraform for you using the -s [stack name] option

```bash
./aws2tf.sh -s <stack name>
```


### Getting everything in an account

Finally you can scan everything in your account by simply running:

```bash
./aws2tf.py
```

But this is **Not recommended** as this will take quite some time to complete!

You can also try the experimental fast mode which uses multi threading to speed things up:

```bash
./aws2tf.py -f
```

## Advanced Options

### Overriding the Terraform version

You can override the default Terraform provider version used by using the -tv flag

```bash
./aws2tf.py -t vpc -tv 5.86.0
```

You need to ensure the provider version you specify is valid, as (currently) the version is just passed straight through without any validation checks 


### Importing EC2 instances by tag

You can import EC2 instances selectively by using the -ec2tag option

```bash
./aws2tf.py -t aws_instance -ec2tag "project:my value"
```

The above will only import instances that have a tag key/value pair of "project" and a value of "my value"


### Using Terraform data resources:


** still under test **

These flags will cause aws2tf to use data statements for certain resource types - useful for enterprises where for example networking components are provided by a different team, the available flags are:

* -dnet:  uses data resources for aws_vpc, aws_subnet and aws_security_group
* -dkms:  uses data statements for aws_kms_key
* -dkey:  uses data statements for aws_key_pair

----------


## Reporting Errors

You may come across some kind of error as trying to test everyone's AWS combinations in advance isn't possible.

**If you happen to find one of these errors please open an issue [here](https://github.com/aws-samples/aws2tf/issues) and paste in the error and it will get fixed.**

For stack sets (-s option) look for these two files in the generated/tf* directory - and paste their contents into the issue:

* stack-unprocessed.err
* stack-null.err


---

## Running aws2tf as a container

See the instructions [here](https://github.com/aws-samples/aws2tf/blob/master/README-docker.md)

Note you do not need to clone this repo if you want to run aws2tf as a container

---

## Supported Resources

### Supported Stack Resources (subject to ongoing testing)

see [here](https://github.com/aws-samples/aws2tf/blob/master/Stack-Resources.md) for a list

### Supported Terraform Resources (subject to ongoing testing)

see [here](https://github.com/aws-samples/aws2tf/blob/master/Terraform-Resources.md) for a list

----

### Terraform State

aws2tf maintains state in it's own local directory:

generated/tf.<account-number>.<region>/

When using cumulative mode this same state file is used / added to.

It is not possible at this time to use your own state location (eg. on s3)


----

**October  2024**

*The python version of this tool `aws2tf.py` has now superceded the old bash script version.*
*You can still find and use the old version in the bash-version branch`*

```bash
git clone -b bash-version https://github.com/aws-samples/aws2tf.git
``` 


