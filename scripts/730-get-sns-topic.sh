#!/bin/bash
source ../../scripts/functions.sh
#echo "globals = $mysub $myreg"
if [[ "$1" != "" ]]; then
    if [[ "$1" == "arn:"* ]];then 
        cmd[0]="$AWS sns get-topic-attributes --topic-arn $1"
        pref[0]="Attributes"
    else
        echo "you must pass an arn for the parameter"
        exit
    fi

else
    cmd[0]="$AWS sns list-topics"
    pref[0]="Topics"
fi

tft[0]="aws_sns_topic"
idfilt[0]="TopicArn"

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
            if [[ $1 != "" ]]; then
                cname=$(echo $awsout | jq -r ".${pref[(${c})]}.${idfilt[(${c})]}")
            else
                cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")
            fi
            if [[ "$cname" == "null" ]]; then "echo topic = $cname skipping..." && continue; fi

            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_} && rname=${rname/${mysub}/}

            echo "$ttft $cname"
            echo "$ttft,$cname,$rname" >>data/arn-map.dat
            fn=$(printf "%s__%s.tf" $ttft $rname)
            if [ -f "$fn" ]; then echo "$fn exists already skipping" && continue; fi

            printf "resource \"%s\" \"%s\" {}\n" $ttft $rname >$fn

            terraform import $ttft.${rname} "${cname}" | grep Importing
            terraform state show -no-color $ttft.${rname} >t1.txt

            rm -f $fn

            tarn=""
            file="t1.txt"
            echo $aws2tfmess >$fn
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
                    if [[ ${tt1} == "url" ]]; then skip=1; fi
                    if [[ ${tt1} == "owner" ]]; then skip=1; fi
                    if [[ ${tt1} == *":"* ]]; then
                        tt1=$(echo $tt1 | tr -d '"')
                        t1=$(printf "\"%s\"=%s" $tt1 $tt2)
                        #echo "**** T1=$t1"
                    fi

                    if [[ ${tt1} == "signature_version" ]]; then
                        tt2=$(echo $tt2 | tr -d '"')
                        if [[ $tt2 == "0" ]]; then
                            skip=1
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

                    ## commented to stop - Error: Self-referential block

                    if [[ ${tt1} == "Resource" ]]; then
                        tt2=$(echo $tt2 | tr -d '"')
                        if [[ "$tt2" == *":aws:sns:"* ]]; then
                            tarn=$(echo $tt2)
                            rn=${tt2//:/_} && rn=${rn//./_} && rn=${rn//\//_}
                            if [[ "$tarn" != "$cname" ]]; then ## to stop - Error: Self-referential block
                                t1=$(printf "%s = aws_sns_topic.%s.arn" $tt1 $rn)
                            fi
                            #else
                            #fixra "$tt1" "$tt2"
                        
                        # Causes cycle issues
                        #
                        #elif [[ "$tt2" == *"arn:aws:lambda:"* ]]; then
                        #    tfn=$(echo "$tt2" | rev | cut -d':' -f1 | rev)
                        #    t1=$(printf "%s = aws_lambda_function.%s.arn" $tt1 $tfn)
                        #    #else
                            #fixra "$tt1" "$tt2"
                        fi

                    fi

                    if [[ ${tt1} == "AWS" ]]; then
                        tt2=$(echo $tt2 | tr -d '"')
                        if [[ "$tt2" == "arn:aws:iam::${mysub}:root" ]]; then
                            tsub="%s"
                            t1=$(printf "%s = format(\"arn:aws:iam::%s:root\",data.aws_caller_identity.current.account_id)" $tt1 $tsub)
                        fi
                    fi
                    fixra "$tt1" "$tt2"

                fi # end if =

                if [ "$skip" == "0" ]; then wtf "$t1" "$fn"; fi

            done <"$file"

            ../../scripts/731-get-sns-subscriptions.sh $cname
            if [[ "$tarn" != "" ]]; then
              #echo $tarn
                ../../scripts/731-get-sns-subscriptions.sh $tarn
            fi

        done
    fi
done
#cat aws_sns_topic__*.tf
rm -f t*.txt
