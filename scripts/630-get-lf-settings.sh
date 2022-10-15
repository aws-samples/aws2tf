#!/bin/bash
mysub=`echo $AWS2TF_ACCOUNT`
echo "mysub=$mysub"
if [[ "$1" != "" ]]; then
    cmd[0]="$AWS lakeformation get-data-lake-settings --catalog-id $1"
    pref[0]="Database"
else
    cmd[0]="$AWS lakeformation get-data-lake-settings"
    pref[0]="DataLakeSettings"
fi

pref[0]="DataLakeSettings"
idfilt[0]="Name"
tft[0]="aws_lakeformation_data_lake_settings"


for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        exit
    fi

    count=1

    
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            echo $i
            if [[ "$1" != "" ]]; then
                cname=`echo $1`
            else
                cname=`echo $mysub`
            fi
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            echo "$ttft c__${cname}"
            fn=`printf "%s__c__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

            printf "resource \"%s\" \"c__%s\" {}" $ttft $rname > $fn

    
            terraform import $ttft.c__${rname} "${cname}" | grep Import
            terraform state show -no-color $ttft.c__${rname} > t1.txt

            rm -f $fn

            file="t1.txt"
            echo $aws2tfmess > $fn
            tarn=""
            inttl=0
            doneatt=0
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
        done
    fi 
done

#rm -f t*.txt

