#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS ec2 describe-route-tables --filters \"Name=vpc-id,Values=$1\""
else
    cmd[0]="$AWS ec2 describe-route-tables"
fi
c=0
cm=${cmd[$c]}
echo $cm


pref[0]="RouteTables"
tft[0]="aws_route_table"

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
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].RouteTableId" | tr -d '"'`
            echo $cname
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
            pcxs=()
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
                    if [[ ${tt1} == "availability_zone" ]];then skip=1;fi
                    if [[ ${tt1} == "availability_zone_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "default_route_table_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "default_network_acl_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "ipv6_association_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "ipv6_cidr_block" ]];then skip=1;fi
                    if [[ ${tt1} == "network_interface_id" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        if [ "$tt2" != "" ]; then
                            t1=`printf "%s = aws_network_interface.%s.id" $tt1 $tt2`
                        fi
                    fi              
                    if [[ ${tt1} == "instance_id" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        if [ "$tt2" != "" ]; then
                            t1=`printf "%s = aws_instance.%s.id" $tt1 $tt2`
                        fi
                    fi
                    if [[ ${tt1} == "vpc_id" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        if [ "$tt2" != "" ]; then
                            t1=`printf "%s = aws_vpc.%s.id" $tt1 $tt2`
                        fi
                    fi
                    if [[ ${tt1} == "nat_gateway_id" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        if [ "$tt2" != "" ]; then
                            t1=`printf "%s = aws_nat_gateway.%s.id" $tt1 $tt2`
                        fi
                    fi
                    if [[ ${tt1} == "transit_gateway_id" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        if [ "$tt2" != "" ]; then
                            t1=`printf "%s = aws_ec2_transit_gateway.%s.id" $tt1 $tt2`
                        fi
                    fi
                    if [[ ${tt1} == "gateway_id" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        if [ "$tt2" != "" ]; then
                            t1=`printf "%s = aws_internet_gateway.%s.id" $tt1 $tt2`
                        fi
                    fi
                    if [[ ${tt1} == "vpc_peering_connection_id" ]]; then
                        ttt2=`echo $tt2 | tr -d '"'`
                        if [ "$ttt2" != "" ]; then
                            t1=`printf "%s = aws_vpc_peering_connection.%s.id" $tt1 $ttt2`
                            echo "adding $tt2"
                            pcxs+=$tt2
                        fi
                    fi

                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo $t1 >> $fn
                fi
                
            done <"$file"
            for ip in ${pcxs[@]}; do
                pcx=`echo $ip | tr -d '"'`
                echo "calling for $pcx"
                ../../scripts/210-get-vpcpeer.sh $pcx
            done

                     
        done
    fi
done
terraform fmt
terraform validate
rm -f t*.txt

