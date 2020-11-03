#!/bin/bash
if [ "$1" != "" ]; then
    arn=`echo $1`
    arn="arn:aws:servicediscovery:eu-west-1:566972129213:service/srv-pdhsivbua7ukgz6i"
    comm=`printf "$AWS servicediscovery list-services | jq '.Services[] | select(.Arn==\"%s\").Id' | tr -d '\"'" $arn`
    srvid=`eval $comm`
    nsid=`$AWS servicediscovery get-service --id $srvid | jq .Service.NamespaceId | tr -d '\"'`
    echo $nsid
    # get zone id
    hzid=`$AWS servicediscovery get-namespace --id $nsid | jq .Namespace.Properties.DnsProperties.HostedZoneId | tr -d '"'`
    echo $hzid
    cmd[0]="$AWS route53 list-resource-record-sets --hosted-zone-id $hzid" 
else
    echo "Must provide a service Arn - exiting ..."
    exit
fi

ttft="aws_route53_zone"


#rm -f ${tft[0]}.tf


            cname=`echo $hzid`
            
            rname=${cname//:/_}
            rname=${rname//\//_}
            echo "getting hostzone $rname"
            fn=`printf "%s__%s.tf" $ttft $rname`
            printf "resource \"%s\" \"%s\" {\n" $ttft $rname > $fn
            printf "}"  >> $fn
            
            terraform import $ttft.$rname $rname
            terraform state show $ttft.$rname > t2.txt
            
            rm $fn

            tfa=`printf "%s.%s" $ttft $rname`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > $tfa.json
            #echo $awsj | jq . 
           
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
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    if [[ ${tt1} == "propagate_tags" ]];then skip=1;fi
                    #if [[ ${tt1} == "availability_zone" ]];then skip=1;fi
                    if [[ ${tt1} == "availability_zone_id" ]];then skip=1;fi
                    if [[ ${tt1} == "state" ]];then skip=1;fi
                    if [[ ${tt1} == "dns_entry" ]];then skip=1;fi

                    if [[ ${tt1} == "requester_managed" ]];then skip=1;fi
                    if [[ ${tt1} == "revision" ]];then skip=1;fi
                    if [[ ${tt1} == "cidr_blocks" ]];then
                        echo "matched cidr"  
                        skip=1
                        while [[ "$t1" != "]" ]] ;do
                            read line
                            t1=`echo "$line"`
                            echo $t1
                        done
                    fi
                    if [[ ${tt1} == "network_interface_ids" ]];then skip=1;fi
                    if [[ ${tt1} == "vpc_id" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_vpc.%s.id" $tt1 $tt2`
                    fi
               
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo $t1 >> $fn
                fi
                
            done <"$file"
            

terraform fmt
terraform validate
rm t*.txt
#$AWS route53 get-hosted-zone --id Z0956511MQ670ZMC5AV9
# get vpc-id from above
# resource "aws_service_discovery_private_dns_namespace" "example" {
# name from   $AWS servicediscovery get-namespace --id $nsid
# vpc =
# }  



