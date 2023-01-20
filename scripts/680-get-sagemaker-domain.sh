#!/bin/bash
if [[ "$1" != "" ]];then
    cmd[0]=$(printf "$AWS sagemaker list-domains | jq '. | select(.Domains[].DomainId==\"%s\")'" $1)
else
    cmd[0]="$AWS sagemaker list-domains"
fi

pref[0]="Domains"
tft[0]="aws_sagemaker_domain"
idfilt[0]="DomainId"
ncpu=$(getconf _NPROCESSORS_ONLN)
ncpu=`expr $ncpu - 1`
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
    #echo $count
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi
            #echo "calling import sub"
            #terraform state rm $ttft.$rname > /dev/null
            echo "$ttft $cname import"
            . ../../scripts/parallel_import2.sh $ttft $cname &
            jc=`jobs -r | wc -l | tr -d ' '`
            while [ $jc -gt $ncpu ];do
                echo "Throttling - $jc Terraform imports in progress"
                sleep 10
                jc=`jobs -r | wc -l | tr -d ' '`
            done
        done

         
        jc=`jobs -r | wc -l | tr -d ' '`
        if [ $jc -gt 0 ];then
            echo "Waiting for $jc Terraform imports"
            wait
            echo "Finished importing"
        fi
        ../../scripts/parallel_statemv.sh $ttft
        
        
        # tf files
        for i in `seq 0 $count`; do
            #echo $i
            cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            #echo "$ttft $cname tf files"
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

            file=`printf "%s-%s-1.txt" $ttft $rname`
            keyid=""
            imnam=""
            aic=""
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
                    if [[ ${tt1} == "role_arn" ]];then skip=1;fi
                    if [[ ${tt1} == "home_efs_file_system_id" ]];then skip=1;fi
                    if [[ ${tt1} == "url" ]];then skip=1;fi
                    if [[ ${tt1} == "single_sign_on_managed_application_instance_id" ]];then skip=1;fi

                    if [[ ${tt1} == "vpc_id" ]];then 
                        vpcid=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_vpc.%s.id" $tt1 $vpcid`
                    
                    fi
                    if [[ ${tt1} == "execution_role" ]];then 
                        rarn=`echo $tt2 | tr -d '"'`
                        erole=`echo "$tt2" | rev | cut -d'/' -f1 | rev | tr -d '"'`
                        t1=`printf "%s = aws_iam_role.%s.arn" $tt1 $erole`                
                    fi
                    if [[ ${tt1} == "kms_key_id" ]];then 
                        keyid=`echo $tt2 | rev | cut -f1 -d'/' | rev | tr -d '"'`
                        t1=`printf "%s = aws_kms_key.k_%s.arn" $tt1 $keyid`
                        printf "lifecycle {\n" >> $fn
                        printf "   ignore_changes = [kms_key_id]\n" >> $fn
                        printf "}\n" >> $fn
                    fi
                    if [[ ${tt1} == "image_name" ]];then 
                        imnam=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_sagemaker_image.%s.id" $tt1 $imnam`
                    fi
                    if [[ ${tt1} == "sagemaker_image_arn" ]];then 
                        imarn=`echo $tt2 | tr -d '"'`
                        imnam2=`echo "$tt2" | rev | cut -d'/' -f1 | rev | tr -d '"'`
                        t1=`printf "%s = aws_sagemaker_image.%s.arn" $tt1 $imnam2`
                    fi
                    if [[ ${tt1} == "app_image_config_name" ]];then 
                        aic=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_sagemaker_app_image_config.%s.id" $tt1 $aic`
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

            echo "role  $rarn"
            if [[ $rarn != "" ]];then
                ../../scripts/050-get-iam-roles.sh $rarn
            fi
            if [[ "$vpcid" != "" ]]; then
                echo "vpcid=$vpcid"
                echo "calling vpc"
                ../../scripts/100-get-vpc.sh $vpcid  # vpc                
                ../../scripts/105-get-subnet.sh $vpcid # subnets
                ../../scripts/110-get-security-group.sh $vpcid 
                ../../scripts/140-get-route-table.sh $vpcid
                ../../scripts/141-get-route-table-associations.sh $vpcid
                ../../scripts/161-get-vpce.sh $vpcid   
            fi
            if [[ "$keyid" != "" ]];then
                ../../scripts/080-get-kms-key.sh $keyid
            fi

            if [[ "$imnam" != "" ]];then
                rimnam=${imnam//:/_} && rimnam=${rimnam//./_} && rimnam=${rimnam//\//_}
                ../../scripts/get-sagemaker-image.sh $rimnam
            fi
            if [[ "$imnam2" != "" ]];then
                rimnam2=${imnam2//:/_} && rimnam2=${rimnam2//./_} && rimnam2=${rimnam2//\//_}
                ../../scripts/get-sagemaker-image.sh $rimnam2
            fi

            if [[ "$aic" != "" ]];then
                ../../scripts/get-sagemaker-app-image-config.sh $aic
            fi
            echo "SM Execution role = $erole"
            if [[ "$erole" != "" ]];then
                ../../scripts/050-get-iam-roles.sh $erole
            fi


        done
    fi
done

rm -f *.backup 



#