#!/bin/bash
ttft="aws_flow_log"
pref="FlowLogs"
idfilt="FlowLogId"

cm="$AWS ec2 describe-flow-logs"
if [[ "$1" != "" ]]; then
    cm=$(printf "$AWS ec2 describe-flow-logs  | jq '.${pref}[] | select(.${idfilt}==\"%s\")' | jq ." $1)
fi

count=1
echo $cm
awsout=$(eval $cm 2>/dev/null)
#echo $awsout | jq .

if [ "$awsout" == "" ]; then echo "$cm : You don't have access for this resource" && exit; fi
if [[ "$1" == "" ]]; then count=$(echo $awsout | jq ".${pref} | length"); fi
if [ "$count" -eq "0" ]; then echo "No resources found exiting .." && exit; fi
count=$(expr $count - 1)
for i in $(seq 0 $count); do
    #echo $i
    if [[ "$1" != "" ]]; then
        cname=$(echo $awsout | jq -r ".${idfilt}")
    else
        cname=$(echo $awsout | jq -r ".${pref}[(${i})].${idfilt}")
    fi
    rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
    echo "$ttft ${cname}"

    fn=$(printf "%s__%s.tf" $ttft $rname)
    if [ -f "$fn" ]; then echo "$fn exists already skipping" && continue; fi

    printf "resource \"%s\" \"%s\" {}" $ttft $rname >$fn
    terraform import $ttft.${rname} "${cname}" | grep Importing
    terraform state show -no-color $ttft.${rname} >t1.txt

    rm -f $fn

    file="t1.txt"
    lgd=0
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
            if [[ ${tt1} == "log_group_name" ]]; then skip=1; fi
            if [[ ${tt1} == "log_destination" ]]; then
                lgd=1
                rarn=$(echo $tt2 | tr -d '"')
                if [[ $rarn == *"*" ]]; then
                    trole=$(echo $tt2 | rev | cut -f2 -d':' | rev | tr -d '"')
                else
                    trole=$(echo $tt2 | rev | cut -f1 -d':' | rev | tr -d '"')
                fi
                skip=1
                t1=$(printf "%s = aws_cloudwatch_log_group.%s.arn" $tt1 $trole)

            fi
            if [[ ${tt1} == "log_format" ]]; then

                if [[ $t1 == *"\${"* ]]; then
                    t1=${t1//$/&}
                fi
                printf "lifecycle {\n" >>$fn
                printf "   ignore_changes = [log_format]\n" >>$fn
                printf "}\n" >>$fn

            fi

        fi

        if [ "$skip" == "0" ]; then echo "$t1" >>$fn; fi

    done <"$file"
    # dependancies here
done

#rm -f t*.txt
