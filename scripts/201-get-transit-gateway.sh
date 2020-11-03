#!/bin/bash
pref[0]="TransitGateways"
tft[0]="aws_ec2_transit_gateway"
c=0
ttft=${tft[(${c})]}
if [ "$1" != "" ]; then
    cmd[0]="$AWS ec2 describe-transit-gateways --transit-gateway-ids $1 --filters \"Name=state,Values=available\"" 
    cname=$1
    fn=`printf "%s__%s.tf" $ttft $cname`
    if [ -f "$fn" ] ; then
        echo "$fn exists already skipping"
        exit
    fi
else
    cmd[0]="$AWS ec2 describe-transit-gateways"
fi

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
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].TransitGatewayId" | tr -d '"'`
            echo $cname
            fn=`printf "%s__%s.tf" $ttft $cname`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                exit
            fi
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
                    if [[ ${tt1} == "association_default_route_table_id" ]];then skip=1;fi
                    if [[ ${tt1} == "propagation_default_route_table_id" ]];then skip=1;fi
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
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

            dfn=`printf "data/data_%s__%s.tf" $ttft $cname`
            printf "data \"%s\" \"%s\" {\n" $ttft $cname > $dfn
            printf "id = \"%s\"\n" $cname >> $dfn
            printf "}\n" $ttft $cname >> $dfn
            
        done
    fi
done
terraform fmt
terraform validate
rm -f t*.txt

