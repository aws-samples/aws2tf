#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS rds describe-db-subnet-groups --db-subnet-group-name $1"

else
    cmd[0]="$AWS rds describe-db-subnet-groups"
fi

pref[0]="DBSubnetGroups"
tft[0]="aws_db_subnet_group"
idfilt[0]="DBSubnetGroupName"
subnets=()

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
            if [[ "$cname" == "default" ]];then echo "skipping default" && continue;fi
            
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

                    if [[ ${tt1} == "supported_network_types" ]];then
                        tt2=`echo $tt2 | tr -d '"'` 
                        skip=1
                        while [ "$t1" != "]" ] && [ "$tt2" != "[]" ] ;do
                            read line
                            t1=`echo "$line"`
                            #echo $t1
                        done
                    fi


                else
                    if [[ "$t1" == *"subnet-"* ]]; then
                        t1=`echo $t1 | tr -d '"|,'`
                        subnets+=`printf "\"%s\" " $t1`
                        t1=`printf "aws_subnet.%s.id," $t1`
                    fi     
                fi

                if [ "$skip" == "0" ]; then echo "$t1" >> $fn;fi               
            done <"$file"
            
            # get subnetss
            for sub in ${subnets[@]}; do
                #echo "therole=$therole"
                sub1=`echo $sub | tr -d '"'`
                echo "calling for $sub1"
                if [ "$sub1" != "" ]; then
                    ../../scripts/105-get-subnet.sh $sub1
                    if [[ $? -eq 199 ]];then
                        echo "WARNING: Could not find depandant subnet $sub1"
                        echo "Removing $ttft $cname resources to prevent validation errors"
                        rm -f $fn
                        terraform state rm $ttft.${rname}
                        exit 199
                    fi
                fi
            done
        done
    fi 
done

#rm -f t*.txt



