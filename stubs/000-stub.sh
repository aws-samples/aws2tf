#!/bin/bash
bus="default"
if [[ "$1" != "" ]]; then
    if [[ ${1} == "arn:aws:iam"* ]]; then
        cmd[0]="$AWS iam list-roles | jq '.Roles[] | select(.Arn==\"${1}\")'"
    else
        cmd[0]="$AWS iam list-roles | jq '.Roles[] | select(.RoleName==\"${1}\")'"
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
        echo "You don't have access for this resource"
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
            cname=`echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}"`
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            echo "$ttft $cname"
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

            printf "resource \"%s\" \"%s\" {" $ttft $rname > $fn
            printf "}" >> $fn
    
            terraform import $ttft.${rname} "${cname}" | grep Import
            terraform state show $ttft.${rname} > t2.txt

            rm -f $fn
            cat t2.txt | perl -pe 's/\x1b.*?[mGKH]//g' > t1.txt

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
            
        done
    fi 
done

rm -f t*.txt

