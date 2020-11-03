#!/bin/bash
echo $AWS
if [ "$1" != "" ]; then
    kcount=1
else
    kcount=`$AWS eks list-clusters | jq ".clusters | length"`
fi

if [ "$kcount" -gt "0" ]; then
    kcount=`expr $kcount - 1`
    #echo kcount=$kcount
    for k in `seq 0 $kcount`; do
        #echo "***k=$k"
        
        if [ "$1" != "" ]; then
            cln=`echo $1`
        else
            cln=`$AWS eks list-clusters  | jq ".clusters[(${k})]" | tr -d '"'`      
        fi
                
        echo cluster name $cln
        cname=`echo $cln`

        jcount=`$AWS eks list-nodegroups --cluster-name $cln | jq ".nodegroups | length"`
        
        echo jcount=$jcount
        if [ "$jcount" -gt "0" ]; then
            jcount=`expr $jcount - 1`
            for j in `seq 0 $jcount`; do
                ng=`$AWS eks list-nodegroups --cluster-name $cln   | jq ".nodegroups[(${j})]" | tr -d '"'`     
                echo "***** node group = $ng"
                cmd[0]=`echo "$AWS eks describe-nodegroup --cluster-name $cln --nodegroup-name $ng"`      
                pref[0]="nodegroup"
                tft[0]="aws_eks_node_group"
                rm -f ${tft[0]}_*.tf
        
                for c in `seq 0 0`; do
                    rm -f ${tft[0]}*.tf
                    cm=${cmd[$c]}
                    ttft=${tft[(${c})]}
                    echo "inner command=$cm"
                    awsout=`eval $cm`
                    #echo awsout
                    #echo $awsout | jq .
                    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
                    count=1 # one cluster at a time !
                    if [ "$count" -gt "0" ]; then
                        count=`expr $count - 1`
                        for i in `seq 0 $count`; do
                            echo $i
                            cname=`echo $awsout | jq ".${pref[(${c})]}.clusterName" | tr -d '"'`
                            ngnam=`echo $awsout | jq ".${pref[(${c})]}.nodegroupName" | tr -d '"'`
                            ocname=`printf "%s:%s" $cname $ngnam`

                            cname=${ocname//:/_}
                            echo cname = $cname

                            printf "resource \"%s\" \"%s\" {" $ttft $cname > $ttft.$cname.tf
                            printf "}" >> $ttft.$cname.tf
                            #echo "pre-import"
                            #ls -l
                            echo "Importing ....."
                            terraform import $ttft.$cname $ocname
                            terraform state show $ttft.$cname > t2.txt
                            tfa=`printf "%s.%s" $ttft $cname`
                            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > $tfa.json
                            echo $tfa.json | jq .
                  
                            #ls -l *.tf
                            rm $ttft.$cname.tf
                            #ls *.tf
                            cat t2.txt | perl -pe 's/\x1b.*?[mGKH]//g' > t1.txt
                            mv="version"
                            file="t1.txt"
                            fn=`printf "%s__%s.tf" $ttft $cname`
                            echo $aws2tfmess > $fn
                            iscust=0
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
                                    if [[ ${tt1} == "arn" ]];then 
                                        t1=`printf "depends_on = [aws_eks_cluster.%s]\n" $cln`
                                    fi
                                    if [[ ${tt1} == "id" ]];then skip=1; fi
                                    #if [[ ${tt1} == "role_arn" ]];then skip=1;fi
                                    if [[ ${tt1} == "ami_type" ]];then 
                                        ## temp hack for AMI type
                                        amit=`echo $tt2 | tr -d '"'`
                                        if [[ ${amit} == "CUSTOM" ]];then
                                            skip=1
                                            iscust=1
                                        fi
                                    fi
                                    if [[ ${tt1} == "node_role_arn" ]];then 
                                        rarn=`echo $tt2 | tr -d '"'` 
                                        skip=0;
                                        trole=`echo "$tt2" | cut -f2- -d'/' | tr -d '"'`
                                        #echo "depends_on = [aws_iam_role.$trole]" >> $fn              
                                        t1=`printf "%s = aws_iam_role.%s.arn" $tt1 $trole`
                            
                                    fi
                                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                                    if [[ ${tt1} == "association_id" ]];then skip=1;fi
                                    if [[ ${tt1} == "unique_id" ]];then skip=1;fi
                                    if [[ ${tt1} == "create_date" ]];then skip=1;fi
                                    if [[ ${tt1} == "version" ]];then 
                                        if [ "$iscust" == "1" ]; then
                                            skip=1;
                                            iscust=0  # skip first occurance but not the second
                                        fi
                                    fi
                                    if [[ ${tt1} == "release_version" ]];then 
                                        if [ "$iscust" == "1" ]; then
                                            skip=1;
                                        fi
                                    fi
                                    #if [[ ${tt1} == "certificate_authority" ]];then 
                                    # skip the block
                                    #    echo $SL
                                    #    SL= read line
                                    #    read line
                                    #    read line
                                    #    read line
                                    #    skip=1
                                    #fi
                                    #if [[ ${tt1} == "private_ip" ]];then skip=1;fi
                                    #if [[ ${tt1} == "accept_status" ]];then skip=1;fi
                                    #if [[ ${tt1} == "created_at" ]];then skip=1;fi
                                    #if [[ ${tt1} == "endpoint" ]];then skip=1;fi
                                    #if [[ ${tt1} == "status" ]];then skip=1;fi
                                    if [[ ${tt1} == "resources" ]];then 
                                        read line
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
                                    #if [[ ${tt1} == "platform_version" ]];then skip=1;fi
                                    if [[ ${tt1} == "status" ]];then skip=1;fi
                                    #if [[ ${tt1} == "cluster_security_group_id" ]];then skip=1;fi
                                else
                                    if [[ "$t1" == *"subnet-"* ]]; then
                                        t1=`echo $t1 | tr -d '"|,'`
                                        t1=`printf "aws_subnet.%s.id," $t1`
                                    fi                           
                                fi
                                #
                                if [ "$skip" == "0" ]; then
                                    #echo $skip $t1
                                    echo $t1 >> $fn
                                fi
                                
                            done <"$file"   # done while

                            # pick up the launch template here
                            ltid=`echo $awsout | jq .nodegroup.launchTemplate.id | tr -d '"'`
                            echo "ltid=$ltid"
                            ../../scripts/eks-launch_template.sh $ltid
                     
                        done # done for i
                    fi
                done
            done
            if [ "$1" != "" ]; then
                # get other stuff
                #terraform refresh > /dev/null
                #echo "finish refresh"
                rm -f t*.txt

                #echo $rarn
                ../../scripts/050-get-iam-roles.sh $rarn
            fi




        fi
        
    done
fi

## Look for unmanaged Nodes vis autoscaling group

../../scripts/eks-auto-scaling-groups.sh $cln





