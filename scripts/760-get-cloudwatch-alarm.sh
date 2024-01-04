#!/bin/bash
mysub=$(echo $AWS2TF_ACCOUNT)
myreg=$(echo $AWS2TF_REGION)
ttft="aws_cloudwatch_metric_alarm"
pref="MetricAlarms"
idfilt="AlarmName"

cm="$AWS cloudwatch describe-alarms"
if [[ "$1" != "" ]]; then
    cm=$(printf "$AWS cloudwatch describe-alarms | jq '.${pref}[] | select(.${idfilt}==\"%s\")' | jq ." $1)
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
    rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_} && rname=${rname//@/_at_}
    echo "$ttft ${cname}"

    fn=$(printf "%s__%s.tf" $ttft $rname)
    if [ -f "$fn" ]; then echo "$fn exists already skipping" && continue; fi

    printf "resource \"%s\" \"%s\" {}" $ttft $rname >$fn
    terraform import $ttft.${rname} "${cname}" | grep Importing

    terraform state show -no-color $ttft.${rname} >t1.txt
    if [[ $? -ne 0 ]]; then 
        echo "WARNING: $ttft $cname - not created or imported" 
        rm -f $fn
        continue
    fi

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
            if [[ ${tt1} == "datapoints_to_alarm" ]]; then
                tt2=$(echo $tt2 | tr -d '"')
                if [[ ${tt2} == "0" ]]; then skip=1; fi
            fi
        fi

        if [ "$skip" == "0" ]; then
            at1=$(echo $t1 | tr -d ' |"')
            if [[ "$at1" == "arn:aws:"* ]]; then
                tstart=$(echo $at1 | cut -f1-3 -d ':')
                treg=$(echo $at1 | cut -f4 -d ':')
                tacc=$(echo $at1 | cut -f5 -d ':')
                tend=$(echo $at1 | cut -f6- -d ':')
                tsub="%s"
                tcomm=","

                if [[ "$treg" != "" ]] || [[ "$tacc" != "" ]]; then
                    if [[ "$tend" == *"," ]]; then
                        tend=$(echo ${tend%?})
                    fi
                    if [[ "$mysub" == "$tacc" ]]; then
                        if [[ "$treg" != "" ]]; then
                            t1=$(printf "format(\"%s:%s:%s:%s\",data.aws_region.current.name,data.aws_caller_identity.current.account_id)," $tstart $tsub $tsub "$tend")
                        else
                            t1=$(printf "format(\"%s::%s:%s\",data.aws_caller_identity.current.account_id)," $tstart $tsub "$tend")

                        fi
                    fi
                fi

            fi

            echo "$t1" >>$fn
        fi

    done <"$file"
    # dependancies here
done

#rm -f t*.txt
