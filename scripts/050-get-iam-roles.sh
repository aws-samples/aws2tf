# CodeWhisperer convert the following bash script to a python script
#!/bin/bash
mysub=$(echo $AWS2TF_ACCOUNT)
myreg=$(echo $AWS2TF_REGION)
tft[0]="aws_iam_role"
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

for c in $(seq 0 0); do

    cm=${cmd[$c]}
    #echo "role command = $cm"
    ttft=${tft[(${c})]}
    #echo $cm
    awsout=$(eval $cm 2>/dev/null)
    if [ "$awsout" == "" ]; then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    if [ "$1" != "" ]; then
        count=1
    else
        count=$(echo $awsout | jq ".${pref[(${c})]} | length")
    fi
    #echo "count=$count"
    if [ "$count" -gt "0" ]; then
        count=$(expr $count - 1)
        for i in $(seq 0 $count); do
            #echo $i
            if [ "$1" != "" ]; then
                cname=$(echo $awsout | jq ".RoleName" | tr -d '"')
                marn=$(echo $awsout | jq ".Arn" | tr -d '"')
                rpath=$(echo $awsout | jq ".Path" | tr -d '"')
            else
                cname=$(echo $awsout | jq ".${pref[(${c})]}[(${i})].RoleName" | tr -d '"')
                marn=$(echo $awsout | jq ".${pref[(${c})]}[(${i})].Arn" | tr -d '"')
                rpath=$(echo $awsout | jq ".${pref[(${c})]}[(${i})].Path" | tr -d '"')
            fi

            if [[ "$rpath" == *"service-role"* ]]; then
                #if [[ ${1} != "arn:aws:iam"* ]]; then
                if [[ ${1} == "" ]]; then
                    echo "skipping a service_role ...."
                    continue
                fi
            fi
            ocname=$(echo $cname)
            cname=${cname//./_}

            #temp

            echo "$ttft $cname $rpath"
            fn=$(printf "%s__%s.tf" $ttft $cname)
            if [ -f "$fn" ]; then
                echo "$fn exists already skipping"
                continue
            fi

            rn=$(echo $marn | rev | cut -f1 -d'/' | rev | tr -d '"')
            echo "aws_iam_role,$marn,$rn" >>data/arn-map.dat

            printf "resource \"%s\" \"r-%s\" {}" $ttft $cname >$fn

            terraform import $ttft.r-${cname} $ocname | grep Importing
            terraform state show -no-color $ttft.r-${cname} >t1.txt
            rm -f $fn

            file="t1.txt"
            nl=$(cat $file | wc -l)
            if [[ $nl -eq 0 ]]; then
                echo "--> ERROR - state show empty for role $ocname"
            fi
            reps=()
            getrole=()
            ccid=""
            echo $aws2tfmess >$fn
            while IFS= read line; do
                skip=0
                trole=""
                # display $line or do something with $line
                t1=$(echo "$line")
                if [[ ${t1} == *"="* ]]; then
                    tt1=$(echo "$line" | cut -f1 -d'=' | tr -d ' ')
                    tt2=$(echo "$line" | cut -f2- -d'=')
                    if [[ ${tt1} == *":"* ]]; then
                        tt1=$(echo $tt1 | tr -d '"')
                        t1=$(printf "\"%s\"=%s" $tt1 $tt2)
                    fi
                    if [[ ${tt1} == "arn" ]]; then skip=1; fi
                    if [[ ${tt1} == "id" ]]; then skip=1; fi
                    if [[ ${tt1} == "role_arn" ]]; then skip=1; fi
                    if [[ ${tt1} == "owner_id" ]]; then skip=1; fi
                    if [[ ${tt1} == "association_id" ]]; then skip=1; fi
                    if [[ ${tt1} == "unique_id" ]]; then skip=1; fi
                    if [[ ${tt1} == "create_date" ]]; then skip=1; fi
                    #if [[ ${tt1} == "public_ip" ]];then skip=1;fi
                    if [[ ${tt1} == "private_ip" ]]; then skip=1; fi
                    if [[ ${tt1} == "accept_status" ]]; then skip=1; fi

                    if [[ ${tt1} == "role_last_used" ]]; then
                        # skip the block
                        tt2=$(echo $tt2 | tr -d '"')
                        skip=1
                        while [ "$t1" != "]" ] && [ "$tt2" != "[]" ]; do
                            read line
                            t1=$(echo "$line")
                        done
                    fi

                    if [[ ${tt1} == *":"* ]]; then
                        lh=$(echo $tt1 | tr -d '"')
                        skip=0
                        # check $tt2 for '"'
                        tt2=$(echo $tt2 | sed 's/"//')
                        tt2=$(echo $tt2 | rev | sed 's/"//' | rev)
                        tt2=$(echo $tt2 | sed 's/"/\\"/g')
                        #echo "-1-> $lh - $tt2"
                        if [[ $tt2 == "[" ]] || [[ $tt2 == "]" ]] || [[ $tt2 == "{" ]]; then
                            t1=$(printf "\"%s\"=%s" $lh "$tt2")
                        else
                            t1=$(printf "\"%s\"=\"%s\"" $lh "$tt2")
                        fi
                        #echo "-2->$t1"
                    fi
                    if [[ ${tt1} == "AWS" ]]; then
                        tt2=$(echo $tt2 | tr -d '"')
                        if [[ ${tt2} == "arn:aws:iam::"* ]]; then
                            tstart=$(echo $tt2 | cut -f1-4 -d ':')
                            tacc=$(echo $tt2 | cut -f5 -d ':')
                            tend=$(echo $tt2 | cut -f6- -d ':')
                            tsub="%s"
                            if [[ "$mysub" == "$tacc" ]]; then
                                t1=$(printf "\"%s\" = format(\"%s:%s:%s\",data.aws_caller_identity.current.account_id)" $tt1 $tstart $tsub $tend)
                            fi
                        fi
                    fi

                    if [[ ${tt1} == "Resource" ]]; then
                        if [[ "$tt2" != *"*"* ]]; then
                            if [[ "$tt2" == *"${mysub}:role/"* ]]; then
                                if [[ "$tt2" != *"${mysub}:role/aws-service-role"* ]]; then
                                    rarn=$(echo $tt2 | tr -d '"')
                                    trole=$(echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"')
                                    if [[ $trole != $cname ]]; then
                                        t1=$(printf "%s = aws_iam_role.r-%s.arn" $tt1 $trole)
                                        getrole+=$(printf "\"%s\" " $rarn)
                                        echo "aws_iam_role,$rarn,$trole" >>data/arn-map.dat
                                    fi
                                else
                                    echo "Found Service Role $tt2"
                                fi
                            elif [[ "$tt2" == "arn:aws:sns:${myreg}:${mysub}:"* ]]; then
                                rsns=$(echo $tt2 | tr -d '"')
                                mtopic=$(echo "$tt2" | cut -f2- -d'/' | tr -d '"')
                                t1=$(printf "%s = aws_sns_topic.%s.arn" $tt1 $mtopic)
                            elif [[ "$tt2" == *"arn:aws:kms:${myreg}:${mysub}:key/"* ]]; then
                                kid=$(echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"')
                                t1=$(printf "%s = aws_kms_key.k_%s.arn" $tt1 $kid)
                            elif [[ "$tt2" == *"arn:aws:ecr:${myreg}:${mysub}:repository/"* ]]; then
                                rep=$(echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"')
                                reps+=$(printf "\"%s\" " $rep)
                                t1=$(printf "%s = aws_ecr_repository.%s.arn" $tt1 $rep)
                            elif [[ "$tt2" == *"arn:aws:codecommit:${myreg}:${mysub}:"* ]]; then
                                ccid=$(echo $tt2 | rev | cut -f1 -d':' | rev | tr -d '"')
                                echo "ccid=$ccid"
                                t1=$(printf "%s = aws_codecommit_repository.%s.arn" $tt1 $ccid)

                            elif [[ "$tt2" == *"arn:aws:codepipeline:${myreg}:${mysub}:"* ]]; then
                                cpid=$(echo $tt2 | rev | cut -f1 -d':' | rev | tr -d '"')
                                t1=$(printf "%s = aws_codepipeline.r-%s.arn" $tt1 $cpid)

                            elif [[ "$tt2" == *"arn:aws:codebuild:${myreg}:${mysub}:project/"* ]]; then
                                cbid=$(echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"')
                                t1=$(printf "%s = aws_codebuild_project.%s.arn" $tt1 $cbid)

                            else # check tt2 for $ and '"'
                                # arn catch all

                                if [[ "$tt2" == *"arn:aws:"*":$myreg:$mysub:"* ]]; then
                                    echo $t1
                                    echo $tt2
                                    tstart=$(echo $tt2 | cut -f1-3 -d ':')
                                    treg=$(echo $tt2 | cut -f4 -d ':')
                                    tacc=$(echo $tt2 | cut -f5 -d ':')
                                    tend=$(echo $tt2 | cut -f6- -d ':')
                                    tsub="%s"
                                    if [[ "$mysub" == "$tacc" ]]; then
                                        t1=$(printf "%s = format(\"%s:%s:%s:%s\",data.aws_region.current.name,data.aws_caller_identity.current.account_id)" $tt1 $tstart $tsub $tsub $tend)
                                    fi
                                else
                                    tt2=${tt2//$/&}
                                    tt1=$(echo $tt1 | tr -d '"')
                                    t1=$(printf "\"%s\"=%s" $tt1 "$tt2")
                                fi
                            fi
                        else
                            tt2=$(echo $tt2 | tr -d '"')
                            tt2=$(echo ${tt2:0:-1}) # chop off the star
                            tstart=$(echo ${tt2:0:8})
                            #echo $tstart
                            if [[ "$tstart" == "arn:aws:" ]];then

                                #echo "inside $tt2"
                                tstart=$(echo $tt2 | cut -f1-3 -d ':')
                                treg=$(echo $tt2 | cut -f4 -d ':')
                                tacc=$(echo $tt2 | cut -f5 -d ':')
                                tend=$(echo $tt2 | cut -f6- -d ':')
                                tsub="%s"
                                if [[ "$mysub" == "$tacc" ]]; then
                                    t1=$(printf "%s = format(\"%s:%s:%s:%s*\",data.aws_region.current.name,data.aws_caller_identity.current.account_id)" $tt1 $tstart $tsub $tsub $tend)
                                fi
                                #echo "t1=$t1"
                            #else
                            #    tt2=${tt2//$/&}
                            #    tt1=$(echo $tt1 | tr -d '"')
                            #    t1=$(printf "\"%s\"=%s" $tt1 "$tt2")
                            fi

                        fi # if no stars

                    fi # end Resource

                fi
                if [ "$skip" == "0" ]; then
                    echo $t1

                    if [[ $t1 == "arn:aws:"* ]];then
                        echo "in $t1"

                    fi

                    echo "$t1" >>$fn
                fi

            done <"$file" # done while

            # Get attached role policies

            echo "role policies $ocname"
            ../../scripts/051-get-iam-role-policies.sh $ocname
            echo "attached role policies $ocname"
            ../../scripts/052-get-iam-attached-role-policies.sh $ocname

            for rep in ${reps[@]}; do
                rep=$(echo $rep | tr -d '"')
                #echo "***** calling for $topic"
                if [[ "$rep" != "" ]]; then
                    ../../scripts/get-ecr.sh $rep
                fi
            done

            for sub in ${getrole[@]}; do
                #echo "therole=$therole"
                sub1=$(echo $sub | tr -d '"')
                echo "calling for $sub1"
                if [ "$sub1" != "" ]; then
                    ../../scripts/050-get-iam-roles.sh $sub1
                fi
            done

            if [[ $ccid != "" ]]; then
                ../../scripts/628-get-code-commit-repository.sh $ccid $ccid # pass same param twice deliberately
            fi

            #if [[ $getrole != "" ]]; then
            #    ../../scripts/050-get-iam-roles.sh $getrole
            #fi

        done # done for i
    fi
done

rm -f t*.txt
