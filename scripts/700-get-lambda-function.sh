#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS lambda get-function --function-name $1"
    pref[0]="Configuration"
else
    cmd[0]="$AWS lambda list-functions"
    pref[0]="Functions"

fi

tft[0]="aws_lambda_function"
idfilt[0]="FunctionName"

#rm -f ${tft[0]}.tf

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
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
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            if [ "$1" != "" ]; then
                cname=$(echo $awsout | jq -r ".${pref[(${c})]}.${idfilt[(${c})]}")
            else
                cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")
            fi
            echo "$ttft $cname"
            fn=`printf "%s__%s.tf" $ttft $cname`
            if [ -f "$fn" ] ; then
                echo "$fn exists already skipping"
                continue
            fi
            printf "resource \"%s\" \"%s\" {" $ttft $cname > $ttft.$cname.tf
            printf "}" >> $ttft.$cname.tf
            printf "terraform import %s.%s %s" $ttft $cname $cname > data/import_$ttft_$cname.sh
            terraform import $ttft.$cname "$cname" | grep Import
            terraform state show -no-color $ttft.$cname > t1.txt
            tfa=`printf "%s.%s" $ttft $cname`
            terraform show  -json | jq --arg myt "$tfa" '.values.root_module.resources[] | select(.address==$myt)' > data/$tfa.json
            #echo $awsj | jq . 
            s3rep=$($AWS lambda get-function --function-name $cname | jq -r .Code.RepositoryType)
            if [ $s3rep == "S3" ]; then
                s3loc=$($AWS lambda get-function --function-name $cname | jq -r .Code.Location)
                echo "Getting Lambda function code:  $cname.zip"
                curl -s -o $cname.zip ${s3loc}
            fi 
            rm -f $ttft.$cname.tf

            file="t1.txt"
            echo $aws2tfmess > $fn
            sgs=()
            subnets=()
            doarn=0
            while IFS= read line
            do
				skip=0
                # display $line or do something with $line
                t1=`echo "$line"` 
                if [[ ${t1} == *"file_system_config"* ]];then doarn=1 ;fi
                if [[ ${t1} == *"="* ]];then

                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                    tt2=`echo "$line" | cut -f2- -d'='`
                    if [[ ${tt1} == "arn" ]];then 
                        if [[ $doarn == "0" ]];then 
                            skip=1;
                            efsarn=`echo "$tt2"` 
                        fi 
                    fi                
                    if [[ ${tt1} == "id" ]];then
                        if [ -f "$cname.zip" ]; then 
                            t1=`printf "filename = \"%s.zip\"" $cname`
                            printf "lifecycle {\n" >> $fn
                            printf "   ignore_changes = [filename]\n" >> $fn
                            printf "}\n" >> $fn
                        fi
                    fi  
                    if [[ ${tt1} == "invoke_arn" ]];then skip=1;fi        
                    if [[ ${tt1} == "role_arn" ]];then skip=1;fi
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    if [[ ${tt1} == "last_modified" ]];then skip=1;fi
                    if [[ ${tt1} == "source_code_hash" ]];then 
                      t1=`printf "source_code_hash = filebase64sha256(\"%s.zip\")" $cname`
                    fi
                    if [[ ${tt1} == "qualified_arn" ]];then skip=1;fi
                    if [[ ${tt1} == "version" ]];then skip=1;fi
                    if [[ ${tt1} == "qualified_invoke_arn" ]];then skip=1;fi
                    if [[ ${tt1} == "source_code_size" ]];then skip=1;fi
                    if [[ ${tt1} == "vpc_id" ]]; then
                        vpcid=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_vpc.%s.id" $tt1 $vpcid`
                        skip=1
                    fi
                    if [[ ${tt1} == "role" ]];then 
                        rarn=`echo $tt2 | tr -d '"'` 
                        skip=0;
                        #trole=`echo "$tt2" | cut -f2- -d'/' | tr -d '"'`
                        trole=`echo "$tt2" | rev | cut -d'/' -f1 | rev | tr -d '"'`
                                                    
                        t1=`printf "%s = aws_iam_role.%s.arn" $tt1 $trole`
                    fi

                else
                    if [[ "$t1" == *"subnet-"* ]]; then
                        t1=`echo $t1 | tr -d '"|,'`
                        subnets+=`printf "\"%s\" " $t1`
                        t1=`printf "aws_subnet.%s.id," $t1`
                    fi
                    if [[ "$t1" == *"sg-"* ]]; then
                        t1=`echo $t1 | tr -d '"|,'`
                        sgs+=`printf "\"%s\" " $t1`
                        t1=`printf "aws_security_group.%s.id," $t1`
                    fi

                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"

            if [ "$trole" != "" ]; then
                ../../scripts/050-get-iam-roles.sh $trole
            fi
            if [ "$vpcid" != "" ]; then
                ../../scripts/100-get-vpc.sh $vpcid
            fi


            for sub in ${subnets[@]}; do
                #echo "therole=$therole"
                sub1=`echo $sub | tr -d '"'`
                echo "calling for $sub1"
                if [ "$sub1" != "" ]; then
                    ../../scripts/105-get-subnet.sh $sub1
                fi
            done

            for sg in ${sgs[@]}; do
                #echo "therole=$therole"
                sg1=`echo $sg | tr -d '"'`
                echo "calling for $sg1"
                if [ "$sg1" != "" ]; then
                    ../../scripts/110-get-security-group.sh $sg1
                fi
            done 

            if [ "$cname" != "" ]; then
                ../../scripts/get-lambda-alias.sh $cname
                ../../scripts/get-lambda-permission.sh $cname
                ../../scripts/get-lambda-event-invoke-configs.sh $cname
            fi
        
        done

    fi
done


rm -f t*.txt

