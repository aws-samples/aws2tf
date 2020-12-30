#!/bin/bash
cmd[0]="$AWS autoscaling describe-auto-scaling-groups"
pref[0]="AutoScalingGroups"
tft[0]="aws_autoscaling_group"


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
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].AutoScalingGroupName" | tr -d '"'`
            echo "$ttft $cname"
            printf "resource \"%s\" \"%s\" {" $ttft $cname > $ttft.$cname.tf
            printf "}" $cname >> $ttft.$cname.tf
            terraform import $ttft.$cname "$cname" | grep Import
            terraform state show $ttft.$cname > t2.txt
            rm $ttft.$cname.tf
            cat t2.txt | perl -pe 's/\x1b.*?[mGKH]//g' > t1.txt
            #	for k in `cat t1.txt`; do
            #		echo $k
            #	done
            az-0
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
                    if [[ ${tt1} == "primary_network_interface_id" ]];then skip=1;fi
                    if [[ ${tt1} == "instance_state" ]];then skip=1;fi
                    if [[ ${tt1} == "private_dns" ]];then skip=1;fi

                    if [[ ${tt1} == "volume_id" ]];then skip=1;fi
                    if [[ ${tt1} == "user_data" ]];then skip=1;fi
                    if [[ ${tt1} == "availability_zones" ]];then 
                        az=1;
                    fi

                    if [[ ${tt1} == "vpc_zone_identifier" ]];then
                        if [[ ${az} == "1" ]];then
                            echo "vpc_zone_identifier skipping ..."  
                            skip=1
                            while [[ "$t1" != "]" ]] ;do
                                read line
                                t1=`echo "$line"`
                            done
                        fi
                    fi


                    #if [[ ${tt1} == "default_route_table_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "default_network_acl_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "ipv6_association_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "ipv6_cidr_block" ]];then skip=1;fi
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo $t1 >> $fn
                fi
                
            done <"$file"
            
        done
    fi
done

rm -f t*.txt

