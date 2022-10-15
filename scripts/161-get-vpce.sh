#!/bin/bash
if [ "$1" != "" ]; then
    if [[ "$1" == "vpce-"* ]]; then
        cmd[0]="$AWS ec2 describe-vpc-endpoints --filters \"Name=vpc-endpoint-id,Values=$1\"" 
    else
        cmd[0]="$AWS ec2 describe-vpc-endpoints --filters \"Name=vpc-id,Values=$1\""
    fi 
else
    cmd[0]="$AWS ec2 describe-vpc-endpoints"
fi

pref[0]="VpcEndpoints"
tft[0]="aws_vpc_endpoint"
idfilt[0]="VpcEndpointId"

#rm -f ${tft[0]}.tf

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	echo $cm
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
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}" | tr -d '"'`
            echo "$ttft $cname"
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

            printf "resource \"%s\" \"%s\" {" $ttft $cname > $fn
            printf "}" >> $fn

            terraform import $ttft.$cname "$cname" | grep Import
            terraform state show -no-color $ttft.$cname > t1.txt
            tfa=`printf "%s.%s" $ttft $cname`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > data/$tfa.json
            #echo $awsj | jq . 
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
                    if [[ ${tt1} == *":"* ]];then 
                        tt1=`echo $tt1 | tr -d '"'`
                        t1=`printf "\"%s\"=%s" $tt1 "$tt2"`
                    fi
                    if [[ ${tt1} == "arn" ]];then skip=1; fi                
                    if [[ ${tt1} == "id" ]];then skip=1; fi          
                    if [[ ${tt1} == "role_arn" ]];then skip=1;fi
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    if [[ ${tt1} == "ipv6_cidr_block_association_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "availability_zone" ]];then skip=1;fi
                    if [[ ${tt1} == "availability_zone_id" ]];then skip=1;fi
                    if [[ ${tt1} == "state" ]];then skip=1;fi
                    #if [[ ${tt1} == "dns_entry" ]];then skip=1;fi
                    if [[ ${tt1} == "dns_entry" ]];then
                        #echo "dns block" 
                        tt2=`echo $tt2 | tr -d '"'` 
                        skip=1
                        while [ "$t1" != "]" ] && [ "$tt2" != "[]" ] ;do
                        #while [[ "$t1" != "]" ]] ;do

                            read line
                            t1=`echo "$line"`
                            #echo $t1
                        done
                    fi


                    if [[ ${tt1} == "requester_managed" ]];then skip=1;fi
                    if [[ ${tt1} == "prefix_list_id" ]];then skip=1;fi
                    if [[ ${tt1} == "cidr_blocks" ]];then
                        #echo "cidr block" 
                        tt2=`echo $tt2 | tr -d '"'` 
                        skip=1
                        while [ "$t1" != "]" ] && [ "$tt2" != "[]" ] ;do
                        #while [[ "$t1" != "]" ]] ;do

                            read line
                            t1=`echo "$line"`
                            #echo $t1
                        done
                    fi
                    if [[ ${tt1} == "network_interface_ids" ]];then 
                        #echo "network interface id block" 
                        tt2=`echo $tt2 | tr -d '"'` 
                        skip=1
                        while [ "$t1" != "]" ] && [ "$tt2" != "[]" ] ;do
                            read line
                            t1=`echo "$line"`
                            #echo $t1
                        done
                    fi
                    if [[ ${tt1} == "vpc_id" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_vpc.%s.id" $tt1 $tt2`
                    fi
                else
                    if [[ "$t1" == *"subnet-"* ]]; then
                        sbid=`echo $t1 | tr -d '"|,'`
                        t1=`printf "aws_subnet.%s.id," $sbid`
                    fi 
                    if [[ "$t1" == *"sg-"* ]]; then
                        sgid=`echo $t1 | tr -d '"|,'`
                        t1=`printf "aws_security_group.%s.id," $sgid`
                    fi
                    if [[ "$t1" == *"rtb-"* ]]; then
                        rtid=`echo $t1 | tr -d '"|,'`
                        t1=`printf "aws_route_table.%s.id," $rtid`
                    fi
               
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"
            if [[ $sgid != "" ]];then
                ../../scripts/110-get-security-group.sh $sgid
            fi
            if [[ $sbid != "" ]];then
                ../../scripts/105-get-subnet.sh $sbid
            fi
            if [[ $rtid != "" ]];then
                ../../scripts/140-get-route-table.sh $rtid
            fi
            
        done
    fi 
done

#if [ "$1" != "" ]; then
#    if [[ "$1" == "vpc-"* ]]; then
#        ../../scripts/get-vpce-services.sh $1
#    fi 
#else
#../../scripts/get-vpce-service-config.sh
#fi

rm -f t*.txt

