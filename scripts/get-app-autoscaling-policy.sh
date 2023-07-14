#!/bin/bash
ttft="aws_appautoscaling_policy"
pref="ScalingPolicies"
idfilt="ResourceId"

if [[ "$1" == "" ]]; then
    echo "must pass service namespace as first parameter"
    exit
fi

if [[ "$1" == "ecs" ]]; then
    if [[ "$2" == "" ]]; then
        echo "must pass cluster name as second parameter"
        exit
    fi
    if [[ "$2" == "" ]]; then
        echo "must pass ecs service name as second parameter"
        exit
    fi
else
    echo "must pass ecs as first parameter - only ecs supported for now"
    exit
fi

ss=printf("service/%s/%s", $1, $2)


cm="$AWS application-autoscaling describe-scaling-policies"
if [[ "$1" != "" ]]; then
    cm=$(printf "$AWS application-autoscaling describe-scaling-policies  --service-namespace %s | jq '.${pref}[] | select(.${idfilt}==\"%s\")' | jq ." $1 $ss)
fi

count=1
#echo $cm

awsout=$(eval $cm 2>/dev/null)
#echo $awsout | jq .

if [ "$awsout" == "" ]; then echo "$cm : You don't have access for this resource" && exit; fi
if [[ "$1" == "" ]]; then count=$(echo $awsout | jq ".${pref} | length"); fi
if [ "$count" -eq "0" ]; then echo "No resources found exiting .." && exit; fi
count=$(expr $count - 1)
for i in $(seq 0 $count); do
    #echo $i

    cname=$(echo $awsout | jq -r ".${idfilt}")
    sd=$(echo $awsout | jq -r ".ScalableDimension")
    pn=$(echo $awsout | jq -r ".PolicyName")

    rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
    rname2=${sd//:/_} && rname2=${rname2//./_} && rname2=${rname2//\//_}
    rname3=${pn//:/_} && rname3=${rname3//./_} && rname3=${rname3//\//_}

    echo "$ttft $1 ${cname} $sd $pn"
    #echo "$rname $rname2 $rname3"

    fn=$(printf "%s__%s__%s__%s__%s.tf" $ttft $1 $rname $rname2 $rname3)
    if [ -f "$fn" ]; then echo "$fn exists already skipping" && continue; fi
    #echo $fn

    printf "resource \"%s\" \"%s__%s__%s__%s\" {}\n" $ttft $1 $rname $rname2 $rname3 >$fn
    #cat $fn
    terraform import $ttft.${1}__${rname}__${rname2}__${rname3} "$1/${cname}/$sd/$pn"
    if [ "$?" != "0" ]; then
        echo "Error importing $1/${cname}/$sd/$pn" && exit
    fi

    terraform state show -no-color $ttft.${1}__${rname}__${rname2}__${rname3} >t1.txt

    rm -f $fn

    file="t1.txt"
    echo $aws2tfmess >$fn
    while IFS= read t1; do
        skip=0
        if [[ ${t1} == *"="* ]]; then
            tt1=$(echo "$t1" | cut -f1 -d'=' | tr -d ' ')
            tt2=$(echo "$t1" | cut -f2- -d'=')

            if [[ ${tt1} == "alarm_arns" ]]; then
                # skip the block
                tt2=$(echo $tt2 | tr -d '"')
                skip=1
                while [ "$t1" != "]" ] && [ "$tt2" != "[]" ]; do
                    read line
                    t1=$(echo "$line")
                done
            fi

            if [[ ${tt1} == "id" ]]; then skip=1; fi
            if [[ ${tt1} == "create_date" ]]; then skip=1; fi
            if [[ ${tt1} == "arn" ]]; then skip=1; fi
            if [[ ${tt1} == "owner_id" ]]; then skip=1; fi

            if [[ ${tt1} == "resource_id" ]]; then
                t1=$(printf "%s = service/${aws_ecs_cluster.%s.name}/${aws_ecs_service.%s.name}" $tt1 $t2 $t3)
            fi

        fi

        if [ "$skip" == "0" ]; then echo "$t1" >>$fn; fi

    done <"$file"
    # dependancies here
done

#rm -f t*.txt
