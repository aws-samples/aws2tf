#!/bin/bash
ttft="aws_vpclattice_listener_rule"
pref="items"
idfilt="id"

cm="$AWS vpc-lattice list-listeners"
if [[ "$1" != "" ]]; then
    if [[ "$1" == "svc-"* ]]; then

        if [[ "$2" != "" ]]; then
            if [[ "$2" == "listener-"* ]]; then
                cm=$(printf "$AWS vpc-lattice list-rules --service-identifier $1 --listener-identifier $2")
            fi
        else
            echo "must pass listener identifier listener-* as second parameter"
            exit
        fi

    fi
else
    echo "must pass service identifier svc-* as first parameter"
    exit
fi

count=1
#echo $cm
awsout=$(eval $cm 2>/dev/null)
#echo $awsout | jq .

if [ "$awsout" == "" ]; then echo "$cm : You don't have access for this resource" && exit; fi
if [[ "$1" == "" ]]; then count=$(echo $awsout | jq ".${pref} | length"); fi
count=$(echo $awsout | jq ".${pref} | length")
if [ "$count" -eq "0" ]; then echo "No resources found exiting .." && exit; fi
count=$(expr $count - 1)
for i in $(seq 0 $count); do
    #echo $i

    cname=$(echo $awsout | jq -r ".${pref}[(${i})].${idfilt}")

    rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
    echo "$ttft $1 $2 ${cname}"

    fn=$(printf "%s__%s__%s__%s.tf" $ttft $1 $2 $rname)
    if [ -f "$fn" ]; then echo "$fn exists already skipping" && continue; fi

    printf "resource \"%s\" \"%s__%s__%s\" {}" $ttft $1 $2 $rname >$fn
    #echo ">> Importing for $fn"
    terraform import $ttft.$1__$2__${rname} "$1/$2/${cname}"
    #echo ">> Import status $?"
    if [[ $? -ne 0 ]];then
        echo ">> Import failed for $fn"
        rm -f $fn
        continue
    fi
    
    terraform state show -no-color $ttft.$1__$2__${rname} >t1.txt

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
            if [[ ${tt1} == "status" ]]; then skip=1; fi
            if [[ ${tt1} == "listener_id" ]]; then skip=1; fi
            if [[ ${tt1} == "created_at" ]]; then skip=1; fi
            if [[ ${tt1} == "last_updated_at" ]]; then skip=1; fi
            if [[ ${tt1} == "rule_id" ]]; then skip=1; fi

            if [[ ${tt1} == "dns_entry" ]]; then
                # skip the block
                tt2=$(echo $tt2 | tr -d '"')
                skip=1
                while [ "$t1" != "]" ] && [ "$tt2" != "[]" ]; do
                    read line
                    t1=$(echo "$line")
                done
            fi

            if [[ ${tt1} == "service_identifier" ]]; then
                si=$(echo $tt2 | tr -d '"')
                t1=$(printf "$tt1 = aws_vpclattice_service.%s.id" $si)
            fi

            if [[ ${tt1} == "service_arn" ]]; then
                sa=$(echo $tt2 | tr -d '"')
                t1=$(printf "$tt1 = aws_vpclattice_service.%s.arn" $1)
            fi

        fi

        if [ "$skip" == "0" ]; then echo "$t1" >>$fn; fi

    done <"$file"
    # dependancies here
    # get listener rules
done

#rm -f t*.txt
