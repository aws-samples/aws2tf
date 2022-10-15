#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS ec2 describe-vpn-connections --filters \"Name=transit-gateway-id,Values=$1\"" 
else
    cmd[0]="$AWS ec2 describe-vpn-connections"
fi


pref[0]="VpnConnections"
tft[0]="aws_vpn_connection"

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
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].VpnConnectionId" | tr -d '"'`
            echo "$ttft $cname"
            cgwid=`echo $awsout | jq ".${pref[(${c})]}[(${i})].CustomerGatewayId" | tr -d '"'`

            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            echo "$ttft ${cname}"
            
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

            printf "resource \"%s\" \"%s\" {}" $ttft $rname > $fn   
            terraform import $ttft.${rname} "${cname}" | grep Import
            terraform state show -no-color $ttft.${rname} > t1.txt

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
                    if [[ ${tt1} == "transit_gateway_attachment_id" ]];then skip=1;fi
                    if [[ ${tt1} == "tunnel1_vgw_inside_address" ]];then skip=1;fi
                    if [[ ${tt1} == "tunnel1_preshared_key" ]];then skip=1;fi
                    if [[ ${tt1} == "tunnel2_preshared_key" ]];then skip=1;fi
                    if [[ ${tt1} == "tunnel1_bgp_asn" ]];then skip=1;fi
                    if [[ ${tt1} == "tunnel2_bgp_asn" ]];then skip=1;fi
                    if [[ ${tt1} == "tunnel1_address" ]];then skip=1;fi
                    if [[ ${tt1} == "tunnel1_vgw_inside_address" ]];then skip=1;fi
                    if [[ ${tt1} == "tunnel2_address" ]];then skip=1;fi
                    if [[ ${tt1} == "tunnel2_vgw_inside_address" ]];then skip=1;fi
                    if [[ ${tt1} == "tunnel1_cgw_inside_address" ]];then skip=1;fi
                    if [[ ${tt1} == "tunnel2_cgw_inside_address" ]];then skip=1;fi
                    if [[ ${tt1} == "tunnel1_bgp_holdtime" ]];then skip=1;fi
                    if [[ ${tt1} == "tunnel2_bgp_holdtime" ]];then skip=1;fi 

                    if [[ ${tt1} == "vgw_telemetry" ]];then skip=1;fi                                    
                    if [[ ${tt1} == "routes" ]];then skip=1;fi
                    if [[ ${tt1} == "customer_gateway_configuration" ]];then skip=1;fi
                    #echo $tt1
                    if [[ ${tt1} == "type" ]];then
                        echo "$t1" >> $fn
                        echo "}" >> $fn
                        break
                    fi

                fi
                if [[ ${t1} == *"<"* ]] ;then 
                    #echo "one char=" ${t1:0:1}
                    #echo $t1
                    skip=1
                fi

                if [[ ${t1} == *"EOT"* ]] ;then 
                    #echo "one char=" ${t1:0:1}
                    #echo $t1
                    skip=1
                fi

                
                if [ "$skip" == "0" ]; then
                    #echo $tt2                
                    if [[ "$tt2" == *"EOT" ]]; then
                        #echo "******Here*********"
                        t1=`echo "$tt1 = <<EOT"`
                        #echo $t1
                    fi
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"

## get customer gateway
            ../../scripts/220-get-custgw.sh $cgwid
            
        done
    fi
done

#rm -f t*.txt

