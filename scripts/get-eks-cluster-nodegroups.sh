#!/bin/bash
#echo $AWS
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
                
        #echo cluster name $cln
        cname=`echo $cln`
        #rm -f ${tft[0]}_*.tf
        jcount=`$AWS eks list-nodegroups --cluster-name $cln | jq ".nodegroups | length"`
        
        echo "Found $jcount node groups for cluster $cln"
        if [ "$jcount" -gt "0" ]; then
            jcount=`expr $jcount - 1`
            for j in `seq 0 $jcount`; do
                ng=`$AWS eks list-nodegroups --cluster-name $cln   | jq ".nodegroups[(${j})]" | tr -d '"'`     
                echo "***** node group = $ng"
                cmd[0]=`echo "$AWS eks describe-nodegroup --cluster-name $cln --nodegroup-name $ng"`      
                pref[0]="nodegroup"
                tft[0]="aws_eks_node_group"
                ## 

        
                for c in `seq 0 0`; do
                    #rm -f ${tft[0]}*.tf
                    cm=${cmd[$c]}
                    ttft=${tft[(${c})]}
                    #echo "inner command=$cm"
                    awsout=`eval $cm 2> /dev/null`
                    if [ "$awsout" == "" ];then
                        echo "$cm : You don't have access for this resource"
                        exit
                    fi
                    #echo awsout
                    #echo $awsout | jq .
                    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
                    count=1 # one cluster at a time !
                    if [ "$count" -gt "0" ]; then
                        count=`expr $count - 1`
                        for i in `seq 0 $count`; do
                            #echo $i
                            cname=`echo $awsout | jq ".${pref[(${c})]}.clusterName" | tr -d '"'`
                            ngnam=`echo $awsout | jq ".${pref[(${c})]}.nodegroupName" | tr -d '"'`
                            ocname=`printf "%s:%s" $cname $ngnam`

                            cname=${ocname//:/_}
                           
                            #echo "cname=$cname ngname=$ngnam ocname=$ocname"
                            fn=`printf "%s__%s.tf" $ttft $cname`
                            echo "$ttft $cname import"
                            if [ -f "$fn" ]; then continue; fi

                            printf "resource \"%s\" \"%s\" {}\n" $ttft $cname > $fn
                
                            #echo "pre-import"
                            #ls -l
                            echo "Importing ....."
                            terraform import $ttft.$cname $ocname | grep Import
                            terraform state show -no-color $ttft.$cname > t1.txt
                            rm -f $fn
            
                            mv="version"
                            file="t1.txt"
                            
                            echo $aws2tfmess > $fn
                            iscust=0
                            allowid=0
  
                            while IFS= read line
                            do
                                skip=0
                                # display $line or do something with $line
                                t1=`echo "$line"`
                                if [[ ${t1} == *"launch_template"* ]];then allowid=1; fi
                                if [[ ${t1} == *"="* ]];then
                                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '`
                                    tt2=`echo "$line" | cut -f2- -d'='`
                                    if [[ ${tt1} == *":"* ]];then
                                        tt1=`echo $tt1 | tr -d '"'`
                                        t1=`printf "\"%s\"=%s" $tt1 $tt2`
                                    fi
                                    if [[ ${tt1} == "arn" ]];then 
                                        t1=`printf "depends_on = [aws_eks_cluster.%s]\n" $cln`
                                    fi
                                    if [[ ${tt1} == "id" ]];then 
                                        if [[ ${allowid} == "0" ]];then
                                            skip=1 
                                        else
                                            skip=0
                                            ltid=`echo $tt2 | tr -d '"'`
                                            t1=`printf "%s = aws_launch_template.%s.id" $tt1 $ltid`
                                            allowid=0
                                        fi
                                    fi
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
                                    if [[ ${tt1} == "name" ]];then skip=1;fi
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
                                        #if [ "$iscust" == "1" ]; then
                                            skip=1;
                                        #fi
                                    fi

                                    if [[ ${tt1} == "max_unavailable_percentage" ]];then 
                                        tt2=`echo $tt2 | tr -d ' '`
                                        if [ "$tt2" == "0" ]; then
                                            skip=1;
                                        fi
                                    fi


                                    if [[ ${tt1} == "max_unavailable" ]];then 
                                        tt2=`echo $tt2 | tr -d ' '`
                                        if [ "$tt2" == "0" ]; then
                                            skip=1;
                                        fi
                                    fi

                                    if [[ ${tt1} == "resources" ]];then 
                                        #echo $t1
                                        skip=1
                                        lbc=0
                                        rbc=0
                                        breq=0
                                        while [[ $breq -eq 0 ]];do 
                                            if [[ "${t1}" == *"["* ]]; then lbc=`expr $lbc + 1`; fi
                                            if [[ "${t1}" == *"]"* ]]; then rbc=`expr $rbc + 1`; fi
                                            #echo "$lbc $rbc $t1"
                                            read line
                                            t1=`echo "$line"`
                                            if [[ $rbc -eq $lbc ]]; then breq=1; fi
                                        done 
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
                                    echo "$t1" >> $fn
                                fi
                                
                            done <"$file"   # done while
                            if [[ $rarn != "" ]];then
                                ../../scripts/050-get-iam-roles.sh $rarn
                            fi
                            # pick up the launch template here
                            ltid=`echo $awsout | jq .nodegroup.launchTemplate.id | tr -d '"'`
                            echo "ltid=$ltid calling eks-launch_template.sh "
                            ../../scripts/eks-launch_template.sh $ltid
                     
                        done # done for i
                    fi
                done
            done





        fi
        
    done
fi

echo "##### Look for unmanaged Nodes via autoscaling group"

../../scripts/eks-auto-scaling-groups.sh $cln





