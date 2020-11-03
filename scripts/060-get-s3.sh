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

theregion=`echo $AWS | cut -f5 -d ' '`
 
for c in `seq 0 0`; do
   
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	echo $cm | jq .
    echo "here"
    if [ "$1" != "" ]; then 
        awsout=`echo $cm | jq .`
    else
        awsout=`eval $cm`
    fi 
    echo awsout=$awsout
    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    echo count=$count
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}" | tr -d '"'`
            echo $cname
            if [ "$cname" != "null" ] ; then
                
                # check region
                br=`$AWS s3api get-bucket-location --bucket ${cname}`
                if [ $? -ne 0 ]; then
                    br="null"
                else
                    br=`echo $br | jq .LocationConstraint | tr -d '"'`
                fi
                echo $cname $br $theregion
                
                if [ "$br" == "$theregion" ]; then
                             
                
                    printf "resource \"%s\" \"%s\" {" $ttft $cname > $ttft.$cname.tf
                    printf "}" $cname >> $ttft.$cname.tf
                    terraform import $ttft.$cname $cname
                    terraform state show $ttft.$cname > t2.txt
                    rm $ttft.$cname.tf
                    cat t2.txt | perl -pe 's/\x1b.*?[mGKH]//g' > t1.txt
                    file="t1.txt"
                    fn=`printf "%s__%s.tf" $ttft $cname`
                    flines=`wc -l $file | awk '{ print $1 }'`
                    #echo "$cname lines in file t1.txt= $flines"
                    if [[ $flines > 0 ]]; then
                        flc=0
                        fd=0
                        acl=0
                        echo $aws2tfmess > $fn
                        while IFS= read line
                        do
                            skip=0
                            # display $line or do something with $line
                            t1=`echo "$line"` 
                            if [[ ${t1} == *"="* ]];then
                                tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                                    
                                if [[ ${tt1} == "arn" ]];then	
                                    #printf "acl = \"private\" \n" >> $fn
                                    #printf "force_destroy = false \n" >> $fn

                                    skip=1
                                fi
                                    
                                if [[ ${tt1} == "id" ]];then
                                    #printf "acl = \"private\"\n" >> $fn
                                    #printf "force_destroy = false \n" >> $fn

                                    skip=1
                                fi
                                if [[ ${tt1} == "region" ]];then
                                    skip=1
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
                                skip=0
                                acl=1
                                fi
                                if [[ ${tt1} == "bucket_domain_name" ]];then skip=1;fi
                                if [[ ${tt1} == "bucket_regional_domain_name" ]];then skip=1;fi
                                if [[ ${tt1} == "allocated_capacity" ]];then skip=1;fi
                            fi


                            ((flc=flc+1))
                            if [[ $flc = $flines ]];then
                                if [[ $fd = 0 ]]; then
                                    echo "force_destroy=false" >> $fn
                                fi
                                if [[ $acl = 0 ]]; then
                                    printf "acl = \"private\" \n" >> $fn
                                fi
                            fi
                            if [ "$skip" == "0" ];then
                                #echo $skip $t1 $ttft
                                echo $t1 >> $fn
                            fi                
                        
                        done <"$file" 
                    fi
                fi
            fi
        done
    else
        terraform state rm $ttft.$cname
    fi 
    echo "Done $cname"
done

# get the policies that were pulled out:



terraform fmt
terraform validate


rm -f t*.txt
exit
