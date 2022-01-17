#!/bin/bash
if [ "$1" != "" ]; then 
    BUCKET_NAME=$1
    JSON_STRING=$( jq -n \
                  --arg bn "$BUCKET_NAME" \
                  '{Buckets: [{Name: $bn}]}' )


    cmd[0]=`echo $JSON_STRING | jq .`
else
    cmd[0]="$AWS s3api list-buckets"
fi

pref[0]="Buckets"
tft[0]="aws_s3_bucket"
idfilt[0]="Name"
theregion=`cat aws.tf | grep region | awk '{print $3}' | tr -d '"'`
keyid=""
#theregion=`echo $AWS | cut -f5 -d ' '`
 
for c in `seq 0 0`; do
   
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm | jq .
    #echo "here"
    if [ "$1" != "" ]; then 
        awsout=`echo $cm | jq .`
        if [ "$awsout" == "" ];then
            echo "$cm : You don't have access for this resource"
            exit
        fi
    else
        awsout=`eval $cm 2> /dev/null`
        if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        exit
        fi
    fi 
    #echo awsout=$awsout
    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    #echo count=$count
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}" | tr -d '"'`
            echo "$ttft $cname"

            if [ "$cname" != "null" ] ; then
                fn=`printf "%s__%s.tf" $ttft $cname`
                if [ -f "$fn" ] ; then
                    echo "$fn exists already skipping"
                    exit
                fi
                
                # check region
                br=`$AWS s3api get-bucket-location --bucket ${cname}`
                if [ $? -ne 0 ]; then
                    br="null"
                else
                    br=`echo $br | jq .LocationConstraint | tr -d '"'`
                fi
                
                if [ "$br" == "$theregion" ]; then
                             
                
                    printf "resource \"%s\" \"%s\" {" $ttft $cname > $fn
                    printf "}" >> $fn
            
                    terraform import $ttft.$cname "$cname" 2> /dev/null
                    if [[ $? -eq 1 ]];then
                        echo "Can't access bucket $cname - continue"
                        rm -f $fn
                        continue
                    fi
                    terraform state show $ttft.$cname > t2.txt
                    rm -f $fn
                    cat t2.txt | perl -pe 's/\x1b.*?[mGKH]//g' > t1.txt
                    file="t1.txt"
                    fn=`printf "%s__%s.tf" $ttft $cname`

                    flines=`wc -l $file | awk '{ print $1 }'`
                    #echo "$cname lines in file t1.txt= $flines"
                    if [[ $flines > 0 ]]; then
                        flc=0
                        fd=0
                        acl=0
                        keyid=""
                        doacl=1
                        doid=0
                        echo $aws2tfmess > $fn

                        while IFS= read line
                        do
                            skip=0
                            # display $line or do something with $line
                            t1=`echo "$line"` 

                            if [[ "$t1" == *"grant"* ]];then
                                    doacl=0
                                    doid=1
                            fi

                            if [[ ${t1} == *"="* ]];then
                                tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                                tt2=`echo "$line" | cut -f2- -d'='`  

                                if [[ ${tt1} == "arn" ]];then	
                                    #printf "acl = \"private\" \n" >> $fn
                                    #printf "force_destroy = false \n" >> $fn

                                    skip=1
                                fi
                                    
                                if [[ ${tt1} == "id" ]];then 
                                    if [[ "$doid" == "0" ]];then 
                                    skip=1; 
                                        printf "lifecycle {\n" >> $fn
                                        printf "   ignore_changes = [acl,force_destroy]\n" >> $fn
                                        printf "}\n" >> $fn
                                    
                                    fi 
                                fi

                                if [[ ${tt1} == "region" ]];then skip=1 ;fi
                                if [[ ${tt1} == "kms_master_key_id" ]];then 
                              
                                    keyid=`echo $tt2 | tr -d '"'`
                                    if [[ $keyid == *":"* ]]; then
                                        keyid=$(echo $keyid | rev | cut -f1 -d'/' | rev)
                                    fi
                                    # quick check it exists

                                    $AWS kms describe-key --key-id $keyid 2> /dev/null
                                    if [[ $? -eq 0 ]];then
                                        t1=`printf "%s = aws_kms_key.k_%s.id" $tt1 $keyid`
                                    else
                                        t1=`printf "# COMMENT THIS KEY DOESN'T EXIST %s = aws_kms_key.k_%s.id" $tt1 $keyid`
                                        keyid=""
                                    fi
                                fi
                                    
                                if [[ ${tt1} == "role_arn" ]];then 
                                    printf "provider = \"aws.regional\"\n" >> $fn
                                    skip=0;
                                fi
                                if [[ ${tt1} == "force_destroy" ]];then
                                skip=0
                                fd=1
                                fi
                                if [[ ${tt1} == "acl" ]];then
                                    if [[ "$doacl" == "1" ]]; then
                                        skip=0
                                        acl=1
                                    fi
                                fi
                                if [[ ${tt1} == "bucket_domain_name" ]];then skip=1;fi
                                if [[ ${tt1} == "bucket_regional_domain_name" ]];then skip=1;fi
                                if [[ ${tt1} == "allocated_capacity" ]];then skip=1;fi
                                if [[ ${tt1} == "hosted_zone_id" ]];then skip=1;fi
                            fi


                            ((flc=flc+1))
                            if [[ $flc = $flines ]];then
                                if [[ $fd = 0 ]]; then
                                    echo "force_destroy=false" >> $fn
                                fi
                                if [[ $acl = 0 ]]; then
                                    if [[ "$doacl" == "1" ]]; then
                                        printf "acl = \"private\" \n" >> $fn

                                    fi
                                fi
                            fi
                            if [ "$skip" == "0" ];then
                                #echo $skip $t1 $ttft
                                echo "$t1" >> $fn
                            fi                
                        
                        done <"$file" 
                        
                        if [[ "$keyid" != "" ]]; then
                            echo "*** key for $keyid"
                            ../../scripts/080-get-kms-key.sh $keyid
                            echo "*** key alias for $keyid"
                            ../../scripts/081-get-kms-alias.sh $keyid
                        fi 

                        echo "*** policy for $cname"
                        ../../scripts/get-s3-policy.sh $cname
                    fi
                else
                    echo "Bucket $cname not in current region $theregion skipped ..."
                fi # $br
            fi # $cname
        done # i
    else
        terraform state rm $ttft.$cname
    fi 
    #echo "Done $cname"
done
rm -f t*.txt