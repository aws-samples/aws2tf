## aws2tf.py Documentation

aws2tf.py will help import into Terraform exiting AWS infrastructure, and produce the corresponding Terraform HCL files.

The end result should be that a terraform plan will show the Terraform code matches the exisitng infrastructure.

aws2tf will also attemnpt to:

Dereference hardcodes values into their Terraform addresses
Find depentant resources and import them
Where possible remove region and account references and replace with Terraform data values.

You ban use aws2tf in a number of different ways:

Not recommended:

Juat run aws2tf.py with no flags



Getting started:

To see the command line help use:

./aws2tf.py -h

or for more extensive help

./aws2tf.py -l


Try a simple run to get all your VPC's:

./aws2tf.py -t vpc   (or)  ./aws2tf.py -t aws_vpc


Using the merge mode, you can combine multiple runs of aws2tf.py to pull togeather resources by using the `-m` flag - to enable the merge mode:

./aws2tf -t aws_vpc
./aws2tf -t kms -m
./aws2tf -t aws_s3_bucket -i my_bucket_name -m

aws2tf can also import the resources associated with a successfully deployed stack set to get the resources of a deployed stack set "mystack_name" use:

./aws2tf.py -t stack -i mystack_name


