#!/bin/bash
ttft="aws_efs_mount_target"
pref="MountTargets"

idfilt="MountTargetId"

cm="$AWS efs describe-mount-targets"
if [[ "$1" != "" ]]; then  
    if [[ ${1} == "fs-"* ]]; then   
        cm=`printf "$AWS efs describe-mount-targets --file-system-id $1"`
    else
        echo "must provide a fs- id as a parameter"
        exit   
    fi
else
    echo "must provide a fs id as a parameter"
    exit   
fi


count=1
echo $cm
awsout=`eval $cm 2> /dev/null`
#echo $awsout | jq . 

if [ "$awsout" == "" ];then echo "$cm : You don't have access for this resource" && exit; fi
count=`echo $awsout | jq ".${pref} | length"`  
if [ "$count" -eq "0" ]; then echo "No resources found exiting .." && exit; fi
echo $count

count=`expr $count - 1`
for i in `seq 0 $count`; do

    cname=`echo $awsout | jq -r ".${pref}[(${i})].${idfilt}"`
    rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
    echo "$ttft ${cname} $rname"
    echo $ttft
    echo $rname

    fn=`printf "%s__%s.tf" $ttft $rname`

    if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

    printf "resource \"%s\" \"%s\" {}\n" $ttft $rname > $fn   

    
    terraform import $ttft.${rname} "${cname}" | grep Import
    terraform state show -no-color $ttft.${rname} > t1.txt

    rm -f $fn
 
    file="t1.txt"
    
    echo $aws2tfmess > $fn
    while IFS= read t1
    do
		skip=0
        if [[ ${t1} == *"="* ]];then
            tt1=`echo "$t1" | cut -f1 -d'=' | tr -d ' '` 
            tt2=`echo "$t1" | cut -f2- -d'='`             
            if [[ ${tt1} == "id" ]];then skip=1; fi  
            if [[ ${tt1} == "create_date" ]];then skip=1; fi  
            if [[ ${tt1} == "arn" ]];then skip=1;fi
            if [[ ${tt1} == "owner_id" ]];then skip=1;fi    
            if [[ ${tt1} == "dns_name" ]];then skip=1;fi 
            if [[ ${tt1} == "file_system_arn" ]];then skip=1;fi 
            if [[ ${tt1} == "network_interface_id" ]];then skip=1;fi 
            if [[ ${tt1} == "mount_target_dns_name" ]];then skip=1;fi 
            if [[ ${tt1} == "availability_zone_name" ]];then skip=1;fi 
            if [[ ${tt1} == "availability_zone_id" ]];then skip=1;fi 
                      

            if [[ ${tt1} == "file_system_id" ]];then
                tt2=`echo $tt2 | tr -d '"'`
                t1=`printf "%s = aws_efs_file_system.%s.id" $tt1 $tt2`
            fi


        fi

        if [ "$skip" == "0" ]; then echo "$t1" >> $fn ;fi
                
    done <"$file"

    # dependancies here
done

#rm -f t*.txt

