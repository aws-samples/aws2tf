#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS ec2 describe-vpc-endpoint-service-configurations --filters \"Name=service-id,Values=$1\"" 
else
    cmd[0]="$AWS ec2 describe-vpc-endpoint-service-configurations"
fi

pref[0]="ServiceConfigurations"
tft[0]="aws_vpc_endpoint_service"
idfilt[0]="ServiceId"

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
    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}" | tr -d '"'`
            echo "$ttft $cname"
            fn=`printf "%s__%s.tf" $ttft $cname`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
            printf "resource \"%s\" \"%s\" {}" $ttft $cname > $ttft.$cname.tf
            
            terraform import $ttft.$cname "$cname" | grep Import
            terraform state show -no-color $ttft.$cname > t1.txt
            tfa=`printf "%s.%s" $ttft $cname`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > data/$tfa.json
            #echo $awsj | jq . 
            rm -f $ttft.$cname.tf

            file="t1.txt"
            lbs=()
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
                    if [[ ${tt1} == "service_type" ]];then skip=1;fi
      
                    if [[ ${tt1} == "state" ]];then skip=1;fi
                    if [[ ${tt1} == "private_dns_name_configuration" ]];then skip=1;fi
                    if [[ ${tt1} == "service_name" ]];then skip=1;fi

                    if [[ ${tt1} == "requester_managed" ]];then skip=1;fi
                    if [[ ${tt1} == "manages_vpc_endpoints" ]];then skip=1;fi
                    if [[ ${tt1} == "base_endpoint_dns_names" ]];then
                        echo "base_endpoint_dns_names"  
                        skip=1
                        while [[ "$t1" != "]" ]] ;do
                            read line
                            t1=`echo "$line"`
                            #echo $t1
                        done
                    fi
                    if [[ ${tt1} == "availability_zones" ]];then
                        echo "availability_zones"  
                        skip=1
                        while [[ "$t1" != "]" ]] ;do
                            read line
                            t1=`echo "$line"`
                        done
                    fi
                    if [[ ${tt1} == "gateway_load_balancer_arns" ]];then 
                        if [[ ${tt2} == *"[]"* ]];then 
                            skip=1
                        fi
                    fi
                    if [[ ${tt1} == "network_load_balancer_arns" ]];then 
                        if [[ ${tt2} == *"[]"* ]];then 
                            skip=1
                        fi
                    fi

                    if [[ ${tt1} == "network_interface_ids" ]];then skip=1;fi
                    if [[ ${tt1} == "vpc_id" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_vpc.%s.id" $tt1 $tt2`
                    fi
                else
                    if [[ "$t1" == *"arn:aws:elasticloadbalancing:"* ]]; then
                        #echo "in arn"
                        lbarn=`echo $t1 | tr -d '"|,'`
                        #echo $lbarn
                        lbs+=`printf "\"%s\" " $lbarn`
                        #t1=`printf "aws_subnet.%s.id," $t1`
                    fi
               
                fi

                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"

            for lb in ${lbs[@]}; do
                lb1=`echo $lb | tr -d '"'`
                echo "calling for $lb1"
                if [ "$lb1" != "" ]; then
                    ../../scripts/elbv2.sh $lb1
                fi
            done
            
        done
    fi
done

rm -f t*.txt

