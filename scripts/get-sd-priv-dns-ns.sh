#!/bin/bash
p1="default"
r1="eu-west-1"
ttft="aws_service_discovery_private_dns_namespace"
export AWS="$AWS --profile $p1 --region $r1 "
echo $$AWS 
for ids in `${AWS} servicediscovery list-namespaces | jq '.Namespaces[] | select(.Type=="DNS_PRIVATE") | .Id' | tr -d '"'`;do
echo $ids
hz=`${AWS} servicediscovery get-namespace --id $ids | jq '.Namespace.Properties.DnsProperties.HostedZoneId' | tr -d '"'`
hznam=`${AWS} servicediscovery get-namespace --id $ids | jq '.Namespace.Name' | tr -d '"'`
echo $hz
vpc=`$AWS route53 get-hosted-zone --id $hz | jq .VPCs[0].VPCId | tr -d '"'`
cname=`echo $hznam | sed 's/\./_/g'`
echo $cname
fn=`printf "%s__%s.tf" $ttft $cname`
printf "resource \"%s\" \"%s\" {\n" $ttft $cname > $fn
printf "name= \"%s\"\n" $cname >> $fn
printf "vpc= \"%s\"\n" $vpc >> $fn
printf "}\n" $cname >> $fn
done

terraform fmt
terraform validate


