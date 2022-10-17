#!/bin/bash
mysub=`echo $AWS2TF_ACCOUNT`
myreg=`echo $AWS2TF_REGION`
#echo "globe vars $myreg $mysub"
if [ "$1" != "" ]; then
    cmd[0]="$AWS kms describe-key --key-id $1"
    pref[0]="KeyMetadata"   
else
    cmd[0]="$AWS kms list-keys"
    pref[0]="Keys"
fi

tft[0]="aws_kms_key"
idfilt[0]="KeyId"

#rm -f ${tft[0]}.tf

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "You don't have access for this resource or it doesn't exist"
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
                cname=$(echo $awsout | jq -r ".${pref[(${c})]}.${idfilt[(${c})]}")
            else
                cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")
            fi
            keyd=`$AWS kms describe-key --key-id $cname 2> /dev/null`
            if [ "$awsout" == "" ];then
                echo "$cm : You don't have access for this resource"
                break
            fi

            keystate=$(echo $keyd | jq -r .KeyMetadata.KeyState)
            keyman=$(echo $keyd | jq -r .KeyMetadata.KeyManager)
            #echo "keystate=$keystate keyman=$keyman"
            if [ "$keystate" == "Enabled" ] && [ "$keyman" != "AWS" ]; then
                echo "$ttft $cname"
                fn=`printf "%s__k_%s.tf" $ttft $cname`
                if [ -f "$fn" ] ; then
                    echo "$fn exists already skipping ..."
                    continue
                fi
                printf "resource \"%s\" \"k_%s\" {" $ttft $cname > $fn
                printf "}" >> $fn
                printf "terraform import %s.k_%s %s" $ttft $cname $cname > "data/import_$ttft_$cname.sh"
                echo "$cname import"
                terraform import $ttft.k_$cname "$cname" | grep Import
                if [ $? -eq 0 ]; then
               
                    #terraform state mv $ttft.$cname $ttft.k_$cname
                    terraform state show -no-color $ttft.k_$cname > t1.txt
                    tfa=`printf "%s.%s" $ttft k_$cname`
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
                            #if [[ ${tt1} == "availability_zone" ]];then skip=1;fi
                            if [[ ${tt1} == "kms:"* ]]; then
                                tt2=`echo $tt2 | tr -d '"'`
                                t1=`printf "\"%s\" = \"%s\"" $tt1 $tt2`
                            fi
                            if [[ ${tt1} == "aws:"* ]]; then
                                tt2=`echo $tt2 | tr -d '"'`
                                t1=`printf "\"%s\" = \"%s\"" $tt1 $tt2`
                            fi

                            #if [[ ${tt1} == "Resource" ]]; then
                            #    tt2=`echo $tt2 | tr -d '"'`
                            #    if [[ "$tt2" != *"*"* ]];then
                            #        if [[ "$tt2" == *"arn:aws:kms:${myreg}:${mysub}:key/"* ]];then
                            #            kid=`echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"'`  
                            #            # can't do this - self referential block error                               
                            #            # t1=`printf "%s = aws_kms_key.k_%s.arn" $tt1 $kid`
                            #        fi
                            #    fi
                            #fi

                            if [[ ${tt1} == "AWS" ]]; then
                                tt2=`echo $tt2 | tr -d '"'`
                                if [[ ${tt2} == "arn:aws:iam::"* ]];then
                                    tstart=$(echo $tt2 | cut -f1-4 -d ':')
                                    tacc=$(echo $tt2 | cut -f5 -d ':')
                                    tend=$(echo $tt2 | cut -f6- -d ':')
                                    tsub="%s"
                                    if [[ "$mysub" == "$tacc" ]];then
                                        t1=$(printf "\"%s\" = format(\"%s:%s:%s\",data.aws_caller_identity.current.account_id)" $tt1 $tstart $tsub $tend)
                                    fi
                                fi
                            fi

                            if [[ ${tt2} == "aws:SourceVpce" ]]; then
                                tt2=`echo $tt2 | tr -d '"'`
                                t1=$(printf "\"%s\" = \"aws_vpc_endpoint.%s.id\"" $tt1 $tt2)
                            fi


                        # else
                            #              
                        fi

                        if [ "$skip" == "0" ]; then
                            #echo $skip $t1
                            echo "$t1" >> $fn
                        fi
                        
                    done <"$file"

                    # get any alias
                    ../../scripts/081-get-kms-alias.sh $cname

                else # import failed
                    echo "Import Failed $ttft $cname"
                    mv $ttft.$cname.tf $ttft.$cname.tf.failed
                fi 
            else
                echo "$ttft $cname key state = $keystate  key manager = $keyman"

            fi  
            if [ "$keyman" == "AWS" ];then
                dfn=`printf "data_%s__k_%s.tf" $ttft $cname`
                # get alias
                ../../scripts/081-get-kms-alias.sh $cname
                echo "AWS managed key data $dfn"
                printf "data \"%s\" \"k_%s\" {\n" $ttft $cname > $dfn
                printf "key_id = \"%s\"\n" $cname >> $dfn
                printf "}\n" >> $dfn
            fi
        done

    fi
done

rm -f t*.txt

