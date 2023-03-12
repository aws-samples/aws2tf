#!/bin/bash
pref[0]="UserProfiles"
tft[0]="aws_sagemaker_user_profile"
idfilt[0]="UserProfileName"

if [ "$1" != "" ]; then
    if [[ $1 == *"|"* ]];then 
        domid=$(echo $1 | cut -f2 -d'|')
        up=$(echo $1 | cut -f1 -d'|')
        cmd[0]=`printf "$AWS sagemaker list-user-profiles --domain-id-equals $domid | jq '.${pref}[] | select(.${idfilt}==\"%s\")' | jq ." $up`
    else
        cmd[0]=`printf "$AWS sagemaker list-user-profiles | jq '.${pref}[] | select(.${idfilt}==\"%s\")' | jq ." $1`
    fi
else
    cmd[0]="$AWS sagemaker list-user-profiles"
fi

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    if [ "$1" != "" ]; then
        count=1
    else
        count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    fi
    #echo "count=$count"
    #echo $awsout | jq .
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            if [ "$1" != "" ]; then
                upn=$(echo $awsout | jq -r ".${idfilt[(${c})]}")    
                domid=$(echo $awsout | jq -r ".DomainId")
            else
                upn=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")    
                domid=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].DomainId")
            fi
            cname=$($AWS sagemaker describe-user-profile --domain-id $domid --user-profile-name $upn  --query UserProfileArn | jq -r .)
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
         
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

            echo "$ttft $cname import"


            printf "resource \"%s\" \"%s\" {}\n" $ttft $upn > $fn
            terraform import $ttft.$upn "$cname" | grep Importing
            terraform state show -no-color $ttft.$upn > t1.txt
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
                    if [[ ${tt1} == "url" ]];then skip=1;fi
                    if [[ ${tt1} == "home_efs_file_system_uid" ]];then skip=1;fi
                    if [[ ${tt1} == "domain_id" ]];then 
                                skip=0;
                                did=`echo "$tt2" | cut -f2- -d'/' | tr -d '"'`          
                                t1=`printf "domain_id = aws_sagemaker_domain.%s.id" $did`
                    fi
                    if [[ ${tt1} == "single_sign_on_managed_application_instance_id" ]];then skip=1;fi
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"
            ../../scripts/get-sagemaker-app.sh $domid $upn
            
        done
    fi
done

rm -f *.backup 



#