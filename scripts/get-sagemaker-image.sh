#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]=$(printf "$AWS sagemaker list-images | jq '. | select(.Images[].ImageName==\"%s\")'" $1)
else
    cmd[0]="$AWS sagemaker list-images"
fi

pref[0]="Images"
tft[0]="aws_sagemaker_image"
idfilt[0]="ImageName"

#rm -f ${tft[0]}.tf

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm
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
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}" | tr -d '"'`
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
                        
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi

            echo "$ttft $cname import"
            printf "resource \"%s\" \"%s\" {" $ttft $rname > $fn
            printf "}" $cname >> $fn
            printf "terraform import %s.%s %s" $ttft $rname $cname > import_$ttft_$rname.sh
            terraform import $ttft.$rname $cname | grep Import
            terraform state show -no-color $ttft.$rname > t1.txt
            tfa=`printf "%s.%s" $ttft $rname`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > data/$tfa.json
            #echo $awsj | jq . 
            rm -f $ttft.$rname.tf

            file="t1.txt"
            echo $aws2tfmess > $fn
            keyid=""
            tarn=""
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
         
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    
                    
                    if [[ ${tt1} == "role_arn" ]]; then
                        tarn=`echo $tt2 | tr -d '"'`
                        tanam=$(echo $tarn | rev | cut -f1 -d'/' | rev)
                        tlarn=${tarn//:/_} && tlarn=${tlarn//./_} && tlarn=${tlarn//\//_}
                        t1=`printf "%s = aws_iam_role.%s.arn" $tt1 $tanam`
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

            ../../scripts/get-sagemaker-image-versions.sh $cname

            
        done

    fi
done

rm -f t*.txt

