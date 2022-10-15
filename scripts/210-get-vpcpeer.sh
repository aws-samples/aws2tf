#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS ec2 describe-vpc-peering-connections --vpc-peering-connection-ids $1"
else
    cmd[0]="$AWS ec2 describe-vpc-peering-connections"
fi

pref[0]="VpcPeeringConnections"
tft[0]="aws_vpc_peering_connection"

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
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].VpcPeeringConnectionId" | tr -d '"'`
            echo "$ttft $cname"
            fn=`printf "%s__%s.tf" $ttft $cname`
            if [ -f "$fn" ] ; then
                    echo "$fn exists already skipping"
                    continue
                fi
            printf "resource \"%s\" \"%s\" {}" $ttft $cname > $fn
      
            terraform import $ttft.$cname "$cname" | grep Import
            terraform state show -no-color $ttft.$cname > t1.txt
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
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    if [[ ${tt1} == "association_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "public_dns" ]];then skip=1;fi
                    if [[ ${tt1} == "allow_vpc_to_remote_classic_link" ]];then skip=1;fi
                    if [[ ${tt1} == "allow_classic_link_to_remote_vpc" ]];then skip=1;fi
                    if [[ ${tt1} == "private_ip" ]];then skip=1;fi
                    if [[ ${tt1} == "accept_status" ]];then skip=1;fi
                    #if [[ ${tt1} == "default_network_acl_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "ipv6_association_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "ipv6_cidr_block" ]];then skip=1;fi
                    if [[ ${tt1} == "vpc_id" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_vpc.%s.id" $tt1 $tt2`
                        lvpc=`echo $tt2`
                    fi
                    if [[ ${tt1} == "peer_vpc_id" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_vpc.%s.id" $tt1 $tt2`
                        rvpc=`echo $tt2`
                    fi
                    # can't do this a vpc is in remote account
                    #if [[ ${tt1} == "peer_vpc_id" ]]; then
                    #    tt2=`echo $tt2 | tr -d '"'`
                    #    t1=`printf "%s = aws_vpc.%s.id" $tt1 $tt2`
                    #fi
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"
            ../../scripts/100-get-vpc.sh $lvpc
            ../../scripts/100-get-vpc.sh $rvpc
        done
    fi
done

rm -f t*.txt

