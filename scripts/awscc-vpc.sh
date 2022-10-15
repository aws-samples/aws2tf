# VPC cloud control version
export AWS=aws
#!/bin/bash
if [ "$1" != "" ]; then
    cm="$AWS cloudcontrol get-resource --type-name AWS::EC2::VPC --identifier $1"
    pref="ResourceDescription"
else
    cm="$AWS cloudcontrol list-resources --type-name AWS::EC2::VPC"
    pref="ResourceDescriptions"
fi

#aws cloudcontrol list-resources --type-name AWS::EC2::VPC | jq -r .ResourceDescriptions[].Properties | jq .
ttft="awscc_ec2_vpc"
idfilt="Identifier"
echo $cm
awsout=`eval $cm 2> /dev/null`
echo $awsout | jq .
if [ "$awsout" == "" ];then echo "$cm : You don't have access for this resource" && exit; fi
    
count=`echo $awsout | jq ".${pref} | length"`
echo $count
if [ "$count" -eq "0" ];then echo "Zero count" && exit ; fi
if [ "$1" != "" ]; then count=1; fi
count=`expr $count - 1`
echo $count
for i in `seq 0 $count`; do
            echo "in loop $i"
            if [ "$1" != "" ]; then
                cname=$(echo $awsout | jq -r ".${pref}.${idfilt}")
            else
                cname=$(echo $awsout | jq -r ".${pref}[(${i})].${idfilt}")
            fi
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            
            echo "$ttft $cname import"
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

            printf "resource \"%s\" \"%s\" {}" $ttft $rname > $fn

            terraform import $ttft.${rname} "${cname}" | grep Import
            terraform state show -no-color $ttft.${rname} > t1.txt

            rm -f $fn
         

            file="t1.txt"
            echo $aws2tfmess > $fn

            while IFS= read line
            do
				skip=0
                # display $line or do something with $line
                t1=`echo "$line"` 
                if [[ "$t1" == *"ttl"* ]]; then inttl=1; fi
                if [[ "$t1" == "}" ]]; then inttl=0; fi

                if [[ ${t1} == *"="* ]];then
                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                    tt2=`echo "$line" | cut -f2- -d'='`             
                    if [[ ${tt1} == "id" ]];then skip=1; fi          
                    if [[ ${tt1} == "arn" ]];then skip=1;fi
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    
                fi

                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"
            #../../scripts/get-glue-table.sh ${catid} ${cname}
done






exit





#aws cloudcontrol list-resources --type-name AWS::EC2::VPC