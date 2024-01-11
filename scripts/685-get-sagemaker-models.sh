#!/bin/bash
ttft="aws_sagemaker_model"
pref="Models"
idfilt="ModelName"

cm="$AWS sagemaker list-models"
if [[ "$1" != "" ]]; then
    if [[ "$1" == "arn:"* ]]; then
        cm=$(printf "$AWS iam list-access-keys  | jq '.${pref}[] | select(.ModelArn==\"%s\")' | jq ." $1)
    else
        cm=$(printf "$AWS iam list-access-keys  | jq '.${pref}[] | select(.${idfilt}==\"%s\")' | jq ." $1)
    fi
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
            if [[ ${tt1} == "execution_role_arn" ]]; then
                trarn=$(echo $tt2 | tr -d '"')
                skip=0
                trole=$(echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"')
                t1=$(printf "%s = aws_iam_role.r-%s.arn" $tt1 ${trole//./_})

            fi

        fi

        if [ "$skip" == "0" ]; then echo "$t1" >>$fn; fi

    done <"$file"
    # dependancies here
    if [[ "$trarn" != "" ]]; then
        ../../scripts/050-get-iam-roles.sh $trarn
    fi

done

#rm -f t*.txt
