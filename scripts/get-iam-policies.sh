#!/bin/bash
mysub=`echo $AWS2TF_ACCOUNT`
myreg=`echo $AWS2TF_REGION`
ttft="aws_iam_policy"
if [[ "$1" != "" ]]; then
    if [[ "$1" != *":aws:policy"* ]];then
        # fast fail
        fn=`printf "%s__%s.tf" $ttft $1`
        if [ -f "$fn" ] ; then echo "$fn exists already skipping" && exit; fi
        # is is an arn ?
        if [[ "$1" == "arn:"* ]];then
            cmd[0]=`printf "$AWS iam list-policies | jq '.Policies[] | select(.Arn==\"%s\")' | jq ." $1`
        else # assume it's a policy name
            cmd[0]=`printf "$AWS iam list-policies | jq '.Policies[] | select(.PolicyName==\"%s\")' | jq ." $1`
        fi
    else
        echo "skipping AWS managed policy $1"
        exit
        #cmd[0]=`printf "$AWS iam list-policies | jq '.Policies[] | select(.Arn==\"%s\")' | jq ." $1`
    fi
else
    cmd[0]="$AWS iam list-policies --scope Local"
fi
#echo $1
pref[0]="Policies"
tft[0]="aws_iam_policy"
getp=0
for c in `seq 0 0`; do
    cm=${cmd[$c]}
    ttft=${tft[(${c})]}
    #echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    if [ "$1" != "" ]; then
        count=`echo $awsout | jq ". | length"`
        if [ "$count" -gt "1" ]; then
            count=1
        fi
    else
        count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    fi
    #echo "count=$count"
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            if [ "$1" != "" ]; then
                cname=`echo $awsout | jq ".Arn" | tr -d '"'`
                parn=`echo $awsout | jq ".Arn" | tr -d '"'`
                ocname=`echo $cname`
                cname=`echo $cname | rev | cut -f1 -d'/' | rev `
                pname=`echo $awsout | jq -r ".PolicyName"`
            else
                cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].Arn" | tr -d '"'`
                parn=`echo $awsout | jq ".${pref[(${c})]}[(${i})].Arn" | tr -d '"'`
                ocname=`echo $cname`
                cname=`echo $cname | rev | cut -f1 -d'/' | rev `
                pname=`echo $awsout | jq -r ".${pref[(${c})]}[(${i})].PolicyName"`
            fi
            
            echo "$ttft $cname $ocname $parn $pname"
            getp=1
            if [ "$1" != "" ]; then
              
                #getp=0
                if [ $parn == $1 ]; then
                    echo "Match"
                    #getp=1
                fi
            #else
                #echo "not set dollar 1"
                #getp=0
            fi
            echo $getp $1 $parn
            if [ "$getp" == "1" ]; then
                fn=`printf "%s__%s.tf" $ttft $cname`
                if [ -f "$fn" ] ; then
                    echo "$fn exists already skipping"
                    continue
                fi

                #echo "cname=$cname"
                printf "resource \"%s\" \"%s\" {}\n" $ttft $cname > $ttft.$cname.tf
    
                terraform import $ttft.$cname $ocname | grep Import
                terraform state show -no-color $ttft.$cname > t1.txt
                rm -f $ttft.$cname.tf

                file="t1.txt"
                #fn=`printf "%s__%s.tf" $ttft $cname`
                #if [ -f "$fn" ] ; then
                #    echo "$fn exists already skipping"
                #    exit
                #fi
                trole=""
                echo $aws2tfmess > $fn
                echo "# $0" >> $fn
                while IFS= read line
                do
                    skip=0
                    # display $line or do something with $line
                    t1=`echo "$line"`
                    if [[ ${t1} == *"="* ]];then
                        tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '`
                        tt2=`echo "$line" | cut -f2- -d'='`
                        if [[ ${tt1} == *":"* ]];then
                            # check tt2 for $
                            tt2=${tt2//$/&} 
                            tt1=`echo $tt1 | tr -d '"'` 
                            t1=`printf "\"%s\"=%s" $tt1 "$tt2"`
                        fi
                        if [[ ${tt1} == "Resource" ]];then
                            if [[ "$tt2" == *"${mysub}:role/aws-service-role"* ]];then
                                tt2=${tt2//$/&} 
                                tt1=`echo $tt1 | tr -d '"'` 
                                t1=`printf "%s=%s" $tt1 "$tt2"`         
                            
                            elif [[ "$tt2" == *"${mysub}:role/"* ]];then
                                rarn=`echo $tt2 | tr -d '"'` 
                                # test if * in role
                                if [[ "$tt2" == *"*"* ]];then
                                    echo "--> Wildcard Role"
                                    t1=`printf "%s = %s" $tt1 $tt2`
                                else
                                    
                                    trole=`echo "$tt2" | cut -f2- -d'/' | tr -d '"'`                       
                                    t1=`printf "%s = aws_iam_role.%s.arn" $tt1 $trole`
                                fi
                            else
                                tt2=${tt2//$/&} 
                                tt1=`echo $tt1 | tr -d '"'` 
                                t1=`printf "\"%s\"=%s" $tt1 "$tt2"`
                            fi
                        fi
                        if [[ ${tt1} == "arn" ]];then skip=1; fi
                        if [[ ${tt1} == "id" ]];then skip=1; fi
                        if [[ ${tt1} == "policy_id" ]];then skip=1; fi
                        if [[ ${tt1} == "role_arn" ]];then skip=1;fi
                    fi
                    if [ "$skip" == "0" ]; then
                        #echo $skip $t1
                    
                        echo "$t1" >> $fn
                    fi
                    
                done <"$file"   # done while

                # probably should be an array
                if [[ $rarn != "" ]];then
                    ../../scripts/050-get-iam-roles.sh $rarn
                fi
                
            fi
        done # done for i
    fi
done



rm -f t*.txt

