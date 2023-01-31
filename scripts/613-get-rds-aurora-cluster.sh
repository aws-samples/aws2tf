#!/bin/bash
cmd[0]="$AWS rds describe-db-clusters"
pref[0]="DBClusters"
tft[0]="aws_rds_cluster"


for c in `seq 0 0`; do

    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	echo $cm
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
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].DBClusterIdentifier" | tr -d '"'`
            echo "$ttft $cname"
            printf "resource \"%s\" \"%s\" {}\n" $ttft $cname > $ttft.$cname.tf
  
            terraform import $ttft.$cname "$cname" | grep Import
            terraform state show -no-color $ttft.$cname > t1.txt
            rm -f $ttft.$cname.tf

            file="t1.txt"
            fn=`printf "%s__%s.tf" $ttft $cname`
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
                    if [[ ${tt1} == "cluster_identifier" ]];then skip=1;fi
                    if [[ ${tt1} == "cluster_resource_id" ]];then skip=1;fi
                    if [[ ${tt1} == "endpoint" ]];then skip=1;fi
                    if [[ ${tt1} == "reader_endpoint" ]];then skip=1;fi
                    if [[ ${tt1} == "address" ]];then skip=1;fi
                    if [[ ${tt1} == "dbi_resource_id" ]];then skip=1;fi
                    if [[ ${tt1} == "engine_version_actual" ]];then skip=1;fi
                    if [[ ${tt1} == "hosted_zone_id" ]];then skip=1;fi
                    if [[ ${tt1} == "network_type" ]];then skip=1;fi

                    if [[ ${tt1} == "db_subnet_group_name" ]];then
                        dbsn=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_db_subnet_group.%s.name" $tt1 $dbsn`
                    fi

                    #if [[ ${tt1} == "db_cluster_parameter_group_name" ]];then
                    #    paramid=`echo $tt2 | tr -d '"'`
                    #    t1=`printf "%s = aws_rds_cluster_parameter_group.%s.name" $tt1 $paramid`
                    #fi

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

