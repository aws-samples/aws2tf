#!/bin/bash
mysub=$(echo $AWS2TF_ACCOUNT)
myreg=$(echo $AWS2TF_REGION)
pref[0]="Trails"
tft[0]="aws_cloudtrail"
idfilt[0]="Name"

cm="$AWS cloudtrail list-trails"

if [[ "$1" != "" ]]; then
    cm=$(printf "$AWS cloudtrail list-trails  | jq '.${pref}[] | select(.${idfilt}==\"%s\")' | jq ." $1)
fi

count=1
#echo $cm
awsout=$(eval $cm 2>/dev/null)

if [ "$awsout" == "" ]; then echo "$cm : You don't have access for this resource" && exit; fi
if [[ "$1" == "" ]]; then count=$(echo $awsout | jq ".${pref} | length"); fi
if [ "$count" -eq "0" ]; then echo "No resources found exiting .." && exit; fi
count=$(expr $count - 1)

c=0
region=$(echo $myreg)

ttft=${tft[(${c})]}

awsout=$(eval $cm 2>/dev/null)
#echo $awsout | jq .
if [ "$awsout" == "" ]; then
    echo "$cm : You don't have access for this resource"
    exit
fi

for i in $(seq 0 $count); do
    #echo $i
    if [[ "$1" != "" ]]; then
        regname=$(echo $awsout | jq -r ".HomeRegion")
    else
        regname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].HomeRegion")
    fi

    if [ "$region" == "$regname" ]; then
        #echo "in region"
        if [[ "$1" != "" ]]; then
            cname=$(echo $awsout | jq -r ".${idfilt}")
        else
            cname=$(echo $awsout | jq -r ".${pref}[(${i})].${idfilt}")
        fi

        fn=$(printf "%s__%s.tf" $ttft $rname)
        if [ -f "$fn" ]; then echo "$fn exists already skipping" && continue; fi

        echo "$ttft $cname"
        printf "resource \"%s\" \"%s\" {}\n" $ttft $cname > $fn
        terraform import $ttft.$cname "$cname" | grep Importing
        terraform state show -no-color $ttft.$cname >t1.txt
        rm -f $fn

        file="t1.txt"
        fn=$(printf "%s__%s.tf" $ttft $cname)
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
                if [[ ${tt1} == "home_region" ]]; then skip=1; fi
                if [[ ${tt1} == "s3_bucket_name" ]]; then
                    s3buck=$(echo $tt2 | tr -d '"')
                    t1=$(printf "%s = aws_s3_bucket.b_%s.bucket" $tt1 $s3buck)
                fi
                if [[ ${tt1} == "cloud_watch_logs_group_arn" ]]; then
                    cwarn=$(echo $tt2 | tr -d '"')
                    #echo $cwarn
                    rwarn=$(echo $cwarn | rev | cut -f2- -d':' | rev)
                    # save arn
                
                    sub="log-group:"
                    rest=${cwarn#*$sub}

                    cwnam=$(echo $rest | cut -f1 -d':')
                    rcwnam=${cwnam//:/_}
                    rcwnam=${rcwnam//./_}
                    rcwnam=${rcwnam//\//_}
                    cwt="aws_cloudwatch_log_group"
                    echo "$cwt,$rwarn,$rcwnam" >> data/arn-map.dat
                    skip=0
                    t1=`echo "$tt1 = format(\"%s:*\",aws_cloudwatch_log_group.$rcwnam.arn)"`
                fi

                if [[ ${tt1} == "cloud_watch_logs_role_arn" ]]; then
                    rarn=$(echo $tt2 | tr -d '"')
                    skip=0
                    trole=$(echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"')

                    t1=$(printf "%s = aws_iam_role.%s.arn" $tt1 $trole)
                fi
                if [[ ${tt1} == "kms_key_id" ]]; then
                    kid=$(echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"')
                    kmsarn=$(echo $tt2 | tr -d '"')
                    #echo $t1
                    t1=$(printf "%s = aws_kms_key.k_%s.arn" $tt1 $kid)
                fi

                if [[ ${tt1} == "equals" ]] || [[ ${tt1} == "ends_with" ]] || [[ ${tt1} == "not_ends_with" ]] || [[ ${tt1} == "not_equals" ]] || [[ ${tt1} == "not_starts_with" ]] || [[ ${tt1} == "starts_with" ]]; then
                    tt2=$(echo $tt2 | tr -d '"')
                    if [[ $tt2 == "[]" ]]; then
                        skip=1
                    fi
                fi

            fi
            if [ "$skip" == "0" ]; then
                #echo $skip $t1
                echo "$t1" >>$fn
            fi

        done <"$file"


        if [ "$cwnam" != "" ]; then
            echo "get log grp $cwnam"
            ../../scripts/070-get-cw-log-grp.sh "$cwnam"
        fi
        if [ "$trole" != "" ]; then
            ../../scripts/050-get-iam-roles.sh $trole
        fi
        if [ "$s3buck" != "" ]; then
            ../../scripts/060-get-s3.sh $s3buck
        fi

        if [ "$kmsarn" != "" ]; then
            ../../scripts/080-get-kms-key.sh $kmsarn
        fi


    fi
done

rm -f t*.txt
