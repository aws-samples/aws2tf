#!/bin/bash
ttft="aws_vpclattice_target_group_attachment"
pref="items"
idfilt="id"
ncpu=2

if [[ "$1" != "" ]]; then
    if [[ "$1" == "tg-"* ]]; then
        cm=$(printf "$AWS vpc-lattice list-targets  --target-group-identifier %s | jq ." $1)
    fi
else
    echo "must pass target identifier tg-* as a parameter"
    exit
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
    echo "i=$i"


    cname=$(echo $awsout | jq -r ".${pref}[(${i})].${idfilt}")
    rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
    echo "$ttft ${cname}"

    fn=$(printf "%s__%s.tf" $ttft $rname)
    if [ -f "$fn" ]; then echo "$fn exists already skipping" && continue; fi

    echo "--> Calling parallel import3 sub $ttft $1"
    . ../../scripts/parallel_import3.sh $ttft $1
    jc=$(jobs -r | wc -l | tr -d ' ')
    while [ $jc -gt $ncpu ]; do
        echo "Throttling - $jc Terraform imports in progress"
        sleep 10
        jc=$(jobs -r | wc -l | tr -d ' ')
    done

    jc=$(jobs -r | wc -l | tr -d ' ')
    echo "Waiting for $jc Terraform imports"
    wait
    echo "Finished importing"
done

for i in $(seq 0 $count); do


    cname=$(echo $awsout | jq -r ".${pref}[(${i})].${idfilt}")
    rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}

    echo "$ttft ${cname}"

    echo "$ttft $cname tf files"
    fn=$(printf "%s__%s.tf" $ttft $rname)
    if [ -f "$fn" ]; then echo "$fn exists already skipping" && continue; fi

    file=$(printf "%s-%s-1.txt" $ttft $rname)
    if [ ! -f "$file" ]; then echo "$file does not exist" && continue; fi

    rm -f $fn

    islambda=0
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

            if [[ ${tt1} == "port" ]]; then
                pn=$(echo $tt2 | tr -d '"')
                if [[ $pn == "0" ]]; then
                    skip=1
                fi
            fi

            if [[ ${tt1} == "target_group_identifier" ]]; then
                tgi=$(echo $tt2 | tr -d '"')
                t1=$(printf "$tt1 = aws_vpclattice_target_group.%s.id" $tgi)
            fi
        fi

        if [ "$skip" == "0" ]; then echo "$t1" >>$fn; fi

    done <"$file"
    # dependancies here

done

#rm -f t*.txt
