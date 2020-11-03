../../scripts/201-get-transit-gateway.sh $1
../../scripts/get-transit-gateway-vpc-attachments.sh $1
../../scripts/get-transit-gateway-vpn-attachments.sh $1
echo "post fix vpn"
for i in `ls aws_ec2_transit_gateway_vpn_attachment*.tf` ; do
#echo $i
tgatid=`echo $i | cut -f2 -d'.'`
echo $tgatid
for j in `ls aws_ec2_transit_gateway_route*.tf` ; do
#echo $j
grep $tgatid $j
    if [ $? -eq 0 ]; then
    echo "Fixing $j"
    comm=`printf "sed 's/aws_ec2_transit_gateway_vpc_attachment.%s/data.aws_ec2_transit_gateway_vpn_attachment.%s/' %s > %s.tmp " $tgatid $tgatid $j $j`
    echo "command = $comm"
    eval $comm
    cp $j.tmp $j
fi
#
done
done
echo "**** Type Validate Call****" 
terraform validate