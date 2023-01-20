#!/bin/bash
if [ "$1" != "" ]; then
    if [[ "$1" == "vpc-"* ]]; then
        cmd[0]="$AWS ec2 describe-security-groups --filters \"Name=vpc-id,Values=$1\"" 
    else
        cmd[0]="$AWS ec2 describe-security-groups --group-ids $1" 
    fi
else
    cmd[0]="$AWS ec2 describe-security-groups"
fi
c=0
pref[0]="SecurityGroups"
tft[0]="aws_security_group"
idfilt[0]="GroupId"
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
    #echo "count=$count"
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")
            sgname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].GroupName")
            sgvpcid=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].VpcId")
            echo "$ttft $cname import"
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then  
                if [[ "$1" == "sg-"* ]]; then
                    echo "$fn exists already exit ..."
                    exit
                else
                    echo "$fn exists already skipping ..."
                    continue
                fi 
            fi


            if [[ $sgname == "default" ]];then
                echo "is default data..."
                echo "${sgname}:${cname}:${sgvpcid}" >> data/def-sgs.dat
                printf "data \"%s\" \"%s\" {\n" $ttft $rname > data-$fn
                printf "name = \"%s\"\n" $sgname >> data-$fn
                printf "vpc_id = aws_vpc.%s.id\n" $sgvpcid >> data-$fn
                printf "}\n" >> data-$fn
                
                
            fi
           
            #echo "calling import sub"
            . ../../scripts/parallel_import2.sh $ttft $cname &
            jc=`jobs -r | wc -l | tr -d ' '`
            while [ $jc -gt $ncpu ];do
                echo "Throttling - $jc Terraform imports in progress"
                sleep 10
                jc=`jobs -r | wc -l | tr -d ' '`
            done
        
        done

        jc=`jobs -r | wc -l | tr -d ' '`
        echo "Waiting for $jc Terraform imports"
        wait
        echo "Finished importing"
        ../../scripts/parallel_statemv.sh $ttft


        # tf files
        for i in `seq 0 $count`; do
            #echo $i
            cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")
            sgname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].GroupName")
            echo "$ttft $cname"
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ]; then echo "$fn exists continuing .." && continue; fi
            #if [[ $sgname == "default" ]];then echo "is default continue..." ; fi
            
            file=`printf "%s-%s-1.txt" $ttft $rname`
            if [ ! -f "$file" ] ; then echo "$file does not exist skipping" && continue; fi
            echo "Generating $fn"
            echo $aws2tfmess > $fn
            while IFS= read line
            do
				skip=0
                # display $line or do something with $line
                t1=`echo "$line"` 
                if [[ ${t1} == *"="* ]]; then
                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                    tt2=`echo "$line" | cut -f2- -d'='`
                    if [[ ${tt1} == "arn" ]];then skip=1; fi                
                    if [[ ${tt1} == "id" ]];then skip=1; fi          
                    if [[ ${tt1} == "role_arn" ]];then skip=1;fi
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    if [[ ${tt1} == "ipv6_cidr_block_association_id" ]];then skip=1;fi
                    #if [[ ${tt1} == "availability_zone" ]];then skip=1;fi
                    if [[ ${tt1} == "availability_zone_id" ]];then skip=1;fi
                    if [[ ${tt1} == "vpc_id" ]]; then
                        vpcid=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_vpc.%s.id" $tt1 $vpcid`
                    fi

                    ### rules must be seperated out to aws_default_security_group
                    if [[ ${tt1} == "ingress" ]];then 
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

                    ### rules must be seperated out to aws_default_security_group
                    if [[ ${tt1} == "egress" ]];then 
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

                # else
                    #
                fi
                if [[ "$skip" == "0" ]]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"


            if [[ "$vpcid" != "" ]]; then
                ../../scripts/100-get-vpc.sh $vpcid
            fi

        done # for i

        for i in `seq 0 $count`; do
            #echo $i
            cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")
            sgname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].GroupName")      

            ../../scripts/get-sg-rules.sh $cname ingress
            ../../scripts/get-sg-rules.sh $cname egress         
        done # for i
    fi
done  # for c




rm -f *.backup 


