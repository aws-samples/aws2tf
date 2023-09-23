#!/bin/bash
ttft="aws_autoscaling_group"
pref="AutoScalingGroups"
idfilt="AutoScalingGroupName"

cm="$AWS autoscaling describe-auto-scaling-groups"
if [[ "$1" != "" ]]; then
    cm=$(printf "$cm  | jq '.${pref}[] | select(.${idfilt}==\"%s\")' | jq ." $1)
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
    isw=0
    isfd=0
    isfdwp=0
    lc=$(wc -l t1.txt | awk '{print $1}')
    li=0
    echo $aws2tfmess >$fn
    while IFS= read t1; do
        skip=0
        li=$(expr $li + 1)
        if [[ ${t1} == *"="* ]]; then
            tt1=$(echo "$t1" | cut -f1 -d'=' | tr -d ' ')
            tt2=$(echo "$t1" | cut -f2- -d'=')
            if [[ ${tt1} == "id" ]]; then skip=1; fi
            if [[ ${tt1} == "create_date" ]]; then skip=1; fi
            if [[ ${tt1} == "arn" ]]; then skip=1; fi
            if [[ ${tt1} == "owner_id" ]]; then skip=1; fi

            if [[ ${tt1} == "primary_network_interface_id" ]]; then skip=1; fi
            if [[ ${tt1} == "instance_state" ]]; then skip=1; fi
            if [[ ${tt1} == "private_dns" ]]; then skip=1; fi

            if [[ ${tt1} == "volume_id" ]]; then skip=1; fi
            if [[ ${tt1} == "user_data" ]]; then skip=1; fi
            
            if [[ ${tt1} == "force_delete" ]]; then isfd=1; fi
            if [[ ${tt1} == "force_delete_warm_pool" ]]; then isfdwp=1; fi
            if [[ ${tt1} == "wait_for_capacity_timeout" ]]; then isw=1; fi
            
            if [[ ${tt1} == "warm_pool_size" ]]; then skip=1; fi
            if [[ ${tt1} == "predicted_capacity" ]]; then skip=1; fi
            
            if [[ ${tt1} == "availability_zones" ]]; then
                az=1
            fi
            if [[ ${tt1} == "launch_configuration" ]]; then
                lcn=`echo $tt2 | tr -d '"'`
                t1=`printf "%s = aws_launch_configuration.%s.id" $tt1 $lcn`
            fi
            if [[ ${tt1} == "load_balancers" ]]; then
                lbn=`echo $tt2 | tr -d '"'`
                if [[ $lbn = "[]" ]]; then
                    skip=1
                fi       
            fi
            if [[ ${tt1} == "name" ]]; then
                tt2=`echo $tt2 | tr -d '"'`
                if [[ $tt2 == "lt-"* ]];then
                    t1=`printf "%s = aws_launch_tmplate.%s.name" $tt1 $tt2`
                fi
            fi

            if [[ ${tt1} == "vpc_zone_identifier" ]];then
                if [[ ${az} == "1" ]];then
                    echo "vpc_zone_identifier skipping ..."  
                    skip=1
                        while [[ "$t1" != "]" ]] ;do
                            read line
                            t1=`echo "$line"`
                        done
                fi
            fi
        


        fi

        if [ "$skip" == "0" ]; then echo "$t1" >>$fn; fi
        if [[ $li == $lc ]];then
            echo "last line ? = $t1"
        fi
    done <"$file"
    # dependancies here
    if [[ $lcn != "" ]];then
        ../../scripts/get-launch-configuration.sh $lcn
    fi

    ../../scripts/get-autoscaling-lifecycle-hook.sh $cname
done

#rm -f t*.txt
