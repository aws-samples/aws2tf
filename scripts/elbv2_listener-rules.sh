#!/bin/bash
if [[ "$1" != "" ]]; then
    if [[ "$1" == *"listener-rule"* ]];then
        cmd[0]="$AWS elbv2 describe-rules --rule-arns \"$1\""
    else
        cmd[0]="$AWS elbv2 describe-rules --listener-arn \"$1\""
    fi
else
    echo "must pass listener or listener-rule arn"
    exit
fi

c=0
cm=${cmd[$c]}

pref[0]="Rules"
tft[0]="aws_lb_listener_rule"
idfilt[0]="RuleArn"

rm -f ${tft[(${c})]}.*.tf

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
    #echo $awsout | jq .

    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            echo $i
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}" | tr -d '"'`
            echo "$ttft $cname"
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            fn=`printf "%s__%s.tf" $ttft $rname`
            #echo $fn
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi
            printf "resource \"%s\" \"%s\" {\n" $ttft $rname > $fn
            printf "}"  >> $fn

            terraform import $ttft.$rname "$cname" | grep Import
            terraform state show -no-color $ttft.$rname > t1.txt
            
            rm -f $fn

            file="t1.txt"
            
         
            #echo "#" > $fn
            echo $aws2tfmess > $fn
            while IFS= read line
            do
				skip=0
                # display $line or do something with $line
                t1=`echo "$line"` 
                if [[ ${t1} == *"="* ]];then
                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                    tt2=`echo "$line" | cut -f2- -d'='`
                    if [[ ${tt1} == "arn" ]];then
                        if [[ ${tt2} == *"listener"* ]];then
                            listarn=`echo ${tt2}`
                            echo $listarn
                            skip=1
                        else
                            skip=0; 
                        fi
                    fi                
                    if [[ ${tt1} == "id" ]];then skip=1; fi          
                    if [[ ${tt1} == "role_arn" ]];then skip=1;fi
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    if [[ ${tt1} == "association_id" ]];then skip=1;fi

                    if [[ ${tt1} == "order" ]];then skip=1;fi
                    if [[ ${tt1} == "dns_name" ]];then skip=1;fi
                    if [[ ${tt1} == "vpc_id" ]];then skip=1;fi
                    if [[ ${tt1} == "default_version" ]];then skip=1;fi
                    if [[ ${tt1} == "latest_version" ]];then skip=1;fi
                    if [[ ${tt1} == "security_group_names" ]];then skip=1;fi
                    if [[ ${tt1} == "zone_id" ]];then skip=1;fi
                    if [[ ${tt1} == "arn_suffix" ]];then skip=1;fi
                    #if [[ ${tt1} == "ipv6_cidr_block" ]];then skip=1;fi
                    if [[ ${tt1} == "subnet_id" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_subnet.%s.id" $tt1 $tt2`
                    fi
                    if [[ ${tt1} == "listener_arn" ]]; then
                        larn=`echo $tt2 | tr -d '"'`
                        rlarn=${larn//:/_} && rlarn=${rlarn//./_} && rlarn=${rlarn//\//_}
                        t1=`printf "%s = aws_lb_listener.%s.arn" $tt1 $rlarn`
                    fi
                    if [[ ${tt1} == "target_group_arn" ]]; then
                        tarn=`echo $tt2 | tr -d '"'`
                        tlarn=${tarn//:/_} && tlarn=${tlarn//./_} && tlarn=${tlarn//\//_}
                        t1=`printf "%s = aws_lb_target_group.%s.arn" $tt1 $tlarn`
                    fi


                fi
                
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"

            # get the listener
            if [[ "$larn" != "" ]]; then
                ../../scripts/elbv2_listener.sh $larn
            fi
            if [[ "$tarn" != "" ]]; then
                ../../scripts/elbv2-target-groups.sh $tarn
            fi

        done
    fi
done

#rm -f t*.txt

