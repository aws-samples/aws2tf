#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS kms list-aliases --key-id $1"  
else
    cmd[0]="$AWS kms list-aliases"
fi

pref[0]="Aliases"
tft[0]="aws_kms_alias"
idfilt[0]="AliasName"
c=0
#rm -f ${tft[0]}.tf

if [[ "$1" == "null" ]];then
    echo "null key alias exiting ...."
    exit
fi
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

            cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")
            rname=${cname//:/_}
            rname=${rname//./_}
            rname=${rname//\//_}
            if [[ "$cname" == "null" ]];then
                echo "null key alias continue ...."
                continue
            fi
            
            
            #echo "$ttft $cname"
            if [[ "$cname" != *"alias/aws/"* ]];then
                echo "$ttft $cname"
                fn=`printf "%s__%s.tf" $ttft $rname`
                if [ -f "$fn" ] ; then
                    echo "$fn exists already skipping"
                    continue
                fi

                kmsid=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].TargetKeyId")
                #if [ "$kmsid" != "" ]; then
                #    ../../scripts/080-get-kms-key.sh $kmsid
                #fi

                printf "resource \"%s\" \"%s\" {" $ttft $rname > $fn
                printf "}" >> $fn


                printf "terraform import %s.%s %s" $ttft $rname "$cname" > import_$ttft_$rname.sh
                terraform import $ttft.$rname "$cname" | grep Import
                
                terraform state show -no-color $ttft.$rname > t1.txt
                tfa=`printf "%s.%s" $ttft $rname`
                terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > data/$tfa.json
                #echo $awsj | jq . 
                rm -f $fn
                # rename state to save problems later

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
                        if [[ ${tt1} == "target_key_arn" ]];then skip=1;fi
                        if [[ ${tt1} == "kms:"* ]]; then
                            tt2=`echo $tt2 | tr -d '"'`
                            t1=`printf "\"%s\" = \"%s\"" $tt1 $tt2`
                        fi
                        if [[ ${tt1} == "target_key_id" ]];then                             
                            kid=$(echo $tt2 | tr -d '"')
                            
                            t1=`printf "%s = aws_kms_key.k_%s.id" $tt1 $kid`                    
                        fi

                    # else
                        #              
                    fi

                    if [ "$skip" == "0" ]; then
                        #echo $skip $t1
                        echo "$t1" >> $fn
                    fi
                    
                done <"$file"

                if [ "$kmsid" != "" ]; then
                    ../../scripts/080-get-kms-key.sh $kmsid
                fi


            else
                cmd2=`printf "$AWS kms list-aliases | jq -r '.Aliases[] | select(.AliasName==\"%s\").TargetKeyId'" $cname`
                tgtid=$(eval $cmd2)
                desc=`$AWS kms describe-key --key-id $tgtid 2>/dev/null`
                if [ "$desc" != "" ]; then
                    dfn=`printf "data_%s__%s.tf" $ttft $rname`
                    echo "AWS managed key alias data $dfn $cname"
                    printf "data \"%s\" \"%s\" {\n" $ttft $rname > $dfn
                    printf "name = \"%s\"\n" "$cname" >> $dfn
                    printf "}\n" >> $dfn
                else
                    echo "You don't have access for this resource $cname"
                fi

            fi
            
        done

    fi
done


rm -f t*.txt

