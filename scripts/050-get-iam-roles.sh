#!/bin/bash
if [[ "$1" != "" ]]; then
   
    if [[ ${1} == "arn:aws:iam"* ]]; then
        cmd[0]="$AWS iam list-roles | jq '.Roles[] | select(.Arn==\"${1}\")'"
    else
        cmd[0]="$AWS iam list-roles | jq '.Roles[] | select(.RoleName==\"${1}\")'"
    fi
else
    cmd[0]="$AWS iam list-roles"
fi


pref[0]="Roles"
tft[0]="aws_iam_role"

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
    #echo "role command = $cm"
    ttft=${tft[(${c})]}
    echo $cm
    awsout=`eval $cm`
    if [ "$1" != "" ]; then
        count=1
    else
        count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    fi
    #echo "count=$count"
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            if [ "$1" != "" ]; then
                cname=`echo $awsout | jq ".RoleName" | tr -d '"'` 
            else
                cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].RoleName" | tr -d '"'`
            fi
            ocname=`echo $cname`
            cname=${cname//./_}
            echo $cname
            fn=`printf "%s__%s.tf" $ttft $cname`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                exit
            fi


            printf "resource \"%s\" \"%s\" {" $ttft $cname > $ttft.$cname.tf
            printf "}" >> $ttft.$cname.tf
            echo $ttft.$cname $ocname
            terraform import $ttft.$cname $ocname
            terraform state show $ttft.$cname > t2.txt
            rm $ttft.$cname.tf
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
                    if [[ ${tt1} == *":"* ]];then
                        t1=`printf "\"%s\"=%s" $tt1 $tt2`
                    fi
                    if [[ ${tt1} == "arn" ]];then skip=1; fi
                    if [[ ${tt1} == "id" ]];then skip=1; fi
                    if [[ ${tt1} == "role_arn" ]];then skip=1;fi
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    if [[ ${tt1} == "association_id" ]];then skip=1;fi
                    if [[ ${tt1} == "unique_id" ]];then skip=1;fi
                    if [[ ${tt1} == "create_date" ]];then skip=1;fi
                    #if [[ ${tt1} == "public_ip" ]];then skip=1;fi
                    if [[ ${tt1} == "private_ip" ]];then skip=1;fi
                    if [[ ${tt1} == "accept_status" ]];then skip=1;fi
                    #if [[ ${tt1} == "default_network_acl_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "ipv6_association_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "ipv6_cidr_block" ]];then skip=1;fi
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo $t1 >> $fn
                fi
                
            done <"$file"   # done while
            
        done # done for i
        # Get attached role policies
        pwd
        echo "role policies $ocname"
        ../../scripts/051-get-iam-role-policies.sh $ocname
         echo "attached role policies $ocname"
        ../../scripts/052-get-iam-attached-role-policies.sh $ocname
        
        echo "fmt"
        terraform fmt
        echo "validate"
        terraform validate
    
    fi
done

rm -f t*.txt

