#!/bin/bash
issingle=0
if [ "$1" != "" ]; then
    if [[ "$1" == "vpc-"* ]];then
        cmd[0]="$AWS ec2 describe-instances --filters \"Name=vpc-id,Values=$1\" \"Name=instance-state-name,Values=running,stopped\""
    fi
    if [[ "$1" == "i-"* ]];then
        cmd[0]="$AWS ec2 describe-instances --instance-ids $1 --filters \"Name=instance-state-name,Values=running,stopped\""
        issingle=1
    fi


else
    cmd[0]="$AWS ec2 describe-instances --filters \"Name=instance-state-name,Values=running\""
fi

cloud9s=`$AWS ec2 describe-instances --filters "Name=tag-key,Values=aws:cloud9*" | jq .Reservations[].Instances[].InstanceId`
asis=`$AWS ec2 describe-instances --filters "Name=tag-key,Values=aws:autoscaling*" | jq .Reservations[].Instances[].InstanceId`

pref[0]="Reservations"
tft[0]="aws_instance"

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
    #echo "count= $count"
    if [ "$count" != "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo "i=$i"
            skipit=0
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].Instances[].InstanceId" | tr -d '"'`
            echo "$ttft $cname"
            ivpc=`echo $awsout | jq ".${pref[(${c})]}[(${i})].Instances[].VpcId" | tr -d '"'`
            for ci in `echo $cloud9s`;do
                c9=`echo $ci | tr -d '"'`
                if [ "$c9" == "$cname" ]; then
                    #if [ "$issingle" == "0" ];then
                        echo "Instance is cloud9 skipping ....."
                        skipit=1
                    #fi
                fi
            done
            for ci in `echo $asis`;do
                c9=`echo $ci | tr -d '"'`
                if [ "$c9" == "$cname" ]; then
                    echo "Instance is Autoscaling skipping ....."
                    skipit=1
                fi
            done
            if [[ $skipit -eq 1 ]];then
                echo "breaking ..."
                continue 
            fi


            # get instance user_data

            ud=`$AWS ec2 describe-instance-attribute --instance-id $cname --attribute userData | jq .UserData.Value`
            #echo "user_date=$ud"
            $AWS ec2 describe-instance-attribute --instance-id $cname --attribute userData | jq .UserData.Value | tr -d '"' | base64 --decode > $cname.sh

            nets=`echo $awsout | jq ".${pref[(${c})]}[(${i})].Instances[].NetworkInterfaces"`
            
            fn=`printf "%s__%s.tf" $ttft $cname`
            echo $aws2tfmess > $fn
            printf "resource \"%s\" \"%s\" {" $ttft $cname > $ttft.$cname.tf
            printf "}" >> $ttft.$cname.tf
            terraform import $ttft.$cname "$cname" | grep Import
            terraform state show -no-color $ttft.$cname > t1.txt
            rm -f $ttft.$cname.tf

            ebs=0
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
                         
                    if [[ ${tt1} == "user_data" ]];then 
                        skip=0
                        printf "lifecycle {\n" >> $fn
                        printf "   ignore_changes = [user_data,user_data_base64]\n" >> $fn
                        printf "}\n" >> $fn
                        
                        if [[ -f ${cname}.sh ]];then 
                            #echo "user data via file ${cname}.sh"
                            t1=`printf "user_data_base64 = filebase64sha256(\"%s.sh\")" $cname`
                        else
                            t1=`printf "user_data_base64 = %s" $ud`
                        fi
                    fi          
                    if [[ ${tt1} == "role_arn" ]];then skip=1;fi
                    if [[ ${tt1} == "primary_network_interface_id" ]];then skip=1;fi
                    if [[ ${tt1} == "instance_state" ]];then skip=1;fi
                    if [[ ${tt1} == "private_dns" ]];then skip=1;fi

                    if [[ ${tt1} == "volume_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "user_data" ]];then 
                    #    t1=`printf "%s = file(\"%s.sh\")" $tt1 $cname`
                    #fi
                    # These are rarely used
                    if [[ ${tt1} == "cpu_core_count" ]];then skip=1;fi
                    if [[ ${tt1} == "cpu_threads_per_core" ]];then skip=1;fi

                    if [[ ${tt1} == "private_ip" ]];then skip=1;fi
                    if [[ ${tt1} == "public_ip" ]];then skip=1;fi
                    if [[ ${tt1} == "public_dns" ]];then skip=1;fi

                    if [[ ${tt1} == "ipv6_address_count" ]];then
                        tt2=`echo $tt2 | tr -d '"'`
                        if [[ "${tt2}" == "0" ]];then skip=1; fi
                    fi
                    if [[ ${tt1} == "ipv6_addresses" ]];then

                        tt2=`echo $tt2 | tr -d '"'`
                        
                        if [[ "${tt2}" == "[]" ]];then 
                            skip=1
                        else
                                    skip=1
                                    lbc=0
                                    rbc=0
                                    breq=0
                                    dosse=1
                                    while [[ $breq -eq 0 ]];do 
                                        if [[ "${t1}" == *"["* ]]; then lbc=`expr $lbc + 1`; fi
                                        if [[ "${t1}" == *"]"* ]]; then rbc=`expr $rbc + 1`; fi
                                        #echo "op=$lbc $rbc $t1"
                                        if [[ $rbc -eq $lbc ]]; then 
                                            breq=1; 
                                        else
                                            read line
                                            t1=`echo "$line"`


                                        fi
                                    done
                        fi

                        
                    fi

                    
                    if [[ ${tt1} == "device_name" ]];then 
                        if [ ${ebs} == "0" ]; then
                            skip=1;
                        fi
                    fi

                    if [[ ${tt1} == "iam_instance_profile" ]];then
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_iam_instance_profile.%s.id" $tt1 $tt2`
                    fi


                    #if [[ ${tt1} == "ipv6_association_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "ipv6_cidr_block" ]];then skip=1;fi    
                    if [[ ${tt1} == "subnet_id" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_subnet.%s.id" $tt1 $tt2`
                    fi  
                    if [[ ${tt1} == "kms_key_id" ]]; then
                        tt2=`echo $tt2 | cut -f2 -d'/' | tr -d '"'`
                        t1=`printf "%s = data.aws_kms_key.k_%s.arn" $tt1 $tt2`
                    fi   

                else

                    if [[ "$t1" == *"sg-"* ]]; then
                        t1=`echo $t1 | tr -d '"|,'`
                        t1=`printf "aws_security_group.%s.id," $t1`
                    fi
                    if [[ "$t1" == *"ebs_block_device"* ]]; then
                        ebs=1
                    fi
                    if [[ "$t1" == *"root_block_device"* ]]; then
                        ebs=0
                    fi
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"
            pfnm=`echo $awsout | jq ".${pref[(${c})]}[(${i})].Instances[].IamInstanceProfile.Arn" | cut -f2 -d'/' | tr -d '"'`
            #echo "------ $pfnm -------"
            ../../scripts/get-inprof.sh $pfnm

            ## need the vpc
            #../../aws2tf.sh -t vpc -i $ivpc -c yes

            ../../scripts/100-get-vpc.sh $ivpc
            ../../scripts/105-get-subnet.sh $ivpc
            ../../scripts/110-get-security-group.sh $ivpc

            #for com in `ls ../../scripts/1*.sh`; do
            #    comd=`printf "%s %s" $com $ivpc`
            #    echo $comd
            #    eval $comd
            #done


            nl=`echo $nets | jq ". | length"`
            #echo "netifs= $nl"
            # don't get primary (0) interface as created by instance
            if [ $nl -gt 1 ]; then
                nl=`expr $nl - 1`
                for ni in `seq 1 $nl`; do
                    nif=`echo $nets | jq ".[(${ni})].NetworkInterfaceId" | tr -d '"'`
                    echo $ni $nif
                    ../../scripts/get-eni.sh $nif
                    #../../scripts/get-instance-network-interface-attachment.sh $nif
                done
            fi
            
        done
    else
        echo "*** Found $count running instances skipping... ***"
    fi
done

rm -f t*.txt

