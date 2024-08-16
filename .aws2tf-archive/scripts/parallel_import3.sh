#!/bin/bash
if [ "$1" == "" ]; then
    echo "must specify resource type (ttft)"
    exit
fi

if [ "$2" == "" ]; then
    echo "must specify resource name (cname)"
    exit
fi

ttft=$(echo $1 | tr -d '"')
cname=$(echo $2 | tr -d '"')

if [ "$3" == "" ]; then
    rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
else
    rname=$(echo $3 | tr -d '"')
fi

if [[ $4 != "" ]]; then
    if [[ $4 == *"="* ]]; then
        lhs=$(echo $4 | cut -f1 -d'=' | tr -d ' |"')
        rhs=$(echo $4 | cut -f2 -d'=' | tr -d ' |"')
    fi
fi

sl=$(echo $((1 + $RANDOM % 15)))
# override rname for aws_s3_bucket
if [[ $ttft == "aws_s3_bucket" ]]; then
    rname=$(printf "b_%s" $rname)
fi

echo "Importing $ttft $cname $rname $lhs $rhs"
st=$(printf "%s__%s.tfstate" $1 $rname)
if [ -f "$st" ]; then echo "$st exists already skipping" && exit; fi

#echo "parallel2 list check"
(nice -n $sl terraform state list 2>/dev/null | grep ${ttft}.${rname}) >/dev/null
if [[ $? -ne 0 ]]; then

    #echo "Import $rname"
    #terraform state rm $ttft.$rname > /dev/null
    mkdir -p pi2
    cd pi2

    #cp ../aws.tf .
    ls ../.terraform >/dev/null
    if [[ $? -eq 0 ]]; then
        #echo "pi2 using root provider"
        ln -s ../aws.tf aws.tf 2>/dev/null
        ln -s ../main-vars.tf main-vars.tf 2>/dev/null
        ln -s ../data-aws.tf data-aws.tf 2>/dev/null
        ln -s ../.terraform .terraform 2>/dev/null
        ln -s ../.terraform.lock.hcl .terraform.lock.hcl 2>/dev/null
    else
        echo "pi2 using initing TF provider"
        sl=$(echo $((1 + $RANDOM % 15)))
        terraform init -no-color >/dev/null
        if [ $? -ne 0 ]; then
            echo "init backoff & retry for $cname"
            sleep $sl
            terraform init -no-color >/dev/null
            if [ $? -ne 0 ]; then
                echo "init long backoff & retry with full errors for $cname"
                sleep 20
                terraform init -no-color >/dev/null
            fi
        fi
    fi



    tsf=$(printf "%s__%s.json" $ttft $rname)

    #echo $tsf
    printf "{\n" >$tsf
    printf "  \"version\": 4,\n" >>$tsf
    printf "  \"resources\": [ \n" >>$tsf
    printf "     {\n" >>$tsf
    printf "      \"mode\": \"managed\",\n" >>$tsf
    printf "      \"type\": \"%s\",\n" $ttft >>$tsf
    printf "      \"name\": \"%s\",\n" $rname >>$tsf
    echo '      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",' >>$tsf
    printf "      \"instances\": [ \n" >>$tsf
    printf "       {\n" >>$tsf
    printf "         \"attributes\": {\n" >>$tsf

    if [[ $ttft == "aws_vpclattice_target_group_attachment" ]]; then
        tid=$(aws vpc-lattice list-targets --target-group-identifier tg-0c6f94c4ae7a3b620 --query 'items[0].id' --output text)
        pt=$(aws vpc-lattice list-targets --target-group-identifier tg-0c6f94c4ae7a3b620 --query 'items[].port' --output text)
        if [[ $pt == "" ]]; then pt=0; fi

        #printf "         \"target\": [\n" >>$tsf
        #printf "           {\n" >>$tsf
        #printf "             \"id\": \"%s\",\n" $tid >>$tsf
        #printf "             \"port\": %s\n" $pt >>$tsf
        #printf "           }\n" >>$tsf
        #printf "         ],\n" >>$tsf
        printf "         \"target_group_identifier\": \"%s\",\n" $cname >>$tsf
        printf "         \"id\": \"%s/%s/%s\"\n" $cname $tid $pt >>$tsf


    elif [[ $ttft == "aws_iam_user_policy_attachment" ]]; then
        printf "         \"%s\": \"%s\",\n" $lhs $rhs >>$tsf
        printf "         \"policy_arn\": \"%s\",\n" $cname >>$tsf
        printf "         \"id\": \"%s\"\n" ${rhs}-${cname} >>$tsf
    elif [[ $ttft == "aws_security_group_rule" ]]; then
        if [[ $lhs == *"sg"* ]]; then
            sg=$(echo $rhs | cut -f1 -d'_')
            ty=$(echo $rhs | cut -f2 -d'_')
            pr=$(echo $rhs | cut -f3 -d'_')
            p1=$(echo $rhs | cut -f4 -d'_')
            p2=$(echo $rhs | cut -f5 -d'_')
            cd=$(echo $rhs | cut -f6 -d'_')
            idv=$(date +%y%m%d%H%M%S)
            printf "         \"id\": \"sgrule-%s\",\n" $sg $idv >>$tsf
            printf "         \"security_group_id\": \"%s\",\n" $sg >>$tsf
            printf "         \"protocol\": \"%s\",\n" $pr >>$tsf
            printf "         \"from_port\": \"%s\",\n" $p1 >>$tsf
            printf "         \"to_port\": \"%s\",\n" $p2 >>$tsf
            if [[ $lhs == "sg1" ]]; then
                printf "         \"cidr_blocks\": [\n" >>$tsf
                printf "         \"%s\"\n" $cd >>$tsf
                printf "         ],\n" >>$tsf
            fi
            if [[ $lhs == "sg2" ]]; then
                printf "         \"self\": true,\n" >>$tsf
            fi
            if [[ $lhs == "sg3" ]]; then
                printf "         \"source_security_group_id\": \"%s\",\n" $cd >>$tsf
            fi

            printf "         \"type\": \"%s\"\n" $ty >>$tsf
        fi
    else
        printf "         \"id\": \"%s\"\n" $cname >>$tsf
    fi

    printf "         }\n" >>$tsf
    printf "       }\n" >>$tsf
    printf "       ]\n" >>$tsf
    printf "      }\n" >>$tsf
    printf "  ]\n" >>$tsf
    printf "}\n" >>$tsf

    cat $tsf | jq . >$st

    #echo $tsf
    #echo $st

    comm=$(printf "nice -n %s terraform refresh -no-color -state %s &> imp1-%s-%s.log" $sl $st $ttft $rname)
    comm2=$(printf "nice -n %s terraform refresh -no-color -state %s > imp2-%s-%s.log" $sl $st $ttft $rname)
    
    #echo $comm
    eval $comm
    if [ $? -ne 0 ]; then
        echo "--> 2nd Refesh backoff & retry for $rname"
        sl=$(echo $((3 + $RANDOM % 20)))
        sleep $sl
        sync
        sync
        echo $comm2
        eval $comm2
    fi

    nice -n $sl terraform state show -no-color -state $st $ttft.$rname >../$ttft-$rname-1.txt

else
    echo "State $ttft.$rname already exists skipping import ..."
    nice -n $sl terraform state show -no-color $ttft.$rname >$ttft-$rname-1.txt

fi

rm -f terr*.backup

#echo "exit parallel3 import $rname"
