#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS ec2 describe-network-interfaces --filters \"Name=network-interface-id,Values=$1\""
else
    cmd[0]="$AWS ec2 describe-network-interfaces"
fi

pref[0]="NetworkInterfaces"
tft[0]="aws_network_interface"

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
            cname=`echo $awsout | jq -r ".${pref[(${c})]}[(${i})].NetworkInterfaceId"`
            # is it the primary ?
            
            echo "$ttft $cname"
            fn=`printf "%s__%s.tf" $ttft $cname`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
            echo $aws2tfmess > $fn
            printf "resource \"%s\" \"%s\" {" $ttft $cname > $ttft.$cname.tf
            printf "}" >> $ttft.$cname.tf
            terraform import $ttft.$cname "$cname" | grep Import
            terraform state show -no-color $ttft.$cname > t1.txt
            rm -f $ttft.$cname.tf
 
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
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "association_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "public_dns" ]];then skip=1;fi
                    if [[ ${tt1} == "private_dns_name" ]];then skip=1;fi
                    if [[ ${tt1} == "mac_address" ]];then skip=1;fi
                    if [[ ${tt1} == "private_ips_count" ]];then skip=1;fi
                    if [[ ${tt1} == "domain" ]];then skip=1;fi
                    if [[ ${tt1} == "attachment_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "default_network_acl_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "ipv6_association_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "ipv6_cidr_block" ]];then skip=1;fi
                    if [[ ${tt1} == "ipv6_addresses" ]];then 
                        if [[ ${tt2} == *"[]"* ]];then
                            skip=1
                        fi
                    fi

                    if [[ ${tt1} == "ipv6_address_list" ]];then 
                        if [[ ${tt2} == *"[]"* ]];then
                            skip=1
                        fi
                    fi
                    
                    
                    if [[ ${tt1} == "ipv4_prefixes" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        if [ "$tt2" == "[]" ];then
                            skip=1
                        fi
                    fi

                    if [[ ${tt1} == "ipv6_prefixes" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        if [ "$tt2" == "[]" ];then
                            skip=1
                        fi
                    fi

                    if [[ ${tt1} == "private_ip_list" ]];then 
                        tt2=`echo $tt2 | tr -d '"'` 
                        skip=1
                        while [ "$t1" != "]" ] && [ "$tt2" != "[]" ] ;do
                        #while [[ "$t1" != "]" ]] ;do

                            read line
                            t1=`echo "$line"`
                            #echo $t1
                        done
                    fi


                    if [[ ${tt1} == "interface_type" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        if [ "$tt2" == "interface" ];then
                            skip=1
                        fi
                    fi


                    if [[ ${tt1} == "vpc_id" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_vpc.%s.id" $tt1 $tt2`
                    fi
                    if [[ ${tt1} == "subnet_id" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_subnet.%s.id" $tt1 $tt2`
                    fi
                else
                    
                    if [[ "$t1" == *"sg-"* ]]; then
                        t1=`echo $t1 | tr -d '"|,'`
                        t1=`printf "aws_security_group.%s.id," $t1`
                    fi
                    if [[ $t1 == *"attachment {"* ]]; then 
                        #echo "matched attachment"
                        skip=1
                        while [[ "$t1" != "}" ]] ;do
                            read line
                            t1=`echo "$line"`
                            #echo $t1
                        done
                    fi
                
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"
            gid=`echo $awsout | jq ".${pref[(${c})]}[(${i})].Groups[0].GroupId"`
            echo "gid=$gid"
            eipa=`echo $awsout | jq ".${pref[(${c})]}[(${i})].Association.AllocationId"`
            if [ "$eipa" != "null" ];then 
                ../../scripts/get-eip.sh $eipa
            fi            
        done
    fi
done

rm -f t*.txt

