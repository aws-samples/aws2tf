#!/bin/bash
if [ "$1" != "" ]; then
    cmd[0]="$AWS ec2 describe-spot-fleet-requests --spot-fleet-request-ids $1"
    #select(.SpotFleetRequestState!="cancelled")'
else
    cmd[0]="$AWS ec2 describe-spot-fleet-requests"
fi

pref[0]="SpotFleetRequestConfigs"
tft[0]="aws_spot_fleet_request"
idfilt[0]="SpotFleetRequestId"

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    #echo "count= $count"
    if [ "$count" != "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo "i=$i"
            cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")
            state=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].SpotFleetRequestState")
            if [[ "${state}" != "active" ]]; then
                echo "state=${state} continue...."
                continue
            fi
            echo "$ttft $cname"
            
            fn=`printf "%s__%s.tf" $ttft $cname`
            echo $aws2tfmess > $fn
            printf "resource \"%s\" \"%s\" {" $ttft $cname > $ttft.$cname.tf
            printf "}" >> $ttft.$cname.tf
            terraform import $ttft.$cname "$cname" | grep Import
            terraform state show -no-color $ttft.$cname > t1.txt
            rm -f $ttft.$cname.tf

            file="t1.txt"
            fn=`printf "%s__%s.tf" $ttft $cname`
            echo $aws2tfmess > $fn
            subnets=()
            iddo=0
            while IFS= read line
            do
				skip=0
                # display $line or do something with $line
                t1=`echo "$line"` 
                if [[ ${t1} == *"="* ]];then
                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                    tt2=`echo "$line" | cut -f2- -d'='`
                    if [[ ${tt1} == "arn" ]];then skip=1; fi                
                    if [[ ${tt1} == "id" ]];then 
                        if [[ "${iddo}" == "0" ]] ;then
                            skip=1;
                            iddo=1
                            printf "lifecycle {\n" >> $fn
                            printf "   ignore_changes = [load_balancers,target_group_arns,wait_for_fulfillment]\n" >> $fn
                            printf "}\n" >> $fn
                        else
                            tt2=`echo $tt2 | tr -d '"'`
                            t1=`printf "%s = aws_launch_template.%s.id" $tt1 $tt2`
                            lt=`printf "%s" $tt2`
                        fi 
                    fi
                                  
                    if [[ ${tt1} == "role_arn" ]];then skip=1;fi
                    if [[ ${tt1} == "spot_request_state" ]];then skip=1;fi
                    if [[ ${tt1} == "subnet_id" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_subnet.%s.id" $tt1 $tt2`
                        subnets+=`printf "\"%s\" " $tt2`
                    fi
                    if [[ ${tt1} == "iam_fleet_role" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        trole=`echo "$tt2" | rev | cut -d'/' -f1 | rev | tr -d '"'`
                        t1=`printf "%s = aws_iam_role.%s.arn" $tt1 $trole`
                        rarn=`printf "%s" $tt2`
                    fi

                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"

            ../../scripts/255-get-ec2-launch-templates.sh $lt
            for sub in ${subnets[@]}; do
                sub1=`echo $sub | tr -d '"'`
                echo "calling for $sub1"
                if [ "$sub1" != "" ]; then
                    ../../scripts/105-get-subnet.sh $sub1
                fi
            done
            if [[ $rarn != "" ]];then
                ../../scripts/050-get-iam-roles.sh $rarn
            fi 
            ## need the vpc
            #../../aws2tf.sh -t vpc -i $ivpc -c yes
            # instance profile, iam_fleet_role, launch_template
            # 
            #../../scripts/100-get-vpc.sh $ivpc
            
        done
    fi
done

rm -f t*.txt

