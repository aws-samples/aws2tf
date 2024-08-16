#!/bin/bash
ttft="aws_vpclattice_target_group"
pref="items"
idfilt="id"

cm="$AWS vpc-lattice list-target-groups"
if [[ "$1" != "" ]]; then
    if [[ "$1" == "tg-"* ]]; then
        # fast out
        fn=$(printf "%s__%s.tf" $ttft $1)
        if [ -f "$fn" ]; then echo "$fn exists already skipping" && exit;fi

        cm=$(printf "$AWS vpc-lattice list-target-groups | jq '.${pref}[] | select(.${idfilt}==\"%s\")' | jq ." $1)
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

            #if [[ ${tt1} == "protocol_version" ]]; then
            #    pv=$(echo $tt2 | tr -d '"')
            #    echo ">> $pv"
            #    if [[ "$pv" == "HTTP1" ]];then
            #        echo ">> skipping $pv"
            #        skip=1;
            #    fi
            #fi

            if [[ ${tt1} == "type" ]]; then
                ty=$(echo $tt2 | tr -d '"')
                if [[ $ty == *"LAMBDA"* ]]; then
                    islambda=1
                fi
            fi

            if [[ ${tt1} == "vpc_identifier" ]]; then
                vpcid=$(echo $tt2 | tr -d '"')
                t1=$(printf "%s = aws_vpc.%s.id" $tt1 $vpcid)
            fi

            if [[ ${tt1} == "target_group_identifier" ]]; then
                tgi=$(echo $tt2 | tr -d '"')
                t1=$(printf "$tt1 = aws_vpclattice_target_group.%s.id" $tgi)
            fi

        else
            if [[ ${islambda} == "1" ]]; then
                if [[ ${t1} == *"config {"* ]]; then
                    # skip the block
                    echo "skip block"
                    skip=1
                    while [ "$t1" != "}" ]; do
                        read line
                        t1=$(echo "$line")
                    done
                fi
            fi

        fi

        if [ "$skip" == "0" ]; then echo "$t1" >>$fn; fi

    done <"$file"
    # dependancies here
    # get listener rules
    if [[ $vpcid != "" ]]; then
        ../../scripts/100-get-vpc.sh $vpcid
    fi
    # get target group attachments - can't be imported
    #../../scripts/get-vpclattice-target-group-attachments.sh $1

done

#rm -f t*.txt
