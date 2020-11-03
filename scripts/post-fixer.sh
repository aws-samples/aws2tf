# get the cluster name
cln=`grep name aws_eks_cluster*.tf | cut -f2 -d'"' | tr -d ' '`
echo $cln


echo "vpc name"

ls aws_vpc__*.tf &> /dev/null
if [ $? -eq 0 ]; then

    vpcrn=`grep resource aws_vpc__*.tf | cut -f4 -d'"'`
    echo $vpcrn
    if [ "$vpcrn" != "" ];then

        if [ "$vpcrn" == "vpc-$cln" ]; then
        echo "initial check matches cluster name - trying from filename"
        vpcrn=`ls aws_vpc__*.tf | cut -f4 -d'_' | cut -f1 -d'.'`


            if [ "$vpcrn" == "vpc-$cln" ]; then
                echo "secondary check matches cluster name - exiting"
                exit
            fi
        fi
        echo $vpcrn

        cp aws_vpc__${vpcrn}.tf orig/aws_vpc__${vpcrn}.tf.orig

        for i in `ls *.tf`; do
            cmd=`printf "sed -i'.tmp' -e 's/%s/vpc-%s/g' $i" $vpcrn $cln`
            echo $cmd
            eval $cmd
        done

        mv aws_vpc__${vpcrn}.tf vpc-${cln}.tf
        

        echo "manual fix"
        sed -i'.orig' -e 's/vpc-0e3a6de60b6c4e42d/vpc-manamieks/g' aws_vpc_endpoint*.tf
        sed -i'.orig' -e 's/subnet-002988463d16b327e/sub-priv-2a/g' aws_vpc_endpoint*.tf
        sed -i'.orig' -e 's/subnet-084320bcf394562a6/sub-priv-2b/g' aws_vpc_endpoint*.tf
        sed -i'.orig' -e 's/subnet-0ed589f1ec36e0867/sub-priv-2c/g' aws_vpc_endpoint*.tf

    else
        echo "skipping vpc ..."
    fi
else
    echo "skipping vpc ..."
fi


echo "subnet names"

ls aws_subnet__*.tf &> /dev/null
if [ $? -eq 0 ]; then


for i in `ls aws_subnet__*.tf`; do
    subrn=`grep resource $i | cut -f4 -d'"'`
    
    if [[ "$subrn" != *"subnet-"* ]]; then
        echo "trying secondary subnet resource name from filename"
        subrn=`ls $i | cut -f4 -d'_' | cut -f1 -d'.'`
    fi
    zn=`grep availability_zone $i | cut -f3 -d'-' | tr -d ' ' | tr -d '"'`
    #echo $zn
    pb=`grep map_public_ip_on_launch $i | cut -f2 -d'=' | tr -d ' '`
    #echo $pb
    pb=${pb//false/priv}
    pb=${pb//true/pub}
    #echo $pb
    subn=`printf "sub-%s-%s" $pb $zn`
    echo "$subrn --> $subn"
    cmd=`printf "sed -i'.orig' -e 's/%s/%s/g' $i" $subrn $subn`
    echo $cmd
    eval $cmd
    echo "mv aws_subnet__${subrn}.tf ${subn}.tf"
    
    mv aws_subnet__${subrn}.tf ${subn}.tf
    mv aws_subnet__*.orig orig
    # check every file
    for i in `ls *.tf`; do
        cmd=`printf "sed -i'.tmp' -e 's/%s/%s/g' $i" $subrn $subn`
        echo $cmd
        eval $cmd
    done
done

else
echo "skipping subnet"
fi

ls aws_vpc_endpoint__vpce*.tf &> /dev/null
if [ $? -eq 0 ]; then

    echo "VPC endpoint"
    for i in `ls aws_vpc_endpoint__vpce*.tf`; do

        srv=`grep service_name $i | cut -f4,5 -d'.' | tr -d '"'`
        srv=${srv//./_}
        echo $srv
        vpcern=`grep resource $i | cut -f4 -d'"'`
        echo $vpcern

        cmd=`printf "sed -i'.orig' -e 's/%s/vpce-%s/g' $i" $vpcern $srv`
        echo $cmd
        eval $cmd


        mv $i vpce-${srv}.tf
        mv aws_vpc_endpoint__*.orig orig

    done

else
    echo "skipping vpce"
fi









