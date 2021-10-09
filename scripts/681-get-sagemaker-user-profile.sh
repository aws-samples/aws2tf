#!/bin/bash

cmd[0]="$AWS sagemaker list-user-profiles "

pref[0]="UserProfiles"
tft[0]="aws_sagemaker_user_profile"
idfilt[0]="UserProfileName"



for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "You don't have access for this resource"
        exit
    fi
    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    #echo $count
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            upn=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")    
            domid=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].DomainId")
            cname=$($AWS sagemaker describe-user-profile --domain-id $domid --user-profile-name $upn  --query UserProfileArn | jq -r .)
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
         
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then continue; fi

            echo "$ttft $cname import"


            printf "resource \"%s\" \"%s\" {" $ttft $upn > $fn
            printf "}" $cname >> $fn
            terraform import $ttft.$upn "$cname" | grep Import
            terraform state show $ttft.$upn > t2.txt
            rm $ttft.$rname.tf
            cat t2.txt | perl -pe 's/\x1b.*?[mGKH]//g' > t1.txt
            #	for k in `cat t1.txt`; do
            #		echo $k
            #	done
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
                    if [[ ${tt1} == "home_efs_file_system_id" ]];then skip=1;fi
                    if [[ ${tt1} == "home_efs_file_system_uid" ]];then skip=1;fi
                    if [[ ${tt1} == "url" ]];then skip=1;fi
                    if [[ ${tt1} == "single_sign_on_managed_application_instance_id" ]];then skip=1;fi
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"
   

            
        done
    fi
done

rm -f *.backup 



#