#!/bin/bash
if [[ "$1" != "" ]]; then
    cmd[0]="$AWS dynamodb describe-table --table-name $1"
    pref[0]="Table" 
    idfilt[0]="TableName"
else
    cmd[0]="$AWS dynamodb list-tables"
    pref[0]="TableNames"
fi


tft[0]="aws_dynamodb_table"


for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    if [[ "$1" != "" ]]; then
        count=1
    else
        count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    fi
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            if [[ "$1" != "" ]]; then
                cname=`echo $awsout | jq -r ".${pref[(${c})]}.${idfilt[(${c})]}"`
            else
                cname=`echo $awsout | jq -r ".${pref[(${c})]}[(${i})]"`
            fi
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            echo "$ttft $cname"
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

            printf "resource \"%s\" \"%s\" {" $ttft $rname > $fn
            printf "}" >> $fn
    
            terraform import $ttft.${rname} "${cname}" | grep Import
            terraform state show -no-color $ttft.${rname} > t1.txt

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
                if [[ "$t1" == *"ttl"* ]]; then 
                    inttl=1; 
                    tt2=""
                    tt1=""
                fi
                if [[ "$t1" == "}" ]]; then 
                    inttl=0; 
                fi

                if [[ ${t1} == *"="* ]];then
                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                    tt2=`echo "$line" | cut -f2- -d'='`
                    if [[ ${tt1} == "arn" ]];then 
                        printf "lifecycle {\n" >> $fn
                        printf "   ignore_changes = [ttl[0].attribute_name,read_capacity,write_capacity]\n" >> $fn
                        printf "}\n" >> $fn
                        skip=1
                    fi                
                    if [[ ${tt1} == "id" ]];then skip=1; fi          
                    if [[ ${tt1} == "role_arn" ]];then skip=1;fi
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi

                if [[ "$inttl" == "1" ]];then
                    #echo "--> $t1 $tt1 $tt2"
                    if [[ "$tt1" == "attribute_name" ]];then
                        doneatt=1
                    fi
                    if [[ "$tt1" == "enabled" ]];then
                        tt2=`echo $tt2 | tr -d '"'`
                        #echo "** in enabled $tt2"
                        if [[ "$tt2" == "false" ]];then                                                
                            if [[ "$doneatt" == "0" ]];then
                                printf "attribute_name = \"TimeToExist\"\n" >> $fn

                                doneatt=1
                            fi
                        fi
                    fi
                fi
                
            done <"$file"

        done
    fi 
done

#rm -f t*.txt

