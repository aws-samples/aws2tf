#!/bin/bash
pref[0]="Routes"
tft[0]="aws_ec2_transit_gateway_route"
c=0

if [ "$1" != "" ]; then
    cmd[0]="$AWS ec2 search-transit-gateway-routes --transit-gateway-route-table-id $1 --filters \"Name=type,Values=static\"" 
    tgwrtbid=`echo $1 | tr -d '"'`
else
    echo "Must supply transit-gateway-route-table-id exiting ....."
    exit
fi


for c in `seq 0 0`; do
   
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm
    awsout=`eval $cm`
    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        #echo "found $count TGW routes"
        for i in `seq 0 $count`; do
            #echo $i
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].DestinationCidrBlock" | tr -d '"'`
        
            echo $cname
            rname=${cname//./_}
            rname=${rname//\//_}
            rname=`printf "%s_%s" $tgwrtbid $rname`
            #echo $rname
            fn=`printf "%s__%s.tf" $ttft $rname`
            rexists="no"
          
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                rexists="yes"
            fi
            #echo "rexists = $rexists"
            if [[ "$rexists" == "no" ]]; then

                printf "resource \"%s\" \"%s\" {" $ttft $rname > $ttft.$rname.tf
                printf "}" >> $ttft.$rname.tf
                echo "importing on  $ttft.$rname \"${tgwrtbid}_${cname}\""
                terraform import $ttft.$rname "${tgwrtbid}_${cname}"

                terraform state show $ttft.$rname > t2.txt
                rm $ttft.$rname.tf
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
                        if [[ ${tt1} == "association_default_route_table_id" ]];then skip=1;fi
                        if [[ ${tt1} == "vpc_owner_id" ]];then skip=1;fi
                        if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                        if [[ ${tt1} == "transit_gateway_attachment_id" ]];then 
                            tt2=`echo $tt2 | tr -d '"'`
                            t1=`printf "%s = aws_ec2_transit_gateway_vpc_attachment.%s.id" ${tt1} ${tt2}`
                        fi
                        if [[ ${tt1} == "transit_gateway_route_table_id" ]];then 
                            tt2=`echo $tt2 | tr -d '"'`
                            t1=`printf "%s = aws_ec2_transit_gateway_route_table.%s.id" ${tt1} ${tt2}`
                        fi
                        if [[ ${tt1} == "default_propagation_route_table" ]];then skip=1;fi
                        if [[ ${tt1} == "default_association_route_table" ]];then skip=1;fi
                        #if [[ ${tt1} == "ipv6_cidr_block" ]];then skip=1;fi
                    fi
                    if [ "$skip" == "0" ]; then
                        #echo $skip $t1
                        echo $t1 >> $fn
                    fi
                    
                done <"$file"
            fi # if rexists
        done # for i
    fi
done  # for c
terraform fmt
#terraform validate
rm -f t*.txt


