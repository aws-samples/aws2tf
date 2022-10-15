#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS codeartifact describe-domain --domain $1" 
    pref[0]="domain"
else
    cmd[0]="$AWS codeartifact list-domains"
    pref[0]="domains"
fi

tft[0]="aws_codeartifact_domain"
idfilt[0]="name"

#rm -f ${tft[0]}.tf

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
        count=1
    else
        count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    fi
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            if [ "$1" != "" ]; then
                cname=`echo $awsout | jq ".${pref[(${c})]}.${idfilt[(${c})]}" | tr -d '"'`
                aarn=`echo $awsout | jq ".${pref[(${c})]}.arn" | tr -d '"'`
            else
                cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}" | tr -d '"'`
                aarn=`echo $awsout | jq ".${pref[(${c})]}[(${i})].arn" | tr -d '"'`
            fi
            echo "$ttft $cname"
            fn=`printf "%s__%s.tf" $ttft $cname`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
            printf "resource \"%s\" \"%s\" {" $ttft $cname > $ttft.$cname.tf
            printf "}" >> $ttft.$cname.tf
            printf "terraform import %s.%s %s" $ttft $cname $cname > data/import_$ttft_$cname.sh
            terraform import $ttft.$cname "$aarn" | grep Import
            terraform state show -no-color $ttft.$cname > t1.txt
            tfa=`printf "%s.%s" $ttft $cname`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > data/$tfa.json
            #echo $awsj | jq .
            
            rm -f $ttft.$cname.tf            
            echo $aws2tfmess > $fn

            file="t1.txt"
            while IFS= read line
            do
				skip=0
                # display $line or do something with $line
                t1=`echo "$line"` 
                if [[ ${t1} == *"="* ]];then
                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                    tt2=`echo "$line" | cut -f2- -d'='`
                    if [[ ${tt1} == "arn" ]];then skip=1; fi                
                    if [[ ${tt1} == "id" ]];then skip=1; fi   
                    if [[ ${tt1} == "asset_size_bytes" ]];then skip=1; fi 
                    if [[ ${tt1} == "created_time" ]];then skip=1; fi  
                    if [[ ${tt1} == "owner" ]];then skip=1; fi 
                    if [[ ${tt1} == "repository_count" ]];then skip=1; fi 
                    
                    if [[ ${tt1} == "encryption_key" ]]; then
                        keyid=`echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"'`
                        kt=$($AWS kms describe-key --key-id $keyid --query KeyMetadata.KeyManager | jq -r .)
                        if [[ "$kt" == "AWS" ]];then
                            # skip as default key
                            skip=1
                        else
                            t1=`printf "%s = aws_kms_key.k_%s.arn" $tt1 $keyid`
                        fi
                    fi               
               
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"

            if [[ "$keyid" != "" ]]; then
                ../../scripts/080-get-kms-key.sh $keyid
                ../../scripts/081-get-kms-alias.sh $keyid
            fi

        done
        
    fi
done

rm -f t*.txt

