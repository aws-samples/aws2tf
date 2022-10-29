#!/bin/bash
if [ "$1" != "" ]; then
    if [[ "$1" == "rtb-"* ]]; then
        cmd[0]="$AWS ec2 describe-route-tables --filters \"Name=route-table-id,Values=$1\""
    else
        cmd[0]="$AWS ec2 describe-route-tables --filters \"Name=vpc-id,Values=$1\""
    fi
else
    cmd[0]="$AWS ec2 describe-route-tables"
fi
c=0
cm=${cmd[$c]}
#echo $cm

pref[0]="RouteTables"
tft[0]="aws_route_table"

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
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].RouteTableId" | tr -d '"'`
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            echo "$ttft $cname import"
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi
            printf "resource \"%s\" \"%s\" {}\n" $ttft $rname > $fn
          
            terraform import $ttft.$rname "$cname" | grep Import
            echo "done import"
            
            terraform state show -no-color $ttft.$rname > t1.txt
            #terraform state show -no-color $ttft.$rname
        
            rm -f $fn

            file="t1.txt"
           
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
                    if [[ ${tt1} == "ipv6_cidr_block" ]];then 
                    #skip=1;
                        tt2=`echo $tt2 | tr -d '"'`
                        if [ "$tt2" == "" ]; then
                            t1=`printf "%s = null" $tt1`
                        fi
                    fi

                    if [[ ${tt1} == "cidr_block" ]];then 
                    #skip=1;
                        tt2=`echo $tt2 | tr -d '"'`
                        if [ "$tt2" == "" ]; then
                            t1=`printf "%s = null" $tt1`
                        fi
                    fi
                             
                    
                    if [[ ${tt1} == "network_interface_id" ]]; then
                        nifid=`echo $tt2 | tr -d '"'`
                        #echo "--> netifid $nifid"
                        if [ "$nifid" != "" ]; then
                            t1=`printf "%s = aws_network_interface.%s.id" $tt1 $nifid`
                        fi
                    fi     
                    # depreciated - but you have to have it anyway ?         
                    if [[ ${tt1} == "instance_id" ]]; then
                        #skip=1
                        tt2=`echo $tt2 | tr -d '"'`
                        if [[ $tt2 == "" ]]; then
                            t1=`printf "%s = null" $tt1`
                        fi
                        #if [[ $tt2 == *"i-"* ]]; then
                        #    t1=`printf "%s = aws_instance.%s.id" $tt1 $tt2`
                        #fi
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
                        tgwid=`echo $tt2 | tr -d '"'`
                        if [ "$tgwid" != "" ]; then
                            t1=`printf "%s = aws_ec2_transit_gateway.%s.id" $tt1 $tgwid`
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
                    echo "$t1" >> $fn
                fi
                
            done <"$file"
            for ip in ${pcxs[@]}; do
                pcx=`echo $ip | tr -d '"'`
                echo "calling for $pcx"
                ../../scripts/210-get-vpcpeer.sh $pcx
            done
            if [[ "$tgwid" != "" ]];then
                ../../scripts/201-get-transit-gateway.sh $tgwid
            fi  
            if [[ "$nifid" != "" ]];then
                ../../scripts/get-eni.sh $nifid
            fi                  
        done
    fi
done


rm -f t*.txt

