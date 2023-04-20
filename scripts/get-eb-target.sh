#!/bin/bash
mysub=`echo $AWS2TF_ACCOUNT`
myreg=`echo $AWS2TF_REGION`
#echo "globals = $mysub $myreg"
bus="default"
if [[ "$1" != "" ]]; then
    if [[ "$1" == *"|"* ]]; then
        bus=$(echo $1 | cut -f1 -d '|')
        ru=$(echo $1 | cut -f2 -d '|')      
        cmd[0]="$AWS events list-targets-by-rule --rule $ru --event-bus-name $bus" 
    else
        echo "invalid format should be bus|rulename try with default .."
        cmd[0]="$AWS events list-targets-by-rule --rule $1 --event-bus-name default"
        ru=$(echo $1)
    fi
else
    echo "must pass bus|rulename as parameter exiting .."
    exit
fi

pref[0]="Targets"
tft[0]="aws_cloudwatch_event_target"
idfilt[0]="Id"


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
            cname=`echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}"`

            #echo "$ttft $bus $ru $cname"

            fn=`printf "%s__%s__%s__%s.tf" $ttft $bus $ru $cname`
            if [ -f "$fn" ] ; then
                    echo "$fn exists already skipping"
                    continue
            fi

            printf "resource \"%s\" \"%s__%s__%s\" {}\n" $ttft $bus $ru $cname > $fn

            if [[ "$bus" == "default" ]];then
                terraform import $ttft.${bus}__${ru}__${cname} "${ru}/${cname}" | grep Importing
            else
                terraform import $ttft.${bus}__${ru}__${cname} "${bus}/${ru}/${cname}" | grep Importing
            fi
            
# get input_template to file
            
            echo $awsout | jq ".${pref[(${c})]}[(${i})].InputTransformer.InputTemplate" > data/it_${bus}_${ru}_${cname}.json
            inpt=$(echo $awsout | jq ".${pref[(${c})]}[(${i})].InputTransformer.InputTemplate")
            
            terraform state show -no-color $ttft.${bus}__${ru}__${cname} > t1.txt

            #echo $awsj | jq . 
            rm -f $fn
  
            file="t1.txt"
            echo $aws2tfmess > $fn
            lfn=""
            while IFS= read line
            do
				skip=0
                # display $line or do something with $line
                t1=`echo "$line"` 
                if [[ ${t1} == *"="* ]];then
                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                    tt2=`echo "$line" | cut -f2- -d'='`
                    if [[ ${tt1} == "arn" ]];then 
                        tt2=$(echo $tt2 | tr -d '"')
                        if [[ "$tt2" == *":lambda:"* ]]; then
                            lfn=$(echo $tt2 | rev | cut -f1 -d':' | rev)
                            t1=`printf "%s = aws_lambda_function.%s.arn" $tt1 $lfn`
                        fi  
                        if [[ "$tt2" == "arn:aws:sns:${myreg}:${mysub}:"* ]]; then
                            rsns=`echo $tt2 | tr -d '"'` 
                            trole=${rsns//:/_} && trole=${trole//./_} && trole=${trole//\//_} && trole=${trole/${mysub}/}                    
                            t1=`printf "%s = aws_sns_topic.%s.arn" $tt1 $trole`
                        elif [[ "$tt2" == *"arn:aws:codepipeline:${myreg}:${mysub}:"* ]];then
                            cpid=`echo $tt2 | rev | cut -f1 -d':' | rev | tr -d '"'`                                 
                            t1=`printf "%s = aws_codepipeline.r-%s.arn" $tt1 $cpid`

                        fi             
                    fi     

                    if [[ ${tt1} == "id" ]];then 
                        printf "lifecycle {\n" >> $fn
                        printf "   ignore_changes = [input_transformer[0].input_template]\n" >> $fn
                        printf "}\n" >> $fn
                    skip=1; 
                    fi          
                    if [[ ${tt1} == "role_arn" ]];then 
                        trarn=`echo "$tt2" | rev | cut -f1 -d'/' | rev | tr -d '"'`
                        t1=`printf "%s = aws_iam_role.r-%s.arn" $tt1 $trarn`
                    fi
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    if [[ ${tt1} == "input_template" ]];then
                        t1=`printf "input_template = jsonencode(file(\"data/it_%s_%s_%s.json\"))" $bus $ru $cname`
                        
                        if [[ "$tt2" == *"EOT"* ]];then
                            read line
                            ts1=`echo "$line"`
                            echo "EOT ts1 = $ts1"
                            while [[ $ts1 != *"EOT"* ]];do
                                read line
                                ts1=`echo "$line"`
                            done
                            
                        fi

                    fi

                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"
            #echo "--> lfn = $lfn"
            if [[ "$lfn" != "" ]];then
                ../../scripts/700-get-lambda-function.sh $lfn
            fi
            if [[ "$trarn" != "" ]];then
                ../../scripts/050-get-iam-roles.sh $trarn
            fi

            if [[ "$cpid" != "" ]];then
                ../../scripts/629-get-code-pipeline.sh $cpid
            fi

            
        done
    fi 
done

#rm -f t*.txt

