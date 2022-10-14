#!/bin/bash
ttft="aws_redshift_subnet_group"
pref="ClusterSubnetGroups"
idfilt="ClusterSubnetGroupName"

cm="$AWS redshift describe-cluster-subnet-groups"
if [[ "$1" != "" ]]; then
    cm=`printf "$AWS redshift describe-cluster-subnet-groups  | jq '.${pref}[] | select(.${idfilt}==\"%s\")' | jq ." $1`
fi

count=1
echo $cm
awsout=`eval $cm 2> /dev/null`
#echo $awsout | jq .

if [ "$awsout" == "" ];then echo "$cm : You don't have access for this resource" && exit; fi
if [[ "$1" == "" ]]; then count=`echo $awsout | jq ".${pref} | length"`; fi   
if [ "$count" -eq "0" ]; then echo "No resources found exiting .." && exit; fi
count=`expr $count - 1`
for i in `seq 0 $count`; do
    #echo $i
    if [[ "$1" != "" ]]; then
        cname=`echo $awsout | jq -r ".${idfilt}"`
    else
        cname=`echo $awsout | jq -r ".${pref}[(${i})].${idfilt}"`
    fi
    rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
    echo "$ttft ${cname}"
    
    fn=`printf "%s__%s.tf" $ttft $rname`
    if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

    printf "resource \"%s\" \"%s\" {}" $ttft $rname > $fn   
    terraform import $ttft.${rname} "${cname}" | grep Import
    terraform state show -no-color $ttft.${rname} > t1.txt

    rm -f $fn
    subnets=()
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

        else
            if [[ "$t1" == *"subnet-"* ]]; then
                t1=`echo $t1 | tr -d '"|,'`
                subnets+=`printf "\"%s\" " $t1`
                t1=`printf "aws_subnet.%s.id," $t1`
            fi

        fi       

        if [ "$skip" == "0" ]; then echo "$t1" >> $fn ;fi
                
    done <"$file"

    for sub in ${subnets[@]}; do
        sub1=`echo $sub | tr -d '"'`
        echo "calling for $sub1"
        if [ "$sub1" != "" ]; then
            ../../scripts/105-get-subnet.sh $sub1
        fi
    done

    # dependancies here
done

#rm -f t*.txt

