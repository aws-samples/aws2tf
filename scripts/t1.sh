#!/bin/bash
bucks=()
if [ "$1" != "" ]; then 
    bucks+=`s3api list-buckets --query Buckets[*].Name | jq .[] | grep $1`
else
    bucks+=`aws s3api list-buckets --query Buckets[*].Name | jq .[]`
fi

for cname in ${bucks[@]}; do
    cname=`echo $cname | tr -d '"'`
    echo $cname         
done











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
                fn=`printf "%s__%s.tf" $ttft $rname`
                if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi
                
                # check region
                br=`$AWS s3api get-bucket-location --bucket ${cname}`
                if [ $? -ne 0 ]; then
                    br="null"
                else
                    br=`echo $br | jq .LocationConstraint | tr -d '"'`
                fi
                if [[ "$br" == "$theregion" ]]; then        
                    echo "$ttft $cname Import"
                    #terraform state list $ttft.$cname &> /dev/null
                    #if [[ $? -ne 0 ]];then
                    . ../../scripts/parallel_import2.sh $ttft $cname &
                    #fi
                    jc=`jobs -r | wc -l | tr -d ' '`
                    echo "$jc jobs"
                    while [ $jc -gt 15 ];do
                        echo "Throttling - $jc Terraform imports in progress"
                        sleep 10
                        jc=`jobs -r | wc -l | tr -d ' '`
                    done
                else
                    echo "Bucket is not in region $theregion"
                fi #in region
            else
                echo "Bucket name is null"
                continue
            fi # cname is not null
        done # for i count

        jc=`jobs -r | wc -l | tr -d ' '`
        if [ $jc -gt 0 ];then
            echo "Waiting for $jc Terraform imports"
            wait
            echo "Finished importing"
        fi

        ../../scripts/parallel_statemv.sh $ttft        

# remove these 3 lines post testing
 

# Terraform files section
# for c
    # if count
        for i in `seq 0 $count`; do
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}" | tr -d '"'`
            s3b=$(terraform state show -no-color $ttft.$cname 2> /dev/null)
            echo "$ttft $cname tf files"
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

            file=`printf "%s-%s-1.txt" $ttft $rname`
            if [ ! -f "$file" ] ; then echo "$file does not exist skipping" && continue; fi
            echo $aws2tfmess > $fn
            rm -f $fn 
            fn=`printf "%s__%s.tf" $ttft $cname`

            flines=`echo "$s3b" | wc -l | awk '{ print $1 }'`
                    #echo "$cname lines in file t1.txt= $flines"
            lifec=0
            doacl2=0       
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
              
                        
                done # while file
            }
        done # for i
    fi
done
exit    
                          
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
                        #wait
                        #../../scripts/get-s3-request-payer.sh $cname
                                           
                    
            # Parallel job throttle
            jc=`jobs -r | wc -l | tr -d ' '`
            while [ $jc -gt 15 ];do
                echo "Throttling - $jc Terraform imports in progress"
                sleep 10
                jc=`jobs -r | wc -l | tr -d ' '`
            done
            
        done # i
        jc=`jobs -r | wc -l | tr -d ' '`
        echo "Pre state mv waiting for $jc jobs ....."
        if [[ $jc -ne 0 ]];then
            echo "waiting for $jc jobs ....."
        fi
        wait  
        ../../scripts/local_statemv.sh aws_s3

    #else
    #    terraform state rm $ttft.$cname
    fi #count > 0
    #echo "Done $cname"
done # for c
echo "run cross checker"
../../scripts/cross-check-s3-all.sh
