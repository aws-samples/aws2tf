#!/bin/bash
ttft="aws_appautoscaling_target"
pref="ScalableTargets"
idfilt="ResourceId"

if [[ "$1" == "" ]]; then
    echo "must pass service namespace as first parameter"
    exit
fi

if [[ "$2" == "" ]]; then
    echo "must pass service id as first parameter"
    exit
fi

cm="$AWS application-autoscaling describe-scalable-targets"
if [[ "$1" != "" ]]; then
    cm=$(printf "$AWS application-autoscaling describe-scalable-targets  --service-namespace %s | jq '.${pref}[] | select(.${idfilt}==\"%s\")' | jq ." $1 $2)
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
    rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
    rname2=${sd//:/_} && rname2=${rname2//./_} && rname2=${rname2//\//_}

    echo "$ttft $1 ${cname} $sd"

    fn=$(printf "%s__%s__%s__%s.tf" $ttft $1 $rname $rname2)
    if [ -f "$fn" ]; then echo "$fn exists already skipping" && continue; fi

    printf "resource \"%s\" \"%s__%s__%s\" {}\n" $ttft $1 $rname $rname2 >$fn
    terraform import $ttft.${1}__${rname}__${rname2} "$1/${cname}/$sd"
    if [ "$?" != "0" ]; then
        echo "Error importing $1/${cname}/$sd" && exit
    fi

    terraform state show -no-color $ttft.${1}__${rname}__${rname2} >t1.txt

    rm -f $fn

    file="t1.txt"
    echo $aws2tfmess >$fn
    while IFS= read t1; do
        skip=0
        if [[ ${t1} == *"="* ]]; then
            tt1=$(echo "$t1" | cut -f1 -d'=' | tr -d ' ')
            tt2=$(echo "$t1" | cut -f2- -d'=')
            if [[ ${tt1} == "id" ]]; then skip=1; fi
            if [[ ${tt1} == "create_date" ]]; then skip=1; fi
            if [[ ${tt1} == "arn" ]]; then skip=1; fi
            if [[ ${tt1} == "owner_id" ]]; then skip=1; fi

            if [[ ${tt1} == "role_arn" ]]; then
                tt2=$(echo $tt2 | tr -d '"')
                tstart=$(echo $tt2 | cut -f1-3 -d ':')
                tacc=$(echo $tt2 | cut -f4 -d ':')
                tend=$(echo $tt2 | cut -f5- -d ':')
                tsub="%s"
                t1=$(printf "%s = format(\"%s:%s:%s\",data.aws_caller_identity.current.account_id)" $tt1 $tstart $tsub $tend)
                # don't get target group - as ecs servioce creates this for us
                #tgarn=$(echo $tt2)
            fi

        fi

        if [ "$skip" == "0" ]; then echo "$t1" >>$fn; fi

    done <"$file"
    # dependancies here
done

#rm -f t*.txt
