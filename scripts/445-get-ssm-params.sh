#!/bin/bash
mysub=$(echo $AWS2TF_ACCOUNT)
myreg=$(echo $AWS2TF_REGION)
if [ "$1" != "" ]; then
    cmd[0]="$AWS ssm describe-parameters  --filters Key=Name,Values=$1"
else
    cmd[0]="$AWS ssm describe-parameters"
fi

tft[0]="aws_ssm_parameter"
idfilt[0]="Name"
pref[0]="Parameters"

#rm -f ${tft[0]}.tf

for c in $(seq 0 0); do

    cm=${cmd[$c]}
    ttft=${tft[(${c})]}
    #echo $cm
    awsout=$(eval $cm 2>/dev/null)
    if [ "$awsout" == "" ]; then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    #echo $awsout | jq .
    if [ "$1" != "" ]; then
        count=1
    else
        count=$(echo $awsout | jq ".${pref[(${c})]} | length")
    fi
    if [ "$count" -gt "0" ]; then
        count=$(expr $count - 1)
        for i in $(seq 0 $count); do
            #echo $i

            cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")
            tv=$($AWS ssm get-parameter --name $cname --query Parameter.Value)
            if [[ "$tv" == *"{"* ]]; then
                echo "control chr { in value for $cname skipping ..."
                continue
            fi

            echo "$ttft $cname"
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}

            fn=$(printf "%s__%s.tf" $ttft $rname)
            if [ -f "$fn" ]; then
                echo "$fn exists already skipping"
                continue
            fi
            printf "resource \"%s\" \"%s\" {" $ttft $rname >$ttft.$rname.tf
            printf "}" >>$ttft.$rname.tf
            printf "terraform import %s.%s %s" $ttft $rname $cname >data/import_$ttft_$rname.sh
            terraform import $ttft.$rname "$cname" | grep Importing
            terraform state show -no-color $ttft.$rname >t1.txt
            tfa=$(printf "%s.%s" $ttft $rname)
            terraform show -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' >data/$tfa.json
            #echo $awsj | jq .
            rm $ttft.$rname.tf

            file="t1.txt"
            echo $aws2tfmess >$fn
            sgs=()
            subnets=()
            while IFS= read line; do
                skip=0
                # display $line or do something with $line
                t1=$(echo "$line")
                if [[ ${t1} == *"="* ]]; then
                    tt1=$(echo "$line" | cut -f1 -d'=' | tr -d ' ')
                    tt2=$(echo "$line" | cut -f2- -d'=')
                    if [[ ${tt1} == "arn" ]]; then skip=1; fi
                    if [[ ${tt1} == "id" ]]; then skip=1; fi
                    if [[ ${tt1} == "latest_version" ]]; then skip=1; fi
                    if [[ ${tt1} == "owner" ]]; then skip=1; fi
                    if [[ ${tt1} == "version" ]]; then skip=1; fi
                    if [[ ${tt1} == "value" ]]; then
                        tv=$($AWS ssm get-parameter --name $cname --query Parameter.Value)
                        tt2=$(echo $tv | tr -d '"')
                        tstart=$(echo ${tt2:0:8})
                        #echo $tstart
                        if [[ "$tstart" == "arn:aws:" ]]; then
                            tstart=$(echo $tt2 | cut -f1-3 -d ':')
                            treg=$(echo $tt2 | cut -f4 -d ':')
                            tacc=$(echo $tt2 | cut -f5 -d ':')
                            tend=$(echo $tt2 | cut -f6- -d ':')
                            tsub="%s"
                            if [[ "$treg" != "" ]] || [[ "$tacc" != "" ]]; then
                                if [[ "$mysub" == "$tacc" ]]; then
                                    if [[ "$treg" != "" ]]; then
                                        t1=$(printf "%s = format(\"%s:%s:%s:%s*\",data.aws_region.current.name,data.aws_caller_identity.current.account_id)" $tt1 $tstart $tsub $tsub $tend)
                                    else
                                        t1=$(printf "%s = format(\"%s::%s:%s*\",data.aws_caller_identity.current.account_id)" $tt1 $tstart $tsub $tend)
                                    fi
                                fi
                            fi
                        fi

                        t1=$(printf "%s = %s" $tt1 "$tv")
                        printf "lifecycle {\n" >>$fn
                        printf "   ignore_changes = [value]\n" >>$fn
                        printf "}\n" >>$fn
                    fi

                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >>$fn
                fi

            done <"$file"

        done

    fi
done

rm -f t*.txt
