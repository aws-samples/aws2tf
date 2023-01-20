#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS ec2 describe-vpcs --vpc-ids $1"
else
    cmd[0]="$AWS ec2 describe-vpcs"
fi
pref[0]="Vpcs"
tft[0]="aws_vpc"
idfilt[0]="VpcId"
ncpu=$(getconf _NPROCESSORS_ONLN)
ncpu=`expr $ncpu - 1`
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
    #echo $count
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`

        for i in `seq 0 $count`; do
            #echo $i
            cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then continue; fi
            
            #echo "calling import sub"
            #terraform state rm $ttft.$rname > /dev/null
            echo "$ttft $cname import"
            . ../../scripts/parallel_import2.sh $ttft $cname &
            jc=`jobs -r | wc -l | tr -d ' '`
            while [ $jc -gt $ncpu ];do
                echo "Throttling - $jc Terraform imports in progress"
                sleep 10
                jc=`jobs -r | wc -l | tr -d ' '`
            done
        done

         
        jc=`jobs -r | wc -l | tr -d ' '`
        if [ $jc -gt 0 ];then
            echo "Waiting for $jc Terraform imports"
            wait
            echo "Finished importing"
        fi
                
        ../../scripts/parallel_statemv.sh $ttft
        
        
        # tf files
        for i in `seq 0 $count`; do
            #echo $i
            cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            #echo "$ttft $cname tf files"
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then continue; fi

            file=`printf "%s-%s-1.txt" $ttft $rname`
            
            echo $aws2tfmess > $fn
            skipipv6=0
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
                    if [[ ${tt1} == "allocated_capacity" ]];then skip=1;fi
                    if [[ ${tt1} == "dhcp_options_id" ]];then skip=1;fi
                    if [[ ${tt1} == "main_route_table_id" ]];then skip=1;fi
                    if [[ ${tt1} == "default_security_group_id" ]];then skip=1;fi
                    if [[ ${tt1} == "default_route_table_id" ]];then skip=1;fi
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    if [[ ${tt1} == "default_network_acl_id" ]];then skip=1;fi
                    if [[ ${tt1} == "ipv6_association_id" ]];then skip=1;fi
                    if [[ ${tt1} == "enable_classiclink" ]];then skip=1;fi
                    if [[ ${tt1} == "enable_classiclink_dns_support" ]];then skip=1;fi
                    if [[ ${tt1} == "assign_generated_ipv6_cidr_block" ]];then 
                        tt2=`echo $tt2 | tr -d '"'`
                        if [[ $tt2 == "true" ]];then
                            skipipv6=1
                        fi
                    fi
                    if [[ ${tt1} == "ipv6_cidr_block" ]];then 
                        if [[ $skipipv6 == "1" ]];then
                            skip=1;
                        fi
                    fi
                    if [[ ${tt1} == "ipv6_netmask_length" ]];then
                        tt2=`echo $tt2 | tr -d '"'`
                        if [[ "${tt2}" == "0" ]];then skip=1; fi
                    fi
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"

            #dfn=`printf "data/data_%s__%s.tf" $ttft $cname`
            #printf "data \"%s\" \"%s\" {\n" $ttft $cname > $dfn
            #printf "id = \"%s\"\n" $cname >> $dfn
            #printf "}\n" $ttft $cname >> $dfn
            
        done
    fi
done

rm -f *.backup 
rm -f $ttft*.txt


#