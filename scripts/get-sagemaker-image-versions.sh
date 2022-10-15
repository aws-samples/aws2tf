#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS sagemaker list-image-versions --image-name $1"
else
    echo "Must supply image name as a parameter exiting ..."
    exit   
fi

pref[0]="ImageVersions"
tft[0]="aws_sagemaker_image_version"
idfilt[0]="ImageVersionArn"

#rm -f ${tft[0]}.tf

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	echo $cm
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
            #cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}" | tr -d '"'`
            cname=$(echo $1)
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
                        
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi

            echo "$ttft $cname import"
            printf "resource \"%s\" \"%s\" {}" $ttft $rname > $fn
            printf "terraform import %s.%s %s" $ttft $rname $cname > import_$ttft_$rname.sh
            terraform import $ttft.$rname $cname | grep Import
            terraform state show -no-color $ttft.$rname > t1.txt
   
            rm -f $fn

            file="t1.txt"
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
                    
                    if [[ ${tt1} == "image_arn" ]]; then skip=1; fi 
                    if [[ ${tt1} == "container_image" ]]; then skip=1; fi 
                    if [[ ${tt1} == "version" ]]; then skip=1; fi 

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

