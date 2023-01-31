#!/bin/bash
cmd[0]="$AWS rds describe-db-instances"
pref[0]="DBInstances"
tft[0]="aws_db_instance"
if [ "$1" != "" ]; then
    cmd[0]="$AWS rds describe-db-instances --db-instance-identifier $1"
fi

for c in `seq 0 0`; do
   
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm
    awsout=`eval $cm 2> /dev/null`
    #echo $awsout | jq .
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    awsout=`echo $awsout | jq "select(.${pref[(${c})]}[].StorageType != \"aurora\")"`
    #echo $awsout | jq .
    
    if [ "$awsout" == "" ];then
        echo "No resources found exiting .."
        exit
    fi
    

    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    echo $count
    
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].DBInstanceIdentifier" | tr -d '"'`
            echo "$ttft $cname"
            fn=`printf "%s__%s.tf" $ttft $cname`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi


            printf "resource \"%s\" \"%s\" {}\n" $ttft $cname > $fn
   
            terraform import $ttft.$cname "$cname" | grep Import
            terraform state show -no-color $ttft.$cname > t1.txt
            rm -f $fn

            file="t1.txt"

            echo $aws2tfmess > $fn
            sgs=()
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
                    if [[ ${tt1} == "availability_zone" ]];then skip=1;fi
                    if [[ ${tt1} == "endpoint" ]];then skip=1;fi
                    if [[ ${tt1} == "replicas" ]];then 
                        tt2=`echo $tt2 | tr -d '"'` 
                        skip=1
                        while [ "$t1" != "]" ] && [ "$tt2" != "[]" ] ;do
                            read line
                            t1=`echo "$line"`
                            #echo $t1
                        done
                    fi
                    if [[ ${tt1} == "address" ]];then skip=1;fi
                    if [[ ${tt1} == "hosted_zone_id" ]];then skip=1;fi
                    if [[ ${tt1} == "status" ]];then skip=1;fi
                    if [[ ${tt1} == "resource_id" ]];then skip=1;fi
                    if [[ ${tt1} == "latest_restorable_time" ]];then skip=1;fi
                    if [[ ${tt1} == "engine_version_actual" ]];then skip=1;fi

                    #if [[ ${tt1} == "db_parameter_group_name" ]];then
                    #    paramid=`echo $tt2 | tr -d '"'`
                    #    t1=`printf "%s =  aws_db_parameter_group.%s.name" $tt1 $paramid`
                    #fi


                    if [[ ${tt1} == "db_subnet_group_name" ]];then 
                        dbsn=`echo $tt2 | tr -d '"'` 
                        t1=`printf "%s = aws_db_subnet_group.%s.name" $tt1 $dbsn`
                    fi

                    if [[ ${tt1} == "monitoring_role_arn" ]]; then
                        tarn=`echo $tt2 | tr -d '"'`
                        tanam=$(echo $tarn | rev | cut -f1 -d'/' | rev)
                        tlarn=${tarn//:/_} && tlarn=${tlarn//./_} && tlarn=${tlarn//\//_}
                        t1=`printf "%s = aws_iam_role.%s.arn" $tt1 $tanam`
                    fi 


                    if [[ ${tt1} == "kms_key_id" ]];then 
                        kid=`echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"'`                            
                        kmsarn=$(echo $tt2 | tr -d '"')
                        km=`$AWS kms describe-key --key-id $kid --query KeyMetadata.KeyManager | jq -r '.' 2>/dev/null`
                            #echo $t1
                        if [[ $km == "AWS" ]];then
                            t1=`printf "%s = data.aws_kms_key.k_%s.arn" $tt1 $kid`
                        else
                            t1=`printf "%s = aws_kms_key.k_%s.arn" $tt1 $kid`
                        fi 
                                           
                    fi

                    if [[ ${tt1} == "performance_insights_kms_key_id" ]];then 
                        pkid=`echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"'`                            
                        pkmsarn=$(echo $tt2 | tr -d '"')
                        km=`$AWS kms describe-key --key-id $pkid --query KeyMetadata.KeyManager | jq -r '.' 2>/dev/null`
                        if [[ $km == "AWS" ]];then
                            t1=`printf "%s = data.aws_kms_key.k_%s.arn" $tt1 $pkid`
                        else
                            t1=`printf "%s = aws_kms_key.k_%s.arn" $tt1 $pkid`
                        fi 
                 
                    fi
              
                else
                    if [[ "$t1" == *"sg-"* ]]; then
                        t1=`echo $t1 | tr -d '"|,'`
                        sgs+=`printf "\"%s\" " $t1`
                        t1=`printf "aws_security_group.%s.id," $t1`
                    fi               
                
                fi



                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"


            for sg in ${sgs[@]}; do
                #echo "therole=$therole"
                sg1=`echo $sg | tr -d '"'`
                echo "calling for $sg1"
                if [ "$sg1" != "" ]; then
                    ../../scripts/110-get-security-group.sh $sg1
                fi
            done 

            if [ "$tarn" != "" ]; then
                echo "getting role $tarn"
                ../../scripts/050-get-iam-roles.sh $tarn
            fi           

            if [ "$kmsarn" != "" ]; then
                echo "getting key $kid"
                ../../scripts/080-get-kms-key.sh $kid
            fi

            if [ "$pkmsarn" != "" ]; then
                echo "getting key $pkid"
                ../../scripts/080-get-kms-key.sh $pkid
            fi

            if [ "$dbsn" != "" ]; then
                echo "getting db subnet group $dbsn"
                ../../scripts/get-rds-db-subnet-group.sh $dbsn
                if [[ $? -eq 199 ]];then
                        echo "WARNING: Problems in dependant db subnet group $dbsn"
                        echo "Removing $ttft $cname resources to prevent validation errors"
                        rm -f $fn
                        terraform state rm $ttft.${cname}
                        exit
                    fi
            fi

            
        done
    fi
done

rm -f t*.txt

