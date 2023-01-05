#!/bin/bash
if [ "$1" == "" ]; then
    echo "must specify resource type (ttft)"
    exit
fi

ttft=`echo $1 | tr -d '"'`
cname=`echo $2 | tr -d '"'`
rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
sl=`echo $((1 + $RANDOM % 15))` 
# override rname for aws_s3_bucket
if [[ $ttft == "aws_s3_bucket" ]];then
  rname=`printf "b_%s" $rname`
fi

#echo "Importing $ttft $cname $rname"
st=`printf "%s__%s.tfstate" $1 $rname`
if [ -f "$st" ] ; then echo "$st exists already skipping" && exit; fi

#echo "parallel2 list check"
(nice -n $sl terraform state list 2> /dev/null | grep ${ttft}.${rname}) > /dev/null 
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
        ln -s ../main-vars.tf main-vars.tf  2> /dev/null
        ln -s ../data-aws.tf data-aws.tf  2> /dev/null
        ln -s ../.terraform .terraform 2> /dev/null
        ln -s ../.terraform.lock.hcl .terraform.lock.hcl 2> /dev/null
    else
        echo "pi2 using initing TF provider"
        sl=`echo $((1 + $RANDOM % 15))`
        terraform init -no-color > /dev/null
        if [ $? -ne 0 ]; then
            echo "init backoff & retry for $cname"
            sleep $sl
            terraform init -no-color > /dev/null
            if [ $? -ne 0 ]; then
                    echo "init long backoff & retry with full errors for $cname"
                    sleep 20
                    terraform init -no-color > /dev/null
            fi
        fi
    fi

    fn=`printf "%s__%s.tf" $ttft $rname`
    printf "resource \"%s\" \"%s\" {}\n" $ttft $rname > $fn
    sync && sync

    if [[ ! -f "$fn" ]]; then echo "Error in pi2: prototype $fn does not exist exiting..." && exit; fi
           
    comm=$(printf "nice -n %s terraform import -state %s %s.%s \"%s\" &> /dev/null" $sl $st $ttft $rname $cname)
    #echo $comm
    sleep $sl
    eval $comm

    if [ $? -ne 0 ]; then
        printf "resource \"%s\" \"%s\" {}\n" $ttft $rname > $fn
        sync && sync
        echo "--> 1st Import backoff & retry for $rname"
        sl=`echo $((4 + $RANDOM % 10))`
        sleep $sl
        eval $comm
        if [ $? -ne 0 ]; then
                echo "--> 2nd Import backoff & retry for $rname"
                sl=`echo $((8 + $RANDOM % 20))`
                sleep $sl
                sync;sync
                eval $comm
                if [ $? -ne 0 ]; then
                    echo "--> ** 3rd (Final) Import backoff & retry with full errors for $rname"
                    sl=`echo $((16 + $RANDOM % 40))`
                    sleep $sl
                    sync;sync
                    eval $comm
                    if [ $? -ne 0 ]; then
                        echo "** ERROR ** $rname Import failed"
                        mv $fn ../data/$fn.pi2
                    else
                        echo "Imported $ttft.$rname"                    
                    fi
                else
                    echo "Imported $ttft.$rname"
                fi
        else
           echo "Imported $ttft.$rname"  
        fi
    else
       echo "Imported $ttft.$rname" 
    fi
    #echo "local state list"
    #terraform state list -no-color

    #echo $comm > ../data/import_$ttft_$rname.sh

    #terraform state show -state $st $ttft.$rname

    nice -n $sl terraform state show -no-color -state $st $ttft.$rname > ../$ttft-$rname-1.txt 
    #rm -f $fn

else
    echo "State $ttft.$rname already exists skipping import ..."
    nice -n $sl terraform state show -no-color $ttft.$rname > $ttft-$rname-1.txt

fi

rm -f terr*.backup

#echo "exit parallel2 import $rname"