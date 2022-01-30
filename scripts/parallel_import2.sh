#!/bin/bash
if [ "$1" == "" ]; then
    echo "must specify resource type (ttft)"
    exit
fi

ttft=`echo $1 | tr -d '"'`
cname=`echo $2 | tr -d '"'`
rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}

echo "Importing $cname $rname"
st=`printf "%s__%s.tfstate" $1 $rname`
if [ -f "$st" ] ; then echo "$st exists already skipping" && exit; fi

#echo "parallel2 list check"
(terraform state list 2> /dev/null | grep ${ttft}.${rname}) > /dev/null 
if [[ $? -ne 0 ]];then

    #echo "Import $rname"
    #terraform state rm $ttft.$rname > /dev/null
    mkdir -p pi2
    cd pi2

    #cp ../aws.tf .
    ls ../.terraform > /dev/null
    if [[ $? -eq 0 ]];then 
        #echo "pi2 using root provider"
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
    fn=`printf "%s__%s.tf" $ttft $rname`
    printf "resource \"%s\" \"%s\" {}" $ttft $rname > $fn

     
    sl=`echo $((1 + $RANDOM % 15))` 
    #echo "$st import"        
    comm=$(printf "nice -n %s terraform import -state %s %s.%s \"%s\" | grep Import " $sl $st $ttft $rname $cname)
    echo $comm
    #eval $comm | grep Import
    eval $comm

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

    #terraform state show -state $st $ttft.$rname

    terraform state show -state $st $ttft.$rname | perl -pe 's/\x1b.*?[mGKH]//g' > ../$ttft-$rname-1.txt 
    #rm -f $fn

else
    echo "State $ttft.$rname already exists skipping import ..."
    terraform state show $ttft.$rname | perl -pe 's/\x1b.*?[mGKH]//g' > $ttft-$rname-1.txt


fi

rm -f terr*.backup

echo "exit parallel2 import $rname"