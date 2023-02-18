#!/bin/bash
ttft="aws_iam_user_policy_attachment"
pref="AttachedPolicies"
idfilt="PolicyArn"

if [[ "$1" != "" ]]; then
    cm=$(printf "$AWS  iam list-attached-user-policies --user-name $1")
else
    echo "you must pass username as a parameter - exiting ...."
    exit
fi

count=1
echo $cm
awsout=$(eval $cm 2>/dev/null)
#echo $awsout | jq .

if [ "$awsout" == "" ]; then echo "$cm : You don't have access for this resource" && exit; fi
count=$(echo $awsout | jq ".${pref} | length")
if [ "$count" -eq "0" ]; then echo "No resources found exiting .." && exit; fi
count=$(expr $count - 1)
#echo $count
for i in $(seq 0 $count); do
    #echo $i

    cname=$(echo $awsout | jq -r ".${pref}[(${i})].${idfilt}")
    echo "$ttft ${cname}"
    rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}

    fn=$(printf "%s__%s__%s.tf" $ttft $1 $rname)
    if [ -f "$fn" ]; then echo "$fn exists already skipping" && continue; fi

    printf "resource \"%s\" \"%s__%s\" {}\n" $ttft $1 $rname >$fn
    terraform import $ttft.$1__${rname} "${1}/${cname}" | grep Import
    terraform state show -no-color $ttft.${1}__${rname} >t1.txt

    rm -f $fn
    parn=""
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

            if [[ ${tt1} == "policy_arn" ]]; then
                #echo "tt2=$tt2"
                if [[ "${tt2}" == *"service-role"* ]]; then
                    pnam=$(echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"')
                    parn=$(echo $tt2 | tr -d '"')
                    #echo "parn=$parn"
                    #echo "pnam=$pnam"

                fi
                if [[ "${tt2}" == *":policy/"* ]]; then
                    pnam=$(echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"')
                    parn=$(echo $tt2 | tr -d '"')
                    #echo "parn=$parn"
                    #echo "pnam=$pnam"
                    if [[ "$parn" == *":aws:policy"* ]]; then
                        t1=$(printf "%s = \"%s\"" $tt1 $parn)
                    else
                        t1=$(printf "%s = aws_iam_policy.p_%s.arn" $tt1 $pnam)
                    fi

                fi
                skip=0
            fi

        fi

        if [ "$skip" == "0" ]; then echo "$t1" >>$fn; fi

    done <"$file"
    # dependancies here

    if [[ "$pnam" != "" ]]; then
        #echo "Get the Policy name=$pnam arn=$parn"
        ../../scripts/get-iam-policies.sh $parn
    fi
done

#rm -f t*.txt
