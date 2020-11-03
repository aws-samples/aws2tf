#!/bin/bash

if [ "$1" != "" ]; then
    cmd[0]="$AWS eks list-fargate-profiles --cluster-name $1"
else
    echo "Must supply Cluster Name as a parameter - exiting ..."
    exit
fi

pref[0]="fargateProfileNames"
tft[0]="aws_eks_fargate_profile"
cln=`echo $1`

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	echo $cm
    awsout=`eval $cm`
    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            echo $i
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})]" | tr -d '"'`
            echo $cname
            ren=`printf "%s:%s" $cln $cname`
            of=`printf "%s__%s__%s.tf" $ttft $cln $cname`
            printf "resource \"%s\" \"%s\" {" $ttft $cname > $of
            printf "}" $cname >> $of
            echo "$ttft.$cname $ren"
            terraform import $ttft.$cname $ren
            terraform state show $ttft.$cname > t2.txt
            rm -f $of
            cat t2.txt | perl -pe 's/\x1b.*?[mGKH]//g' > t1.txt
    
            file="t1.txt"
            fn=`printf "%s__%s__%s.tf" $ttft $cln $cname`
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
                    if [[ ${tt1} == "id" ]];then 
                        t1=`printf "depends_on = [aws_eks_cluster.%s]" $cln`
                        skip=0; 
                    fi          
                    if [[ ${tt1} == "role_arn" ]];then skip=1;fi
                    if [[ ${tt1} == "pod_execution_role_arn" ]];then 
                        trole=`echo "$tt2" | cut -f2- -d'/' | tr -d '"'`           
                        t1=`printf "%s = aws_iam_role.%s.arn" $tt1 $trole`
                        skip=0;
                    fi

                    if [[ ${tt1} == "primary_network_interface_id" ]];then skip=1;fi
                    if [[ ${tt1} == "instance_state" ]];then skip=1;fi
                    if [[ ${tt1} == "private_dns" ]];then skip=1;fi

                    if [[ ${tt1} == "status" ]];then skip=1;fi
                    #if [[ ${tt1} == "user_data" ]];then skip=1;fi
                    if [[ ${tt1} == "security_group_names" ]];then skip=1;fi
                    #if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "default_network_acl_id" ]];then skip=1;fi
                    if [[ ${tt1} == "latest_version" ]];then skip=1;fi
                    if [[ ${tt1} == "default_version" ]];then skip=1;fi
                else
                    if [[ "$t1" == *"subnet-"* ]]; then
                        t1=`echo $t1 | tr -d '"|,'`
                        t1=`printf "aws_subnet.%s.id," $t1`
                    fi
                fi

                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo $t1 >> $fn
                fi
                
            done <"$file"
            
        done
    fi
done
terraform fmt
terraform validate
rm -f t*.txt

