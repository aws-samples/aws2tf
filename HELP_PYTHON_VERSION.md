## `aws2tf.py`, The Python version - Alpha release

aws2tf.py will help import into Terraform exiting AWS infrastructure, and produce the corresponding Terraform HCL files. The end result should be that a terraform plan will show the Terraform code matches the exisitng infrastructure.

This Python version has several advantages over the original bash version:

* Performance
* Better coverage of AWS resources
* Better coverage of stack resources


`aws2tf.py` will also attempt to:

* De-reference hardcodes values into their Terraform addresses
* Find depentant resources and import them
* Where possible remove region and account references and replace with Terraform data values.

You can use `aws2tf.py` in a number of different ways:


Getting started:

To see the command line help use:

```
./aws2tf.py -h
```

or for more extensive help:

```
./aws2tf.py -l
```

Try a simple run to get all your VPC's:

./aws2tf.py -t vpc   (or)  ./aws2tf.py -t aws_vpc

or a specific vpc:

./aws2tf.py -t aws_vpc -i vpc-xxxxxxxxx


Using the merge mode, you can combine multiple runs of aws2tf.py to pull togeather resources by using the `-m` flag - to enable the merge mode:

```
./aws2tf -t aws_vpc
./aws2tf -t kms -m
./aws2tf -t aws_s3_bucket -i my_bucket_name -m
```

aws2tf can also import the resources associated with a successfully deployed stack set to get the resources of a deployed stack set "mystack_name" use:

```
./aws2tf.py -t stack -i mystack_name
```


Not recommended:

Juat run `aws2tf.py` with no flags , which will look for every resource supported in your account.

-----

## Reporting Problems

This Python version of `aws2tf.py` has not undergone as much testing as the bash version `aws2tf.sh` so please report and problems you find by opening an issue.

-----


## Supported Stack Set Resources (subject to ongoing testing)

see [here](https://github.com/aws-samples/aws2tf/blob/master/StackSet-Resources.md) for a list

## Supported Terraform Resources (subject to ongoing testing)

see [here](https://github.com/aws-samples/aws2tf/blob/master/Terraform-Resources.md) for a list


## Requirements & Prerequisites
+ The tool is written using Python3.8 and has been tested on macOS 14.5.
+ Terraform **version v1.5.4** or newer needs to be installed 
+ + Recommend v1.7.5 or 1.8.5+
+ + Avoid early point releases like 1.8.0 & 1.8.1 etc.
+ **Python version 3.8 or later**.
+ boto3 1.34.93 or later (pip3 install -r requirements.txt).
