#!/bin/bash
ttft="aws_key_pair"
pref="KeyPairs"
idfilt="KeyName"

cm="$AWS ec2 describe-key-pairs"
if [[ "$1" != "" ]]; then
    cm=$(printf "$AWS ec2 describe-key-pairs --key-names $1")
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

    cname=$(echo $awsout | jq -r ".${pref}[(${i})].${idfilt}")

    rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
    echo "$ttft ${cname}"

    fn=$(printf "%s__%s.tf" $ttft $rname)
    dn=$(printf "data-%s__%s.tf" $ttft $rname)
    if [ -f "$fn" ]; then echo "$fn exists already skipping" && continue; fi

    printf "resource \"%s\" \"%s\" {}" $ttft $rname >$fn
    terraform import $ttft.${rname} "${cname}" | grep Importing
    terraform state show -no-color $ttft.${rname} >t1.txt

    printf "data \"%s\" \"%s\" {\n" $ttft $rname >$dn
    printf "key_name  = \"%s\"\n" $cname >>$dn
    printf "include_public_key = true\n" >>$dn
    printf "}\n" $ttft $rname >>$dn



    rm -f $fn

    file="t1.txt"
    echo $aws2tfmess >$fn
    while IFS= read t1; do
        skip=0
        if [[ ${t1} == *"="* ]]; then
            tt1=$(echo "$t1" | cut -f1 -d'=' | tr -d ' ')
            tt2=$(echo "$t1" | cut -f2- -d'=')
            if [[ ${tt1} == "id" ]]; then 
                printf "public_key = data.%s.%s.public_key\n" $ttft $rname >>$fn
                printf "lifecycle {\n" >>$fn
                printf "   ignore_changes = [public_key]\n" >>$fn
                printf "}\n" >>$fn
                skip=1; 
            fi

            if [[ ${tt1} == "create_date" ]]; then skip=1; fi
            if [[ ${tt1} == "arn" ]]; then skip=1; fi
            if [[ ${tt1} == "owner_id" ]]; then skip=1; fi
            if [[ ${tt1} == "key_type" ]] || [[ ${tt1} == "key_pair_id" ]] || [[ ${tt1} == "fingerprint" ]]; then skip=1; fi
        fi

        if [ "$skip" == "0" ]; then echo "$t1" >>$fn; fi

    done <"$file"
    # dependancies here
done

#rm -f t*.txt
