#!/bin/bash
if [ "$1" != "" ]; then
    hzid=$(echo $1)
    #arn=`echo $1`
    #arn="arn:aws:servicediscovery:eu-west-1:566972129213:service/srv-pdhsivbua7ukgz6i"
    #comm=`printf "$AWS servicediscovery list-services | jq '.Services[] | select(.Arn==\"%s\").Id' | tr -d '\"'" $arn`
    #srvid=`eval $comm`
    #nsid=`$AWS servicediscovery get-service --id $srvid | jq .Service.NamespaceId | tr -d '\"'`
    #echo $nsid
    # get zone id
    #hzid=`$AWS servicediscovery get-namespace --id $nsid | jq .Namespace.Properties.DnsProperties.HostedZoneId | tr -d '"'`
    echo $hzid
    cmd[0]="$AWS route53 list-resource-record-sets --hosted-zone-id $hzid" 
else
    echo "Must provide a hosted zone id - exiting ..."
    exit
fi

c=0
tft[0]="aws_route53_zone"
ttft=${tft[(${c})]}

#rm -f ${tft[0]}.tf
cname=`echo $hzid`
            

echo "getting hostzone hzid=$cname"
rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
fn=`printf "%s__%s.tf" $ttft $rname`
if [ -f "$fn" ] ; then echo "$fn exists already skipping" && exit; fi

printf "resource \"%s\" \"%s\" {\n" $ttft $rname > $fn
printf "}"  >> $fn
            
terraform import $ttft.$rname "${cname}" | grep Import
terraform state show -no-color $ttft.$rname > t1.txt
            
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
                    if [[ ${tt1} == "propagate_tags" ]];then skip=1;fi
                    #if [[ ${tt1} == "availability_zone" ]];then skip=1;fi
                    if [[ ${tt1} == "availability_zone_id" ]];then skip=1;fi
                    if [[ ${tt1} == "state" ]];then skip=1;fi
                    if [[ ${tt1} == "dns_entry" ]];then skip=1;fi
                    if [[ ${tt1} == "zone_id" ]];then skip=1;fi
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
                    if [[ ${tt1} == "name_servers" ]];then 
                        #echo $t1
                        skip=1
                        lbc=0
                        rbc=0
                        breq=0
                        while [[ $breq -eq 0 ]];do 
                            if [[ "${t1}" == *"["* ]]; then lbc=`expr $lbc + 1`; fi
                            if [[ "${t1}" == *"]"* ]]; then rbc=`expr $rbc + 1`; fi

                            if [[ $rbc -eq $lbc ]]; then 
                                breq=1; 
                            else
                                read line
                                t1=`echo "$line"`
                            fi
                        done 
                    fi

                    if [[ ${tt1} == "network_interface_ids" ]];then skip=1;fi
                    if [[ ${tt1} == "vpc_id" ]]; then
                        vpcid=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_vpc.%s.id" $tt1 $vpcid`
                    fi
               
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"
            if [[ "$vpcid" != "" ]];then
                 ../../scripts/100-get-vpc.sh $vpcid
            fi
            

rm t*.txt




