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
theregion=`echo "var.region" | terraform console | tr -d '"'`
keyid=""
doacl2=0
 
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
            lifec=0
            doacl2=0

            if [ "$cname" != "null" ] ; then
                fn=`printf "%s__%s.tf" $ttft $cname`
                if [ -f "$fn" ] ; then
                    echo "$fn exists already skipping"
                    continue
                fi
                
                # check region
                br=`$AWS s3api get-bucket-location --bucket ${cname}`
                if [ $? -ne 0 ]; then
                    br="null"
                else
                    br=`echo $br | jq .LocationConstraint | tr -d '"'`
                fi
                if [[ "$br" == "$theregion" ]]; then        
                    echo "$ttft $cname"
                    terraform state list $ttft.$cname &> /dev/null
                    if [[ $? -ne 0 ]];then
                        printf "resource \"%s\" \"%s\" {}\n" $ttft $cname > $fn
                        terraform import $ttft.$cname "$cname" &> /dev/null
                        if [[ $? -ne 0 ]];then
                            echo "Can't import/access bucket $cname - continue"
                            rm -f $fn
                            continue
                        fi
                    fi
                    #terraform state show $ttft.$cname | perl -pe 's/\x1b.*?[mGKH]//g' > t1.txt
                    s3b=$(terraform state show $ttft.$cname 2> /dev/null | perl -pe 's/\x1b.*?[mGKH]//g')
                    #echo $s3b
                    s3l=${#s3b}
                    vl=${#s3b}
                    if [[ $vl -eq 0 ]];then
                        echo "Retry for $ttft $cname"
                        sleep 5
                        s3b=$(terraform state show $ttft.$cname 2> /dev/null | perl -pe 's/\x1b.*?[mGKH]//g')
                        echo "S3 $ttft $cname Bucket Len=${#s3b}"
                        vl=${#s3b}
                        if [[ $vl -eq 0 ]];then
                            echo "Second Retry for $ttft $cname"
                            sleep 5
                            s3b=$(terraform state show $ttft.$cname 2> /dev/null | perl -pe 's/\x1b.*?[mGKH]//g')
                            echo "S3 $ttft $cname Bucket Len=${#s3b}"
                            vl=${#s3b}
                            if [[ $vl -eq 0 ]];then
                            echo "** Error Zero state $ttft $cname continue...."
                            continue
                            fi
                        fi
                    fi

                    rm -f $fn 
                    fn=`printf "%s__%s.tf" $ttft $cname`

                    flines=`echo "$s3b" | wc -l | awk '{ print $1 }'`
                    #echo "$cname lines in file t1.txt= $flines"
                    if [[ $s3l -gt 0 ]]; then
                        flc=0
                        fd=0
                        acl=0
                        keyid=""
                        doacl=1
                        doid=0
                        dosse=0
                        dover=0
                        dopol=0
                        dolog=0
                        
                        echo $aws2tfmess > $fn
                        
                        website=0
                        echo "$s3b" | { while IFS= read -r line  # open { for varaible scope

                        do
                            skip=0
                            # display $line or do something with $line
                            t1=`echo "$line"` 

                            if [[ "$t1" == *"grant"* ]];then
                                    doacl=0
                                    doid=1
                            fi

                            if [[ "$t1" == *"server_side_encryption_configuration"* ]];then 
                                    #echo $t1
                                    skip=1
                                    lbc=0
                                    rbc=0
                                    breq=0
                                    dosse=1
                                    while [[ $breq -eq 0 ]];do 
                                        if [[ "${t1}" == *"{"* ]]; then lbc=`expr $lbc + 1`; fi
                                        if [[ "${t1}" == *"}"* ]]; then rbc=`expr $rbc + 1`; fi
                                        #echo "op=$lbc $rbc $t1"
                                        if [[ $rbc -eq $lbc ]]; then 
                                            breq=1; 
                                        else
                                            read line
                                            t1=`echo "$line"`
                                        fi
                                    done 
                            fi


                            if [[ "$t1" == *"versioning"* ]];then 
                                    #echo $t1
                                    skip=1
                                    lbc=0
                                    rbc=0
                                    breq=0
                                    dover=1
                                    while [[ $breq -eq 0 ]];do 
                                        if [[ "${t1}" == *"{"* ]]; then lbc=`expr $lbc + 1`; fi
                                        if [[ "${t1}" == *"}"* ]]; then rbc=`expr $rbc + 1`; fi
                                        #echo "op=$lbc $rbc $t1"
                                        if [[ $rbc -eq $lbc ]]; then 
                                            breq=1; 
                                        else
                                            read line
                                            t1=`echo "$line"`
                                        fi
                                    done 
                            fi

                            if [[ "$t1" == *"logging"* ]];then 
                                    #echo $t1
                                    skip=1
                                    lbc=0
                                    rbc=0
                                    breq=0
                                    dolog=1
                                    while [[ $breq -eq 0 ]];do 
                                        if [[ "${t1}" == *"{"* ]]; then lbc=`expr $lbc + 1`; fi
                                        if [[ "${t1}" == *"}"* ]]; then rbc=`expr $rbc + 1`; fi
                                        #echo "op=$lbc $rbc $t1"
                                        if [[ $rbc -eq $lbc ]]; then 
                                            breq=1; 
                                        else
                                            read line
                                            t1=`echo "$line"`
                                        fi
                                    done 
                            fi





                            if [[ "$t1" == *"website"* ]];then 
                                    #echo $t1
                                    skip=1
                                    lbc=0
                                    rbc=0
                                    breq=0
                                    website=1
                                    while [[ $breq -eq 0 ]];do 
                                        if [[ "${t1}" == *"{"* ]]; then lbc=`expr $lbc + 1`; fi
                                        if [[ "${t1}" == *"}"* ]]; then rbc=`expr $rbc + 1`; fi
                                        #echo "op=$lbc $rbc $t1"
                                        if [[ $rbc -eq $lbc ]]; then 
                                            breq=1; 
                                        else
                                            read line
                                            t1=`echo "$line"`
                                        fi
                                    done 
                            fi

                            if [[ ${t1} == *"grant"* ]];then 
                                    #echo $t1
                                    skip=1
                                    lbc=0
                                    rbc=0
                                    breq=0
                                    doacl2=1
                                    while [[ $breq -eq 0 ]];do 
                                        if [[ "${t1}" == *"{"* ]]; then lbc=`expr $lbc + 1`; fi
                                        if [[ "${t1}" == *"}"* ]]; then rbc=`expr $rbc + 1`; fi
                                        #echo "op=$lbc $rbc $t1"
                                        if [[ $rbc -eq $lbc ]]; then 
                                            breq=1; 
                                        else
                                            read line
                                            t1=`echo "$line"`
                                        fi
                                    done 
                            fi

                            if [[ ${t1} == *"lifecycle_rule"* ]];then 
                                    #echo $t1
                                    skip=1
                                    lbc=0
                                    rbc=0
                                    breq=0
                                    lifec=1
                                    while [[ $breq -eq 0 ]];do 
                                        if [[ "${t1}" == *"{"* ]]; then lbc=`expr $lbc + 1`; fi
                                        if [[ "${t1}" == *"}"* ]]; then rbc=`expr $rbc + 1`; fi
                                        #echo "op=$lbc $rbc $t1"
                                        if [[ $rbc -eq $lbc ]]; then 
                                            breq=1; 
                                        else
                                            read line
                                            t1=`echo "$line"`
                                        fi
                                    done 
                            fi

                            if [[ ${t1} == *"policy"* ]];then 
                                    #echo $t1
                                    skip=1
                                    lbc=0
                                    rbc=0
                                    breq=0
                                    dopol=1
                                    while [[ $breq -eq 0 ]];do 
                                        if [[ "${t1}" == *"("* ]]; then lbc=`expr $lbc + 1`; fi
                                        if [[ "${t1}" == *")"* ]]; then rbc=`expr $rbc + 1`; fi
                                        #echo "op=$lbc $rbc $t1"
                                        if [[ $rbc -eq $lbc ]]; then 
                                            breq=1; 
                                        else
                                            read line
                                            t1=`echo "$line"`
                                        fi
                                    done 
                            fi

                            if [[ ${t1} == *"="* ]];then
                                tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                                tt2=`echo "$line" | cut -f2- -d'='`  

                                if [[ ${tt1} == "arn" ]];then skip=1 ;fi
                                    
                                if [[ ${tt1} == "id" ]];then skip=1 ;fi

                                if [[ ${tt1} == "s3:"* ]]; then
                                    tt2=`echo $tt2 | tr -d '"'`
                                    tt1=`echo $tt1 | tr -d '"'`
                                    t1=`printf "\"%s\" = \"%s\"" $tt1 $tt2`
                                fi

                                if [[ ${tt1} == "aws:"* ]]; then
                                    tt2=`echo $tt2 | tr -d '"'`
                                    tt1=`echo $tt1 | tr -d '"'`
                                    t1=`printf "\"%s\" = \"%s\"" $tt1 $tt2`
                                fi

                                if [[ ${tt1} == "region" ]];then skip=1 ;fi
                                if [[ ${tt1} == "request_payer" ]];then skip=1 ;fi
                                if [[ ${tt1} == "kms_master_key_id" ]];then 
                              
                                    keyid=`echo $tt2 | tr -d '"'`
                                    if [[ $keyid == *":"* ]]; then
                                        keyid=$(echo $keyid | rev | cut -f1 -d'/' | rev)
                                    fi
                                    # quick check it exists

                                    $AWS kms describe-key --key-id $keyid &> /dev/null
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
                                #if [[ ${tt1} == "force_destroy" ]];then
                                #skip=0
                                #fd=1
                                #fi
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
                                if [[ ${tt1} == "website_endpoint" ]];then skip=1;fi
                                if [[ ${tt1} == "website_domain" ]];then skip=1;fi
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
                        
                        done
                          
                        if [[ "$keyid" != "" ]]; then
                            #echo "*** key for $keyid"
                            ../../scripts/080-get-kms-key.sh $keyid 
                            #echo "*** key alias for $keyid"
                            ../../scripts/081-get-kms-alias.sh $keyid 
                        fi 


                        #echo "Out: $dopol $dover $doacl2 $dosse $lifec $website"        
                        if [[ $dolog -eq 1 ]];then
                            ../../scripts/get-aws_s3_bucket_logging.sh $cname & 
                        fi
                        if [[ $dopol -eq 1 ]];then
                            ../../scripts/get-aws_s3_bucket_policy.sh $cname & 
                        fi
                        if [[ $dover -eq 1 ]];then 
                            #echo "versioning job for $cname"
                            ../../scripts/get-aws_s3_bucket_versioning.sh $cname &
                        fi
                        if [[ $doacl2 -eq 1 ]];then 
                            #echo "acl job for $cname"
                            ../../scripts/get-aws_s3_bucket_acl.sh $cname & 
                        fi
                        if [[ $lifec -eq 1 ]];then 
                            #echo "lifecycle job for $cname"
                            ../../scripts/get-aws_s3_bucket_lifecycle_configuration.sh $cname &
                        fi
                        if [[ $dosse -eq 1 ]];then 
                            #echo "sse job for $cname"
                            ../../scripts/get-aws_s3_bucket_server_side_encryption_configuration.sh $cname &
                        fi
                        if [[ $website -eq 1 ]];then
                            #echo "website job for $cname" 
                            ../../scripts/get-aws_s3_bucket_website_configuration.sh $cname &
                        fi
                        jc=`jobs -r | wc -l | tr -d ' '`
                        echo "waiting for $jc jobs ....."
                        #if [[ $jc -ne 0 ]];then
                        #    sleep $jc   
                        #    jc=`jobs -r | wc -l | tr -d ' '`
                        #    echo "waiting for $jc jobs ....."
                        #    if [[ $jc -gt 2 ]];then sleep $jc ;fi
                        #    if [[ $jc -gt 4 ]];then echo "waiting..." && wait ;fi
                        #fi
                        wait
                        #../../scripts/get-s3-request-payer.sh $cname
                        }                    
                    fi
                else
                    echo "Bucket $cname not in current region $theregion skipped ..."
                fi # $br
            fi # $cname
            # Parallel job throttle
            #jc=`jobs -r | wc -l | tr -d ' '`
            #if [[ $jc -ne 0 ]];then
            #echo "waiting for $jc jobs ....."
            #    sleep $jc   
            #    jc=`jobs -r | wc -l | tr -d ' '`
            #    echo "waiting for $jc jobs ....."
            #    if [[ $jc -gt 2 ]];then sleep $jc ;fi
            #    if [[ $jc -gt 4 ]];then echo "waiting..." && wait ;fi
            #fi
            
        done # i
        jc=`jobs -r | wc -l | tr -d ' '`
        echo "Pre state mv waiting for $jc jobs ....."
        if [[ $jc -ne 0 ]];then
            echo "waiting for $jc jobs ....."
        fi
        wait  
        ../../scripts/local_statemv.sh aws_s3

    else
        terraform state rm $ttft.$cname
    fi 
    #echo "Done $cname"
done # for c
echo "run cross checker"
../../scripts/cross-check-s3-all.sh
