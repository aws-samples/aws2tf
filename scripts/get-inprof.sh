#!/bin/bash

if [ "$1" == "null" ]; then 
    echo "****inst prof $1 *****"
    exit 
fi
cmd[0]="$AWS iam get-instance-profile --instance-profile-name $1"
pref[0]="InstanceProfile"
tft[0]="aws_iam_instance_profile"

for c in `seq 0 0`; do
   
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	echo $cm
    awsout=`eval $cm`
    count=1 # as only one profile name
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            cname=`echo $awsout | jq ".${pref[(${c})]}.InstanceProfileName" | tr -d '"'`
            echo $cname
            fn=`printf "%s__%s.tf" $ttft $cname`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
        
            instroles=`echo $awsout | jq ".${pref[(${c})]}.Roles"`
            printf "resource \"%s\" \"%s\" {" $ttft $cname > $ttft.$cname.tf
            printf "}" $cname >> $ttft.$cname.tf
            terraform import $ttft.$cname $cname
            terraform state show $ttft.$cname > t2.txt
            rm $ttft.$cname.tf
            cat t2.txt | perl -pe 's/\x1b.*?[mGKH]//g' > t1.txt
            #	for k in `cat t1.txt`; do
            #		echo $k
            #	done
            file="t1.txt"
            fn=`printf "%s__%s.tf" $ttft $cname`
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
                    if [[ ${tt1} == "create_date" ]];then skip=1;fi
                    #if [[ ${tt1} == "public_dns" ]];then skip=1;fi
                    #if [[ ${tt1} == "private_dns" ]];then skip=1;fi
                    #if [[ ${tt1} == "public_ip" ]];then skip=1;fi
                    #if [[ ${tt1} == "private_ip" ]];then skip=1;fi
                    if [[ ${tt1} == "unique_id" ]];then skip=1;fi
                    if [[ ${tt1} == "roles" ]];then 
                        read line
                        read line
                        skip=1;
                    fi
                    #if [[ ${tt1} == "ipv6_association_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "ipv6_cidr_block" ]];then skip=1;fi
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo $t1 >> $fn 
                fi
                
                
            done <"$file"

            nl=`echo $instroles | jq ". | length"`
            echo "num inst roles= $nl"
            if [ "$nl" != "0" ]; then
                nl=`expr $nl - 1`
                for ni in `seq 0 $nl`; do
                    nif=`echo $instroles | jq ".[(${ni})].RoleName" | tr -d '"'`
                    echo $ni $nif
                    ../../scripts/050-get-iam-roles.sh $nif
                done
            fi


            
        done
    fi
done
terraform fmt

rm -f t*.txt

