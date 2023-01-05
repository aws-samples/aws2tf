#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS kinesis describe-stream --stream-name $1"
    pref[0]="StreamDescription"
else
    cmd[0]="$AWS kinesis list-streams"
    pref[0]="StreamNames"
fi


tft[0]="aws_kinesis_stream"
idfilt[0]="StreamName"


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
    
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            if [ "$1" != "" ]; then
                cname=`echo $awsout | jq -r ".${pref[(${c})]}.${idfilt[(${c})]}"`
            else                
                cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})]")           
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
            s3buck=""
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
                    if [[ ${tt1} == "endpoint" ]];then skip=1;fi
                    if [[ ${tt1} == "estimated_number_of_users" ]];then skip=1;fi 

                    if [[ ${tt1} == "role_arn" ]]; then
                        tarn=`echo $tt2 | tr -d '"'`
                        tanam=$(echo $tarn | rev | cut -f1 -d'/' | rev)
                        tlarn=${tarn//:/_} && tlarn=${tlarn//./_} && tlarn=${tlarn//\//_}
                        t1=`printf "%s = aws_iam_role.%s.arn" $tt1 $tanam`
                    fi    
                    if [[ ${tt1} == "bucket_arn" ]]; then
                        tarn=`echo $tt2 | tr -d '"'`
                        s3buck=$(echo $tarn | rev | cut -f1 -d':' | rev)
                        t1=`printf "%s = aws_s3_bucket.b_%s.arn" $tt1 $s3buck`
                    fi               
                    

                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"

            if [[ "$tarn" != "" ]];then
                ../../scripts/050-get-iam-roles.sh $tarn
            fi
            if [[ "$s3buck" != "" ]];then
                ../../scripts/060-get-s3.sh $s3buck
            fi
        done
    fi 
done

#rm -f t*.txt



