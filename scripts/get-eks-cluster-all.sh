#!/bin/bash
pref[0]="cluster"
tft[0]="aws_eks_cluster"
echo $1
c=0
kcount=`$AWS eks list-clusters | jq ".clusters | length"`
if [ "$kcount" -gt "0" ]; then
    kcount=`expr $kcount - 1`
    for k in `seq 0 $kcount`; do
        cln=`$AWS eks list-clusters  | jq ".clusters[(${k})]" | tr -d '"'`
        echo cluster name $cln        
        cmd[0]=`echo "$AWS eks describe-cluster --name $cln"` 
        cm=${cmd[$c]}
        awsout=`eval $cm`
        
        if [ "$1" != "" ]; then
            echo "get other stuff"
            tcmd=`echo $awsout | jq ".${pref[(${c})]}.resourcesVpcConfig.vpcId" | tr -d '"'`
            ../../scripts/100-get-vpc.sh $tcmd
            ../../scripts/102-get-subnet.sh $tcmd
            #
            ../../scripts/130-get-igw.sh $tcmd
            #
            ../../scripts/120-get-route-table.sh $tcmd
            ../../scripts/121-get-route-table-associations.sh $tcmd
            #
            ../../scripts/140-get-natgw.sh $tcmd
            #../../scripts/115-get-security_group.sh $tcmd

            rarn=`echo $awsout | jq ".${pref[(${c})]}.roleArn" | tr -d '"'`
            echo $rarn
            ../../scripts/050-get-iam-roles.sh $rarn
            csg=`echo $awsout | jq ".${pref[(${c})]}.resourcesVpcConfig.clusterSecurityGroupId" | tr -d '"'`
            ../../scripts/103-get-security_group.sh $csg

            sgs=`echo $awsout | jq ".${pref[(${c})]}.resourcesVpcConfig.securityGroupIds[]" | tr -d '"'`
            for s1 in `echo $sgs` ; do
                echo $s1
                ../../scripts/103-get-security_group.sh $s1
            done


        
        fi

              
        for c in `seq 0 0`; do
            
            cm=${cmd[$c]}
            ttft=${tft[(${c})]}
            echo $cm
            awsout=`eval $cm`
            count=`echo $awsout | jq ".${pref[(${c})]} | length"`
            count=1 # one cluster at a time !
            if [ "$count" -gt "0" ]; then
                count=`expr $count - 1`
                for i in `seq 0 $count`; do
                    #echo $i
                    cname=`echo $awsout | jq ".${pref[(${c})]}.name" | tr -d '"'`
                    ocname=`echo $cname`
                    cname=${cname//./_}
                    echo cname = $cname

                    printf "data \"%s\" \"%s\" {\n" $ttft $cname > data-$ttft.$cname.tf
                    printf "name=\"%s\"\n" $ocname >> data-$ttft.$cname.tf
                    printf "}\n" >> data-$ttft.$cname.tf

                    printf "data \"%s_auth\" \"%s\" {\n" $ttft $cname >> data-$ttft.$cname.tf
                    printf "name=\"%s\"\n" $ocname >> data-$ttft.$cname.tf
                    printf "}\n" >> data-$ttft.$cname.tf

                    printf "output \"%s_%s_role_arn\" {\n" $ttft $cname >> data-$ttft.$cname.tf
                    printf "\t value = data.aws_eks_cluster.%s.role_arn\n" $cname >> data-$ttft.$cname.tf
                    printf "}\n" >> data-$ttft.$cname.tf


                    printf "output \"%s_%s_endpoint\" {\n" $ttft $cname >> data-$ttft.$cname.tf
                    printf "\t value = data.aws_eks_cluster.%s.endpoint\n" $cname >> data-$ttft.$cname.tf
                    printf "}\n" >> data-$ttft.$cname.tf   

                    printf "output \"%s_%s_cluster_security_group_id\" {\n" $ttft $cname >> data-$ttft.$cname.tf
                    printf "\t value = data.aws_eks_cluster.%s.vpc_config.0.cluster_security_group_id\n" $cname >> data-$ttft.$cname.tf
                    printf "}\n" >> data-$ttft.$cname.tf

                    printf "output \"%s_%s_security_group_ids\" {\n" $ttft $cname >> data-$ttft.$cname.tf
                    printf "\t value = data.aws_eks_cluster.%s.vpc_config.0.security_group_ids\n" $cname >> data-$ttft.$cname.tf
                    printf "}\n" >> data-$ttft.$cname.tf

                    printf "output \"%s_%s_subnet_ids\" {\n" $ttft $cname >> data-$ttft.$cname.tf
                    printf "\t value = data.aws_eks_cluster.%s.vpc_config.0.subnet_ids\n" $cname >> data-$ttft.$cname.tf
                    printf "}\n" >> data-$ttft.$cname.tf

                    printf "output \"%s_%s_vpc_id\" {\n" $ttft $cname >> data-$ttft.$cname.tf
                    printf "\t value = data.aws_eks_cluster.%s.vpc_config.0.vpc_id\n" $cname >> data-$ttft.$cname.tf
                    printf "}\n" >> data-$ttft.$cname.tf

                    printf "resource \"%s\" \"%s\" {" $ttft $cname > $ttft.$cname.tf
                    printf "}" >> $ttft.$cname.tf
                    terraform import $ttft.$cname $ocname
                    terraform state show $ttft.$cname > t2.txt
                    rm $ttft.$cname.tf
                    cat t2.txt | perl -pe 's/\x1b.*?[mGKH]//g' > t1.txt
                    #	for k in `cat t1.txt`; do
                    #		echo $k
                    #	done
                    file="t1.txt"
                    fn=`printf "%s__%s.tf" $ttft $cname`
                    while IFS= read line
                    do
                        skip=0
                        # display $line or do something with $line
                        t1=`echo "$line"`
                        if [[ ${t1} == *"="* ]];then
                            tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '`
                            tt2=`echo "$line" | cut -f2- -d'='`
                            if [[ ${tt1} == *":"* ]];then
                                t1=`printf "\"%s\"=%s" $tt1 $tt2`
                            fi
                            if [[ ${tt1} == "arn" ]];then skip=1; fi
                            if [[ ${tt1} == "id" ]];then skip=1; fi
                            #if [[ ${tt1} == "role_arn" ]];then skip=1;fi
                            if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                            if [[ ${tt1} == "association_id" ]];then skip=1;fi
                            if [[ ${tt1} == "unique_id" ]];then skip=1;fi
                            if [[ ${tt1} == "create_date" ]];then skip=1;fi
                            if [[ ${tt1} == "certificate_authority" ]];then 
                            # skip the block
                                SL= read line
                                echo $SL
                                read line
                                read line
                                read line
                                skip=1
                            fi
                            if [[ ${tt1} == "private_ip" ]];then skip=1;fi
                            if [[ ${tt1} == "accept_status" ]];then skip=1;fi
                            if [[ ${tt1} == "created_at" ]];then skip=1;fi
                            if [[ ${tt1} == "endpoint" ]];then skip=1;fi
                            if [[ ${tt1} == "status" ]];then skip=1;fi
                            if [[ ${tt1} == "identity" ]];then 
                                skip=1
                                read line
                                read line
                                read line
                                read line
                                read line
                                read line
                                read line
                                read line
                            
                            fi
                            if [[ ${tt1} == "platform_version" ]];then skip=1;fi
                            if [[ ${tt1} == "vpc_id" ]];then skip=1;fi
                            if [[ ${tt1} == "cluster_security_group_id" ]];then skip=1;fi
                            if [[ ${tt1} == "platform_version" ]];then skip=1;fi
                        else
                            if [[ "$t1" == *"subnet-"* ]]; then
                                t1=`echo $t1 | tr -d '"|,'`
                                t1=`printf "aws_subnet.%s.id," $t1`
                            fi
                            if [[ "$t1" == *"sg-"* ]]; then
                                t1=`echo $t1 | tr -d '"|,'`
                                t1=`printf "aws_security_group.%s.id," $t1`
                            fi
                        fi
                        
                        if [ "$skip" == "0" ]; then
                            #echo $skip $t1
                            echo $t1 >> $fn
                        fi
                        
                    done <"$file"   # done while
                    
                done # done for i
            fi
        done 
        # address supporting eks cluster resources
        echo "fmt"
        terraform fmt
        echo "validate"
        terraform validate
        
    done  # k  
fi







