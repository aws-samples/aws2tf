#!/bin/bash
if [ "$1" != "" ]; then
        cmd[0]="$AWS cloudfront get-distribution --id $1"
        pref[0]="Distribution"
else
    cmd[0]="$AWS cloudfront list-distributions"
    pref[0]="DistributionList.Items"
fi

pref[0]="DistributionList.Items"
tft[0]="aws_cloudfront_distribution"
idfilt[0]="Id"
ncpu=$(getconf _NPROCESSORS_ONLN)
ncpu=`expr $ncpu - 1`
#rm -f ${tft[0]}.tf

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
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            if [ "$1" != "" ]; then
                cname=$(echo $awsout | jq -r ".${pref[(${c})]}")
            else
                cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")
            fi
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            echo "$ttft $cname import"
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi
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
            if [ ! -f "$file" ] ; then echo "$file does not exist skipping" && continue; fi
            echo $aws2tfmess > $fn
            allowdn=0
            while IFS= read line
            do
				skip=0
                # display $line or do something with $line
                t1=`echo "$line"` 
                if [[ ${t1} == *origin* ]];then allowdn=1; fi
                if [[ ${t1} == *"="* ]];then
                    tt1=`echo "$line" | cut -f1 -d'=' | tr -d ' '` 
                    tt2=`echo "$line" | cut -f2- -d'='`
                    if [[ ${tt1} == "arn" ]];then skip=1; fi                
                    if [[ ${tt1} == "id" ]];then skip=1; fi          
                    if [[ ${tt1} == "role_arn" ]];then skip=1;fi
                    if [[ ${tt1} == "owner_id" ]];then skip=1;fi
                    if [[ ${tt1} == "caller_reference" ]];then skip=1;fi
                    if [[ ${tt1} == "hosted_zone_id" ]];then skip=1;fi
                    if [[ ${tt1} == "in_progress_validation_batches" ]];then skip=1;fi
                    if [[ ${tt1} == "status" ]];then skip=1; fi
                    if [[ ${tt1} == "last_modified_time" ]];then skip=1; fi                   
                    if [[ ${tt1} == "caller_reference" ]];then skip=1; fi
                    if [[ ${tt1} == "domain_name" ]];then 
                        if [[ $allowdn == "0" ]]; then  
                            skip=1
                        else
                            skip=0
                        fi
                    fi
                    if [[ ${tt1} == "etag" ]];then skip=1;fi
                    if [[ ${tt1} == "map_customer_owned_ip_on_launch" ]];then skip=1;fi


                    if [[ ${tt1} == "trusted_signers" ]];then 
                        tt2=`echo $tt2 | tr -d '"'` 
                        skip=1
                        while [ "$t1" != "]" ] && [ "$tt2" != "[]" ] ;do
                            read line
                            t1=`echo "$line"`
                            #echo $t1
                        done
                    fi
                    if [[ ${tt1} == "trusted_key_groups" ]];then 
                        tt2=`echo $tt2 | tr -d '"'` 
                        skip=1
                        while [ "$t1" != "]" ] && [ "$tt2" != "[]" ] ;do
                            read line
                            t1=`echo "$line"`
                            #echo $t1
                        done

                    fi



                # else
                    #
                fi
                if [ "$skip" == "0" ]; then
                    #echo $skip $t1
                    echo "$t1" >> $fn
                fi
                
            done <"$file"

            if [ "$vpcid" != "" ]; then
                #echo "subnet vpc call with vpcid=$vpcid"
                ../../scripts/100-get-vpc.sh $vpcid
            fi


            dfn=`printf "data/data_%s__%s.tf" $ttft $rname`
            printf "data \"%s\" \"%s\" {\n" $ttft $rname > $dfn
            printf "id = \"%s\"\n" "$cname" >> $dfn
            printf "}\n" >> $dfn
            
        done
    fi
done


rm -f *.backup 


