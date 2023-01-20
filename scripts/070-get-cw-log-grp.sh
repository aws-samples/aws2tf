#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS logs describe-log-groups --log-group-name-prefix \"$1\"" 
else
    cmd[0]="$AWS logs describe-log-groups"
fi

pref[0]="logGroups"
tft[0]="aws_cloudwatch_log_group"
idfilt[0]="logGroupName"
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
            cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            echo "$ttft $cname import"
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi
            #echo "calling import sub"
            ../../scripts/parallel_import2.sh $ttft $cname &
            jc=`jobs -r | wc -l | tr -d ' '`
            while [ $jc -gt $ncpu ];do
                echo "Throttling - $jc Terraform imports in progress"
                sleep 10
                jc=`jobs -r | wc -l | tr -d ' '`
            done

        done

        jc=`jobs -r | wc -l | tr -d ' '`
        echo "Waiting for $jc Terraform imports"
        wait       
        echo "Wait completed ..... imported $count"
        ../../scripts/parallel_statemv.sh $ttft
        
        for i in `seq 0 $count`; do
            #echo $i
            cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            echo "$ttft $cname tf files"
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

            file=`printf "%s-%s-1.txt" $ttft $rname`
            if [ ! -f "$file" ] ; then echo "$file does not exist skipping" && continue; fi
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
                    if [[ ${tt1} == "vpc_id" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_vpc.%s.id" $tt1 $tt2`
                    fi
                # else
                    #
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"
            
        done

    fi
done

rm -f $ttft*.txt



