#!/bin/bash
ttft="aws_network_acl"
pref="NetworkAcls"
idfilt="NetworkAclId"
c=0
cm="$AWS ec2 describe-network-acls"
if [[ "$1" == *"acl-"* ]]; then
    #cm=`printf "$AWS ec2 describe-network-acls  | jq '.${pref}[] | select(.${idfilt}==\"%s\")' | jq ." $1`
    cm="$AWS ec2 describe-network-acls --network-acl-ids $1"
elif [[ "$1" == *"vpc-"* ]]; then
    cm="$AWS ec2 describe-network-acls --filters \"Name=vpc-id,Values=$1\""
else
    cm="$AWS ec2 describe-network-acls"
fi

count=1

#echo $cm
awsout=`eval $cm 2> /dev/null`
#echo $awsout | jq .

if [ "$awsout" == "" ];then echo "$cm : You don't have access for this resource" && exit; fi
if [[ "$1" != "" ]]; then count=`echo $awsout | jq ".${pref} | length"`; fi  
if [ "$count" -eq "0" ]; then echo "No resources found exiting .." && exit; fi
count=`expr $count - 1`

for i in `seq 0 $count`; do
    #echo $i

    cname=`echo $awsout | jq -r ".${pref}[(${i})].${idfilt}"`
    isdef=`echo $awsout | jq -r ".${pref}[(${i})].IsDefault"`
    echo $isdef
    if [[ "$isdef" == "true" ]];then
        ttft="aws_default_network_acl"
    fi
    rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
    echo "$ttft ${cname}"
    
    fn=`printf "%s__%s.tf" $ttft $rname`
    if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

    printf "resource \"%s\" \"%s\" {}" $ttft $rname > $fn   
    terraform import $ttft.${rname} "${cname}" | grep Import
    terraform state show -no-color $ttft.${rname} > t1.txt

    rm -f $fn

    echo $isdef
    file="t1.txt"
    echo $aws2tfmess > $fn
    while IFS= read t1
    do
		skip=0
        if [[ ${t1} == *"="* ]];then
            tt1=`echo "$t1" | cut -f1 -d'=' | tr -d ' '` 
            tt2=`echo "$t1" | cut -f2- -d'='`             
            if [[ ${tt1} == "id" ]];then skip=1; fi  
            if [[ ${tt1} == "create_date" ]];then skip=1; fi  
            if [[ ${tt1} == "arn" ]];then skip=1;fi
            if [[ ${tt1} == "owner_id" ]];then skip=1;fi 
            if [[ ${tt1} == "vpc_id" ]]; then
                if [[ "$isdef" != "true" ]];then
                    echo "in vpcid ! $isdef"
                    vpcid=`echo $tt2 | tr -d '"'`
                    t1=`printf "%s = aws_vpc.%s.id" $tt1 $vpcid`
                else
                    skip=1
                fi
            fi

        else
            if [[ "$t1" == *"subnet-"* ]]; then
                t1=`echo $t1 | tr -d '"|,'`
                t1=`printf "aws_subnet.%s.id," $t1`
            fi

        fi

        if [ "$skip" == "0" ]; then echo "$t1" >> $fn ;fi
                
    done <"$file"
    # dependancies here

done

#rm -f t*.txt

