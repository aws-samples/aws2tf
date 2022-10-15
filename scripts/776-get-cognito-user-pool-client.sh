#!/bin/bash
# describe-user-pool-client --user-pool-id, --client-id
if [[ "$2" != "" ]]; then
    cmd[0]="$AWS cognito-idp describe-user-pool-client --user-pool-id $1 --client-id $2"
    pref[0]="UserPoolClient"
else
    if [[ "$1" != "" ]]; then
        cmd[0]="$AWS cognito-idp list-user-pool-clients --user-pool-id $1"
        pref[0]="UserPoolClients"
    else
        echo "must specify user pool id exiting ..."
        exit
    fi 
fi

tft[0]="aws_cognito_user_pool_client"
idfilt[0]="ClientId"

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        exit
    fi

    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i

            
            cname=`echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}"`
            
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            echo "$ttft $cname"
            fn=`printf "%s__c_%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

            printf "resource \"%s\" \"c_%s\" {" $ttft $rname > $fn
            printf "}" >> $fn
    
            terraform import $ttft.c_${rname} "${1}/${cname}" | grep Import
            terraform state show -no-color $ttft.c_${rname} > t1.txt

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
                    if [[ ${tt1} == "client_secret" ]];then skip=1;fi

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

