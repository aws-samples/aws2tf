for i in $(grep aws_ ../../TOPORT_from_aws2tf.md); do
j=`echo $i | cut -f2 -d'*'`
    echo $j
    cd /Users/awsandy/odp/AWS/sw/my-aws-samples/aws2tf-py
    ./aws2tf.py -t $j
done
