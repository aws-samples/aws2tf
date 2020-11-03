#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS iam list-attached-role-policies --role-name $1"
else
    exit
fi
c=0
cm=${cmd[$c]}
echo $cm


pref[0]="AttachedPolicies"
tft[0]="aws_iam_role_policy_attachment"

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
    ttft=${tft[(${c})]}
    #echo $cm
    awsout=`eval $cm`
    #echo "awsout $awsout"
    if [ "$1" != "" ]; then
        count=1
    else
        count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    fi
    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i

            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].PolicyName" | tr -d '"'`
            rarn=`echo $awsout | jq ".${pref[(${c})]}[(${i})].PolicyArn" | tr -d '"'`
            ocname=`echo $cname`
            cname=${cname//./_}
            cname=`printf "%s__%s" $1 $cname`
            echo $cname
            
            printf "resource \"%s\" \"%s\" {" $ttft $cname > $ttft.$cname.tf
            printf "}" >> $ttft.$cname.tf
            terraform import $ttft.$cname $1/$rarn
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
                    if [[ ${tt1} == *":"* ]];then
                        t1=`printf "\"%s\"=%s" $tt1 $tt2`
                    fi
                    if [[ ${tt1} == "role" ]];then 
                        tsel=`echo $tt2 |  tr -d '"'`
                        t1=`printf "%s = aws_iam_role.%s.id" $tt1 $tsel`
                        skip=0;
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
    fi
done
echo "fmt"
terraform fmt
echo "validate"
terraform validate
rm -f t*.txt

