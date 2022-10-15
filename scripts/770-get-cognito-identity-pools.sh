#!/bin/bash
if [[ "$1" != "" ]]; then
    cmd[0]="$AWS cognito-identity describe-identity-pool --identity-pool-id $1"
else
    cmd[0]="$AWS cognito-identity list-identity-pools --max-results 60"
fi

pref[0]="IdentityPools"
tft[0]="aws_cognito_identity_pool"
idfilt[0]="IdentityPoolId"

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
                # get the user pool name
                upn=`echo $awsout | jq -r ".CognitoIdentityProviders[0].ProviderName" | cut -f2 -d'/'`
            else
                cname=`echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}"`
                # get the user pool name
                upn=`echo $awsout | jq -r ".${pref[(${c})]}[(${i})].CognitoIdentityProviders[0].ProviderName" | cut -f2 -d'/'`
            fi
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            echo "$ttft $cname"
            echo "User pool name 0 = $upn"
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

            printf "resource \"%s\" \"%s\" {" $ttft $rname > $fn
            printf "}" >> $fn
    
            terraform import $ttft.${rname} "${cname}" | grep Import
            terraform state show -no-color $ttft.${rname} > t1.txt
            rm -f $fn

            file="t1.txt"
            echo $aws2tfmess > $fn
            upn=""
      

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
                    if [[ ${tt1} == "client_id" ]];then 
                        cid=$(echo $tt2 | tr -d '"')
                        t1=`printf "%s = aws_cognito_user_pool_client.c_%s.id" $tt1 $cid`
                    fi
                                     

                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"

            ../../scripts/771-get-cognito-identity-pool-roles-attachment.sh $cname

            if [[ "$upn" != "" ]];then
                if [[ "$cid" != "" ]];then
                    ../../scripts/776-get-cognito-user-pool-client.sh $upn $cid
                else
                    ../../scripts/776-get-cognito-user-pool-client.sh $upn
                fi
            fi

        done
    fi 
done

rm -f t*.txt

