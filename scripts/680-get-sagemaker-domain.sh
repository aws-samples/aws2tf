#!/bin/bash

cmd[0]="$AWS sagemaker list-domains"

pref[0]="Domains"
tft[0]="aws_sagemaker_domain"
idfilt[0]="DomainId"

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "You don't have access for this resource"
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
            . ../../scripts/parallel_import.sh $ttft $cname &
        done

         
        jc=`jobs -r | wc -l | tr -d ' '`
        if [ $jc -gt 0 ];then
            echo "Waiting for $jc Terraform imports"
            wait
            echo "Finished importing"
        fi
        
        
        
        # tf files
        for i in `seq 0 $count`; do
            #echo $i
            cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            #echo "$ttft $cname tf files"
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

            file=`printf "%s-%s-1.txt" $ttft $rname`
            
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

            echo "role  $rarn"
            ../../scripts/050-get-iam-roles.sh $rarn
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

            
        done
    fi
done

rm -f *.backup 



#