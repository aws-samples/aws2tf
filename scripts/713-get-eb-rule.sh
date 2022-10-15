#!/bin/bash
bus="default"
if [[ "$1" != "" ]]; then
    if [[ "$1" == *"|"* ]]; then
        bus=$(echo $1 | cut -f1 -d '|')
        ru=$(echo $1 | cut -f2 -d '|')      
        cmd[0]="$AWS events describe-rule --name $ru --event-bus-name $bus" 
    else
        cmd[0]="$AWS events describe-rule --name $1" # assumes default bus
    fi
    
else
    cmd[0]="$AWS events list-rules"
fi

pref[0]="Rules"
tft[0]="aws_cloudwatch_event_rule"
idfilt[0]="Name"


#rm -f ${tft[0]}.tf

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    if [[ "$1" != "" ]]; then
        count=1
    else
        count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    fi
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            if [[ "$1" != "" ]];then 
                cname=`echo $awsout | jq -r ".${idfilt[(${c})]}"`
                bus=`echo $awsout | jq -r ".EventBusName"`
            else
                cname=`echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}"`
                bus=`echo $awsout | jq -r ".${pref[(${c})]}[(${i})].EventBusName"`
            fi
            echo "$ttft $bus $cname"

            fn=`printf "%s__%s__%s.tf" $ttft $bus $cname`


            printf "resource \"%s\" \"%s__%s\" {" $ttft $bus $cname > $fn
            printf "}" >> $fn
            if [[ "$bus" == "default" ]];then
                terraform import $ttft.${bus}__${cname} "${cname}" | grep Import
            else
                terraform import $ttft.${bus}__${cname} "${bus}/${cname}" | grep Import
            fi
            
            terraform state show -no-color $ttft.${bus}__${cname} > t1.txt

            rm -f $fn
  
            file="t1.txt"
            echo $aws2tfmess > $fn
            while IFS= read line
            do
				skip=0
                # display $line or do something with $line
                t1=`echo "$line"` 
                if [[ ${t1} == *"="* ]];then
                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                    tt2=`echo "$line" | cut -f2- -d'='`
                    if [[ ${tt1} == "arn" ]];then skip=1; fi                
                    if [[ ${tt1} == "id" ]];then skip=1; fi          
                    if [[ ${tt1} == "role_arn" ]];then skip=1;fi
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi

                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"
            
            ../../scripts/714-get-eb-target.sh "${bus}|${cname}"
            
        done
    fi 
done

#rm -f t*.txt

