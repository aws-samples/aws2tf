#!/bin/bash
source ../../scripts/functions.sh
echo "mysub=$mysub"
ttft="aws_sns_topic_policy"

if [[ "$1" != "arn:"* ]]; then echo "must pass topic arn" && exit; fi
cname=$(echo $1 | rev | cut -f1 -d':' | rev)
rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
echo "$ttft ${cname}"

fn=$(printf "%s__%s.tf" $ttft $rname)
if [ -f "$fn" ]; then echo "$fn exists already skipping" && exit; fi

printf "resource \"%s\" \"%s\" {}\n" $ttft $rname >$fn
echo ${1}
terraform import $ttft.${rname} ${1}

terraform state show -no-color $ttft.${rname} >t1.txt
rm -f $fn
file="t1.txt"
echo $aws2tfmess >$fn
while IFS= read t1; do
    skip=0
    if [[ ${t1} == *"="* ]]; then
        tt1=$(echo "$t1" | cut -f1 -d'=' | tr -d ' ')
        tt2=$(echo "$t1" | cut -f2- -d'=')
        if [[ ${tt1} == "id" ]]; then skip=1; fi
        if [[ ${tt1} == "create_date" ]]; then skip=1; fi
        if [[ ${tt1} == "arn" ]]; then
            rsns=$(echo $tt2 | tr -d '"')
            # modified arn is used for sns topic terraform name account id is removed
            rrsns=${rsns//:/_} && rrsns=${rrsns//./_} && rrsns=${rrsns//\//_} && rrsns=${rrsns/${mysub}/}
            #mtopic=$(echo "$tt2" | rev | cut -f1 -d':' | rev)
            t1=$(printf "%s = aws_sns_topic.%s.arn" $tt1 $rrsns)

        fi
        if [[ ${tt1} == "Resource" ]]; then
            tt2=$(echo $tt2 | tr -d '"')
            if [[ "$tt2" == *"arn:aws:lambda:"* ]]; then
                tfn=$(echo "$tt2" | rev | cut -d':' -f1 | rev)
                t1=$(printf "%s = aws_lambda_function.%s.arn" $tt1 $tfn)
            #else
                #fixra "$tt1" "$tt2"
            fi
        fi

        if [[ ${tt1} == "owner" ]]; then skip=1; fi
        fixra "$tt1" "$tt2"
    fi

    if [ "$skip" == "0" ]; then echo "$t1" >>$fn; fi

done <"$file"
# dependancies here

#rm -f t*.txt
