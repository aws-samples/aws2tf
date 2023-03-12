#!/bin/bash
mysub=`echo $AWS2TF_ACCOUNT`
myreg=`echo $AWS2TF_REGION`
ttft="aws_glue_connection"
pref="ConnectionList"
idfilt="Name"

cm="$AWS glue get-connections"
if [[ "$1" != "" ]]; then
    cm=`printf "$AWS glue get-connections  | jq '.${pref}[] | select(.${idfilt}==\"%s\")' | jq ." $1`
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
        cxp=`echo $awsout | jq -r ".ConnectionProperties" | grep :`
    else
        cname=`echo $awsout | jq -r ".${pref}[(${i})].${idfilt}"`
        cxp=`echo $awsout | jq -r ".${pref}[(${i})].ConnectionProperties" | grep :`
    fi
    rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
    echo "$ttft ${cname}"
    
    fn=`printf "%s__%s.tf" $ttft $rname`
    if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

    printf "resource \"%s\" \"%s\" {}" $ttft $rname > $fn   
    terraform import $ttft.${rname} "${mysub}:${cname}" | grep Importing
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
            if [[ ${tt1} == "arn" ]];then 
            skip=1;
            #printf "lifecycle {\n" >>$fn
            #printf "   ignore_changes = [connection_properties]\n" >>$fn
            #printf "}\n" >>$fn
            
            
            fi
            if [[ ${tt1} == "owner_id" ]];then skip=1;fi  

            if [[ ${tt1} == "connection_properties" ]];then
                skip=1
                cxo=""
                printf "connection_properties = {\n" >>$fn
                cx1=$(echo $cxp | cut -f1 -d',')
                cxp=$(echo $cxp | cut -f2- -d',')
                while [[ $cxp != $cxo ]];do
                    cx2=$(echo $cx1 | tr -d ' |,' | sed 's/"//' | sed 's/\":/ = /')
                    #echo $cx2
                    echo "$cx2" >>$fn
                    cx1=$(echo $cxp | cut -f1 -d',')
                    cxo=$(echo $cxp)   
                    cxp=$(echo $cxp | cut -f2- -d',')
                done

                cx2=$(echo $cx1 | tr -d ' |,' | sed 's/"//' | sed 's/\":/ = /')
                echo "$cx2" >>$fn
                printf "}\n" >>$fn
            fi

        fi

        if [ "$skip" == "0" ]; then echo "$t1" >> $fn ;fi
                
    done <"$file"
    # dependancies here
done

#rm -f t*.txt

