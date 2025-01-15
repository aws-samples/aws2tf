#!/bin/bash
ttft="aws_vpclattice_access_log_subscription"
pref="items"
idfilt="id"

# parameter service network or service
cm="$AWS vpc-lattice list-listeners"
if [[ "$1" != "" ]]; then
    if [[ "$1" == "svc-"* ]] ||[[ "$1" == "sn-"* ]]; then
        cm=$(printf "$AWS vpc-lattice list-access-log-subscriptions --resource-identifier $1")
    fi
else
    echo "must pass resource identifier (service or service network) as a parameter"
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

    cname=$(echo $awsout | jq -r ".${pref}[(${i})].${idfilt}")
    
    rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
    echo "$ttft ${cname}"

    fn=$(printf "%s__%s__%s.tf" $ttft $1 $rname)
    if [ -f "$fn" ]; then echo "$fn exists already skipping" && continue; fi

    printf "resource \"%s\" \"%s__%s\" {}" $ttft $1 $rname >$fn
    terraform import $ttft.$1__${rname} "$1/${cname}" | grep Importing
    terraform state show -no-color $ttft.$1__${rname} >t1.txt

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
            if [[ ${tt1} == "resource_arn" ]]; then  skip=1; fi


            if [[ ${tt1} == "resource_identifier" ]]; then
                si=$(echo $tt2 | tr -d '"')
                if [[ $si == "svc-"* ]];then
                    t1=$(printf "$tt1 = aws_vpclattice_service.%s.id" $si)
                elif [[ $si == "sn-"* ]];then
                    t1=$(printf "$tt1 = aws_vpclattice_service_network.%s.id" $si)
                else
                    echo "Warning: unexpected value=$si"
                fi
            fi


        fi

        if [ "$skip" == "0" ]; then echo "$t1" >>$fn; fi

    done <"$file"
    # dependancies here
    # get listener rules
done

#rm -f t*.txt
