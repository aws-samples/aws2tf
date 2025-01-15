#!/bin/bash
source ../../scripts/functions.sh
if [[ "$1" != "" ]]; then
    pref=$(echo $1 | rev | cut -f1 -d'/' | rev)
    cmd[0]="$AWS sqs list-queues --queue-name-prefix $pref"

else
    cmd[0]="$AWS sqs list-queues"
fi

pref[0]="QueueUrls"
tft[0]="aws_sqs_queue"
idfilt[0]=""

for c in $(seq 0 0); do

    cm=${cmd[$c]}
    ttft=${tft[(${c})]}
    #echo $cm
    awsout=$(eval $cm 2>/dev/null)
    if [ "$awsout" == "" ]; then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    if [[ "$1" != "" ]]; then
        count=1
    else
        count=$(echo $awsout | jq ".${pref[(${c})]} | length")
    fi
    if [ "$count" -gt "0" ]; then
        count=$(expr $count - 1)
        for i in $(seq 0 $count); do
            #echo $i
            cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})]")
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            echo "$ttft $cname"
            fn=$(printf "%s__%s.tf" $ttft $rname)
            if [ -f "$fn" ]; then echo "$fn exists already skipping" && continue; fi

            printf "resource \"%s\" \"%s\" {}\n" $ttft $rname >$fn

            terraform import $ttft.${rname} "${cname}" | grep Importing
            terraform state show -no-color $ttft.${rname} >t1.txt

            rm -f $fn

            file="t1.txt"
            echo $aws2tfmess >$fn
            tarn=""
            while IFS= read line; do
                skip=0
                # display $line or do something with $line
                t1=$(echo "$line")
                if [[ ${t1} == *"="* ]]; then
                    tt1=$(echo "$line" | cut -f1 -d'=' | tr -d ' ')
                    tt2=$(echo "$line" | cut -f2- -d'=')
                    if [[ ${tt1} == "arn" ]]; then skip=1; fi
                    if [[ ${tt1} == "id" ]]; then skip=1; fi
                    if [[ ${tt1} == "role_arn" ]]; then skip=1; fi
                    if [[ ${tt1} == "owner_id" ]]; then skip=1; fi
                    if [[ ${tt1} == "url" ]]; then
                        skip=1
                        tt2=$(echo $tt2 | tr -d '"')
                        qurl=${tt2//:/_} && rn=${rn//./_} && rn=${rn//\//_}
                    fi

                    if [[ ${tt1} == "sqs_managed_sse_enabled" ]]; then
                        tt2=$(echo $tt2 | tr -d '"')
                        if [[ $tt2 == "false" ]]; then
                            skip=1
                        fi
                    fi

                    if [[ ${tt1} == "deadLetterTargetArn" ]]; then
                        tt2=$(echo $tt2 | tr -d '"')
                        if [[ "$tt2" == *":aws:sqs:"* ]]; then
                            qnam=$(echo $tt2 | rev | cut -f1 -d':' | rev)
                            rurl=$($AWS sqs get-queue-url --queue-name $qnam | jq -r ".QueueUrl")
                            rn=${rurl//:/_} && rn=${rn//./_} && rn=${rn//\//_}

                            if [[ "$rurl" != "$cname" ]]; then ## to stop - Error: Self-referential block
                                t1=$(printf "%s = aws_sqs_queue.%s.arn" $tt1 $rn)
                            fi
                        fi
                    fi

                    if [[ ${tt1} == "kms_master_key_id" ]]; then

                        keyid=$(echo $tt2 | tr -d '"')
                        if [[ $keyid == *":"* ]]; then
                            keyid=$(echo $keyid | rev | cut -f1 -d'/' | rev)
                        fi
                        # quick check it exists

                        $AWS kms describe-key --key-id $keyid &>/dev/null
                        if [[ $? -eq 0 ]]; then
                            t1=$(printf "%s = aws_kms_key.k_%s.id" $tt1 $keyid)
                        else
                            t1=$(printf "# COMMENT THIS KEY DOESN'T EXIST %s = aws_kms_key.k_%s.id" $tt1 $keyid)
                            keyid=""
                        fi
                    fi

                    if [[ ${tt1} == *":"* ]]; then

                        tt2=$(echo $tt2 | tr -d '"')
                        #echo "-1->> $tt1 $tt2"
                        if [[ ${tt1} == *"aws:SourceArn"* ]]; then
                            #echo "-2->> $tt2"
                            if [[ ${tt2} == *":aws:sns:"* ]]; then
                                tarn=$(echo $tt2)
                                #echo "-3->> $tarn"
                                #rn=${tt2//:/_} && rn=${rn//./_} && rn=${rn//\//_}
                                rn=${tt2//:/_} && rn=${rn//./_} && rn=${rn//\//_} && rn=${rn/${mysub}/}
                                t1=$(printf "%s = aws_sns_topic.%s.arn" $tt1 $rn)
                            else
                                tt1=$(echo $tt1 | tr -d '"')
                                t1=$(printf "\"%s\"=\"%s\"" $tt1 $tt2)
                            fi
                        else
                            tt1=$(echo $tt1 | tr -d '"')
                            t1=$(printf "\"%s\"=%s" $tt1 $tt2)
                        fi
                    fi
                    if [[ ${tt1} == "Resource" ]]; then
                        tt2=$(echo $tt2 | tr -d '"')
                        if [[ "$tt2" == *":aws:sqs:"* ]]; then
                            qnam=$(echo $tt2 | rev | cut -f1 -d':' | rev)
                            rurl=$($AWS sqs get-queue-url --queue-name $qnam | jq -r ".QueueUrl")
                            rn=${rurl//:/_} && rn=${rn//./_} && rn=${rn//\//_}
                            echo "In Resource cname=$cname rurl=$rurl"

                            if [[ "$rurl" != "$cname" ]]; then ## to stop - Error: Self-referential block
                                t1=$(printf "%s = aws_sqs_queue.%s.arn" $tt1 $rn)
                            fi
                        elif [[ "$tt2" == *":aws:sns:"* ]]; then
                            tarn2=$(echo $tt2)
                            rn=${tt2//:/_} && rn=${rn//./_} && rn=${rn//\//_}
                            if [[ "$tarn2" != "$cname" ]]; then ## to stop - Error: Self-referential block
                                t1=$(printf "%s = aws_sns_topic.%s.arn" $tt1 $rn)
                            fi
                        #else
                            #fixra "$tt1" "$tt2"
                        fi
                    fi
                    fixra "$tt1" "$tt2"
                fi

                #fixarn "$tt2" - as it breaks self referenntial block
                if [ "$skip" == "0" ]; then wtf "$t1" "$fn"; fi

            done <"$file"

            if [[ $tarn != "" ]]; then
                #echo "-4- >> $tarn"
                ../../scripts/730-get-sns-topic.sh $tarn
            fi
            if [[ $tarn2 != "" ]]; then
                #echo "-5- >> $tarn2"
                ../../scripts/730-get-sns-topic.sh $tarn2
            fi
        done
    fi
done

#rm -f t*.txt
