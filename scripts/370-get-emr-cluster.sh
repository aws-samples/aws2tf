#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS emr list-clusters --active" 
else
    cmd[0]="$AWS emr list-clusters --active"
fi

pref[0]="Clusters"
tft[0]="aws_emr_cluster"
idfilt[0]="Id"

#rm -f ${tft[0]}.tf

for c in `seq 0 0`; do
    
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
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}" | tr -d '"'`
            echo "$ttft $cname"
            fn=`printf "%s__%s.tf" $ttft $cname`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
            printf "resource \"%s\" \"%s\" {" $ttft $cname > $ttft.$cname.tf
            printf "}" >> $ttft.$cname.tf
            printf "terraform import %s.%s %s" $ttft $cname $cname > data/import_$ttft_$cname.sh
            terraform import $ttft.$cname "$cname" | grep Import
            terraform state show -no-color $ttft.$cname > t1.txt
            tfa=`printf "%s.%s" $ttft $cname`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > data/$tfa.json
            #echo $awsj | jq . 
            rm -f $ttft.$cname.tf

            file="t1.txt"
            iddo=0
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
                    if [[ ${tt1} == "resource_owner" ]];then skip=1;fi
                    if [[ ${tt1} == "cluster_state" ]];then skip=1;fi
                    if [[ ${tt1} == "master_public_dns" ]];then skip=1;fi
                    if [[ ${tt1} == "realm" ]];then 
                        echo "kdc_admin_password = \"CHANGE-ME\"" >> $fn

                    fi
            
                    if [[ ${tt1} == "last_updated_date" ]];then skip=1;fi

                    if [[ ${tt1} == "emr_managed_master_security_group" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_security_group.%s.id" $tt1 $tt2`
                    fi
                    if [[ ${tt1} == "emr_managed_slave_security_group" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_security_group.%s.id" $tt1 $tt2`
                    fi
                    if [[ ${tt1} == "service_access_security_group" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_security_group.%s.id" $tt1 $tt2`
                    fi
                    if [[ ${tt1} == "service_role" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_iam_role.%s.arn" $tt1 $tt2`
                    fi


                    if [[ ${tt1} == "subnet_id" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_subnet.%s.id" $tt1 $tt2`
                    fi


                    if [[ ${tt1} == "vpc_id" ]]; then
                        vpcid=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_vpc.%s.id" $tt1 $vpcid`
                    fi
               
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                    if [[ ${t1} == "resource"* ]];then
                        echo "lifecycle {" >> $fn
                        echo "ignore_changes = [kerberos_attributes[0].kdc_admin_password]" >> $fn
                        echo "}" >> $fn
                    fi
                fi
                
            done <"$file"

            ../../scripts/get-emr-inst-group.sh $cname
            ../../scripts/100-get-vpc.sh $vpcid
            ../../scripts/105-get-subnet.sh $vpcid
            ../../scripts/110-get-security-group.sh $vpcid
            #../../scripts/get-emr-scal-policy.sh $cname

        done

    fi
done

rm -f t*.txt

