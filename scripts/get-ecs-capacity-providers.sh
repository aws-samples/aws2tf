#!/bin/bash
source ../../scripts/functions.sh
ttft="aws_ecs_capacity_provider"
pref="capacityProviders"
idfilt="name"

cm="$AWS ecs describe-capacity-providers"
if [[ "$1" == "" ]]; then
    echo "Usage: $0 <cluster-name>"
    exit
fi
#    cm=`printf "$AWS ecs describe-capacity-providers  | jq '.${pref}[] | select(.${idfilt}==\"%s\")' | jq ." $1`
#fi

count=1
echo $cm
awsout=`eval $cm 2> /dev/null`
#echo $awsout | jq .

if [ "$awsout" == "" ];then echo "$cm : You don't have access for this resource" && exit; fi
if [[ "$1" == "" ]]; then count=`echo $awsout | jq ".${pref} | length"`; fi  
count=`echo $awsout | jq ".${pref} | length"`   
if [ "$count" -eq "0" ]; then echo "No resources found exiting .." && exit; fi
count=`expr $count - 1`
#echo "count=$count"
for i in `seq 0 $count`; do
    #echo $i
    #if [[ "$1" != "" ]]; then
    #    cname=`echo $awsout | jq -r ".${idfilt}"`
    #else
        cname=`echo $awsout | jq -r ".${pref}[(${i})].${idfilt}"`
    #fi
    rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
    echo "$ttft ${cname}"
    
    fn=`printf "%s__%s.tf" $ttft $rname`
    if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

    if [[ $cname == *"FARGATE"* ]];then
        ttft="aws_ecs_cluster_capacity_providers"
        cname=$(echo $1)
        rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
    fi

    echo "$ttft ${cname}"

    fn=`printf "%s__%s.tf" $ttft $rname`
    if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi


    printf "resource \"%s\" \"%s\" {}" $ttft $rname > $fn   
    terraform import $ttft.${rname} "${cname}" | grep Importing
    terraform state show -no-color $ttft.${rname} > t1.txt

    rm -f $fn
 
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
            if [[ ${tt1} == "auto_scaling_group_arn " ]];then 
                fixarn "$tt2"
            fi
            if [[ ${tt1} == "cluster_name" ]];then
                t1=$(printf "%s = aws_ecs_cluster.%s.name\n" $tt1 $1)
            fi
        fi

        if [ "$skip" == "0" ]; then echo "$t1" >> $fn ;fi
                
    done <"$file"
    # dependancies here
done

#rm -f t*.txt

