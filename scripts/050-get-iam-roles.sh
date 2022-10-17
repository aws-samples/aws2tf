#!/bin/bash
mysub=`echo $AWS2TF_ACCOUNT`
myreg=`echo $AWS2TF_REGION`
#echo "globe vars $myreg $mysub"
if [[ "$1" != "" ]]; then  
    if [[ ${1} == "arn:aws:iam"* ]]; then
        cmd[0]="$AWS iam list-roles | jq '.Roles[] | select(.Arn==\"${1}\")'"
    else
        cmd[0]="$AWS iam list-roles | jq '.Roles[] | select(.RoleName==\"${1}\")'"
    fi
else
    cmd[0]="$AWS iam list-roles"
fi


pref[0]="Roles"
tft[0]="aws_iam_role"

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
    #echo "role command = $cm"
    ttft=${tft[(${c})]}
    #echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    if [ "$1" != "" ]; then
        count=1
    else
        count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    fi
    #echo "count=$count"
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            if [ "$1" != "" ]; then
                cname=`echo $awsout | jq ".RoleName" | tr -d '"'` 
                rpath=`echo $awsout | jq ".Path" | tr -d '"'` 
            else
                cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})].RoleName" | tr -d '"'`
                rpath=`echo $awsout | jq ".${pref[(${c})]}[(${i})].Path" | tr -d '"'`
            fi
        
                if [[ "$rpath" == *"service-role"* ]]; then 
                    #if [[ ${1} != "arn:aws:iam"* ]]; then
                    if [[ ${1} == "" ]]; then
                        echo "skipping a service_role ...."
                        continue
                    fi
                fi
                ocname=`echo $cname`
                cname=${cname//./_}

                #temp                

                echo "$ttft $cname $rpath"
                fn=`printf "%s__%s.tf" $ttft $cname`
                if [ -f "$fn" ] ; then
                    echo "$fn exists already skipping"
                    continue
                fi

                printf "resource \"%s\" \"%s\" {}" $ttft $cname > $fn
                  
                terraform import $ttft.$cname $ocname | grep Import
                terraform state show -no-color $ttft.$cname > t1.txt
                rm -f $fn
  
                file="t1.txt"
                nl=$(cat $file | wc -l)
                if [[ $nl -eq 0 ]];then
                    echo "--> ERROR - state show empty for role $ocname"
                fi
                reps=()
                echo $aws2tfmess > $fn
                while IFS= read line
                do
                    skip=0
                    trole=""
                    # display $line or do something with $line
                    t1=`echo "$line"`
                    if [[ ${t1} == *"="* ]];then
                        tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '`
                        tt2=`echo "$line" | cut -f2- -d'='`
                        if [[ ${tt1} == *":"* ]];then
                            tt1=`echo $tt1 | tr -d '"'`
                            t1=`printf "\"%s\"=%s" $tt1 $tt2`
                        fi
                        if [[ ${tt1} == "arn" ]];then skip=1; fi
                        if [[ ${tt1} == "id" ]];then skip=1; fi
                        if [[ ${tt1} == "role_arn" ]];then skip=1;fi
                        if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                        if [[ ${tt1} == "association_id" ]];then skip=1;fi
                        if [[ ${tt1} == "unique_id" ]];then skip=1;fi
                        if [[ ${tt1} == "create_date" ]];then skip=1;fi
                        #if [[ ${tt1} == "public_ip" ]];then skip=1;fi
                        if [[ ${tt1} == "private_ip" ]];then skip=1;fi
                        if [[ ${tt1} == "accept_status" ]];then skip=1;fi
                        if [[ ${tt1} == *":"* ]];then 
                            lh=`echo $tt1 | tr -d '"'`
                            skip=0;
                            t1=`printf "\"%s\"=%s" $lh $tt2`
                            #echo $t1
                        fi
                        if [[ ${tt1} == "AWS" ]]; then
                            tt2=`echo $tt2 | tr -d '"'`
                            if [[ ${tt2} == "arn:aws:iam::"* ]];then
                                tstart=$(echo $tt2 | cut -f1-4 -d ':')
                                tacc=$(echo $tt2 | cut -f5 -d ':')
                                tend=$(echo $tt2 | cut -f6- -d ':')
                                tsub="%s"
                                if [[ "$mysub" == "$tacc" ]];then
                                    t1=$(printf "\"%s\" = format(\"%s:%s:%s\",data.aws_caller_identity.current.account_id)" $tt1 $tstart $tsub $tend)
                                fi
                            fi
                        fi

                        if [[ ${tt1} == "Resource" ]];then
                            if [[ "$tt2" != *"*"* ]];then
                                if [[ "$tt2" == *"${mysub}:role/"* ]];then
                                    if [[ "$tt2" != *"${mysub}:role/aws-service-role"* ]];then
                                        rarn=`echo $tt2 | tr -d '"'` 
                                        trole=`echo "$tt2" | cut -f2- -d'/' | tr -d '"'` 
                                        if [[ $trole != $cname ]];then                      
                                            t1=`printf "%s = aws_iam_role.%s.arn" $tt1 $trole`
                                            getrole="echo $trole"
                                        fi
                                    else
                                        echo "Found Service Role $tt2"    
                                    fi
                                elif [[ "$tt2" == "arn:aws:sns:${myreg}:${mysub}:"* ]];then
                                    rsns=`echo $tt2 | tr -d '"'` 
                                    mtopic=`echo "$tt2" | cut -f2- -d'/' | tr -d '"'`                       
                                    t1=`printf "%s = aws_sns_topic.%s.arn" $tt1 $mtopic`
                                elif [[ "$tt2" == *"arn:aws:kms:${myreg}:${mysub}:key/"* ]];then
                                    kid=`echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"'`                                 
                                    t1=`printf "%s = aws_kms_key.k_%s.arn" $tt1 $kid`
                                elif [[ "$tt2" == *"arn:aws:ecr:${myreg}:${mysub}:repository/"* ]];then
                                    rep=`echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"'` 
                                    reps+=`printf "\"%s\" " $rep`                                
                                    t1=`printf "%s = aws_ecr_repository.%s.arn" $tt1 $rep`
                                elif [[ "$tt2" == *"arn:aws:codecommit:${myreg}:${mysub}:"* ]];then
                                    ccid=`echo $tt2 | rev | cut -f1 -d':' | rev | tr -d '"'`                                 
                                    t1=`printf "%s = aws_codecommit_repository.%s.arn" $tt1 $ccid`

                                elif [[ "$tt2" == *"arn:aws:codepipeline:${myreg}:${mysub}:"* ]];then
                                    cpid=`echo $tt2 | rev | cut -f1 -d':' | rev | tr -d '"'`                                 
                                    t1=`printf "%s = aws_codepipeline.%s.arn" $tt1 $cpid`

                                elif [[ "$tt2" == *"arn:aws:codebuild:${myreg}:${mysub}:project/"* ]];then
                                    cbid=`echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"'`                                 
                                    t1=`printf "%s = aws_codebuild_project.%s.arn" $tt1 $cbid`


                                else   # check tt2 for $
                                    tt2=${tt2//$/&} 
                                    tt1=`echo $tt1 | tr -d '"'`
                                    t1=`printf "\"%s\"=%s" $tt1 "$tt2"`
                                fi
                            fi
                        fi                       

                    fi
                    if [ "$skip" == "0" ]; then
                        #echo $skip $t1
                        echo "$t1" >> $fn
                    fi
                    
                done <"$file"   # done while

                # Get attached role policies
                
                echo "role policies $ocname"
                ../../scripts/051-get-iam-role-policies.sh $ocname
                echo "attached role policies $ocname"
                ../../scripts/052-get-iam-attached-role-policies.sh $ocname
  
                for rep in ${reps[@]}; do
                    rep=`echo $rep | tr -d '"'`
                    #echo "***** calling for $topic"
                    if [[ "$rep" != "" ]]; then
                        ../../scripts/get-ecr.sh $rep
                    fi
                done 

                if [[ $getrole != "" ]];then
                    ../../scripts/050-get-iam-roles.sh $getrole
                fi


        done    # done for i      
    fi
done

rm -f t*.txt


