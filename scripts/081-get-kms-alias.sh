#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS kms list-aliases --key-id $1"  
else
    cmd[0]="$AWS kms list-aliases"
   
fi

pref[0]="Aliases"
tft[0]="aws_kms_alias"
idfilt[0]="AliasName"

#rm -f ${tft[0]}.tf

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm
    awsout=`eval $cm`
    if [ "$1" != "" ]; then
        count=1
    else
        count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    fi
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i

            cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")
            if [[ "$cname" != *"alias/aws/"* ]];then
                rname=${cname//:/_}
                rname=${rname//./_}
                rname=${rname//\//_}

                echo "$ttft $cname"
                fn=`printf "%s__%s.tf" $ttft $rname`
                if [ -f "$fn" ] ; then
                    echo "$fn exists already skipping"
                    continue
                fi

                kmsid=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].TargetKeyId")
                if [ "$kmsarn" != "" ]; then
                    ../../scripts/080-get-kms-key.sh $kmsid
                fi

                printf "resource \"%s\" \"%s\" {" $ttft $rname > $ttft.$rname.tf
                printf "}" >> $ttft.$rname.tf
                printf "terraform import %s.%s %s" $ttft $rname "$cname" > import_$ttft_$rname.sh
                terraform import $ttft.$rname "$cname"
                
                terraform state show $ttft.$rname > t2.txt
                tfa=`printf "%s.%s" $ttft $rname`
                terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > $tfa.json
                #echo $awsj | jq . 
                rm $ttft.$rname.tf
                # rename state to save problems later
                cat t2.txt | perl -pe 's/\x1b.*?[mGKH]//g' > t1.txt
                #	for k in `cat t1.txt`; do
                #		echo $k
                #	done
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
                        if [[ ${tt1} == "arn" ]];then skip=1; fi                
                        if [[ ${tt1} == "id" ]];then skip=1; fi          
                        if [[ ${tt1} == "role_arn" ]];then skip=1;fi
                        if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                        if [[ ${tt1} == "key_id" ]];then skip=1;fi
                        #if [[ ${tt1} == "availability_zone" ]];then skip=1;fi
                        if [[ ${tt1} == "kms:"* ]]; then
                            tt2=`echo $tt2 | tr -d '"'`
                            t1=`printf "\"%s\" = \"%s\"" $tt1 $tt2`
                        fi
                        if [[ ${tt1} == "target_key_arn" ]];then 
                            kid=`echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"'`                            
                            kmsarn=$(echo $tt2 | tr -d '"')
                            #echo $t1
                            t1=`printf "%s = aws_kms_key.k_%s.arn" $tt1 $kid`                    
                        fi

                    # else
                        #              
                    fi

                    if [ "$skip" == "0" ]; then
                        #echo $skip $t1
                        echo $t1 >> $fn
                    fi
                    
                done <"$file"
            fi
        done

    fi
done

if [[ "$1" == "" ]]; then   
    terraform fmt
    terraform validate
fi

rm -f t*.txt

