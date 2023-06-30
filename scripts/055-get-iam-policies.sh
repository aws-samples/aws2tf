#!/bin/bash
mysub=$(echo $AWS2TF_ACCOUNT)
myreg=$(echo $AWS2TF_REGION)
if [ "$1" != "" ]; then
    if [[ "$1" == *"arn:"* ]]; then
        if [[ "$1" != *":aws:policy"* ]]; then
            cmd[0]="$AWS iam get-policy --policy-arn $1"
            pref[0]="Policy"
        else
            echo "skipping AWS managed policy $1"
            exit
        fi
    else
        echo "must pass an arn as a parameter"
        exit
    fi
else
    cmd[0]="$AWS iam list-policies --scope Local"
    pref[0]="Policies"
fi

tft[0]="aws_iam_policy"
getp=0
for c in $(seq 0 0); do

    cm=${cmd[$c]}
    ttft=${tft[(${c})]}
    #echo $cm
    awsout=$(eval $cm 2>/dev/null)
    if [ "$awsout" == "" ]; then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    count=$(echo $awsout | jq ".${pref[(${c})]} | length")
    if [ "$count" -gt "0" ]; then
        count=$(expr $count - 1)
        for i in $(seq 0 $count); do
            #echo $i
            # is it AWS Managed ?
            awsm=""

            if [ "$1" != "" ]; then
                pname=$(echo $awsout | jq -r ".${pref[(${c})]}.PolicyName")
                cname=$(echo $awsout | jq ".${pref[(${c})]}.Arn" | tr -d '"')
            else
                pname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].PolicyName")
                cname=$(echo $awsout | jq ".${pref[(${c})]}[(${i})].Arn" | tr -d '"')
            fi

            ocname=$(echo $cname)
            cname=$(echo $cname | rev | cut -f1 -d'/' | rev)

            if [ "$1" != "" ]; then

                getp=0
                if [ $cname == $1 ]; then
                    getp=1
                fi
            else
                #echo "not set"
                getp=1
            fi
            if [ "$getp" == "1" ]; then
                fn=$(printf "%s__p_%s.tf" $ttft $cname)
                if [ -f "$fn" ]; then
                    echo "$fn exists already skipping"
                    continue
                fi

                echo "$ttft $cname"
                echo "aws_iam_policy,$ocname,$cname" >>data/arn-map.dat
                printf "resource \"%s\" \"p_%s\" {}\n" $ttft $cname >$fn
                terraform import $ttft.p_$cname $ocname | grep Importing
                terraform state show -no-color $ttft.p_$cname >t1.txt
                rm -f $fn

                file="t1.txt"
                echo $aws2tfmess >$fn
                echo "# $0" >>$fn
                while IFS= read line; do
                    skip=0
                    # display $line or do something with $line
                    t1=$(echo "$line")
                    if [[ ${t1} == *"="* ]]; then
                        tt1=$(echo "$line" | cut -f1 -d'=' | tr -d ' ')
                        tt2=$(echo "$line" | cut -f2- -d'=')
                        if [[ ${tt1} == *":"* ]]; then
                            # check tt2 for $
                            tt2=${tt2//$/&}
                            tt1=$(echo $tt1 | tr -d '"')
                            t1=$(printf "\"%s\"=%s" $tt1 "$tt2")
                        fi
                        if [[ ${tt1} == "Resource" ]]; then
                            tt2=${tt2//$/&}
                            tt1=$(echo $tt1 | tr -d '"')
                            t1=$(printf "\"%s\"=%s" $tt1 "$tt2")
                        fi

                        if [[ ${tt1} == "arn" ]]; then skip=1; fi
                        if [[ ${tt1} == "id" ]]; then skip=1; fi
                        if [[ ${tt1} == "policy_id" ]]; then skip=1; fi
                        if [[ ${tt1} == "role_arn" ]]; then skip=1; fi
                    else

                        if [[ $t1 == *"\${"* ]]; then
                            t1=${t1//$/&}
                        fi

                    fi

                    if [ "$skip" == "0" ]; then
                        #echo $skip $t1

                        at1=$(echo $t1 | tr -d ' |"')
                        if [[ "$at1" == "arn:aws:"* ]]; then
                            tstart=$(echo $at1 | cut -f1-3 -d ':')
                            treg=$(echo $at1 | cut -f4 -d ':')
                            tacc=$(echo $at1 | cut -f5 -d ':')
                            tend=$(echo $at1 | cut -f6- -d ':')
                            tsub="%s"
                            tcomm=","
                            if [[ "$treg" != "" ]] !! [[ "$tacc" != "" ]]; then
                                if [[ "$tend" == *"," ]]; then
                                    tend=$(echo ${tend:0:-1})
                                fi
                                if [[ "$mysub" == "$tacc" ]]; then
                                    if [[ "$treg" != "" ]]; then
                                        t1=$(printf "format(\"%s:%s:%s:%s\",data.aws_region.current.name,data.aws_caller_identity.current.account_id)," $tstart $tsub $tsub "$tend")
                                    else
                                        t1=$(printf "format(\"%s::%s:%s\",data.aws_caller_identity.current.account_id)," $tstart $tsub "$tend")

                                    fi
                                fi
                            fi

                        fi

                        echo "$t1" >>$fn
                    fi

                done <"$file" # done while
            fi
        done # done for i
    fi
done

rm -f t*.txt
