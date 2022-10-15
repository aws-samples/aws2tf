#!/bin/bash
if [ "$1" != "" ]; then
    fp=$(echo $1 | cut -f1 -d ':')
    cmd[0]="$AWS ecs list-task-definitions --family-prefix $fp" 
else
    cmd[0]="$AWS ecs list-task-definitions"
fi

tft[0]="aws_ecs_task_definition"
pref[0]="taskDefinitionArns"
idfilt[0]=""

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
    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            cname=`echo $awsout | jq ".${pref[(${c})]}[(${i})]" | tr -d '"'`
            tname=$(echo $cname | cut -f6-10 -d':')
            rname=${tname//:/_} && rname=${rname//./_} && rname=${rname//\//_}

            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

            printf "resource \"%s\" \"%s\" {\n" $ttft $rname > $fn
            printf "}"  >> $fn
            terraform import $ttft.$rname "$cname" | grep Import
            terraform state show -no-color $ttft.$rname > t1.txt
            
            rm -f $fn
            
            file="t1.txt"
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
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "ipv6_cidr_block_association_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "availability_zone" ]];then skip=1;fi
                    #if [[ ${tt1} == "availability_zone_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "state" ]];then skip=1;fi
                    #if [[ ${tt1} == "dns_entry" ]];then skip=1;fi

                    #if [[ ${tt1} == "requester_managed" ]];then skip=1;fi
                    #if [[ ${tt1} == "revision" ]];then skip=1;fi
                    if [[ ${tt1} == "cidr_blocks" ]];then
                        echo "matched cidr"  
                        skip=1
                        while [[ "$t1" != "]" ]] ;do
                            read line
                            t1=`echo "$line"`
                            echo $t1
                        done
                    fi
                    if [[ ${tt1} == "revision" ]];then skip=1;fi
                    if [[ ${tt1} == "vpc_id" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_vpc.%s.id" $tt1 $tt2`
                    fi
                    if [[ ${tt1} == "@type" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf type = \"%s\"" $tt2`
                    fi

                    if [[ ${tt1} == "task_role_arn" ]];then 
                        trarn=`echo $tt2 | tr -d '"'` 
                        skip=0;
                        trole=`echo "$tt2" | rev | cut -d'/' -f1 | rev | tr -d '"'`                     
                        t1=`printf "%s = aws_iam_role.%s.arn" $tt1 $trole`
                    fi

                    if [[ ${tt1} == "execution_role_arn" ]];then 
                        erarn=`echo $tt2 | tr -d '"'` 
                        skip=0;
                        trole=`echo "$tt2" | rev | cut -d'/' -f1 | rev | tr -d '"'`                     
                        t1=`printf "%s = aws_iam_role.%s.arn" $tt1 $trole`
                    fi


                    if [[ ${tt1} == "awslogs-group" ]];then 
                        cwl=`echo $tt2 | tr -d '"'`
                        cwln=${cwl//\//_}
                        t1=`printf "%s = aws_cloudwatch_log_group.%s.name" $tt1 $cwln`
                    fi
               
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"
            if [[ "$trarn" != "" ]];then
                ../../scripts/050-get-iam-roles.sh $trarn
            fi
            if [[ "$erarn" != "" ]];then
                ../../scripts/050-get-iam-roles.sh $erarn
            fi
            if [[ "$cwl" != "" ]];then
                ../../scripts/070-get-cw-log-grp.sh $cwl
            fi
            
        done
    fi
done

rm -f t*.txt


