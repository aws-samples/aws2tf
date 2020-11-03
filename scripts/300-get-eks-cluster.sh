#!/bin/bash
echo $AWS $1
pref[0]="cluster"
tft[0]="aws_eks_cluster"

c=0
if [ "$1" != "" ]; then
    kcount=1
else
    kcount=`$AWS eks list-clusters | jq ".clusters | length"`
fi

if [ "$kcount" -gt "0" ]; then
    kcount=`expr $kcount - 1`
    for k in `seq 0 $kcount`; do
        if [ "$1" != "" ]; then
            cln=`echo $1`
        else
            cln=`$AWS eks list-clusters  | jq ".clusters[(${k})]" | tr -d '"'`         
        fi
        echo cluster name $cln  
         
        cmd[0]=`echo "$AWS eks describe-cluster --name $cln"` 
        cm=${cmd[$c]}
        awsout=`eval $cm`
            
        tcmd=`echo $awsout | jq ".${pref[(${c})]}.resourcesVpcConfig.vpcId" | tr -d '"'`
        ../../scripts/100* $tcmd  # vpc
        ../../scripts/101* $tcmd  # vpc cidrs
        ../../scripts/105* $tcmd  # subnets
            ## EKS creates it's own SG's - no it doesn't
        ../../scripts/110*.sh $tcmd  # security groups
            
            # don't keep eni's - created by nat gw and node group instances
            # still need to call as eip is nested from eni's

        rm -f aws_network_interface*.tf
            # need to rip out eni state
        terraform state list | grep aws_network_interface > tf2.tmp
        for ts in `cat tf2.tmp` ; do
            terraform state rm $ts > t2.txt
        done
        
        
            
            ## this needs to loop !!
            ## this is now done in NatGW code 
            #natgw=`$AWS ec2 describe-nat-gateways --filter "Name=vpc-id,Values=${tcmd}"
            #cnatgw=`echo $natgw | jq ".NatGateways | length"`
            #echo "found $cnatgw NAT GW's"
            #if [ "$cnatgw" -gt "0" ]; then
            #    np=`expr $cnatgw - 1`
            #    for g in `seq 0 $cnatgw`; do
            #        eipall=`echo $natgw | jq ".NatGateways[(${g})].NatGatewayAddresses[0].AllocationId" | tr -d '"'`
            #        ../../scripts/get-eip.sh $eipall         
            #    done
            #fi
   

        ../../scripts/120*.sh $tcmd  # igw
        ../../scripts/130*.sh $tcmd  # nat gw
            # still need to call as eip is nested from nat gw
        ../../scripts/135*.sh $tcmd  # TGW

            ## need these or will it do it's own ?
        ../../scripts/140*.sh $tcmd  # route table
        ../../scripts/141*.sh $tcmd  # route table assoc
        ../../scripts/161*.sh $tcmd  # vpce

        rarn=`echo $awsout | jq ".${pref[(${c})]}.roleArn" | tr -d '"'`
        #echo "rarn=$rarn"
        ../../scripts/050-get-iam-roles.sh $rarn
        csg=`echo $awsout | jq ".${pref[(${c})]}.resourcesVpcConfig.clusterSecurityGroupId" | tr -d '"'`
            #../../scripts/103-get-security_group.sh $csg

        sgs=`echo $awsout | jq ".${pref[(${c})]}.resourcesVpcConfig.securityGroupIds[]" | tr -d '"'`
        for s1 in `echo $sgs` ; do
            echo $s1
                #../../scripts/103-get-security_group.sh $s1
        done

        fgp=`$AWS eks list-fargate-profiles --cluster-name $cln`
        #echo "fgp=${fgp}"
        if [ "$fgp" != "" ]; then
            np=`echo $fgp | jq ".fargateProfileNames | length"`
            if [ "$np" -gt "0" ]; then
                np=`expr $np - 1`
                for p in `seq 0 $np`; do
                    pname=`echo $fgp | jq ".fargateProfileNames[(${p})]" | tr -d '"'`
                    echo "faregate profile = $pname"
                    fg=`$AWS eks describe-fargate-profile --cluster-name $cln --fargate-profile-name $pname`
                    echo "fargate"
                    fgparn=`echo $fg | jq ".fargateProfile.fargateProfileArn" | tr -d '"'`
                    podarn=`echo $fg | jq ".fargateProfile.podExecutionRoleArn" | tr -d '"'`
                    echo "Fargate profile arn = $fgparn" 
                    echo "Get Fargate Pod execution role arn = $podarn" 
                    ../../scripts/050-get-iam-roles.sh $podarn

                    # Get the fargate profile
                    #../../scripts/fargate_profile.sh $cname


                done # end for p
            fi
        fi      

        echo "pre-reqs complete - getting EKS"
              
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

                    printf "resource \"%s\" \"%s\" {" $ttft $cname > $ttft.$cname.tf
                    printf "}" >> $ttft.$cname.tf
                    terraform import $ttft.$cname $ocname
                    terraform state show $ttft.$cname > t2.txt
                    tfa=`printf "%s.%s" $ttft $cname`
                    terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > $tfa.json
                    #cat $tfa.json | jq .
       
                    rm $ttft.$cname.tf
                    cat t2.txt | perl -pe 's/\x1b.*?[mGKH]//g' > t1.txt
                    #	for k in `cat t1.txt`; do
                    #		echo $k
                    #	done
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
                            if [[ ${tt1} == *":"* ]];then
                                t1=`printf "\"%s\"=%s" $tt1 $tt2`
                            fi
                            #if [[ ${tt1} == "endpoint_public_access" ]];then
                            #    # must start public and flick over
                            #    t1=`printf "\"%s\"= false" $tt1`
                            #fi


                            if [[ ${tt1} == "arn" ]];then skip=1; fi
                            if [[ ${tt1} == "id" ]];then skip=1; fi
                            if [[ ${tt1} == "role_arn" ]];then 
                                skip=0;
                                trole=`echo "$tt2" | cut -f2- -d'/' | tr -d '"'`
                                echo "depends_on = [aws_iam_role.$trole]" >> $fn              
                                t1=`printf "%s = aws_iam_role.%s.arn" $tt1 $trole`
                            fi
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

                    # Get the fargate profile
                    ../../scripts/fargate_profile.sh $cname


                done # done for i
            fi
        done # done for c
    # address supporting eks cluster resources

    ../../scripts/get-eks-cluster-nodegroups.sh $cln
    
    done  # k  
fi

#### potfix private net
####  endpoint_public_access  = true



echo "fmt"
terraform fmt
echo "validate"
terraform validate
rm -f t*.txt
echo "run command ....."
echo "$AWS eks update-kubeconfig --name $cname"







