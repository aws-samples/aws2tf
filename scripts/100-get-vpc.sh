#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS ec2 describe-vpcs --vpc-ids $1"
else
    cmd[0]="$AWS ec2 describe-vpcs"
fi
pref[0]="Vpcs"
tft[0]="aws_vpc"
#echo ${cmd[0]}


for c in `seq 0 0`; do
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm
    awsout=`eval $cm`
    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].VpcId" | tr -d '"'`
            echo $cname
            fn=`printf "%s__%s.tf" $ttft $cname`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
            printf "resource \"%s\" \"%s\" {" $ttft $cname > $ttft.$cname.tf
            printf "}" $cname >> $ttft.$cname.tf
            printf "terraform import %s.%s %s" $ttft $cname $cname > import_$ttft_$cname.sh
            terraform import $ttft.$cname $cname
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
                    if [[ ${tt1} == "arn" ]];then skip=1; fi                
                    if [[ ${tt1} == "id" ]];then skip=1; fi          
                    if [[ ${tt1} == "role_arn" ]];then skip=1;fi
                    if [[ ${tt1} == "allocated_capacity" ]];then skip=1;fi
                    if [[ ${tt1} == "dhcp_options_id" ]];then skip=1;fi
                    if [[ ${tt1} == "main_route_table_id" ]];then skip=1;fi
                    if [[ ${tt1} == "default_security_group_id" ]];then skip=1;fi
                    if [[ ${tt1} == "default_route_table_id" ]];then skip=1;fi
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    if [[ ${tt1} == "default_network_acl_id" ]];then skip=1;fi
                    if [[ ${tt1} == "ipv6_association_id" ]];then skip=1;fi
                    if [[ ${tt1} == "ipv6_cidr_block" ]];then skip=1;fi
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo $t1 >> $fn
                fi
                
            done <"$file"

            ofn=`printf "output__%s__%s.tf" $ttft $cname`
            printf "output \"%s__%s__id\" {\n" $ttft $cname > $ofn
            printf "value = %s.%s.id\n" $ttft $cname >> $ofn
            printf "}\n" $ttft $cname >> $ofn
   

            dfn=`printf "data/data_%s__%s.tf" $ttft $cname`
            printf "data \"%s\" \"%s\" {\n" $ttft $cname > $dfn
            printf "id = \"%s\"\n" $cname >> $dfn
            printf "}\n" $ttft $cname >> $dfn
            
        done
        terraform fmt
        terraform validate
    fi
done

rm -f t*.txt

#