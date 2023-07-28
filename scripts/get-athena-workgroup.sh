#!/bin/bash
ttft="aws_athena_workgroup"
pref="WorkGroup"
idfilt="Name"

if [[ "$1" == "" ]]; then
    echo "Must specify query id exiting ..."
    exit
else
    cm=$(printf "$AWS athena get-work-group --work-group $1")
fi

count=1
echo $cm
awsout=$(eval $cm 2>/dev/null)
#echo $awsout | jq .

if [ "$awsout" == "" ]; then echo "$cm : You don't have access for this resource" && exit; fi

count=$(expr $count - 1)
for i in $(seq 0 $count); do
    #echo $i
    cname=$(echo $awsout | jq -r ".${pref}.${idfilt}")
    rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
    echo "$ttft ${cname}"

    fn=$(printf "%s__a_%s.tf" $ttft $rname)
    if [ -f "$fn" ]; then echo "$fn exists already skipping" && continue; fi

    printf "resource \"%s\" \"a_%s\" {}" $ttft $rname >$fn
    terraform import $ttft.a_${rname} "${cname}" | grep Importing
    terraform state show -no-color $ttft.a_${rname} >t1.txt

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
            if [[ ${tt1} == "effective_engine_version" ]]; then skip=1; fi

        fi

        if [ "$skip" == "0" ]; then echo "$t1" >>$fn; fi

    done <"$file"
    # dependancies here
done

#rm -f t*.txt
