#!/bin/bash
ttft="aws_glue_job"
pref="Jobs"
idfilt="Name"

cm="$AWS glue get-jobs"
if [[ "$1" != "" ]]; then
    cm=`printf "$AWS glue get-jobs  | jq '.${pref}[] | select(.${idfilt}==\"%s\")' | jq ." $1`
fi

count=1
echo $cm
awsout=`eval $cm 2> /dev/null`
#echo $awsout | jq .

if [ "$awsout" == "" ];then echo "$cm : You don't have access for this resource" && exit; fi
if [[ "$1" == "" ]]; then count=`echo $awsout | jq ".${pref} | length"`; fi   
if [ "$count" -eq "0" ]; then echo "No resources found exiting .." && exit; fi
count=`expr $count - 1`
for i in `seq 0 $count`; do
    #echo $i
    if [[ "$1" != "" ]]; then
        cname=`echo $awsout | jq -r ".${idfilt}"`
    else
        cname=`echo $awsout | jq -r ".${pref}[(${i})].${idfilt}"`
    fi
    rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_} && rname=${rname// /_}
    echo "$ttft ${cname}"
    
    fn=`printf "%s__%s.tf" $ttft $rname`
    if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

    printf "resource \"%s\" \"%s\" {}" $ttft $rname > $fn   
    terraform import $ttft.${rname} "${cname}" | grep Importing
    terraform state show -no-color $ttft.${rname} > t1.txt

    rm -f $fn
    mc=0
    nw=0
    rarn=""
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

            if [[ ${tt1} == "max_capacity" ]];then 
                mc=`echo $tt2 | tr -d '"'` 
                if [[ ${mc} == "0" ]];then
                    skip=1;
                fi    
            fi 

            if [[ ${tt1} == "role_arn" ]];then 
                rarn=`echo $tt2 | tr -d '"'`
                trole=$(echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"')
                t1=`printf "%s = aws_iam_role.r-%s.arn" $tt1 $trole`

            fi


            if [[ ${tt1} == "number_of_workers" ]];then 
                if [[ $mc == "0" ]];then 
                    nw=`echo $tt2 | tr -d '"'` 
                    if [[ ${nw} == "0" ]];then
                        skip=1;
                    fi  
                else # max capacity is not 0 so skip number_of workers
                    skip=1  
                fi
            fi 

            if [[ ${tt1} == "worker_type" ]];then 
                if [[ $mc == "0" ]];then 
                    skip=0;  
                else # max capacity is not 0 so skip number_of workers
                    skip=1  
                fi
            fi 



        fi

        if [ "$skip" == "0" ]; then echo "$t1" >> $fn ;fi
                
    done <"$file"
    
    if [[ $rarn != "" ]];then
        ../../scripts/050-get-iam-roles.sh $rarn
    fi
    # dependancies here
done

#rm -f t*.txt

