#!/bin/bash
cmd[0]="$AWS ec2 describe-client-vpn-endpoints"
pref[0]="ClientVpnEndpoints"
tft[0]="aws_ec2_client_vpn_endpoint"
cmd[1]="$AWS ec2 describe-client-vpn-target-networks --client-vpn-endpoint-id "
pref[1]="ClientVpnTargetNetworks"
tft[1]="aws_ec2_client_vpn_network_association"


for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm
    awsout=`eval $cm`
    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
       
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].ClientVpnEndpointId" | tr -d '"'`
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
                    if [[ ${tt1} == "dns_name" ]];then skip=1;fi
                    if [[ ${tt1} == "availability_zone_id" ]];then skip=1;fi
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

        for d in `seq 1 1`; do
            echo inner 2 $cname2
            rm -f ${tft[1]}*.tf
            echo $cmd[1]
            cm2=`printf "%s %s " "${cmd[$d]}" $cname`
            ttft2=${tft[(${d})]}
            echo command2 = $cm2 
            awsout2=`eval $cm2`
            echo $awsout2 | jq .
            count2=`echo $awsout2 | jq ".${pref[(${d})]} | length"`
            count2=`expr $count2 - 1`
            for j in `seq 0 $count2`; do
                fn2=`printf "%s__%s.tf.new" $ttft2 $cname2`             
                cname2=`echo $awsout2 | jq ".${pref[(${d})]}[(${j})].AssociationId" | tr -d '"'`
                subid=`echo $awsout2 | jq ".${pref[(${d})]}[(${j})].TargetNetworkId" | tr -d '"'`
                cvpnid=`echo $awsout2 | jq ".${pref[(${d})]}[(${j})].ClientVpnEndpointId" | tr -d '"'`

                echo $cname2
                printf "resource \"%s\" \"%s\" {\n" $ttft2 $cname2 > $fn2
                printf "subnet_id = \"%s\" \n" $subid >> $fn2
                printf "client_vpn_endpoint_id = \"%s\" \n" $fn2
                printf "}\n" >> $fn2

            done
        done

    fi
done
terraform fmt
terraform validate
#rm -f t*.txt

