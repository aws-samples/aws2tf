#!/bin/bash
if [[ "$1" != "" ]]; then
    cmd[0]="$AWS cognito-idp describe-user-pool --user-pool-id $1"
    pref[0]="UserPool"
else
    cmd[0]="$AWS cognito-idp list-user-pools --max-results 60"
    pref[0]="UserPools"
fi

tft[0]="aws_cognito_user_pool"
idfilt[0]="Id"

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
            if [[ "$1" != "" ]]; then
                cname=`echo $awsout | jq -r ".${pref[(${c})]}.${idfilt[(${c})]}"`
            else
                cname=`echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}"`
            fi
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            echo "$ttft $cname"
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

            printf "resource \"%s\" \"%s\" {" $ttft $rname > $fn
            printf "}" >> $fn
    
            terraform import $ttft.${rname} "${cname}" | grep Import
            terraform state show -no-color $ttft.${rname} > t1.txt

            rm -f $fn

            file="t1.txt"
            echo $aws2tfmess > $fn
            tarn=""
            while IFS= read line
            do
				skip=0
                # display $line or do something with $line
                t1=`echo "$line"` 
                if [[ ${t1} == *"="* ]];then
                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                    tt2=`echo "$line" | cut -f2- -d'='`
         
                    if [[ ${tt1} == "id" ]];then skip=1;fi
                    if [[ ${tt1} == "arn" ]];then skip=1;fi
                    if [[ ${tt1} == "creation_date" ]];then skip=1;fi
                    if [[ ${tt1} == "last_modified_date" ]];then skip=1;fi
                    if [[ ${tt1} == "endpoint" ]];then skip=1;fi
                    if [[ ${tt1} == "estimated_number_of_users" ]];then skip=1;fi                  
                    if [[ ${tt1} == "email_verification_message" ]];then skip=1;fi
                    if [[ ${tt1} == "email_verification_subject" ]];then skip=1;fi
                    if [[ ${tt1} == "sms_verification_message" ]];then skip=1;fi
                fi

                if [ "$skip" == "0" ]; then echo "$t1" >> $fn ;fi
                
            done <"$file"

            ../../scripts/776-get-cognito-user-pool-client.sh "${cname}"

        done
    fi 
done

#rm -f t*.txt

