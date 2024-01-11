#!/bin/bash
pref[0]="Clusters"
tft[0]="aws_emr_cluster"
idfilt[0]="Id"
if [ "$1" != "" ]; then
    cmd[0]=`printf "$AWS emr list-clusters --active  | jq '.${pref}[] | select(.${idfilt}==\"%s\")' | jq ." $1`
else
    cmd[0]="$AWS emr list-clusters --active"
fi


for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    if [[ $1 != "" ]]; then
        count=1
    else
        count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    fi
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            if [ "$1" != "" ]; then
                cname=`echo $awsout | jq ".${idfilt[(${c})]}" | tr -d '"'`
            else
                cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}" | tr -d '"'`
            fi
            echo "$ttft $cname"
            fn=`printf "%s__%s.tf" $ttft $cname`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
            printf "resource \"%s\" \"%s\" {}\n" $ttft $cname > $fn

            terraform import $ttft.$cname "$cname" | grep Importing
            terraform state show -no-color $ttft.$cname > t1.txt
            tfa=`printf "%s.%s" $ttft $cname`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > data/$tfa.json
            #echo $awsj | jq . 
            rm -f $fn
            

            file="t1.txt"
            iddo=0
            subnets=()
            sgs=()
            donesub=0
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
                    if [[ ${tt1} == "security_configuration" ]];then
                        scon=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_emr_security_configuration.%s.id" $tt1 $scon`
                    fi
                    if [[ ${tt1} == "master_public_dns" ]];then skip=1;fi
                    if [[ ${tt1} == "realm" ]];then 
                        echo "kdc_admin_password = \"CHANGE-ME\"" >> $fn

                    fi
            
                    if [[ ${tt1} == "last_updated_date" ]];then 
                        printf "lifecycle {\n" >> $fn
                        printf "   ignore_changes = [security_configuration]\n" >> $fn
                        printf "}\n" >> $fn
                        skip=1
                    fi

                    if [[ ${tt1} == "emr_managed_master_security_group" ]]; then
                        mmsg=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_security_group.%s.id" $tt1 $mmsg`
                    fi
                    if [[ ${tt1} == "emr_managed_slave_security_group" ]]; then
                        mssg=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_security_group.%s.id" $tt1 $mssg`
                    fi
                    if [[ ${tt1} == "service_access_security_group" ]]; then
                        sasg=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_security_group.%s.id" $tt1 $sasg`
                    fi
                    if [[ ${tt1} == "service_role" ]]; then
                        srvrole=`echo $tt2 | tr -d '"'`
          
                        t1=`printf "%s = aws_iam_role.r-%s.name" $tt1 ${srvrole//./_}`
                    fi

                    #if [[ ${tt1} == "autoscaling_role" ]]; then
                    #    asrole=`echo $tt2 | tr -d '"'`
                    #    t1=`printf "%s = aws_iam_role.r-%s.arn" $tt1 $asrole`
                    #fi

                    if [[ ${tt1} == "instance_profile" ]]; then
                        instp=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_iam_instance_profile.%s.name" $tt1 $instp`
                    fi


                    if [[ ${tt1} == "subnet_id" ]]; then
                        subid=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_subnet.%s.id" $tt1 $subid`
                        donesub=1
                    fi

                    if [[ ${tt1} == "subnet_ids" ]]; then
                  
                        if [[ $donesub == "1" ]];then
                            # skip the block 
                            tt2=`echo $tt2 | tr -d '"'` 
                            skip=1
                            while [ "$t1" != "]" ] && [ "$tt2" != "[]" ] ;do
                                read line
                                t1=`echo "$line"`
                              
                            done
                        fi
                    fi




                    if [[ ${tt1} == "vpc_id" ]]; then
                        vpcid=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_vpc.%s.id" $tt1 $vpcid`
                    fi
                else
                    if [[ "$t1" == *"subnet-"* ]]; then
                        t1=`echo $t1 | tr -d '"|,'`
                        subnets+=`printf "\"%s\" " $t1`
                        t1=`printf "aws_subnet.%s.id," $t1`
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
            
            if [[ $vpcid != "" ]];then
                ../../scripts/100-get-vpc.sh $vpcid
            fi
  
            for sub in ${subnets[@]}; do
                sub1=`echo $sub | tr -d '"'`
                if [ "$sub1" != "" ]; then
                    ../../scripts/105-get-subnet.sh $sub1
                fi
            done

            if [[ $subid != "" ]];then
                ../../scripts/105-get-subnet.sh $subid
            fi

            if [[ $mmsg != "" ]];then
                ../../scripts/110-get-security-group.sh $mmsg
            fi
            if [[ $mmsg != "" ]];then
                ../../scripts/110-get-security-group.sh $mssg
            fi
            if [[ $sasg != "" ]];then
                ../../scripts/110-get-security-group.sh $sasg
            fi

            if [[ $scon != "" ]];then
                ../../scripts/371-get-emr-sec-config.sh $scon
            fi

            if [[ $srvrole != "" ]];then
                ../../scripts/050-get-iam-roles.sh $srvrole
            fi

            if [[ $asrole != "" ]];then
                echo "-4- $asrole"
                ../../scripts/050-get-iam-roles.sh $asrole
            fi

            if [[ $instp != "" ]];then
                ../../scripts/056-get-iam-instance-profile.sh $instp
            fi

       
        done

    fi
done

rm -f t*.txt

