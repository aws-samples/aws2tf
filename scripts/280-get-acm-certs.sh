#!/bin/bash
ttft="aws_acm_certificate"
pref="CertificateSummaryList"
idfilt="CertificateArn"

cm="$AWS acm list-certificates"
if [[ "$1" != "" ]]; then
    cm=`printf "$cm  | jq '.${pref}[] | select(.${idfilt}==\"%s\")' | jq ." $1`
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
    rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
    rname=`printf "b_%s" $rname`
    echo "$ttft ${cname}"
    
    fn=`printf "%s__%s.tf" $ttft $rname`
    if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

    printf "resource \"%s\" \"%s\" {}" $ttft $rname > $fn   
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
            if [[ ${tt1} == "not_after" ]];then skip=1;fi 
            if [[ ${tt1} == "not_before" ]];then skip=1;fi    
            if [[ ${tt1} == "pending_renewal" ]];then skip=1;fi   
            if [[ ${tt1} == "renewal_eligibility" ]];then skip=1;fi     
            if [[ ${tt1} == "status" ]];then skip=1;fi   
            if [[ ${tt1} == "type" ]];then skip=1;fi

            if [[ ${tt1} == "renewal_summary" ]];then 
                tt2=`echo $tt2 | tr -d '"'` 
                skip=1
                while [ "$t1" != "]" ] && [ "$tt2" != "[]" ] ;do
                    read line
                    t1=`echo "$line"`
                done
            fi
            if [[ ${tt1} == "validation_emails" ]];then 
                tt2=`echo $tt2 | tr -d '"'` 
                skip=1
                while [ "$t1" != "]" ] && [ "$tt2" != "[]" ] ;do
                    read line
                    t1=`echo "$line"`
                done
            fi
            if [[ ${tt1} == "domain_validation_options" ]];then 
                tt2=`echo $tt2 | tr -d '"'` 
                skip=1
                while [ "$t1" != "]" ] && [ "$tt2" != "[]" ] ;do
                    read line
                    t1=`echo "$line"`
                done
            fi




        fi

        if [ "$skip" == "0" ]; then echo "$t1" >> $fn ;fi
                
    done <"$file"
    # dependancies here
done

#rm -f t*.txt

