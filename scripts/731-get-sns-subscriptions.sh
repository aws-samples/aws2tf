#!/bin/bash
mysub=`echo $AWS2TF_ACCOUNT`
myreg=`echo $AWS2TF_REGION`
pref[0]="Subscriptions"
tft[0]="aws_sns_topic_subscription"
idfilt[0]="SubscriptionArn"
count=1
cc=1
if [[ "$1" != "" ]]; then
    if [[ "$1" == "arn:aws:"* ]];then
        cc=$(echo $1 | tr -d -c ':' | wc -m | tr -d ' ')
        if [[ $cc == "5" ]];then 
            cmd[0]="$AWS sns list-subscriptions-by-topic --topic-arn $1"
        else
            cmd[0]=`printf "$AWS sns list-subscriptions | jq '.${pref}[] | select(.${idfilt}==\"%s\")' | jq ." $1`
        fi
    
    else
        echo "invalid topic arn exit ...."
        exit
    fi  
    
else
    cmd[0]="$AWS sns list-subscriptions"
    
fi



for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    if [[ "$1" == "" ]];then
        count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    fi
    echo $count

    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            if [[ "$1" == "" ]];then
                cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")
            elif [[ $cc == "6" ]];then 
                cname=$(echo $awsout | jq -r ".${idfilt[(${c})]}")
            else
                cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")
            fi
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_} && rname=${rname/${mysub}/}
            if [[ $cname == "null" ]];then
                echo "null cname exit ... cc=$cc"
                exit
            fi
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
            while IFS= read line
            do
				skip=0
                # display $line or do something with $line
                t1=`echo "$line"` 
                if [[ ${t1} == *"="* ]];then
                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                    tt2=`echo "$line" | cut -f2- -d'='`
                    if [[ ${tt1} == "arn" ]];then skip=1; fi                
                    if [[ ${tt1} == "id" ]];then 
                        skip=1; 
                        printf "lifecycle {\n" >> $fn
                        printf "   ignore_changes = [confirmation_timeout_in_minutes,endpoint_auto_confirms]\n" >> $fn
                        printf "}\n" >> $fn
                    fi  

                    if [[ ${tt1} == "role_arn" ]];then skip=1;fi
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    if [[ ${tt1} == "url" ]];then skip=1;fi
                    if [[ ${tt1} == "owner" ]];then skip=1;fi
                    if [[ ${tt1} == "confirmation_was_authenticated" ]];then skip=1;fi
                    if [[ ${tt1} == "pending_confirmation" ]];then skip=1;fi
                    if [[ ${tt1} == *":"* ]];then 
                        tt1=`echo $tt1 | tr -d '"'`
                        t1=`printf "\"%s\"=%s" $tt1 $tt2`
                    fi
                    if [[ ${tt1} == "topic_arn" ]];then 
                        tt2=$(echo $tt2 | tr -d '"')
                        if [[ "$tt2" == *":aws:sns:"* ]];then
                            tarn=$(echo $tt2)
                            rn=${tt2//:/_} && rn=${rn//./_} && rn=${rn//\//_} && rn=${rn/${mysub}/}
                            t1=`printf "%s = aws_sns_topic.%s.arn" $tt1 $rn`
                        fi
                    fi

                    if [[ ${tt1} == "endpoint" ]];then 
                        tt2=$(echo $tt2 | tr -d '"')
                        if [[ "$tt2" == *":aws:sqs:"* ]];then
                            qnam=$(echo $tt2 | rev | cut -f1 -d':' | rev)
                            rurl=$($AWS sqs get-queue-url --queue-name $qnam | jq -r ".QueueUrl")
                            rn=${rurl//:/_} && rn=${rn//./_} && rn=${rn//\//_}
                            t1=`printf "%s = aws_sqs_queue.%s.arn" $tt1 $rn`
                        fi
                    fi


                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"
            if [[ $tarn != "" ]];then
                echo "$ttft getting topic arn: $tarn"
                ../../scripts/730-get-sns-topic.sh $tarn
            fi
            
        done
    fi 
done

#rm -f t*.txt

