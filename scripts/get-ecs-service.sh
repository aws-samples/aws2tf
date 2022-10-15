#!/bin/bash
mysub=`echo $AWS2TF_ACCOUNT`
myreg=`echo $AWS2TF_REGION`
if [[ "$1" != "" ]]; then
    if [[ "$1" == *":"* ]]; then
        #echo "## process arn"
        cln=$(echo $1 | rev | cut -f2 -d "/" | rev | tr -d '"')
        srv=$(echo $1 | rev | cut -f1 -d "/" | rev | tr -d '"')
        cmd[0]="$AWS ecs describe-services --cluster $cln --services $srv"
        pref[0]="services"
        idfilt[0]="serviceArn"
    else
        cln=$(echo $1)
        cmd[0]="$AWS ecs list-services --cluster $cln"
        pref[0]="serviceArns" 
        idfilt[0]=""
    fi
else
    echo "Must provide a cluster name or arn - exiting ..."
    exit
fi

tft[0]="aws_ecs_service"

#rm -f ${tft[0]}.tf
echo "idfilt=${idfilt[0]}"
for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	ttft=${tft[(${c})]}
	#echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [[ "$awsout" == "" ]];then
        echo "$cm : You don't have access for this resource"
        exit
    fi
    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            if [[ ${idfilt[0]} == "" ]]; then
                arn=`echo $awsout | jq ".${pref[(${c})]}[(${i})]" | tr -d '"'`
                srv=$(echo $arn | rev | cut -f1 -d "/" | rev | tr -d '"')
            else
                arn=`echo $awsout | jq ".${pref[(${c})]}[(${i})].serviceArn" | tr -d '"'`
            fi
            #echo "ARN = $arn"

            cname=$(echo $srv)
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}

            echo "cname=$cname cln=$cln"
            fn=`printf "%s__%s__%s.tf" $ttft $cln $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi
            printf "resource \"%s\" \"%s__%s\" {\n" $ttft $cln $rname > $fn
            printf "}"  >> $fn
            #echo "terraform import $ttft.$rname $1/$cname"
            terraform import ${ttft}.${cln}__${rname} "${cln}/${cname}" | grep Import
            terraform state show -no-color ${ttft}.${cln}__${rname} > t1.txt
            
            rm -f $fn 
            sgs=()
            subs=()
           
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
                    if [[ ${tt1} == "propagate_tags" ]];then 
                        tt2=`echo $tt2 | tr -d '"'`
                        if [[ "$tt2" == "NONE" ]];then
                            skip=1
                        fi
                    fi
                    #if [[ ${tt1} == "availability_zone" ]];then skip=1;fi
                    if [[ ${tt1} == "availability_zone_id" ]];then skip=1;fi
                    if [[ ${tt1} == "state" ]];then skip=1;fi
                    if [[ ${tt1} == "dns_entry" ]];then skip=1;fi

                    if [[ ${tt1} == "requester_managed" ]];then skip=1;fi
                    if [[ ${tt1} == "revision" ]];then skip=1;fi
                    if [[ ${tt1} == "cidr_blocks" ]];then
                        echo "matched cidr"  
                        skip=1
                        while [[ "$t1" != "]" ]] ;do
                            read line
                            t1=`echo "$line"`
                            echo $t1
                        done
                    fi
                    if [[ ${tt1} == "network_interface_ids" ]];then skip=1;fi
                    if [[ ${tt1} == "vpc_id" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_vpc.%s.id" $tt1 $tt2`
                    fi
                    if [[ ${tt1} == "cluster" ]]; then
                        tt2=`echo $tt2 | tr -d '"'`
                        if [[ "$tt2" == *":cluster/"* ]];then
                            clnam=$(echo $tt2 | rev | cut -f1 -d'/' | rev)
                            t1=`printf "%s = aws_ecs_cluster.%s.arn" $tt1 $clnam`
                        fi
                    fi



                else
                    if [[ "$t1" == *"subnet-"* ]]; then
                        t1=`echo $t1 | tr -d '"|,'`
                        subs+=`printf "\"%s\" " $t1`
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

            echo "get hostzone id for $cln $srv"
            comm=`printf "$AWS ecs describe-services --services %s --cluster %s | jq '.services[].serviceRegistries[0].registryArn' | tr -d '\"'" $srv $cln`
            srvid=`eval $comm`
            srvid=`echo $srvid | cut -f2 -d'/'`

            echo "srvid = $srvid"
            if [ "$srv" != "null" ]; then
                    nsid=`$AWS servicediscovery get-service --id $srvid | jq .Service.NamespaceId | tr -d '\"'`
                    echo $nsid
                    # get zone id
                    hzid=`$AWS servicediscovery get-namespace --id $nsid | jq .Namespace.Properties.DnsProperties.HostedZoneId | tr -d '"'`
                    ../../scripts/get-priv-hzn.sh $hzid
            fi

                # get cluster if needed
            cfn=`printf "%s__%s.tf" $ttft $cln`
            if [ -f "$cfn" ] ; then 
                    echo "$cfn exists already skipping" 
            else
                    ../../scripts/350-get-ecs-cluster.sh $cln
            fi

            for sub in ${subs[@]}; do
                #echo "therole=$therole"
                sub1=`echo $sub | tr -d '"'`
                if [ "$sub1" != "" ]; then
                    ../../scripts/105-get-subnet.sh $sub1
                fi
            done

            for sg in ${sgs[@]}; do
                sg1=`echo $sg | tr -d '"'`
                if [ "$sg1" != "" ]; then
                    ../../scripts/110-get-security-group.sh $sg1
                fi
            done


        done # i
    fi
done

rm -f t*.txt

