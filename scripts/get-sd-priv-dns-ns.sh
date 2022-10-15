
#!/bin/bash
echo "entered get-sd-priv-dns-ns with $1"
if [ "$1" != "" ]; then
    cmd[0]="$AWS servicediscovery get-namespace --id $1" 
    pref[0]="Namespace"
else
    echo "must specify a namespace id"
    exit
    #cmd[0]="$AWS servicediscovery list-namespaces"
    #pref[0]="Namespaces"
fi

tft[0]="aws_service_discovery_private_dns_namespace"
idfilt[0]="Id"

#rm -f ${tft[0]}.tf

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    #if [[ "$1" != "" ]]; then
        count=1
    #else
        #count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    #fi

    if [[ "$count" -gt "0" ]]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
   
            if [[ "$1" != "" ]]; then
                cname=`echo $awsout | jq ".${pref[(${c})]}.${idfilt[(${c})]}" | tr -d '"'`
                nstype=`echo $awsout | jq ".${pref[(${c})]}.Type" | tr -d '"'`
            else
                cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}" | tr -d '"'`
            fi

            if [[ "$nstype" != "DNS_PRIVATE" ]];then
                echo "Namespace type is not DNS_PRIVATE exiting ...."
                exit
            fi

            echo "cname=$cname"
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}

            
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [[ -f "$fn" ]] ; then echo "$fn exists already skipping" && continue; fi       
            echo "$ttft $cname Import"
            #also need vpc id for import
            hz=`${AWS} servicediscovery get-namespace --id ${cname} | jq '.Namespace.Properties.DnsProperties.HostedZoneId' | tr -d '"'`
            hznam=`${AWS} servicediscovery get-namespace --id ${cname} | jq '.Namespace.Name' | tr -d '"'`
            echo "Hosted Zone id=$hz"
            vpc=`$AWS route53 get-hosted-zone --id $hz | jq .VPCs[0].VPCId | tr -d '"'`
            echo "$ttft $cname $vpc Import"
            printf "resource \"%s\" \"%s\" {" $ttft $rname > $fn
            printf "}" >> $fn
            terraform import $ttft.$rname "${cname}:${vpc}" | grep Import
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
                    if [[ ${tt1} == "ipv6_cidr_block_association_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "availability_zone" ]];then skip=1;fi
                    if [[ ${tt1} == "availability_zone_id" ]];then skip=1;fi
                    if [[ ${tt1} == "state" ]];then skip=1;fi
                    if [[ ${tt1} == "dns_entry" ]];then skip=1;fi

                    if [[ ${tt1} == "hosted_zone" ]];then skip=1;fi
                    if [[ ${tt1} == "prefix_list_id" ]];then skip=1;fi
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

                    if [[ ${tt1} == "vpc" ]]; then
                        vpcid=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_vpc.%s.id" $tt1 $vpcid`
                    fi
               
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"
            # get the namespace vpc
            if [[ "$vpcid" != "" ]];then
                 ../../scripts/100-get-vpc.sh $vpcid
            fi
            
        done
    fi
done
echo "exit $ttft"

rm -f t*.txt
exit