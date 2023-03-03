#!/bin/bash
pref[0]="SecurityConfigurations"
tft[0]="aws_emr_security_configuration"
idfilt[0]="Name"
if [ "$1" != "" ]; then
    cmd[0]=`printf "$AWS emr list-security-configurations  | jq '.${pref}[] | select(.${idfilt}==\"%s\")' | jq ." $1`
else
    cmd[0]="$AWS emr list-security-configurations"
fi


for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm
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
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            if [ "$1" != "" ]; then
                cname=`echo $awsout | jq ".${idfilt[(${c})]}" | tr -d '"'`
            else
                cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}" | tr -d '"'`
            fi
            echo "$ttft $cname"
            fn=`printf "%s__%s.tf" $ttft $cname`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
            printf "resource \"%s\" \"%s\" {}\n" $ttft $cname > $fn

            terraform import $ttft.$cname "$cname" | grep Import
            terraform state show -no-color $ttft.$cname > t1.txt

            #echo $awsj | jq . 
            rm -f $fn

            file="t1.txt"
            iddo=0
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
                    if [[ ${tt1} == "resource_owner" ]];then skip=1;fi
                    if [[ ${tt1} == "creation_date" ]];then skip=1;fi
                    if [[ ${tt1} == "master_public_dns" ]];then skip=1;fi
                    if [[ ${tt1} == "realm" ]];then 
                    echo "kdc_admin_password = \"CHANGE-ME\"" >> $fn

                    fi
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

