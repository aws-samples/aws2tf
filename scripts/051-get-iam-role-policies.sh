#!/bin/bash
mysub=$(echo $AWS2TF_ACCOUNT)
myreg=$(echo $AWS2TF_REGION)
#echo "globals = $mysub $myreg"
if [ "$1" != "" ]; then
    cmd[0]="$AWS iam list-role-policies --role-name $1"
else
    exit
fi
c=0
cm=${cmd[$c]}

pref[0]="PolicyNames"
tft[0]="aws_iam_role_policy"

for c in $(seq 0 0); do

    cm=${cmd[$c]}
    ttft=${tft[(${c})]}
    #echo $cm
    awsout=$(eval $cm 2>/dev/null)
    if [ "$awsout" == "" ]; then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    #echo "awsout $awsout"

    count=$(echo $awsout | jq ".${pref[(${c})]} | length")
    if [ "$count" -gt "0" ]; then
        count=$(expr $count - 1)
        #echo $count
        for i in $(seq 0 $count); do
            pname=$(echo $awsout | jq ".${pref[(${c})]}[(${i})]" | tr -d '"')
            awsout2=$($AWS iam get-role-policy --role-name ${1} --policy-name ${pname})
            cname=$(echo $awsout2 | jq ".PolicyName" | tr -d '"')
            ocname=$(echo $cname)
            cname=${cname//./_}
            cname=$(printf "%s__%s" $1 $cname)
            fn=$(printf "%s__%s.tf" $ttft $cname)
            if [ -f "$fn" ]; then
                echo "$fn exists already skipping"
                continue
            fi

            echo "$ttft $cname"

            printf "resource \"%s\" \"%s\" {}\n" $ttft $cname >$fn
            terraform import $ttft.$cname $1:$pname | grep Importing
            terraform state show -no-color $ttft.$cname >t1.txt
            rm -f $fn

            file="t1.txt"
            echo $aws2tfmess >$fn
            tl=()
            while IFS= read line; do
                skip=0
                # display $line or do something with $line
                t1=$(echo "$line")
                if [[ ${t1} == *"="* ]]; then
                    tt1=$(echo "$line" | cut -f1 -d'=' | tr -d ' ')
                    tt2=$(echo "$line" | cut -f2- -d'=')
                    if [[ ${tt1} == *":"* ]]; then
                        tt1=$(echo $tt1 | tr -d '"')
                        t1=$(printf "\"%s\"=%s" $tt1 $tt2)
                    fi
                    if [[ ${tt1} == "arn" ]]; then skip=1; fi
                    if [[ ${tt1} == "id" ]]; then skip=1; fi
                    if [[ ${tt1} == "role_arn" ]]; then skip=1; fi
                    if [[ ${tt1} == "role" ]]; then
                        tsel=$(echo $tt2 | tr -d '"')
                        t1=$(printf "%s = aws_iam_role.%s.id" $tt1 $tsel)
                        skip=0
                    fi
                    if [[ ${tt1} == "owner_id" ]]; then skip=1; fi
                    if [[ ${tt1} == "association_id" ]]; then skip=1; fi
                    if [[ ${tt1} == "unique_id" ]]; then skip=1; fi
                    if [[ ${tt1} == "create_date" ]]; then skip=1; fi
                    #if [[ ${tt1} == "public_ip" ]];then skip=1;fi
                    if [[ ${tt1} == "private_ip" ]]; then skip=1; fi
                    if [[ ${tt1} == "accept_status" ]]; then skip=1; fi

                    if [[ ${tt1} == "Resource" ]]; then
                        tt2=$(echo $tt2 | tr -d '"| ')
                        if [[ "$tt2" != "*" ]]; then

                            if [[ "$tt2" == *"["* ]]; then
                                t1=$(echo $t1)
                            elif [[ "$tt2" == *"${mysub}:role/"* ]]; then
                                #echo "in role/ match"
                                if [[ "$tt2" != *"${mysub}:role/aws-service-role"* ]]; then

                                    rarn=$(echo $tt2 | tr -d '"')
                                    trole=$(echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"')

                                    if [[ $trole != $cname ]]; then
                                        t1=$(printf "%s = aws_iam_role.%s.arn" $tt1 $trole)
                                    fi
                                fi
                            elif [[ "$tt2" == "arn:aws:sns:${myreg}:${mysub}:"* ]]; then

                                rsns=$(echo $tt2 | tr -d '"')
                                #echo $rsns
                                tl+=$(printf "\"%s\" " $rsns)
                                trole=${rsns//:/_} && trole=${trole//./_} && trole=${trole//\//_} && trole=${trole/${mysub}/}

                                t1=$(printf "%s = aws_sns_topic.%s.arn" $tt1 $trole)
                            elif [[ "$tt2" == *"arn:aws:dynamodb:${myreg}:${mysub}:table/"* ]]; then
                                rdyn=$(echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"')
                                t1=$(printf "%s = aws_dynamodb_table.%s.arn" $tt1 $rdyn)
                                echo "aws_dynamodb_table,$tt2,$rdyn" >> data/arn-map.dat
                            elif [[ "$tt2" == *"arn:aws:kms:${myreg}:${mysub}:key/"* ]]; then
                                kid=$(echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"')
                                t1=$(printf "%s = aws_kms_key.k_%s.arn" $tt1 $kid)
                            elif [[ "$tt2" == *"arn:aws:s3:::"* ]]; then
                                s3arn=$(echo $tt2)
                                if [[ "$tt2" != *"/"* ]]; then
                                    s3id=$(echo $tt2 | rev | cut -f1 -d':' | rev | tr -d '"')
                                    echo "aws_s3_bucket,$s3arn,$s3id" >> data/arn-map.dat
                                    echo "**> s3id=$s3id"
                                    if [[ $s3id == "*" ]];then
                                        t1=$(printf "%s = \"arn:aws:s3:::*\"" $tt1)
                                    else
                                        t1=$(printf "%s = aws_s3_bucket.b_%s.arn" $tt1 $s3id)
                                    fi
                                fi
                            elif [[ "$tt2" == *"arn:aws:ecr:${myreg}:${mysub}:repository/"* ]]; then
                                rep=$(echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"')
                                #reps+=`printf "\"%s\" " $rep`
                                t1=$(printf "%s = aws_ecr_repository.%s.arn" $tt1 $rep)
                            elif [[ "$tt2" == *"arn:aws:codecommit:${myreg}:${mysub}:"* ]]; then
                                ccid=$(echo $tt2 | rev | cut -f1 -d':' | rev | tr -d '"')
                                t1=$(printf "%s = aws_codecommit_repository.%s.arn" $tt1 $ccid)

                            elif [[ "$tt2" == *"arn:aws:codepipeline:${myreg}:${mysub}:"* ]]; then
                                cpid=$(echo $tt2 | rev | cut -f1 -d':' | rev | tr -d '"')
                                t1=$(printf "%s = aws_codepipeline.r-%s.arn" $tt1 $cpid)

                            elif [[ "$tt2" == *"arn:aws:codebuild:${myreg}:${mysub}:project/"* ]]; then
                                cbid=$(echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"')
                                t1=$(printf "%s = aws_codebuild_project.%s.arn" $tt1 $cbid)

                            else # check tt2 for $
                                tt2=${tt2//$/&}
                                if [[ "$tt2" != "[" ]]; then
                                    t1=$(printf "%s=\"%s\"" $tt1 "$tt2")
                                else
                                    t1=$(printf "%s=%s" $tt1 "$tt2")
                                fi
                            fi
                        fi
                    fi
                fi
                if [ "$skip" == "0" ]; then echo "$t1" >>$fn; fi

            done <"$file" # done while
            if [[ $s3id != "" ]]; then
                ../../scripts/060-get-s3.sh $s3id
            fi

            #echo "--> TOPIC $tl"
            for topic in ${tl[@]}; do
                topic=$(echo $topic | tr -d '"')
                #echo "***** calling for $topic"
                if [[ "$topic" != "" ]]; then
                    ../../scripts/730-get-sns-topic.sh $topic
                fi

            done

        done # done for i
    fi
done # done for

rm -f t*.txt
