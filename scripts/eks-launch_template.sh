#!/bin/bash
echo "eks-launch-template.sh"
if [ "$1" != "" ]; then
    cmd[0]="$AWS ec2 describe-launch-templates --launch-template-ids $1"
else
    echo "launch template id not set exiting"
    exit
fi
if [ "$1" == "null" ]; then
    echo "passed null lt id - exiting"
    exit
fi
c=0
cm=${cmd[$c]}

pref[0]="LaunchTemplates"
tft[0]="aws_launch_template"
idfilt[0]="LaunchTemplateId"
sgs=()
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
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi
            printf "resource \"%s\" \"%s\" {}" $ttft $cname > $ttft.$cname.tf

            terraform import $ttft.$cname "$cname" | grep Import
            terraform state show  -no-color $ttft.$cname > t1.txt
            rm -f $ttft.$cname.tf

            file="t1.txt"
            $AWS ec2 describe-launch-template-versions --launch-template-id $cname | jq .LaunchTemplateVersions[0].LaunchTemplateData.UserData | tr -d '"' | base64 --decode > $cname.sh
            fn=`printf "%s__%s.tf" $ttft $cname`
            #echo "******* $fn"
            echo $aws2tfmess > $fn
            while IFS= read line
            do
				skip=0
                # display $line or do something with $line
                t1=`echo "$line"` 


                if [[ ${t1} == *"metadata_options"* ]];then 
                        #echo $t1
                        skip=1
                        lbc=0
                        rbc=0
                        breq=0
                        while [[ $breq -eq 0 ]];do 
                            if [[ "${t1}" == *"{"* ]]; then lbc=`expr $lbc + 1`; fi
                            if [[ "${t1}" == *"}"* ]]; then rbc=`expr $rbc + 1`; fi
                            #echo "$lbc $rbc $t1"
                            read line
                            t1=`echo "$line"`
                            if [[ $rbc -eq $lbc ]]; then breq=1; fi
                        done 
                fi



                if [[ ${t1} == *"="* ]];then
                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                    tt2=`echo "$line" | cut -f2- -d'='`
                    if [[ ${tt1} == "arn" ]];then
                        if [[ ${tt2} == *"launch-template"* ]];then
                            skip=1
                        else
                            skip=0; 
                        fi
                    fi                
                    if [[ ${tt1} == "id" ]];then skip=1; fi          
                    if [[ ${tt1} == "role_arn" ]];then skip=1;fi
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    if [[ ${tt1} == "association_id" ]];then skip=1;fi
                    if [[ ${tt1} == "iops" ]];then 
                        iops=`echo $tt2 | tr -d '"'`
                        if [ "$iops" == "0" ];then
                            skip=1;
                        fi
                    fi
                    if [[ ${tt1} == "throughput" ]];then 
                        thpt=`echo $tt2 | tr -d '"'`
                        if [ "$thpt" == "0" ];then
                            skip=1;
                        fi
                    fi

                    #if [[ ${tt1} == "public_dns" ]];then skip=1;fi
                    #if [[ ${tt1} == "private_dns" ]];then skip=1;fi
                    if [[ ${tt1} == "default_version" ]];then skip=1;fi
                    if [[ ${tt1} == "latest_version" ]];then skip=1;fi
                    if [[ ${tt1} == "security_group_names" ]];then skip=1;fi
                    #if [[ ${tt1} == "default_network_acl_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "ipv6_association_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "ipv6_cidr_block" ]];then skip=1;fi
                    if [[ ${tt1} == "subnet_id" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_subnet.%s.id" $tt1 $tt2`
                    fi
                    if [[ ${tt1} == "allocation_id" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_eip.%s.id" $tt1 $tt2`
                    fi

                else
                    if [[ "$t1" == *"sg-"* ]]; then
                        t1=`echo $t1 | tr -d '"|,'`
                        sgs+=$(echo $t1)
                        t1=`printf "aws_security_group.%s.id," $t1`
                     
                    fi
                fi
                
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"

            # get sg's
            for sg in ${sgs[@]}; do
                echo "Getting lt SG $sg"
                ../../scripts/110-get-security-group.sh $sg
            done
            
        done
    fi
done


