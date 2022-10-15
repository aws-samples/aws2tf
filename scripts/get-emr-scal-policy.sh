#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS emr get-managed-scaling-policy --cluster-id $1" 
else
    echo "Must cpecify a cluster id"
    exit
fi

pref[0]="ManagedScalingPolicy"
tft[0]="aws_emr_managed_scaling_policy"
idfilt[0]="InstanceGroupId"

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
            fn=`printf "%s__%s__%s.tf" $ttft $1 $cname`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
            printf "resource \"%s\" \"%s__%s\" {" $ttft $1 $cname > $ttft.$1__$cname.tf
            printf "}" $cname >> $ttft.$1__$cname.tf
            printf "terraform import %s.%s__%s %s__%s" $ttft $1 $cname $1 $cname > data/import_$ttft_$1_$cname.sh
            terraform import $ttft.$1__$cname "$1" | grep Import
            
            terraform state show -no-color $ttft.$1__$cname > t1.txt
            tfa=`printf "data/%s.%s__%s" $ttft $1 $cname`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > data/$tfa.json
            #echo $awsj | jq . 
            rm -f $ttft.$1__$cname.tf

            file="t1.txt"
            echo $aws2tfmess > $fn
            iddo=0
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
                    if [[ ${tt1} == "resource_owner" ]];then skip=1;fi
                    if [[ ${tt1} == "running_instance_count" ]];then skip=1;fi
                    if [[ ${tt1} == "status" ]];then skip=1;fi

                    #if [[ ${tt1} == "availability_zone" ]];then skip=1;fi
                    if [[ ${tt1} == "last_updated_date" ]];then skip=1;fi
                    if [[ ${tt1} == "vpc_id" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_vpc.%s.id" $tt1 $tt2`
                    fi
               
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"
           
        done

    fi
done

rm -f t*.txt

