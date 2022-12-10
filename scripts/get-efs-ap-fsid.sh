#!/bin/bash
ttft="aws_efs_access_point"
pref="AccessPoints"

idfilt="FileSystemId"
cm="$AWS efs describe-access-points"
if [[ "$1" != "" ]]; then  
    if [[ ${1} == "fs-"* ]]; then   
        cm=`printf "$AWS efs describe-access-points  | jq '.${pref}[] | select(.${idfilt}==\"%s\")' | jq ." $1`
    else
        echo "must provide a fs id as a parameter"
        exit   
    fi
fi


count=1
#echo $cm
awsout=`eval $cm 2> /dev/null`
# build array
fsap=()
fsap+=$(echo $awsout | jq . | grep AccessPointId | cut -f2 -d ':' | cut -f1 -d',' | jq -r .)
count=`echo $awsout | jq . | grep AccessPointId | wc -l | tr -d ' '`

for cname in ${fsap[@]}; do
    rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
    echo "$ttft ${cname} $rname"
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
            if [[ ${tt1} == "arn" ]];then skip=1;fi
            if [[ ${tt1} == "owner_id" ]];then skip=1;fi
            if [[ ${tt1} == "file_system_arn" ]];then skip=1;fi 
            if [[ ${tt1} == "file_system_id" ]];then
                tt2=`echo $tt2 | tr -d '"'`
                t1=`printf "%s = aws_efs_file_system.%s.id" $tt1 $tt2`
            fi

        fi

        if [ "$skip" == "0" ]; then echo "$t1" >> $fn ;fi
                
    done <"$file"





done
exit

# build array



rm -f t*.txt

