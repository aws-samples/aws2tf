#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS rds describe-db-cluster-parameter-groups --db-cluster-parameter-group-name $1"

else
    cmd[0]="$AWS rds describe-db-cluster-parameter-groups"
fi

pref[0]="DBClusterParameterGroups"
tft[0]="aws_rds_cluster_parameter_group"
idfilt[0]="DBClusterParameterGroupName"


for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    if [ "$1" != "" ]; then
        count=1
    else
        count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    fi
    echo "count=$count"
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")          
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            echo "$ttft $cname"
            if [[ "$cname" == "default"* ]];then echo "skipping a default param group" && continue;fi
            
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

            printf "resource \"%s\" \"%s\" {}\n" $ttft $rname > $fn
    
            terraform import $ttft.${rname} "${cname}" | grep Import
            terraform state show -no-color $ttft.${rname} > t1.txt

            rm -f $fn

            file="t1.txt"
            echo $aws2tfmess > $fn
            tarn=""
            s3buck=""
            subnets=()
            while IFS= read line
            do
				skip=0
                # display $line or do something with $line
                t1=`echo "$line"` 
                if [[ ${t1} == *"="* ]];then
                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                    tt2=`echo "$line" | cut -f2- -d'='`
         
                    if [[ ${tt1} == "id" ]];then skip=1;fi
                    if [[ ${tt1} == "arn" ]];then skip=1;fi
                    if [[ ${tt1} == "creation_date" ]];then skip=1;fi
                    if [[ ${tt1} == "last_modified_date" ]];then skip=1;fi    
                fi

                if [ "$skip" == "0" ]; then echo "$t1" >> $fn;fi               
            done <"$file"
            
            # get subnetss
        done
    fi 
done

#rm -f t*.txt



