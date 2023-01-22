#!/bin/bash

if [ "$1" != "" ]; then
    mkey=`echo "kubernetes.io/cluster/${1}"`
    #echo $mkey
    cmd[0]="$AWS autoscaling describe-auto-scaling-groups | jq '.AutoScalingGroups[] | select(.Tags[].Key==\"${mkey}\").AutoScalingGroupName'"
    
else
    echo "Cluster name not set exiting"
    exit
fi

# check if related to a node group

c=0
cm=${cmd[$c]}
#echo $cm

asgs=`eval $cm`
#echo $asgs
for t in ${asgs[@]}; do
    killer=0
    cname=`echo $t | tr -d '"'`
    #echo "cname=$cname"
    cm=`echo "${AWS} autoscaling describe-auto-scaling-groups --auto-scaling-group-names ${cname}"`

    pref[0]="AutoScalingGroups"
    tft[0]="aws_autoscaling_group"
    idfilt[0]="AutoScalingGroupName"
    rm -f ${tft[(${c})]}.*.tf

    ttft=${tft[(${c})]}

    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    

    echo "$ttft $cname"
    rname=$(echo $cname)
    fn=`printf "%s__%s.tf" $ttft $rname`
    if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi
    printf "resource \"%s\" \"%s\" {}" $ttft $rname > $fn

            
    terraform import $ttft.$rname "$cname" | grep Import
    terraform state show  -no-color $ttft.$rname > t1.txt
    rm -f $fn


    file="t1.txt"
           
    #echo "#" > $fn
    echo $aws2tfmess > $fn
    while IFS= read line
            do
				skip=0
                # display $line or do something with $line
                t1=`echo "$line"` 
                
                if [[ ${t1} == *"="* ]];then
                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                    tt2=`echo "$line" | cut -f2- -d'='`
                    #echo $tt2
                    if [[ ${tt1} == "arn" ]];then
                        if [[ ${tt2} == *"autoscaling"* ]];then
                            skip=1
                            #printf "force_delete= false\n" >> $fn
                            #printf "wait_for_capacity_timeout = \"10m\"\n" >> $fn
                            printf "lifecycle {\n" >> $fn
                            printf "\t ignore_changes = [force_delete,wait_for_capacity_timeout]\n"  >> $fn
                            printf "}\n" >> $fn 
                        else
                            skip=0; 
                        fi
                    fi                
                    if [[ ${tt1} == "id" ]];then skip=1; fi          
                    if [[ ${tt1} == "role_arn" ]];then skip=1;fi
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    if [[ ${tt1} == "association_id" ]];then skip=1;fi

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

                    if [[ ${tt1} == "availability_zones" ]];then 
                        skip=1
                        while [[ "$t1" != "]" ]] ;do
                            read line
                            t1=`echo "$line"`
                            #echo $t1
                        done
                    fi

                    #  hmm needed ?
                    if [[ ${tt2} == *"eks:nodegroup-name"* ]];then 
                        echo " --> $tt2"
                        killer=0
                        #killer=1
                    fi

                #
                else
                    if [[ "$t1" == *"subnet-"* ]]; then
                        t1=`echo $t1 | tr -d '"|,'`
                        t1=`printf "aws_subnet.%s.id," $t1`
                    fi
                #else
                #    if [[ "$t1" == *"sg-"* ]]; then
                #        t1=`echo $t1 | tr -d '"|,'`
                #        t1=`printf "aws_security_group.%s.id," $t1`
                #    fi
                fi
                
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"

        # get the launch template

        if [ "$killer" == "0" ]; then
            echo $awsout | jq .
            ltid=`echo $awsout | jq .AutoScalingGroups[0].LaunchTemplate.LaunchTemplateId | tr -d '"'`
            if [[ $ltid == "null" ]];then
                ltid=`echo $awsout | jq .AutoScalingGroups[0].MixedInstancesPolicy.LaunchTemplate.LaunchTemplateSpecification.LaunchTemplateId | tr -d '"'`
            fi
            echo "--> ltid=$ltid"
            ../../scripts/eks-launch_template.sh $ltid
        else
            rm -f $fn
            terraform state rm $ttft.$cname
        fi
            
done # for t


