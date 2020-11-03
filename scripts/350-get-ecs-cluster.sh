#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS ecs describe-clusters --cluster $1" 
    pref[0]="clusters"
    idfilt[0]="clusterName"
else
    cmd[0]="$AWS ecs list-clusters"
    pref[0]="clusterArns"
    idfilt[0]=""
fi

tft[0]="aws_ecs_cluster"


#rm -f ${tft[0]}.tf

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	echo $cm
    awsout=`eval $cm`
    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            if [ "$1" != "" ]; then
                cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}" | tr -d '"'`
            else
                cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})]" | cut -f2 -d'/' | tr -d '"'`
            fi
            echo $cname
            fn=`printf "%s__%s.tf" $ttft $cname`
            printf "resource \"%s\" \"%s\" {" $ttft $cname > $ttft.$cname.tf
            printf "}" $cname >> $ttft.$cname.tf
            terraform import $ttft.$cname $cname
            terraform state show $ttft.$cname > t2.txt
            tfa=`printf "%s.%s" $ttft $cname`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > $tfa.json
            #echo $awsj | jq . 
            rm $ttft.$cname.tf
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
                    if [[ ${tt1} == "ipv6_cidr_block_association_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "availability_zone" ]];then skip=1;fi
                    if [[ ${tt1} == "availability_zone_id" ]];then skip=1;fi
                    if [[ ${tt1} == "state" ]];then skip=1;fi
                    if [[ ${tt1} == "dns_entry" ]];then skip=1;fi

                    if [[ ${tt1} == "requester_managed" ]];then skip=1;fi
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
            ../../scripts/get-ecs-service.sh $cname
        done
    fi
done
terraform fmt
terraform validate
rm -f t*.txt


# $AWS ecs list-attributes --target-type container-instance --cluster myecsprod
# $AWS ecs list-container-instances --cluster myecsprod
# $AWS ecs describe-container-instances --container-instances arn:aws:ecs:eu-west-1:566972129213:container-instance/b05e4516-71c3-487f-a2cf-31b42f7bc722 --cluster myecsprod 
# get instance id
# use above to find asg
# $AWS autoscaling describe-auto-scaling-groups

