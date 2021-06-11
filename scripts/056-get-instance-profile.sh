#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS iam get-instance-profile --instance-profile-name $1" 
    pref[0]="InstanceProfile"
else
    cmd[0]="$AWS iam list-instance-profiles"
    pref[0]="InstanceProfiles"
fi


tft[0]="aws_iam_instance_profile"
idfilt[0]="InstanceProfileName"

#rm -f ${tft[0]}.tf

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm
    awsout=`eval $cm`
    if [ "$1" != "" ]; then
        count=1
    else
        count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    fi
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            if [ "$1" != "" ]; then
                cname=`echo $awsout | jq ".${pref[(${c})]}.${idfilt[(${c})]}" | tr -d '"'`
            else
                cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}" | tr -d '"'`
            fi
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            echo "$ttft $cname import"
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi
            #echo "calling import sub"
            . ../../scripts/parallel_import.sh $ttft $cname &
        done
        jc=`jobs -r | wc -l | tr -d ' '`
        echo "Waiting for $jc Terraform imports"
        wait
        echo "Finished importing"

        for i in `seq 0 $count`; do
            #echo $i
            if [ "$1" != "" ]; then
                cname=`echo $awsout | jq ".${pref[(${c})]}.${idfilt[(${c})]}" | tr -d '"'`
                rarn=`echo $awsout | jq ".${pref[(${c})]}.Roles[0].Arn" | tr -d '"'`
            else
                cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}" | tr -d '"'`
                rarn=`echo $awsout | jq ".${pref[(${c})]}[(${i})].Roles[0].Arn" | tr -d '"'`
            fi
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            echo "$ttft $cname tf files"
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
                    if [[ ${tt1} == "role" ]];then 
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_iam_role.%s.name" $tt1 $tt2`
                    fi
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    if [[ ${tt1} == "unique_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "availability_zone" ]];then skip=1;fi
                    if [[ ${tt1} == "create_date" ]];then skip=1;fi
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
            echo "role  $rarn"
            ../../scripts/050-get-iam-roles.sh $rarn
            
        done
   
    fi
done

rm -f t*.txt

