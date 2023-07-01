#!/bin/bash
mysub=$(echo $AWS2TF_ACCOUNT)
myreg=$(echo $AWS2TF_REGION)

function wtf {
    t1="$1"
    fn="$2"
    at1=$(echo $t1 | tr -d ' |"')
    #echo "at1=$at1"
    if [[ "$at1" == "arn:aws:"* ]]; then
        tstart=$(echo $at1 | cut -f1-3 -d ':')
        treg=$(echo $at1 | cut -f4 -d ':')
        tacc=$(echo $at1 | cut -f5 -d ':')
        tend=$(echo $at1 | cut -f6- -d ':')
        tsub="%s"
        tcomm=","

        if [[ "$treg" != "" ]] || [[ "$tacc" != "" ]]; then
            
            if [[ "$tend" == *"," ]]; then
                #echo "tend1=$tend"
                tend=$(echo ${tend%?})
                #echo "tend2=$tend"
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
}

