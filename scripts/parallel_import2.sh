#!/bin/bash
if [ "$1" == "" ]; then
    echo "must specify resource type (ttft)"
    exit
fi

ttft=`echo $1 | tr -d '"'`
cname=`echo $2 | tr -d '"'`
rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
st=`printf "%s__%s.tfstate" $1 $rname`

echo "parallel2 list check"
(terraform state list 2> /dev/null | grep ${ttft}.${rname}) > /dev/null 
if [[ $? -ne 0 ]];then

    #echo "Import $rname"
    #terraform state rm $ttft.$rname > /dev/null
    mkdir -p pi2
    cd pi2

    #cp ../aws.tf .
    ls ../.terraform > /dev/null
    if [[ $? -eq 0 ]];then 
        echo "pi2 using root provider"
        ln -s ../aws.tf aws.tf  2> /dev/null
        ln -s ../.terraform .terraform 2> /dev/null
        ln -s ../.terraform.lock.hcl .terraform.lock.hcl 2> /dev/null
    else
        echo "pi2 using initing TF provider"
        sl=`echo $((1 + $RANDOM % 15))`
        terraform init -no-color > /dev/null
        if [ $? -ne 0 ]; then
            echo "init backoff & retry for $rname"
            sleep 10
            terraform init -no-color > /dev/null
            if [ $? -ne 0 ]; then
                    echo "init long backoff & retry with full errors for $rname"
                    sleep 20
                    terraform init -no-color > /dev/null
            fi
        fi
    fi
    sl=`echo $((1 + $RANDOM % 4))`
    sleep $sl
    printf "resource \"%s\" \"%s\" {}" $ttft $rname > $ttft__$rname.tf


    echo "Importing... pi2"
    pwd
     
    sl=`echo $((1 + $RANDOM % 15))` 
    echo "$st import"        
    comm=$(printf "nice -n %s terraform import -state %s %s.%s \"%s\"" $sl $st $ttft $rname $cname)
    echo $comm
    eval $comm
    #nice -n $sl terraform import -state $st $ttft.$rname "$cname" > /dev/null

    if [ $? -ne 0 ]; then
        echo "Import backoff & retry for $rname"
        sl=`echo $((1 + $RANDOM % 10))`
        sleep $sl
        eval $comm
        if [ $? -ne 0 ]; then
                echo "Import long backoff & retry with full errors for $rname"
                sl=`echo $((2 + $RANDOM % 20))`
                sleep $sl
                eval $comm
        fi
    fi
    #echo "local state list"
    #terraform state list -no-color

    echo $comm > ../data/import_$ttft_$rname.sh

    terraform  tate show -state $st $ttft.$rname

    terraform  tate show -state $st $ttft.$rname | perl -pe 's/\x1b.*?[mGKH]//g' > $ttft-$rname-1.txt 
    rm $ttft.$rname.tf

else
    echo "State $ttft.$rname already exists skipping import ..."
    terraform state show $ttft.$rname | perl -pe 's/\x1b.*?[mGKH]//g' > $ttft-$rname-1.txt
    ls $ttft*-1.txt

fi

rm -f terr*.backup
#rm -rf $ttft-$rname/.terraform*
# rmdir $ttft-$rname
#rm -f $ttft-$rname-1.txt
#echo "top level state list"
#terraform state list | grep $ttft.$rname
echo "exit parallel2 import $rname"