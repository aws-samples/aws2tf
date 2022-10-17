#!/bin/bash

tft[0]="aws_sagemaker_notebook_instance"
pref[0]="NotebookInstances"
idfilt[0]="NotebookInstanceName"
c=0

cm="$AWS sagemaker list-notebook-instances "
if [[ "$1" != "" ]]; then
    cm=`printf "$cm | jq '. | select(.NotebookInstances[].NotebookInstanceName==\"%s\")'" $1`
fi

count=1
trole=""

#rm -f ${tft[0]}.tf

for c in `seq 0 0`; do
    
    
	ttft=${tft[(${c})]}
	echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    if [[ "$1" == "" ]]; then
        count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    fi
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

            printf "terraform import %s.%s %s" $ttft $cname $cname > data/import_$ttft_$cname.sh
            terraform import $ttft.$cname "$cname" | grep Import
            terraform state show -no-color $ttft.$cname > t1.txt
            tfa=`printf "%s.%s" $ttft $cname`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > data/$tfa.json
            #echo $awsj | jq . 
            rm -f $ttft.$cname.tf

            file="t1.txt"
            echo $aws2tfmess > $fn
            sgs=()
            subnets=()
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
                    #if [[ ${tt1} == "role_arn" ]];then skip=1;fi
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    if [[ ${tt1} == "rule_id" ]];then skip=1;fi
                    if [[ ${tt1} == "url" ]];then skip=1;fi
                    if [[ ${tt1} == "availability_zone_id" ]];then skip=1;fi
                    if [[ ${tt1} == "role_arn" ]]; then
                        rarn=`echo $tt2 | tr -d '"'` 
                        trole=`echo "$tt2" | rev | cut -f1 -d'/' | rev | tr -d '"'`
                        t1=`printf "%s = aws_iam_role.%s.arn" $tt1 $trole`
                    fi
                    if [[ ${tt1} == "security_groups" ]];then 
                        if [[ ${tt2} == *"[]"* ]];then 
                            skip=1
                        fi
                    fi

                else
                    if [[ "$t1" == *"subnet-"* ]]; then
                        t1=`echo $t1 | tr -d '"|,'`
                        subnets+=`printf "\"%s\" " $t1`
                        t1=`printf "aws_subnet.%s.id," $t1`
                    fi
                    if [[ "$t1" == *"sg-"* ]]; then
                        t1=`echo $t1 | tr -d '"|,'`
                        sgs+=`printf "\"%s\" " $t1`
                        t1=`printf "aws_security_group.%s.id," $t1`
                    fi
               
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"

            if [ "$trole" != "" ]; then
                ../../scripts/050-get-iam-roles.sh $trole
            fi

            for sub in ${subnets[@]}; do
                sub1=`echo $sub | tr -d '"'`
                echo "calling for $sub1"
                if [ "$sub1" != "" ]; then
                    ../../scripts/105-get-subnet.sh $sub1
                fi
            done

            for sg in ${sgs[@]}; do
                sg1=`echo $sg | tr -d '"'`
                echo "calling for $sg1"
                if [ "$sg1" != "" ]; then
                    ../../scripts/110-get-security-group.sh $sg1
                fi
            done 



            
        done

    fi
done

rm -f t*.txt

