#!/bin/bash
mysub=$(echo $AWS2TF_ACCOUNT)
myreg=$(echo $AWS2TF_REGION)
ncpu=$(getconf _NPROCESSORS_ONLN)
ncpu=$(expr $ncpu - 1)
c=0
#echo "functions ....."

function wtf {
    t1="$1"
    fn="$2"
    at1=$(echo $t1 | tr -d ' |"')
    #echo "raw t1=$t1"
    #echo "raw at1 = $at1"

    if [[ "$at1" == "arn:aws:"* ]]; then
        tstart=$(echo $at1 | cut -f1-3 -d ':' | tr -d '"')
        treg=$(echo $at1 | cut -f4 -d ':')
        tacc=$(echo $at1 | cut -f5 -d ':')
        tend=$(echo $at1 | cut -f6- -d ':' | tr -d '"')
        tsub="%s"
        tcomm=","
        #echo "at1 is arn  at1=$at1 tstart=$tstart tend=$tend"

        if [[ "$treg" != "" ]] || [[ "$tacc" != "" ]]; then

            if [[ "$tend" == *"," ]]; then
                #echo "tend1=$tend"
                tend=$(echo ${tend%?})
                #echo "tend2=$tend"
            fi
            #echo "pre sub at1=$at1 tstart=$tstart tend=$tend"
            if [[ "$mysub" == "$tacc" ]]; then
                if [[ "$treg" != "" ]]; then
                    t1=$(printf "format(\"%s:%s:%s:%s\",data.aws_region.current.name,data.aws_caller_identity.current.account_id)," $tstart $tsub $tsub "$tend")
                else
                    t1=$(printf "format(\"%s::%s:%s\",data.aws_caller_identity.current.account_id)," $tstart $tsub "$tend")

                fi
            fi
        fi

    fi
    if [[ $t1 == *"\"\""* ]]; then
        echo "wtf t1=$t1"
    fi
    echo "$t1" >>$fn
}

function fixarn {
    isstar=0
    isslash=0
    tsub="%s"
    tt2=$(echo $1 | tr -d ' |"')
    ot1=$(echo $t1)
    if [[ $tt2 == *"*"* ]]; then isstar=1; fi
    if [[ $tt2 == *"/"* ]]; then isslash=1; fi
    #echo "fixarn tt2=$tt2 myreg=$myreg"
    #if is arn change
    if [[ "$tt2" == *"arn:aws:"*":$myreg:$mysub:"* ]]; then
        tt2=$(echo $1 | tr -d ' |"')
        #echo $tt2
        tstart=$(echo $tt2 | cut -f1-3 -d ':' | tr -d '"')
        treg=$(echo $tt2 | cut -f4 -d ':')
        tacc=$(echo $tt2 | cut -f5 -d ':')
        tend=$(echo $tt2 | cut -f6- -d ':' | tr -d '"')

        if [[ $tt2 == "arn:aws:lambda:"* ]]; then
            lnam=$(echo $tt2 | rev | cut -f1 -d':' | rev)
            t1=$(printf "%s = aws_lambda_function.%s.arn" $tt1 $lnam)

        elif [[ "$tt2" == "arn:aws:sqs:"* ]]; then
            rsqs=$(echo $tt2 | tr -d '"')
            qnam=$(echo "$tt2" | rev | cut -f1 -d':' | rev)
            # modified sqs url is use for sqs queue
            # aws_sqs_queue.https___sqs_us-east-1_amazonaws_com_817339700138_lf-automation
            qnam2=$(printf "https___sqs_%s_amazonaws_com_%s_%s" $myreg $mysub $qnam)
            echo "wtf qnam=$qnam2"
            t1=$(printf "%s = aws_sqs_queue.%s.arn" $tt1 $qnam2)

        else # catch all remove region / account id

            if [[ "$treg" != "" ]] || [[ "$tacc" != "" ]]; then
                if [[ "$mysub" == "$tacc" ]]; then
                    if [[ "$treg" != "" ]]; then
                        tt2=$(printf "format(\"%s:%s:%s:%s\",data.aws_region.current.name,data.aws_caller_identity.current.account_id)" $tstart $tsub $tsub $tend)
                    else
                        tt2=$(printf "format(\"%s::%s:%s\",data.aws_caller_identity.current.account_id)" $tstart $tsub $tend)
                    fi
                fi
            fi
            if [[ $tt1 == *":"* ]]; then
                t1=$(printf "\"%s\" = %s" $tt1 $tt2)
            else
                t1=$(printf "%s = %s" $tt1 $tt2)
            fi
        fi

    elif [[ "$tt2" == "$myreg" ]]; then
        if [[ $tt1 == *":"* ]]; then
            t1=$(printf "\"%s\" = data.aws_region.current.name" $tt1)
        else
            t1=$(printf "%s = data.aws_region.current.name" $tt1)
        fi

    elif [[ "$tt2" == "$mysub" ]]; then
        if [[ $tt1 == *":"* ]]; then
            t1=$(printf "\"%s\" = data.aws_caller_identity.current.account_id" $tt1)
        else
            t1=$(printf "%s = data.aws_caller_identity.current.account_id" $tt1)
        fi

    elif [[ "$tt2" == "arn:aws:iam::${mysub}:root" ]]; then
        tsub="%s"
        if [[ $tt1 == *":"* ]]; then
            t1=$(printf "\"%s\" = format(\"arn:aws:iam::%s:root\",data.aws_caller_identity.current.account_id)" $tt1 $tsub)
        else
            t1=$(printf "%s = format(\"arn:aws:iam::%s:root\",data.aws_caller_identity.current.account_id)" $tt1 $tsub)

        fi
    fi

}

function fixra {
    at0=$(echo $1 | tr -d ' |"')
    at1=$(echo $2 | tr -d ' |"')
    #echo "raw at0 = ${at0} at1 = ${at1}"
    if [[ "$at1" != "*" ]]; then

        #echo "mysub = $mysub"

        if [[ "$at1" == "$myreg" ]]; then
            t1=$(printf "%s = data.aws_region.current.name" $tt1)

        elif [[ "$at1" == "$mysub" ]]; then
            if [[ $at0 == *":"* ]]; then
                t1=$(printf "\"%s\" = data.aws_caller_identity.current.account_id" $tt1)       
            else
                t1=$(printf "%s = data.aws_caller_identity.current.account_id" $tt1)
            fi

        elif [[ $at1 == *"arn:aws:iam::$mysub:root"* ]]; then
            #echo "here....."
            tsub="%s"
            t1=$(printf "%s = format(\"arn:aws:iam::%s:root\",data.aws_caller_identity.current.account_id)" $tt1 $tsub)

        elif [[ "$at1" == "arn:aws:"* ]]; then
            tstart=$(echo $at1 | cut -f1-3 -d ':' | tr -d '"')
            treg=$(echo $at1 | cut -f4 -d ':')
            tacc=$(echo $at1 | cut -f5 -d ':')
            tend=$(echo $at1 | cut -f6- -d ':' | tr -d '"')
            tsub="%s"
            tcomm=","
            #echo "at1 is arn  at1=$at1 tstart=$tstart tend=$tend"

            if [[ "$treg" != "" ]] || [[ "$tacc" != "" ]]; then

                if [[ "$tend" == *"," ]]; then
                    #echo "tend1=$tend"
                    tend=$(echo ${tend%?})
                    #echo "tend2=$tend"
                fi
                #echo "pre sub at1=$at1 tstart=$tstart tend=$tend"
                if [[ "$mysub" == "$tacc" ]]; then
                    if [[ "$treg" != "" ]]; then
                        tt2=$(printf "format(\"%s:%s:%s:%s\",data.aws_region.current.name,data.aws_caller_identity.current.account_id)," $tstart $tsub $tsub "$tend")
                    else
                        tt2=$(printf "format(\"%s::%s:%s\",data.aws_caller_identity.current.account_id)," $tstart $tsub "$tend")

                    fi
                fi

            fi

        fi
    fi
}
