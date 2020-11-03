#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS ec2 describe-transit-gateway-attachments --filters \"Name=transit-gateway-id,Values=$1\"" 
else
    cmd[0]="$AWS ec2 describe-transit-gateway-attachments"
fi

pref[0]="TransitGatewayAttachments"
tft[0]="aws_ec2_transit_gateway_vpn_attachment"
tgwlist=()
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
            atttype=`echo $awsout | jq ".${pref[(${c})]}[(${i})].ResourceType" | tr -d '"'`
            if [ "$atttype" == "vpn" ]; then
                cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].TransitGatewayAttachmentId" | tr -d '"'`
                tgwid=`echo $awsout | jq ".${pref[(${c})]}[(${i})].TransitGatewayId" | tr -d '"'`
                vpnid=`echo $awsout | jq ".${pref[(${c})]}[(${i})].ResourceId" | tr -d '"'`
                echo $cname $tgwid
                printf "data \"%s\" \"%s\" {\n" $ttft $cname > $ttft.$cname.tf
                printf "transit_gateway_id = aws_ec2_transit_gateway.%s.id \n" $tgwid >> $ttft.$cname.tf
                printf "vpn_connection_id  = aws_vpn_connection.%s.id \n" $vpnid >> $ttft.$cname.tf
                printf "}\n" $cname >> $ttft.$cname.tf
### get vpn connection
                ../../scripts/227-get-vpn-connections.sh $tgwid


            fi
        done

    fi
done
terraform fmt
#terraform validate
rm -f t*.txt

