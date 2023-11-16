#!/bin/bash
pref[0]="Subnets"
ttft="aws_subnet"
idfilt[0]="SubnetId"

if [[ $AWS2TF_PY -eq 2 ]]; then
    echo "$1"
    if [[ "$1" == "" ]]; then
        #echo "100 Python $ttft with id $1"
        ../../.python/aws2tf.py -t $ttft -r $AWS2TF_REGION -m True
    else
        #echo "100 Python $ttft"
        ../../.python/aws2tf.py -t $ttft -r $AWS2TF_REGION -i $1 -m True
    fi
    exit
fi

if [ "$1" != "" ]; then
    if [[ "$1" == "vpc-"* ]]; then
        cmd[0]="$AWS ec2 describe-subnets --filters \"Name=vpc-id,Values=$1\"" 
    else
        ## fast out:
        fn=$(printf "%s__%s.tf" $ttft $1)
        if [ -f "$fn" ]; then exit; fi
        cmd[0]="$AWS ec2 describe-subnets --subnet-ids $1"
    fi
else
    cmd[0]="$AWS ec2 describe-subnets"
fi


ncpu=$(getconf _NPROCESSORS_ONLN)
ncpu=`expr $ncpu \* 2`


#rm -f ${tft[0]}.tf

for c in `seq 0 0`; do
    
    cm=${cmd[$c]}
	#echo $cm
    awsout=`eval $cm 2> /dev/null`
    if [ "$awsout" == "" ];then
        echo "$cm : You don't have access for this resource"
        if [ "$1" != "" ]; then
            exit 199
        else
            exit
        fi
    fi
    count=`echo $awsout | jq ".${pref[(${c})]} | length"`
    if [ "$count" -gt "0" ]; then
        count=`expr $count - 1`
        for i in `seq 0 $count`; do
            #echo $i
            cname=$(echo $awsout | jq -r ".${pref[(${c})]}[(${i})].${idfilt[(${c})]}")
            rname=${cname//:/_} && rname=${rname//./_} && rname=${rname//\//_}
            #echo "$ttft $cname import"
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi
            #echo "calling import sub"
            . ../../scripts/parallel_import3.sh $ttft $cname &
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
            echo "$ttft $cname tf files"
            fn=`printf "%s__%s.tf" $ttft $rname`
            if [ -f "$fn" ] ; then echo "$fn exists already skipping" && continue; fi

            file=`printf "%s-%s-1.txt" $ttft $rname`
            if [ ! -f "$file" ] ; then echo "$file does not exist skipping" && continue; fi
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
                    if [[ ${tt1} == "ipv6_cidr_block_association_id" ]];then skip=1;fi
                    if [[ ${tt1} == "map_customer_owned_ip_on_launch" ]];then skip=1;fi
                    #if [[ ${tt1} == "availability_zone" ]];then skip=1;fi
                    if [[ ${tt1} == "availability_zone_id" ]];then skip=1;fi
                    if [[ ${tt1} == "vpc_id" ]]; then
                        vpcid=`echo $tt2 | tr -d '"'`
                        t1=`printf "%s = aws_vpc.%s.id" $tt1 $vpcid`
                    fi
                    if [[ ${tt1} == "enable_lni_at_device_index" ]]; then
                        lni=`echo $tt2 | tr -d '"'`
                        if [[ "$lni" == "0" ]]; then
                             skip=1
                        fi
                   
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
            # route tables
            ../../scripts/140-get-route-table.sh $cname
            ../../scripts/141-get-route-table-associations.sh $cname


            dfn=`printf "data/data_%s__%s.tf" $ttft $rname`
            printf "data \"%s\" \"%s\" {\n" $ttft $rname > $dfn
            printf "id = \"%s\"\n" "$cname" >> $dfn
            printf "}\n" >> $dfn
            
        done
    fi
done # for c
../../scripts/parallel_statemv.sh $ttft
#rm -f $ttft-$rname-1.txt
rm -f *.backup 
rm -f $ttft*.txt
exit 0

