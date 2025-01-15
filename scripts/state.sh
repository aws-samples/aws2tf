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
      
    comm=$(printf "nice -n %s terraform refresh -no-color -state %s &> imp-%s-%s.log" $sl $st $ttft $rname)
    comm2=$(printf "nice -n %s terraform refresh -no-color -state %s > imp-%s-%s.log" $sl $st $ttft $rname)
    #echo $comm

    tsf=$(printf "%s__%s.json" $ttft $rname)
   
    #echo $tsf
    printf "{\n" > $tsf
    printf "  \"version\": 4,\n" >> $tsf
    printf "  \"resources\": [ \n" >> $tsf
    printf "     {\n" >> $tsf
    printf "      \"mode\": \"managed\",\n" >> $tsf
    printf "      \"type\": \"%s\",\n" $ttft >> $tsf
    printf "      \"name\": \"%s\",\n" $rname >> $tsf
    echo '      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",' >> $tsf
    printf "      \"instances\": [ \n" >> $tsf
    printf "       {\n" >> $tsf
    printf "         \"attributes\": {\n" >> $tsf
    printf "         \"id\": \"%s\"\n" $cname >> $tsf
    printf "         }\n" >> $tsf
    printf "       }\n" >> $tsf
    printf "       ]\n" >> $tsf 
    printf "      }\n" >> $tsf
    printf "  ]\n" >> $tsf  
    printf "}\n" >> $tsf
   
    cat $tsf | jq . > $st
  
    eval $comm
    if [ $? -ne 0 ]; then
        echo "--> 2nd Refesh backoff & retry for $rname"
        sl=`echo $((8 + $RANDOM % 20))`
        sleep $sl
        sync;sync
        eval $comm
    fi

    nice -n $sl terraform state show -no-color -state $st $ttft.$rname > ../$ttft-$rname-1.txt 

else
    echo "State $ttft.$rname already exists skipping import ..."
    nice -n $sl terraform state show -no-color $ttft.$rname > $ttft-$rname-1.txt

fi

rm -f terr*.backup

#echo "exit parallel2 import $rname"