#!/bin/bash
if [[ "$1" != "" ]]; then  
    if [[ ${1} == "arn:aws:iam"* ]]; then
        cmd[0]="$AWS iam list-users | jq '.Users[] | select(.Arn==\"${1}\")'"
    else
        cmd[0]="$AWS iam list-users | jq '.Users[] | select(.UserName==\"${1}\")'"
    fi
else
    cmd[0]="$AWS iam list-users"
fi

pref[0]="Users"
tft[0]="aws_iam_user"

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
    #echo "role command = $cm"
    ttft=${tft[(${c})]}
    #echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    if [ "$1" != "" ]; then
        count=1
    else
        count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    fi
    #echo "count=$count"
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            if [ "$1" != "" ]; then
                cname=`echo $awsout | jq -r ".UserName"` 
            else
                cname=`echo $awsout | jq -r ".${pref[(${c})]}[(${i})].UserName"`
            fi
            ocname=`echo $cname`
            cname=${cname//./_}
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            echo "$ttft $cname"
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi


            printf "resource \"%s\" \"%s\" {}" $ttft $cname > $fn
     
            terraform import $ttft.$rname $ocname | grep Import
            terraform state show -no-color $ttft.$rname > t1.txt
            rm -f $fn

            file="t1.txt"

            echo $aws2tfmess > $fn
            while IFS= read line
            do
                skip=0
                # display $line or do something with $line
                t1=`echo "$line"`
                if [[ ${t1} == *"="* ]];then
                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '`
                    tt2=`echo "$line" | cut -f2- -d'='`
                    if [[ ${tt1} == *":"* ]];then
                        tt1=`echo $tt1 | tr -d '"'`
                        t1=`printf "\"%s\"=%s" $tt1 $tt2`
                    fi
                    if [[ ${tt1} == "arn" ]];then skip=1; fi
                    if [[ ${tt1} == "id" ]];then skip=1; fi
                    if [[ ${tt1} == "role_arn" ]];then skip=1;fi
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    if [[ ${tt1} == "unique_id" ]];then skip=1;fi
                    if [[ ${tt1} == "create_date" ]];then skip=1;fi

                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"   # done while
            ##../../scripts/get-iam-groups-for-user.sh $cname
            
        done # done for i
        # Get attached role policies       
        
    fi
done

rm -f t*.txt

