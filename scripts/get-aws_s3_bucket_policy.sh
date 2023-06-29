#!/bin/bash
mysub=$(echo $AWS2TF_ACCOUNT)
myreg=$(echo $AWS2TF_REGION)
if [ "$1" == "" ]; then echo "must specify bucket name" && exit; fi
c=0
tft[0]="aws_s3_bucket_policy"
ttft=${tft[(${c})]}

#echo $i
cname=$(echo $1)
rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
rname=$(printf "b_%s" $rname)
#echo "$ttft $rname"

fn=$(printf "%s__%s.tf" $ttft $rname)
if [ -f "$fn" ]; then echo "$fn exists already skipping" && exit; fi

#echo "$ttft $cname $rname state get ..."
../../scripts/parallel_import3.sh $ttft ${cname} $rname "user=${1}"
#echo "$ttft $rname move"
#../../scripts/parallel_statemv.sh $ttft
file=$(printf "%s-%s-1.txt" $ttft $rname)

while IFS= read t1; do

    skip=0
    # display $line or do something with $line
    if [[ "$t1" == "}" ]]; then
        if [[ "$dopol" == "1" ]]; then
            echo 'policy = ""' >>$fn
        fi
    fi
    if [[ ${t1} == *"="* ]]; then
        tt1=$(echo "$t1" | cut -f1 -d'=' | tr -d ' ')
        tt2=$(echo "$t1" | cut -f2- -d'=')
        if [[ ${tt1} == "arn" ]]; then skip=1; fi

        if [[ ${tt1} == "bucket" ]]; then
            tt1=$(echo $tt1 | tr -d '"')
            bn=$(echo $tt2 | tr -d '"')
            t1=$(printf "%s=aws_s3_bucket.b_%s.id" $tt1 $bn)
        fi

        if [[ ${tt1} == "id" ]]; then
            idv=$(echo $tt2 | tr -d '"')
            if [[ "$idv" == "$bn" ]]; then
                skip=1
            fi
        fi

        if [[ ${tt1} == "role_arn" ]]; then skip=1; fi
        if [[ ${tt1} == "owner_id" ]]; then skip=1; fi
        if [[ ${tt1} == "resource_owner" ]]; then skip=1; fi
        if [[ ${tt1} == "creation_date" ]]; then skip=1; fi
        if [[ ${tt1} == "rotation_enabled" ]]; then skip=1; fi

        if [[ ${tt1} == "policy" ]]; then
            dopol=0
        fi

        if [[ ${tt1} == *":"* ]]; then
            tt1=$(echo $tt1 | tr -d '"')
            tt2=$(echo $tt2 | tr -d '"')
            if [[ "$tt2" != " $myreg" ]]; then
                t1=$(printf "\"%s\"=%s" $tt1 $tt2)
            else
                t1=$(printf "\"%s\" = data.aws_caller_identity.current.account_id" $tt1)
            fi

        fi

    fi
    if [ "$skip" == "0" ]; then
        #echo $skip $t1
        echo "$t1" >>$fn
    fi
done <"$file"
