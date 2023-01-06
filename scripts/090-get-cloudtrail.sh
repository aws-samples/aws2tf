#!/bin/bash
cmd[0]="$AWS cloudtrail list-trails"
pref[0]="Trails"
tft[0]="aws_cloudtrail"
idfilt[0]="SubnetId"

for c in `seq 0 0`; do
    region=`echo "var.region" | terraform console | tr -d '"'`
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            regname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].HomeRegion")
            if [ "$region" == "$regname" ]; then
                cname=`echo $awsout | jq -r ".${pref[(${c})]}[(${i})].Name"`
                echo "$ttft $cname"
                printf "resource \"%s\" \"%s\" {" $ttft $cname > $ttft.$cname.tf
                printf "}" >> $ttft.$cname.tf
                terraform import $ttft.$cname "$cname" | grep Import
                terraform state show -no-color $ttft.$cname > t1.txt
                rm -f $ttft.$cname.tf

                file="t1.txt"
                fn=`printf "%s__%s.tf" $ttft $cname`
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
                        if [[ ${tt1} == "home_region" ]];then skip=1;fi
                        if [[ ${tt1} == "s3_bucket_name" ]];then                             
                            s3buck=$(echo $tt2 | tr -d '"')
                            t1=`printf "%s = aws_s3_bucket.b_%s.bucket" $tt1 $s3buck`                    
                        fi
                        if [[ ${tt1} == "cloud_watch_logs_group_arn" ]];then 
                            cwarn=`echo $tt2 | tr -d '"'`
                           
                            sub="log-group:"
                            rest=${cwarn#*$sub}
                           
                            cwnam=`echo $rest | cut -f1 -d':'`
                            rcwnam=${cwnam//:/_}
                            rcwnam=${rcwnam//./_}
                            rcwnam=${rcwnam//\//_}
                            #echo "** cwnam= $cwnam   rcwnam= $rcwnam"
                            skip=0;                                                                         
                            t1=`printf "%s = aws_cloudwatch_log_group.%s.arn" $tt1 $rcwnam`
                        fi

                        if [[ ${tt1} == "cloud_watch_logs_role_arn" ]];then 
                            rarn=`echo $tt2 | tr -d '"'` 
                            skip=0;
                            trole=`echo "$tt2" | cut -f2- -d'/' | tr -d '"'`
                                                    
                            t1=`printf "%s = aws_iam_role.%s.arn" $tt1 $trole`
                        fi
                        if [[ ${tt1} == "kms_key_id" ]];then 
                            kid=`echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"'`                            
                            kmsarn=$(echo $tt2 | tr -d '"')
                            #echo $t1
                            t1=`printf "%s = aws_kms_key.k_%s.arn" $tt1 $kid`                    
                        fi

                    fi
                    if [ "$skip" == "0" ]; then
                        #echo $skip $t1
                        echo "$t1" >> $fn
                    fi
                    
                done <"$file"
                if [ "$s3buck" != "" ]; then
                    ../../scripts/060-get-s3.sh $s3buck
                fi
                if [ "$trole" != "" ]; then
                    ../../scripts/050-get-iam-roles.sh $trole
                fi
                if [ "$kmsarn" != "" ]; then
                    ../../scripts/080-get-kms-key.sh $kmsarn
                fi
                if [ "$cwnam" != "" ]; then
                    echo "get log grp $cwnam"
                    ../../scripts/070-get-cw-log-grp.sh "$cwnam"
                fi

            fi
        done
    fi
done


rm -f t*.txt

