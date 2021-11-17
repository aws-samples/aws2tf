#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS iam list-attached-role-policies --role-name $1"
else
    exit
fi
c=0
cm=${cmd[$c]}

pref[0]="AttachedPolicies"
tft[0]="aws_iam_role_policy_attachment"

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
    ttft=${tft[(${c})]}
    #echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "You don't have access for this resource"
        exit
    fi
    #echo "awsout $awsout"
    if [ "$1" != "" ]; then
        count=1
    else
        count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    fi
    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            #echo $awsout | jq .
            
            
            
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].PolicyName" | tr -d '"'`
            rarn=`echo $awsout | jq ".${pref[(${c})]}[(${i})].PolicyArn" | tr -d '"'`
            ocname=`echo $cname`
            cname=${cname//./_}
            cname=`printf "%s__%s" $1 $cname`
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            
            echo "$ttft $cname import"
            fn=`printf "%s__%s.tf" $ttft $rname`

            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
            printf "resource \"%s\" \"%s\" {" $ttft $rname > $ttft.$rname.tf
            printf "}"  >> $ttft.$rname.tf
            printf "terraform import %s.%s %s" $ttft $rname "$cname" > data/import_$ttft_$rname.sh
            
            terraform import $ttft.$rname $1/$rarn | grep Import
            #terraform import $ttft.$rname "$cname" | grep Import
            terraform state show $ttft.$rname > t2.txt
            tfa=`printf "data/%s.%s" $ttft $rname`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > $tfa.json
            #echo $awsj | jq . 
            rm $ttft.$rname.tf
            
            cat t2.txt | perl -pe 's/\x1b.*?[mGKH]//g' > t1.txt
            #	for k in `cat t1.txt`; do
            #		echo $k
            #	done
            file="t1.txt"
            pnam=""
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
                        t1=`printf "\"%s\"=%s" $tt1 $tt2`
                    fi
                    if [[ ${tt1} == "role" ]];then 
                        tsel=`echo $tt2 |  tr -d '"'`
                        tsel=${tsel//:/_} && tsel=${tsel//./_} && tsel=${tsel//\//_}
                        t1=`printf "%s = aws_iam_role.%s.id" $tt1 $tsel`
                        skip=0;
                    fi
                    if [[ ${tt1} == "policy_arn" ]];then 
                        #echo "tt2=$tt2"
                        if [[ "${tt2}" == *"service-role"* ]]; then
                            pnam=`echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"'`
                            parn=`echo $tt2 | tr -d '"'`
                            #echo "parn=$parn"
                            #echo "pnam=$pnam"
            
                            t1=`printf "%s = aws_iam_policy.%s.arn" $tt1 $pnam`
                        fi
                        skip=0;
                    fi


                    if [[ ${tt1} == "arn" ]];then skip=1; fi
                    if [[ ${tt1} == "id" ]];then skip=1; fi
                    if [[ ${tt1} == "role_arn" ]];then skip=1;fi
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    if [[ ${tt1} == "association_id" ]];then skip=1;fi
                    if [[ ${tt1} == "unique_id" ]];then skip=1;fi
                    if [[ ${tt1} == "create_date" ]];then skip=1;fi
                    #if [[ ${tt1} == "public_ip" ]];then skip=1;fi
                    if [[ ${tt1} == "private_ip" ]];then skip=1;fi
                    if [[ ${tt1} == "accept_status" ]];then skip=1;fi
                    #if [[ ${tt1} == "default_network_acl_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "ipv6_association_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "ipv6_cidr_block" ]];then skip=1;fi
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"   # done while
            #echo "pre-policy pnam=$pnam"
            if [[ "$pnam" != "" ]];then 
                #echo "Get the Policy name=$pnam arn=$parn"
                ../../scripts/get-iam-policies.sh $parn
            fi
        done # done for i
    fi
done

rm -f t*.txt

