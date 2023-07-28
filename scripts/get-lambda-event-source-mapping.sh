#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS lambda list-event-source-mappings --function-name $1"

else
    echo "must supply a finction name"
    exit
fi

source ../../scripts/functions.sh

pref[0]="EventSourceMappings"
tft[0]="aws_lambda_event_source_mapping"
idfilt[0]="UUID"

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
            cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")

            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_} && rname=${rname//$/_}
            echo "$ttft $cname"
            fn=$(printf "%s__l-%s.tf" $ttft $rname)
            if [ -f "$fn" ]; then echo "$fn exists already skipping" && continue; fi

            printf "resource \"%s\" \"l-%s\" {" $ttft $rname >$fn
            printf "}" >>$fn

            terraform import $ttft.l-${rname} "${cname}" | grep Importing
            terraform state show -no-color $ttft.l-${rname} >t1.txt

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

                    if [[ ${tt1} == "id" ]]; then skip=1; fi
                    if [[ ${tt1} == "arn" ]]; then skip=1; fi
                    if [[ ${tt1} == "creation_date" ]]; then skip=1; fi
                    if [[ ${tt1} == "last_modified_date" ]]; then skip=1; fi
                    if [[ ${tt1} == "endpoint" ]]; then skip=1; fi
                    if [[ ${tt1} == "estimated_number_of_users" ]]; then skip=1; fi
                    if [[ ${tt1} == "function_arn" ]]; then skip=1; fi
                    if [[ ${tt1} == "last_modified" ]]; then skip=1; fi
                    if [[ ${tt1} == "state" ]]; then skip=1; fi
                    if [[ ${tt1} == "state_transition_reason" ]]; then skip=1; fi
                    if [[ ${tt1} == "uuid" ]]; then skip=1; fi
                    if [[ ${tt1} == "last_modified" ]]; then skip=1; fi

                    if [[ ${tt1} == "maximum_record_age_in_seconds" ]]; then
                        tt2=$(echo $tt2 | tr -d '"')
                        if [[ $tt2 == "0" ]]; then skip=1; fi
                    fi
                    if [[ ${tt1} == "parallelization_factor" ]]; then
                        tt2=$(echo $tt2 | tr -d '"')
                        if [[ $tt2 == "0" ]]; then skip=1; fi
                    fi
                fixarn "$tt2"
                fi

                
                if [ "$skip" == "0" ]; then wtf "$t1" "$fn"; fi
                #if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                #    echo "$t1" >>$fn
                #fi

            done <"$file"
        done
    fi
done

#rm -f t*.txt
