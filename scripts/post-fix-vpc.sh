# get the cluster name
cln=`grep name aws_eks_cluster*.tf | cut -f2 -d'"' | tr -d ' '`
echo $cln


echo "vpc name"

vpcrn=`grep resource aws_vpc__*.tf | cut -f4 -d'"'`

if [ $vpcrn == vpc-$cln ]; then
echo "initial check matches cluster name - trying form filename"
vpcrn=`ls aws_vpc__*.tf | cut -f4 -d'_' | cut -f1 -d'.'`
    if [ $vpcrn == vpc-$cln ]; then
        echo "secondary check matches cluster name - exiting"
        exit
    fi
fi
echo $vpcrn


for i in `ls *.tf`; do
    cmd=`printf "sed -i'.orig' -e 's/%s/vpc-%s/g' $i" $vpcrn $cln`
    echo $cmd
    eval $cmd
done

cp aws_vpc__${vpcrn}.tf vpc-${cln}.tf
mv aws_vpc__${vpcrn}.tf aws_vpc__${vpcrn}.tf.orig


