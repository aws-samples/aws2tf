#!/bin/bash
ttft="aws_ram_principal_association"
pref="principals"
idfilt="resourceShareArn"

cm="$AWS ram list-principals --resource-owner SELF"
if [[ "$1" != "" ]]; then
    cm=`printf "$AWS ram list-principals --resource-owner SELF | jq '.${pref}[] | select(.${idfilt}==\"%s\")' | jq ." $1`
else
    echo "must specify resource share ARN"
    EXIT
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
        prinid=`echo $awsout | jq -r ".id"`
    else
        cname=`echo $awsout | jq -r ".${pref}[(${i})].${idfilt}"`
    fi
    rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}

    echo "$ttft ${cname} ${prinid}"
    
    fn=`printf "%s__%s__%s.tf" $ttft $rname $prinid`
    if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

    printf "resource \"%s\" \"%s__%s\" {}\n" $ttft $rname $prinid > $fn  
    
    terraform import $ttft.${rname}__${prinid} "${cname}","${prinid}" | grep Import
    terraform state show -no-color $ttft.${rname}__${prinid} > t1.txt

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
        fi

        if [ "$skip" == "0" ]; then echo "$t1" >> $fn ;fi
                
    done <"$file"
    # dependancies here
done

#rm -f t*.txt

