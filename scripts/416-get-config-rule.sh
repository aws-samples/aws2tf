#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS configservice describe-config-rules  --config-rule-names $1" 
else
    cmd[0]="$AWS configservice describe-config-rules"
fi

pref[0]="ConfigRules"
tft[0]="aws_config_config_rule"
idfilt[0]="ConfigRuleName"
ncpu=$(getconf _NPROCESSORS_ONLN)
ncpu=`expr $ncpu - 1`
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
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then continue; fi

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


        for i in `seq 0 $count`; do
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}" | tr -d '"'`
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi          
            file=`printf "%s-%s-1.txt" $ttft $rname`
            
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
                    if [[ ${tt1} == "rule_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "availability_zone" ]];then skip=1;fi
                    if [[ ${tt1} == "availability_zone_id" ]];then skip=1;fi
                    if [[ ${tt1} == "vpc_id" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_vpc.%s.id" $tt1 $tt2`
                    fi
                    if [[ ${tt1} == "description" ]]; then
                        tt2=`echo "$tt2" | tr -d '"'`
                        dl=${#tt2}
                        #echo $dl $tt2
                        if [[ $dl -gt 254 ]];then 
                        tt2=${tt2:0:252}; 
                        echo "--> description shortened"
                        fi
                        dl=${#tt2}
                        #echo $dl $tt2
                        t1=`printf "%s = \"%s\"" $tt1 "$tt2"`
                        printf "lifecycle {\n" >> $fn
                        printf "   ignore_changes = [description]\n" >> $fn
                        printf "}\n" >> $fn
                    fi
                    if [[ ${tt1} == "name" ]]; then
                        tt2=`echo "$tt2" | tr -d '"'`
                        nl=${#tt2}
                        if [[ $nl -gt 64 ]];then tt2=${tt2:0:64}; fi
                        tt2=$(echo $tt2 | tr -d ' ')
                        t1=`printf "%s = \"%s\"" $tt1 "$tt2"`
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
rm -f $ttft*.txt
